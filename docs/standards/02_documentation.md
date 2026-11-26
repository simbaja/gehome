# Documentation & Commenting Standards

This document defines the **Documentation and Commenting Standards** for `gehomesdk`.

It exists to:
* Preserve protocol and architectural intent over time (especially undocumented SmartHQ/ERD quirks)
* Maximize scanability in large client and appliance modules
* Serve as authoritative context for human contributors and AI agents

---

## 1. Scope & Applicability

Documentation strictness scales with module complexity and architectural importance.

| Layer | Strictness | Requirements |
| :--- | :--- | :--- |
| **Clients & Auth (`clients/`)** | **High** | Module docstring, Tier 1/2/3 hierarchy for large files, Google-style docstrings, protocol "why" comments |
| **Core Model (`ge_appliance.py`, `erd_encoder.py`)** | **High** | Module docstring, Google-style docstrings, invariant comments |
| **Complex Converters / CLI** | **Medium** | Google-style docstrings, byte-layout or bitmask "why" comments |
| **Simple ERD Values / Converters / Exceptions** | **Lightweight** | Concise class/method docstrings; no structural region overhead |

> **Rule:** Do not add Tier 1/2/3 structural headers or regions to small, single-purpose files (under ~200 lines) such as individual ERD enums or simple converters.

---

## 2. Module-Level Documentation

Every non-trivial module must begin with a module docstring describing its role.

```python
"""
SmartHQ WebSocket client implementation.

Manages the persistent WebSocket connection, keepalive heartbeats,
message dispatch, and automatic reconnection with backoff.
"""
```

---

## 3. Structural Hierarchy & Navigation (Large Files)

Files exceeding ~250 lines or spanning multiple responsibilities (such as `base_client.py`, `websocket_client.py`, `ge_appliance.py`) should use a three-tier visual hierarchy:

### Tier 1: Major Divisions
Used for major architectural splits within large modules.
* **Style:** Bold Uppercase, Triple Hashes (`# ### SECTION NAME ###`)
* **Buffer:** 2 blank lines above / below

### Tier 2: Functional Groups
Used for conceptual grouping within a division.
* **Style:** Mixed case, Triple Dashes (`# --- Group Name ---`)
* **Buffer:** 1 blank line above / below

### Tier 3: Collapsible Regions
Used to group 3–5 closely related methods.
* **Style:** `# region Name` ... `# endregion`
* **Rules:** Do NOT nest regions; include a short summary comment immediately after `# region Name`; always pair every `# region` with `# endregion`.

```python
# region Event Handlers
# Registration and dispatch for client lifecycle callbacks.

def add_event_handler(self, ...): ...

# endregion
```

---

## 4. Technical Docstrings

All public classes, methods, and functions require docstrings.

* **Format:** Google Python Style Guide for all new/updated code.
* **Voice:** Imperative ("Decode the raw hex payload." not "Decodes the raw hex payload.").
* **Focus:** Document side effects, raised exceptions (`GeAuthFailedError`, `ValueError`), and protocol assumptions rather than repeating type hints.

```python
def decode_value(self, erd_code: ErdCodeType, erd_value: str) -> Any:
    """Decode a raw ERD hex payload into its typed Python representation.

    Falls back to raw bytes when the ERD code is unregistered or decoding
    raises a ValueError.

    Args:
        erd_code: Known ``ErdCode`` enum member or hex string identifier.
        erd_value: Raw hex payload string without a leading ``0x`` prefix.

    Returns:
        Decoded value object, raw bytes on fallback, or ``None`` if empty.
    """
```

---

## 5. Architectural & Protocol Signals ("Why" Comments)

Comments must explain **design intent or SmartHQ/ERD protocol behavior**, not narrate Python syntax.

```python
# SmartHQ rotates refresh tokens on reconnect; persist the new token on
# the client so callers can avoid re-triggering MFA on the next restart.
```

```python
# ERD bitmask byte 2 encodes fan speed in the lower nibble (0x0F).
```

---

## 6. Temporal Markers

Time-sensitive workarounds or technical debt must use explicit markers:

```python
# TODO: Consolidate duplicate OAuth2 header construction into async_login_flows.
# TEMP: SmartHQ EU endpoint returns HTTP 502 intermittently during token refresh.
# DEBT: Legacy XMPP reference remains in docstring until 2027 cleanup.
```

Unmarked temporal comments are prohibited.

---

## 7. Summary Checklist

Before committing:
* [ ] Module docstring present on non-trivial modules
* [ ] Public interfaces documented (Google style)
* [ ] Structural hierarchy applied only where file size/complexity warrants it
* [ ] Region parity verified (every `# region` has a matching `# endregion`)
* [ ] Comments explain protocol/design intent ("why"), not code narration ("what")
