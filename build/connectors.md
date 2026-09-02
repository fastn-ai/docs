---
description: Every system your customers can authorise — managed, imported or built by you.
---

# Connectors

**Integrations → Connectors** · `/integrations?tab=connectors`

<figure><img src="../.gitbook/assets/connectors-list.jpg" alt="The connector catalogue"><figcaption></figcaption></figure>

A connector is the definition of one external system: its actions, its authentication methods, its webhook configuration and its versions. It is not a credential — that is a [connection](connections.md).

### The catalogue

The page header states the intent plainly:

> Every system your customers can authorise. Depth on the ones that block deals, not a catalogue count.

Connectors marked **managed** are maintained by fastn — when the vendor ships a breaking change, you get a proposal under [Pending updates](connector-updates.md) rather than a broken sync. Ones you build yourself are badged **Custom**. Either badge is replaced by **Connected** once at least one connection exists.

| Control            | What it filters                                          | URL              |
| ------------------ | ---------------------------------------------------------- | ---------------- |
| **Search connectors** | Name and description                                   | `?q=`            |
| **All / Connected / OAuth** | Everything · at least one live connection · offers OAuth 2.0 | `?category=` |
| **All Visibility** | `All Visibility`, `Private`, `Public`                     | `?visibility=`   |

There is no sort control. The list pages at 24 per page with a footer reading `1–24 of 236`; the page number is not kept in the URL, so a deep link always lands on page one.

A search that matches nothing shows `No connectors match "x"`, *Try another search or category.* and a **Clear search** button.

**Card anatomy.** Favicon, name, badge, description, an `OAuth 2.0` chip where it applies, and a provenance string. The footer button reads **Connect**, or **Add another connection** with a chevron offering **Reconnect** and **Disconnect**. The `⋯` menu holds **Select**, **Edit**, **Export** and **Delete**.

**Header controls.** **Create connector** opens the create dialog. **Import** is a bare file input — it takes a JSON connector definition with no intermediate dialog. Selecting cards (via `⋯ → Select`) reveals **Export Selected (n)**.

{% hint style="warning" %}
Three things about this list are known to mislead, and are worth knowing before you count anything:

* The catalogue contains duplicates — Asana, HubSpot, Salesforce, Slack, Notion and Cin7 Core each appear twice, once `managed` and once `Custom` — so the total is not a count of distinct systems.
* A connector badged `Connected` in the list can still report `0 connections` on its own detail page.
* Provenance is written three different ways for the same thing: *Managed by Fastn*, *Managed by fastn.ai* and *Managed by fastn*.
{% endhint %}

### Inside a connector

`/integrations/connectors/<slug>`. Three panes: the connector list on the left, that connector's actions in the middle, and the detail tabs on the right.

