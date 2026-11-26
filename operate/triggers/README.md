---
description: Calling the triggers you have built from your own apps, and checking that they fire.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Triggers

Once a [trigger](../../build/triggers/README.md) exists, it starts your workflows on its own. These pages cover what you do with it after that: call a webhook trigger from your own backend, and check that your triggers fire.

To create or change a trigger, including its routes, schedule and authentication, see [Triggers](../../build/triggers/README.md) under Build.

### Check that triggers fire

* **Events:** Every inbound arrival, such as a webhook call or a scheduled run, with a filter that shows whether your schedules are firing. It is under **Operate → Logs → Events**. An empty Events log when you expected a trigger to fire points to the trigger, not the workflow. [Learn more](../events.md) · [Open in Fastn](https://app.fastn.dev/activity/events)
* **Executions:** Every workflow run, with what started it in the **Triggered by** column, under **Operate → Logs → Executions**. [Learn more](../executions.md) · [Open in Fastn](https://app.fastn.dev/activity/executions)
* **Health:** Any customer's trigger that is not listening, under **Operate → Health → Needs attention**. [Learn more](../health.md) · [Open in Fastn](https://app.fastn.dev/health)
* **The trigger's detail panel:** Failed deliveries with **Replay**, and on a schedule trigger, its status history and failure count, under **Build → Integrations → Triggers**. [Learn more](../../build/triggers/README.md#inspect-a-trigger) · [Open in Fastn](https://app.fastn.dev/integrations?tab=triggers)

### In this section

* [Call a webhook trigger](using-a-webhook-trigger.md): send a request to a webhook trigger from your backend.
