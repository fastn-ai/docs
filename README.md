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

Build integrations with your preferred AI agent using Fastn's MCP tools, and embed them in your product in minutes. Fastn also handles customizability, monitoring and maintenance for every integration. See [Features](getting-started/features.md).

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

## Not sure Fastn fits your use case?

Ask your AI tool. [Find out if Fastn fits your use case](getting-started/plan-your-integration.md) shows how, in four steps. Or copy this line into your AI tool, and it sets itself up to answer your questions about Fastn:

```
Fetch and execute the instructions to set me up for fastn from https://raw.githubusercontent.com/fastn-ai/fastn-claude-plugins/main/agent-setup/prompt.md
```

## Learn more

* [Features](getting-started/features.md): everything Fastn runs for you, so you don't have to build it yourself.
* [Core concepts](getting-started/concepts.md): the building blocks, such as connectors, connections, workflows and triggers.
* [Architecture](getting-started/architecture.md): how the parts fit together and how a request flows.
* [Authentication and API keys](tutorials/developer/authentication-and-api-keys.md): test and live keys, and how your backend calls Fastn.
* [REST API reference](reference/rest/README.md) and [SDK](reference/sdk/README.md): every endpoint and method.
* [FAQs](reference/faqs.md) and [Glossary](reference/glossary.md).
