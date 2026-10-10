---
description: "What Active, Inactive, Expired and Failed mean, and what to do about each."
---

# Statuses

Every connection has one status. It shows in the **Status** column on the [Connections](README.md) page, on the connector's **Connections** tab, and as a badge on the [connection's detail page](inside-a-connection.md), where a one-line explanation sits next to it.

| Status | Meaning | What to do |
| --- | --- | --- |
| **Active** | The connection works. | Nothing. |
| **Inactive** | The connection exists but is not active. | **Reconnect** it, or **Disconnect** it if it is no longer needed. |
| **Expired** | *Authorised, but the credential has expired. Reconnecting usually clears it.* | **Reconnect**. For a customer's connection, the customer signs in again through your widget. |
| **Failed** | The credential is not accepted. | Same as Expired: sign in again. |

Use the status chips at the top of the Connections page to list only connections in one state.

{% hint style="info" %}
A workflow that runs through an Expired or Failed connection cannot reach the app. Check connection status when a sync stops, and set an [alert](../../operate/alerts.md) so you hear about a broken connection before your customer does.
{% endhint %}
