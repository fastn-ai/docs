---
description: >-
  Where to start with fastn, how an integration goes from build to running for
  your customers, and who does what.
---

# Welcome to fastn

fastn is the embedded integration platform for SaaS: you embed one widget in your product, and your customers connect, customize and run their integrations inside it while fastn keeps them working.

## Start here

Pick the path that matches what you're doing today.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><strong>New to fastn</strong></td><td>The four building blocks, connections, and how a build fits together, in ten minutes.</td><td><a href="getting-started/README.md">getting-started/README.md</a></td></tr>
<tr><td><strong>Build your first integration</strong></td><td>Describe an integration to the agent and get a tested, working workflow.</td><td><a href="getting-started/quickstart.md">getting-started/quickstart.md</a></td></tr>
<tr><td><strong>Embed it in your product</strong></td><td>For developers: render the widget and generate tokens from your backend.</td><td><a href="tutorials/developer/embedding-quickstart.md">tutorials/developer/embedding-quickstart.md</a></td></tr>
<tr><td><strong>Test, deploy and release</strong></td><td>Test cases, versions, environments, and shipping a change safely.</td><td><a href="build/workflows/lifecycle.md">build/workflows/lifecycle.md</a></td></tr>
<tr><td><strong>Monitor and get alerted</strong></td><td>Health, alerts and every customer's runs, in one place.</td><td><a href="operate/health.md">operate/health.md</a></td></tr>
<tr><td><strong>Help for your customers</strong></td><td>Pages you can share with the people using integrations inside your product.</td><td><a href="tutorials/end-user/README.md">tutorials/end-user/README.md</a></td></tr>
</tbody></table>

## How it works

<figure><img src=".gitbook/assets/lifecycle/fastn-lifecycle.svg" alt="The fastn integration lifecycle: who does what across Build, Publish, Embed, Customize, and Run and monitor"><figcaption><p>Five stages, three parties: your team, your customer and fastn</p></figcaption></figure>

{% stepper %}
{% step %}
### Build

Your integration builder describes the integration in plain words, with **Build with AI** in the dashboard, or from your AI tool, such as Claude or Cursor, over MCP. fastn's agent picks the connectors, writes the workflow, and generates and runs test cases. [Build with the agent](build/README.md)
{% endstep %}

{% step %}
### Publish

You save, publish and deploy a version, then add it to your widget's integration catalog and choose what each customer is allowed to change. [Build your widget](tutorials/saas-admin/building-your-widget.md)
{% endstep %}

{% step %}
### Embed

Your developer drops the widget into your product with an iframe or the SDK. Your backend issues a short-lived token per customer, so every connection is scoped to the right customer. [Embed the widget](embed/embedding/README.md)
{% endstep %}

{% step %}
### Customize

Inside your product, each customer connects their own accounts, maps fields to fit how they work, and can ask the widget's AI assistant for a change or an integration that doesn't exist yet. Nothing ships until it is approved. [What your customers see](tutorials/end-user/README.md)
{% endstep %}

{% step %}
### Run and monitor

**Operate → Health** shows what needs attention across every customer, with the fix for each, and alerts you set up there tell you when a run fails. **Operate → Activity** has every customer's events and runs. fastn handles retries, rate limits and token renewal, and its agents catch API changes and propose the fix. [Operate](operate/overview.md)
{% endstep %}
{% endstepper %}

## Two audiences, one platform

| Who                                   | Where they work                                                                                   |
| ------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **You**, the SaaS company using fastn | The fastn dashboard: build integrations, embed the widget, monitor and manage                     |
| **Your customer**                     | The fastn widget inside your product. They never need a fastn account or to sign in to fastn      |

## Words we use

- An **integration** is a connector, a connection, its triggers (app event, schedule or webhook) and the workflow logic around them.
- The **integration catalog** is the set of integrations your customers can turn on in the widget.
- **SaaS company** means you, fastn's customer. **Customer** means your own customer.

The full list is in the [Glossary](reference/glossary.md).

## Need help?

Check the [FAQs](reference/faqs.md) and [Troubleshooting](operate/troubleshooting.md), or [book a demo](https://fastn.ai).
