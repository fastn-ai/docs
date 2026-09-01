---
description: Every system your customers can authorise — managed, imported or built by you.
---

# Connectors

**Integrations → Connectors**

<figure><img src="../.gitbook/assets/connectors-list.jpg" alt="The connector catalogue"><figcaption></figcaption></figure>

A connector is the definition of one external system: its actions, its authentication methods, its webhook configuration and its versions. It is not a credential — that is a [connection](connections.md).

### The catalogue

The page header states the intent plainly: *depth on the ones that block deals, not a catalogue count*. Connectors marked **managed** are maintained by fastn — when the vendor ships a breaking change, you get a proposal under [Connector updates](connector-updates.md) rather than a broken sync.

| Control            | What it filters                                                     |
| ------------------ | --------------------------------------------------------------------- |
| **Search**         | Name and description                                                 |
| **All**            | Everything in the catalogue                                          |
| **Connected**      | Connectors with at least one live connection                         |
| **OAuth**          | Connectors offering OAuth 2.0                                        |
| **All Visibility** | Private (your workspace only) or Public (visible to your workspaces) |

Cards show the connector's name, a managed/custom/Connected badge, its description, its auth methods, and who maintains it. The button reads **Connect** on an unconnected connector and **Add another connection** on one already in use.

### Inside a connector

Click any card to open it. A searchable list of every action sits on the left; five tabs on the right.

<figure><img src="../.gitbook/assets/connector-detail-overview.jpg" alt="A connector's overview tab"><figcaption>The Overview tab: connections, auth methods, current version.</figcaption></figure>

#### Overview

Three counters — connections, auth methods, current version — and a details table.

| Field            | Meaning                                                                                      |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| **Slug**         | The identifier used in API paths and in workflow code.                                        |
| **Visibility**   | **Private**: your workspace only. **Public**: workspaces under your org can use it when Catalog connectors is on. Other organisations never see it. |
| **Auth methods** | What your customers authorise with.                                                           |
| **Created**      | When it entered the catalogue.                                                                |

The **Versions** panel lists every version with its Test/Live state.

#### Auth

<figure><img src="../.gitbook/assets/connector-auth-tab.jpg" alt="A connector's authentication methods"><figcaption></figcaption></figure>

The authentication methods your customers can use, one marked **Default**. Two shapes:

* **OAuth** — customers sign in with the provider and approve access. The providers link shows which OAuth apps back it.
* **Token or key** — customers paste a credential they generate themselves.

{% hint style="warning" %}
Until you register your own OAuth app for a connector, your customers see **fastn.ai** on the provider's consent screen. Set up your own app on this tab to show your brand instead.
{% endhint %}

#### Connections

Every customer who has authorised this connector, with the auth method they used and the connection's status. It is the same data as the workspace-wide [Connections](connections.md) page, filtered to this one system — the fastest way to answer "how many of our customers have connected Salesforce, and are any of them broken?"

#### Version pins

Connectors are versioned, and a customer can be held on a specific version rather than the current one.

Pin a customer when they cannot absorb a change yet — a field they depend on moved, or their own integration needs a release first. Everyone else moves forward while that customer stays put, and you unpin them when they are ready. Without pins, a connector change is all-or-nothing across your whole customer base.

#### Webhook config

Where inbound event delivery from this system is set up: the endpoint the vendor calls, the signing secret used to verify that a delivery really came from them, and which events are subscribed.

This is the plumbing behind an [app event trigger](triggers.md). Configure it here once, and app event triggers on this connector work for every customer without each of them registering a webhook themselves.

### Actions

The left panel lists every action with its HTTP verb. Asana, for example, exposes 159. Checkboxes let you scope which actions a workflow or an agent is allowed to use — the point of *"read-only Jira for one customer, nothing beyond that"*.

### Creating a connector

**Create connector** opens a dialog with two sections.

<figure><img src="../.gitbook/assets/create-connector-dialog.jpg" alt="The create connector dialog"><figcaption></figcaption></figure>

| Field           | Notes                                                                        |
| --------------- | ------------------------------------------------------------------------------ |
| **Name**        | Required. What people see.                                                    |
| **Slug**        | Derived from the name; editable. Used in API paths and code, so choose once.  |
| **Description** | Optional, but the agent reads it when deciding what a connector is for.       |
| **Protocol**    | REST, MCP, FTP, Database or REDIS.                                            |
| **Visibility**  | Starts Private. Publishing to the customer catalog is done by a platform admin. |
| **Domain**      | Optional. The vendor's domain.                                                |
| **Icon URL**    | Optional. Shown on the card and in the widget.                                |

Authentication is configured after creation, from **No Auth**, **Basic Auth**, **Digest Auth**, **Bearer Token**, **API Key**, **OAuth 2.0** or **Custom**.

{% hint style="info" %}
You rarely need to do this by hand. Describe the system to the [Agent](agent.md) and give it a spec URL or an OpenAPI file — it will discover the actions, build the connector, and test it.
{% endhint %}

### Importing

**Import** brings in a connector definition that already exists — exported from another workspace, or generated from a spec.
