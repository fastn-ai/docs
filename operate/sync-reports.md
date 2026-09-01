---
description: What changed on the last run of each sync, record by record.
---

# Sync reports

**Activity → Sync reports**

Executions tell you a run succeeded. Sync reports tell you what it did — which records were created, updated, skipped or rejected.

### How a report is produced

> A report appears the first time a workflow runs `fastn.diff.compare`.

Reports are opt-in at the workflow level. A workflow that compares its source and target through `fastn.diff.compare` produces a report; one that does not, does not. Workflows built by the agent for data syncs generally include it.

### What it is for

The gap between "the run succeeded" and "the data is right" is where support tickets live. A sync report closes it:

* A customer says three orders are missing → the report shows they were skipped, and why.
* A field is empty downstream → the report shows whether it was ever mapped.
* A run took much longer than usual → the report shows the record count.

Each workflow also has a **Sync reports** tab in its editor, scoped to that workflow.

{% hint style="info" %}
If you are building a data sync and this page stays empty, ask the agent to add diff reporting. It is far easier than reconstructing what a run did from logs afterwards.
{% endhint %}
