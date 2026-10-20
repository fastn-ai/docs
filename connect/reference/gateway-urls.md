---
description: >-
  Every form of the Fastn Connect gateway URL: the root, per organisation, per
  workspace, single app, the tool picker and Fastn Workspace links.
---

# Gateway URLs

**What this page answers**

* Which URL do I give a client?
* How do I point a client at one workspace, or one app?
* Do I need `/mcp` on the end?

All MCP traffic goes to `https://mcp.fastn.dev`. The app at `https://connect.fastn.dev` never serves MCP, so a client pointed at it fails.

### The forms

| URL | Connects to |
| --- | --- |
| `https://mcp.fastn.dev` | The workspace you are currently in. People in several workspaces get a workspace picker on the consent screen. |
| `https://mcp.fastn.dev/<org>` | Your organisation's default workspace. This is the URL on Home. |
| `https://mcp.fastn.dev/<org>/<workspace>` | One named workspace. |
| `https://mcp.fastn.dev/<org>/<workspace>/<app>` | Only that app's tools. No tool picker: a signed-in member is authorised straight through. |
| `.../all` (for example `https://mcp.fastn.dev/<org>/all`) | Asks for the tool picker explicitly. |
| `https://mcp.fastn.dev/fastn-workspace` (or `/<org>/fastn-workspace`) | Only the Fastn Workspace app (the fastn platform's own tools), with no tool picker. |

`<org>` is your organisation's short name and `<workspace>` the workspace's slug. Copy them from Home rather than building them by hand.

### Trailing `/mcp`

Optional everywhere. `https://mcp.fastn.dev/<org>/mcp` and `https://mcp.fastn.dev/<org>` are the same endpoint, and `https://mcp.fastn.dev/mcp` is the same as `https://mcp.fastn.dev`.

### Links your customers use

If you embed fastn widgets in your product, a widget can give your end user a one-time link for their own AI client:

```
https://mcp.fastn.dev/fastn-workspace/c/<code>
```

It comes from **Generate MCP URL** in the widget's menu, works once, and expires after 10 minutes. The end user needs no fastn account and sees no consent screen. Their client keeps working until someone disconnects it in fastn; if it goes unused for 30 days, they generate a new URL.

Older share-link URLs of the form `/fastn-workspace/s/<id>` no longer connect a client. They show *Use a connect URL* and point the user at **Generate MCP URL**.

### Retired addresses

`connect.fastn.dev/<org>/mcp` was the gateway URL in early versions. It no longer serves MCP. Update any client still using it to `https://mcp.fastn.dev/<org>`.
