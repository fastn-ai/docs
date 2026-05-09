---
description: >-
  Connect your AI agent to 250+ tools in under 5 minutes using Fastn's Unified
  Context Layer. Choose the MCP server for AI assistants or the Python SDK for
  custom agents.
---

# Quickstart: Connect your AI agent to tools

This quickstart walks you through connecting an AI agent to real-world tools — Slack, GitHub, Jira, Gmail, and more — using UCL. Pick the path that fits your setup:

| Path | Best for | Time |
|------|----------|------|
| [**Option A: MCP server**](#option-a-connect-via-mcp-server) | Claude Desktop, Cursor, or any MCP-compatible client | 2 min |
| [**Option B: Python SDK**](#option-b-connect-via-python-sdk) | Custom AI agents built with OpenAI, Anthropic, or Gemini | 5 min |

## Prerequisites

Before you start, complete these one-time setup steps:

1. **Create a Fastn account** — Sign up at [app.fastn.ai](https://app.fastn.ai) and select a workspace.
2. **Connect at least one app** — From your dashboard's **Connect** page, enable a connector (for example, Slack or GitHub) and authorize access.

{% hint style="info" %}
UCL handles all OAuth token management in the background. Your application code never touches raw credentials.
{% endhint %}

---

## Option A: Connect via MCP server

Use Fastn's hosted MCP server to give any MCP-compatible AI assistant access to your connected tools. No installation required.

### 1. Add the MCP server config

Open your client's MCP configuration file and add the Fastn server:

{% tabs %}
{% tab title="Claude Desktop" %}
Edit your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "fastn": {
      "url": "https://mcp.live.fastn.ai/shttp"
    }
  }
}
```
{% endtab %}

{% tab title="Cursor" %}
Create or edit `.cursor/mcp.json` in your project root:

```json
{
  "mcpServers": {
    "fastn": {
      "url": "https://mcp.live.fastn.ai/shttp/tools"
    }
  }
}
```

{% hint style="info" %}
The `/shttp/tools` endpoint exposes only the five core tools (`find_tools`, `execute_tool`, `list_connectors`, `list_skills`, `list_projects`), which keeps your context window lean.
{% endhint %}
{% endtab %}

{% tab title="Claude Code" %}
Create or edit `.mcp.json` in your project root:

```json
{
  "mcpServers": {
    "fastn": {
      "url": "https://mcp.live.fastn.ai/shttp/tools"
    }
  }
}
```
{% endtab %}
{% endtabs %}

### 2. Authenticate

Restart your AI client. The first time it connects, a browser window opens and prompts you to log in with your Fastn account. This is a standard MCP OAuth 2.1 flow — authenticate once and the server manages token refresh automatically.

{% hint style="info" %}
If you prefer to skip the browser flow, pass an API key directly via a header instead:

```json
{
  "mcpServers": {
    "fastn": {
      "url": "https://mcp.live.fastn.ai/shttp",
      "headers": {
        "Authorization": "Bearer <your-api-key>"
      }
    }
  }
}
```

Generate an API key from the **Settings** page in your Fastn dashboard.
{% endhint %}

### 3. Try it out

Ask your AI assistant to perform an action using one of your connected tools. For example:

> "Send a message to #general on Slack saying 'Hello from Fastn!'"

Behind the scenes, the MCP server:

1. Searches 250+ connectors for the most relevant tool (`find_tools`)
2. Returns the tool schema to your AI assistant
3. Executes the action via the Fastn platform (`execute_tool`)

You're done! Your AI assistant now has access to every tool you've enabled in your UCL workspace.

---

## Option B: Connect via Python SDK

Use the SDK to programmatically give your AI agent access to tools. This example uses OpenAI, but the SDK also supports Anthropic, Gemini, and Bedrock.

### 1. Install the SDK

```bash
pip install fastn-ai
```

### 2. Set your credentials

You need two values from your Fastn dashboard:

- **API key** — Generate one from the **Settings** page
- **Project ID** — Visible on your workspace dashboard (also called Space ID)

Set them as environment variables:

```bash
export FASTN_API_KEY="your-api-key"
export FASTN_PROJECT_ID="your-project-id"
```

{% hint style="info" %}
Alternatively, run `fastn login` for browser-based OAuth authentication. The CLI stores credentials in `.fastn/config.json` so the SDK picks them up automatically.
{% endhint %}

### 3. Discover tools

The SDK uses semantic search to find the right tools for your prompt. Create a file called `agent.py`:

```python
from fastn import FastnClient

fastn = FastnClient()

# Describe what you need in natural language
tools = fastn.get_tools_for(
    "Send a message on Slack",
    format="openai",
)

print(f"Found {len(tools)} tools:")
for tool in tools:
    print(f"  - {tool['function']['name']}: {tool['function']['description']}")
```

Run it:

```bash
python agent.py
```

The SDK sends your prompt to the Fastn platform, which returns the top five semantically matched tools formatted for OpenAI's function calling API.

### 4. Build an agent loop

Now wire the tools into an LLM call. Update `agent.py`:

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

# 2. Send tools and a user prompt to the LLM
client = openai.OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Send 'Hello from Fastn!' to #general on Slack"}],
    tools=tools,
)

# 3. Execute the tool call returned by the LLM
for choice in response.choices:
    if choice.message.tool_calls:
        for tool_call in choice.message.tool_calls:
            result = fastn.execute(
                tool=tool_call.function.name,
                params=json.loads(tool_call.function.arguments),
            )
            print("Result:", result)
```

Run the agent:

```bash
python agent.py
```

The SDK handles schema translation, credential injection, and execution — your code never touches OAuth tokens or raw API calls.

{% hint style="info" %}
To use a different LLM provider, change the `format` parameter:

| Provider | Format value | Package |
|----------|-------------|---------|
| OpenAI | `openai` | `openai` |
| Anthropic | `anthropic` | `anthropic` |
| Google Gemini | `gemini` | `google-generativeai` |
| AWS Bedrock | `bedrock` | `boto3` |
{% endhint %}

### 5. Verify in the dashboard

Open the **Monitoring** page in your UCL dashboard to see the tool execution log. Each call shows the connector, action, status, and response time.

---

## Next steps

- [About Unified Context Layer](about-unified-context-layer/) — Learn how UCL works and why it complements MCP
- [Multitenancy](about-unified-context-layer/multitenancy.md) — Scope tools to different customers with `tenant_id`
- [Embedding UCL onto your AI Agent](about-unified-context-layer/embedding-ucl-onto-your-ai-agent.md) — Embed UCL into a full-stack web application
- [How UCL works in real scenarios](how-ucl-works-in-real-scenarios/) — End-to-end walkthroughs with Google Docs, Jira, and Notion
