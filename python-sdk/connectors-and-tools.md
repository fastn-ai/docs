---
description: >-
  Browse the connector catalog, inspect tool schemas, and discover tools
  formatted for OpenAI, Anthropic, Gemini, and Bedrock.
---

# Connectors and tools

The connector catalog provides programmatic access to browse, inspect, and discover tools across Fastn's 250+ connectors. Access it through the `fastn.connectors` namespace.

## Connector catalog

### `connectors.list()`

List all available connectors from the local registry.

```python
fastn = FastnClient()
connectors = fastn.connectors.list()

for connector in connectors:
    print(f"{connector['name']} — {connector['tool_count']} tools")
```

**Returns:** `list[dict]` — Each dict contains:

| Field | Type | Description |
|-------|------|-------------|
| `name` | `str` | Connector identifier (e.g., `"slack"`) |
| `display_name` | `str` | Human-readable name (e.g., `"Slack"`) |
| `category` | `str` | Connector category |
| `tool_count` | `int` | Number of available tools |

{% hint style="info" %}
The `AsyncFastnClient`'s `connectors.list()` method fetches from the API instead of the local registry, returning workspace and community connectors with `name`, `display_name`, and `id` fields.
{% endhint %}

### `connectors.get()`

Get detailed information about a specific connector.

```python
slack = fastn.connectors.get("slack")
print(slack["display_name"])  # "Slack"
print(len(slack["tools"]))    # Number of tools
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `connector_name` | `str` | Yes | Connector identifier |

**Returns:** `dict` with `name`, `display_name`, `category`, and `tools`.

**Raises:** `ConnectorNotFoundError` if the connector is not in the registry.

### `connectors.get_tools()`

Get all tools for a connector with full schemas.

```python
tools = fastn.connectors.get_tools("slack")
for tool in tools:
    print(f"{tool['name']}: {tool['description']}")
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `connector_name` | `str` | Yes | Connector identifier |

**Returns:** `list[dict]` — Each tool contains:

| Field | Type | Description |
|-------|------|-------------|
| `name` | `str` | Tool name (e.g., `"send_message"`) |
| `description` | `str` | What the tool does |
| `toolId` | `str` | Server-side tool identifier |
| `inputSchema` | `dict` | JSON Schema for input parameters |
| `outputSchema` | `dict` | JSON Schema for output |

### `connectors.get_tool()`

Get a single tool's schema.

```python
tool = fastn.connectors.get_tool("slack", "send_message")
print(tool["inputSchema"])
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `connector_name` | `str` | Yes | Connector identifier |
| `tool_name` | `str` | Yes | Tool name |

**Returns:** `dict` — Same shape as items in `get_tools()`.

**Raises:** `ToolNotFoundError` if the tool is not found. Supports underscore-collapsed name matching (e.g., `send_message` matches `sendmessage`).

## Tool discovery

### Semantic search

Use `get_tools_for()` on the client to find tools via natural language:

```python
tools = fastn.get_tools_for(
    "Create a Jira ticket for a bug",
    format="openai",
    limit=5,
)
```

This calls the Fastn API which uses semantic matching to return the most relevant tools. Results are formatted for your LLM provider.

### Supported LLM formats

| Format | Provider | Description |
|--------|----------|-------------|
| `"openai"` | OpenAI | Function calling format with `type: "function"` wrapper |
| `"anthropic"` | Anthropic (Claude) | Tool use format with `input_schema` |
| `"gemini"` | Google Gemini | Function declarations format |
| `"bedrock"` | AWS Bedrock | `toolSpec` wrapper with `inputSchema.json` |
| `"raw"` | Any | Unformatted tool definitions |

### Schema unwrapping

Before formatting for LLMs, the SDK automatically unwraps single-wrapper schemas. For example, a schema like `{body: {type: object, properties: {...}}}` is unwrapped one level so the LLM sees the actual parameters directly.

## Connector access patterns

### Direct attribute access

Access connectors as attributes on the client:

```python
fastn.slack.send_message(channel="general", text="Hello!")
fastn.jira.create_issue(project="PROJ", summary="New task")
```

### Bound connections

For multi-tenant or multi-connection scenarios, bind a connection:

```python
# Bind once, reuse for all calls
slack = fastn.connect("conn_abc")
slack.send_message(channel="general", text="Hello!")
slack.list_channels()
```

### Per-call overrides

Override `connection_id` or `tenant_id` on individual calls:

```python
fastn.slack.send_message(
    channel="general",
    text="Hello!",
    connection_id="conn_abc",
    tenant_id="tenant_123",
)
```

## Migration support

The SDK provides backward compatibility when connector tool schemas change:

| Migration type | Behavior |
|----------------|----------|
| `deprecated_params` | Strips removed parameters and emits a `DeprecationWarning` |
| `param_defaults` | Fills new required parameter defaults and emits a `DeprecationWarning` |
| `type_coercions` | Warns about type changes |

Migration records are stored in `.fastn/migrations.json` and applied automatically during tool calls.
