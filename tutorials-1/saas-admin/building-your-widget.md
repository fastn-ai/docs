---
description: >-
  Use the Widget Builder to create an embeddable integration hub add
  integrations, customize layout and style, configure embed code, and preview
  the customer experience.
---

# Building Your Widget

**Prerequisites:** At least one connector configured and one workflow created. See [Configuring a Connector](https://claude.ai/chat/configuring-a-connector.md) and [Creating a Workflow in Code](https://claude.ai/chat/creating-a-workflow-in-code.md).

### Opening the Widget Builder

1. Click **Widgets** in the top nav.
2. The Widget Builder opens with two panels: the builder on the left, the live preview on the right.

> **Screenshot needed:** Full Widget Builder page showing both panels.

### Adding integrations

The left panel shows an **INTEGRATIONS** section at the top.

1. Click **+ Add** to add an integration to the hub.
2. Select from your configured connectors and workflows.
3. Each integration appears as a card with edit (✏️) and delete (🗑) icons.
4. Drag to reorder how they appear in the hub.

> **Screenshot needed:** INTEGRATIONS list showing added integrations with edit/delete icons.

### Configuring Layout

Click the **Layout** tab in the left panel:

| Field             | What it sets                                                                                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Title**         | Header text your customers see (e.g., "Integrations")                                                                                                         |
| **Subtitle**      | Subtext below the title (e.g., "Connect your favorite tools")                                                                                                 |
| **Use Templates** | Workflow templates available to your customers. Click **+ Add** to add templates with a name and category (e.g., "Generate discovery deck in Gamma" / Sales). |

Templates appear in the **Workflows** tab of the preview. When a customer clicks a template, it launches an Integration Agent session to set up the workflow.

> **Screenshot needed:** Layout tab showing Title, Subtitle, and Use Templates with added template cards.

### Customizing Style

Click the **Style** tab:

* **Theme presets** — pick a pre-built color scheme
* **Color tokens** — granular control over individual colors (primary, background, text, borders)
* **Typography** — font family and sizes
* **Border radii** — corner rounding
* **Shadows** — drop shadow settings

All style values are exportable as **CSS variables** or **JSON tokens** for consistency with your product's design system.

> **Screenshot needed:** Style tab showing theme presets and color token controls.

### Features (Coming Soon)

Click the **Features** tab:

* **Widget Filter** — let customers filter integrations by category (Coming Soon)
* **RBAC** — role-based visibility control for which integrations customers see (Coming Soon)

### Embedding in your product

Click the **Embed** tab. Two integration methods:

#### Method A: React SDK (drop-in component)

```bash
npm install @fastn/react
```

```jsx
import { FastnHub } from '@fastn/react';

export function IntegrationsPage() {
  return (
    <FastnHub
      token={embedToken}
      theme={{ primary: '#8f85e8' }}
    />
  );
}
```

The `embedToken` is generated from your backend and scopes the widget to a specific customer. Each customer sees only their own connections and data.

#### Method B: Headless SDK (full design freedom)

```bash
npm install @fastn/headless
```

```js
import { createFastnClient } from '@fastn/headless';

const fastn = createFastnClient({
  token: embedToken,
  baseUrl: 'https://live.fastn.ai',
});
```

Use hooks for data:

```jsx
import { useWidgets, useConnections } from '@fastn/headless';

function MyIntegrations() {
  const { widgets } = useWidgets();
  const { connections } = useConnections();
  return ( /* your custom UI */ );
}
```

Trigger actions programmatically:

```js
await fastn.connect(widgetId);        // Connect a widget
await fastn.disconnect(connectionId); // Disconnect
await fastn.configure(widgetId, {     // Open configure chat
  context: 'Sync products with HubSpot',
});
```

> **Screenshot needed:** Embed tab showing the React SDK and Headless SDK code with tab toggles.

#### Which method to choose

|                   | React SDK                   | Headless SDK              |
| ----------------- | --------------------------- | ------------------------- |
| **Setup time**    | Minutes — drop-in component | Hours — build your own UI |
| **Customization** | Theme prop for colors       | Every pixel is yours      |
| **Best for**      | Quick launch, standard look | Custom design, unique UX  |

### Using the Live Preview

The right panel shows what your customers will see. Controls at the top:

* **Viewport toggles** — Mobile / Tablet / Desktop
* **Open full-page preview** — larger view
* **Live Preview** status indicator (green dot)

#### Apps tab

Shows connected integrations as cards with:

* App icon and name
* **Connected** status (green dot)
* **Configure** button — opens the field mapping dialog
* **Disconnect** button

At the bottom: an **AI Assistant card** — "Can't find what you need? Tell AI what you want to automate and it will configure it for you." with a "Build with AI" button.

> **Screenshot needed:** Apps tab in the preview showing connected integrations and the AI assistant card.

#### Workflows tab

Shows:

* **Active workflows** — click the arrow to open the interactive workflow visualizer (node graph with TRIGGER, PROCESS, DECISION, READ, WRITE, DONE nodes)
* **Use Template** cards — click to launch an Integration Agent session

> **Screenshot needed:** Workflows tab showing an active workflow and template cards.

> **Screenshot needed:** Workflow visualizer showing the interactive node graph.

#### Insights tab

Shows KPI cards with a time-range selector (7 days / 30 days / 90 days):

| Card                   | What it shows                       |
| ---------------------- | ----------------------------------- |
| **Runs Today**         | Number of workflow executions today |
| **Records Processed**  | Synced, failed, and skipped counts  |
| **Needs Attention**    | Issues requiring action             |
| **Connectors**         | Connected and broken count          |
| **Most-Used Workflow** | Highest run count workflow          |

> **Screenshot needed:** Insights tab showing KPI cards.

### Configuring integrations

Click **Configure** on any connected integration in the Apps preview:

* If no configuration exists: a modal prompts "Run the Integration Agent to set up field mappings and filters"
* If configuration exists: the **Integration Configuration** dialog opens

#### Integration Configuration dialog

Header shows sync type ("Ongoing sync") and entity count ("2 entities"). Toggle between **Config** and **Plan** views.

**Config view:**

* Bidirectional sub-tabs (e.g., "HubSpot Company → Cin7 Customer" and "Cin7 Customer → HubSpot Company")
* **Field Mappings** — source/target pills, mapping rows with preview values, Change/delete actions, "Add field mapping" link
* **Filters** — "only sync records where" with field, operator, and value. Operators: is not empty, is empty, equals, does not equal, contains, greater than, is one of, is not one of

**Plan view:**

* Shows the Integration Agent-generated plan
* Empty state: "No plan data available yet. Run the Integration Agent to generate a plan."

Footer: "Changes apply on the next workflow run" with Cancel / Save Configuration buttons.

> **Screenshot needed:** Integration Configuration dialog showing bidirectional field mappings with preview values.

> **Screenshot needed:** Filters section showing filter rows with operator dropdown.

### Publishing

When everything looks right:

1. Click **Save & Publish** (bottom-left of the builder panel)
2. Your widget hub is live and ready for embedding

Click **Reset** to discard unsaved changes.

### What you've learned

* How to add and manage integrations in the Widget Builder
* Layout, Style, Features, and Embed configuration
* Two embed methods: React SDK (drop-in) and Headless SDK (custom UI)
* The three preview tabs: Apps, Workflows, Insights
* Integration configuration with bidirectional field mappings and filters
* The workflow visualizer.
