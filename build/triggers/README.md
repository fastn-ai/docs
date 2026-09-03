---
description: What starts a workflow — an inbound webhook, a schedule, or an event from a connected system.
---

# Triggers

**Integrations → Triggers** · `/integrations?tab=triggers`

<figure><img src="../../.gitbook/assets/triggers.jpg" alt="The triggers page"><figcaption></figcaption></figure>

A workflow with no trigger only runs when something calls it. A trigger is what makes it run on its own.

The page splits into three sub-tabs — **Webhooks**, **Schedulers** (`?trigger=scheduler`) and **App events** (`?trigger=app`) — with a status select offering `All statuses`, `Active` and `Disabled`.

### Choosing a type

<figure><img src="../../.gitbook/assets/add-trigger-dialog.jpg" alt="The add trigger dialog"><figcaption></figcaption></figure>

| Type          | Fires when                                                     | Reach for it when                                            |
| ------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| **Webhook**   | Another system calls a URL you give it. Nothing is polled.     | The sender can push, and you want it immediate.               |
| **Schedule**  | A clock you set.                                               | Nightly reconciliation, hourly pulls, anything time-based.    |
| **App event** | Something changes in a connected system.                       | A HubSpot deal moves, a GitHub PR merges.                     |

### Managing triggers

The status select separates active from disabled. Disabling a trigger stops it firing without losing its configuration — the right move while you fix a workflow, and better than deleting it.

### In this section

* [Webhook triggers](webhooks.md)
* [Schedule triggers](schedulers.md)
* [App event triggers](app-events.md)
