---
description: "What Active, Inactive, Expired and Failed mean, and what to do about each."
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

# Statuses

Every connection has one status. It shows in the **Status** column on the [Connections](README.md) page, on the connector's **Connections** tab, and as a badge on the [connection's detail page](inside-a-connection.md), where a one-line explanation sits next to it.

| Status | Meaning | What to do |
| --- | --- | --- |
| **Active** | The connection works. On the detail page, one that has never been used reads *Authorized, but nothing has called it yet.* | Nothing. |
| **Inactive** | *Stored but idle. Nothing is calling it at the moment.* | **Reconnect** it, or **Disconnect** it if it is no longer needed. |
| **Expired** | *Authorized, but the credential has expired. Reconnecting usually clears it.* | **Reconnect**. For a customer's connection, the customer signs in again through your widget. |
| **Failed** | *Not working. The credential was rejected, so calls are failing.* | Same as Expired: sign in again. |

Use the status chips at the top of the Connections page to list only connections in one state. The **Needs action** chip lists every connection that needs someone to act: those that are not active, and active ones that can no longer renew their token.

{% hint style="info" %}
A workflow that runs through an Expired or Failed connection cannot reach the app. Check connection status when a sync stops, and set an [alert](../../operate/alerts.md) so you hear about a broken connection before your customer does.
{% endhint %}
