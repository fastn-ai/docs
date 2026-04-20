---
description: Install the Python SDK, connect to a service, and execute your first tool call in under 5 minutes.
---

# Python SDK quickstart

In this tutorial, you install the Fastn Python SDK, authenticate with the platform, and send a Slack message — all from a Python script. By the end, you have a working integration that calls any of Fastn's 250+ connectors from code.

### What you'll learn

* How to install and configure the Fastn Python SDK
* How to authenticate using an API key
* How to call a connector action (Slack) directly from Python
* How to discover tools and use them with an LLM agent

**Estimated time:** 5 minutes

### Prerequisites

* **Python 3.8 or higher** installed on your machine
* A **Fastn account** — sign up at [fastn.ai](https://fastn.ai/) if you do not have one
* A **Fastn API key** and **project ID** — find these in your Fastn dashboard under **Settings → API Keys**
* A **Slack workspace** connected to your Fastn project (with the Slack connector authenticated in Fastn)

### Step 1: Install the SDK

Install the `fastn-ai` package from PyPI:

```bash
pip install fastn-ai
```

To use the CLI tools as well (for login, connector management, and more), install with the CLI extras:

```bash
pip install fastn-ai[cli]
```

### Step 2: Configure your credentials

You can provide credentials in three ways. The SDK checks them in this order:

1. **Constructor parameters** (highest priority)
2. **Environment variables**
3. **Config file** at `.fastn/config.json`

For this tutorial, set environment variables:

```bash
export FASTN_API_KEY="your-api-key"
export FASTN_PROJECT_ID="your-project-id"
```

> **Tip**: Store these in a `.env` file for local development. Never commit API keys to version control.

### Step 3: Send your first Slack message

Create a file called `quickstart.py`:

```python
from fastn import FastnClient

# Picks up FASTN_API_KEY and FASTN_PROJECT_ID from environment variables
fastn = FastnClient()

# Send a message to Slack
result = fastn.slack.send_message(
    channel="general",
    text="Hello from the Fastn Python SDK!",
)

print("Result:", result)
```

Run it:

```bash
python quickstart.py
```

Check your Slack channel — the message "Hello from the Fastn Python SDK!" should appear.

> **Note**: Fastn manages OAuth tokens securely. Your code never handles raw Slack credentials. You authenticate Slack once in the Fastn dashboard, and the SDK handles the rest.

### Step 4: Verify it worked

If the call succeeded, `result` contains the Slack API response with the message timestamp and channel ID. If something went wrong, the SDK raises a descriptive exception:

| Exception | Cause |
|-----------|-------|
| `AuthError` | Invalid API key or expired token |
| `ConnectorNotFoundError` | Connector not in your local registry |
| `APIError` | Upstream API returned an error |

```python
from fastn import FastnClient, AuthError, ConnectorNotFoundError, APIError

fastn = FastnClient()

try:
    result = fastn.slack.send_message(channel="general", text="Hello!")
    print("Sent:", result)
except AuthError:
    print("Check your FASTN_API_KEY — it may be invalid or expired.")
except ConnectorNotFoundError:
    print("Slack connector not found. Connect Slack in your Fastn dashboard.")
except APIError as e:
    print(f"API error (HTTP {e.status_code}): {e}")
```

### Step 5: Discover tools with semantic search

Fastn connects to 250+ services. Instead of memorizing tool names, use `get_tools_for()` to find relevant tools by describing what you need:

```python
from fastn import FastnClient

fastn = FastnClient()

# Find the top 5 tools related to your task
tools = fastn.get_tools_for("Send a message on Slack", format="openai")

for tool in tools:
    print(tool["function"]["name"])
```

The `format` parameter controls the output shape. Supported values:

| Format | Use with |
|--------|----------|
| `openai` | OpenAI GPT models |
| `anthropic` | Anthropic Claude models |
| `gemini` | Google Gemini models |
| `bedrock` | AWS Bedrock models |
| `raw` | Direct use (no LLM) |

### Step 6: Build an LLM agent (optional)

Combine `get_tools_for()` with an LLM to create an agent that picks the right tool and fills in the parameters automatically:

```python
import json
from fastn import FastnClient

fastn = FastnClient()

# Get tools formatted for OpenAI
tools = fastn.get_tools_for("Send a message on Slack", format="openai")

# Pass tools to OpenAI
import openai

client = openai.OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Send 'Hello from my AI agent!' to #general on Slack"}],
    tools=tools,
)

# Execute the tool calls Fastn identified
for tool_call in response.choices[0].message.tool_calls:
    result = fastn.execute(
        tool=tool_call.function.name,
        params=json.loads(tool_call.function.arguments),
    )
    print("Executed:", tool_call.function.name, "→", result)
```

Or use the AI-powered shortcut that does discovery and execution in a single call:

```python
result = fastn.run("Send 'Hello from my AI agent!' to #general on Slack")
print(result)
```

### Summary

You installed the Fastn Python SDK, authenticated with the platform, sent a Slack message from code, and explored semantic tool discovery. The same pattern works for any of Fastn's 250+ connectors — replace `fastn.slack.send_message()` with `fastn.github.create_issue()`, `fastn.jira.create_issue()`, or any other connector action.

### Next steps

* **Explore connectors**: Browse available connectors and their actions in your Fastn dashboard, or run `fastn.connectors.list()` in Python.
* **Add multi-tenancy**: Pass `tenant_id` to execute actions on behalf of your customers — see [Multitenancy](../ucl-unified-context-layer/getting-started/about-unified-context-layer/multitenancy.md).
* **Use async**: Replace `FastnClient` with `AsyncFastnClient` for non-blocking calls in async applications.
* **Build flows**: Create automated workflows that chain multiple connector actions — see the [Quick Start Guide](../flows/quick-start-guide.md).
* **Connect via MCP**: Integrate Fastn with Claude Desktop or Cursor using the MCP server — see [Defining an MCP Server](../ucl-unified-context-layer/getting-started/about-unified-context-layer/defining-an-mcp-server.md).

### Troubleshooting

| Problem | Solution |
|---------|----------|
| `ConfigError: api_key is required` | Set `FASTN_API_KEY` environment variable or pass `api_key` to `FastnClient()` |
| `AuthError` on every call | Verify your API key is correct and active in **Settings → API Keys** |
| `ConnectorNotFoundError: slack` | Connect Slack in your Fastn dashboard and ensure the connector is authenticated |
| `ImportError: No module named 'fastn'` | Run `pip install fastn-ai` (the package name is `fastn-ai`, not `fastn`) |
| Timeout errors | Increase timeout with `FastnClient(timeout=60)` — default is 30 seconds |
