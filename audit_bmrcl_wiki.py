"""Offline BMRCL wiki audit.

Reads wiki, OKF and parsed JSON.
Writes reports only under output/wiki_audit/.
Does not call Gemini, edit wiki pages or perform Git operations.
"""

import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import re

from collections import defaultdict
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import unquote


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(text):
    return " ".join(re.findall(r"\w+", text.casefold()))


def load_ingestion_module(project):
    script = project / "ingest_wiki.py"

    if not script.is_file():
        raise ValueError(f"Missing ingestion script: {script}")

    spec = importlib.util.spec_from_file_location(
        "bmrcl_ingestion_for_audit",
        script,
    )

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def run_audit(project):
    q = load_ingestion_module(project)

    wiki = project / "wiki"
    schema = wiki / "SCHEMA.md"

    for directory in [
        wiki,
        project / "OKF_bundle",
        project / "parsed_json",
    ]:
        if not directory.is_dir():
            raise ValueError(f"Missing directory: {directory}")

    if not schema.is_file():
        raise ValueError("wiki/SCHEMA.md is missing.")

    protected = {
        path: file_hash(path)
        for directory in [
            wiki,
            project / "OKF_bundle",
            project / "parsed_json",
        ]
        for path in directory.rglob("*")
        if path.is_file()
    }

    errors = []
    findings = []
    pages = {}
    claims = []
    usage = defaultdict(list)

    def error(kind, location, detail):
        errors.append(
            {
                "kind": kind,
                "location": location,
                "detail": str(detail),
            }
        )

    def review(kind, location, detail):
        findings.append(
            {
                "kind": kind,
                "location": location,
                "detail": str(detail),
            }
        )

    # Read saved wiki claims and citations.
    for path in sorted(wiki.rglob("*.md")):
        relative = path.relative_to(project).as_posix()

        try:
            metadata, body, _ = q.metadata(
                path.read_text(encoding="utf-8-sig")
            )

            pages[relative] = {
                "metadata": metadata,
                "body": body,
            }

            for claim in metadata.get("claims", []):
                location = (
                    relative
                    + "#"
                    + str(claim.get("id", "missing-id"))
                )

                claims.append((location, claim))

                ids = claim.get("evidence_ids", [])
                citations = claim.get("citations", [])
                citation_ids = [
                    citation.get("id")
                    for citation in citations
                ]

                if (
                    set(ids) != set(citation_ids)
                    or len(ids) != len(set(ids))
                    or len(citations) != len(ids)
                ):
                    error(
                        "citation_list",
                        location,
                        "Evidence IDs and saved citations disagree.",
                    )

                if claim.get("kind") in {
                    "summary",
                    "parameter",
                    "relation",
                }:
                    if not any(
                        identifier.startswith("J")
                        for identifier in ids
                    ):
                        error(
                            "missing_json_citation",
                            location,
                            ids,
                        )

                if claim.get("kind") == "relation":
                    start = claim.get("from_id")
                    end = claim.get("to_id")

                    if (
                        start not in ids
                        or end not in ids
                        or start == end
                    ):
                        error(
                            "relation_endpoints",
                            location,
                            "Endpoints must be distinct cited IDs.",
                        )

                for citation in citations:
                    usage[citation.get("id")].append(location)

        except Exception as exc:
            error("wiki_parse", relative, exc)

    # Rebuild evidence using the same loader as ingestion.
    source_paths = list(q.JSON_GROUPS)

    source_paths.extend(
        [
            "Technical/Vol3/vol3_appendices_instructions_forms.md",
            "Financial/vol4_secJ.md",
        ]
    )

    source_paths.extend(
        f"addendum_and_corrigendum/A_and_C{number}.md"
        for number in [1, 2, 3]
    )

    catalogue = {}
    source_ids = {}

    for relative in source_paths:
        full_path = "OKF_bundle/" + relative

        try:
            with contextlib.redirect_stdout(io.StringIO()):
                document, evidence = q.read_source(
                    project,
                    full_path,
                )

                _, json_evidence = q.read_matching_json(
                    project,
                    document,
                    evidence,
                )

            evidence.update(json_evidence)
            catalogue.update(evidence)
            source_ids[full_path] = set(evidence)

        except Exception as exc:
            error("source_load", full_path, exc)

    # Read batch completion markers.
    log_path = wiki / "log.md"

    log_text = (
        log_path.read_text(encoding="utf-8-sig")
        if log_path.is_file()
        else ""
    )

    checkpoints = []

    for raw in re.findall(
        r"<!-- wiki_batch_checkpoint (.*?) -->",
        log_text,
    ):
        try:
            checkpoints.append(json.loads(raw))
        except Exception as exc:
            error("checkpoint_parse", "wiki/log.md", exc)

    schema_hash = file_hash(schema)
    source_results = []

    for source, ids in source_ids.items():
        try:
            evidence = {
                identifier: catalogue[identifier]
                for identifier in catalogue
                if identifier in ids
            }

            batches = q.batch_plan(evidence, ids)

            with contextlib.redirect_stdout(io.StringIO()):
                amendment_paths = q.applicable_corrigenda(
                    project,
                    source,
                )

            amendment_ids = set()

            for path in amendment_paths:
                relative = path.relative_to(project).as_posix()

                amendment_ids.update(
                    source_ids.get(relative, set())
                )

            signature_input = {
                "version": q.BATCH_VERSION,
                "schema": schema_hash,
                "source": source,
                "batch_ids": [
                    [
                        evidence_record["id"]
                        for evidence_record in batch
                    ]
                    for batch in batches
                ],
                "amendment_ids": sorted(amendment_ids),
            }

            signature = q.sha(
                json.dumps(
                    signature_input,
                    sort_keys=True,
                ).encode()
            )

            completed = {
                marker["batch"]
                for marker in checkpoints
                if (
                    marker.get("signature") == signature
                    and isinstance(marker.get("batch"), int)
                )
            }

            expected = set(range(1, len(batches) + 1))
            valid_completed = completed & expected

            if completed - expected:
                error(
                    "checkpoint_range",
                    source,
                    sorted(completed - expected),
                )

            if valid_completed == expected:
                status = "checkpoints_complete"
            else:
                status = "incomplete_or_legacy"

            legacy_pattern = (
                r"- Selected source: `"
                + re.escape(source)
                + r"`\."
            )

            if (
                not valid_completed
                and re.search(legacy_pattern, log_text)
            ):
                status = (
                    "legacy_ingest_record_no_matching_checkpoints"
                )

            uncited = sorted(ids - set(usage))

            source_results.append(
                {
                    "source": source,
                    "batch_status": status,
                    "saved_batches": len(valid_completed),
                    "planned_batches": len(batches),
                    "evidence_units": len(ids),
                    "cited_units": len(ids) - len(uncited),
                    "uncited": [
                        {
                            "id": identifier,
                            "heading": catalogue[identifier]["heading"],
                            "json_pointer": catalogue[identifier].get(
                                "json_pointer"
                            ),
                        }
                        for identifier in uncited
                    ],
                }
            )

            if status != "checkpoints_complete":
                review(
                    "batch_status",
                    source,
                    status
                    + ". Inspect historical logs and source/schema "
                    "versions before deciding whether to rerun.",
                )

            if uncited:
                review(
                    "citation_coverage",
                    source,
                    f"{len(uncited)} evidence units have no saved "
                    "claim citation. These may be context, duplicates "
                    "or genuine knowledge gaps.",
                )

        except Exception as exc:
            error("batch_plan", source, exc)

    # Compare saved citations with freshly loaded evidence.
    for location, claim in claims:
        for citation in claim.get("citations", []):
            identifier = citation.get("id")

            if identifier not in catalogue:
                error(
                    "unknown_or_stale_evidence",
                    location,
                    identifier,
                )

            elif catalogue[identifier] != citation:
                error(
                    "changed_citation_payload",
                    location,
                    identifier,
                )

    # Check wiki body links. Supporting quoted passages are excluded.
    for relative, page in pages.items():
        body = page["body"].split("<details>", 1)[0]

        # Code spans/fences illustrate syntax; they are not live link destinations.
        live_lines = []
        fence_char = None
        fence_length = 0
        for line in body.splitlines():
            match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
            if fence_char is not None:
                if match and match[1][0] == fence_char and len(match[1]) >= fence_length and not match[2].strip():
                    fence_char = None
                continue
            if match:
                fence_char = match[1][0]
                fence_length = len(match[1])
                continue
            live_lines.append(line)
        body = "\n".join(live_lines)
        body = re.sub(r"(`+)(?!`)(.*?)\1(?!`)", "", body, flags=re.DOTALL)


        for link in re.findall(r"\[\[([^\]]+)\]\]", body):
            destination = link.split("|", 1)[0]
            target_name, _, heading = destination.partition("#")

            if not target_name.endswith(".md"):
                target_name += ".md"

            candidates = [
                project / target_name,
                project / "OKF_bundle" / target_name,
                (project / relative).parent / target_name,
            ]

            matches = [
                candidate
                for candidate in candidates
                if (
                    candidate.is_file()
                    and candidate.resolve().is_relative_to(project)
                )
            ]

            if not matches:
                error("broken_wikilink", relative, link)
                continue

            target_text = matches[0].read_text(
                encoding="utf-8-sig"
            )

            headings = re.findall(
                r"^#{1,6}\s+(.+?)\s*$",
                target_text,
                re.MULTILINE,
            )

            if heading and heading not in headings:
                error("missing_heading", relative, link)

        for destination in re.findall(
            r"(?<!!)\[[^\]]*\]\(([^)]+)\)",
            body,
        ):
            if re.match(
                r"\w+://|mailto:",
                destination,
            ):
                continue

            filename = unquote(
                destination.split("#", 1)[0]
            )

            if not filename:
                continue

            target = (
                project / relative
            ).parent / filename

            if (
                not target.resolve().is_relative_to(project)
                or not target.is_file()
            ):
                error(
                    "broken_markdown_link",
                    relative,
                    destination,
                )

    # Exact duplicate text; duplication across hubs may be intentional.
    text_groups = defaultdict(list)

    for location, claim in claims:
        text_groups[
            normalized(claim.get("text", ""))
        ].append(location)

    exact_duplicates = [
        locations
        for text, locations in text_groups.items()
        if text and len(locations) > 1
    ]

    # Similar text sharing evidence is only a review candidate.
    similar_pairs = []

    prepared_claims = [
        (
            location,
            claim,
            normalized(claim.get("text", "")),
        )
        for location, claim in claims
    ]

    for index, (location, first, first_text) in enumerate(
        prepared_claims
    ):
        for other_location, second, second_text in (
            prepared_claims[index + 1:]
        ):
            if not first_text or first_text == second_text:
                continue

            shared_ids = (
                set(first.get("evidence_ids", []))
                & set(second.get("evidence_ids", []))
            )

            if not shared_ids:
                continue

            longest = max(len(first_text), len(second_text))

            if (
                abs(len(first_text) - len(second_text))
                > longest * 0.25
            ):
                continue

            similarity = SequenceMatcher(
                None,
                first_text,
                second_text,
                autojunk=False,
            ).ratio()

            if similarity >= 0.88:
                similar_pairs.append(
                    {
                        "first": location,
                        "second": other_location,
                        "similarity": round(similarity, 3),
                        "first_text": first["text"],
                        "second_text": second["text"],
                    }
                )

    # Put amendment source records beside the claims citing them.
    # This does not decide legal precedence or supersession.
    amendment_results = []

    amendment_file = (
        project
        / "parsed_json"
        / "addendum_corrigendum"
        / "corrigenda_amendments.json"
    )

    if amendment_file.is_file():
        amendment_data = json.loads(
            amendment_file.read_text(encoding="utf-8-sig")
        )

        amendment_relative = amendment_file.relative_to(
            project
        ).as_posix()

        for index, record in enumerate(
            amendment_data.get("amendments", [])
        ):
            pointer = f"/amendments/{index}"

            evidence_ids = {
                identifier
                for identifier, evidence in catalogue.items()
                if (
                    evidence.get("json_path")
                    == amendment_relative
                    and evidence.get("json_pointer") == pointer
                )
            }

            linked_locations = {
                location
                for identifier in evidence_ids
                for location in usage.get(identifier, [])
            }

            linked_claims = [
                {
                    "location": location,
                    "text": claim["text"],
                }
                for location, claim in claims
                if location in linked_locations
            ]

            amendment_results.append(
                {
                    "source_record": record,
                    "linked_claims": linked_claims,
                    "status": (
                        "cited_meaning_and_supersession_pending"
                        if linked_claims
                        else "uncited_review_required"
                    ),
                }
            )

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project": str(project),
        "wiki_page_count": len(pages),
        "claim_count": len(claims),
        "errors": errors,
        "review_findings": findings,
        "sources": source_results,
        "exact_duplicate_groups": exact_duplicates,
        "possible_duplicates": similar_pairs,
        "amendments": amendment_results,
        "open_review_questions": [
            {
                "location": location,
                "text": claim["text"],
            }
            for location, claim in claims
            if claim.get("kind") == "review_question"
        ],
        "limitations": [
            "Citation coverage does not establish complete meaning.",
            "Similar-text detection is not semantic contradiction detection.",
            "Repeated claims across hubs may be intentional.",
            "Amendment citation does not prove correct supersession.",
            "Original PDFs were not independently reviewed.",
            "No compliance or legal applicability decision is made.",
        ],
    }

    # Confirm input files were not changed during the audit.
    for path, original_hash in protected.items():
        if not path.is_file() or file_hash(path) != original_hash:
            raise RuntimeError(
                f"Protected input changed during audit: {path}. "
                "Reports were not saved."
            )

    run_name = datetime.now(timezone.utc).strftime(
        "run_%Y%m%dT%H%M%S%fZ"
    )

    output = project / "output" / "wiki_audit" / run_name
    output.mkdir(parents=True, exist_ok=False)

    json_path = output / "audit.json"
    markdown_path = output / "audit.md"

    json_path.write_text(
        json.dumps(
            report,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    def table_text(value):
        return (
            str(value)
            .replace("|", "\\|")
            .replace("\n", " ")
        )

    lines = [
        "# BMRCL Wiki Audit",
        "",
        "Automated structure, provenance and review-candidate checks.",
        "This report does not approve semantic accuracy, applicability "
        "or complete amendment supersession.",
        "",
        f"- Wiki Markdown pages: {len(pages)}",
        f"- Structured claims/findings: {len(claims)}",
        f"- Structural/provenance errors: {len(errors)}",
        f"- Review flags: {len(findings)}",
        "",
        "## Batch and Citation Coverage",
        "",
        "Citation counts measure evidence-unit usage, not complete "
        "or correct interpretation. Section A may have a legacy "
        "ingestion record without matching batch checkpoints.",
        "",
        "| Source | Batch status | Saved/planned | Cited/evidence |",
        "|---|---|---|---|",
    ]

    for result in source_results:
        lines.append(
            f"| {table_text(result['source'])} "
            f"| {result['batch_status']} "
            f"| {result['saved_batches']}/"
            f"{result['planned_batches']} "
            f"| {result['cited_units']}/"
            f"{result['evidence_units']} |"
        )

    lines.extend(["", "## Errors", ""])

    if errors:
        for item in errors:
            lines.append(
                f"- **{item['kind']}** — "
                f"`{item['location']}`: {item['detail']}"
            )
    else:
        lines.append(
            "No errors detected by the implemented checks. "
            "This is not semantic approval."
        )

    lines.extend(["", "## Review Flags", ""])

    for item in findings:
        lines.append(
            f"- **{item['kind']}** — "
            f"`{item['location']}`: {item['detail']}"
        )

    lines.extend(
        [
            "",
            "## Duplicate Candidates",
            "",
            f"- Exact duplicate-text groups: {len(exact_duplicates)}",
            f"- Similar-text pairs sharing evidence: {len(similar_pairs)}",
            "",
            "See audit.json for the candidate locations. Repetition "
            "across hubs may be intentional. Nothing was deleted.",
            "",
            "## Amendment Comparison Queue",
            "",
            "Compare each source record with its linked claims. "
            "Confirm baseline, replacement, exact scope and whether "
            "earlier wiki statements remain clearly historical.",
            "",
        ]
    )

    for index, result in enumerate(amendment_results, start=1):
        lines.extend(
            [
                f"### Amendment Record {index}",
                "",
                "```json",
                json.dumps(
                    result["source_record"],
                    ensure_ascii=False,
                    indent=2,
                ),
                "```",
                "",
                f"Status: {result['status']}",
                "",
            ]
        )

        for claim in result["linked_claims"]:
            lines.append(
                f"- `{claim['location']}`: {claim['text']}"
            )

    lines.extend(
        [
            "",
            "## Required Human Review",
            "",
            "- Inspect uncited records in audit.json.",
            "- Distinguish contextual/duplicate evidence from real gaps.",
            "- Review duplicate candidates before merging anything.",
            "- Compare amendment wording with retained baseline claims.",
            "- Confirm exact deletion and replacement scope.",
            "- Review unresolved dates, durations and template conflicts.",
            "- Verify interpretations against original PDFs before approval.",
            "",
            "Only audit reports were written. Wiki, SCHEMA, OKF and "
            "parsed JSON were not modified. No API requests or Git "
            "operations were performed.",
        ]
    )

    markdown_path.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )

    print(f"Wiki Markdown pages: {len(pages)}")
    print(f"Structured claims/findings: {len(claims)}")
    print(f"Structural/provenance errors: {len(errors)}")
    print(f"Review flags: {len(findings)}")
    print(f"Exact duplicate-text groups: {len(exact_duplicates)}")
    print(f"Similar-text pairs: {len(similar_pairs)}")
    print(f"Amendment records: {len(amendment_results)}")
    print("Saved:", markdown_path)
    print("Saved:", json_path)
    print()
    print("Wiki, SCHEMA, OKF and JSON unchanged.")
    print("No API requests or Git operations.")
    print("Semantic accuracy and supersession require review.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "--project",
        type=Path,
        default=Path.cwd(),
    )

    arguments = parser.parse_args()

    try:
        run_audit(arguments.project.resolve())
    except Exception as exc:
        raise SystemExit(f"STOP: {exc}")