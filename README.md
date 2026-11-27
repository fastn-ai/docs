---
description: >-
  Fastn is an embedded integration platform for B2B SaaS. Build each
  integration once, and offer it to your customers inside your product.
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Welcome to Fastn

Fastn is an embedded integration platform for B2B SaaS products. It lets your customers connect the apps they already use, such as their CRM, ERP or support desk, from inside your product.

Build integrations with your preferred AI agent using Fastn's MCP tools, and embed them in your product in minutes. Fastn includes:

* **Fine-tuning for each customer:** every customer can adjust an integration to fit their own use case.
* **Insights and alerts:** customers can review logs and metrics for their integrations and set their own alerts.
* **A maintainer agent:** it tells you when a third-party app changes its API, and helps you deploy the update your integrations need.

## Get started

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><strong>Build your first integration</strong></td><td>For your team. Describe an integration to your AI tool, and it builds and tests it for you. No code needed.</td><td><a href="getting-started/quickstart.md">getting-started/quickstart.md</a></td></tr>
<tr><td><strong>Embed Fastn in your product</strong></td><td>For developers. Put the widget in your product, so your customers can connect their apps.</td><td><a href="tutorials/developer/embedding-quickstart.md">tutorials/developer/embedding-quickstart.md</a></td></tr>
<tr><td><strong>Using integrations in a product?</strong></td><td>For customers of a product that uses Fastn. Connect your apps and manage your integrations.</td><td><a href="tutorials/end-user/README.md">tutorials/end-user/README.md</a></td></tr>
</tbody></table>

{% hint style="info" %}
**Try it in five minutes, on the free plan.** Sign up at [app.fastn.dev](https://app.fastn.dev), click **Connect your AI tool** in the top bar, and ask Claude or Cursor: *"Using Fastn, when a new contact is created in HubSpot, post their name and email in our #sales Slack channel."* Then run its test, fully mocked, so no real data is touched. Step by step: [Quickstart](getting-started/quickstart.md).
{% endhint %}

## How it works

<figure><img src=".gitbook/assets/overview/fastn-build-once-use-everywhere.svg" alt="Build once, extend per customer, use everywhere. You build an integration once in the Fastn dashboard, from your AI tool through the Fastn MCP server, or with the Fastn agent. Each customer uses it as is or extends it, and their changes stay with that customer. Your product uses it through the widget and API, and your AI agents through the MCP gateway. Fastn runs and maintains it against each customer's apps."><figcaption><p>Build once, extend per customer, use everywhere</p></figcaption></figure>

* **Build once:** you build an integration from your AI tool through the Fastn MCP server, with the Fastn agent, or in the dashboard. One build serves every customer, so a new customer adds no integration work.
* **Each customer makes it their own:** customers use the integration as it is, or adjust it in the widget, for example to add fields, filter records or change the sync direction. A change applies only to that customer, so it can't break anyone else's setup.
* **Use it everywhere:** the same integration runs in your product, through the widget and the API, and for your AI agents, through Fastn Connect. They share one set of integrations, credentials and logs.
* **Fastn runs and maintains it:** Fastn runs every call with the right customer's setup, logs it, and alerts you when something fails. When an app changes its API, Fastn proposes a fix, and it reaches every customer once you accept it.

## The parts of Fastn

* **Dashboard:** the web app at [app.fastn.dev](https://app.fastn.dev) where your team builds integrations, sets up the widget and watches every run. Used by your team.
* **Widget:** the panel inside your product where each customer connects their apps and turns integrations on. Used by your customers.
* **API and SDK:** let your backend register customers, start the widget for a customer, run workflows and read data. Used by your developers.
* **Fastn Connect:** an MCP server that gives AI agents a customer's connected apps as tools. Every call is checked against your policies, logged, and runs with that customer's account. Used by your AI agents, including agents that act for your customers.

To learn the building blocks, such as connectors, connections and workflows, see [Core concepts](getting-started/concepts.md).

## What Fastn handles for you

Each row is something you would otherwise build and run yourself.

| Area | What Fastn does | What you don't have to build |
| --- | --- | --- |
| **Sign-in and credentials** | The widget runs each app's own OAuth or API-key sign-in. Fastn stores every credential encrypted, scoped to one customer, and renews OAuth tokens. | An OAuth flow per app, a credential store, and token refresh. |
| **Customer isolation** | Your backend mints a short-lived token for one customer. The widget, API calls and runs see only that customer's connections and data. | Customer separation in every integration, and the risk of one customer's data reaching another. |
| **Connector catalog** | Over 1,000 connectors, each with its actions, auth methods and webhooks, plus unified APIs that work the same way across every app of a kind, such as every CRM. | A client for each app's API, and a separate code path per CRM or helpdesk. |
| **Building from a description** | Describe an integration to your AI tool through the Fastn MCP server (every plan), or to the Fastn agent (Scale or Enterprise). It picks the connectors, writes the workflow and tests it. | Hand-written workflows, and developer time for every new integration request. |
| **Per-customer changes** | Customers change field mappings, filters and sync direction in the widget, or ask the widget assistant. Changes apply only to that customer. | Custom builds and forks for individual customers. |
| **Running workflows** | Workflows run on a webhook, a schedule or an app event, synchronously for up to 25 seconds or in the background for long jobs. Fastn handles rate limits, retries temporary failures, and keeps deliveries that run out of retries in a dead-letter queue. | Queues, workers, schedulers, retry logic and rate-limit handling. |
| **Monitoring** | Every event, run and app call is logged per customer. **Health** shows what needs attention, and alerts go out by email, Slack, Microsoft Teams or webhook. | Logging, dashboards and alerts per integration, and tracing which customer a failure hit. |
| **API changes** | Fastn's maintainer agent watches the apps you use. When a vendor changes something your workflows depend on, it proposes a fix in **Health → Pending updates**. Nothing changes until you accept it. | Tracking every vendor's changelog, and fixing breakages after customers report them. |
| **AI agent access** | Fastn Connect gives your AI agents one customer's connected apps as tools. Every call is checked against your policies, logged, and runs with that customer's account. | A separate auth and tool layer for your agents, and agents holding raw customer credentials. |

## Not sure Fastn fits your use case?

Ask your AI tool. [Find out if Fastn fits your use case](getting-started/plan-your-integration.md) shows how, in four steps. Or copy this line into your AI tool, and it sets itself up to answer your questions about Fastn:

```
Fetch and execute the instructions to set me up for fastn from https://raw.githubusercontent.com/fastn-ai/fastn-claude-plugins/main/agent-setup/prompt.md
```

## Learn more

* [Core concepts](getting-started/concepts.md): the building blocks, such as connectors, connections, workflows and triggers.
* [Architecture](getting-started/architecture.md): how the parts fit together and how a request flows.
* [Authentication and API keys](tutorials/developer/authentication-and-api-keys.md): test and live keys, and how your backend calls Fastn.
* [REST API reference](reference/rest/README.md) and [SDK](reference/sdk/README.md): every endpoint and method.
* [FAQs](reference/faqs.md) and [Glossary](reference/glossary.md).
