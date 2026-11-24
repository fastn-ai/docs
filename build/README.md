---
description: >-
  Describe an integration in plain words, from your AI tool or the dashboard,
  and fastn builds, tests, and publishes it.
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

# Build

<figure><img src="../.gitbook/assets/lifecycle/fastn-lifecycle-1-build.svg" alt="Stage 1, Build: the integration builder describes the integration and fastn writes and tests it"><figcaption>Where Build fits in the integration lifecycle</figcaption></figure>

## What does it do?

Build turns a plain-language description into a working integration. You say what should happen, for example *when a deal closes in HubSpot, create the customer in Stripe*, and fastn picks the connectors, writes the workflow, proposes the field mappings, and writes and runs test cases. You approve each step, then publish it so your customers can turn it on.

## Who is it for?

| Role | What they use Build for |
| --- | --- |
| **Integration or solutions engineer** | Build and test integrations from a description |
| **Product manager** | Describe an integration and review its plan and test cases, without writing code |
| **Developer** | Read the generated workflow code where code view is on for your organization, and edit it or write it yourself where code editing is also on |

## How do I use it?

{% tabs %}
{% tab title="Your AI tool" %}
Add fastn to Claude, Cursor, Codex, or another MCP client, then ask for the integration in the chat. Your AI tool follows the same steps as the dashboard and asks you to approve each one. It uses no fastn AI credits.

```bash
claude mcp add --transport http fastn https://mcp.fastn.dev/fastn-workspace
```

[Connect your AI tool](mcp-gateway/README.md) · [What happens when you ask](building-from-your-ai-agent.md)
{% endtab %}

{% tab title="fastn agent" %}
Open **Integrations → Create integration → Build with fastn agent** in the dashboard, or type into the prompt on Home, and describe the integration. The fastn agent runs in the browser. It needs a paid plan (Scale or Enterprise) and uses AI credits. On Launch, build from your AI tool instead.

[Build with fastn agent](agent/README.md) · [Create a workflow with the fastn agent, step by step](../tutorials/saas-admin/creating-a-workflow-via-ai.md)
{% endtab %}

{% tab title="Code" %}
Every workflow is a JavaScript module you can test with sample input and version. Reading the code in the workflow editor needs code view to be switched on for your organization (fastn turns it on), and editing it needs code editing as well. Where code view is off, the editor shows diagrams and docs only, and you change a workflow by describing the change to the fastn agent.

[Workflows](workflows/README.md) · [Write a workflow in code](../tutorials/saas-admin/configuring-a-workflow-in-code.md)
{% endtab %}
{% endtabs %}

## Example prompts

Paste these into your AI tool or the fastn agent, and adjust the apps and fields.

| Job | Prompt |
| --- | --- |
| Sync records | *When a deal is closed-won in HubSpot, create a customer in Stripe and post it to Slack.* |
| React to your product | *When an order is created in our app, create the matching sales order in NetSuite.* |
| Schedule | *Every night, copy new Zendesk tickets into a Google Sheet.* |
| Change an integration | *Only sync contacts whose lifecycle stage is customer, and add their company domain.* |
| Check before publishing | *Run the test cases for the order sync and tell me what failed.* |

## The building blocks

| Block | What it is |
| --- | --- |
| [Connectors](connectors/README.md) | The apps your customers can connect, with their actions, auth, and webhooks |
| [Connect your product](../manage/saas-connectors.md) | Your own product's API and webhooks, as the connector that is yours |
| [Workflows](workflows/README.md) | The code that moves and transforms data between apps |
| [Triggers](triggers/README.md) | What starts a workflow: a webhook, a schedule, or an app event |
| [Unified APIs](unified-apis/README.md) | One endpoint per business object (contact, deal, ticket) across many apps |

## Questions?

* New to a screen? **Help (?) → Take a tour** in the dashboard walks you through it.
* Common answers: [FAQs](../reference/faqs.md) and [Troubleshooting](../operate/troubleshooting.md).
* Stuck? **Help (?) → Contact support** in the dashboard reaches the team.

## Works with

* [Embed](../embed/README.md): put what you build in front of your customers.
* [Test and release](workflows/lifecycle.md): test, publish, and deploy across environments.
* [Operate](../operate/overview.md): watch every customer's integrations once they are live.

## All Build pages

Build is where integrations are made. The pages follow the **Build** section of the dashboard sidebar: **Connect your product** and **Integrations**.

Four of them match a tab under **Build → Integrations**: Connectors, Unified APIs, Workflows, and Triggers. **Connections** lives under **Operate → Connections**, and **Pending updates** is a tab on **Operate → Health**. The fastn agent has no sidebar row: open it from **Integrations → Create integration → Build with fastn agent** or the *What should your customers be able to do?* prompt on Home. *Build from your AI tool*, the *fastn MCP server*, and *Common patterns* have no screen of their own; they cut across several. The **Widget** lives under Embed and is documented under [Embed](../embed/README.md).

{% content-ref url="agent/README.md" %}[Build with fastn agent](agent/README.md){% endcontent-ref %}

{% content-ref url="building-from-your-ai-agent.md" %}[Build from your AI tool](building-from-your-ai-agent.md){% endcontent-ref %}

{% content-ref url="mcp-gateway/README.md" %}[fastn MCP server](mcp-gateway/README.md){% endcontent-ref %}

{% content-ref url="../manage/saas-connectors.md" %}[Connect your product](../manage/saas-connectors.md){% endcontent-ref %}

{% content-ref url="integrations.md" %}[Integrations](integrations.md){% endcontent-ref %}

{% content-ref url="connectors/README.md" %}[Connectors](connectors/README.md){% endcontent-ref %}

{% content-ref url="unified-apis/README.md" %}[Unified APIs](unified-apis/README.md){% endcontent-ref %}

{% content-ref url="workflows/README.md" %}[Workflows](workflows/README.md){% endcontent-ref %}

{% content-ref url="triggers/README.md" %}[Triggers](triggers/README.md){% endcontent-ref %}

{% content-ref url="workflows/lifecycle.md" %}[Test and release](workflows/lifecycle.md){% endcontent-ref %}

{% content-ref url="patterns.md" %}[Common patterns](patterns.md){% endcontent-ref %}
