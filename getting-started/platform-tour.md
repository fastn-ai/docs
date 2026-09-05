---
description: A screen-by-screen walk through the dashboard, so you know where everything lives.
---

# Platform tour

### The chrome

The top bar carries five things that follow you everywhere.

| Element               | What it does                                                                        |
| --------------------- | ------------------------------------------------------------------------------------ |
| **Search** (⌘K / Ctrl+K) | Placeholder *Search connectors, workflows, customers*. Results group under CONNECTORS, WORKFLOWS and CUSTOMERS. |
| **Connect to Claude** | Attaches this workspace to an MCP client so an assistant can call your connectors.   |
| **Documentation**     | Opens these docs in a new tab.                                                       |
| **Theme**             | Switches the dashboard between light and dark.                                       |
| **AI credits**        | Reads *AI credits: n of m remaining this month*. Click it for a breakdown by agent and an org total, plus the reset date — quota resets at the start of each calendar month, UTC. |

The account card at the bottom-left switches organisation and opens your profile.

### Where everything lives

| Group     | Item                | Route                              |
| --------- | ------------------- | ------------------------------------ |
| —         | Home                | `/`                                 |
| BUILD     | Integrations        | `/integrations?tab=connectors`      |
|           | Connectors          | `/integrations?tab=connectors`      |
|           | Unified APIs        | `/integrations?tab=unified`         |
|           | Connections         | `/integrations?tab=connections`     |
|           | Workflows           | `/integrations?tab=workflows`       |
|           | Triggers            | `/integrations?tab=triggers`        |
|           | Pending updates     | `/integrations/updates`             |
|           | Widgets             | `/widgets`                          |
| OPERATE   | Activity            | `/activity/*`                       |
|           | Customers           | `/settings/customers`               |
| MANAGE    | Settings            | `/settings/*`                       |
| —         | Profile             | `/profile`                          |

{% hint style="info" %}
The sidebar parent **Integrations** links to its connectors view (`/integrations?tab=connectors`), and its badge shows the number of connectors in your catalogue. **Agent** is the first item under Integrations, at `/agent`; the **What do you want to build?** prompt on Home opens the same screen. Both are worth knowing before you go looking for a page that seems to have moved.
{% endhint %}

### Home

<figure><img src="../.gitbook/assets/home.jpg" alt="The fastn Home screen: a Good evening, Zain greeting, one What do you want to build? prompt box, four suggestion chips, and a Connect to Claude button"><figcaption>Nothing else competes for attention here — no counters, no recent activity.</figcaption></figure>

One prompt box: *What do you want to build?* Type an integration in plain words and fastn routes you to the right agent. Four suggestion chips sit underneath — *Sync TikTok settlements*, *Notify Slack on orders*, *Log errors to Google Sheets* and *Build a Notion connector* — each a starting point you can take as-is or rewrite. **Connect to Claude** sits below them.

### BUILD → Integrations

The BUILD group holds two nav items: **Integrations**, which expands into the six pages below, and **Widgets**.

<figure><img src="../.gitbook/assets/connectors-list.jpg" alt="Integrations → Connectors showing 24 of 354 catalogue cards — AbstractAPI Email Reputation, AbstractAPI Holidays, Adyen, Agile CRM, Aha! — each badged managed and Managed by Fastn, with Import and Create connector top-right"><figcaption>Integrations → Connectors, filtered by connection state, auth type and visibility.</figcaption></figure>

| Page                  | Purpose                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------ |
| **Connectors**        | Every system your customers can authorise. Create, import, connect.                              |
| **Unified APIs**      | One canonical endpoint per business entity, backed by whichever providers you connect.           |
| **Connections**       | Authenticated links between a customer and a system, with auth type and status.                  |
| **Workflows**         | The JavaScript that runs, with editor, tests, executions and API details.                        |
| **Triggers**          | Webhooks, schedules and app events that start workflows.                                         |
| **Pending updates**   | Vendor changes to your integrations, and the fixes proposed for them. Nothing is applied until you accept it. |

**Connect to Claude** — in the top bar, and again on Home — exposes all of this to an AI client. See [MCP gateway](../build/mcp-gateway.md).

### BUILD → Widgets

<figure><img src="../.gitbook/assets/widget-builder-layout.jpg" alt="Widget builder, Layout tab, badged Live, beside a Tablet-width preview: purple Integrations header, Connect your favorite tools, a search box, and TikTok Shop marked Not connected"><figcaption>Left: what you configure. Right: exactly what your customer sees.</figcaption></figure>

The widget builder has four tabs — Layout, Style, Features, Embed — and a live preview that renders at mobile, tablet and desktop widths. A sticky footer carries **Reset** and **Save and publish**; a **Live** badge appears once the widget is saved, and **Widget actions** offers **Reset to defaults**.

### OPERATE → Activity

<figure><img src="../.gitbook/assets/activity-events.jpg" alt="Activity → Events listing repeated Perigon article-alert webhook rows, each tagged webhook, Delivered, timestamped Sep 4, with a Replay link, under chips All 20, Webhook 20, Scheduled 0, Manual 0"><figcaption>Activity → Events, the inbound and outbound record.</figcaption></figure>

| Page             | Answers                                                        |
| ---------------- | -------------------------------------------------------------- |
| **Events**       | What arrived, from where, and was it delivered?                |
| **Traces**       | Which connected systems did a run call, and how slow were they? |
| **Alerts**       | What should page us, and where?                                 |
| **Executions**   | Which runs happened, and how did they end?                      |
| **Sync reports** | What actually changed, record by record?                        |

### OPERATE → Customers

<figure><img src="../.gitbook/assets/customers.jpg" alt="The Customers list holding a single row — testing, identifier testing, 1 connection, Active — beside an All tiers filter, with Create customer top-right and View connections on the row"><figcaption>Every customer using your embedded integrations; this workspace has only a test one.</figcaption></figure>

**Customers** appears as its own item in the OPERATE group, a sibling of Activity rather than a page inside it — though its route is `/settings/customers`, not `/customers`. It lists everyone using your embedded integrations, with columns *Customer*, *Connections* and *Status* — `Active` or `Pending admin activation` — plus **Create customer**, a search box, and **View connections** on each row. Documented with [Operate](../operate/customers.md).

### MANAGE → Settings

**The Settings navigation is scoped to your role.** What you see there depends on who you are in this organisation:

| Role                | Settings contains                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Owner / Admin**   | People, General, API keys, Secrets, Environments, Configs, Database, SaaS Connectors, Billing, Roles, Audit log, Trash |
| **Developer**       | API keys, Secrets, Environments, Configs, Database, Trash                                                 |

Trash is in the sidebar for Owners, Admins and Developers alike, at `/settings/trash`. Two capabilities are gated by role rather than by permission — using the AI assistant, and reading the audit log. Each screen has its own page under [Settings](../manage/README.md).

<figure><img src="../.gitbook/assets/settings-general.jpg" alt="Settings → General: an Organisation block with Name Zain's Organisation and Timezone Asia/Karachi, then Joining by email domain with an empty domain field and Approve automatically off"><figcaption>General is where Settings opens for an Owner — organisation identity first, joining rules second.</figcaption></figure>

### The account card

Bottom-left. It shows who you are and which organisation you are in. The chevron opens [your profile](../manage/profile.md); the up-down arrows open **SWITCH ORGANISATION**, which lists every organisation you belong to with your role in each — Platform Admin, Owner, Admin, Developer or Operator. Everything else in the dashboard is scoped to whichever organisation is selected, so check this first when something you expected to find is missing.
