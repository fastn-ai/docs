---
description: Authenticated links between your customers and their systems.
---

# Connections

**Integrations → Connections** · `/integrations?tab=connections`

![The connections table](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/connections-list.jpg)

A connection is one customer's authorised link to one connector. It holds the credential — encrypted, never displayed — and records how it was obtained.

### How connections work

A connection is an authenticated link between one of your customers and one connector — the stored, encrypted result of that customer authorising access once, which every later API call reuses so nobody signs in again. A few properties are worth holding in mind before the detail below:

* **Who it belongs to — Scope.** Most connections belong to a single customer (one tenant). Some belong to your organisation instead: those read `Account level` on the detail page, meaning the link is shared across the workspace rather than tied to one customer.
* **How you address it — the connection ID.** Every connection has an id of the form `ucl:org_<org>:<env>:<connectorId>:<authId>:<tenant>`. You pass it to the API to act as that customer, and it is what routes a call to the right credential.
* **Whether it still works — Status.** A connection is `Active`, `Inactive`, `Expired` or `Failed`. Active needs nothing; the other three need attention.
* **Fixing or ending one — Reconnect / Disconnect.** Every row's `⋯` menu offers **Reconnect** (re-run authorisation to restore a broken link) and **Disconnect** (syncing stops and the credential is deleted).
* **Making one yourself — the picker.** **New connection** opens the full-screen **Connect a system** picker; customer connections should instead come through your embedded widget.

The rest of this page is the detail behind each of those.

### The table

| Column        | What it tells you                                   |
| ------------- | --------------------------------------------------- |
| **Connector** | The system, with the tenant key on the second line. |
| **Customer**  | Which customer owns it.                             |
| **Auth**      | How it was authorised.                              |
| **Status**    | Active, Inactive, Expired or Failed.                |
| **Created**   | When the customer authorised it.                    |
| **⋯**         | **Reconnect** and **Disconnect**.                   |

The table pages at 10 rows. Filter chips above it — **All**, **Active**, **Inactive**, **Expired**, **Failed** — are not kept in the URL, so a filtered view cannot be linked.

{% hint style="warning" %}
The `Active`, `Inactive`, `Expired` and `Failed` chips currently return nothing, even when every row in the unfiltered table shows `Active`. Until that is fixed, triage from the full list rather than the chips.
{% endhint %}

### Status, and what to do about each

| Status       | Meaning                                                                                  | Action                                                                          |
| ------------ | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Active**   | Working.                                                                                 | Nothing.                                                                        |
| **Inactive** | Exists but disabled.                                                                     | **Reconnect** from the row menu, or **Disconnect** if it is genuinely finished. |
| **Expired**  | The credential ran out and could not be refreshed.                                       | The customer re-authorises through your widget.                                 |
| **Failed**   | The last verification call was rejected — revoked access, changed password, rotated key. | Same: the customer reconnects.                                                  |

{% hint style="info" %}
Expired and Failed connections are the most common cause of "the sync stopped working". Watch them, or set an [alert](../operate/alerts.md) on broken connectors so you hear about it before your customer does.
{% endhint %}

### Auth types

The `Auth` column mixes display names and raw enum values for the same concepts — you will see `OAuth 2.0` and `OAUTH` for one, `Custom` and `INPUT` for the other. They are the same two shapes:

**OAuth** — the customer signed in with the provider. fastn holds the refresh token and renews access tokens on its own. Whether that is still working is visible on the connection's detail page, under **Token and activity**.

**Custom / INPUT** — the customer pasted a key, token or connection string. These do not expire on their own but do break when rotated upstream.

### Inside a connection

Opening a row gives four sections.

**Connection** — `Customer`, `Connector`, `Auth method`, `Scope` and `Connection ID`. Scope reads `Account level` when the connection is shared across the workspace rather than belonging to one customer. The connection id has the form:

```
ucl:org_<org>:<env>:<connectorId>:<authId>:<tenant>
```

The page's own note on it is the operative one:

> Pass this to the API to act as this customer.

**Token and activity** — `Expires`, `Last refreshed`, `Last used`, `Created`, `Updated`. This is where you check whether a refresh is still succeeding.

**Recent activity** — the last calls made on this connection, with **View all** into [Activity](../operate/).

**Danger zone** — **Disconnect this customer**:

> Syncing stops immediately and the credential is deleted.

### Creating a connection yourself

**New connection** opens a full-screen **Connect a system** picker: a **Search systems** box, an A–Z index, a counter reading `236 of 236 systems`, and one row per connector showing its auth-method label.

Use it for connections your organisation owns — your own Slack workspace, your own data warehouse — which a workflow then uses at account level rather than per customer.

Customer connections should be created by the customer, through your embedded widget. That is what keeps their credentials theirs.
