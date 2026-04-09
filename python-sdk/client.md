---
description: >-
  Reference for FastnClient, AsyncFastnClient, and the DynamicConnector proxy
  that provides typed access to 250+ connectors.
---

# Client

The client classes are the primary interface to the Fastn platform. `FastnClient` provides synchronous access, and `AsyncFastnClient` provides asynchronous access with identical functionality.

## FastnClient

```python
from fastn import FastnClient

fastn = FastnClient(
    api_key="your-api-key",
    project_id="your-project-id",
)
```

### Constructor parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api_key` | `str` or `None` | `None` | Fastn platform API key. Falls back to `FASTN_API_KEY` env var or `.fastn/config.json`. |
| `project_id` | `str` or `None` | `None` | Project/workspace ID. Falls back to `FASTN_PROJECT_ID` env var or config file. |
| `timeout` | `float` or `None` | `None` | HTTP request timeout in seconds. Resolves to `30.0` from config when not specified. |
| `config_path` | `str` or `None` | `None` | Explicit path to `.fastn/config.json`. |
| `auth_token` | `str` or `None` | `None` | JWT access token from `fastn login`. |
| `agent_id` | `str` or `None` | `None` | Agent identifier. Defaults to the resolved project ID. |
| `tenant_id` | `str` or `None` | `None` | Multi-tenant identifier for scoping connections. |
| `stage` | `str` or `None` | `None` | Deployment stage: `"LIVE"`, `"STAGING"`, or `"DEV"`. Resolves to `"LIVE"` from config when not specified. |
| `max_retries` | `int` | `3` | Maximum retry count for failed HTTP requests. |
| `verbose` | `bool` | `False` | Enable debug logging to stdout. |

### Namespaces

The client exposes these namespace attributes for domain-specific operations:

| Attribute | Type | Description |
|-----------|------|-------------|
| `fastn.connectors` | `_ConnectorCatalog` | Browse and inspect connectors and tools |
| `fastn.flows` | `_FlowsSync` | Create, run, deploy, and manage flows |
| `fastn.auth` | `_AuthSync` | Manage OAuth connections |
| `fastn.projects` | `_ProjectsSync` | List projects |
| `fastn.skills` | `_SkillsSync` | List agent skills |
| `fastn.kit` | `_KitSync` | Manage Connect Kit configuration |

### Methods

#### `execute()`

Execute a tool by its tool ID with pre-built parameters.

```python
result = fastn.execute(
    tool="slack_send_message",
    params={"channel": "general", "text": "Hello!"},
    connection_id="conn_abc",   # optional
    tenant_id="acme-corp",      # optional
)
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tool` | `str` | Yes | Tool identifier (e.g., `"slack_send_message"`) |
| `params` | `dict` | Yes | Tool input parameters |
| `connection_id` | `str` or `None` | No | Override the connection for this call |
| `tenant_id` | `str` or `None` | No | Override the tenant for this call |

**Returns:** `Any` — The tool execution result from the Fastn API.

#### `run()`

AI-powered tool discovery and execution in one call. Describe your intent in plain English and Fastn discovers the right tool, extracts parameters, and executes.

```python
result = fastn.run("Send hello to #general on Slack")
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `prompt` | `str` | Yes | Natural language description of the task |
| `connection_id` | `str` or `None` | No | Override the connection |

**Returns:** `dict` — The execution result with tool selection details.

#### `get_tools_for()`

Discover tools via semantic search, formatted for a specific LLM provider.

```python
tools = fastn.get_tools_for(
    "Send a message on Slack",
    format="openai",
    limit=5,
    connector="slack",
)
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | `str` | Yes | — | Natural language query for semantic tool search |
| `format` | `str` | No | `"openai"` | LLM format: `"openai"`, `"anthropic"`, `"gemini"`, `"bedrock"`, `"raw"` |
| `limit` | `int` | No | `5` | Maximum number of tools to return |
| `connector` | `str`, `list`, or `None` | No | `None` | Scope search to specific connector(s) |

**Returns:** `list[dict]` — Tool definitions formatted for the specified LLM provider.

{% hint style="info" %}
Dynamic tool filtering sends only the top 5 semantically relevant tools to the LLM by default, reducing 250+ tools to approximately 2,500 tokens.
{% endhint %}

#### `get_tools()`

Get all tools for a connector with raw schemas from the local registry.

```python
tools = fastn.get_tools("slack")
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `connector_name` | `str` | Yes | Connector name (e.g., `"slack"`) |

**Returns:** `list[dict]` — Tool definitions with `name`, `description`, `toolId`, `inputSchema`, and `outputSchema`.

#### `get_tool()`

Get a single tool's raw schema from the local registry.

```python
tool = fastn.get_tool("slack", "send_message")
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `connector_name` | `str` | Yes | Connector name |
| `tool_name` | `str` | Yes | Tool name |

**Returns:** `dict` — Tool definition with schema details.

#### `connect()`

Bind a `connection_id` and return a connector proxy. All calls through this proxy use the specified connection.

