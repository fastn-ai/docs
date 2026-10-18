---
description: >-
  Connect AI assistants to Fastn's MCP server i.e. native tools, dynamic tools,
  per-customer scoping, and integration patterns.
hidden: true
---

# MCP Gateway Integration

**Prerequisites:** Understanding of the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). A Fastn project with at least one configured connector.

Fastn implements an MCP server that exposes your integrations as tools for AI assistants. Any MCP-compatible client Claude Desktop, custom agents, or your own AI features can discover and invoke these tools.

### What the MCP gateway provides

#### Native tools

Six built-in tools are always available:

| Tool                           | What it does                                      |
| ------------------------------ | ------------------------------------------------- |
| `fastn_list_integrations`      | List all active integrations for a customer       |
| `fastn_get_integration_status` | Get detailed status of a specific integration     |
| `fastn_create_flow`            | Create a new automation flow from a specification |
| `fastn_get_event_history`      | Retrieve recent events for a customer             |
| `fastn_get_usage_summary`      | Get quota usage summary                           |
| `fastn_search_entities`        | Search CDM entities across integrations           |

#### Dynamic tools

In addition to the native tools, the gateway auto-generates tools from your connector capabilities. If a customer has Slack and Shopify connected, the gateway exposes tools like:

* `slack_send_message`
* `slack_list_channels`
* `shopify_list_orders`
* `shopify_get_customer`

Dynamic tools are scoped per tenant — a customer who only connected Slack will only see Slack tools. A tenant with Slack and Shopify sees both.

### Connecting to the MCP server

#### MCP server URL

`mcp.ucl.dev` no longer resolves. The dashboard's **Connect an agent** dialog gives you the current URL for your workspace, with a **Copy** button beside it. [MCP gateway](../../build/mcp-gateway.md) covers that dialog, the one-click Claude install and the API key in one place, so the examples below write it as `YOUR_FASTN_MCP_URL` rather than keeping a second copy here.

Two things changed with the host, and both matter for the samples:

* **The URL carries no credentials.** The server advertises `bearer_methods_supported: ["header"]` at `/.well-known/oauth-protected-resource`, so the key goes in an `Authorization` header and nowhere else. The old `?id=&api_key=&space_id=` form is gone.
* **The path is what selects the workspace**, in the form `mcp.<zone>/<org>[/<workspace>]`, which is the job `space_id` used to do. Which customers a key may reach on top of that is set on the key itself, under *Customers it can reach*.

#### Claude Desktop configuration

Claude adds a remote MCP server under **Customize → Connectors → Add custom connector**, not through `claude_desktop_config.json`. Paste the URL there; the same dialog takes a fixed request header, which is where `Authorization: Bearer fsk_live_<your-key>` goes.

`claude_desktop_config.json` runs local commands, so the file form of the same thing proxies through `mcp-remote`:

```json
{
  "mcpServers": {
    "fastn": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "YOUR_FASTN_MCP_URL"]
    }
  }
}
```

Either way, Claude can then discover and invoke Fastn tools directly in conversation.

> **Screenshot:** Claude Desktop with Fastn MCP tools visible in the tool list and showing both native and dynamic tools.

#### Programmatic integration

For custom AI applications, connect to the MCP server using any MCP client library:

```typescript
// Example using the MCP SDK
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const client = new Client({
  name: 'my-ai-app',
  version: '1.0.0'
});

// Connect to Fastn's MCP server. connect() takes a transport, and the key
// rides on the transport's request headers.
const transport = new StreamableHTTPClientTransport(new URL('YOUR_FASTN_MCP_URL'), {
  requestInit: {
    headers: { Authorization: `Bearer ${process.env.FASTN_API_KEY}` }
  }
});
await client.connect(transport);

// List available tools
const tools = await client.listTools();
console.log(tools);
// Returns: fastn_list_integrations, fastn_search_entities, slack_send_message, ...

// Invoke a tool
const result = await client.callTool({
  name: 'fastn_list_integrations',
  arguments: { tenant_id: 'acme-corp' }
});
```

#### Using with the Anthropic API

If you're building with Claude via the API, pass the MCP server in your request:

```javascript
const response = await fetch("https://api.anthropic.com/v1/messages", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": process.env.ANTHROPIC_API_KEY,
    "anthropic-version": "2023-06-01",
    // The MCP connector is in beta and the request is rejected without this.
    "anthropic-beta": "mcp-client-2025-11-20"
  },
  body: JSON.stringify({
    model: "claude-sonnet-5-5",
    max_tokens: 1000,
    messages: [
      { role: "user", content: "List all active integrations for tenant acme-corp" }
    ],
    mcp_servers: [
      {
        type: "url",
        url: "YOUR_FASTN_MCP_URL",
        name: "fastn",
        authorization_token: process.env.FASTN_API_KEY
      }
    ],
    // mcp_servers alone fails validation: each server also needs a toolset entry.
    tools: [
      { type: "mcp_toolset", mcp_server_name: "fastn" }
    ]
  })
});
```

An `mcp_servers` entry takes only `type`, `url`, `name` and `authorization_token`, with no field for extra headers. A Fastn **test** key is refused without `X-fastn-Test-Mode: true`, so this path needs a live key. Clients that can set their own headers, such as the Connectors dialog and the SDK transport above, can use either.

> **Screenshot:** API response showing Claude using a Fastn MCP tool and returning integration data.

### Per-customer tool scoping

This is what makes Fastn's MCP gateway multi-customer-aware. When an AI assistant invokes a tool, the gateway:

1. Identifies the customer from the request context
2. Checks which connectors the customer has active
3. Only exposes tools for the customer's connected apps
4. Executes the tool using the customer's credentials

Customer A (connected: Slack, Shopify) sees:

```
fastn_list_integrations, fastn_search_entities, ...,
slack_send_message, slack_list_channels,
shopify_list_orders, shopify_get_customer
```

Customer B (connected: Slack only) sees:

```
fastn_list_integrations, fastn_search_entities, ...,
slack_send_message, slack_list_channels
```

No Shopify tools appear for Customer B because they haven't connected Shopify.

### Resource listing

The MCP gateway also implements the MCP resource protocol, allowing AI assistants to discover available data:

```typescript
// List available resources
const resources = await client.listResources();
// Returns: integrations, entities, events, usage data
```

Resources provide read access to data without executing actions — useful for AI assistants that need to answer questions about a customer's integration state.

### Integration patterns

#### Pattern 1: AI-powered support

Your support team uses Claude Desktop with Fastn MCP tools. When a customer reports an issue, the agent can:

1. Look up the customer's integrations (`fastn_list_integrations`)
2. Check integration status (`fastn_get_integration_status`)
3. Search for related entities (`fastn_search_entities`)
4. View recent events (`fastn_get_event_history`)

#### Pattern 2: In-product AI assistant

Your SaaS product has an AI chat feature. You connect it to Fastn via MCP so users can:

* "Show me my recent Shopify orders" → `shopify_list_orders`
* "Send a summary to my Slack channel" → `slack_send_message`
* "What integrations do I have active?" → `fastn_list_integrations`

#### Pattern 3: Automated operations

A monitoring agent runs on a schedule, uses MCP tools to check integration health, and creates alerts when something fails:

* Check all customers' integration status
* Query event history for failures
* Review usage against quotas
* Create notifications for the ops team

### What you've learned

* The 6 native MCP tools and how dynamic tools are generated from connectors
* How to connect Claude Desktop, custom apps, and the Anthropic API to Fastn's MCP server
* How per-customer tool scoping works
* Three integration patterns for real-world use
