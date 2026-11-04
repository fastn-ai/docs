---
description: "The connector detail page: the connector rail, the header, and the Overview, Connections and Version pins tabs."
---

# Inside a connector

`/integrations/connectors/<slug>`. Click a connector's name in the catalog to open it.

<figure><img src="../../.gitbook/assets/connector-detail-overview.webp" alt="The HubSpot connector detail page: on the left the connector rail with HubSpot expanded to its 162 actions, each with a method chip such as PUT or DELETE and a checkbox; on the right the header HubSpot, Fastn · OAuth 2.0, a v1.0 · Test chip, a Disconnect button and a three-dot menu, the tabs Overview, Auth, Connections, Version pins and Webhook config, and the Overview tab with tiles 1 Connection, 1 Auth method and v1.0 Current version above a Details table"><figcaption>The detail page has two panes: the connector rail on the left and the selected connector on the right.</figcaption></figure>

### The connector rail (left)

* **←** (Back to all connectors) returns to the catalog.
* **+** (Create a connector) opens the [Create a connector](creating-a-connector.md) dialog.
* **Search connectors** filters the rail.
* Every connector is listed with its icon. The open connector is expanded: it shows its action count, a green dot if it is connected, and a chevron that collapses or expands its action list.
* Under it, **Select all** and one row per action, each with a checkbox and a method chip (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`). Click an action to open it in the [action editor](action-detail.md). Tick actions to export them; see [Importing and exporting](importing-and-exporting.md).

### The header

| Element | Meaning |
| --- | --- |
| **Name** and icon | The connector. |
| `<owner> · <auth types>` | Who maintains it (*Fastn* for managed connectors, your organization's name for connectors you own) and all of its auth methods, comma separated, for example `Fastn · OAuth 2.0` or `Fastn · OAuth 2.0, API key`. |
| Version chip, for example `v1.0 · Test` | The connector's current version and whether that version is in **Test** or **Live**. |
| **Publish** | Shown on a connector your workspace owns while its version is in **Test**. Publishes the version to **Live**; see [Editing, publishing and deleting](editing-and-deleting.md#publish-a-version). |
| **Connect** or **Disconnect** | **Connect** opens the connect dialog. Once you are connected it changes to **Disconnect**, which removes your connection after a confirmation. |
| **⋯** (More actions) | On a managed connector you are connected to: **Disconnect**. On a connector your workspace owns: **Edit** and **Delete**; see [Editing, publishing and deleting](editing-and-deleting.md). |

Below the header are five tabs: **Overview**, **Auth**, **Connections**, **Version pins** and **Webhook config**. **Auth** is covered in [Auth methods and providers](auth-methods.md) and **Webhook config** in [Webhook config](webhook-config.md).

### Overview

The connector's description, then three tiles:

| Tile | Shows |
| --- | --- |
| **Connection(s)** | How many connections use this connector (*Customers using this connector*). |
| **Auth method(s)** | How many auth methods it offers, and which is the default, for example *OAuth 2.0, set as default*. |
| **Current version** | The current version, and *In test, not published* or the live state. |

Then a **Details** table:

| Field | Meaning |
| --- | --- |
| **Slug** | *Used in the API path and in code.* |
| **Visibility** | **Private**: *Only your organization can see it.* **Public**: *Customers under your organization can use it when Catalog connectors is on. Other organizations never see it.* |
| **Auth methods** | *What your customers authorise with.* |
| **Created** | When the connector was added. |

#### Versions

Every saved change to a connector creates a version. The **Versions** section lists the five most recent, newest first, with a note such as *Initial version* or *Auto-versioned on update* and the date.

* **Test** lists versions that are still being tested. Customers do not run them.
* **Live** lists published versions, the ones customers run.

If a list is empty it reads *No test versions yet.* (or the live equivalent). On a connector your workspace owns, each test version also has a **Publish to live** button; see [Editing, publishing and deleting](editing-and-deleting.md#publish-a-version).

### Connections

> Every customer who has authorised this connector. Make one yourself to test the flow end to end.

| Column | Meaning |
| --- | --- |
| **Name** | The connection's name (`default` unless it was named), with its connection ID underneath. |
| **Status** | `Active`, or the connection's stored status as-is for anything else, for example `INACTIVE`. See [Statuses](../connections/statuses.md). |
| **Default** | Marks the connection that is set as the default for this connector. |
| 🗑 | Disconnects that connection. |

**Connect** adds a connection. Before anyone has connected, the tab reads *Nobody has connected yet* with a **Connect &lt;connector&gt;** button:

This tab shows the same connections as the workspace-wide [Connections](../connections/README.md) page, limited to one connector.

### Version pins

> Hold one customer on one version while everyone else moves on. A version set in code still wins over a pin.

A pin keeps one customer on an older version of an action while every other customer moves to the new one. Use it when a customer cannot take a change yet, for example because a field they depend on moved. Remove the pin when they are ready.

The second sentence matters: a pin is a fallback. If a workflow asks for a specific version in its code, that version is used, pin or not.

Pins work on actions that have an external version (`externalVersion`), which you create in the action editor with **New version → New external version** (see [Actions](action-detail.md#versions)). Until a connector has such actions, the tab reads *No versioned actions yet* · *Add actions with an externalVersion to enable per-customer routing.*

**Compare two versions** shows what changed in an action's contract between two versions before you upgrade or deprecate:

| Field | What to enter |
| --- | --- |
| **Action** | The action to compare, picked from a searchable list (*Select an action*). |
| **From** / **To** | The two provider versions. |
| **From major** / **To major** | The internal major versions (`Default` or `major 1`, `major 2` and so on). |

**Compare** shows the difference.
