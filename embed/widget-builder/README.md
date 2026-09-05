---
description: Integrations, layout, style and features of the panel your customers see.
---

# Widget builder

**Widgets** — the Layout, Style and Features tabs. The Embed tab has its [own page](../embedding/README.md).

Opening **Widgets** takes you straight into the builder; there is no widget list page. A **Live** badge sits in the header once the widget has been saved, and **Widget actions** ⋯ offers **Reset to defaults**. The sticky footer carries **Reset** and **Save and publish**.

## Integrations

Above the tabs, the **INTEGRATIONS** panel lists what appears in the widget, with a count. This panel *is* the widget list — the offer your customers browse. Everything else on this screen is presentation.

An integration that moves data between two systems shows both logos and a direction marker, such as `Dynamics 365 F&O → BigCommerce B2B  outbound →`. A status dot marks each one **draft** or **active**.

### Add Integrations

**Add** opens the **Add Integrations** dialog, with two tabs:

| Tab         | What it offers                                                    |
| ----------- | ------------------------------------------------------------------- |
| **Apps**    | **Select connectors** — individual systems from your catalogue.    |
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

The pencil on a row opens **Edit Integration**, which is where most of the configuration actually lives.

| Field                      | Notes                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------- |
| **NAME**                   | What the customer sees on the card.                                                        |
| **CONFIGURATION TEMPLATE** | **Edit field mappings & sync rules** — the defaults a customer starts from.                |
| **Widget enabled**         | Switch. Off hides the integration from the widget without removing it.                     |
| **Activation mode**        | **Single activation** (default) or **Multi-connection**.                                   |
| **Customer visibility**    | **All customers** (default) or **Specific customers**.                                     |
| **Connectors**             | The connectors this integration uses.                                                      |
| **UNIFIED APIS**           | Unified entities this integration uses.                                                    |
| **Workflows**              | Bound automatically on **Save and publish**.                                               |
| **Triggers**               | Each trigger has a gear for its template defaults and for whether the end user may edit it. |
| **Trigger categories**     | Groups triggers for the customer.                                                          |

**Callbacks** send your backend an HTTP call when a customer does something in the widget. There are six:

| Callback                       | Fires when                                       |
| ------------------------------ | -------------------------------------------------- |
| **Customer activates**         | A customer turns the integration on.              |
| **Customer deactivates**       | A customer turns it off.                          |
| **Customer changes settings**  | A customer edits its configuration.               |
| **Customer creates a trigger** | A customer adds a trigger.                        |
| **Customer updates a trigger** | A customer edits one.                             |
| **Customer deletes a trigger** | A customer removes one.                           |

{% hint style="info" %}
Callbacks are how your own product learns what happened in the widget — a customer activating an integration is usually something your billing, onboarding or support tooling wants to know about.
{% endhint %}

### In this section

* [Layout](layout.md)
* [Style](style.md)
* [Features](features.md)
