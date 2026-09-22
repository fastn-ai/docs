---
description: Integrations, layout, style and features of the panel your customers see.
---

# Widget builder

**Widgets**: the Layout, Style and Features tabs. The Embed tab has its [own page](../embedding/README.md).

Opening **Widgets** takes you straight into the builder; there is no widget list page. A **Live** badge sits in the header once the widget has been saved, and **Widget actions** ⋯ offers **Reset to defaults**. The sticky footer carries **Reset** and **Save and publish**.

## Integrations

Above the tabs, the **INTEGRATIONS** panel lists what appears in the widget, with a count. This panel *is* the widget list: the offer your customers browse. Everything else on this screen is presentation.

An integration that moves data between two systems shows both logos and a direction marker, such as `Dynamics 365 F&O → BigCommerce B2B  outbound →`. A status dot marks each one **draft** or **active**.

### Add Integrations

**Add** opens the **Add Integrations** dialog, with two tabs:

| Tab         | What it offers                                                    |
| ----------- | ------------------------------------------------------------------- |
| **Apps**    | **Select connectors**: individual systems from your catalogue.    |
| **Unified** | Unified API categories rather than one connector at a time.        |

**Scope:** decides whose credentials the integration uses.

| Scope          | Meaning                                                        |
| -------------- | ---------------------------------------------------------------- |
| **Org level**  | Default. Connections are shared across the organisation.        |
| **User level** | Each customer connects their own account.                       |

{% hint style="warning" %}
**Org level** is the default, and it is the wrong default for most embedded products: it shares one set of connections rather than giving each customer their own. If your customers are meant to authorise their own accounts, choose **User level**.
{% endhint %}

### Edit Integration

The pencil on a row opens **Edit Integration**, where most of the configuration lives: the configuration template, activation mode, customer visibility, the connectors and their per-connector overrides, the workflows that auto-bind to every connected customer, triggers, and the callbacks that run a workflow when a customer activates or changes something.

It has a page of its own: [Edit Integration](edit-integration.md).

### In this section

* [Edit Integration](edit-integration.md)
* [Layout](layout.md)
* [Style](style.md)
* [Features](features.md)
