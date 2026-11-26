---
description: >-
  Use the widget builder to choose the integrations your customers see,
  set the layout and style, and preview the customer experience.
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

# Build your widget

The widget is what your customers see: the integrations panel embedded inside your product, where they connect apps and turn integrations on. You configure it visually in the widget builder; your development team handles the embed code separately.

### Before you start

* **Who this is for:** an Owner, Admin, Developer, or Operator. Viewers can open the builder but not change the widget.
* The [Quickstart: your first integration](../../getting-started/quickstart.md), or at least one connector or workflow to offer.

***

### Open the widget builder

In the sidebar, open **Embed → Widget** (`/widgets`). There is no list of widgets: the page is the builder.

The builder opens with two panels: the **Widget builder** on the left, with **Layout**, **Style**, **Features**, and **Embed** tabs, and the **Live preview** on the right. Everything you change on the left updates the preview in real time.

***

### Add integrations to the widget

Below the tabs at the top of the left panel is an **INTEGRATIONS** section. This is the list of integrations your customers can turn on through the widget.

1. Click **Add** to open the **Add Integrations** dialog.
2. Pick connectors on the **Apps** tab, or unified API categories on the **Unified** tab.

**You should see:** each integration as a row with a status dot (**draft** or **active**) and two buttons: **Edit integration** (pencil) and **Delete integration** (trash).

The pencil opens **Edit Integration**, where you set the integration's connectors, workflows, triggers, and callbacks. See [Edit integration](../../embed/widget-builder/edit-integration.md).

{% hint style="warning" %}
**Deleting an integration takes effect immediately.** It disappears from every customer's widget at once, with no draft or publish step, and it cannot be undone.
{% endhint %}

***

### Configure the layout

Click the **Layout** tab. It has two groups.

#### Header content

**Title** - The heading your customers see at the top of the widget (default `Integrations`).

**Subtitle** - A short line beneath the title (default `Connect your favorite tools`). Leave it empty to hide it.

#### Sections

The **Sections** group toggles the optional parts of the widget. A count beside the heading reads **N of 3 shown**. Each row has a switch, and you can reorder rows by dragging or with the up and down arrows that appear on hover.

| Section | What it shows |
| --- | --- |
| **Header and branding** | Your title, subtitle, and accent color across the top. Turn it off if your product already has its own header above the widget. |
| **AI assistant** | The widget assistant: a floating **Ask the assistant** launcher in the bottom-right corner, where a customer can ask questions and change their configuration in plain words. Building new integrations from it needs a paid plan. |
| **Search bar** | A **Search integrations** field. Worth showing once there are more than about a dozen connectors. |

