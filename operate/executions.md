---
description: Every workflow run, newest first.
---

# Executions

**Activity → Executions**

<figure><img src="../.gitbook/assets/activity-executions.jpg" alt="The executions log"><figcaption></figcaption></figure>

The workspace-wide run history. Each workflow also has its own Executions tab in the editor.

### Filters

Status chips carry live counts:

| Status        | Meaning                                                           |
| ------------- | ------------------------------------------------------------------- |
| **Pending**   | Accepted, not yet queued.                                          |
| **Queued**    | Waiting for a runner.                                              |
| **Running**   | In progress.                                                       |
| **Completed** | Finished successfully.                                             |
| **Failed**    | Raised an error.                                                   |
| **Timeout**   | Exceeded its execution timeout.                                    |
| **Cancelled** | Stopped before finishing.                                          |

Alongside them: a time range (**All time**, Last 15m, 1h, 6h, 24h, 7d, 30d), a workflow selector, a search box, **Refresh**, and rows-per-page.

### What counts as an execution

> A workflow appears here the moment it runs, whether a trigger fired it, a schedule reached it, the API called it, or an agent did. Test runs started from a workflow's own Execute button are not recorded here.

That last sentence means the **Run Live** button on a workflow's Test tab. The exclusion is deliberate. This log is the record of real traffic; iterating in the Test tab does not pollute it.

### Reading the statuses

**Failed** is a workflow error — bad data, a rejected call, a bug. Open the execution for the error and the logs.

**Timeout** means the tier's budget ran out. Either the work genuinely needs longer, or a single external call is hanging. Check [Traces](traces.md) before raising the timeout.

**Queued** for an extended period suggests you are at a concurrency limit. Check [Billing](../manage/billing.md) for the concurrent-workflows cap.

**Cancelled** means something stopped it — a deploy replacing the version mid-run, or a manual cancel.

### Retries

When a workflow's retry policy is on, retries appear as separate executions. A cluster of failures followed by a success is the policy working, not four separate incidents.
