---
description: "What a connector is, how it relates to actions, auth methods, connections, and webhooks, and where each part lives in the app."
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

# Connectors

**Build → Integrations → Connectors** · [Open in Fastn](https://app.fastn.dev/integrations)

A **connector** is the definition of one external app's API, such as HubSpot, Jira or Stripe. It covers the app's actions, its auth methods (how users sign in to it) and its webhook events. Workflows, the Fastn agent and your AI tool use connectors to read from and write to apps.

For example, the HubSpot connector knows how to call *Create Contact* and *List Owners*, and that people sign in to HubSpot with OAuth 2.0. It doesn't know anyone's HubSpot account. The page describes it in one line:

> A connector is fastn's bridge to one app: it handles sign-in and exposes the app's actions and events. Sign in to one to create a connection.

### Connector versus connection

A connector holds no credentials. Credentials live on a [connection](../connections/README.md), which is created when someone signs in to the connector.

* **Connector:** the definition: this API, these actions, these auth methods, this webhook config. One per app. You manage it on **Build → Integrations → Connectors**.
* **Connection:** one signed-in account on that connector, for your organization or for one customer. One connector can have many connections. You manage them on **Operate → Connections** · [Open in Fastn](https://app.fastn.dev/connections).

### The parts of a connector

| Part | What it is | Where you see it |
| --- | --- | --- |
| **Actions** | One operation the app can perform, such as *Create Contact* or *List Owners*. Each action is an HTTP request with an input schema and an output schema. | The action list on the connector's detail page. See [Actions](action-detail.md). |
| **Auth methods** | How a customer proves who they are to the app, such as OAuth 2.0, API key, bearer token, or basic auth. A connector can offer several; one is the default. | The **Auth** tab. See [Auth methods and providers](auth-methods.md). |
| **Auth providers** | For OAuth methods, the OAuth app (client ID and secret) that Fastn uses to send people to the app's consent screen. | **Auth → Manage providers**. See [Auth providers](auth-methods.md#auth-providers). |
| **Webhook config** | Instructions for subscribing to the app's events on behalf of each customer, so an [app event trigger](../triggers/app-events.md) can fire. | The **Webhook config** tab. See [Webhook config](webhook-config.md). |
| **Versions** | Every change to a connector produces a version. Versions live in **Test** until they are published to **Live**. | **Overview → Versions**, and the **Version pins** tab. See [Inside a connector](inside-a-connector.md#versions). |
| **Connections** | Signed-in accounts that use this connector. | The **Connections** tab, and the workspace-wide [Connections](../connections/README.md) page. |

### Managed and custom connectors

Every connector is one of two kinds, shown as a badge on its card:

* **managed:** built and maintained by Fastn. The card reads *Managed by Fastn*. You can view every part of it, connect to it, export its actions, and run them, but you cannot edit, delete, or publish it. To suggest a change to one of its actions, use [Propose an update](action-detail.md#platform-owned-actions-and-propose-an-update). Fastn reviews it, and vendor changes reach you as proposals under [Pending updates](../connector-updates.md) · [Open in Fastn](https://app.fastn.dev/health?tab=updates).
* **Custom:** created in your workspace, from scratch, with AI or from a file. See [Create a connector](creating-a-connector.md). Your workspace owns it, so you can edit it, add actions, set up its webhook config, publish versions, and delete it. See [Edit, publish, and delete](editing-and-deleting.md).

Once a connector has connections, the badge shows their state instead. See [What a card shows](the-catalogue.md#what-a-card-shows).

### Per-customer versus platform-wide connectors

Inside a workflow, each connector is wired one of two ways.

| Mode              | Credential used                                  | Use for                                            |
| ----------------- | ------------------------------------------------ | -------------------------------------------------- |
| **Per customer**  | The connection belonging to the running customer | Anything touching customer data                    |
| **Platform-wide** | A single connection owned by your organization, shared across the workspace | Your own apps: your Slack, your data warehouse |

Both modes are labeled in the UI: the workflow's Connectors tab shows a **Per customer** or **Platform-wide** badge on each connector. On the connection side, a connection that belongs to your organization rather than to one customer shows `Scope: Account level` on its detail page.

### How the pieces work together

{% stepper %}
{% step %}
#### Pick or build a connector

Find the app in the [catalog](the-catalogue.md). If it is not there, [request it](creating-a-connector.md#request-a-connector) or [create it](creating-a-connector.md).
{% endstep %}

{% step %}
#### Connect

**Connect** opens a dialog that asks for the credential the default auth method needs (an API key, or an OAuth sign-in). The result is a connection. This signs in your own account; your customers sign in their own accounts through the widget. See [Connect an app](connect-an-app.md).
{% endstep %}

{% step %}
#### Use the actions

Workflows, the Fastn agent, and your AI tool (over MCP) call the connector's actions through that connection. The connection decides whose account the call runs as.
{% endstep %}

{% step %}
#### Receive events (optional)

If the connector has a webhook config, Fastn runs its subscription code for each new connection, so that events from that account reach Fastn and an app event trigger can start a workflow.
{% endstep %}
{% endstepper %}

### In this section

* [Configure a connector](../../tutorials/saas-admin/configuring-a-connector.md): create a connector, set up its auth and connect to it, step by step.
* [The catalog](the-catalogue.md): searching, filtering, and reading the connector cards.
* [Create a connector](creating-a-connector.md): the ways to create one, the Create a connector dialog, and Request connector.
* [Inside a connector](inside-a-connector.md): the detail page, its Overview, Connections, and Version pins tabs, and versions.
* [Auth methods and providers](auth-methods.md): the Auth tab and the OAuth apps behind it.
* [Actions](action-detail.md): the action list and the action editor with its seven tabs.
* [Webhook config](webhook-config.md): how Fastn subscribes to an app's events.
* [Edit, publish, and delete](editing-and-deleting.md): what you can change on a connector your workspace owns.
* [Import and export](importing-and-exporting.md): moving connectors and actions in and out as JSON.
* [Connect an app](connect-an-app.md): making a connection, step by step.
