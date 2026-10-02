---
description: >-
  Be told when an integration breaks instead of finding out from a customer.
  Set up your own alerts from inside the widget.
hidden: true
---

# Getting Alerted

A sync that stops is worse than a sync that fails loudly: nothing errors, nothing appears in your inbox, and the first signal is a colleague asking why a record never arrived. Alerts close that gap, and you can set them up yourself from inside the widget — no fastn account, no request to your provider.

### Where they live

In the widget header, open the **⋮** menu (_More options_) and choose **Insights**. The panel that opens has your integration metrics at the top and the alerts section below them. With none set up it reads:

> No alerts yet. Create one to be notified when something looks off.

> **Screenshot needed:** the widget header with the **⋮** menu open, showing the **Insights** item. Capture in the embedded widget (end-user token), not the dashboard preview.

> **Screenshot needed:** the **Insights** modal scrolled to the alerts section below the divider, with one alert card expanded so the metric, comparator, threshold, window and recipient fields are all visible.

{% hint style="info" %}
**No ⋮ menu, or no Insights in it?** Insights lives in that menu and is on by default, but an older widget configuration can leave it hidden. If it is not there, contact your SaaS provider — this is the only place alerts for your organization can be set up, so there is no alternative route they can use on your behalf.
{% endhint %}

### Creating one

Add an alert and you get a card you edit in place. Each card is one rule:

1. **Name it** for what it means to you — _Orders stopped arriving_ beats _Alert 1_.
2. **Pick the metric** you want watched.
3. **Set the comparison** — above or below — and a number.
4. **Pick the window** the metric is measured over: 1 hour, 24 hours, 7 days or 30 days.
5. **Add at least one recipient.** An alert with no recipients notifies nobody.
6. **Enable it.** A new alert is created **paused** and will not fire until you flip the toggle on the card. Its tooltip reads _Paused - click to enable_.

{% hint style="danger" %}
**A new alert is paused, and the card saves as you type.** Those two together are the trap: edits persist the moment you make them, with no Save button to confirm and nothing to cancel — but completing every field still leaves the rule **paused** until you flip the toggle. A card you filled in and walked away from is not watching anything. If you created one by accident, delete it; closing the panel leaves it behind.
{% endhint %}

### What you can watch

| Metric | Measures | Unit |
| --- | --- | --- |
| **Error rate** | Percent of runs that failed in the window. | % |
| **Success rate** | Percent that succeeded — alert when it drops. | % |
| **Failed runs** | Number of runs that failed. | count |
| **Total runs** | Number of runs — alert when activity drops off. | count |
| **Records synced** | Records successfully synced — alert when a sync stalls. | count |
| **Records failed** | Records that failed to sync. | count |
| **Avg run time** | Average run duration. | ms |
| **p95 run time** | Slowest runs — catches tail latency. | ms |
| **Broken connectors** | Connections that are not active right now. | count |
| **Inactive workflows** | Enabled integrations that have not run in the window. | count |

{% hint style="warning" %}
Watch the unit when you type a threshold. **Error rate above 5** means five _percent_. Switch to **Failed runs** and the same 5 means five _runs_ — a much tighter trigger than it looks. The run-time metrics are in milliseconds, so a five-second threshold is `5000`.
{% endhint %}

### Where it gets delivered

| Channel | What you provide |
| --- | --- |
| **Email** | One or more addresses. |
| **Slack** | An Incoming Webhook URL — there is no Slack app to connect here, you paste the URL. |
| **Webhook** | An endpoint of your own — route it into whatever you already use. |

> **Screenshot needed:** the delivery section of one alert card showing the Slack Incoming Webhook URL field, the email list and the webhook list, with the **Send test** button visible.

Each card has a **Send test** button that posts a sample through whatever channels you have configured. It is disabled until you add one — the tooltip says _Add a channel first_ — and it is the fastest way to confirm a Slack URL or webhook actually works, rather than waiting for a real failure to find out.

### A starting set

Three alerts cover most of what actually goes wrong:

| Alert | Catches |
| --- | --- |
| **Failed runs** above 0 over 1 hour | Something is erroring right now. |
| **Total runs** below 1 over 24 hours | A sync stopped running entirely — the failure that is otherwise silent. |
| **Broken connectors** above 0 | An app's authorization expired, before anyone notices missing data. |

The second one is the one people skip and later wish they had.

### How soon you hear

Threshold alerts are checked **every 15 minutes**, so expect notice within that window rather than instantly. fastn records every firing against the rule, so your provider can see whether an alert is a real signal or a threshold set too tight. If one has been firing every hour since yesterday, the threshold is wrong, not your integration.

Each rule also has a cooldown, so a sustained problem does not turn into a flood of identical messages.

### Who sees what

**Alerts are not shared.** Each organization has its own:

* Alerts you create here watch **your** integrations and notify **your** recipients. Your SaaS provider does not receive them.
* Alerts your provider has set up on their own account do **not** cover you specifically. Them being alerted is not you being alerted.

So if an integration failing matters to you, set up your own rule — do not assume someone upstream is watching on your behalf. If you would rather not manage it, ask your provider to create the alerts against your organization and point them at your address; they can do that from their side.

### What you can do next

* [Viewing Sync Status & History](viewing-sync-status-and-history.md) — what to look at once an alert fires
* [Extending a Pre-Built Integration](extending-a-prebuilt-integration.md) — fixing the configuration that caused it
