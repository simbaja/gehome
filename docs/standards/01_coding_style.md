# Coding Style

## 1. Imports (3-Group Standard)

All Python files **MUST** order imports into three groups separated by **a single blank line**:

1. **Python Standard Library**
2. **Third-party dependencies** (`aiohttp`, `websockets`, `bidict`, `pytest`, etc.)
3. **Local `gehomesdk` imports**

### Correct

```python
import asyncio
import logging
from typing import Optional

import aiohttp

from ..erd import ErdCode, ErdCodeType
from ..exception import GeAuthFailedError
```

### Guidelines & Exceptions

* **Explicit imports in implementation and test files:** Do not add new `from module import *` statements in implementation modules or tests.
* **Barrel `__init__.py` exports:** Package `__init__.py` files and `erd_encoder.py` / `erd_configuration.py` currently use star imports for re-exporting ERD symbols; preserve existing barrel exports unless refactoring a package intentionally.
* **Avoid unnecessary `from __future__ import annotations`:** Use it only when forward references or circular `TYPE_CHECKING` imports require it.

## 2. Naming Standards

* **Modules, functions, variables, methods:** `snake_case`.
* **Classes and Exceptions:** `PascalCase` (SDK exceptions inherit from `GeException` and use `Ge*Error` naming).
* **Constants and Enum members:** `UPPER_SNAKE_CASE`.
* **Async methods:** Prefix public coroutine methods with `async_` (e.g., `async_get_credentials`, `async_set_erd_value`, `async_request_update`).
* **Magic strings/hex codes:** Move shared ERD codes to `ErdCode` and event/config constants to `clients/const.py`.

## 3. Comment Style

Comments are **architectural signals**, not narration.
* **Rule:** Explain *why*, never *what*.
* **Tone:** Neutral, technical, concise.

### Correct

```python
# Preserve raw hex bytes alongside decoded values so callers can inspect
# unparsed or partially supported ERDs without losing wire fidelity.
```

### Forbidden

```python
# Set _available to True
self._available = True
```

## 4. Docstrings

* Required for all public classes, methods, and functions.
* Short, factual, technical (Google style preferred for new code).
* Do not restate parameter types already expressed in type annotations.

## 5. Typing Patterns

* Target **Python 3.13+** compatibility (matches `setup.py` and `.vscode/settings.json` standard type checking).
* Annotate all public function/method parameters and return types.
* Avoid `Any` unless dealing with genuinely dynamic JSON or heterogeneous ERD decode outputs.
* Parametrize generic collections (`dict[str, GeAppliance]`, `list[str]`, `set[ErdCodeType]`). Use modern union syntax (`str | None`) or `Optional[str]` consistently within a file.

## 6. Hard Red Lines (Forbidden)

* Blocking I/O (`time.sleep`, synchronous `requests`) inside `async def` functions.
* Bare `except:`.
* Swallowing exceptions silently without logging or re-raising.
* Logging credentials, passwords, OAuth tokens, or session cookies.
* Hardcoding environment-specific paths or real user credentials.
