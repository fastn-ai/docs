---
description: >-
  Configure sync preferences, field mappings, scheduling, and other settings for
  your active integrations through the widget.
---

# Customizing Your Integrations

**Prerequisites:** Have at least one app connected in Fastn. Learn more in [Your First Integration](https://docs.fastn.ai/~/revisions/m0hEPQFsdMhQVmegKM0n/fastn/getting-started/your-first-integration).

After connecting an app, some integrations let you customize how they work. Not all do — it depends on how the SaaS company set things up. If customization is available, you'll see configuration options in the widget after connecting.

### What you might be able to customize

Depending on the integration, configuration options can include:

**What data syncs** — Choose which types of data flow between apps. For example, sync only orders above a certain amount, or only contacts in a specific segment.

**Sync direction** — Some integrations support two-way sync. You might choose:

* One-way: data flows from App A to App B only
* Two-way: changes in either app update the other

**Sync frequency** — How often data syncs:

* Real-time (as soon as something changes)
* Scheduled (every hour, daily, weekly)
* Manual (only when you trigger it)

**Field mappings** — Which fields in one app correspond to fields in another. For example, mapping "Company Name" in your CRM to "Organization" in your helpdesk.

**Filters and conditions** — Rules that control which records sync. For example, only sync contacts tagged as "Active" or orders with status "Completed."

> **Screenshot:** Configuration widget showing options like sync direction toggles, frequency dropdowns, and field mapping selectors.

### How to access configuration

1. Open the integration widget in your product.
2. Find the connected app you want to configure.
3. Look for a **Settings**, **Configure**, or **gear icon** button next to the app.
4. The configuration screen opens with the available options.

> **Screenshot:** Widget showing a connected app with a Settings/Configure button highlighted.

{% hint style="info" %}
**Note:** If you don't see a configuration option, the integration may not support customization. The SaaS company decides what's configurable i.e. contact their support team if you need changes that aren't available.
{% endhint %}

### Configuring a dropdown or selection

Some configuration screens show dropdown menus where you pick from options:

**Static options** — A fixed list set by the SaaS company (e.g., "Sync Frequency: Hourly / Daily / Weekly").

**Dynamic options** — A list pulled from your connected app (e.g., a dropdown showing your actual Slack channels, or your Shopify collections). These update based on your account data.

Select the option that matches your needs and save.

> **Screenshot:** Configuration screen showing a dropdown with dynamic options (e.g., a list of the user's actual Slack channels pulled from their connected account).

### Saving configuration

After making your choices:

1. Click **Save** (or **Apply** / **Confirm**).
2. The widget confirms your settings are saved.
3. The integration starts using your new configuration on the next sync.

Changes to sync frequency take effect on the next cycle. If you change from daily to hourly, the next sync runs within the hour. If you change field mappings, existing data isn't retroactively updated — only new or changed records use the new mapping.

### Resetting to defaults

If you want to undo your customization:

1. Open the configuration screen.
2. Look for a **Reset** or **Restore Defaults** option.
3. This reverts all settings to what the SaaS company originally configured.

If no reset option exists, you can disconnect and reconnect the app — this clears your configuration and starts fresh.

### What you've done

* Accessed configuration options for a connected integration
* Understood the types of customization available (data, direction, frequency, fields, filters)
* Configured and saved your preferences
* Know how to reset to defaults if needed
