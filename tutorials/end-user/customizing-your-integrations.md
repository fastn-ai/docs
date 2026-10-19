---
description: >-
  Configure sync preferences, field mappings, scheduling, and other settings for
  your active integrations through the widget.
hidden: true
---

# Customizing Your Integrations

After connecting an app, you can customize how data flows between it and the product you're using which fields sync, which records are included, and in which direction. The AI assistant can handle most of this for you, or you can fine-tune it yourself.

### Opening the configuration

1. Open the integration widget in your product.
2. Find the connected app you want to customize.
3. Click **Configure**.

What happens next depends on whether the integration has been configured before.

#### First-time configuration

If no configuration exists yet, you'll see **No configuration found for this widget**, with a note that the Integration Agent sets up field mappings and filters for you — and, as a customer, _Ask whoever administers this workspace to finish setting it up._

That first pass belongs to your SaaS provider: starting the agent needs an operator role, so the button is deliberately not shown to a customer session rather than sending you to a permission error. Ask them to run it once. After that the configuration exists and everything on this page is yours to adjust.

See [Extending a Pre-Built Integration](extending-a-prebuilt-integration.md) for what you can change yourself, and how to ask the AI assistant for it.

#### Returning to an existing configuration

If the integration has already been configured (either by the AI or by you previously), clicking Configure opens the **Integration Configuration dialog** directly.

### The configuration dialog

The dialog header shows the sync type (e.g., "Ongoing sync") and how many data types are configured (e.g., "2 entities"). Below the header, you can switch between two views: **Config** and **Plan**.

#### Config view

This is where you review and adjust how data flows.

**Sync direction tabs**

If the integration syncs data in both directions, you'll see sub-tabs for each direction, for example:

* **"HubSpot Company → Cin7 Customer"** (data flowing from HubSpot to Cin7)
* **"Cin7 Customer → HubSpot Company"** (data flowing from Cin7 to HubSpot)

Click a tab to see and edit the field mappings for that direction. Each direction has its own independent configuration.

**Field mappings**

Field mappings control which fields in one app correspond to fields in the other. Each mapping row shows:

* A plain-language description of what it does
* The **source field** (where the data comes from) and the **target field** (where it goes) displayed as paired labels
* A preview of actual values so you can see what data will flow
* A **Change** button to modify the mapping
* A delete icon to remove it

To add a mapping the AI didn't include, click **"Add field mapping"** at the bottom of the list.

**Filters**

Filters let you narrow which records sync. For example, you might only want to sync contacts tagged as "Active" or orders above a certain amount.

Each filter row has three parts:

* **Field** — Which field to check (e.g., "Status," "Amount," "Email")
* **Operator** — The condition to apply
* **Value** — What to compare against

Available operators:

| Operator       | What it does                                                    |
| -------------- | --------------------------------------------------------------- |
| is not empty   | Syncs records where the field has any value                     |
| is empty       | Syncs records where the field is blank                          |
| equals         | Syncs records where the field matches exactly                   |
| does not equal | Syncs records where the field doesn't match                     |
| contains       | Syncs records where the field includes the text                 |
| greater than   | Syncs records where the field is above a number                 |
| is one of      | Syncs records where the field matches any value in a list       |
| is not one of  | Syncs records where the field doesn't match any value in a list |

### Saving your changes

After making adjustments:

1. Click **Save Configuration** at the bottom of the dialog.
2. The footer confirms: **"Changes apply on the next workflow run."**

This means your changes don't take effect immediately on existing data. The next time the automation runs (whether that's in real-time, on a schedule, or manually triggered), it uses your updated configuration. Existing data that has already synced is not retroactively changed and only new or updated records use the new settings.

Click **Cancel** to discard your changes and close the dialog without saving.

### Using the AI assistant for changes

If you're not sure how to adjust the configuration manually, use the AI assistant at the bottom of the widget's Apps tab. Describe what you want in plain language:

* "Only sync contacts with an email address"
* "Stop syncing orders under $50"
* "Add the phone number field to the sync"

Click **Build with AI** and the agent will update the configuration for you.

### Viewing active workflows

Click the **Workflows** tab in the widget to see the automations running on your integrations. Active workflows show as cards, click the arrow on any workflow to open an interactive visual diagram showing how the automation works, step by step. You can trace the flow from trigger to completion and see each decision point along the way.

You'll also see **template cards** for pre-built automations. Click one to launch an AI assistant session that sets it up for you.

### Troubleshooting

* **I don't see a Configure button**\
  Not all integrations support customization. The SaaS company decides what's configurable. If you need changes that aren't available, contact the product's support team.
* **My changes didn't take effect:**\
  Changes apply on the next sync run, not immediately. If the integration runs daily, your changes will be reflected in the next day's sync. The Insights view shows recent activity, so you can confirm the run after your change succeeded — it does not show when the next one is due, so ask your provider if you need the schedule.
* **I want to start over:**\
  Disconnect the app from the Apps tab and reconnect it. This clears the configuration — but rebuilding it with the Integration Agent is your provider's to run, so ask them before you clear anything you still depend on.

### What you've done

* Opened the configuration dialog for a connected integration
* Understood the two paths: AI-assisted first-time setup vs manual adjustment
* Reviewed and modified field mappings and filters
* Know how to use the AI assistant for configuration changes
* Know that changes apply on the next workflow run
