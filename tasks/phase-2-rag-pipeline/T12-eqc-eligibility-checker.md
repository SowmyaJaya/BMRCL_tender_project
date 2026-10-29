# T12 — Build EQC Deterministic Eligibility Checker

**Phase:** 2 — RAG Pipeline  
**Priority:** P1 — High  
**Effort:** 3–5 days  
**Depends on:** T02 (eqc_criteria.json must be reviewed — financial thresholds must be verified)  
**Status:** Not started

---

## Context

The most valuable single feature for a bidder is: **"Does my company qualify to bid on this tender?"**

The EQC (Eligibility Qualification Criteria) in `parsed_json/vol1/section_c_eqc/eqc_criteria.json` contains machine-readable financial thresholds and experience requirements with IDs like `3.1.A.(i)`. This evaluation should be **deterministic** — not LLM-based. An LLM deciding eligibility is unpredictable and unauditable; a rule engine is reproducible and explainable.

The LLM is used only for the explanation layer: once the rule engine has determined pass/fail for each criterion, the LLM explains the result in plain language and lists the required evidence documents.

**This task has no RAG or vector store dependency.** It reads `eqc_criteria.json` directly and evaluates a company profile against its rules. It can be built and tested before the vector store is set up.

---

## Current EQC criteria (from reviewed JSON)

The key criteria for tender `DLN-P1/2026/157` (verify against reviewed JSON):

```
3.1.A.(i): ONE similar work ≥ ₹3.79 Crores in last 7 years
3.1.A.(ii): TWO similar works, each ≥ ₹2.37 Crores in last 7 years
[Either 3.1.A.(i) OR 3.1.A.(ii) must be satisfied — not both required]
[Additional criteria may exist — check full eqc_criteria.json]
```

---

## Tasks

### 12.1 Define the company profile input schema

```python
from pydantic import BaseModel
from datetime import date

class CompletedWork(BaseModel):
    description: str
    contract_value_inr_crores: float
    completion_date: date
    is_similar_nature: bool     # user declares this; checker verifies it's plausible
    client_name: str
    certificate_available: bool

class CompanyProfile(BaseModel):
    company_name: str
    entity_type: str            # "single_entity", "jv_member", "jv_lead"
    annual_turnover_inr_crores: float | None = None
    net_worth_inr_crores: float | None = None
    completed_works: list[CompletedWork]
    profile_date: date          # the reference date for "last 7 years"
```

---

### 12.2 Parse EQC criteria into rule objects

```python
from dataclasses import dataclass

@dataclass
class EQCRule:
    criterion_id: str           # "3.1.A.(i)"
    group_id: str               # "work_experience"
    description: str
    rule_type: str              # "min_single_work", "min_multiple_works", "min_turnover", etc.
    threshold_inr_crores: float | None
    min_number_of_works: int | None
    lookback_years: int         # 7 for this tender
    required_documents: list[str]

def load_eqc_rules(json_path: Path) -> list[EQCRule]:
    """Parses eqc_criteria.json into structured EQCRule objects."""
    ...
```

---

### 12.3 Build the rule engine

```python
@dataclass
class CriterionResult:
    criterion_id: str
    passed: bool
    reason: str                 # human-readable explanation
    matching_works: list[str]  # which company works satisfied this criterion
    missing: str | None        # what's missing if failed

def evaluate_criterion(rule: EQCRule, profile: CompanyProfile) -> CriterionResult:
    """Deterministic evaluation of one EQC criterion against a company profile."""
    cutoff_date = profile.profile_date.replace(year=profile.profile_date.year - rule.lookback_years)
    eligible_works = [
        w for w in profile.completed_works
        if w.completion_date >= cutoff_date and w.is_similar_nature
    ]
    
    if rule.rule_type == "min_single_work":
        qualifying = [w for w in eligible_works if w.contract_value_inr_crores >= rule.threshold_inr_crores]
        passed = len(qualifying) >= 1
        ...
    
    elif rule.rule_type == "min_multiple_works":
        qualifying = [w for w in eligible_works if w.contract_value_inr_crores >= rule.threshold_inr_crores]
        passed = len(qualifying) >= rule.min_number_of_works
        ...
    
    return CriterionResult(...)

def evaluate_eligibility(rules: list[EQCRule], profile: CompanyProfile) -> dict:
    """
    Evaluates all criteria. Returns overall pass/fail and per-criterion results.
    Handles OR-groups (3.1.A.(i) OR 3.1.A.(ii)).
    """
    results = [evaluate_criterion(r, profile) for r in rules]
    # Group by group_id and apply OR logic within groups
    ...
    return {
        "overall": "ELIGIBLE" | "NOT_ELIGIBLE" | "BORDERLINE",
        "criteria": results,
        "required_documents": [...],
    }
```

---

### 12.4 Add LLM explanation layer

Once the rule engine returns a result, pass it to the LLM for plain-language explanation:

```python
def explain_eligibility_result(result: dict, profile: CompanyProfile) -> str:
    """
    Uses the LLM to explain the eligibility result in plain language.
    The LLM does NOT make the eligibility decision — it only explains the rule engine's output.
    """
    prompt = f"""
    A company has been evaluated against BMRCL tender DLN-P1/2026/157 EQC criteria.
    
    Rule engine result: {json.dumps(result, indent=2)}
    Company profile summary: {profile.company_name}, {len(profile.completed_works)} completed works
    
    Explain this result clearly:
    1. Whether the company is eligible and why
    2. Which specific criteria passed/failed
    3. What documents they need to submit
    4. If borderline, what additional evidence might help
    
    Be specific about amounts (₹ values) and dates. Do not add information not in the result.
    """
    ...
```

---

### 12.5 Write tests

```python
def test_eligible_single_work():
    """Company with one ₹4.5Cr similar work passes 3.1.A.(i)."""
    profile = CompanyProfile(
        completed_works=[CompletedWork(contract_value_inr_crores=4.5, is_similar_nature=True, ...)]
    )
    result = evaluate_eligibility(rules, profile)
    assert result["overall"] == "ELIGIBLE"

def test_ineligible_insufficient_value():
    """Company with one ₹3.0Cr similar work (below ₹3.79Cr threshold) fails 3.1.A.(i)."""
    ...
    assert result["overall"] == "NOT_ELIGIBLE"

def test_eligible_two_works_alternate_path():
    """Company with two ₹2.5Cr works passes via 3.1.A.(ii)."""
    ...

def test_lookback_period_exclusion():
    """Work completed 8 years ago is excluded from consideration."""
    ...

def test_cutoff_date_uses_profile_date():
    """Lookback window is relative to profile_date, not today."""
    ...
```

---

## Acceptance Criteria

- [ ] Rule engine gives deterministic results (same input always produces same output)
- [ ] All 5 test cases pass
- [ ] Financial thresholds in the rule engine match the reviewed `eqc_criteria.json` exactly
- [ ] OR-group logic correctly handles alternative paths (3.1.A.(i) OR 3.1.A.(ii))
- [ ] Works older than 7 years from `profile_date` are excluded
- [ ] Output includes the list of required supporting documents for each satisfied criterion
- [ ] LLM explanation layer is clearly separated from the rule engine (LLM cannot override the rule engine's pass/fail)
