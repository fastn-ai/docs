---
description: >-
  Describe an integration in plain words, from your AI tool or the dashboard,
  and fastn builds, tests and publishes it.
---

# Build

<figure><img src="../.gitbook/assets/lifecycle/fastn-lifecycle-1-build.svg" alt="Stage 1, Build: the integration builder describes the integration and fastn writes and tests it"><figcaption>Where Build fits in the integration lifecycle</figcaption></figure>

## What does it do?

Build turns a plain-language description into a working integration. You say what should happen, for example *when a deal closes in HubSpot, create the customer in Stripe*, and fastn picks the connectors, writes the workflow, proposes the field mappings, and writes and runs test cases. You approve each step, then publish it so your customers can turn it on.

## Who is it for?

| Role | What they use Build for |
| --- | --- |
| **Integration or solutions engineer** | Turn a customer request into a tested integration the same day |
| **Product manager** | Ship the integration a deal is waiting on, without queueing it for engineering |
| **Developer** | Read the generated workflow code where code view is on for your organization, and edit it or write it yourself where code editing is also on |
| **Founder or CTO** | Say yes to "do you integrate with X?" and keep engineers on the core product |

## How do I use it?

{% tabs %}
{% tab title="Your AI tool" %}
Add fastn to Claude, Cursor, Codex or another MCP client, then ask for the integration in the chat. Your AI tool follows the same steps as the dashboard and asks you to approve each one. It uses no fastn AI credits.

```bash
claude mcp add --transport http fastn https://mcp.fastn.dev/fastn-workspace
```

[Connect your AI tool](mcp-gateway/README.md) · [What happens when you ask](building-from-your-ai-agent.md)
{% endtab %}

{% tab title="Build with AI" %}
Open **Build → Build with AI** in the dashboard, or type into the prompt on Home, and describe the integration. fastn's builder runs in the browser and uses your plan's AI credits.

[Build with AI](agent/README.md) · [Create a workflow with AI, step by step](../tutorials/saas-admin/creating-a-workflow-via-ai.md)
{% endtab %}

{% tab title="Code" %}
Every workflow is a JavaScript module you can test with sample input and version. Reading the code in the workflow editor needs code view to be switched on for your organization (fastn turns it on), and editing it needs code editing as well. Where code view is off, the editor shows diagrams and docs only, and you change a workflow by describing the change to Build with AI.

[Workflows](workflows/README.md) · [Write a workflow in code](../tutorials/saas-admin/configuring-a-workflow-in-code.md)
{% endtab %}
{% endtabs %}

## Example prompts

Paste these into your AI tool or Build with AI, and adjust the apps and fields.

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
| [Connectors](connectors/README.md) | The apps your customers can connect, with their actions, auth and webhooks |
| [Connect your product](../manage/saas-connectors.md) | Your own product's API and webhooks, as the connector that is yours |
| [Workflows](workflows/README.md) | The code that moves and transforms data between systems |
| [Triggers](triggers/README.md) | What starts a workflow: a webhook, a schedule or an app event |
| [Unified APIs](unified-apis/README.md) | One endpoint per business object (contact, deal, ticket) across many apps |

## Questions?

* New to a screen? **Help (?) → Take a tour** in the dashboard walks you through it.
* Common answers: [FAQs](../reference/faqs.md) and [Troubleshooting](../operate/troubleshooting.md).
* Stuck? **Help (?) → Contact support** in the dashboard reaches the team.

## Works with

* [Embed](../embed/README.md): put what you build in front of your customers.
* [Test and release](workflows/lifecycle.md): test, publish and deploy across environments.
* [Operate](../operate/overview.md): watch every customer's integrations once they are live.

## All Build pages

Build is where integrations are made. Ten pages, in roughly the order you meet them.

Four of them match a tab under **Build → Integrations**: Connectors, Unified APIs, Workflows and Triggers. **Connections** lives under **Operate → Connections**, and **Pending updates** is a tab on **Operate → Health**. **Build with AI** has its own sidebar item and is also reached from the Home *What should your customers be able to do?* prompt. *Building from your AI agent*, *MCP gateway* and *Common patterns* have no screen of their own; they cut across several. The **Widget** lives under Embed and is documented under [Embed](../embed/README.md).

{% content-ref url="agent/README.md" %}[Build with AI](agent/README.md){% endcontent-ref %}

{% content-ref url="building-from-your-ai-agent.md" %}[Building from your AI agent](building-from-your-ai-agent.md){% endcontent-ref %}

{% content-ref url="connectors/README.md" %}[Connectors](connectors/README.md){% endcontent-ref %}

{% content-ref url="unified-apis/README.md" %}[Unified APIs](unified-apis/README.md){% endcontent-ref %}

{% content-ref url="connections/README.md" %}[Connections](connections/README.md){% endcontent-ref %}

{% content-ref url="workflows/README.md" %}[Workflows](workflows/README.md){% endcontent-ref %}

{% content-ref url="triggers/README.md" %}[Triggers](triggers/README.md){% endcontent-ref %}

{% content-ref url="connector-updates.md" %}[Pending updates](connector-updates.md){% endcontent-ref %}

{% content-ref url="mcp-gateway/README.md" %}[MCP gateway](mcp-gateway/README.md){% endcontent-ref %}

{% content-ref url="patterns.md" %}[Common patterns](patterns.md){% endcontent-ref %}