* **Left** — **Back to all connectors**, **Create a connector**, a search box, and the connector list with `<Name> operations` expanders. Connectors your org owns also get **Add action**.
* **Middle** — the action list, each with a method chip (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`), plus **Select all**. Selecting actions is how you scope what a workflow or an agent may use — the point of *read-only Jira for one customer, nothing beyond that*.
* **Right** — the connector name, a `<owner> · <auth type>` line, a version chip such as `v1.0 · Test`, a **Connect** button, and a `⋯` menu with **Edit** and **Delete**. Below that, five tabs.

<figure><img src="../.gitbook/assets/connector-detail-overview.jpg" alt="A connector's overview tab"><figcaption>The Overview tab: connections, auth methods, current version.</figcaption></figure>

#### Overview

Three tiles — **Connections**, **Auth method(s)**, **Current version** — and a details table.

| Field            | Meaning                                                                       |
| ---------------- | ------------------------------------------------------------------------------- |
| **Slug**         | The identifier used in API paths and in workflow code.                         |
| **Visibility**   | Private or Public. New connectors start Private; publishing publicly is a platform-admin action. |
| **Auth methods** | What your customers authorise with.                                            |
| **Created**      | When it entered the catalogue.                                                 |

A **Versions** section underneath carries a `Test` / `Live` toggle and a **Publish to live** control.

#### Auth

<figure><img src="../.gitbook/assets/connector-auth-tab.jpg" alt="A connector's authentication methods"><figcaption></figcaption></figure>

One row per authentication method, plus a **9 providers** button showing the OAuth apps behind it. The tab describes the two shapes in your customer's terms:

> Your customers sign in with the provider and approve access.

> Your customers paste a key they generate themselves.

#### Connections

Every customer who has authorised this connector. Before anyone has, it reads `Nobody has connected yet`. It is the same data as the workspace-wide [Connections](connections.md) page, filtered to this one system.

#### Version pins

> Hold one customer on one version while everyone else moves on. A version set in code still wins over a pin.

That second sentence is the rule that matters: a pin is a fallback, not an override. Pin a customer when they cannot absorb a change yet — a field they depend on moved, or their own integration needs a release first — then unpin them when they are ready.

With nothing to pin, the tab reads `No versioned actions yet` / *Add actions with an externalVersion to enable per-tenant routing.*

The tab also carries a **Compare two versions** tool: `Action slug`, `From`, `To`, `From major`, `To major`, and **Compare**.

#### Webhook config

**New config** creates one. Until then:

> No webhook config yet

> Until one exists, customers of this connector can be polled but cannot be notified.

That is the plumbing behind an [app event trigger](triggers.md) — configure it once here and app event triggers on this connector work for every customer, rather than each of them registering a webhook themselves.

### Action detail

Opening an action from the middle pane gives seven tabs: **Params**, **Headers**, **Auth**, **Body**, **Input schema**, **Output schema** and **Mocks**. The footer shows the action's version and a **New version** button.

Actions on a platform-owned connector are marked **Read-only — owned by platform** and offer **Propose an update** instead of an edit — that proposal is what surfaces under [Pending updates](connector-updates.md).

### Creating a connector

**Create connector** opens a dialog with three sections: **Identity**, **Connection** and **Authentication**.

<figure><img src="../.gitbook/assets/create-connector-dialog.jpg" alt="The create connector dialog"><figcaption></figcaption></figure>

| Field           | Type   | Notes                                                                        |
| --------------- | ------ | ------------------------------------------------------------------------------ |
| **Name**        | text   | Required. What people see. Placeholder `Salesforce`.                          |
| **Slug**        | text   | Required. *Derived from the name. Edit it to override.* Used in API paths and code. |
| **Description** | text   | Optional, but the agent reads it when deciding what a connector is for.       |
| **Protocol**    | select | Required. `REST` (default), `MCP`, `FTP`, `Database`, `REDIS`.                |
| **Visibility**  | select | Offers only `Private` — publishing a connector publicly is a platform-admin action. |
| **Domain**      | text   | Optional. The vendor's domain, e.g. `salesforce.com`.                         |
| **Icon URL**    | text   | Optional. Shown on the card and in the widget.                                |

Authentication is set up **in the same dialog**, not afterwards. **Add method** adds one; each method has a type:

| Type            | Internal value |
| --------------- | -------------- |
| No Auth         | `NO_AUTH`      |
| Basic Auth      | `BASIC`        |
| Digest Auth     | `DIGEST`       |
| Bearer Token    | `BEARER`       |
| API Key         | `API_KEY`      |
| OAuth 2.0 (default) | `OAUTH_2`  |
| Custom          | `INPUT`        |

Those internal values are worth knowing because some of them surface raw in the `Auth` column on [Connections](connections.md).

Each method also carries a **Set as default** radio, an **Authentication docs URL(optional)** field, a **Use Dynamic Client Registration (DCR)** checkbox (RFC 7591), and an **Additional OAuth Config(optional)** key/value repeater. Choosing Basic Auth or API Key swaps in a **Configuration** section with a `Form` / `JSON` toggle and a key/value repeater.

The dialog footer will not let you save until the connector is named — the hint reads *Give it a name to continue.*

{% hint style="info" %}
You rarely need to do this by hand. Describe the system to the [Agent](agent.md) and give it a spec URL or an OpenAPI file — it will discover the actions, build the connector, and test it.
{% endhint %}

### Importing and exporting

**Import** takes a JSON connector definition straight from a file picker — exported from another workspace, or generated from a spec. In the other direction, `⋯ → Export` exports one card, and **Export Selected (n)** exports a batch.
