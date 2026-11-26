# Meta-Rules & Philosophy

These directives govern all development in `gehomesdk`. Deviation is considered a defect.

## 1. Primary Goals

1. **Library Reliability & Backwards Compatibility:** `gehomesdk` is consumed by downstream integrations (primarily Home Assistant's `ge_home`) and CLI tools. Public symbols, event names, and exception types must remain stable and predictable.
2. **Async-Safe, Non-Blocking Execution:** All network and protocol I/O in client paths must be `asyncio`-safe and never block the caller's event loop.
3. **Architectural & Stylistic Consistency:** New appliances, ERD codes, and client features must follow existing `erd/` and `clients/` patterns rather than inventing one-off abstractions.
4. **Protocol Resilience:** SmartHQ payloads and network connections are noisy. Unknown ERD codes, partial frames, and transient network errors must degrade gracefully without crashing the client loop.
5. **Strict Credential Hygiene:** Authentication tokens, passwords, MFA codes, and session cookies must never be logged or persisted in source control.

## 2. The Scratchpad Rule

**Agent Rule:** All temporary scripts, payload captures, or throwaway analysis artifacts MUST be written to `.scratchpad/`. This directory is git-ignored. Do not write temporary files to the repository root or `gehomesdk/`.

## 3. Compliance Checklist

Before considering a change complete:

* [ ] Offline `pytest` suite passes (`.venv\Scripts\python.exe -m pytest -q`).
* [ ] Lint check passes (`.venv\Scripts\python.exe -m ruff check gehomesdk tests`).
* [ ] Workspace type check passes (`pyright`).
* [ ] Markdown documentation is clean against `.markdownlint.json` rules when editing docs.
* [ ] Async code paths contain no blocking I/O (`time.sleep`, synchronous `requests` calls).
* [ ] Public classes, methods, and functions have clear type annotations and docstrings.
* [ ] New ERD codes are registered in `gehomesdk/erd/erd_configuration.py` and exported cleanly.
* [ ] No credentials, tokens, or PII appear in logs, tests, or committed files.

## 4. Feature Workflows

### Adding or Updating an ERD Code / Converter

1. **Define the Code:** Add the hex code to `ErdCode` in `gehomesdk/erd/erd_codes.py`.
2. **Define Value Types (if needed):** Add enums, dataclasses, or namedtuples under `gehomesdk/erd/values/<appliance>/` and export them in `__init__.py`.
3. **Implement Converter:** Add or reuse an `ErdValueConverter` subclass under `gehomesdk/erd/converters/<appliance>/` and export it in `__init__.py`.
4. **Register:** Map the `ErdCode` to its converter, `ErdCodeClass`, and `ErdDataType` in `gehomesdk/erd/erd_configuration.py`.
5. **Test:** Add unit tests in `tests/` covering `erd_decode`, `erd_encode` (if writable), boundary values, and malformed/empty payloads.

### Modifying Client / Auth / Appliance Behavior

1. **Write or Update Tests First (Red):** Add offline tests in `tests/` using mocked `aiohttp` / client transports.
2. **Implement Change (Green):** Keep transport/auth concerns in `clients/`, data caching in `ge_appliance.py`, and protocol errors in `exception/`.
3. **Verify:** Run `pytest` and ensure no background tasks are leaked.
