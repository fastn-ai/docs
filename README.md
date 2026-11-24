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
    visible: true
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
| **Dashboard** | The web app at app.fastn.dev where the operator builds integrations, sets up the widget and watches every run | The operator: the person on your team who sets up and runs integrations |
| **Widget**      | The panel inside your product where a customer connects apps and turns integrations on            | Your customers       |
| **API and SDK** | Register customers, mint embed tokens, run workflows and read data from your backend              | Your developers      |
| **fastn Connect** | The MCP gateway for integrations, built for AI agents. One URL gives an agent the connected apps as tools. Every call is checked against your policies, logged, and runs with the right customer's or person's account | Your AI agents, including agents that act for your customers |

## Get started

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><strong>Build your first integration</strong></td><td>For your team. Describe an integration to the fastn agent, then test it. No code needed.</td><td><a href="getting-started/quickstart.md">getting-started/quickstart.md</a></td></tr>
<tr><td><strong>Embed fastn in your product</strong></td><td>For developers. Mint a token from your backend and render the widget.</td><td><a href="tutorials/developer/embedding-quickstart.md">tutorials/developer/embedding-quickstart.md</a></td></tr>
<tr><td><strong>Using integrations in a product?</strong></td><td>For customers of a product that uses fastn. Connect your apps and manage your integrations.</td><td><a href="tutorials/end-user/README.md">tutorials/end-user/README.md</a></td></tr>
</tbody></table>

## How it works

<figure><img src=".gitbook/assets/overview/fastn-build-once-use-everywhere.svg" alt="Build once, extend per customer, use everywhere. You build an integration once in the fastn dashboard, from your AI tool through the fastn MCP server, or with the fastn agent. Each customer uses it as is or extends it, and their changes stay with that customer. Your product uses it through the widget and API, and your AI agents through the MCP gateway. fastn runs and maintains it against each customer's apps."><figcaption><p>Build once, extend per customer, use everywhere</p></figcaption></figure>

* **Build once.** Build an integration in the dashboard, from your AI tool through the fastn MCP server, or by describing it to the fastn agent.
* **Extend per customer.** Each customer uses the integration as is, or extends it in the widget: add fields, filter records, change direction, or ask the widget assistant. A customer's changes apply only to that customer.
* **Use everywhere.** The same integration runs in your product, through the widget and the API, and for your AI agents, through the MCP gateway.
* **Runs and maintains.** fastn runs every call with that customer's setup, logs it and sends alerts. When an app's API changes, the maintainer agent proposes a fix, and it applies to every customer once you accept it.

## What fastn runs for you

* **Sign-in and credentials.** The widget runs each app's own OAuth or API-key sign-in. fastn stores every credential encrypted, scoped to one customer, and renews OAuth tokens.
* **Customer isolation.** Your backend mints a short-lived embed token for one customer, and the widget, API calls and runs see only that customer's connections and data.
* **Running workflows.** Workflows run on a webhook, a schedule or an app event, synchronously for up to 25 seconds or in the background for up to 36 hours. fastn handles each app's rate limits. A retry policy with backoff retries transient failures, and deliveries that run out of retries wait in a dead-letter queue until someone acts.
* **Monitoring.** Every event, run and call to an app is logged per customer. Alerts go out by email, Slack, Microsoft Teams or webhook when a run fails or a threshold is crossed.
* **API changes.** fastn's maintainer agent watches the apps you use. When a vendor changes something your workflows depend on, it proposes a patch in **Health → Pending updates**. Nothing is applied until you accept it.

## Learn more

* [Core concepts](getting-started/concepts.md): customers, connectors, connections, workflows and triggers.
* [Authentication and API keys](tutorials/developer/authentication-and-api-keys.md): test and live keys, and how your backend calls fastn.
* [REST API reference](reference/rest/README.md) and [SDK](reference/sdk/README.md): every endpoint and method.
* [FAQs](reference/faqs.md) and [Glossary](reference/glossary.md).
