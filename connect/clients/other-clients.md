---
description: >-
  Connect Cursor, VS Code, Windsurf, Cline, Zed or any other MCP client to
  your Fastn Connect gateway, with OAuth or an access key.
---

# Cursor, VS Code, Windsurf and other clients

Every client takes the same gateway URL from **Home**:

```
https://mcp.fastn.dev/<your-org>
```

Clients that support OAuth for remote MCP servers open the Fastn Connect sign-in and consent screen on first connect, exactly as described in [Connecting AI clients](README.md#what-happens-when-someone-connects-with-oauth). Clients that do not need an **access key**: an admin creates one on the [Agents](../agents/README.md#create-an-access-key) page. Send it as `Authorization: Bearer ucl_<your-key>`.

{% hint style="warning" %}
An access key is not tied to a person. Every call made with it runs as the key, under the key's own policies. Create one key per client, name it after the client, and give it the narrowest policy that works.
{% endhint %}

### Cursor

Add the gateway in **Cursor Settings** → **MCP** → **Add new MCP server**, or edit `~/.cursor/mcp.json` (all projects) or `.cursor/mcp.json` (one project):

```json
{
  "mcpServers": {
    "fastn-connect": {
      "url": "https://mcp.fastn.dev/<your-org>"
    }
  }
}
```

Cursor shows the server as needing sign-in. Click it to open the Fastn Connect consent screen. To use a key instead, add `"headers": { "Authorization": "Bearer ucl_<your-key>" }`.

### VS Code

In `.vscode/mcp.json` (or **MCP: Add Server** from the command palette, choosing **HTTP**):

```json
{
  "servers": {
    "fastn-connect": {
      "type": "http",
      "url": "https://mcp.fastn.dev/<your-org>"
    }
  }
}
```

Start the server from the file or the **MCP** view, and sign in when prompted.

### Windsurf

Windsurf uses an access key. In `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "fastn-connect": {
      "serverUrl": "https://mcp.fastn.dev/<your-org>",
      "headers": { "Authorization": "Bearer ucl_<your-key>" }
    }
  }
}
```

Refresh the MCP servers list in Windsurf's Cascade panel.

### Cline

Cline uses an access key. Open Cline's **MCP Servers** → **Configure** and add the gateway as a remote server with the URL and an `Authorization: Bearer ucl_<your-key>` header. The **Config file** tab of the Cline tile on Home gives you the snippet.

### Zed

Zed uses the **Config file** tab of the Zed tile on Home. Add the gateway under `context_servers` in Zed's `settings.json`, with the URL and an `Authorization: Bearer ucl_<your-key>` header. Check Zed's MCP documentation for the exact keys your version expects.

### Any other MCP client

The gateway speaks standard MCP over Streamable HTTP and implements `initialize`, `tools/list` and `tools/call`. To check a key from a terminal:

```bash
curl https://mcp.fastn.dev/<your-org> \
  -H "Authorization: Bearer ucl_<your-key>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

The response lists every tool the key can reach. See the [Gateway API reference](../reference/gateway-api.md).
