---
description: >-
  Change what a pre-built integration does — fields, filters, direction and
  scope — using the agent inside the widget, and know where its authority ends.
hidden: true
---

# Extending a Pre-Built Integration

The integration your SaaS provider shipped is a starting point, not a fixed contract. Most of what it does — which fields move, which records qualify, which direction data flows — is configuration you can change from inside the widget, without a fastn account and without filing a ticket.

This page is about **what you can change and how to ask for it**. For the click-by-click tour of the dialog itself, see [Customizing Your Integrations](customizing-your-integrations.md).

### The two ways in

| Route | Use it when | Where |
| --- | --- | --- |
| **Ask the agent** | You can describe the outcome but not the field names. Fastest for anything involving more than one field. | The **AI assistant** prompt box in the widget |
| **Edit it yourself** | You know exactly which field or filter is wrong. | **Configure** → the Config view |

Both write to the same configuration. Neither needs a developer.

### What the agent will do

The Integration Agent reads the real schemas of both connected apps — the actual fields on your HubSpot account, not a generic template — and rewrites the configuration to match what you asked for.

It is reliable at:

* **Adding or removing a field** — "also sync the phone number", "stop sending the internal notes field"
* **Narrowing what qualifies** — "only contacts with an email address", "skip orders under $50", "only companies in the UK"
* **Fixing a wrong pairing** — "the company name is landing in the wrong field"
* **Adjusting direction** — a per-field **Sync both ways** toggle is right there on each mapping row. Flipping a whole integration to one-way ("only from HubSpot into Cin7") is something only the agent can rewrite, so treat that one as a request rather than a setting
* **Explaining itself** — "what does this integration actually sync?" is a fair question and gets a real answer

#### Worked example

> **You type:** Only sync companies that have a billing country, and add the phone number to the sync.

The agent inspects both schemas, finds the phone field on each side, adds the mapping, and adds a `Billing Country` → `is not empty` filter. The configuration dialog then opens with both changes in place, labelled in plain language, so you can see what it did before you keep it.

If it guesses a field wrong, re-pick the field on that one row rather than re-prompting — you will get there faster. Each row has a field picker on each side and a remove icon.

{% hint style="info" %}
**First time on an integration?** There may be no configuration at all yet. **Configure** then shows _No configuration found for this widget_, with the note that _The Integration Agent sets up field mappings and filters for you_ — and, for a customer, _Ask whoever administers this workspace to finish setting it up._ That first pass is your provider's to run, not yours: the button that starts it needs an operator role, so it is deliberately not offered to a customer session rather than sent to a dead end. Ask them to run it once, and everything below is yours to adjust from then on.
{% endhint %}

### What the agent will not do

Knowing the edges saves you from fighting the tool:

| Request | Why it does not work | What to do instead |
| --- | --- | --- |
| "Connect my Shopify store too" | The apps on offer are chosen by your SaaS provider. The agent configures what is offered, it does not widen the catalogue. | Ask your provider to add the connector |
| "Re-sync everything from last year with the new mapping" | Configuration applies to future runs. Already-synced records are not rewritten. | Ask your provider about a backfill |
| "Run this every 5 minutes instead of hourly" | Schedules belong to the workflow, not the configuration. | Ask your provider |
| "Send me a Slack message when a record fails" | That is an alert, not a mapping. | [Getting Alerted](getting-alerted.md) — you can set this up yourself |
| "Write custom code in the middle of this sync" | Workflow logic is the provider's. | Ask your provider |

The rule of thumb: **the agent changes _what_ data moves and _which_ records qualify. It does not change _when_ the integration runs, _which_ apps exist, or _what logic_ sits between them.**

### After you save

Two things are true of every change, and both surprise people:

* **It applies on the next run, not now.** The Save button's tooltip says so: _Changes apply on the next sync run_. On a daily sync, that means tomorrow.
* **It is not retroactive.** Records already synced keep the values they were given under the old configuration. Only new and updated records use the new settings.

Check the **Insights** view after the next run to confirm it succeeded with your change in place. It shows recent activity and what needs attention; it does not tell you when the next run is due, so if you need that, ask your provider what the schedule is.

### If something is not there

* **No Configure button on an app** — that integration was shipped as fixed. Your provider decides what is configurable.
* **No AI assistant in the widget** — it is a widget section like any other (on by default), and your provider may have switched it off.
* **The change saved but nothing happened** — confirm a run has actually happened since you saved, then check that run in Insights.

In all three cases the answer is the same: contact your SaaS provider's support team, not fastn. They own the widget you are looking at.

### What you can do next

* [Getting Alerted](getting-alerted.md) — be told when an integration breaks instead of discovering it
* [Connecting Claude and other AI clients](connecting-claude.md) — driving your integrations from an AI client
* [Customizing Your Integrations](customizing-your-integrations.md) — the full dialog reference
