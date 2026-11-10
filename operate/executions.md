---
description: Every workflow run, newest first.
---

# Executions

**Activity → Executions**

The workspace-wide run history. Each workflow also has its own Executions tab in the editor.

### The table

| Column           | Notes                                                          |
| ---------------- | ---------------------------------------------------------------- |
| **Workflow**     | Name, with a version chip.                                      |
| **Tier**         | Instant, Standard or Long.                                      |
| **Status**       | See below.                                                      |
| **Duration**     | How long the run took.                                          |
| **Triggered by** | What started it.                                                |
| **When**         | Timestamp, in your timezone.                                    |
| **Actions**      | **Replay** re-runs a finished execution. A pending, queued or running one shows **Stop** instead. |

**Rows per page** is 10, 20 or 50.

### Filters

| Filter          | Values                                                                            |
| --------------- | ----------------------------------------------------------------------------------- |
| Date range      | **All time** (default), Last 15m, 1h, 6h, 24h, 7d, 30d, or **Custom range**        |
| Status          | **All**, Pending, Queued, Running, Completed, Failed, Timed out, Cancelled         |
| Workflow        | One workflow, or all                                                               |

Alongside them: **Search executions**, **Refresh**, a **Runs** / **Logs** switch, and **Enable payload searching**, a toggle that extends the search into run payloads so you can find an id that came inside the event itself.

| Status        | Meaning                                                           |
| ------------- | ------------------------------------------------------------------- |
| **Pending**   | Accepted, not yet queued.                                          |
| **Queued**    | Waiting for a runner.                                              |
| **Running**   | In progress.                                                       |
| **Completed** | Finished successfully.                                             |
| **Failed**    | Raised an error.                                                   |
| **Timed out** | Exceeded its execution timeout.                                    |
| **Cancelled** | Stopped before finishing.                                          |

### Opening a run

This is where debugging actually happens. A row expands **inline** (you do not leave the page), into:

* A **result banner** with its **Raw response**, on a run that completed and returned output.
* Chips summarizing the run: **Steps**, **Success**, **Error**, **Slowest**.
* Tabs **Summary**, **Input**, **Output** and **Logs**, plus **Error** when the run errored.
* A footer carrying the two identifiers you need when asking anyone else about the run: `exec_…` and `wf_…`.

The Summary JSON carries the keys worth knowing by name:

| Key                                          | Tells you                                                  |
| -------------------------------------------- | ------------------------------------------------------------ |
| `totalSteps`, `succeeded`, `failed`          | How much of the run got through.                            |
| `slowestStep`, `slowestMs`                   | Where the time went: the first thing to read on a slow run. |
| `peakSandboxMB`, `sandboxMemoryLimitMB`      | How close the run came to its memory ceiling.               |

{% hint style="warning" %}
Read `peakSandboxMB` against `sandboxMemoryLimitMB` on any run that failed without an obvious error. Out-of-memory is one of the failures a retry policy never retries, so an OOM run will not quietly recover the way a transient failure does. It just stops.
{% endhint %}

### Reading the statuses

**Failed** is a workflow error: bad data, a rejected call, a bug. Expand the row and open the **Error** tab (**AI Diagnosis** and **Error Details**), then check [Traces](traces.md) (by URL, `/activity/traces`) for the external call behind it.

**Timed out** means the tier's budget ran out. Either the work genuinely needs longer, or a single external call is hanging. Check [Traces](traces.md) before raising the timeout.

**Queued** for an extended period means the run has been accepted but has not yet reached a runner.

**Cancelled** means the run stopped before finishing.

### The per-workflow tab

The **Executions** tab inside a workflow's editor filters differently: its pills are HTTP status codes (**All**, `200`, `201`, `400`, `404`, `422`, `500`), rather than run statuses. Use this page when you want to know *how a run ended*, and that tab when you want to know *what the caller got back*.
