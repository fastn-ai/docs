---
description: What changed on the last run of each sync, record by record.
---

# Sync reports

**Activity → Sync reports**

Executions tell you a run succeeded. Sync reports tell you what it did, record by record.

### How a report is produced

> A report appears the first time a workflow runs `fastn.diff.compare`.

Which implies reports are effectively opt-in at the workflow level: a workflow that compares its source and target through `fastn.diff.compare` produces one, and a workflow that does not, does not.

### What it is for

The gap between "the run succeeded" and "the data is right" is where support tickets live. When a customer says records are missing, this is the page that distinguishes _the record was filtered out_ from _the record was never seen_ — which the executions log cannot tell you.

Each workflow also has a **Sync reports** tab in its editor, scoped to that workflow, with the same empty-state note.

### Controls

**Search reports**, and nothing else. Unlike Events, Traces and Executions, this page has no status filters and no date range.

Until a workflow has run `fastn.diff.compare`, the page reads **No sync reports yet**.

{% hint style="info" %}
This page is thin in these docs because no sync report had been produced in the workspace we documented from — the shape of a populated report is not something we can describe accurately. If you are building a data sync and this page stays empty, ask the agent to add diff reporting. It is far easier than reconstructing what a run did from logs afterwards.
{% endhint %}
