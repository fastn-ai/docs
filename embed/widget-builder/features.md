---
description: "The Features tab: optional features your customers get in the widget, and workflows that decide what each customer can see and do."
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

# Features

**Embed → Widget** → **Features** tab · [Open in Fastn](https://app.fastn.dev/widgets)

The **Features** tab turns on optional features your customers get inside the widget, and lets you choose workflows that decide what each customer can see and do.

### Available now

* **Catalog connectors:** shows all catalog connectors in the widget, so customers can browse and connect them. Off by default.
* **Workflow Diagram:** shows the generated flow diagram of a workflow inside the widget. Off by default.
* **Generate MCP URL:** lets a customer generate a one-time URL from the widget's header menu. The URL connects an MCP client (Claude, ChatGPT, Cursor and others) to their integrations, with no account. You can disconnect it from the Embed tab. On by default. To create the URL from your own product, see [Customer MCP URL](../embedding/customer-mcp-url.md).
* **App page layout:** **One tab, side by side** (activity next to the workflows) or **Separate tabs**.
* **Installations layout:** **Table** (one row per setup) or **Cards** (an expandable card each).

**Catalog connectors** changes what you offer: instead of only the integrations you chose, customers see everything public in your catalog. That suits self-serve products, but is too broad for most. Turn it on only if you mean to offer your whole catalog.

### Customer access

**Customer access** appears once your organization has a workflow on the [Instant tier](../../build/workflows/README.md#execution-tiers) to pick. Each setting names one such workflow:

* **Widget filter:** a workflow that decides, for each customer and user, which integrations show and how: hidden, disabled with a message, offered as an upgrade, or shown with buttons hidden.
* **Access check:** a workflow that answers what the signed-in user may do: connect, disconnect or configure. Anything it does not allow is hidden and refused.
