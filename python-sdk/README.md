---
description: >-
  Complete reference for the Fastn Python SDK — connect AI agents and
  applications to 250+ enterprise integrations with a few lines of code.
---

# Python SDK reference

The Fastn Python SDK (`fastn-ai`) provides a programmatic interface to the Fastn integration platform. Use it to connect your AI agents and applications to 250+ enterprise services including Slack, Jira, GitHub, Salesforce, PostgreSQL, Stripe, and more.

## Installation

Install from PyPI:

```bash
pip install fastn-ai
```

To use the CLI commands, install with the CLI extras:

```bash
pip install fastn-ai[cli]
```

{% hint style="info" %}
The SDK requires Python 3.8 or higher. The only core dependency is `httpx>=0.23.0`.
{% endhint %}

## Quickstart

### Authenticate

Run the CLI login command to authenticate and select a project:

```bash
fastn login
```

This opens a browser for OAuth authentication, then prompts you to select a workspace. Credentials are saved to `.fastn/config.json`.

Alternatively, set environment variables:

```bash
export FASTN_API_KEY="your-api-key"
export FASTN_PROJECT_ID="your-project-id"
```

### Sync connectors

Download tool schemas for the connectors you need:

```bash
fastn connector sync
fastn connector add slack hubspot jira
```

### Execute tools

```python
from fastn import FastnClient

fastn = FastnClient()
fastn.slack.send_message(channel="general", text="Hello from Fastn!")
```

### Async usage

```python
from fastn import AsyncFastnClient

async with AsyncFastnClient() as fastn:
    await fastn.slack.send_message(channel="general", text="Hello!")
```

### AI-powered execution

Describe your intent in plain English and let Fastn discover and execute the right tool:

```python
result = fastn.run("Send hello to #general on Slack")
```

### LLM tool integration

Discover tools formatted for your LLM provider:

```python
tools = fastn.get_tools_for(
    "Send a message on Slack",
    format="openai",
    limit=5,
)

# Pass tools to your LLM, then execute the selected tool
result = fastn.execute(
    tool="slack_send_message",
    params={"channel": "general", "text": "Hi from my agent"},
)
```

## Package exports

The `fastn` package exports the following public symbols:

| Export | Type | Description |
|--------|------|-------------|
| `FastnClient` | Class | Synchronous client |
| `AsyncFastnClient` | Class | Asynchronous client |
| `FastnError` | Exception | Base exception |
| `APIError` | Exception | HTTP API errors |
| `AuthError` | Exception | Authentication failures |
| `ConfigError` | Exception | Missing configuration |
| `ConnectionNotFoundError` | Exception | Ambiguous connection |
| `ConnectorNotFoundError` | Exception | Unknown connector |
| `FlowNotFoundError` | Exception | Unknown flow |
| `OAuthError` | Exception | OAuth flow failures |
| `RegistryError` | Exception | Registry sync failures |
| `RunNotFoundError` | Exception | Unknown flow run |
| `ToolNotFoundError` | Exception | Unknown tool |
| `__version__` | String | SDK version (currently `0.3.7`) |

## Authentication model

Fastn uses three distinct authentication layers:

| Layer | Purpose | Credential type |
|-------|---------|----------------|
| **API key** | App-to-Fastn platform auth | Static key via `x-fastn-api-key` header |
| **OAuth token** | Developer-to-Fastn auth | JWT from `fastn login`, auto-refreshes |
| **Connections** | End-user OAuth to external services | Fully managed by Fastn's SOC 2 vault |

Your application code never handles raw tokens for external services. Fastn manages the entire OAuth lifecycle for end-user connections.

## Reference pages

| Page | Description |
|------|-------------|
| [Client](client.md) | `FastnClient`, `AsyncFastnClient`, and the dynamic connector proxy |
| [Connectors and tools](connectors-and-tools.md) | Connector catalog, tool discovery, and LLM format conversion |
| [Flows](flows.md) | Workflow orchestration — create, run, deploy, and manage flows |
| [Authentication](authentication.md) | OAuth connections, connection status, and custom auth providers |
| [Configuration](configuration.md) | `FastnConfig`, environment variables, and the `.fastn/` directory |
| [CLI reference](cli-reference.md) | Complete command-line interface reference |
| [Exceptions](exceptions.md) | Error hierarchy and handling patterns |
