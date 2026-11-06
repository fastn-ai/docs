---
description: "Create a one-time URL from your backend that connects a customer's AI client to fastn."
---

# Customer MCP URL

A customer MCP URL connects a customer's AI client, such as Claude or Cursor, to fastn as that customer, with no fastn account. Your customer can [generate one in the widget](../../tutorials/end-user/connecting-claude.md). This page is for creating one from your own product, for example behind a "Connect Claude" button in your settings.

## Create the URL

Call this with the customer's [embed token](token-api.md). Mint the token on your backend as usual, for the customer and the person the connection is for.

```bash
curl -X POST https://api.fastn.dev/api/v1/embed/mcp-connect-codes \
  -H "Authorization: Bearer emb_<token>" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The customer and user come from the token, so the body is ignored.

```json
{
  "data": {
    "url": "<the URL to show your customer>",
    "expiresAt": "2026-11-06T17:10:00.000Z"
  }
}
```

| Response | Means |
| --- | --- |
| `201` | The URL is in `data.url`. |
| `403` `EMBED_MCP_CONNECT_NO_TENANT` | The token is not tied to a customer and a user. |
| `403` | The token is a link token, which cannot create a connection, or lacks permission. |
| `429` `EMBED_RATE_LIMITED` | Too many URLs requested. Wait and try again. |
| `503` `EMBED_MCP_CONNECT_UNAVAILABLE` | MCP connections are not available on this server. |

{% hint style="warning" %}
**The URL works once, for 10 minutes, and the lifetime cannot be changed.** Show `expiresAt` next to the URL and let the customer ask for a new one. Treat the URL like a password while it is valid.
{% endhint %}

## What happens next

1. Your customer pastes the URL into their AI client as a custom connector. [Connect Claude and other AI clients](../../tutorials/end-user/connecting-claude.md) has the steps for each client.
2. The client connects with OAuth, and fastn approves it without a sign-in screen. The URL is what authorizes it.
3. The connection stays until it is disconnected, even though the URL has expired.

## What the client can reach

The client connects to the Fastn Workspace tools and acts as that customer and that user, with the `end_user` role.

* It reaches only that customer's data and connections, and it cannot see your other customers.
* It can change data. A tool call runs against the customer's connected apps, including creating and updating records.
* What it can call is limited by the `end_user` role, so the list is shorter than the tools you see with your own account. To see the exact list, ask the connected client to list its tools.

## Manage connections

| Task | Call |
| --- | --- |
| List a workspace's connections | `GET /api/v1/embed/share-links?kind=mcp` |
| Disconnect one | `DELETE /api/v1/embed/share-links/{id}` |

These need an API key or session with `connectors.read`. Disconnecting ends the client's sessions and refuses its refresh token.

You can do the same in the widget builder, on the **Embed** tab under **Claude (MCP)**: generate a URL for a selected customer, see live connections, and disconnect them.

## Hide it in the widget

**Generate MCP URL** appears in the widget's header menu in a session tied to a customer. Turn it off on the [Features](../widget-builder/features.md) tab. That setting only controls the menu item: the API call above still works.
