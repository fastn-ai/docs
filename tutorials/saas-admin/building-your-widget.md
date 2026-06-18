---
description: >-
  Use the Widget Builder to create an embeddable integration hub add
  integrations, customize layout and style, and preview the customer experience.
---

# Building Your Widget

The widget is what your customers see — an integration portal embedded inside your product where they connect apps, manage workflows, and monitor sync activity. You configure it visually in the Widget Builder; your development team handles the embed code separately.

**Prerequisites:** Complete [Your First Integration](https://claude.ai/fastn/getting-started/your-first-integration). During the Setup Assistant (Step 4: Embed), you may have already created your first widget. This tutorial covers building or customizing widget hubs beyond that initial setup.

***

### Opening the Widget Builder

Click **Widgets** in the top navigation bar (Home | Integrations | **Widgets** | Activity | Settings).

The Widget Builder opens with two panels: the **builder** on the left and the **live preview** on the right. Everything you change on the left updates the preview in real time.

> 📷 **Screenshot needed:** Full Widget Builder page showing the left builder panel and the right live preview panel side by side.

***

### Adding integrations to the hub

The left panel starts with an **INTEGRATIONS** section at the top. This controls which connectors and workflows your customers can access through the widget.

1. Click **+ Add** to add an integration.
2. Select from your configured connectors and workflows.
3. Each integration appears as a card with edit (✏️) and delete (🗑) icons.
4. Drag cards to reorder how they appear in the hub.

> 📷 **Screenshot needed:** INTEGRATIONS list showing 3-4 added integrations with their app icons, edit/delete icons, and drag handles.

***

### Configuring Layout

Click the **Layout** tab in the left panel. This controls the hub's content and structure.

#### Header Content

**Title** — The heading your customers see at the top of the widget (e.g., "Integrations").

**Subtitle** — A short description beneath the title (e.g., "Connect your favorite tools").

#### Use Templates

Click **+ Add** to add workflow templates that appear in the Workflows tab of the preview. Each template shows as a card with an × to remove it. When a customer clicks a template in the live widget, it launches an **Integration Agent** session that walks them through setting up the workflow — configuring connections, field mappings, and test cases.

> 📷 **Screenshot needed:** Layout tab showing Header Content (Title: "Integrations", Subtitle: "Connect your favorite tools") and the Use Templates section with template cards and the + Add button.

#### Widget Sections

Still within the Layout tab, scroll down to the **Widget Sections** panel. This controls which parts of the widget your customers see and in what order.

The subtext reads: **"Drag to reorder. Toggle to show/hide."**

Six sections are available, each with a drag handle (⠿) and a green toggle switch:

**Header & Branding** — The title bar at the top of the widget showing the title and subtitle you configured above. Toggle OFF to hide the header entirely (useful if your product already has its own header above the widget).

**AI Assistant** — A prompt area in the widget that reads "Can't find what you need?" with the subtext "Tell AI what you want to automate and it will configure it for you." Customers can type a request (e.g., "Sync Shopify orders to my CRM...") and click **Build with AI** to launch an agent session directly inside the widget. This is the customer-facing equivalent of the Build with AI button you use in the Integrations section.

**Search Bar** — A search field ("Search integrations across all categories...") that lets customers filter integrations by name or category.

**Apps** — The integration cards showing connected apps with Configure and Disconnect buttons.

**Workflows** — The active workflows list and template cards.

**Insights** — Performance metrics and KPI cards.

Drag sections to change the order they appear in the widget. Toggle any section OFF to hide it from customers entirely. For example, if you don't want customers building their own automations, toggle off **AI Assistant**. If you don't need workflow visibility, toggle off **Workflows**.

The live preview on the right updates immediately as you reorder or toggle sections.

> 📷 **Screenshot needed:** Widget Sections panel within the Layout tab, showing all six sections with drag handles and green toggles. Show the Reset and Save & Publish buttons at the bottom.

> 🎬 **GIF needed:** Dragging the "AI Assistant" section from its position to above "Apps," then watching the live preview reorder in real time.

> 🎬 **GIF needed:** Toggling off "Search Bar" and watching it disappear from the live preview.

***

### Customizing Style

Click the **Style** tab to match the widget to your product's look and feel. The Style tab has four sub-tabs:

#### Colors

Set the color palette for your widget. Available tokens include: primary, primary-foreground, background, foreground, card, muted, muted-foreground, and border. Adjust each to match your brand.

> 📷 **Screenshot needed:** Colors sub-tab showing the color token controls with color pickers.

#### Typography

Control font family, font size, font weight, and letter spacing for the widget text.

#### Shape

Fine-tune corner rounding with three separate radius controls, each with a slider and quick-select presets (**Square | Rounded | Full**):

* **Global Radius** — Applied to cards, panels, and dropdowns (e.g., 8px)
* **Button Radius** — Applied to all buttons (e.g., 8px)
* **Input Radius** — Applied to inputs and selects (e.g., 6px)

Below the radius controls: **Shadow Strength** with four presets — **None | SM | MD | LG**. This controls the drop shadow depth on cards and panels.

> 📷 **Screenshot needed:** Shape sub-tab showing the three radius sliders with Square/Rounded/Full presets and the Shadow Strength selector with MD selected.

#### Json

This sub-tab lets you export and import your full style configuration as code — useful for sharing with your development team or applying a consistent theme across multiple widgets.

**CSS Variables** — A read-only JSON block showing all your design tokens (colors, radii, typography) as CSS custom properties. Below it, a `:root { }` CSS block with a **Copy** button, labeled "Apply to your container element." Your developers can paste this directly into your product's CSS to match the widget's styling.

**Import from JSON** — Paste a tokens JSON object (e.g., `{ "--primary": "#4F46E5", ... }`) and click **Apply** to set all style values at once. This is useful when you have an existing design system and want to apply it without adjusting each control individually.

> 📷 **Screenshot needed:** Json sub-tab showing the CSS Variables block, the `:root` CSS output with Copy button, and the Import from JSON input area with Apply button.

> 🎬 **GIF needed:** Changing a color in the Colors sub-tab and watching the live preview update in real time.

***

### Features

Click the **Features** tab. A banner reads: **"Coming soon — these features are currently unavailable."**

Two features are listed with greyed-out toggles:

**Widget Filter** — "Let end users filter widgets by category or status." Not yet available.

**RBAC** — "Role-based access control per widget." Not yet available.

These toggles will become active when the features ship. No configuration is needed here for now.

***

### Using the Live Preview

The right panel shows exactly what your customers will see. Use the controls at the top to test different views:

**Viewport toggles** — Three device icons in the top-right of the preview panel let you switch between phone, tablet, and desktop layouts.

**Preview button** — The **⊡ Preview** button opens a full-page preview for detailed inspection.

**Live Preview status** — A green dot with "Live Preview" text in the top-left confirms the preview is syncing with your changes in real time.

The preview has three tabs:

#### Apps tab

Shows the integrations your customers can connect to. At the top, a search bar lets them search across all categories. Each integration appears as a card with:

* App icon and name
* Connection status (green dot + "Connected" label)
* **⚙ Configure** button (dark/filled) — opens the integration configuration dialog (see below)
* **Disconnect** button (outlined)

Below the integration cards, if the **AI Assistant** section is enabled, customers see: "Can't find what you need?" with a text input where they can describe what they want to automate and click **Build with AI** to start an agent session.

At the bottom: **"Powered by fastn"** footer.

This is the first thing your customers see when they open the widget.

> 📷 **Screenshot needed:** Apps tab in the preview showing connected integrations (e.g., HubSpot and Gamma with "Connected" labels), Configure/Disconnect buttons, and the AI Assistant prompt at the bottom.

#### Workflows tab

Shows two things:

**Active workflows** — Workflows currently running for this customer. Click the arrow on any workflow to open the **workflow visualizer** — an interactive node graph showing the full flow logic with TRIGGER, PROCESS, DECISION, READ, WRITE, and DONE nodes. This is the same visualization available in the workflow editor's Docs → Flow tab, but here it's customer-facing so they can understand what's happening with their data.

**Template cards** — The templates you added in the Layout tab. When a customer clicks one, it launches an Integration Agent session that builds and configures the workflow for them through a chat interface.

> 📷 **Screenshot needed:** Workflows tab showing an active workflow card and template cards below.

> 📷 **Screenshot needed:** Workflow visualizer showing the interactive node graph with labeled node types (TRIGGER → PROCESS → DECISION → WRITE → DONE).

#### Insights tab

Shows performance metrics for the customer's integrations with a time-range selector (7 days / 30 days / 90 days). \[VERIFY: what specific KPI cards appear here? Events processed, sync success rate, active connections, error count?]

> 📷 **Screenshot needed:** Insights tab showing KPI cards with the time-range selector.

***

### Configuring an integration

Click **Configure** on any connected integration in the Apps preview. Two things can happen:

**If no configuration exists yet:** A modal appears prompting "Run the Integration Agent to set up field mappings and filters." Click it and the Integration Agent configures the integration — the same agent experience from [Creating a Workflow via AI](https://claude.ai/fastn/tutorials/saas-admin/creating-a-workflow-via-ai), running directly inside the widget.

**If configuration already exists:** The Integration Configuration dialog opens.

#### Integration Configuration dialog

The dialog header shows the sync type (e.g., "Ongoing sync") and entity count (e.g., "2 entities"). You can toggle between two views:

**Config view** — The working configuration:

Bidirectional sub-tabs let you configure each direction separately (e.g., "HubSpot Company → Cin7 Customer" and "Cin7 Customer → HubSpot Company").

**Field Mappings** show source and target fields as paired pills. Each mapping row displays a preview of real values so you can see what data will actually flow. You can:

* Click **Change** to modify a mapping
* Click the delete icon to remove it
* Click **"Add field mapping"** to add a new one the agent didn't include

**Filters** let you narrow which records sync. Each filter row has a field, an operator, and a value. Available operators: is not empty, is empty, equals, does not equal, contains, greater than, is one of, is not one of.

**Plan view** — Shows the Integration Agent's generated plan for this integration. If empty, it shows: "No plan data available yet. Run the Integration Agent to generate a plan."

The footer reads **"Changes apply on the next workflow run"** with **Cancel** and **Save Configuration** buttons.

> 📷 **Screenshot needed:** Integration Configuration dialog showing bidirectional field mappings with source/target pills and preview values.

> 📷 **Screenshot needed:** Filters section showing 2-3 filter rows with the operator dropdown expanded.

***

### Publishing and sharing

When everything looks right in the preview:

1. Click **Save & Publish** at the bottom-left of the builder panel. The widget is published and available to embed.
2. Use **Reset** to discard unsaved changes if needed.

#### Previewing the widget

A **Preview** button at the top-right of the builder opens a full-page preview of the widget — useful for seeing it without the dashboard around it, or for sharing with your team before embedding.

#### Handing off to your developers

Click the **Embed** tab. It has four sub-tabs: **Iframe**, **MCP**, **SDK**, and **A2A** (the last two are marked "coming soon").

* **Iframe** — The current method for embedding the widget into your product. Shows an **Embed Code** block (with a Copy button) containing the iframe snippet. The widget is embedded via an iframe that loads with a short-lived token your developers generate from your backend. The tab notes: "Live token — expires in 15 min. For production, generate tokens from your backend."
* **MCP** — For exposing your integrations as tools to AI agents (the agent use case). See the Developer tutorials.
* **SDK** (coming soon) — A React component (`@fastn/react`) that will wrap the iframe flow.
* **A2A** (coming soon).

Hand this off to your development team — see [Embedding Fastn](https://claude.ai/fastn/tutorials/developer/embedding-fastn) in the Developer tutorials for the token generation and iframe setup.

> 📷 **Screenshot needed:** Embed tab showing the four sub-tabs (Iframe, MCP, SDK, A2A) with the Iframe tab active and the Embed Code block visible.

***

### What you've learned

* How to open the Widget Builder from the Widgets top nav
* How to add, reorder, and manage integrations in the hub
* How to configure Layout — header content, workflow templates, and Widget Sections (drag to reorder, toggle to show/hide)
* How to customize Style across four sub-tabs: Colors (palette), Typography (fonts), Shape (radii + shadow), and Json (export CSS variables, import tokens)
* How the AI Assistant widget section lets your customers build automations directly inside the widget
* How the three preview tabs work: Apps (connections + AI assistant), Workflows (active + templates + visualizer), Insights (metrics)
* How the Integration Agent handles configuration when a customer clicks Configure for the first time
* How to set up bidirectional field mappings and filters in the Configuration dialog
* How to publish, preview the widget, and hand off the Embed tab to your developers
