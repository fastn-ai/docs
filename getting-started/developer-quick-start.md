---
description: >-
  Install the Python SDK, configure credentials, and make your first tool call
  in under five minutes.
---

# Developer quick start

This guide gets you from zero to executing your first tool call through Fastn's Python SDK. By the end you will have the SDK installed, credentials configured, and a working integration that connects your code to 250+ enterprise apps.

## What you'll learn

* How to install and configure the Fastn Python SDK
* How to discover tools with semantic search
* How to execute a tool call (send a Slack message)
* How to feed Fastn tools to an LLM for agentic workflows

**Estimated time:** 5 minutes

## Prerequisites

* Python 3.8 or higher
* A Fastn account — sign up at [fastn.ai](https://fastn.ai/) if you do not have one
* An API key and project ID from your Fastn dashboard (**Settings > API Keys**)

## Step 1: Install the SDK

```bash
pip install fastn-ai
```

This installs the `fastn` package with type stubs for 250+ connectors, giving you IDE autocomplete out of the box.

## Step 2: Configure credentials

You have two options for authentication:

### Option A: Environment variables

```bash
export FASTN_API_KEY="your-api-key"
export FASTN_PROJECT_ID="your-project-id"
```

### Option B: CLI login (OAuth)

```bash
fastn login
```

This opens your browser for authentication, then saves credentials to `.fastn/config.json`. The SDK auto-refreshes tokens before they expire.

> **Note:** The SDK checks credentials in this order: constructor parameters, environment variables, config file. The first value found wins.

## Step 3: Make your first tool call

```python
from fastn import FastnClient

fastn = FastnClient()

# Call any connector directly — the SDK handles auth and routing
fastn.slack.send_message(channel="general", text="Hello from Fastn!")
```

The dynamic proxy (`fastn.slack.send_message`) resolves the connector and tool at runtime, maps your parameters to the correct API schema, and executes the call through Fastn's platform.

## Step 4: Discover tools with semantic search

Fastn manages 250+ connectors with thousands of tools. Instead of browsing them manually, describe what you need in natural language:

```python
tools = fastn.get_tools_for(
    "Send a message on Slack and create a Jira ticket",
    format="openai",
    limit=5,
)

print(tools)
# Returns the top 5 most relevant tools in OpenAI function-calling format
```

The `format` parameter controls the output schema. Supported values:

| Format | LLM provider |
|--------|-------------|
| `openai` | OpenAI (GPT-4o, GPT-4) |
| `anthropic` | Anthropic (Claude) |
| `gemini` | Google (Gemini) |
| `bedrock` | AWS Bedrock |
| `raw` | Unformatted Fastn schema |

## Step 5: Build an agentic workflow

Combine Fastn's tool discovery with an LLM to build AI agents that take real actions:

```python
import json
import openai
from fastn import FastnClient

fastn = FastnClient()

# 1. Discover relevant tools
tools = fastn.get_tools_for(
    "Send a message on Slack",
    format="openai",
)

# 2. Send tools + prompt to the LLM
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Send hello to #general on Slack"}],
    tools=tools,
)

# 3. Execute the tool call the LLM chose
tool_call = response.choices[0].message.tool_calls[0]
result = fastn.execute(
    tool=tool_call.function.name,
    params=json.loads(tool_call.function.arguments),
)
print(result)
```

This pattern works the same way with Anthropic Claude:

```python
import anthropic
from fastn import FastnClient

fastn = FastnClient()
tools = fastn.get_tools_for("Send a message on Slack", format="anthropic")

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Send 'Build passed' to #ci"}],
    tools=tools,
)

for block in response.content:
    if block.type == "tool_use":
        result = fastn.execute(tool=block.name, params=block.input)
        print(result)
```

## Step 6: Add multi-tenant support

If your application serves multiple customers, pass a `tenant_id` to scope tool execution per customer:

```python
fastn = FastnClient(tenant_id="customer_123")

# All calls are scoped to this tenant
fastn.slack.send_message(channel="general", text="Hello!")

# Or override per call
fastn.slack.send_message(
    tenant_id="customer_456",
    channel="general",
    text="Hello from a different tenant!",
)
```

Each tenant's OAuth connections are managed independently by Fastn's SOC 2 certified vault. Your application code never handles raw tokens.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ConfigError: missing api_key` | Set `FASTN_API_KEY` as an environment variable or run `fastn login` |
| `ConnectorNotFoundError` | Run `fastn connector sync` to refresh the local registry |
| `AuthError` on tool execution | Verify the connector is connected in your Fastn dashboard |
| Import error after install | Confirm you installed `fastn-ai` (not `fastn`) |

## Next steps

* [Embedding UCL onto your AI agent](../ucl-unified-context-layer/getting-started/about-unified-context-layer/embedding-ucl-onto-your-ai-agent.md) — embed Fastn tools into a web application
* [Defining an MCP server](../ucl-unified-context-layer/getting-started/about-unified-context-layer/defining-an-mcp-server.md) — connect Fastn to Claude Desktop, Cursor, or other MCP clients
* [Quick start guide (Flows)](../flows/quick-start-guide.md) — build visual workflow automations
* [Multitenancy](../ucl-unified-context-layer/getting-started/about-unified-context-layer/multitenancy.md) — manage per-customer connections at scale
