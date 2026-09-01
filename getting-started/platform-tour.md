---
description: A screen-by-screen walk through the dashboard, so you know where everything lives.
---

# Platform tour

### The chrome

The top bar carries five things that follow you everywhere.

| Element               | What it does                                                                        |
| --------------------- | ------------------------------------------------------------------------------------ |
| **Search** (⌘K / Ctrl+K) | Jumps to a connector, workflow or customer by name.                              |
| **Connect to Claude** | Attaches this workspace to an MCP client so an assistant can call your connectors.   |
| **Documentation**     | Opens these docs in a new tab.                                                       |
| **Theme**             | Switches the dashboard between light and dark.                                       |
| **AI credits**        | How much agent usage is left this period. Detail lives under Settings → Billing.     |

The account card at the bottom-left switches organisation and opens your profile.

### Home

<figure><img src="../.gitbook/assets/home.jpg" alt="fastn home screen"><figcaption></figcaption></figure>

One prompt box: *What do you want to build?* Type an integration in plain words and fastn routes you to the right agent. The suggestion chips underneath are seeded from connectors you already have.

### BUILD → Integrations

The BUILD group holds two nav items: **Integrations**, which expands into the seven pages below, and **Widgets**.

<figure><img src="../.gitbook/assets/connectors-list.jpg" alt="The connectors catalogue"><figcaption>Integrations → Connectors, filtered by connection state, auth type and visibility.</figcaption></figure>

| Page                  | Purpose                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------ |
| **Agent**             | Chat-driven integration builder with a session history sidebar.                                  |
| **Connectors**        | Every system your customers can authorise. Create, import, connect.                              |
| **Unified APIs**      | One canonical endpoint per business entity, backed by whichever providers you connect.           |
| **Connections**       | Authenticated links between a customer and a system, with auth type and status.                  |
| **Workflows**         | The code that runs, with editor, tests, executions and API details.                              |
| **Triggers**          | Webhooks, schedules and app events that start workflows.                                         |
| **Connector updates** | Fixes fastn proposes when an upstream API changes. Nothing applies until you accept it.          |

The sparkle icon in the top bar, and **Connect to Claude** on Home, expose all of this to an AI client — see [MCP gateway](../build/mcp-gateway.md).

### BUILD → Widgets

<figure><img src="../.gitbook/assets/widget-builder-layout.jpg" alt="Widget builder with live preview"><figcaption>Left: what you configure. Right: exactly what your customer sees.</figcaption></figure>

The widget builder has four tabs — Layout, Style, Features, Embed — and a live preview that renders at mobile, tablet and desktop widths.

### OPERATE → Activity and Customers

<figure><img src="../.gitbook/assets/activity-events.jpg" alt="Activity events log"><figcaption>Activity → Events, the inbound and outbound record.</figcaption></figure>

| Page             | Answers                                                        |
| ---------------- | -------------------------------------------------------------- |
| **Events**       | What arrived, from where, and was it delivered?                |
| **Traces**       | Which connected systems did a run call, and how slow were they? |
| **Alerts**       | What should page us, and where?                                 |
| **Executions**   | Which runs happened, and how did they end?                      |
| **Sync reports** | What actually changed, record by record?                        |
| **Customers**    | Who is using your embedded integrations, and are they active?   |

### MANAGE → Settings

Settings expands into People, General, API keys, Secrets, Environments, Configs, Database, Billing, Roles, Audit log and Trash. Customers appears here too, and is documented with [Operate](../operate/customers.md). Each has its own page under [Settings](../manage/README.md).

<figure><img src="../.gitbook/assets/settings-general.jpg" alt="Settings, with the full sub-navigation expanded"><figcaption></figcaption></figure>

### The account card

Bottom-left. It shows who you are and which organisation you are in. The chevron opens [your profile](../manage/profile.md); the up-down arrows switch organisation. Everything else in the dashboard is scoped to whichever organisation is selected, so check this first when something you expected to find is missing.
