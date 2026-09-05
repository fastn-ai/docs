---
description: Integrations, layout, style and features of the panel your customers see.
---

# Widget builder

**Widgets** — the Layout, Style and Features tabs. The Embed tab has its [own page](embedding-the-widget.md).

Opening **Widgets** takes you straight into the builder; there is no widget list page. A **Live** badge sits in the header once the widget has been saved, and **Widget actions** ⋯ offers **Reset to defaults**. The sticky footer carries **Reset** and **Save and publish**.

***

## Integrations

Above the tabs, the **INTEGRATIONS** panel lists what appears in the widget, with a count. This panel _is_ the widget list — the offer your customers browse. Everything else on this screen is presentation.

An integration that moves data between two systems shows both logos and a direction marker, such as `Dynamics 365 F&O → BigCommerce B2B outbound →`. A status dot marks each one **draft** or **active**.

### Add Integrations

**Add** opens the **Add Integrations** dialog, with two tabs:

| Tab         | What it offers                                                  |
| ----------- | --------------------------------------------------------------- |
| **Apps**    | **Select connectors** — individual systems from your catalogue. |
| **Unified** | Unified API categories rather than one connector at a time.     |

**Scope:** decides whose credentials the integration uses.

| Scope          | Meaning                                                  |
| -------------- | -------------------------------------------------------- |
| **Org level**  | Default. Connections are shared across the organisation. |
| **User level** | Each customer connects their own account.                |

{% hint style="warning" %}
**Org level** is the default, and it is the wrong default for most embedded products: it shares one set of connections rather than giving each customer their own. If your customers are meant to authorise their own accounts, choose **User level**.
{% endhint %}

### Edit Integration

The pencil on a row opens **Edit Integration**, which is where most of the configuration actually lives.

| Field                      | Notes                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------- |
| **NAME**                   | What the customer sees on the card.                                                         |
| **CONFIGURATION TEMPLATE** | **Edit field mappings & sync rules** — the defaults a customer starts from.                 |
| **Widget enabled**         | Switch. Off hides the integration from the widget without removing it.                      |
| **Activation mode**        | **Single activation** (default) or **Multi-connection**.                                    |
| **Customer visibility**    | **All customers** (default) or **Specific customers**.                                      |
| **Connectors**             | The connectors this integration uses.                                                       |
| **UNIFIED APIS**           | Unified entities this integration uses.                                                     |
| **Workflows**              | Bound automatically on **Save and publish**.                                                |
| **Triggers**               | Each trigger has a gear for its template defaults and for whether the end user may edit it. |
| **Trigger categories**     | Groups triggers for the customer.                                                           |

**Callbacks** send your backend an HTTP call when a customer does something in the widget. There are six:

| Callback                       | Fires when                           |
| ------------------------------ | ------------------------------------ |
| **Customer activates**         | A customer turns the integration on. |
| **Customer deactivates**       | A customer turns it off.             |
| **Customer changes settings**  | A customer edits its configuration.  |
| **Customer creates a trigger** | A customer adds a trigger.           |
| **Customer updates a trigger** | A customer edits one.                |
| **Customer deletes a trigger** | A customer removes one.              |

{% hint style="info" %}
Callbacks are how your own product learns what happened in the widget — a customer activating an integration is usually something your billing, onboarding or support tooling wants to know about.
{% endhint %}

***

## Layout

![The Layout tab](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/widget-builder-layout.jpg)

**Header content**

| Field        | Default                       |
| ------------ | ----------------------------- |
| **Title**    | `Integrations`                |
| **Subtitle** | `Connect your favorite tools` |

**Sections** toggles the blocks your customers see. All three are on by default.

| Section                 | Notes                                                            |
| ----------------------- | ---------------------------------------------------------------- |
| **Header and branding** | Your title, subtitle and accent colour across the top.           |
| **AI assistant**        | The assistant surface inside the widget.                         |
| **Search bar**          | Worth keeping once there are more than about a dozen connectors. |

***

## Style

![The Style tab](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/widget-style.jpg)

Five sub-tabs: **Theme**, **Accent**, **Type**, **Shape**, **Tokens**.

### Theme

**Light** for a white product, **Dark** for a dark one. Everything except your accent colour derives from it. If you have set custom surface colours that match neither base, the UI tells you: picking one replaces them.

{% hint style="info" %}
Status colours are deliberately not themeable. A customer has to read "failed" correctly no matter what brand sits around it.
{% endhint %}

### Accent

A pair, not a single colour: **Accent** (default `#000000`) and **Text on accent** (default `#fff`), with a live contrast readout beside them. Set both — the readout is there so you can check the pairing is legible before your customers do.

### Type

| Control            | Values                                                                                        |
| ------------------ | --------------------------------------------------------------------------------------------- |
| Font               | `Inter`, `DM Sans`, `Geist`, `Plus Jakarta Sans`, `Nunito`, `Manrope`, `System UI`, `Custom…` |
| **Base size**      | 11–18px                                                                                       |
| **Font weight**    | Light, Regular, Medium                                                                        |
| **Letter spacing** | Tight, Normal, Wide                                                                           |

### Shape

Four presets — **Square**, **Rounded**, **Soft**, **Pill** — over a radius of 0–20, with separate card, button and input radii underneath if the preset is not quite right. **Shadow strength** is None, SM, MD or LG.

### Tokens

Surface colours, set individually: **Background**, **Foreground**, **Card**, **Muted**, **Muted text**, **Border**.

| Control                     | Notes                                       |
| --------------------------- | ------------------------------------------- |
| **Allowed Origins**         | Which origins may embed the widget.         |
| **Show 'Powered by fastn'** | On by default.                              |
| **Compact mode**            | Off by default.                             |
| **Design Tokens**           | `JSON` or `CSS`, plus **Import from JSON**. |

{% hint style="danger" %}
**Allowed Origins** is a security control, not a styling one. It sits on the Tokens tab, which is easy to skip. Set it to the origins that are actually allowed to embed your widget before you ship.
{% endhint %}

The **Design Tokens** block exposes fifteen variables:

`--primary`, `--primary-foreground`, `--background`, `--foreground`, `--card`, `--muted`, `--muted-foreground`, `--border`, `--radius`, `--radius-button`, `--radius-input`, `--font-family`, `--font-size`, `--font-weight`, `--letter-spacing`

**Import from JSON** takes a token set straight from your own design system, which is faster than reproducing it control by control.

***

## Features

![The Features tab](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/widget-features.jpg)

Optional capabilities your customers get inside the widget.

**Available now** — both off by default.

| Feature                | What it does                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------ |
| **Catalog connectors** | Shows all catalog connectors in the widget so end users can browse and connect them. |
| **Workflow Diagram**   | Shows the generated flow diagram on a workflow inside the widget.                    |

**Coming soon**

| Feature               | What it will do                                     |
| --------------------- | --------------------------------------------------- |
| **Widget filter**     | Let end users filter widgets by category or status. |
| **Role based access** | Role-based access control per widget.               |

{% hint style="warning" %}
**Catalog connectors** widens the offer from the integrations you curated to everything public in your catalogue. Useful for self-serve products, too broad for most. Decide deliberately.
{% endhint %}
