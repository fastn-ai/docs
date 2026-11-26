---
description: "The Style tab: theme, accent, type, shape and design tokens that match the widget to your brand."
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

# Style

**Embed → Widget** → **Style** tab · [Open in Fastn](https://app.fastn.dev/widgets)

The **Style** tab makes the widget look like part of your product: its colors, fonts, corners and shadows. The live preview updates as you change it.

It has five sub-tabs:

* **[Theme](#theme):** a light or dark base.
* **[Accent](#accent):** your brand color and the text on it.
* **[Type](#type):** font, size, weight and letter spacing.
* **[Shape](#shape):** corner rounding and shadows.
* **[Tokens](#tokens):** individual colors, allowed origins, the Fastn footer and design tokens.

If you already have a design system, the fastest way to match it is **Import from JSON** on the [Tokens](#tokens) sub-tab.

### Theme

**Light** for a light product, **Dark** for a dark one. Every color except your accent color follows from it. If you have set your own surface colors that match neither base, the builder tells you, because picking a theme replaces them.

Status colors can't be changed, so a customer always reads a status such as "failed" correctly, whatever your brand colors are.

### Accent

A pair of colors, with a live contrast readout beside them:

* **Accent:** your brand color. Default `#4F46E5`.
* **Text on accent:** the color of text on top of it. Default `#FFFFFF`.

Set both, and use the readout to check the text is readable before your customers see it.

### Type

| Control            | Values                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------ |
| Font               | `Inter`, `DM Sans`, `Geist`, `Plus Jakarta Sans`, `Nunito`, `Manrope`, `System UI`, `Custom…`   |
| **Base size**      | 11 to 18px                                                                                      |
| **Font weight**    | Light, Regular, Medium                                                                          |
| **Letter spacing** | Tight, Normal, Wide                                                                             |

### Shape

Four presets, **Square**, **Rounded**, **Soft** and **Pill**, set how rounded the corners are, on a radius from 0 to 20. If a preset is not quite right, set the radii underneath it yourself:

* **Global radius:** cards, panels and dropdowns.
* **Button radius:** buttons.
* **Input radius:** input fields.

**Shadow strength** is None, SM, MD or LG.

### Tokens

Surface colors, each set on its own: **Background**, **Foreground**, **Card**, **Muted**, **Muted text**, **Border**.

| Control                        | Notes                                          |
| ------------------------------ | ------------------------------------------------ |
| **Allowed Origins**            | Which websites (origins) may embed the widget. |
| **Show 'Powered by fastn'**    | On by default. Hiding it is part of white-label, on the Enterprise plan. |
| **Design Tokens**              | Your styles as `JSON` or `CSS`, plus **Import from JSON**.     |

{% hint style="warning" %}
**Set Allowed Origins before you ship.** It controls which websites can embed your widget, so it is a security setting, not a style one, and it is easy to miss on this sub-tab. Set it to the origins that are actually allowed to embed your widget.
{% endhint %}

**Import from JSON** takes a set of tokens straight from your own design system, which is faster than matching it control by control. The **Design Tokens** block has fifteen variables:

`--primary`, `--primary-foreground`, `--background`, `--foreground`, `--card`, `--muted`, `--muted-foreground`, `--border`, `--radius`, `--radius-button`, `--radius-input`, `--font-family`, `--font-size`, `--font-weight`, `--letter-spacing`
