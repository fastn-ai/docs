---
description: "The connection detail page: who and what the connection is, its connection ID, its token and activity, Reconnect, and Disconnect."
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Inside a connection

**Operate → Connections** → select a connection · [Open in Fastn](https://app.fastn.dev/connections)

Each connection has its own detail page. Open it to see whose account the connection is, whether its credential still works, which calls have used it, and to repair or remove it. Its address is `/integrations/connections/<connection-id>`.

{% hint style="info" %}
**Do this from your AI tool.** Fastn recommends connecting your preferred AI agent, such as Claude, Cursor or VS Code, to the [Fastn MCP server](../mcp-gateway/README.md) and using its tools to check, update and remove connections. For example, ask it: *"Check whether my HubSpot connection still works."* To connect your AI agent, see [Connect your AI tool](../mcp-gateway/README.md#open-the-connect-dialog), or the setup guide for [Claude](../mcp-gateway/claude.md), [Claude Code](../mcp-gateway/claude-code.md), [Cursor](../mcp-gateway/cursor.md), [VS Code](../mcp-gateway/vscode.md) or [any other MCP client](../mcp-gateway/README.md#how-your-ai-tool-connects).
{% endhint %}

### Header

The header shows:

* **Name:** the connector's name and icon, and the connection's name, for example `Default`.
* **Status:** the status badge and a one-line explanation, for example *Authorized, but the credential has expired. Reconnecting usually clears it.* See [Statuses](statuses.md).
* **Reconnect:** top right. Repairs the connection. See [Reconnect](#reconnect).
* **←** (**Back to connections**): returns to the list.

### Connection

| Field | Meaning |
| --- | --- |
| **Customer** | *The customer this credential belongs to.* For your own connections, this is your organization. |
| **Connector** | *Opens the connector this connection uses.* Select it to go to the [connector detail page](../connectors/inside-a-connector.md). |
| **Auth method** | How the connection was authorized, for example **OAuth 2.0** (*Your customer signed in and approved access.*) or a key-based method (*Your customer supplied a credential themselves.*). See [Auth types](auth-types.md). |
| **Scope** | **Account level** (*Shared across your whole workspace rather than one project.*), or the workspace the connection is limited to (*Limited to this workspace.*). |
| **Connection scope** | Shown only when the credential was stored under a connector scope: *The SaaS-connector scope this credential was stored under.* |
| **Connection ID** | *Pass this to the API to act as this customer.* The copy button copies it. See [The connection ID](#the-connection-id). |
| **Usable in** | Only on your own organization's connections: the environments whose workflow runs may use it. *Workflow runs in any other environment are refused before they call the app.* |

#### The connection ID

The connection ID identifies one connection. You pass it to the API to act as that account. It has this form:

```
ucl:<workspace>:<customer or default>:<connectorId>:<identity>[:<account>]
```

Every connection ID starts with `ucl:`. The parts after it, separated by colons, are:

* **Workspace:** your workspace.
* **Customer:** the customer the connection belongs to, or `default` when it belongs to your own organization.
* **Connector ID:** the ID of the connector the connection uses.
* **Identity:** an identity for the credential.
* **Account:** an account. This part is optional.

For more on how customers appear in connection IDs, see [Customers](../../operate/customers.md#customers-in-connection-ids).

### Token and activity

| Field | Meaning |
| --- | --- |
| **Expires** | How long until the current credential expires, with the date (for example *3 days* and the date). *fastn renews this automatically before it runs out.* Once the date has passed, it reads *Expired* with the date. For connections that are not OAuth, it reads *Not applicable*; for an OAuth token with no expiry, *Does not expire*. |
| **Last refreshed** | *The last time fastn renewed this credential.* |
| **Last used** | When a call last went through this connection, or *Never*. |
| **Created** | *When your customer authorized it.* |
| **Updated** | *The last change to this connection record.* |

Use this panel to tell whether token refresh is still working. An **Expires** date in the past together with an old **Last refreshed** date usually means Fastn could not renew the token, and the account has to sign in again.

### Recent activity

The latest calls made through this connection. **View all** opens [Logs](../../operate/README.md) on its **Events** tab, which is not filtered to this connection. Until something has run, it reads *Nothing has come through this connection yet. Calls appear here as soon as your customer starts using it.*

### Reconnect

**Reconnect** runs the sign-in again for the same connector and replaces the stored credential. Use it for `Expired` and `Failed` connections, or after the account's password or key changed.

You'll find **Reconnect** in two places: in the header of this page, and in the row's **⋯** menu on the [Connections](README.md) page, alongside **Rename** and **Disconnect**.

### Disconnect

The last panel, **Disconnect this customer**, reads:

> Syncing stops immediately and the credential is deleted. Anything running against this connection stops working until it is connected again.

{% hint style="warning" %}
**Disconnect** deletes the stored credential and cannot be undone. Workflows and triggers that use the connection stop working until someone connects the app again. To fix a broken connection, use **Reconnect** instead.
{% endhint %}

**Disconnect** asks you to confirm first (*This cannot be undone.*). Confirm only when the connection is no longer needed.
