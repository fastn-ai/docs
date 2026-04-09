---
description: >-
  Exception hierarchy, attributes, and handling patterns for Fastn SDK errors.
---

# Exceptions

All SDK exceptions inherit from `FastnError`. Import them from the `fastn` package.

```python
from fastn import FastnError, APIError, AuthError, ConfigError
```

## Exception hierarchy

```
FastnError
├── AuthError
│   └── OAuthError
├── ConfigError
├── ConnectorNotFoundError
├── ToolNotFoundError
├── ConnectionNotFoundError
├── FlowNotFoundError
├── RunNotFoundError
├── APIError
└── RegistryError
```

## Exception reference

### FastnError

Base exception for all SDK errors.

| Attribute | Type | Description |
|-----------|------|-------------|
| `message` | `str` | Human-readable error message |
| `details` | `dict` | Additional error context. Defaults to an empty dict `{}`. |

```python
from fastn import FastnError

try:
    fastn.slack.send_message(channel="general", text="Hello!")
except FastnError as e:
    print(e.message)
    print(e.details)
```

### APIError

Raised when the Fastn API returns an HTTP error (4xx or 5xx).

| Attribute | Type | Description |
|-----------|------|-------------|
| `message` | `str` | Error description |
| `status_code` | `int` or `None` | HTTP status code |
| `response_body` | `dict` or `None` | Raw API response body |

```python
from fastn import APIError

try:
    result = fastn.execute(tool="invalid_tool", params={})
except APIError as e:
    print(f"HTTP {e.status_code}: {e.message}")
```

### AuthError

Raised when authentication fails (invalid or expired credentials).

```python
from fastn import AuthError

try:
    fastn = FastnClient(api_key="invalid-key")
    fastn.slack.send_message(channel="general", text="Hello!")
except AuthError as e:
    print(f"Auth failed: {e.message}")
```

### OAuthError

Raised when the OAuth device flow fails. Inherits from `AuthError`.

| Attribute | Type | Description |
|-----------|------|-------------|
| `error_code` | `str` or `None` | OAuth error code (e.g., `"expired_token"`) |

### ConfigError

Raised when required configuration is missing (no `api_key` or `project_id`).

```python
from fastn import ConfigError

try:
    fastn = FastnClient()  # No credentials available
except ConfigError as e:
    print(f"Missing config: {e.message}")
```

### ConnectorNotFoundError

Raised when a connector name does not exist in the local registry.

| Attribute | Type | Description |
|-----------|------|-------------|
| `connector_name` | `str` | The connector that was not found |

```python
from fastn import ConnectorNotFoundError

try:
    fastn.nonexistent_connector.some_tool()
except ConnectorNotFoundError as e:
    print(f"Connector '{e.connector_name}' not found. Run 'fastn connector sync'.")
```

### ToolNotFoundError

Raised when a tool name does not exist on a connector.

| Attribute | Type | Description |
|-----------|------|-------------|
| `connector_name` | `str` | The connector name |
| `tool_name` | `str` | The tool that was not found |

```python
from fastn import ToolNotFoundError

try:
    fastn.slack.nonexistent_tool()
except ToolNotFoundError as e:
    print(f"Tool '{e.tool_name}' not found on '{e.connector_name}'")
```

### ConnectionNotFoundError

Raised when multiple connections exist for a connector and no `connection_id` was specified.

### FlowNotFoundError

Raised when a flow does not exist.

| Attribute | Type | Description |
|-----------|------|-------------|
| `flow_id` | `str` | The flow that was not found |

### RunNotFoundError

Raised when a flow run does not exist.

| Attribute | Type | Description |
|-----------|------|-------------|
| `run_id` | `str` | The run that was not found |

### RegistryError

Raised when the connector registry fails to sync or parse.

## HTTP status code mapping

The SDK maps HTTP status codes to specific exceptions:

| HTTP status | Exception | Description |
|-------------|-----------|-------------|
| 401 | `AuthError` | Authentication failed |
| 4xx with `FLOW_NOT_FOUND` | `FlowNotFoundError` | Flow does not exist |
| 4xx with `RUN_NOT_FOUND` | `RunNotFoundError` | Run does not exist |
| Other 4xx/5xx | `APIError` | General API error |
| GraphQL errors | `APIError` | GraphQL query failed |

## Handling patterns

### Catch specific errors

```python
from fastn import (
    FastnClient,
    AuthError,
    ConnectorNotFoundError,
    ToolNotFoundError,
    APIError,
)

fastn = FastnClient()

try:
    fastn.slack.send_message(channel="general", text="Hello!")
except AuthError:
    print("Authentication failed. Check your credentials.")
except ConnectorNotFoundError:
    print("Connector not found. Run 'fastn connector sync'.")
except ToolNotFoundError:
    print("Tool not found. Check the tool name.")
except APIError as e:
    print(f"API error (HTTP {e.status_code}): {e.message}")
```

### Catch all SDK errors

```python
from fastn import FastnError

try:
    fastn.slack.send_message(channel="general", text="Hello!")
except FastnError as e:
    print(f"Fastn error: {e.message}")
```
