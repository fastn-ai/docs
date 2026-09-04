---
description: >-
  fastn is an embedded integration platform. You put it inside your product, and
  your customers get native integrations with the tools they already use.
---

# fastn

You sell software. Your prospects ask whether it talks to their CRM, their ERP, their warehouse system. Building and maintaining those integrations is not your product, but losing deals over them is your problem.

fastn is the layer that answers that question for you. You describe what needs to happen in plain words, fastn's agents pick the connectors and write the workflow, and you drop an integrations panel into your own UI. Your customers authorise their own accounts. You never see their credentials, and you never write an OAuth flow.

<figure><img src=".gitbook/assets/home.jpg" alt="The fastn Home screen: a Good evening, Zain greeting over a What do you want to build? prompt box, four suggestion chips, and a Connect to Claude button"><figcaption>Home is a prompt, not a dashboard — describing the integration is how you start one.</figcaption></figure>

### How the platform is laid out

The left rail groups its navigation under three headings — **BUILD**, **OPERATE**, **MANAGE**. Each heading holds one or two nav items, and those items are what page breadcrumbs in this documentation refer to.

| Rail group  | Nav items          | Sub-pages                                                                                | Who spends time here          |
| ----------- | ------------------ | ------------------------------------------------------------------------------------------ | ----------------------------- |
| **BUILD**   | Integrations       | Agent, Connectors, Unified APIs, Connections, Workflows, Triggers, Pending updates          | Developers and solution teams |
|             | Widgets            | Layout, Style, Features, Embed                                                             | Developers and design         |
| **OPERATE** | Activity           | Events, Traces, Alerts, Executions, Sync Reports                                           | Support and on-call           |
|             | Customers          | —                                                                                          | Support and account teams     |
| **MANAGE**  | Settings           | People, General, API keys, Secrets, Environments, Configs, Database, SaaS Connectors, Billing, Roles, Audit log, Trash | Admins and owners  |

So a page in this documentation headed **Integrations → Connectors** is the Connectors sub-page of the Integrations nav item, under the BUILD group.

### Where to start

{% content-ref url="getting-started/README.md" %}
[Overview](getting-started/README.md)
{% endcontent-ref %}

{% content-ref url="getting-started/quickstart.md" %}
[Quickstart: your first integration](getting-started/quickstart.md)
{% endcontent-ref %}

{% content-ref url="getting-started/concepts.md" %}
[Core concepts](getting-started/concepts.md)
{% endcontent-ref %}

{% content-ref url="reference/faqs.md" %}
[FAQs](reference/faqs.md)
{% endcontent-ref %}

{% hint style="info" %}
Screenshots in these pages come from a development workspace. Names, counts and IDs will differ from yours; the layout will not.
{% endhint %}
