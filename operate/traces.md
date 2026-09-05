---
description: Every workflow run that called a connected system.
---

# Traces

**Activity → Traces**

A trace is recorded for every workflow run that calls a connected system. Where [Executions](executions.md) tells you a run failed, traces are where you look for the external call behind it.

### Controls

**Search traces**, and filters for **All**, **Success**, **Error** and **Pending**.

**Pending** is the state worth watching. A trace that never resolves points at an upstream system that accepted the request and never answered — the failure mode that produces timeouts rather than errors, and the one people find hardest to diagnose.

### When the page is empty

Until a workflow calls a connected system there is nothing here. An empty filter gives you **No traces match**, with:

> A trace is recorded for every workflow run that calls a connected system.

{% hint style="info" %}
This page is thin in these docs because no trace had been recorded in the workspace we documented from. The controls above are confirmed; the shape of a populated row is not. If you are working from a workspace with real traffic, trust the screen over this page.
{% endhint %}

### Traces and timeouts

If a workflow is timing out, look here before raising its execution timeout. A longer timeout treats the symptom. Batching the calls, or moving to the Long tier, treats the cause. See [Executions](executions.md) for the run-level view.
