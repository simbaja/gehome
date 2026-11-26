# Testing Standards

This document defines the reliability, isolation, and structure standards for the `gehomesdk` test suite.

These standards optimize for:

* **100% Offline Determinism:** Zero network calls or live SmartHQ credentials.
* **Protocol Fidelity:** Exact verification of hex encoding/decoding and edge cases.
* **Async Hygiene:** Clean event loop execution without leaked background tasks.

---

## 1. Test Runner & Async Execution

* **Runner:** `pytest` configured via `pytest.ini` (`testpaths = tests`, `python_files = test_*.py`).
* **Command:** `.venv\Scripts\python.exe -m pytest -q`
* **Async Tests:** Wrap async test coroutines with `asyncio.run(...)` (no `pytest-asyncio` plugin dependency is required by `requirements-dev.txt`).

```python
def test_example_async_behavior() -> None:
    async def _run() -> None:
        ...

    asyncio.run(_run())
```

---

## 2. File Naming & Scope

Place all tests under `tests/` using descriptive `test_<area>.py` names:

| Scope | Pattern | Examples |
| :--- | :--- | :--- |
| ERD Converters & Values | `tests/test_<appliance_or_feature>_converters.py` | `test_water_heater_converters.py` |
| Appliance Model | `tests/test_<feature>.py` | `test_raw_erd_value.py` |
| Client / Auth / Network | `tests/test_<client_area>.py` | `test_base_client_network_errors.py` |
| Packaging / Imports | `tests/test_imports.py`, `tests/test_readme_and_setup.py` | Existing smoke checks |
| Bug Regressions | `tests/test_regression_<issue_or_bug>.py` | Dedicated reproduction test |

---

## 3. Mandatory Offline Isolation

Tests MUST NOT:

* Open real TCP, HTTP, or WebSocket connections.
* Read `credentials.py`, `secrets.py`, or environment credentials.
* Call `time.sleep` or depend on wall-clock timing.

Mock `aiohttp.ClientSession`, `websockets`, or `GeBaseClient` transport methods using `unittest.mock` (`MagicMock`, `AsyncMock`, `patch`).

---

## 4. What Each Layer Must Test

### 4.1 ERD Converters & Values

Use `@pytest.mark.parametrize` matrices to cover:

* **Decode:** Valid hex strings -> expected enum, dataclass, int, bool, or namedtuple.
* **Encode:** Typed Python values -> expected uppercase/lowercase hex wire format (and round-trip `encode(decode(hex)) == hex` where applicable).
* **Boundary & Invalid Inputs:** Empty strings, unexpected lengths, unknown enum values, and `ValueError` handling.
* **Registration:** Verify new `ErdCode` entries resolve via `ErdEncoder().translate_code(...)` and `decode_value(...)`.

### 4.2 `GeAppliance` State & Events

* Decoded cache (`get_erd_value`) and raw cache (`get_raw_erd_value`) stay synchronized on updates.
* Unregistered hex codes preserve raw wire values without raising.
* Client priority replacement in `GeAppliance.__new__` and `WeakValueDictionary` caching behave deterministically.
* Availability transitions (`set_available`, `set_unavailable`, `initialized`) reflect accurately.

### 4.3 Clients & Authentication

* Refresh token success and rotation (`client.refresh_token` updated).
* Auth failure fallback vs network/timeout error propagation (network errors must NOT silently fall back to full login or wipe a valid refresh token).
* MFA/terms challenges raise `GeAuthMfaRequiredError` / `GeAuthTermsRequiredError` with expected metadata.
* Disconnect and cleanup cancel any scheduled tasks cleanly.

---

## 5. Anti-Patterns (Forbidden)

* ❌ Live network requests or real SmartHQ credentials in tests.
* ❌ `time.sleep(...)` or flaky timing-dependent assertions.
* ❌ Silencing converter exceptions without asserting the fallback or raised error.
* ❌ Duplicating large mock client classes across files when a small local helper or fixture suffices.

---

## 6. Definition of Done

A feature or fix is complete only when:

* [ ] New or modified behavior has deterministic unit tests in `tests/`.
* [ ] Edge cases (empty/malformed hex, network/timeout errors, auth errors) are covered.
* [ ] Full suite passes: `.venv\Scripts\python.exe -m pytest -q`.
* [ ] Lint check passes: `.venv\Scripts\python.exe -m ruff check gehomesdk tests`.
* [ ] Workspace type check passes: `pyright`.
