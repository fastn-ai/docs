---
description: >-
  Understand the two connection modes for connector steps in flows: fixed
  connections using workspace credentials and dynamic connections using
  per-tenant credentials via widgets.
---

# Fixed vs Dynamic Connections

When you add a connector step to a flow, Fastn asks you to choose how the step authenticates with the external app. You have two connection modes: **fixed** and **dynamic**. Each mode determines whose credentials the connector uses at runtime and how those credentials are managed.

## Overview

| Attribute                  | Fixed connection                      | Dynamic connection                          |
| -------------------------- | ------------------------------------- | ------------------------------------------- |
| **Credentials**            | Workspace-level (shared)              | Per-tenant (individual)                     |
| **Who authenticates**      | A workspace admin, once               | Each tenant, through a widget               |
| **Credential storage**     | Workspace vault                       | Tenant-isolated vault                       |
| **Multi-tenancy required** | No                                    | Yes                                         |
| **Best for**               | Internal automations, single-team use | Customer-facing integrations, SaaS products |

***

## Fixed connections

A fixed connection uses a single set of credentials that a workspace admin configures at design time. Every execution of the flow uses the same connection, regardless of who triggers it.

### When to use fixed connections

* **Internal workflows** — Your team owns the app account and every flow run should act as the same user (for example, posting alerts to a shared Slack channel).
* **Back-office automations** — The flow reads from or writes to a company-owned system such as an internal database or CRM instance.
* **Prototyping** — You want to test a flow quickly without setting up widgets and tenants.

### How to set up a fixed connection

1. Open your flow in the editor and select (or add) a connector step.
2. In the right sidebar under **Flow Connection**, select the connector group, the specific connector (for example, Slack), and the endpoint you need.
3. Click **Next** to reach the **Connect** section.
4. Click **Connect** and authenticate with the external app using your workspace credentials (OAuth, API key, or another supported method).
5. After authentication succeeds, Fastn saves the connection to the workspace. Move to the **Configure** section to set the remaining parameters.

{% hint style="info" %}
Fastn stores the credentials securely in the workspace vault and reuses them for every execution of this connector step. You do not need to re-authenticate unless the token expires without a refresh token or an administrator revokes it.
{% endhint %}

### Considerations

* All flow executions share the same credentials, so rate limits and audit trails point to one account.
* If the connection token expires or someone revokes it, the flow fails for all triggers until you re-authenticate.
* Fixed connections do not support per-tenant isolation. If you need different credentials per customer, use a dynamic connection.

***

## Dynamic connections

A dynamic connection delegates authentication to each tenant. Instead of a single workspace credential, every tenant authenticates independently through an embedded [widget](../../classic/embedded-integrations/getting-started-with-fastns-embedded-experience/building-and-configuring-widgets-in-fastn.md). At runtime, Fastn resolves the correct credentials for the tenant that triggered the flow.

### When to use dynamic connections

* **Customer-facing products** — Your application serves multiple customers, and each customer connects their own Slack, HubSpot, or other accounts.
* **Multi-tenant SaaS** — You need strict credential isolation so that Tenant A's tokens are never used for Tenant B's flow executions.
* **Embedded integrations** — You publish a widget that end users interact with to activate, configure, and manage their own connections.

### Prerequisites

Dynamic connections require a multi-tenant setup:

* **Tenants configured** — Create tenants under **Settings > Tenants** in your workspace. Each tenant is identified by a unique tenant ID (`x-fastn-space-tenantid` header).
* **Widget created** — Build a widget that includes the connector as a dependency. The widget provides the UI through which tenants authenticate. See [Building and configuring widgets in Fastn](../../classic/embedded-integrations/getting-started-with-fastns-embedded-experience/building-and-configuring-widgets-in-fastn.md).

### How to set up a dynamic connection

1. **Create and configure a widget**
   * Navigate to **Widgets** in your workspace and click **Add Widget**.
   * Select the connector (for example, Slack) as a dependency connector.
   * Configure the authentication method (OAuth, API key, Bearer Token, Basic Auth, or Custom Input) under **Auth Attributes**.
   * Optionally restrict visibility to specific tenants using the **Enable for specific tenants** toggle.
2. **Link the widget to your flow**
   * Open your flow in the editor and select the connector step.
   * In the **Connect** section, choose the dynamic connection option to link the step to the widget rather than a fixed credential.
   * Fastn now resolves the connection at runtime based on the tenant context of the incoming request.
3. **Deploy the widget**
   * Click **Deploy to LIVE** on the widget page. This publishes the widget and its associated flows to your live environment.
   * End users (tenants) see the widget in your embedded integration hub and can authenticate with their own accounts.
4. **Tenant authenticates**
   * When a tenant opens the widget, they click **Connect** and complete the OAuth flow (or provide their API key) for the external app.
   * Fastn stores the tenant's credentials in an isolated vault, associated with their tenant ID.

{% hint style="info" %}
Fastn stores each tenant's credentials separately in its SOC 2 certified vault. Your application code never accesses raw tokens. Fastn handles token refresh and revocation automatically.
{% endhint %}

### How runtime resolution works

When a flow with a dynamic connection executes:

1. Fastn reads the tenant ID from the request context.
2. It looks up the credentials that tenant authenticated through the widget.
3. The connector step executes using that tenant's credentials.
4. If the tenant has not yet connected, the step fails with an authentication error, prompting the tenant to complete the widget setup.

***

## Choosing the right mode

Use the decision tree below to select the appropriate connection mode for your flow:

```
Does the flow serve multiple customers or tenants?
├── Yes
│   └── Does each tenant need their own credentials?
│       ├── Yes → Dynamic connection
│       └── No (shared account is acceptable) → Fixed connection
└── No
    └── Fixed connection
```

### Common patterns

| Scenario                                | Recommended mode | Reason                                                     |
| --------------------------------------- | ---------------- | ---------------------------------------------------------- |
| Post alerts to a team Slack channel     | Fixed            | Single shared channel, one set of credentials              |
| Sync each customer's HubSpot data       | Dynamic          | Each customer authenticates with their own HubSpot account |
| Internal database backup                | Fixed            | Company-owned database, no tenant context needed           |
| Customer-facing Jira integration widget | Dynamic          | Each customer connects their own Jira instance             |
| Prototype or demo flow                  | Fixed            | Faster setup, no widget or tenant configuration required   |

***

## Related pages

* [Connector types & setup](connector-types-and-setup.md) — Community, workspace, and organization connectors
* [Setting up connector authentication](setting-up-connector-authentication.md) — OAuth, API key, and other auth methods
* [Building and configuring widgets in Fastn](../../classic/embedded-integrations/getting-started-with-fastns-embedded-experience/building-and-configuring-widgets-in-fastn.md) — Create the widget that powers dynamic connections
* [Multitenancy](../../classic/fastn-ucl/getting-started/about-unified-context-layer/multitenancy.md) — Tenant isolation architecture
* [How to manage multiple app connections together](../../tutorials/flow-customization-and-operations/how-to-manage-multiple-app-connections-together.md) — Unified connectors for multi-app flows