```python
slack = fastn.connect("conn_abc")
slack.send_message(channel="general", text="Hello!")
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection_id` | `str` | Yes | Connection identifier |

**Returns:** `DynamicConnector` — A proxy with all tools bound to the specified connection.

#### `close()`

Close the underlying HTTP client and release resources.

```python
fastn.close()
```

### Context manager

`FastnClient` supports the `with` statement for automatic resource cleanup:

```python
with FastnClient(api_key="...") as fastn:
    fastn.slack.send_message(channel="general", text="Hello!")
# HTTP client is closed automatically
```

## AsyncFastnClient

The async client has identical constructor parameters and methods. All I/O methods are coroutines.

```python
from fastn import AsyncFastnClient

async with AsyncFastnClient(api_key="...") as fastn:
    result = await fastn.execute(
        tool="slack_send_message",
        params={"channel": "general", "text": "Hello!"},
    )
    await fastn.slack.send_message(channel="general", text="Hello!")
    tools = await fastn.get_tools_for("Send a Slack message", format="anthropic")
    result = await fastn.run("Send hello to #general on Slack")
```

{% hint style="info" %}
The async client's `connectors.list()` method fetches connector data from the API (workspace + community connectors) rather than using only the local registry.
{% endhint %}

## DynamicConnector

The `DynamicConnector` is a proxy object that maps Python method calls to Fastn tool executions. You don't instantiate it directly — access it through dynamic attribute lookup on the client.

### Accessing connectors

```python
fastn = FastnClient(api_key="...", project_id="...")

# Access any connector as an attribute
fastn.slack.send_message(channel="general", text="Hello!")
fastn.jira.create_issue(project="PROJ", summary="Bug fix")
fastn.github.create_issue(owner="org", repo="app", title="New issue")
```

### Per-call overrides

Every tool call accepts optional `connection_id` and `tenant_id` keyword arguments:

```python
fastn.slack.send_message(
    channel="general",
    text="Hello!",
    connection_id="conn_abc",
    tenant_id="acme-corp",
)
```

These override the client-level defaults for that single call.

### Tool name resolution

The connector resolves tool names in this order:

1. **Exact match** against the tool registry
2. **Underscore-collapsed fallback** — `send_message` matches `sendmessage`
3. **Deprecated tool lookup** from migration records

If no match is found, a `ToolNotFoundError` is raised.

### Bound connectors

Use `connect()` to create a connector proxy bound to a specific connection:

```python
slack = fastn.connect("conn_abc")
slack.send_message(channel="general", text="Hello!")
# All calls through 'slack' use connection_id="conn_abc"
```

### AsyncDynamicConnector

The async variant works identically, but tool calls return awaitables:

```python
async with AsyncFastnClient() as fastn:
    await fastn.slack.send_message(channel="general", text="Hello!")
```

## LLM tool format output

The `get_tools_for()` method returns tool definitions formatted for your LLM provider:

{% tabs %}
{% tab title="OpenAI" %}
```json
{
  "type": "function",
  "function": {
    "name": "slack_send_message",
    "description": "Send a message to a Slack channel",
    "parameters": {
      "type": "object",
      "properties": {
        "channel": {"type": "string"},
        "text": {"type": "string"}
      },
      "required": ["channel", "text"]
    }
  }
}
```
{% endtab %}

{% tab title="Anthropic" %}
```json
{
  "name": "slack_send_message",
  "description": "Send a message to a Slack channel",
  "input_schema": {
    "type": "object",
    "properties": {
      "channel": {"type": "string"},
      "text": {"type": "string"}
    },
    "required": ["channel", "text"]
  }
}
```
{% endtab %}

{% tab title="Gemini" %}
```json
{
  "name": "slack_send_message",
  "description": "Send a message to a Slack channel",
  "parameters": {
    "type": "object",
    "properties": {
      "channel": {"type": "string"},
      "text": {"type": "string"}
    },
    "required": ["channel", "text"]
  }
}
```
{% endtab %}

{% tab title="Bedrock" %}
```json
{
  "toolSpec": {
    "name": "slack_send_message",
    "description": "Send a message to a Slack channel",
    "inputSchema": {
      "json": {
        "type": "object",
        "properties": {
          "channel": {"type": "string"},
          "text": {"type": "string"}
        },
        "required": ["channel", "text"]
      }
    }
  }
}
```
{% endtab %}
{% endtabs %}

## Retry behavior

The client automatically retries failed requests with exponential backoff:

| Condition | Behavior |
|-----------|----------|
| HTTP 429 (rate limit) | Retries with `0.5 * 2^attempt` second delay |
| Connection errors | Retries with exponential backoff |
| Read timeouts | Retries with exponential backoff |
| Max retries exceeded | Raises `APIError` |

The default maximum is 3 retries, configurable via the `max_retries` constructor parameter.

## Token auto-refresh

The client automatically refreshes expired JWT tokens before every API request. A 30-second safety buffer ensures tokens are refreshed before actual expiry. If refresh fails, an `AuthError` is raised.
