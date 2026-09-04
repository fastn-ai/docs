---
description: The integrations panel your customers see inside your own product.
---

# Widgets

**Widgets**

Everything under Build exists so that this screen can do its job. The widget is the only part of fastn your customers ever touch: they browse the integrations you offer, authorise their own accounts, and configure what syncs — inside your product, under your branding.

<figure><img src="../.gitbook/assets/widget-builder-layout.jpg" alt="The widget builder: a left panel with Layout, Style, Features and Embed tabs over Title and Subtitle fields, beside a tablet-width Live preview showing a purple Integrations header and a TikTok Shop row"><figcaption>Configure on the left, see exactly what the customer sees on the right.</figcaption></figure>

Two pages cover it:

{% content-ref url="widget-builder.md" %}[Widget builder](widget-builder/README.md){% endcontent-ref %}

{% content-ref url="embedding.md" %}[Embedding the widget](embedding/README.md){% endcontent-ref %}

### There is no widget list

**Widgets** in the sidebar opens `/widgets`, which *is* the builder. There is no separate list page: the **INTEGRATIONS** panel inside the builder is the list of what your widget offers. A **Live** badge appears in the builder header once the widget has been saved.

### The preview

The preview renders the widget at **Mobile**, **Tablet** and **Desktop** widths, with **Tablet** selected by default. The tenant selector at the top right, defaulting to **View as admin**, renders the widget as any one of your customers — so you can see their actual connection states rather than a mock-up. **Preview** opens it on its own.

### Saving, and the two Resets

**Save and publish** in the sticky footer pushes changes to the live widget.

{% hint style="warning" %}
The two Resets do different things. **Reset**, beside Save and publish in the footer, discards changes you have not saved. **Widget actions** ⋯ → **Reset to defaults** throws the whole configuration back to its defaults. Check which one you are clicking.
{% endhint %}
