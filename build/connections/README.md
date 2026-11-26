---
description: "The Connections page: your organization's and your customers' signed-in accounts, how to find one, and what each column means."
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

# Connections

**Operate → Connections** · [Open in Fastn](https://app.fastn.dev/connections)

A **connection** is one signed-in account on one [connector](../connectors/README.md). It is created when someone on your team or one of your customers authorizes access to an app. Fastn stores the credential encrypted and reuses it on every later call, so nobody has to sign in again. Workflows act through connections.

For example, when Acme, one of your customers, signs in to its HubSpot account through your widget, Fastn creates a connection on the HubSpot connector that belongs to Acme. Your workflows then read and write Acme's HubSpot data through that connection.

The connector is the definition of the app. The connection is a signed-in account on it. One connector can have many connections, for example one for your organization and one for each customer who connects.

### How connections work

* **Owner:** A connection belongs either to your organization (made by someone on your team) or to one of your customers (made through your embedded widget). This page shows the two in separate views.
* **Status:** Each connection is `Active`, `Inactive`, `Expired` or `Failed`, which tells you whether it still works. See [Statuses](statuses.md).
* **Token refresh:** For OAuth connections, Fastn refreshes the access token before it runs out.
* **Connection ID:** Each connection has an ID that you pass to the API to act as that account. See [Inside a connection](inside-a-connection.md#connection).
* **Repair and removal:** **Reconnect** signs in again to repair a broken connection, **Rename** changes its name, and **Disconnect** stops all syncing and deletes the credential. See [Inside a connection](inside-a-connection.md).

### My organization and Customers

The toggle at the top switches between two views.

<figure><img src="../../.gitbook/assets/screens/connections-customers-empty.webp" alt="Operate, Connections, Customers tab with no connections yet: search, an All customers filter, status chips All, Active, Inactive, Expired, Failed and Needs action, and the message No customer connections yet with View your own connections"><figcaption>The <strong>Customers</strong> tab before any customer has connected an app.</figcaption></figure>

| View | Shows | Page subtitle |
| --- | --- | --- |
| **My organization** | Connections your team made. | *Connections your organization holds on its connectors. Workflows act through them.* |
| **Customers** | Connections your customers made through the widget, across every customer. | *Connections your customers have made on your connectors, across every customer.* |

The **Customers** view adds an **All customers** selector to show one customer's connections, and a **Customer** column in the table.

### Find a connection

* **Search connections:** matches the connector and connection name. In the **Customers** view the box reads **Search by customer, connector or name** and also matches customer names.
* **Status chips:** **All**, **Active**, **Inactive**, **Expired**, **Failed** and **Needs action** show only the connections in that state. See [Statuses](statuses.md#find-connections-by-status) for what **Needs action** collects.
* **Count:** the number on the right shows how many connections match, for example *5 connections*.

If connections exist but none match, the page reads *No connections match* · *Adjust the filter, or pick the other view.* When there are no connections at all, the **My organization** view reads *No connections yet* with a button to connect one, and the **Customers** view reads *No customer connections yet* and explains that customers connect their own apps through the widget you embed.

### The table

| Column | Meaning |
| --- | --- |
| **Connector** | The app, with the connection's name underneath (`Default` unless it was named). |
| **Customer** | Only in the **Customers** view: the customer the connection belongs to. |
| **Auth** | The auth type the connection was made with, as a display label: for example **OAuth 2.0**, **Bearer token**, **Custom**. See [Auth types](auth-types.md). |
| **Status** | `Active`, `Inactive`, `Expired` or `Failed`. See [Statuses](statuses.md). |
| **Created** | When the connection was made. |
| **⋯** | **Reconnect**, **Set as default** (on an active connection that is not already the default), **Rename**, and **Disconnect**. |

Select a row to open its detail page. See [Inside a connection](inside-a-connection.md).

**New connection** (top right) connects a new app for your organization. See [Create a connection](creating-a-connection.md).

### In this section

* [Create a connection](creating-a-connection.md): connect an app for your organization with **New connection**.
* [Inside a connection](inside-a-connection.md): the detail page, the connection ID, **Reconnect** and **Disconnect**.
* [Statuses](statuses.md): what each status means and what to do about it.
* [Auth types](auth-types.md): the values in the **Auth** column.
