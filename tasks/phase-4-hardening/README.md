# Phase 4 — Production Hardening

**Goal:** A deployable, monitored, authenticated system with a CI/CD pipeline.  
**Can start:** CI/CD tests (T16) can begin as soon as Phase 1 is complete. Auth and monitoring should be designed in Phase 2 and implemented alongside Phase 3.

---

## Tasks in This Phase

| Task | Description | Effort |
|---|---|---|
| [T16](T16-cicd-test-suite.md) | GitHub Actions CI/CD and test suite | 1–2 weeks |
| [T17](T17-auth-rate-limiting.md) | JWT authentication and rate limiting | 1 week |
| [T18](T18-monitoring-observability.md) | Monitoring and observability | 3–5 days |

---

## Phase Exit Criteria

- [ ] CI passes on every PR (OKF lint + JSON schema + SHA-256 integrity + unit tests)
- [ ] All API endpoints require valid JWT
- [ ] Query latency, retrieval hit rate, and LLM token cost are logged
- [ ] Alerts fire on error rate > 1% or latency p95 > 5s
