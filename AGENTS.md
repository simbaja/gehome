# AGENTS.md

Instructions for AI coding agents working in `gehomesdk`.

## Project Overview

`gehomesdk` is an asynchronous Python SDK (Python 3.13+) for GE WiFi-enabled (SmartHQ) appliances, primarily used to power Home Assistant integrations (such as `ge_home`) and the `gehome-appliance-data` CLI.

Core subsystems:
- `gehomesdk/clients/` — Async WebSocket/HTTP clients (`GeBaseClient`, `GeWebsocketClient`), OAuth2/MFA login flows (`GeSmartHqLogin`), client states, and event constants.
- `gehomesdk/ge_appliance.py` — `GeAppliance` data model, `WeakValueDictionary` instance cache, decoded and raw ERD property caches, and state-change dispatch.
- `gehomesdk/erd/` — ERD protocol definitions (`ErdCode`, `ErdCodeClass`, `ErdDataType`), typed value objects (`values/`), hex-to-Python converters (`converters/`), central registry (`erd_configuration.py`), and `ErdEncoder`.
- `gehomesdk/exception/` — `GeException` hierarchy for auth, MFA, request, and protocol errors.

## Commands

Run all commands from the repository root using the project virtual environment:

- **Run test suite:**
  ```powershell
  .venv\Scripts\python.exe -m pytest -q
  ```
- **Run a single test file:**
  ```powershell
  .venv\Scripts\python.exe -m pytest tests/test_raw_erd_value.py
  ```
- **Lint / check formatting (ruff):**
  ```powershell
  .venv\Scripts\python.exe -m ruff check gehomesdk tests
  ```

## Governance & Standards

All changes must adhere to the repository standards in `docs/standards/`:

- `docs/standards/00_meta_rules.md` — Core principles, security/credential hygiene, scratchpad rule, and feature workflows.
- `docs/standards/01_coding_style.md` — 3-group import sorting, naming, typing patterns, and forbidden constructs.
- `docs/standards/02_documentation.md` — Module docstrings, Tier 1/2/3 visual hierarchy, Google-style docstrings, and "why" comments.
- `docs/standards/03_testing.md` — Offline `pytest` rules, `asyncio.run(...)` patterns, converter matrix tests, and client/appliance testing.
- `docs/standards/04_architecture.md` — Client lifecycle, event callbacks, `GeAppliance` caching, and the ERD encode/decode pipeline.
- `docs/standards/05_logging.md` — Standard `_LOGGER = logging.getLogger(__name__)` usage, log levels, lazy formatting, and secret redaction.

## Priority of Thought

When designing or reviewing changes, apply the standards in this order:

1. **Meta-Rules (`00`)**: Is this async-safe, backwards-compatible for SDK consumers, and free of leaked secrets?
2. **Architecture (`04`)**: Does this fit the `clients/` / `ge_appliance.py` / `erd/` / `exception/` boundaries?
3. **Testing (`03`)**: How will this be verified offline with deterministic inputs and mocks?
4. **Logging (`05`)**: Are lifecycle events, protocol anomalies, and decode errors logged cleanly without PII or tokens?
5. **Coding Style (`01`)**: Are imports grouped, types annotated, and blocking calls avoided?
6. **Documentation (`02`)**: Are public APIs documented (Google style) and non-obvious invariants explained with "why" comments?

## Key Guardrails

- **Never log or commit secrets:** Never log passwords, OAuth2 `access_token` / `refresh_token` values, cookies, or authorization headers. Never commit `credentials.py`, `secrets.py`, or real account data.
- **No network calls in tests:** Unit tests must mock `aiohttp.ClientSession`, websockets, and `GeBaseClient` transport methods.
- **Async-only I/O:** Never use blocking calls (`time.sleep`, synchronous `requests` inside `async def`) on the event loop.
- **Preserve ERD compatibility:** Every new `ErdCode` that requires decoding/encoding must have a corresponding entry in `gehomesdk/erd/erd_configuration.py`, and `GeAppliance` must continue preserving raw hex payloads alongside decoded values.
- **Scratchpad rule:** Write any temporary scripts, payload dumps, or throwaway analysis to `.scratchpad/` (git-ignored), never to the repository root.
