# T16 — CI/CD Pipeline and Test Suite

**Phase:** 4 — Hardening  
**Priority:** P1 — High  
**Effort:** 1–2 weeks  
**Depends on:** T01 (pipeline code committed — first tests are data integrity tests)  
**Status:** Not started

---

## Context

There are currently zero tests and no CI/CD pipeline. The first tests to write are **data integrity tests** — they validate the existing JSON and OKF files without requiring any application code. These can be written as soon as T01 (commit pipeline) is done.

---

## Tasks

### 16.1 Set up GitHub Actions workflow

Create `.github/workflows/ci.yml`:

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: python -m pytest tests/ -v
      - run: python scripts/lint_okf.py
      - run: python scripts/check_sha256_integrity.py
```

### 16.2 Write OKF frontmatter linter test

```python
# tests/test_okf_compliance.py
import pytest
from pathlib import Path
import yaml

OKF_DIR = Path("OKF_bundle/Technical")
REQUIRED_FIELDS = ["type", "title", "description", "status", "generated", "verified"]
VALID_STATUS = {"draft", "stable", "deprecated"}

def get_all_concept_files():
    return [f for f in OKF_DIR.rglob("*.md") if f.name not in ("index.md", "log.md")]

@pytest.mark.parametrize("md_file", get_all_concept_files())
def test_okf_required_fields(md_file):
    content = md_file.read_text()
    parts = content.split("---", 2)
    assert len(parts) >= 3, f"{md_file}: no YAML frontmatter found"
    fm = yaml.safe_load(parts[1])
    for field in REQUIRED_FIELDS:
        assert field in fm, f"{md_file}: missing required field '{field}'"

@pytest.mark.parametrize("md_file", get_all_concept_files())
def test_okf_valid_status(md_file):
    fm = load_frontmatter(md_file)
    assert fm["status"] in VALID_STATUS, f"{md_file}: invalid status '{fm['status']}'"

def test_bundle_root_index_exists():
    assert (OKF_DIR / "index.md").exists()

def test_bundle_root_index_has_okf_version():
    fm = load_frontmatter(OKF_DIR / "index.md")
    assert fm.get("okf_version") == "0.2"
```

### 16.3 Write JSON schema integrity tests

```python
# tests/test_json_integrity.py

def test_all_json_have_source_sha256():
    for json_file in Path("parsed_json").rglob("*.json"):
        data = json.loads(json_file.read_text())
        assert "source_sha256" in data, f"{json_file}: missing source_sha256"

def test_sha256_matches_source_pdf():
    """Verify that source PDFs match their recorded SHA-256 hashes."""
    sha_map = {
        "74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c":
            "BMRCL_TenderData/Tender_Documents/Vol1DLNP1.pdf",
        "e44cc4945aec704af8350cca6388b3fe3b741d76577f7da70cee6a836662582b":
            "BMRCL_TenderData/Tender_Documents/Vol2DLNP1.pdf",
    }
    for expected_hash, pdf_path in sha_map.items():
        actual = compute_sha256(pdf_path)
        assert actual == expected_hash, f"SHA-256 mismatch for {pdf_path}"

def test_no_pending_review_in_chunk_manifest():
    """After Phase 1 review, no JSON should remain pending."""
    for json_file in Path("parsed_json").rglob("*.json"):
        data = json.loads(json_file.read_text())
        assert data.get("review_status") != "pending_manual_review", \
            f"{json_file}: still pending review — cannot be embedded"
```

### 16.4 Write chunker regression tests

After Phase 2, snapshot the chunk manifest and add a regression test:

```python
def test_chunk_count_regression():
    """Chunk count must not change unless intentionally updated."""
    manifest = json.loads(Path("parsed_json/chunk_manifest.json").read_text())
    EXPECTED_CHUNK_COUNT = 342  # update this when intentionally adding/removing chunks
    assert manifest["total_chunks"] == EXPECTED_CHUNK_COUNT
```

### 16.5 Write retrieval smoke test (post-Phase 2)

```python
def test_retrieval_smoke():
    """Basic smoke test: retrieval returns results for a known query."""
    results = retrieve("What is the EMD amount?", ...)
    assert len(results) > 0
    assert any("nit" in r.chunk.chunk_id for r in results)
```

---

## Acceptance Criteria

- [ ] GitHub Actions CI passes on every push to `main`
- [ ] OKF linter test catches a file with `status: source-derived` (negative test)
- [ ] SHA-256 integrity test passes for all current source PDFs
- [ ] All tests run in under 2 minutes on CI
- [ ] Test coverage report generated and stored as CI artifact
