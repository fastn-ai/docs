---
description: "What Active, Inactive, Expired and Failed mean, and what to do about each."
---

# Statuses

Every connection has one status. It shows in the **Status** column on the [Connections](README.md) page, on the connector's **Connections** tab, and as a badge on the [connection's detail page](inside-a-connection.md), where a one-line explanation sits next to it.

| Status | Meaning | What to do |
| --- | --- | --- |
| **Active** | The connection works. | Nothing. |
| **Inactive** | The connection exists but is switched off. | **Reconnect** it, or **Disconnect** it if it is no longer needed. |
| **Expired** | *Authorised, but the credential has expired. Reconnecting usually clears it.* fastn could not renew the token in time. | **Reconnect**. For a customer's connection, the customer signs in again through your widget. |
| **Failed** | The app rejected the credential: access was revoked, the password changed or the key was rotated. | Same as Expired: sign in again. |

Use the status chips at the top of the Connections page to list only connections in one state.

{% hint style="info" %}
Expired and Failed connections are the most common reason a sync stops working. Check them first, and set an [alert](../../operate/alerts.md) so you hear about a broken connection before your customer does.
{% endhint %}
