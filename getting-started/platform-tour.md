---
description: A screen-by-screen walk through the dashboard, so you know where everything lives.
---

# Platform tour

### The top bar

The top bar carries the same controls on every screen.

| Element | What it does |
| --- | --- |
| **Search** (⌘K / Ctrl+K) | Finds connectors, workflows and customers. Results are grouped by type. The action **Connect fastn to your AI tool** is here too. |
| **Help** (?) | **Take a tour** of the current page, **Documentation** (these docs) and **Contact support**. |
| **Theme** | Switches the dashboard between light and dark. |
| **Report a bug** | Sends a bug report to fastn. |
| **Connect AI tools** | Connects Claude, Cursor, ChatGPT or any MCP client to fastn, from any page. Building from your AI tool uses no AI credits. |
| **Credits** | Owners and Admins only. Your AI credits left this month. Click it for a breakdown by agent and the org total. Credits reset at the start of each calendar month, UTC. |

The account card at the bottom-left switches organization and opens your profile.

### Where everything lives

The sidebar starts with **Home**, then follows the three steps of putting fastn in your product: **Build**, **Embed** and **Operate**. **Settings** sits in its own unlabeled group at the end. Every item in a step group is a page; the sections inside a page are its tabs. What you see depends on your [role](../manage/roles.md).

| Group | Item | Route | Docs |
| --- | --- | --- | --- |
| | Home | `/` | [Quickstart](quickstart.md) |
| Build | Build with AI | `/agent` | [Build with the agent](../build/agent/README.md) |
| | Connect your product | `/your-product` | [Connect your product](../manage/saas-connectors.md) |
| | Integrations → Connectors | `/integrations?tab=connectors` | [Connectors](../build/connectors/README.md) |
| | Integrations → Workflows | `/integrations?tab=workflows` | [Workflows](../build/workflows/README.md) |
| | Integrations → Triggers | `/integrations?tab=triggers` | [Triggers](../build/triggers/README.md) |
| | Integrations → Unified APIs | `/integrations?tab=unified` | [Unified APIs](../build/unified-apis/README.md) |
| Embed | Widget | `/widgets` | [Widget](../embed/README.md) |
| | API keys and MCP → API keys | `/access?tab=api-keys` | [API keys](../manage/api-keys.md) |
| | API keys and MCP → MCP server | `/access?tab=mcp` | [Build from Claude, Cursor or any agent](../build/mcp-gateway/README.md) |
| Operate | Customers | `/customers` | [Customers](../operate/customers.md) |
| | Connections | `/connections` | [Connections](../build/connections/README.md) |
| | Health → Needs attention, Overview, Pending updates, Alerts | `/health` | [Operate](../operate/README.md), [Pending connector updates](../build/connector-updates.md), [Alerts](../operate/alerts.md) |
| | Activity → Events, Executions, Sync reports | `/activity/*` | [Activity](../operate/README.md) |
| (own group) | Settings | `/settings/*` | [Settings](../manage/README.md) |

{% hint style="info" %}
**Build with AI** in the sidebar and the **What should your customers be able to do?** prompt on Home open the same builder at `/agent`. See [Build with the agent](../build/agent/README.md).
{% endhint %}

### Home

