# T17 — Authentication and Rate Limiting

**Phase:** 4 — Hardening  
**Priority:** P2 — Medium  
**Effort:** 1 week  
**Depends on:** T13 (API endpoint exists)  
**Status:** Not started

---

## Context

Tender documents can be commercially sensitive — bidder organisations should not be able to see each other's query history. The API needs JWT authentication with per-organisation tenant isolation and rate limiting to prevent abuse of the LLM endpoint (each query costs money).

---

## Tasks

### 17.1 Implement JWT authentication middleware

```python
# src/bmrcl_api/auth.py
from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

SECRET_KEY = os.environ["JWT_SECRET_KEY"]
ALGORITHM = "HS256"

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload   # contains: sub (user_id), org_id, allowed_tenders
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

Apply to the query endpoint:

```python
@router.post("/query", response_model=QueryResponse)
async def query_tender(req: QueryRequest, token: dict = Depends(verify_token)):
    # Verify the user's org is allowed to query this tender
    if req.tender_id not in token.get("allowed_tenders", []):
        raise HTTPException(status_code=403, detail="Not authorised for this tender")
    ...
```

### 17.2 Implement per-organisation rate limiting

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=lambda request: request.state.token["org_id"])

@router.post("/query")
@limiter.limit("20/minute")   # 20 queries per minute per organisation
async def query_tender(request: Request, req: QueryRequest, token: dict = Depends(verify_token)):
    ...
```

### 17.3 Implement audit logging

Every query must be logged with: `org_id`, `user_id`, `question`, `tender_id`, `chunks_retrieved`, `timestamp`. This is a procurement compliance requirement — queries to a procurement AI system should be auditable.

```python
def log_query_audit(token: dict, req: QueryRequest, response: QueryResponse) -> None:
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "org_id": token["org_id"],
        "user_id": token["sub"],
        "tender_id": req.tender_id,
        "question": req.question,
        "chunks_retrieved": len(response.sources),
        "answer_length": len(response.answer),
    }
    # Append to audit log (write to DB in production)
    with open(f"audit_logs/{datetime.utcnow().date()}.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")
```

---

## Acceptance Criteria

- [ ] Request without a valid JWT returns 401
- [ ] Request with a valid JWT for a different tender returns 403
- [ ] More than 20 requests per minute from the same `org_id` returns 429
- [ ] Every successful query logged to audit log with `org_id`, `user_id`, `question`
- [ ] Audit logs are append-only (no delete endpoint)
