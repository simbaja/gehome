# Library Logging Standards

Because `gehomesdk` is a reusable Python library (primarily embedded in Home Assistant), it **MUST** use Python's standard `logging` module and let the host application control formatting, handlers, and log levels.

---

## 1. Core Rules

* **Module Logger:** Every module that logs MUST define `_LOGGER = logging.getLogger(__name__)` at module scope.
* **Never Configure Root Logging in Library Code:** Do not call `logging.basicConfig()` or attach handlers inside `gehomesdk/` (only CLI entry points such as `gather_data.py` or `examples/` may configure logging).
* **Use Lazy `%s` Formatting:** Pass arguments separately to `_LOGGER` calls so string interpolation is skipped when the log level is disabled.

### Correct

```python
_LOGGER.debug("Unknown ERD Code '%s' and value '%s'", erd_code, erd_value)
```

### Avoid (Eager f-strings in hot paths)

```python
_LOGGER.debug(f"Unknown ERD Code '{erd_code}' and value '{erd_value}'")
```

---

## 2. Log Level Semantics

| Level | When to Use | Examples |
| :--- | :--- | :--- |
| `DEBUG` | High-frequency wire frames, raw ERD updates, unknown ERD codes, token refresh steps | Raw incoming/outgoing ERD payloads |
| `INFO` | Lifecycle transitions and appliance availability | Client connected, appliance marked available |
| `WARNING` | Recoverable anomalies, reconnect retries, appliance unavailable, unexpected non-fatal payloads | Connection lost (retrying), unknown enum fallback |
| `ERROR` | Failed ERD decode/encode, unrecoverable protocol errors, failed event handler callbacks | `ValueError` decoding registered ERD |

---

## 3. Credential & PII Redaction (Non-Negotiable)

**Never log:**
* Account passwords
* OAuth2 `access_token`, `refresh_token`, or authorization codes
* `Authorization` headers, cookies, or MFA verification codes
* Full raw auth response bodies that may contain tokens

When logging auth failures, log only the HTTP status code, endpoint stage, or sanitized error type—never the secret payload.
