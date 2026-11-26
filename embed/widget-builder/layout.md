---
description: "The Layout tab: the widget's header text and the sections your customers see."
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

# Layout

**Embed → Widget** → **Layout** tab · [Open in Fastn](https://app.fastn.dev/widgets)

The **Layout** tab sets what appears around your integrations in the widget: the header text at the top, and which optional sections show. The live preview updates as you change it.

{% hint style="info" %}
**Do this from your AI tool.** Fastn recommends connecting your preferred AI agent, such as Claude, Cursor or VS Code, to the [Fastn MCP server](../../build/mcp-gateway/README.md) and using its tools to update your widget's layout. For example, ask it: *"Change my widget's title to Integrations."* To connect your AI agent, see [Connect your AI tool](../../build/mcp-gateway/README.md#open-the-connect-dialog), or the setup guide for [Claude](../../build/mcp-gateway/claude.md), [Claude Code](../../build/mcp-gateway/claude-code.md), [Cursor](../../build/mcp-gateway/cursor.md), [VS Code](../../build/mcp-gateway/vscode.md) or [any other MCP client](../../build/mcp-gateway/README.md#how-your-ai-tool-connects).
{% endhint %}

### Header content

| Field        | What it is | Default |
| ------------ | ---------- | ------- |
| **Title**    | The heading at the top of the widget. | `Integrations` |
| **Subtitle** | A short line below the title. Leave it empty to hide it. | `Connect your favorite tools` |

### Sections

**Sections** turns the optional parts of the widget on and off. All three are on by default, and a count beside the heading reads **N of 3 shown**. Each row has a switch. You can reorder rows by dragging them, or with the up and down arrows that appear when you hover over a row. A section you turn off reads **Hidden from widget**.

* **Header and branding:** your title, subtitle and accent color across the top. Turn it off if your product already has its own header above the widget.
* **AI assistant:** the widget assistant, an **Ask the assistant** launcher at the bottom right. There a customer can ask questions and change their setup in plain words. Building new integrations from it needs a paid plan.
* **Search bar:** a **Search integrations** field. Worth keeping once there are more than about a dozen connectors.

### Other parts of the widget

These parts of the widget are not on the **Sections** list:

* **Apps list:** the integrations you offer. It is the widget's main content, so it is always shown.
* **Workflows:** shown inside each integration's detail view.
* **Insights:** opens from the menu in the widget's header. It shows the customer's own runs, records processed, connection health and alerts, for **Today**, **7 days** or **30 days**.
