---
description: Authenticated links between your customers and their systems.
---

# Connections

**Integrations → Connections**

<figure><img src="../.gitbook/assets/connections-list.jpg" alt="The connections table"><figcaption></figcaption></figure>

A connection is one customer's authorised link to one connector. It holds the credential — encrypted, never displayed — and records how it was obtained.

### The table

| Column        | What it tells you                                                                 |
| ------------- | ----------------------------------------------------------------------------------- |
| **Connector** | The system, with the connection's name underneath (`Default` unless you named it). |
| **Customer**  | Which customer owns it. `—` means a workspace-level connection owned by your org.  |
| **Auth**      | How it was authorised: `OAUTH`, `OAUTH_2`, `INPUT`.                                |
| **Status**    | Active, Inactive, Expired or Failed.                                               |
| **Created**   | When the customer authorised it.                                                   |

The filter chips above the table match the status values, so **Expired** and **Failed** give you a one-click triage list.

### Status, and what to do about each

| Status       | Meaning                                                       | Action                                                              |
| ------------ | ------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Active**   | Working.                                                      | Nothing.                                                            |
| **Inactive** | Exists but disabled.                                          | Re-enable from the row menu, or delete if it is genuinely finished. |
| **Expired**  | The credential ran out and could not be refreshed.            | The customer re-authorises through your widget.                     |
| **Failed**   | The last verification call was rejected — revoked access, changed password, rotated key. | Same: the customer reconnects. |

{% hint style="info" %}
Expired and Failed connections are the most common cause of "the sync stopped working". Watch them, or set an [alert](../operate/alerts.md) on broken connectors so you hear about it before your customer does.
{% endhint %}

### Auth types

**OAUTH / OAUTH\_2** — the customer signed in with the provider. fastn holds the refresh token and renews access tokens on its own. Refresh attempts, successes and failures are all recorded in the [audit log](../manage/audit-log.md).

**INPUT** — the customer pasted a key, token or connection string. These do not expire on their own but do break when rotated upstream.

### Creating a connection yourself

**New connection** is for connections your organisation owns — your own Slack workspace, your own data warehouse — wired into workflows as *workspace* rather than *per customer*.

Customer connections should be created by the customer, through your embedded widget. That is what keeps their credentials theirs.

### Row actions

The **…** menu on each row offers verify, set as default, and delete. Deleting a connection revokes the workflows' access immediately; anything running against it starts failing on the next call.
