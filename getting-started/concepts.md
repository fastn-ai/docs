---
description: The handful of ideas that everything else in Fastn is built from.
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

# Core concepts

These are the terms used across the dashboard and these docs. For one-line definitions, see the [Glossary](../reference/glossary.md).

### The building blocks

* **Connectors:** A connector is the definition of one external app's API, such as HubSpot, Jira or Stripe. It covers the app's actions, its auth methods (how users sign in to it) and its webhook events, and it holds no credentials. You can use one from Fastn's managed catalog, which Fastn keeps up to date when the vendor changes its API, or create your own. [Learn more](../build/connectors/README.md) · [Open in Fastn](https://app.fastn.dev/integrations)
* **Connections:** A connection is one signed-in account on one connector. It is created when someone on your team or one of your customers authorizes access. Fastn stores the credential encrypted, scopes it to that owner and refreshes OAuth tokens, so nobody has to sign in again. One connector can have many connections. [Learn more](../build/connections/README.md) · [Open in Fastn](https://app.fastn.dev/connections)
* **Workflows:** A workflow is the logic of an integration: the steps that run each time it is triggered. It uses connectors to read from and write to apps, for example to fetch new deals from a CRM, reshape them and create matching invoices in an accounting app. You publish numbered versions and deploy them to environments such as `test` and `live`. [Learn more](../build/workflows/README.md) · [Open in Fastn](https://app.fastn.dev/integrations?tab=workflows)
* **Triggers:** A trigger starts a workflow on its own. It can be a webhook (an outside app calls a URL you give it), a schedule (a clock you set) or an app event (something changed in a connected app). A workflow without a trigger runs only when something calls it. [Learn more](../build/triggers/README.md) · [Open in Fastn](https://app.fastn.dev/integrations?tab=triggers)
* **Unified APIs:** A unified API is one standard API for a whole category of apps, such as CRMs. You call one endpoint with one data format, and Fastn translates the call for whichever app that customer connected. For example, a single "create contact" call works the same whether the customer uses HubSpot, Salesforce or Zoho, so you don't write separate code for each app. [Learn more](../build/unified-apis/README.md) · [Open in Fastn](https://app.fastn.dev/integrations?tab=unified)
* **Widget:** The widget is a ready-made integrations page that you embed in your product, styled to match your brand. Your customers use it to browse the integrations you offer, sign in to their own apps and turn integrations on, without leaving your product or creating a Fastn account. For example, a project management tool can put the widget on its Settings page, so each customer connects their own Slack workspace and turns on an integration that posts new tasks to a Slack channel. [Learn more](../embed/widget-builder/README.md) · [Open in Fastn](https://app.fastn.dev/widgets)

### How a build fits together

<figure><img src="../.gitbook/assets/lifecycle/fastn-lifecycle.svg" alt="The Fastn integration lifecycle: who does what across Build, Publish, Embed, Customize, and Run and monitor"><figcaption><p>Who does what: your team, your customer, and Fastn</p></figcaption></figure>

1. Describe the integration to the Fastn agent or your AI tool, or write it in code.
2. The agent picks or creates the connectors and sets up authentication.
3. It drafts the workflow and its test cases, and shows you the diff.
4. You attach a trigger, publish a version, and deploy it to an environment.
5. You add the integration to your widget, and customers turn it on.
6. You watch runs in **Logs** and set an alert so failures are not silent.

What you can see in the dashboard depends on your role: **Owner**, **Admin**, **Developer**, **Operator**, or **Viewer**. People at your customers who use the widget have the **End User** role and never sign in to Fastn. See [Roles](../manage/roles.md).

### Organization and customer management

Fastn has two kinds of organization: yours, and one for each of your customers.

* **Organization:** Your organization is your company, the SaaS business that builds the product your customers use. It holds everything you build in Fastn, such as connectors, workflows, triggers and the widget, along with your settings. Your team members sign in to Fastn, and each one's role, such as Owner, Admin or Developer, decides what they can see and change. [Learn more](../manage/people.md)
* **Customer:** A customer is a company that uses your product. In Fastn, each customer is an organization of its own under yours, with its own users and its own connections to apps. For example, if Acme uses your product, Acme is a customer organization, and several people at Acme can use your widget to connect Acme's HubSpot and Slack. Customers are isolated from each other: one customer's connections, credentials and data never reach another. [Learn more](../operate/customers.md) · [Open in Fastn](https://app.fastn.dev/customers)
* **End users:** An end user is a person at one of your customers who uses the widget inside your product. A customer can have many end users. They have the **End User** role and never sign in to Fastn itself. [Learn more](../manage/roles.md)

<figure><img src="../.gitbook/assets/diagrams/organization-hierarchy.svg" alt="Your organization, its customers and their end users. Your organization is the SaaS company that builds the integrations, with team members in roles such as Owner, Admin and Developer. Under it, each customer is its own organization with its own end users and its own connections to apps such as HubSpot, Salesforce or Jira. Customers are isolated from each other."><figcaption><p>Purple is your organization, and green is your customers' organizations.</p></figcaption></figure>

### Connector versus connection

A **connector** is the definition: this API, these actions, these auth methods, this webhook config. A **connection** is an instance of it for one customer. One connector, many connections.

Connectors are either **managed by Fastn**, maintained upstream and patched when the vendor changes something, or **custom**, created by you.

### Per-customer versus platform-wide connectors

Inside a workflow, each connector is wired one of two ways.

| Mode              | Credential used                                  | Use for                                            |
| ----------------- | ------------------------------------------------ | -------------------------------------------------- |
| **Per customer**  | The connection belonging to the running customer | Anything touching customer data                    |
| **Platform-wide** | A single connection owned by your org, shared across the workspace | Your own apps: your Slack, your data warehouse |

Both modes are labeled in the UI: the workflow's Connectors tab shows a **Per customer** or **Platform-wide** badge on each connector. On the connection side, a connection that belongs to your organization rather than to one customer shows `Scope: Account level` on its detail page.

### Workflows are code

A workflow is a JavaScript module. The editor holds one file, `<slug>.js`, and it exports a single function:

```javascript
export default async function (ctx) {
  // ctx.input, ctx.headers (connectors are called as fastn.connector.<slug>.<action>())
}
```

There is no node palette and no drag-and-drop step builder. The editor's Diagram tab is AI-generated documentation of that code: a read-only picture that regenerates when the code has changed.

### Execution tiers

Every workflow declares how long it may run and how it answers the caller.

| Tier         | Behavior                                        | Returns       | Timeout range | Default |
| ------------ | ----------------------------------------------- | ------------- | ------------- | ------- |
| **Instant**  | Synchronous; the caller waits                   | Result inline | 1s - 25s      | 25s     |
| **Standard** | Asynchronous, run via Temporal                  | 202 Accepted  | 5s - 15min    | 2min    |
| **Long**     | Asynchronous, for large volumes                 | 202 Accepted  | 30s - 36h     | 15min   |

Instant's 25-second ceiling rises to 2 minutes only for organizations where Fastn has turned on the longer Instant timeout. Long runs for up to 36 hours. Pick Instant only when something is waiting on the answer. Most syncs are Standard.

### Test and live

Fastn separates *what the code is* from *where it runs*.

* **Versions** are snapshots created by Publish, numbered v1, v2, … in the workflows list.
* **Environments** are where versions are deployed. `test` and `live` are built in and protected; you can add named ones such as `staging`, and mark any environment **Requires review** so promoting to it opens a pull request on a connected GitHub repository instead of deploying directly.
* **API keys** carry a mode, `Test` or `Live`. A Test key is refused unless the caller sends `X-fastn-Test-Mode: true`.

Test keys act on real data. See [API keys](../manage/api-keys.md).

### Triggers

Three kinds, covered fully in [Triggers](../build/triggers/README.md).

* **Webhook**: an outside app calls a URL you give it.
* **Schedule**: a clock you set.
* **App event**: something changed in a connected app.

### Unified APIs

Where several providers do the same job (HubSpot, Salesforce, and Zoho all hold contacts), Fastn exposes one canonical endpoint per entity and routes to whichever provider that customer connected. Your code calls `/api/v1/unified/crm/contact` and does not branch on the CRM.

The categories and entities available depend on the unified API catalog in your workspace, and the list grows over time; CRM contacts are a typical example. See [Unified APIs](../build/unified-apis/README.md) for how to browse what is available.

### The Fastn agent

The **Fastn agent** is Fastn's own agent for building integrations, on paid plans (Scale or Enterprise). Start it from **Integrations → Create integration → Build with fastn agent** or the prompt on **Home**. It finds API specs, creates connectors, sets up authentication, proposes field mappings, generates test cases, and writes the workflow. It shows you a diff before anything runs, and it uses AI credits.

On any plan, you can build the same way from your AI tool, such as Claude or Cursor, through the Fastn MCP server. That uses no AI credits.

### The Fastn MCP server and Fastn Connect

Fastn has two MCP addresses. The **Fastn MCP server** (`mcp.fastn.dev/fastn-workspace`) lets your AI tool build and manage integrations in your workspace. **Fastn Connect**, the MCP gateway, gives your AI agents each customer's connected apps as tools, with the same customer scoping and permission model. A customer's own AI client can use it too. See [Fastn MCP server](../build/mcp-gateway/README.md) and [Which MCP do I need?](architecture.md#which-mcp-do-i-need).
