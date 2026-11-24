---
description: Setup step 2. Pick the apps your customers get in your widget, then optionally build an integration for them.
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

# Pick your integrations

This step is for choosing the integrations your customers get inside your product, and building the first one. You pick an app your customers use and say what the integration should do; fastn's agent (**Build with AI**) builds it. An integration is a connector, a connection, its triggers and the workflow logic around them: it moves data between your product and the customer's app and does a job there.

**Setup step 2.** Pick the apps your customers need: each one that is in fastn appears in your widget for customers to connect. Building an integration for an app, so it syncs or automates something, is optional. Describe it as a job, for example "when a shipment is created, add it to the customer's HubSpot".

### What it's made of

| Component | What it is | Example |
| --- | --- | --- |
| Connectors | Your product's connector and the connector for the customer's app | Your product and HubSpot |
| Workflow | The code that reads, transforms and writes data | Turn a shipment into a HubSpot deal |
| Trigger | What starts the workflow: an event in a connected app, a webhook, or a schedule | A shipment is created |
| Configuration template | The default field mappings and rules each customer starts from | Shipment status → deal stage |
| Test cases | Checks Build with AI runs before publishing | One deal per shipment |
| Versions | Publishing saves a numbered copy you can go back to; deploying sends it to Test (to try it) or Live (where it runs for customers) | v3 in Live |

### Ways to do it

| Way | Best when | What you do |
| --- | --- | --- |
| Build with AI | You want it built and tested for you | Describe the job, or pick a suggested use case. Review the plan, answer its questions, approve the mappings and tests. Paid plans only (Scale, Enterprise). Uses AI credits |
| Your AI tools | Your team works in Claude, ChatGPT, Cursor or similar | Describe the job in your AI tool through fastn's MCP server, and approve each step in the chat |
| Connectors only | Customers only need to connect an app your own code or agents use | Add the connector to the widget, with no workflow |
| Unified API | Customers use different apps for the same job | Add a category such as CRM: one "create contact" call works with HubSpot, Salesforce or another CRM |
| Whole catalog | Self-serve products, or you don't know yet what customers need | Turn on **Catalog connectors** in the widget builder, and build integrations later |
| By hand | You want full control | Create the workflow and trigger, then add it to the widget. Code editing is off by default (fastn turns it on per organization), so until then you change code by asking Build with AI |

### Use cases and scenarios

| Use case | Example | Trigger | Scope |
| --- | --- | --- | --- |
| Push events out | A shipment created in your product is added to the customer's HubSpot | Event from your product | Organization level |
| Pull data in | The customer's Jira issues are imported into your product | Schedule | Organization level |
| Notifications | A message goes to the customer's Slack when something critical happens | Event from your product | Organization level |
| Personal apps | Meetings booked in your product go to each user's own Google Calendar | Event from your product | User level |

### Scope: shared or per user

Each integration has a **Scope** setting: who shares a connection inside one customer. Either way, each customer's connections stay separate, as long as each embed token is minted for that customer.

|  | Organization level | User level |
| --- | --- | --- |
| One connection for | The whole customer, shared by its users | Each user at a customer |
| Typical apps | CRM, project tool, data warehouse, shared channels | Their own email or calendar |

### In the onboarding

Setup step 2, **Pick your integrations**, lists apps suggested for your product. Pick every app your customers need. Each row carries two badges: whether your product offers that app (**You offer it**, **You don't offer it** or **Needs work**), and whether fastn has a connector for it (**In fastn** or **Not in fastn yet**). Each pick that is in fastn appears in your widget, ready for customers to connect, with nothing built. A pick that is not in fastn yet does not appear; request it, or build its connector later. You can also turn on the whole catalog. **Do it later** skips the step. The step earns 10 AI credits.

### Build an integration

Picking an app lets customers connect it. To make it sync or automate something, build an integration: the optional going-live item **Build an integration**. Build it in your AI tool (**Build in your AI tool**, no AI credits) on every plan, or with **Build with the fastn agent** on Scale and Enterprise. It counts once one of your widgets runs a workflow, and earns 20 AI credits.

### Related docs

[Build with AI](../../build/agent/README.md) · [Creating a workflow via AI](../../tutorials/saas-admin/creating-a-workflow-via-ai.md) · [Workflows](../../build/workflows/README.md) · [Triggers](../../build/triggers/README.md) · [Unified APIs](../../build/unified-apis/README.md) · [Understanding tenancy](../../tutorials/developer/understanding-tenancy.md)
