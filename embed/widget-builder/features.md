---
description: "The Features tab: optional capabilities your customers get inside the widget."
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

Optional capabilities your customers get inside the widget.

**Available now**: **Catalog connectors** and **Workflow Diagram** are off by default; **Generate MCP URL** is on by default.

| Feature                | What it does                                                                         |
| ---------------------- | -------------------------------------------------------------------------------------- |
| **Catalog connectors** | Show all catalog connectors in the widget so customers can browse and connect them.   |
| **Workflow Diagram**   | Shows the generated flow diagram on a workflow inside the widget.                     |
| **Generate MCP URL**   | Lets a customer generate a one-time URL from the header menu that connects an MCP client (Claude, ChatGPT, Cursor and others) to their integrations, with no account. You can disconnect it from the Embed tab. To create the URL from your own product, see [Customer MCP URL](../embedding/customer-mcp-url.md). |

| **App page layout**    | **One tab, side by side** (activity next to the workflows) or **Separate tabs**. |
| **Installations layout** | **Table** (one row per setup) or **Cards** (an expandable card each). |

**Customer access** appears once your workspace has an Instant-tier workflow to pick. Each setting names one such workflow.

| Setting                | What it does                                           |
| ---------------------- | -------------------------------------------------------- |
| **Widget filter**      | A workflow that decides, per customer and user, which integrations show and how: hidden, disabled with a message, offered as an upgrade, or with buttons hidden. |
| **Access check**       | A workflow that answers what the signed-in user may do: connect, disconnect, configure. Anything it does not allow is hidden and refused. |

{% hint style="warning" %}
**Catalog connectors** widens the offer from the integrations you curated to everything public in your catalog. Useful for self-serve products, too broad for most. Decide deliberately.
{% endhint %}
