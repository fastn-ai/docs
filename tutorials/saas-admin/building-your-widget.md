---
description: >-
  Use the widget builder to choose the integrations your customers see,
  set the layout and style, preview the result and publish it.
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

Set up the widget your customers use inside your product: choose its integrations, match it to your brand, check it in the preview and publish it.

The [widget](../../embed/widget-builder/README.md) is a ready-made integrations page that you embed in your product. You set it up in the widget builder, with no code. Your developers then embed it in your product.

### Before you start

* **Who this is for:** an Owner, Admin, Developer or Operator. Viewers can open the builder but can't change the widget.
* **Something to offer:** at least one connector or workflow. If you don't have one yet, follow the [Quickstart: your first integration](../../getting-started/quickstart.md), or build one with your AI tool through the [Fastn MCP server](../../build/mcp-gateway/README.md) (recommended) or with the [Fastn agent](../../build/agent/README.md).

### Open the widget builder

1. In the sidebar, go to **Embed → Widget** ([Open in Fastn](https://app.fastn.dev/widgets)).

**You should see:** the builder. On the left, the **Layout**, **Style**, **Features** and **Embed** tabs with the **INTEGRATIONS** panel below them. On the right, the **Live preview**. There is no list of widgets: the page is the builder.

### Add integrations

The **INTEGRATIONS** panel is the list of integrations your customers can turn on in the widget.

1. Under **INTEGRATIONS**, select **Add** to open the **Add Integrations** dialog.
2. Pick connectors on the **Apps** tab, or unified API categories on the **Unified** tab.

**You should see:** each integration as a row with a status dot (**draft** or **active**), a pencil (**Edit integration**) and a trash (**Delete integration**).

Deleting an integration removes it from every customer's widget at once, and it cannot be undone. See [Delete an integration](../../embed/widget-builder/edit-integration.md#delete-an-integration).

### Set up each integration

1. Select the pencil on an integration's row to open **Edit Integration**.
2. Choose its connectors, the workflows each customer gets, its triggers and its callbacks. For every setting, see [Edit integration](../../embed/widget-builder/edit-integration.md).
3. Select **Save & Publish**, or **Save draft** to keep it a draft.

**You should see:** the dialog close, and the integration's row in the **INTEGRATIONS** panel.

### Set the layout

1. Select the **Layout** tab.
2. Change the **Title** and **Subtitle** if you want different header text.
3. Under **Sections**, turn **Header and branding**, **AI assistant** and **Search bar** on or off, and drag them into the order you want.

**You should see:** the live preview update as you change each setting. For every option, see [Layout](../../embed/widget-builder/layout.md).

### Match your brand

1. Select the **Style** tab.
2. On **Theme**, pick **Light** or **Dark** to match your product.
3. On **Accent**, set your brand color and the text color on it, and check the contrast readout.
4. Adjust **Type** and **Shape** if you need to. If you have a design system, use **Import from JSON** on **Tokens** instead.
5. On **Tokens**, set **Allowed Origins** to the websites that may embed your widget. See [Tokens](../../embed/widget-builder/style.md#tokens) for why this matters.

**You should see:** the live preview in your colors and fonts. For every control, see [Style](../../embed/widget-builder/style.md).

### Turn on features

1. Select the **Features** tab.
2. Turn on the features you want customers to have, such as **Workflow Diagram**.
3. If you want a workflow to decide what each customer can see and do, pick it under **Customer access**.

**You should see:** the features you turned on in the live preview, where they apply. For what each feature does, see [Features](../../embed/widget-builder/features.md).

### Preview it as a customer

1. In the **Live preview** toolbar, switch between **Mobile**, **Tablet** and **Desktop** to check each width.
2. Open the customer selector, which reads **View as admin**, and pick a customer.
3. Optionally, select **Preview** to open the widget full page in a new tab.

**You should see:** the widget with that customer's real connections, with **Connect** on integrations they haven't set up and **Manage** on those they have. For every preview control, see [Live preview](../../embed/widget-builder/README.md#live-preview).

### Publish your changes

1. Select **Save and publish** in the footer.

**You should see:** the badge in the builder header change from **Unsaved changes** to **Live**.

To drop edits you haven't published, use **Discard changes**. Don't use **Reset** for that: it replaces your whole widget with the defaults for every customer. See [Save, discard and reset](../../embed/widget-builder/README.md#save-discard-and-reset).

### Hand off to your developers

1. Select the **Embed** tab.
2. Pick a customer in the **User** dropdown. If you have no customers yet, the snippet uses placeholders until you create one.
3. Share the **Iframe** or **SDK** code with your developers.

**You should see:** the **Embed Code** block for the customer you picked. The snippet has a live token so you can try it straight away. For production, your developers create short-lived tokens from your backend. See [Embed the widget](../../embed/embedding/README.md).

### What's next

* Embed the widget in your product: [Embedding quickstart](../developer/embedding-quickstart.md).
* Before you ship: [Go-live checklist](../../embed/embedding/production-checklist.md).
