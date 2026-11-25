---
description: Every workflow run that called a connected app.
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

# Traces

`/activity/traces`

Traces is not a tab on the **Operate → Logs** strip. The page is only reachable by opening `/activity/traces` directly.

A trace is recorded for every workflow run that calls a connected app. Where [Executions](executions.md) tells you a run failed, traces are where you look for the external call behind it.

### Controls

**Search traces**, and filters for **All**, **Success**, **Error** and **Pending**.

**Pending** is the state worth watching. A trace that never resolves points at an upstream app that accepted the request and never answered: the failure mode that produces timeouts rather than errors, and the one people find hardest to diagnose.

### When the page is empty

Until a workflow calls a connected app there is nothing here. An empty filter gives you **No traces match**, with:

> A trace is recorded for every workflow run that calls a connected app.

{% hint style="info" %}
The controls above are confirmed, but these docs do not yet show a populated trace row. If your workspace has real traffic and the screen differs from this page, trust the screen.
{% endhint %}

### Traces and timeouts

If a workflow is timing out, look here before raising its execution timeout. A longer timeout treats the symptom. Batching the calls, or moving to the Long tier, treats the cause. See [Executions](executions.md) for the run-level view.
