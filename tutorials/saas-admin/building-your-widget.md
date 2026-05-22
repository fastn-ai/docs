---
description: >-
  Use the Widget Builder to create an embeddable integration hub add
  integrations, customize layout and style, and preview the customer experience.
---

# Building Your Widget

The widget is what your customers see which is a branded integration portal embedded inside your product where your customers can connect apps, manage workflows, and monitor sync activity. You can configure it visually in the Widget Builder; while your development team handles the embed code separately.

**Prerequisites:** At least one connector configured and one workflow created to see the full experience.

## Exploring the Widget Builder

Click **Widgets** in the top navigation bar and the Widget Builder opens with two panels:

1. The **builder** on the left
2. The **live preview** on the right.

Everything you change on the left updates the preview in real time.

{% hint style="info" %}
Any changes you make in the preview version of your widget does not affect the published widget unless the changes are saved.
{% endhint %}

> **Screenshot:** Full Widget Builder page showing the left builder panel and the right live preview panel side by side.

Through the widget builder, you can control and customize key four areas:

* Layout
* Style
* Features
* Embedding

### Adding integrations to the widget

The left panel starts with an **INTEGRATIONS** section at the top. This controls which connectors and workflows your customers can access through the widget.

1. Click **+ Add** to add an integration.
2. Select from your configured connectors and workflows.
3. Each integration appears as a card with edit (✏️) and delete (🗑) icons.
4. Drag cards to reorder how they appear in the live preview.

> **Screenshot needed:** INTEGRATIONS list showing 3-4 added integrations with their app icons, edit/delete icons, and drag handles.

### 1. Configuring Layout

Click the **Layout** tab in the left panel. This controls the hub's content and structure. The layout sub section consists of the following:

#### Widget Sections

This controls which parts of the widget your customers see and in what order. Six sections are available as follows:

**Header & Branding** — The title bar at the top of the widget showing the title and subtitle you configured above.

**AI Assistant** — This is the customer-facing equivalent of the Build with AI capability.

**Search Bar** — A search field that lets customers filter integrations by name or category.

{% hint style="info" %}
Customers can only see the integrations on the widget that SaaS Admins have enabled through the widget builder.
{% endhint %}

**Apps** — The integration cards showing connected apps with Configure and Disconnect functionality for users.

**Workflows** — The active workflows list and template cards.

**Insights** — Performance metrics and KPI cards.

Drag sections to change the order they appear in the widget. Toggle any section OFF to hide it from customers entirely.

For example, if you don't want customers building their own automations, toggle off **AI Assistant**. If you don't need workflow visibility, toggle off **Workflows**.

The live preview on the right updates immediately as you reorder or toggle sections.

> **Screenshot:** Widget Sections panel within the Layout tab, showing all six sections with drag handles and green toggles. Show the Reset and Save & Publish buttons at the bottom.

#### Header Content

**Title** — The heading your customers see at the top of the widget (e.g., "Integrations").

**Subtitle** — A short description beneath the title (e.g., "Connect your favorite tools").

#### Use Templates

Click **+ Add** to add workflow templates that appear in the Workflows tab of the preview. Each template shows as a card with an option to remove it. When a customer clicks a template in the live widget, it launches an **Integration Agent** session that walks them through setting up the workflow while the AI handles configuration, field mapping, and testing for them.

> **Screenshot:** Layout tab showing Header Content (Title: "Integrations", Subtitle: "Connect your favorite tools") and the Use Templates section with template cards and the + Add button.

### 2. Customizing Style

Click the **Style** tab to match the widget to your product's look and feel. The Style tab has four sub-tabs:

#### Colors

Set the color palette for your widget. Available tokens include: primary, primary-foreground, background, foreground, card, muted, muted-foreground, and border. Adjust each to match your brand.

> **Screenshot needed:** Colors sub-tab showing the color token controls with color pickers.

#### Typography

Control font family, font size, font weight, and letter spacing for the widget text.

#### Shape

Fine-tune corner rounding with three separate radius controls, each with a slider and quick-select presets as follows:

* **Global Radius** — Applied to cards, panels, and dropdowns (e.g., 8px)
* **Button Radius** — Applied to all buttons (e.g., 8px)
* **Input Radius** — Applied to inputs and selects (e.g., 6px)

This also includes radius controls via **Shadow Strength** that consist of four presets i.e.  None, SM, MD, and LG. This controls the drop shadow depth on cards and panels.

> **Screenshot needed:** Shape sub-tab showing the three radius sliders with Square/Rounded/Full presets and the Shadow Strength selector with MD selected.

#### JSON

This sub-tab lets you export and import your full style configuration as code which is useful for sharing with your development team or applying a consistent theme across multiple widgets.

### 3. Embed

The Embed section is where you can find a previewable URL for your widget and is shareable. This also includes two SDKs that your development team can utilize for embedding.

* **NPM React SDK**
* **Headless SDK**

## Using the Live Preview

The right panel on your widget builders shows exactly what your customers will see. Use the controls at the top to test different views:

**Viewport toggles** — Three device icons in the top-right of the preview panel let you switch between phone, tablet, and desktop layouts.

**Preview button** — The **Preview** button opens a full-page preview for detailed inspection.

The preview has three tabs by default:

### 1. Apps

Apps tab shows the integrations your customers can connect to. At the top, a search bar lets them search across all categories. Each integration appears as a card with:

* App icon and name
* Connection status
* Configure button
* Disconnect button

When you click **Configure** on any connected integration in the Apps preview. Two things can happen:

**If no configuration exists yet:** A modal appears prompting "Run the Integration Agent to set up field mappings and filters." Click it and the AI agent handles the setup which is the same agent experience except its running directly inside the widget.

**If configuration already exists:** The Integration Configuration dialog opens.

Below the integration cards, you'll find the **AI Assistant** section where customers can describe what they want to automate and click **Build with AI** to start an agent session.

This is the first thing your customers see when they open the widget.

> **Screenshot:** Apps tab in the preview showing connected integrations (e.g., HubSpot and Gamma with "Connected" labels), Configure/Disconnect buttons, and the AI Assistant prompt at the bottom.

### 2. Workflows

Shows two things:

**Active workflows** — Workflows currently running for this customer. Click the arrow on any workflow to open the **workflow visualizer** which is an interactive node graph showing the full flow logic and nodes. This is the same visualization available in the workflow editor's Docs → Flow tab, but here it's customer-facing so they can understand what's happening with their data.

**Template cards** — The templates you added in the Layout tab. When a customer clicks one, it launches an Integration Agent session that builds and configures the workflow for them through a chat interface. These are more or so suggestions for your customers to try out on your widget.

> **Screenshot needed:** Workflows tab showing an active workflow card and template cards below.

> **Screenshot needed:** Workflow visualizer showing the interactive node graph with labeled node types.

### 3. Insights&#x20;

Shows performance metrics for the customer's integrations with a time-range selector (7 days / 30 days / 90 days).

> **Screenshot:** Insights tab showing KPI cards with the time-range selector.

## Publishing and sharing

When everything looks right in the preview:

1. Click **Save & Publish** at the bottom-left of the builder panel. Your widget hub is now live and ready for embedding.
2. Use **Reset** to discard unsaved changes if needed.

### What you've learned

* How to open the Widget Builder from the Widgets top nav
* How to add, reorder, and manage integrations in the hub
* How to configure Layout
* How to customize Style across four sub-tabs
* How the AI Assistant widget section lets your customers build automations directly inside the widget
* How the three preview tabs work: Apps (connections + AI assistant), Workflows (active + templates + visualizer), Insights (metrics)
* How to publish a widget or reset changes

