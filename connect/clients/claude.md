---
description: >-
  Add your Fastn Connect gateway to Claude (claude.ai, Claude Desktop or
  Claude Code) as a custom connector, sign in, and use your tools in a chat.
---

# Claude

**You need:** your gateway URL from **Home** (`https://mcp.fastn.dev/<your-org>`) and a Claude plan that allows custom connectors.

{% hint style="info" %}
**Building fastn integrations from Claude instead?** That uses a different URL, `https://mcp.fastn.dev/fastn-workspace`. See [Claude under MCP gateway](../../build/mcp-gateway/claude.md).
{% endhint %}

### Add the connector (claude.ai and Claude Desktop)

Claude Desktop uses the same connectors as claude.ai, so you only add it once.

1. In Fastn Connect, on **Home**, click **Add to Claude** (or the **Claude Desktop** tile under **Connect a client**) and copy the **Gateway URL**.
2. In Claude, open **Customize** → **Connectors** and click **Add custom connector**.
3. Enter a **Name** (for example `Fastn Connect`) and paste the gateway URL as the **MCP server URL**. Click **Add**.
4. Click **Connect** on the new connector. A browser tab opens on Fastn Connect.
5. Click **Continue with fastn** and sign in with your work account.
6. On **Choose what Claude can reach**, pick the apps and tools Claude may use, then click **Authorize Claude**.

<figure><img src="../../.gitbook/assets/connect-consent.webp" alt="The Choose what Claude can reach page: Signed in as an address with a Not you link, Search apps and tools, apps with N of M tool counts, Select all, Reads only and Clear, a tools selected count, and an Authorize Claude button"><figcaption>Choose what Claude can reach. Fewer tools means Claude picks the right one faster.</figcaption></figure>

The tab returns you to Claude and the connector shows as connected.

{% hint style="info" %}
**Claude Team and Enterprise.** Only an organisation owner can add a custom connector. Once the owner has added the gateway URL for the whole organisation, each member opens the connector and clicks **Connect** to sign in as themselves. Everyone shares the URL; nobody shares an account.
{% endhint %}

<figure><img src="../../.gitbook/assets/mcp-claude-team-owner-only.png" alt="Claude's Add custom connector option greyed out, with the note Ask an organization owner to add this for your team"><figcaption>What a Team or Enterprise member sees in place of <strong>Add custom connector</strong>.</figcaption></figure>

If you belong to more than one Claude workspace (Personal and a Team, say), add the connector in the one you chat in. A connector only shows in the workspace it was added to.

### Use it in a chat

1. In a new chat, click **+** → **Connectors** and switch the connector on.
2. Ask for an outcome, naming the app if it helps: *"Summarise the open Linear issues assigned to me."*
3. Claude asks before each tool call: **Allow once**, **Always allow** or **Deny**.

<figure><img src="../../.gitbook/assets/mcp-claude-chat-connectors.png" alt="Claude's chat + menu open on Connectors, with the connector switched on"><figcaption>Switch the connector on for the chat.</figcaption></figure>

If a tool needs your own account and you have not connected it yet, Claude shows a **Connect {app}** link. Open it, sign in to the app, and ask again. See [the connect link](../tools/sign-in-modes.md#each-person-signs-in-the-connect-link).

### Claude Code

Add the gateway as a remote HTTP server, then sign in when Claude Code prompts you (run `/mcp` inside Claude Code to authenticate):

```bash
claude mcp add --transport http fastn-connect https://mcp.fastn.dev/<your-org>
```

To use an access key instead of signing in, pass it as a header:

```bash
claude mcp add --transport http fastn-connect https://mcp.fastn.dev/<your-org> --header "Authorization: Bearer ucl_<your-key>"
```

### Claude Desktop config file

Claude Desktop's `claude_desktop_config.json` starts local servers only. To use the file instead of **Connectors**, bridge to the gateway with `mcp-remote`:

```json
{
  "mcpServers": {
    "fastn-connect": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.fastn.dev/<your-org>"]
    }
  }
}
```

Restart Claude Desktop. `mcp-remote` opens the same Fastn Connect sign-in in your browser the first time.

### Change what Claude can reach

Disconnect and reconnect the connector in Claude, and pick again on the consent screen. An admin can also cut Claude off for you under **Connections** → **MCP clients** → **Revoke**.