Home asks one question: **What should your customers be able to do?** (with your product's name in it once fastn knows it). Under it, for roles that can use the builder, a prompt box reads *Describe an integration in plain words…*. Send it and **Build with AI** opens at `/agent` with your request, and fastn's agent starts building it using AI credits.

Below the box, **Ideas** (or **Ideas for** your product) offers up to three suggestions, written for your product where fastn has researched it. Click one to send it to the builder. Roles that cannot use the builder see links to pages instead, such as **Browse connectors** or **View activity**.

To build from Claude, Cursor or another AI tool instead, use **Connect AI tools** in the top bar.

### Your first integration (setup checklist)

Setup has four steps, the same four that onboarding at `/onboarding` walks you through:

| Step | Done when |
| --- | --- |
| **1. Connect your product** | Your own product is registered under **Build** → **Connect your product**. This is admin work: a Developer sees it waiting on an admin and carries on with step 2. |
| **2. Choose integrations** | Your widget offers at least one connector, **Catalog connectors** is on in the widget, or a workflow exists. |
| **3. Embed the widget** | The widget has loaded on a page of your own product, or a customer has connected (which can only happen through the widget). |
| **4. Customers connect and customize** | A customer has connected an app in the widget (a connection to anything other than your own product), or a customer's installation is active. |

Each step is marked from what actually exists in your account, not from a stored checklist, so a step done from your AI tool or another tab ticks over too. Finishing a step earns its onboarding AI credits.

Owners, Admins and Developers see a **Your first integration** pill at the bottom of the left rail, with how many of the four steps are done (for example `1/4`). Click it on any page to open the checklist: each step with a line on what it needs, where to do it in the app, and its docs. The pill goes away once setup is complete.

### Build → Connect your product

Your own product, through its API or webhooks, registered as a connector so your customers' connections to it can be scoped (for example per store or per warehouse). Required before any integration goes live. One-time setup, admin only. See [Connect your product](../manage/saas-connectors.md).

### Build → Integrations

Integrations is the third-party catalog and opens on **Connectors**: an integration starts from the app your customers use. Your own product is not here; it has its own row, **Connect your product**.

| Tab                   | Purpose                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------ |
| **Connectors**        | Every app your customers can authorize. **Create connector** opens one menu: from scratch, Build with AI, build from Claude or any MCP client, or import from a file. **Request connector** asks fastn to add one. |
| **Workflows**         | The JavaScript that runs, with editor, tests, executions and API details.                        |
| **Triggers**          | Webhooks, schedules and app events that start workflows.                                         |
| **Unified APIs**      | One canonical endpoint per business entity, backed by whichever providers you connect.           |

**Connect AI tools**, in the top bar, exposes all of this to Claude, Cursor or another AI client. See [MCP gateway](../build/mcp-gateway/README.md).

### Embed → Widget

The widget builder has four tabs (Layout, Style, Features, Embed) and a live preview that renders at mobile, tablet and desktop widths. A sticky footer carries **Reset**, **Discard changes** (only while you have unsaved edits) and **Save and publish**. **Reset** publishes the defaults to every customer using the widget straight away, after you type `RESET` to confirm; **Widget actions** → **Reset to defaults** does the same. A **Live** badge appears once the widget is saved.

### Embed → API keys and MCP

Two tabs. **API keys** are what your backend uses to mint embed tokens and call the API. **MCP server** adds fastn's integrations to Claude, Cursor, Codex or any MCP client. See [Build from Claude, Cursor or any agent](../build/mcp-gateway/README.md).

### Operate → Customers

<figure><img src="../.gitbook/assets/customers.jpg" alt="The Customers list holding a single row (testing, identifier testing, 1 connection, Active) beside an All tiers filter, with Create customer top-right and View connections on the row"><figcaption>Every customer using your embedded integrations; this workspace has only a test one.</figcaption></figure>

**Customers** lists everyone using your embedded integrations, with columns *Customer*, *Connections* and *Status* (`Active` or `Pending admin activation`), plus **Create customer**, a search box, and **View connections** on each row. Documented with [Operate](../operate/customers.md).

### Operate → Connections

Every connection your customers have made on your connectors, across every customer, with its status. The **My organization** view shows the connections your own organization holds, which your workflows act through. Documented under [Connections](../build/connections/README.md).

### Operate → Health

First under Operate. The maintainer agent watches the apps you connect to, your customers' connections and your workflows; what it finds, with the fix it proposes, is here. The number on **Health** in the left rail is how many vendor changes are waiting on you.

| Tab | Answers |
| --- | --- |
| **Needs attention** | Opens first. Every vendor change waiting for review, every customer connection that expired or failed, and every workflow that failed today, each with its action: **Review**, **Open connection**, or **Runs** and **Fix with AI**. |
| **Overview** | Every customer's integration health in one place: who needs attention, runs and records over time, connection health, what is failing and why. See [Operate](../operate/README.md). |
| **Pending updates** | The full review of each vendor patch the maintainer agent proposes: the diff, accept or refuse. Nothing is applied until you accept it. See [Pending connector updates](../build/connector-updates.md). |
| **Alerts** | What should page us, and where. See [Alerts](../operate/alerts.md). |

### Operate → Activity

| Tab              | Answers                                                        |
| ---------------- | -------------------------------------------------------------- |
| **Events**       | What arrived, from where, and was it delivered?                |
| **Executions**   | Which runs happened, and how did they end?                      |
| **Sync reports** | What actually changed, record by record?                        |
| **Traces**       | Which connected apps did a run call, and how slow were they? Opened from a run, not the tab strip. |

### Settings

**The Settings navigation is scoped to your role.** Each item has a minimum role:

| Minimum role | Settings pages |
| --- | --- |
| **Admin** (and Owner) | People, General, Billing, Roles, Audit log |
| **Developer** and above | Environments, Secrets, Configs, Database, Workflow tags, Trash |

Two capabilities are gated by role rather than by permission: using the builder, and reading the audit log. Each screen has its own page under [Settings](../manage/README.md).

### The account card

Bottom-left. It shows who you are and which organization you are in. The chevron opens [your profile](../manage/profile.md); the up-down arrows open **Switch organization**, which lists every organization you belong to with your role in each: Owner, Admin, Developer, Operator or Viewer (fastn staff show as Platform Admin). Everything else in the dashboard is scoped to whichever organization is selected, so check this first when something you expected to find is missing.
