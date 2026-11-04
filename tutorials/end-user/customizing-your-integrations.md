---
description: >-
  Adjust field mappings, filters and other settings for an integration you've
  set up, through the widget.
---

# Customizing Your Integrations

After connecting an app, you can customize how data moves between it and the product you're using: which fields sync, which records are included, and how records are matched. The AI assistant can handle much of this for you, or you can fine-tune it yourself.

### Opening the configuration

1. Open the integration widget in your product.
2. Find the integration you want to customize and click **Manage**.
3. On the installation you want to change, click **View**.
4. On the **Configuration** row, click **Open**.

The Configuration row summarizes what's set up, for example _Sync · 2 entities · 14 fields mapped_. The **Open** button stays disabled until every account the integration needs is connected (its tooltip reads _Connect every account first_).

#### First-time configuration

If no configuration exists yet, the dialog shows **No configuration found for this widget.** with the note _fastn's agent sets up field mappings and filters for you._ and, for you as a customer, _Ask whoever administers this organization to finish setting it up._

That first pass belongs to your SaaS provider: the button that starts fastn's agent needs an operator role, so it isn't shown to you. Ask them to run it once. After that the configuration exists and everything on this page is yours to adjust.

See [Extending a Pre-Built Integration](extending-a-prebuilt-integration.md) for what you can change yourself, and how to ask the AI assistant for it.

### The configuration dialog

The dialog is titled **Integration Configuration**. Its header shows the configuration's version and the apps it connects.

#### Entity pairs

When the integration moves more than one kind of record, a rail on the left titled **Entity pairs** lists them. Each row names the apps in the direction data moves (for example **HubSpot → Cin7**), with the records and field count underneath (for example _Company → Customer · 12 fields_). A pair that syncs both ways appears once in each direction.

Click a pair to see and edit its settings. Each pair has its own configuration.

#### Tabs

For the selected pair, the dialog has these tabs:

* **Setup** - questions the integration needs you to answer. Shown only when there are some.
* **Field mappings** - which field in one app feeds which field in the other.
* **Filters** - which records are included.
* **Advanced** - how records are matched between the two apps (**Matching strategy** and **Matching keys**).

A small dot on a tab means something there is incomplete.

#### Field mappings

Each mapping row shows the **source field** (where the data comes from) and the **target field** (where it goes), with a plain-language description of what it does.

* To edit a mapping, click the row or its chevron (**Edit mapping**). It opens in place, where you can re-pick either field.
* To remove a mapping, use the trash icon on the row (**Remove mapping**).
* **Required mappings are locked.** They show a lock icon instead of a remove icon; the tooltip explains the mapping is required by this integration and can't be removed.
* To add a mapping that isn't there, click **Add field mapping** at the bottom of the list.

#### Filters

Filters narrow which records sync. For example, you might only want to sync contacts tagged as "Active" or orders above a certain amount. Click **Add filter** to add one.

Each filter row has three parts:

* **Field** - Which field to check (for example "Status", "Amount" or "Email")
* **Operator** - The condition to apply
* **Value** - What to compare against

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

1. Click **Save changes** in the dialog header. Its tooltip reads _Changes apply on the next sync run_.
2. Close the dialog with the **X**.

Your changes don't take effect immediately on existing data. The next time the workflow runs (whether in real time, on a schedule, or started manually), it uses your updated configuration. Data that already synced is not changed retroactively; only new or updated records use the new settings.

If you close the dialog with unsaved changes, it asks **Discard changes?** Click **Discard** to throw them away, or cancel to go back and save.

### Changing the schedule

If the integration runs on a schedule, the installation's **Triggers** row shows it, for example _Every 1 hours_. Click **Open** on that row to see the triggers. Where your provider made the schedule editable, you can change it there; otherwise ask your provider.

### Using the AI assistant for changes

If you're not sure how to adjust the configuration yourself, click the round sparkle button at the bottom right of the widget (**Ask the assistant**) and describe what you want in plain language:

* "Only sync contacts with an email address"
* "Stop syncing orders under $50"
* "Add the phone number field to the sync"

### Viewing workflows

Workflows live inside each integration. Click **Manage** on an integration to see its **Workflows** list. Click a workflow's chevron to open its details, which start on **Executions** (its run history). A **Diagram** tab showing the workflow step by step appears only if your provider turned it on.

### Troubleshooting

* **I don't see a Configuration row**\
  The row appears only when the integration has a configuration (or configuration fields) set up by your provider. With none, there's no row and nothing for you to configure. Your provider decides what's configurable; if you need changes that aren't available, contact the product's support team.
* **The Open button is grayed out**\
  Connect every account the integration needs first (the tooltip reads _Connect every account first_).
* **My changes didn't take effect**\
  Changes apply on the next sync run, not immediately. Check the installation's **Triggers** row for the schedule, then use **Insights** (in the widget's **⋯** menu) to confirm the run after your change succeeded.
* **I want to start over**\
  Open the integration (**Manage**), click **View** on the installation, and use **Delete installation**; then set it up again. This clears the configuration, but rebuilding it with fastn's agent is your provider's to run. Ask them before you clear anything you still depend on.

### What you've done

* Opened the configuration dialog for an integration
* Understood the two paths: provider-run first-time setup vs your own adjustments
* Reviewed and modified field mappings and filters
* Know how to use the AI assistant for configuration changes
* Know that changes apply on the next sync run
