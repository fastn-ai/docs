---
description: One standard API for a whole category of apps, such as CRMs, that works with whichever app each customer connected.
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

# Unified APIs

**Build → Integrations → Unified APIs** · [Open in Fastn](https://app.fastn.dev/integrations?tab=unified)

A **unified API** is one standard API for a whole category of apps, such as CRMs. You call one endpoint with one data format, and Fastn translates the call for whichever app that customer connected.

For example, three of your customers use three different CRMs: HubSpot, Salesforce and Zoho. Without a unified API, your code needs a separate branch for each CRM to do one thing, create a contact. With one, you send the same "create contact" call for all three customers, and Fastn sends it on to each customer's own CRM.

<figure><img src="../../.gitbook/assets/screens/unified-apis.webp" alt="The Unified APIs page: six category cards, CRM (10 entities), Documents, Knowledge Base, Messaging, Project Management and Scheduling, each with its provider icons and entity count"><figcaption>The icons on each card are the providers currently serving that category.</figcaption></figure>

### Categories, entities and providers

* **Category:** a kind of app, such as **CRM**, **Messaging** or **Project Management**. Each category is one card on the Unified APIs page.
* **Entity:** a kind of record inside a category, such as a `Contact` or an `Opportunity` in a CRM. Each entity has its own endpoints.
* **Provider:** an app that serves an entity, such as HubSpot or Salesforce. An entity is served by one or more providers. In the API you name a provider by its slug, such as `hubspot`; the cards show its display name.
* **Operation:** what an endpoint does to an entity: **List**, **Get**, **Search**, **Create**, **Update** or **Delete**. See [Inside a category](inside-a-category.md).

### The catalog

The catalog is live data: which categories, entities and providers you see depends on what Fastn has published and mapped at the time. As an illustration, the catalog has included the categories **CRM**, **Documents**, **Knowledge Base**, **Messaging**, **Project Management** and **Scheduling**, with entries like these:

| Category      | Example entities                                   | Example providers (slugs)                |
| ------------- | -------------------------------------------------- | ---------------------------------------- |
| **CRM**       | `Account`, `Contact`, `Lead`, `Note`, `Opportunity` | `hubspot`, `salesforce`, `zohoCrm`       |
| **Documents** | `Document`, `Document Content`                     | `googleDocs`, `notion`                   |
| **Messaging** | `Channel Message`, `Direct Message`                | `microsoftTeams`, `slack`                |

Open a category in the dashboard to see its current entities and providers.

The Unified APIs page shows a count chip (for example `N categories`) and a **Search categories** box. A search that matches nothing reads `No categories match` / *Try another search.* The page subtitle reads: *One call that reaches every app of the same kind you have connected: every CRM, every store.*

### Where you can use a unified API

* **From your backend:** send an HTTP request to `/v1/unified/<category>/<entity>` with your Fastn API key. See [Set up and use a unified API](setup-and-usage.md).
* **From a workflow:** call `fastn.unified` instead of a specific connector. See [Workflow runtime API](../../reference/workflow-runtime.md).
* **From the SDK:** use `customer.records()`. See [Unified records](../../reference/sdk/unified-records.md).
* **In the widget:** attach a unified category to an integration, so it serves whichever provider each customer connected. See [Edit integration](../../embed/widget-builder/edit-integration.md#unified-apis).

A unified API covers what apps in a category have in common. For a field or action only one app has, call its [connector](../connectors/README.md) directly. See [Choose between unified and direct](unified-vs-direct.md).

### In this section

* [Set up and use a unified API](setup-and-usage.md): copy a request from the dashboard and send it for one of your customers.
* [Inside a category](inside-a-category.md): a category's entities, providers, connection state and endpoints.
* [Choose between unified and direct](unified-vs-direct.md): when to use a unified API and when to call a connector directly.
