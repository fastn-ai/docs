---
description: Every workflow run that called a connected system, and how long each call took.
---

# Traces

**Activity → Traces**

A trace is recorded for every workflow run that calls a connected system. Where [Executions](executions.md) tells you a run failed, traces tell you which external call was responsible.

### Filters

**All**, **Success**, **Error**, **Pending**, each with a live count.

**Pending** deserves attention. A trace that never resolves usually means an upstream system accepted the request and never answered — the failure mode that produces timeouts rather than errors, and the one people find hardest to diagnose without this view.

### What a trace shows

Each entry covers one workflow run and the connector calls it made, with per-call duration. Reading them tells you three things quickly:

* **Which system is slow.** A workflow that takes 40 seconds is usually waiting on one call, not doing 40 seconds of work.
* **Which call fails.** Error traces name the connector and the action.
* **How many calls a run makes.** A run doing hundreds of calls is a candidate for batching, and is probably close to its tier's timeout.

{% hint style="info" %}
If traces show one connector consistently slow, raising the workflow's execution timeout treats the symptom. Batching the calls, or moving to the Long tier, treats the cause.
{% endhint %}
