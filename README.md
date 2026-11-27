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
<tr><td><strong>Build your first integration</strong></td><td>For your team. Describe an integration to your AI tool, and it builds and tests it for you. About five minutes, on the free plan, with no code.</td><td><a href="getting-started/quickstart.md">getting-started/quickstart.md</a></td></tr>
<tr><td><strong>Embed Fastn in your product</strong></td><td>For developers. Put the widget in your product, so your customers can connect their apps.</td><td><a href="tutorials/developer/embedding-quickstart.md">tutorials/developer/embedding-quickstart.md</a></td></tr>
<tr><td><strong>Using integrations in a product?</strong></td><td>For customers of a product that uses Fastn. Connect your apps and manage your integrations.</td><td><a href="tutorials/end-user/README.md">tutorials/end-user/README.md</a></td></tr>
</tbody></table>

## How it works

<figure><img src=".gitbook/assets/overview/fastn-build-once-use-everywhere.svg" alt="Build once, extend per customer, use everywhere. You build an integration once in the Fastn dashboard, from your AI tool through the Fastn MCP server, or with the Fastn agent. Each customer uses it as is or extends it, and their changes stay with that customer. Your product uses it through the widget and API, and your AI agents through the MCP gateway. Fastn runs and maintains it against each customer's apps."><figcaption><p>Build once, extend per customer, use everywhere</p></figcaption></figure>

* **Build once:** build an integration with your AI tool, the Fastn agent or the dashboard, and it serves every customer.
* **Fine-tune per customer:** each customer can adjust the integration in the widget, and the change applies only to them.
* **Use it everywhere:** the same integration runs in your product, through the widget and the API, and for your AI agents, through Fastn Connect.
* **Fastn runs and maintains it:** Fastn runs every call with the right customer's account, logs it, and proposes a fix when an app changes its API.

To learn more about the different parts of Fastn, and how they are used, see [Architecture](getting-started/architecture.md#the-parts).

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
