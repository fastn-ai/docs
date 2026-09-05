---
description: "The Style tab: theme, accent, type, shape and design tokens."
---

# Style

<figure><img src="../../.gitbook/assets/widget-style.jpg" alt="The Style tab on its Theme sub-tab, beside Accent, Type, Shape and Tokens, offering Light and Dark base cards with a note that neither is selected because custom surfaces are set"><figcaption>Status colours stay fixed whichever base you pick, so failed always reads as failed.</figcaption></figure>

Five sub-tabs: **Theme**, **Accent**, **Type**, **Shape**, **Tokens**.

### Theme

**Light** for a white product, **Dark** for a dark one. Everything except your accent colour derives from it. If you have set custom surface colours that match neither base, the UI tells you: picking one replaces them.

{% hint style="info" %}
Status colours are deliberately not themeable. A customer has to read "failed" correctly no matter what brand sits around it.
{% endhint %}

### Accent

A pair, not a single colour: **Accent** (default `#000000`) and **Text on accent** (default `#fff`), with a live contrast readout beside them. Set both — the readout is there so you can check the pairing is legible before your customers do.

### Type

| Control            | Values                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------ |
| Font               | `Inter`, `DM Sans`, `Geist`, `Plus Jakarta Sans`, `Nunito`, `Manrope`, `System UI`, `Custom…`   |
| **Base size**      | 11–18px                                                                                         |
| **Font weight**    | Light, Regular, Medium                                                                          |
| **Letter spacing** | Tight, Normal, Wide                                                                             |

### Shape

Four presets — **Square**, **Rounded**, **Soft**, **Pill** — over a radius of 0–20, with separate card, button and input radii underneath if the preset is not quite right. **Shadow strength** is None, SM, MD or LG.

### Tokens

Surface colours, set individually: **Background**, **Foreground**, **Card**, **Muted**, **Muted text**, **Border**.

| Control                        | Notes                                          |
| ------------------------------ | ------------------------------------------------ |
| **Allowed Origins**            | Which origins may embed the widget.             |
| **Show 'Powered by fastn'**    | On by default.                                  |
| **Compact mode**               | Off by default.                                 |
| **Design Tokens**              | `JSON` or `CSS`, plus **Import from JSON**.     |

{% hint style="danger" %}
**Allowed Origins** is a security control, not a styling one. It sits on the Tokens tab, which is easy to skip. Set it to the origins that are actually allowed to embed your widget before you ship.
{% endhint %}

The **Design Tokens** block exposes fifteen variables:

`--primary`, `--primary-foreground`, `--background`, `--foreground`, `--card`, `--muted`, `--muted-foreground`, `--border`, `--radius`, `--radius-button`, `--radius-input`, `--font-family`, `--font-size`, `--font-weight`, `--letter-spacing`

**Import from JSON** takes a token set straight from your own design system, which is faster than reproducing it control by control.