The apps list itself is always shown; it is the widget's core content, not a toggle. Workflows appear inside each integration's detail view, and **Insights** (the customer's own runs, records processed, connection health, and alerts for **Today**, **7 days**, or **30 days**) opens from the menu in the widget's header.

A hidden section reads **Hidden from widget**, and the live preview updates immediately as you reorder or toggle sections.

***

### Customize the style

Click the **Style** tab to match the widget to your product. It has five sub-tabs:

* **Theme** - **Light** or **Dark** as the base. Everything except your accent color derives from it.
* **Accent** - **Accent** (default `#4F46E5`) and **Text on accent** (default `#FFFFFF`), with a live contrast readout.
* **Type** - Font, base size, font weight, and letter spacing.
* **Shape** - Corner rounding presets plus **Global radius** (cards, panels, and dropdowns), **Button radius**, **Input radius**, and **Shadow strength** (None, SM, MD, or LG).
* **Tokens** - Individual surface colors, **Allowed Origins**, **Show 'Powered by fastn'** (hiding it is part of white-label, on the Enterprise plan), and the **Design Tokens** block with **Import from JSON**, so you can apply your own design system in one step.

{% hint style="danger" %}
**Allowed Origins** on the Tokens sub-tab is a security control, not a styling one. Set it to the origins that are actually allowed to embed your widget before you ship.
{% endhint %}

For every control, see [Style](../../embed/widget-builder/style.md).

***

### Turn on features

Click the **Features** tab. It has two groups.

**Available now:**

* **Catalog connectors** - Show all catalog connectors in the widget so customers can browse and connect them. Off by default.
* **Workflow Diagram** - Show the generated flow diagram on a workflow in the widget. Off by default.
* **Generate MCP URL** - Let a customer generate a one-time URL from the header menu that connects an MCP client (Claude, ChatGPT, Cursor, and others) to their integrations, with no account. On by default.
* **App page layout** - **One tab, side by side** (activity next to the workflows) or **Separate tabs**.
* **Installations layout** - **Table** (one row per setup) or **Cards** (an expandable card each).

**Customer access** (shown once your workspace has an Instant-tier workflow to pick):

* **Widget filter** - A workflow that decides, per customer and user, which integrations show and how: hidden, disabled with a message, offered as an upgrade, or with buttons hidden.
* **Access check** - A workflow that answers what the signed-in user may do: connect, disconnect, or configure. Anything it does not allow is hidden and refused.

See [Features](../../embed/widget-builder/features.md).

***

### Use the live preview

The right panel shows what your customers see. The toolbar reads **Live preview** · *what your customer sees*, and has these controls:

**Mobile / Tablet / Desktop** - A segmented control that switches the preview width. **Tablet** is selected by default.

**Customer selector** - Reads **View as admin** until you pick a customer. Pick one to render the widget with that customer's real connection states rather than a mock-up. The assistant launcher stays disabled until a customer is picked.

**Preview** - Opens the widget full page in a new tab (`/widgets/hub`), for the customer you picked. It needs a fastn login, so it is for you and your team, not a link to send to a customer.

In the preview, each integration shows its app icons and name, its connection status, and a single action: **Connect** if the customer has not set it up yet, or **Manage** once they have. When the apps list is the only tab, the tab bar is hidden. At the bottom, the **Powered by fastn** footer shows unless you turned it off on the Tokens sub-tab.

***

### Publish and share

The builder header shows a badge: **Live** when everything is saved, **Unsaved changes** while you have edits pending. The sticky footer carries three buttons:

1. **Save and publish** (on the right) publishes your changes to the live widget.
2. **Discard changes** appears only while you have unsaved edits. It puts the builder back to the configuration that is published right now; nothing your customers see changes.
3. **Reset** (on the left) is not undo. It opens **Reset widget to defaults?**, and after you type `RESET` it throws away the whole configuration (sections, integrations, templates, and theme) and publishes the defaults to every customer using the widget, immediately. It cannot be undone. **Widget actions** ⋯ → **Reset to defaults** in the builder header does the same thing.

#### Hand off to your developers

Click the **Embed** tab. It has three sub-tabs: **Iframe**, **SDK**, and **A2A** (marked coming soon).

* **Iframe** - Pick a customer in the **User** dropdown and copy the **Embed Code** block. The snippet carries a live token so you can try it at once; for production, your developers mint short-lived tokens from your backend. Tokens last eight hours. This sub-tab also creates **Shareable links** for a customer, when you need to put the widget in front of them before the embed ships.
* **SDK** - Four variants: **Connect card**, **React component**, **Script tag**, and **Build your own UI**, each with a code block. All but **Script tag** (a hosted bundle) also show an install command.
* **A2A** (coming soon).

Hand this off to your development team. See the [Embedding quickstart](../developer/embedding-quickstart.md) in the Developer tutorials for the token generation and iframe setup.

***

### What you've learned

* How to open the widget builder from **Embed → Widget**
* How to add, edit, and delete the integrations your widget offers
* How to configure Layout: header content and the three optional Sections (show, hide, and reorder)
* How to customize Style across five sub-tabs: Theme, Accent, Type, Shape, and Tokens
* Which features you can turn on, and the Customer access workflows
* How to use the live preview: widths, the customer selector, and the full-page Preview
* How Save and publish, Discard changes, and Reset differ, and how to hand off the Embed tab to your developers

### Next steps

* Embed the widget in your product: [Embedding quickstart](../developer/embedding-quickstart.md).
* Before you ship: [Go-live checklist](../../embed/embedding/production-checklist.md).
