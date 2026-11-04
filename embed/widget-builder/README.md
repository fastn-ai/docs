---
description: Integrations, layout, style and features of the panel your customers see.
---

# Widget builder

<figure><img src="../../.gitbook/assets/lifecycle/fastn-lifecycle-2-publish.svg" alt="Stage 2, Publish: the product owner adds integrations to the widget catalog and chooses what customers may change"><figcaption><p>Where this fits: stage 2 of the integration lifecycle</p></figcaption></figure>

**Embed → Widget**: the Layout, Style and Features tabs. The Embed tab has its [own page](../embedding/README.md).

Opening **Widget** takes you straight into the builder; there is no widget list page. The header badge reads **Live** when everything is saved and **Unsaved changes** while you have edits pending, and **Widget actions** ⋯ offers **Reset to defaults**. The sticky footer carries **Reset**, **Discard changes** (only while you have unsaved edits) and **Save and publish**.

{% hint style="warning" %}
**Reset** and **Reset to defaults** do the same thing: after you type `RESET` in the **Reset widget to defaults?** dialog, they publish the default configuration to every customer using the widget, immediately, and it cannot be undone. To drop edits you have not saved, use **Discard changes**.
{% endhint %}

## Integrations

Above the tabs, the **INTEGRATIONS** panel lists what appears in the widget, with a count. This panel *is* the widget list: the offer your customers browse. Everything else on this screen is presentation.

An integration that moves data between two systems shows both logos and a direction marker, such as `Dynamics 365 F&O → BigCommerce B2B  outbound →`. A status dot marks each one **draft** or **active**.

### Add Integrations

**Add** opens the **Add Integrations** dialog, with two tabs:

| Tab         | What it offers                                                    |
| ----------- | ------------------------------------------------------------------- |
| **Apps**    | **Select connectors**: individual systems from your catalog.      |
| **Unified** | Unified API categories rather than one connector at a time.        |

On the **Apps** tab, **Scope:** offers **Organization level** (the default, captioned "Shared connections") or **User level** ("Per-customer connections"). The choice is recorded on each integration you create (it sets the integration's sync direction and agent context); it does not share or separate connections. Which customer's connections an integration uses comes from the embed token the widget runs with.

### Edit Integration

The pencil on a row opens **Edit Integration**, where most of the configuration lives: the configuration template, activation mode, customer visibility, the connectors and their per-connector overrides, the workflows that auto-bind to every connected customer, triggers, and the callbacks that run a workflow when a customer activates or changes something.

It has a page of its own: [Edit Integration](edit-integration.md).

### In this section

* [Edit Integration](edit-integration.md)
* [Layout](layout.md)
* [Style](style.md)
* [Features](features.md)
