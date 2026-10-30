# T18 — Monitoring and Observability

**Phase:** 4 — Hardening  
**Priority:** P2 — Medium  
**Effort:** 3–5 days  
**Depends on:** T13 (API endpoint), T17 (audit logging in place)  
**Status:** Not started

---

## Context

A production RAG system has three cost/quality signals that need monitoring: query latency (user experience), retrieval quality (are the right clauses being returned?), and LLM token cost (financial).

---

## Tasks

### 18.1 Instrument query latency

The API already records `retrieval_time_ms` and `generation_time_ms` (T13). Add a Prometheus counter and histogram:

```python
from prometheus_client import Histogram, Counter

QUERY_LATENCY = Histogram("query_latency_ms", "End-to-end query latency", buckets=[100, 500, 1000, 2000, 5000])
QUERY_COUNT = Counter("query_total", "Total queries", ["tender_id", "status"])
LLM_TOKENS = Counter("llm_tokens_total", "LLM tokens used", ["type"])  # type: input | output
```

Expose metrics at `/metrics` (Prometheus scrape endpoint).

### 18.2 Track retrieval quality signal

For each query, log whether the user explicitly marked the answer as helpful (add a `POST /feedback` endpoint):

```python
class FeedbackRequest(BaseModel):
    query_id: str
    helpful: bool
    comment: str | None = None

@router.post("/feedback")
async def submit_feedback(req: FeedbackRequest):
    # Store in DB; used for retrieval quality tracking
    ...
```

Track the rolling 7-day helpfulness rate. Alert if it drops below 70%.

### 18.3 Track LLM cost per query

```python
def estimate_cost(input_tokens: int, output_tokens: int) -> float:
    # Claude claude-sonnet-4-6 pricing (verify current rates)
    INPUT_COST_PER_1M = 3.00
    OUTPUT_COST_PER_1M = 15.00
    return (input_tokens / 1_000_000) * INPUT_COST_PER_1M + (output_tokens / 1_000_000) * OUTPUT_COST_PER_1M
```

Log cost per query. Alert if daily cost exceeds a threshold.

### 18.4 Set up alerts

Define alert thresholds in `monitoring/alerts.yml`:

```yaml
alerts:
  - name: high_query_latency
    condition: p95_latency_ms > 5000
    message: "Query p95 latency exceeded 5 seconds"
  - name: high_error_rate
    condition: error_rate_1h > 0.01
    message: "Query error rate exceeded 1%"
  - name: low_helpfulness
    condition: helpfulness_7d < 0.70
    message: "7-day helpfulness rate below 70%"
  - name: daily_cost_exceeded
    condition: daily_llm_cost_usd > 50.00
    message: "Daily LLM cost exceeded $50"
```

### 18.5 Add a `/stats` endpoint

```python
@router.get("/stats")
async def system_stats():
    return {
        "total_queries_today": ...,
        "avg_latency_ms_today": ...,
        "chunks_indexed": ...,
        "unverified_chunk_percentage": ...,
        "stale_chunk_count": ...,
        "helpfulness_rate_7d": ...,
    }
```

---

## Acceptance Criteria

- [ ] `/metrics` endpoint returns Prometheus-format metrics
- [ ] Query latency histogram populated after each request
- [ ] LLM token cost logged per query
- [ ] `/feedback` endpoint stores user feedback
- [ ] `/stats` endpoint returns current system health
- [ ] Alerts defined for latency, error rate, helpfulness, and cost
