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

### Organization and customer management

Fastn has two kinds of organization: yours, and one for each of your customers.

* **Organization:** Your organization is your company, the SaaS business that builds the product your customers use. It holds everything you build in Fastn, such as connectors, workflows, triggers and the widget, along with your settings. Your team members sign in to Fastn, and each one's role, such as Owner, Admin or Developer, decides what they can see and change. [Learn more](../manage/people.md)
* **Customer:** A customer is a company that uses your product. In Fastn, each customer is an organization of its own under yours, with its own users and its own connections to apps. For example, if Acme uses your product, Acme is a customer organization, and several people at Acme can use your widget to connect Acme's HubSpot and Slack. Customers are isolated from each other: one customer's connections, credentials and data never reach another. [Learn more](../operate/customers.md) · [Open in Fastn](https://app.fastn.dev/customers)
* **End users:** An end user is a person at one of your customers who uses the widget inside your product. A customer can have many end users. They have the **End User** role and never sign in to Fastn itself. [Learn more](../manage/roles.md)

<figure><img src="../.gitbook/assets/diagrams/organization-hierarchy.svg" alt="Your organization, its customers and their end users. Your organization is the SaaS company that builds the integrations, with team members in roles such as Owner, Admin and Developer. Under it, each customer is its own organization with its own end users and its own connections to apps such as HubSpot, Salesforce or Jira. Customers are isolated from each other."><figcaption><p>Purple is your organization, and green is your customers' organizations.</p></figcaption></figure>

### Build with the Fastn MCP server or the Fastn agent

You can build an integration by describing it in plain words, in one of two ways. Fastn recommends the Fastn MCP server.

* **Fastn MCP server (recommended):** The Fastn MCP server connects the AI tool you already use, such as Claude, Cursor or VS Code, to your Fastn workspace at `https://mcp.fastn.dev/fastn-workspace`. From a chat, your AI tool can create connectors, set up authentication, write and test workflows, and manage your integrations. It works on every plan and uses no Fastn AI credits. To set it up, see [Connect your AI tool](../build/mcp-gateway/README.md#open-the-connect-dialog), or follow the steps for [Claude](../build/mcp-gateway/claude.md), [Claude Code](../build/mcp-gateway/claude-code.md), [Cursor](../build/mcp-gateway/cursor.md), [VS Code](../build/mcp-gateway/vscode.md) or [any other MCP client](../build/mcp-gateway/README.md#how-your-ai-tool-connects).
* **Fastn agent:** The Fastn agent is Fastn's own build agent, inside the dashboard, on paid plans (Scale or Enterprise). Start it from **Integrations → Create integration → Build with fastn agent** or the prompt on **Home**. It finds API specs, creates connectors, sets up authentication, proposes field mappings, generates test cases and writes the workflow, and it shows you a diff before anything runs. It uses Fastn AI credits. [Learn more](../build/agent/README.md) · [Open in Fastn](https://app.fastn.dev/agent)

**Fastn Connect** is a separate MCP server that gives your AI agents your customers' connected apps as tools. [Learn more about Fastn's MCP tools](architecture.md#which-mcp-do-i-need)

### How a build fits together

<figure><img src="../.gitbook/assets/lifecycle/fastn-lifecycle.svg" alt="The Fastn integration lifecycle: who does what across Build, Publish, Embed, Customize, and Run and monitor"><figcaption><p>Who does what: your team, your customer, and Fastn</p></figcaption></figure>

1. Describe the integration to your AI tool through the Fastn MCP server, or to the Fastn agent, or write it in code.
2. The agent picks or creates the connectors and sets up authentication.
3. It drafts the workflow and its test cases, and shows you the diff.
4. You attach a trigger, publish a version, and deploy it to an environment.
5. You add the integration to your widget, and customers turn it on.
6. You watch runs in **Logs** and set an alert so failures are not silent.

What you can see in the dashboard depends on your role: **Owner**, **Admin**, **Developer**, **Operator**, or **Viewer**. People at your customers who use the widget have the **End User** role and never sign in to Fastn. See [Roles](../manage/roles.md).
