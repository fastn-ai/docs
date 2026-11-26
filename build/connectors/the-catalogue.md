---
description: "The Connectors page: header buttons, categories, search, filters, connector cards, and the page guide."
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

# The catalog

**Build → Integrations → Connectors** · [Open in Fastn](https://app.fastn.dev/integrations)

The catalog lists every [connector](README.md) your workspace can use: the ones Fastn manages and the ones your workspace created. Start here when a workflow needs a new app: if the app is in the catalog, you can connect to it straight away, without building anything.

<figure><img src="../../.gitbook/assets/screens/connectors-catalog.webp" alt="The Connectors page: Request connector and Create connector buttons, a Categories list starting with All connectors 1030, a search box with All, Featured, Connected and OAuth chips and an All Visibility filter, and connector cards badged managed with a Connect button"><figcaption>The connector catalog.</figcaption></figure>

### Page header

Two buttons sit at the top right:

* **Request connector:** asks Fastn to build a connector you need. See [Request a connector](creating-a-connector.md#request-a-connector).
* **Create connector:** opens a menu with every way to add a connector: **From scratch**, **Build in your AI tool**, **Build with fastn agent** and **Import from file**. See [Ways to create a connector](creating-a-connector.md#ways-to-create-a-connector). If your role cannot create connectors, you see an **Import** button instead of this menu.

### Find a connector

| Control | What it does | URL parameter |
| --- | --- | --- |
| **Categories** (left column) | Shows one category, such as *CRM & Sales* or *Communication*. Each category shows how many connectors it holds. **All connectors** clears the category. | `category=` (for example `crm-sales`) |
| **Search connectors** | Searches the catalog by connector name. | `q=` |
| **All / Featured / Connected / OAuth** | **All** shows everything. **Featured** shows connectors Fastn marks as featured. **Connected** shows connectors with at least one active connection. **OAuth** shows connectors that offer an OAuth 2.0 method. | `view=featured`, `view=connected`, `view=oauth` |
| **All Visibility / Private / Public** | **Private** shows connectors only your workspace can see. **Public** shows connectors from the shared catalog. | `visibility=` |

Filters combine. When you search, the category counts change to show how many matches each category holds.

Because the filters are kept in the URL, you can bookmark or share a filtered view. The page number is not kept, so a shared link always opens on page one.

If nothing matches, the page shows *No connectors match these filters* and *Try another search or category.*

{% hint style="info" %}
The **Connected** and **OAuth** views can take several seconds to load the first time you open them, because the page checks each connector's connections and auth methods. The list shows *Loading...* until it is ready.
{% endhint %}

The list is split into pages, with **Previous** and **Next** below it.

### What a card shows

Each card shows:

* the connector's **icon** and **name**;
* a **badge** (see below);
* the **description**, cut to a few lines;
* an **OAuth 2.0** chip if the connector offers OAuth;
* who maintains it: *Managed by Fastn*, or *Managed by* your organization's name for a connector your workspace created;
* a button at the bottom.

The badge is one of:

* **`managed`:** maintained by Fastn.
* **`Custom`:** created in your workspace.
* **`Connected`:** at least one active connection exists. It replaces `managed` or `Custom`.
* **`Inactive`:** the connector has connections, but none is active.

The button depends on whether you have connected:

| State | Button | What it does |
| --- | --- | --- |
| Not connected | **Connect** | Opens the connect dialog for this connector. See [Connect an app](connect-an-app.md). |
| Connected | **Add another connection**, plus a chevron | **Add another connection** opens the connect dialog again so you can sign in a second account. The chevron opens a menu with **Disconnect**. |

Cards of connectors your workspace owns also have a **⋯** menu with **Select**, **Edit**, **Export**, and **Delete**; see [Import and export](importing-and-exporting.md#export-connectors) and [Edit, publish, and delete](editing-and-deleting.md).

Click a card's name to open the [connector's detail page](inside-a-connector.md).

### The page guide

The first time you open the page, a small step-by-step guide offers itself. It is headed *Page guide · 4 steps* and *New to Connectors?*, with **Not now** and **Show me**. **Show me** walks you through four steps, one at a time, each pointing at the real control on the page:

1. **Search for your app**
2. **Press Connect and sign in**: *It says Connected when it works. This signs in your own account, not your customers'.* The guide waits here and moves on by itself once the app is connected.
3. **Not there? Ask us for it**: points at **Request connector**.
4. **Manage it later in Connections**: **Take me there** opens the [Connections](../connections/README.md) page.

The guide never blocks the page; you can keep clicking while it is open. You can minimize it to a small pill and pick it up again later, or close it.
