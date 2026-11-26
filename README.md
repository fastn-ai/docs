---
description: >-
  Fastn lets your product offer integrations with the apps your customers use.
  You build each integration once, embed it in your product, and Fastn runs it
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

# Welcome to Fastn

Fastn lets your product offer integrations with the apps your customers use, such as HubSpot, Salesforce, and Slack. You build each integration once. Each customer then connects their own accounts from inside your product, and Fastn runs the integration for them, scoped to that customer.

## Get started

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><strong>Build your first integration</strong></td><td>For your team. Describe an integration to an AI agent, then test it. No code needed.</td><td><a href="getting-started/quickstart.md">getting-started/quickstart.md</a></td></tr>
<tr><td><strong>Embed Fastn in your product</strong></td><td>For developers. Mint a token from your backend and render the widget.</td><td><a href="tutorials/developer/embedding-quickstart.md">tutorials/developer/embedding-quickstart.md</a></td></tr>
<tr><td><strong>Using integrations in a product?</strong></td><td>For customers of a product that uses Fastn. Connect your apps and manage your integrations.</td><td><a href="tutorials/end-user/README.md">tutorials/end-user/README.md</a></td></tr>
</tbody></table>

{% hint style="success" %}
**Try it in five minutes, on the free plan.** Sign up at [app.fastn.dev](https://app.fastn.dev), click **Connect your AI tool** in the top bar, and ask Claude or Cursor: *"Using Fastn, when a new contact is created in HubSpot, post their name and email in our #sales Slack channel."* Then run its test, fully mocked, so no real data is touched. Step by step: [Quickstart](getting-started/quickstart.md).
{% endhint %}

**Want to know if Fastn fits your use case?** Ask your AI agent. [Find out if Fastn fits your use case](getting-started/plan-your-integration.md) shows how, in four steps. Or copy this line into your AI tool and it sets itself up for Fastn:

```
Fetch and execute the instructions to set me up for fastn from https://raw.githubusercontent.com/fastn-ai/fastn-claude-plugins/main/agent-setup/prompt.md
```

## The parts

Fastn has four parts:

| Part            | What it does                                                                                      | Who uses it          |
| --------------- | ------------------------------------------------------------------------------------------------- | -------------------- |
| **Dashboard** | The web app at app.fastn.dev where your team builds integrations, sets up the widget, and watches every run | Your team: the people who set up and run integrations |
| **Widget**      | The panel inside your product where a customer connects apps and turns integrations on            | Your customers       |
| **API and SDK** | Register customers, mint embed tokens, run workflows, and read data from your backend              | Your developers      |
| **Fastn Connect** | The MCP gateway for integrations, built for AI agents. One URL gives an agent the connected apps as tools. Every call is checked against your policies, logged, and runs with the right customer's or person's account | Your AI agents, including agents that act for your customers |

## How it works

<figure><img src=".gitbook/assets/overview/fastn-build-once-use-everywhere.svg" alt="Build once, extend per customer, use everywhere. You build an integration once in the Fastn dashboard, from your AI tool through the Fastn MCP server, or with the Fastn agent. Each customer uses it as is or extends it, and their changes stay with that customer. Your product uses it through the widget and API, and your AI agents through the MCP gateway. Fastn runs and maintains it against each customer's apps."><figcaption><p>Build once, extend per customer, use everywhere</p></figcaption></figure>

* **Build once.** Build an integration in the dashboard, from your AI tool through the Fastn MCP server, or by describing it to the Fastn agent. *Benefit:* one build serves every customer, so adding a customer adds no integration work.
* **Extend per customer.** Each customer uses the integration as is, or extends it in the widget: add fields, filter records, change direction, or ask the widget assistant. A customer's changes apply only to that customer. *Benefit:* customers handle their own variations without a fork or a support ticket, and no change can break another customer.
* **Use everywhere.** The same integration runs in your product, through the widget and the API, and for your AI agents, through Fastn Connect, the MCP gateway. *Benefit:* your product and your agents share one set of integrations, credentials, and logs instead of two.
* **Runs and maintains.** Fastn runs every call with that customer's setup, logs it, and sends alerts. When an app's API changes, the maintainer agent proposes a fix, and it applies to every customer once you accept it. *Benefit:* you don't run integration infrastructure, and an API change is one review instead of one fix per customer.

## What Fastn runs for you

Each row is something Fastn does that you would otherwise build and run yourself.

| Differentiator | What Fastn does | What it saves you |
| --- | --- | --- |
| **Sign-in and credentials** | The widget runs each app's own OAuth or API-key sign-in. Fastn stores every credential encrypted, scoped to one customer, and renews OAuth tokens. | Building an OAuth flow per app, a credential store, and token refresh. |
| **Customer isolation** | Your backend mints a short-lived embed token for one customer. The widget, API calls, and runs see only that customer's connections and data. | Building customer separation into every integration, and the risk of one customer's data reaching another. |
| **Connector catalog** | Over 1,000 connectors, each with its actions, auth methods, and webhooks, plus unified APIs that read and write the same object (a contact, a ticket) across every app of a kind. | Writing and maintaining a client for each app's API, and a separate code path per CRM or helpdesk. |
| **Building from a description** | Describe an integration to the Fastn agent (Scale or Enterprise) or to your own AI tool through the Fastn MCP server (every plan), and it picks the connectors, writes the workflow, and tests it. | Hand-writing each workflow, and the developer time each new integration request takes. |
| **Per-customer customization** | Customers change field mappings, filters, and sync direction in the widget, or ask the widget assistant. Changes apply only to that customer. | Custom builds and forks for individual customers. |
| **Running workflows** | Workflows run on a webhook, a schedule, or an app event, synchronously for up to 25 seconds or in the background for long jobs. Fastn handles each app's rate limits, retries transient failures with backoff, and holds deliveries that run out of retries in a dead-letter queue. | Queues, workers, schedulers, retry logic, and rate-limit handling. |
| **Monitoring** | Every event, run, and call to an app is logged per customer. **Health** shows what needs attention, and alerts go out by email, Slack, Microsoft Teams, or webhook. | Building logging, dashboards, and alerting per integration, and finding which customer a failure hit. |
| **API changes** | The maintainer agent watches the apps you use. When a vendor changes something your workflows depend on, it proposes a patch in **Health → Pending updates**. Nothing is applied until you accept it. | Tracking every vendor's changelog, and fixing breakages after customers report them. |
| **AI agent access** | Fastn Connect, the MCP gateway, gives your AI agents one customer's connected apps as tools. Every call is checked against your policies, logged, and runs with that customer's account. | A separate auth and tool layer for your agents, and agents holding raw customer credentials. |

## Learn more

* [Core concepts](getting-started/concepts.md): customers, connectors, connections, workflows, and triggers.
* [Architecture](getting-started/architecture.md): how the parts fit together and how a request flows.
* [Authentication and API keys](tutorials/developer/authentication-and-api-keys.md): test and live keys, and how your backend calls Fastn.
* [REST API reference](reference/rest/README.md) and [SDK](reference/sdk/README.md): every endpoint and method.
* [FAQs](reference/faqs.md) and [Glossary](reference/glossary.md).
