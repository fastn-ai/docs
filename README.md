---
description: >-
  fastn lets your product offer integrations with the apps your customers use.
  You build each integration once, embed it in your product, and fastn runs it
  for every customer.
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

# Welcome to fastn

fastn lets your product offer integrations with the apps your customers use, such as HubSpot, Salesforce and Slack. You build each integration once. Each customer then connects their own accounts from inside your product, and fastn runs the integration for them, scoped to that customer.

fastn has four parts:

| Part            | What it does                                                                                      | Who uses it          |
| --------------- | ------------------------------------------------------------------------------------------------- | -------------------- |
| **Dashboard**   | Build integrations with the fastn agent or in code, test and deploy them, and monitor every run   | Your team            |
| **Widget**      | The panel inside your product where a customer connects apps and turns integrations on            | Your customers       |
| **API and SDK** | Register customers, mint embed tokens, run workflows and read data from your backend              | Your developers      |
| **MCP gateway** | Build from an AI tool such as Claude or Cursor, or give an AI agent each customer's apps as tools | Your team and agents |

fastn handles authentication, token renewal, retries, rate limits and changes to each app's API.

## Get started

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><strong>Build your first integration</strong></td><td>For your team. Describe an integration to the fastn agent, then test it. No code needed.</td><td><a href="getting-started/quickstart.md">getting-started/quickstart.md</a></td></tr>
<tr><td><strong>Embed fastn in your product</strong></td><td>For developers. Mint a token from your backend and render the widget.</td><td><a href="tutorials/developer/embedding-quickstart.md">tutorials/developer/embedding-quickstart.md</a></td></tr>
<tr><td><strong>Using integrations in a product?</strong></td><td>For customers of a product that uses fastn. Connect your apps and manage your integrations.</td><td><a href="tutorials/end-user/README.md">tutorials/end-user/README.md</a></td></tr>
</tbody></table>

## Learn more

* [Core concepts](getting-started/concepts.md): customers, connectors, connections, workflows and triggers.
* [Authentication and API keys](tutorials/developer/authentication-and-api-keys.md): test and live keys, and how your backend calls fastn.
* [REST API reference](reference/rest/README.md) and [SDK](reference/sdk/README.md): every endpoint and method.
* [FAQs](reference/faqs.md) and [Glossary](reference/glossary.md).
