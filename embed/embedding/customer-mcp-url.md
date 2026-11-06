---
description: "Create a one-time URL from your backend that connects a customer's AI client to fastn."
---

# Customer MCP URL

A customer MCP URL connects a customer's AI client, such as Claude or Cursor, to fastn as that customer, with no fastn account. Your customer can [generate one in the widget](../../tutorials/end-user/connecting-claude.md). This page is for creating one from your own product, for example behind a "Connect Claude" button in your settings.

## Create the URL

Call this with the customer's [embed token](token-api.md). Mint the token on your backend as usual, and always send `userId` for the person the connection is for. Without it, the token gets a random user id: the call still works, but the client sees none of that person's own connections.

```bash
curl -X POST https://api.fastn.dev/api/v1/embed/mcp-connect-codes \
  -H "Authorization: Bearer <embed token>" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The customer and user come from the token, so any `endOrgId` you send is ignored. The body must still be valid JSON.

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
| `400` | The body is not valid JSON, or a field has the wrong type. |
| `401` | The token is invalid or has expired. Embed tokens last 8 hours, so mint a fresh one. |
| `403` `EMBED_MCP_CONNECT_NO_TENANT` | The token is org-level, not tied to a customer. |
| `403` | The token is a link token, which cannot create a connection, or the call came from an origin the token does not allow. |
| `429` `EMBED_RATE_LIMITED` | Too many URLs requested. Wait and try again. |
| `503` `EMBED_MCP_CONNECT_UNAVAILABLE` | MCP connections are not available on this server. |

{% hint style="warning" %}
**The URL works once, for 10 minutes, and the lifetime cannot be changed.** Show `expiresAt` next to the URL and let the customer ask for a new one. Treat the URL like a password while it is valid.
{% endhint %}

## What happens next

1. Your customer pastes the URL into their AI client as a custom connector. [Connect Claude and other AI clients](../../tutorials/end-user/connecting-claude.md) has the steps for each client.
2. The client connects with OAuth, and fastn approves it without a sign-in screen. The URL is what authorizes it.
3. The connection stays until it is disconnected, even though the URL has expired.

Your call has already returned `201` by the time the customer pastes the URL, so a failure at this point shows only in their AI client. A used or expired URL fails, and so does any URL for a customer that is not active. Either way, offer a new URL.

## What the client can reach

The client connects to the Fastn Workspace tools and acts as that customer and that user, with the `end_user` role.

* It stays inside that customer, and it cannot see your other customers.
* It acts as one person. It uses that user's connections, so a connection another person at the customer made for themselves is not available to it.
* It can change data. A tool call runs against the customer's connected apps, including creating and updating records.
* What it can call is limited by the `end_user` role, so the list is shorter than the tools you see with your own account. To see the exact list, ask the connected client to list its tools.

## Manage connections

Call these from your backend with a key that acts for your own organization and has `connectors.read`. An embed token, or a key limited to one customer, gets an empty list and cannot disconnect.

| Task | Call |
| --- | --- |
| List one customer's connections | `GET /api/v1/embed/share-links?kind=mcp&endOrgId=<fastn customer id>` |
| Disconnect one | `DELETE /api/v1/embed/share-links/{id}` |

The list returns the newest 200 rows, including disconnected ones. Skip any row with a `revoked_at`. Leave out `endOrgId` and it spans all your customers, so always send it when you show the list to a customer. Rows do not say which person connected. Disconnecting a row that is already disconnected returns `404`.

Disconnecting ends the client's sessions and refuses its refresh token.

{% hint style="danger" %}
**Treat each row's `id` as a secret.** Keep it on your backend and do not send it to the browser. Give your settings page your own reference, and look up the `id` on the server when someone disconnects.
{% endhint %}

You can do the same in the widget builder. On the **Embed** tab, select a customer and use the **MCP** card to generate a URL, see live connections and disconnect them.

## Hide it in the widget

**Generate MCP URL** appears in the widget's header menu in a session tied to a customer. Turn it off on the [Features](../widget-builder/features.md) tab. That setting only controls the menu item: the API call above still works.
