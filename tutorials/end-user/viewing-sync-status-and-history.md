---
description: >-
  Check what's syncing, view run history, spot errors, and know when to
  contact support.
---

# Viewing Sync Status & History

Once your integrations are connected and running, the widget shows you how they're doing: what's running, what succeeded or failed, and what needs attention. The overview lives in **Insights**, which you open from the **⋯** menu in the widget header. Each integration's own run history is in its detail view.

**Prerequisites:** At least one app connected via the widget. See [Connecting Apps via Widget](connecting-apps-via-widget.md).

***

### Insights

In the widget header, open the **⋯** menu and choose **Insights**. A range selector lets you switch between **Today**, **7 days** (the default), **30 days**, and **Custom** (pick your own from and to dates).

If there is no **⋯** menu, your provider has hidden the widget header; if the menu is there without Insights, your provider's widget setup has it turned off. In either case, contact the product's support team.

#### Panels

Panels across the top give you an at-a-glance view:

| Panel                 | Shows                                                                                                                   |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Runs**              | How many runs happened in the range, with the change against the previous period. When something failed, a **N needs attention** button appears (for example "3 need attention"). |
| **Records processed** | How many records moved, split into synced, failed and skipped                                                           |
| **Connection health** | How many of your connections are healthy, and how many need action                                                      |
| **Busiest workflows** | The workflows that ran the most in the range                                                                            |

#### Workflows

Below the panels, a list of your workflows shows each one's recent activity. Its footer summarizes how many were active, such as "5/13 active in range", and how many have been idle a month or more, such as "8 idle 30d+".

#### Connections

The **Connections** section shows counts at the top ("N total", "N healthy", "N need action") and a row for each connection with its status: **Active**, **Reauth needed**, **Broken**, **Disconnected** or **Inactive**. **Reauth needed** means the app revoked or expired your sign-in: reconnect that account from the integration's detail view.

#### What needs attention

Click the **N needs attention** button on the Runs panel to see recent failures. Each failure is grouped by an error category:

| Category | Usually means |
| --- | --- |
| **user\_data** | The data in a record was rejected (for example a missing or invalid field). |
| **configuration** | Something in the setup is wrong or missing. |
| **dependency** | One of the connected apps failed or was unavailable. |
| **system** | An internal error on the platform side. |
| **oom** | The run ran out of memory. |
| **Unknown Outcome** | The run ended without a clear result. |

This is the fastest place to see what's gone wrong and which workflow it affects.

***

### One integration's history

Click **Manage** on an integration to open its detail view.

* **Activity** shows the last 7 days for that integration: records, runs and issues, plus its latest runs. Each run reads **ran**, **failed**, **timed out**, **cancelled**, **queued** or **running**. Click **View all runs** for the full list.
* **Workflows** lists the integration's workflows. Each row has a **Run workflow** button, may have an enable or disable toggle, and opens the workflow's details when you click the row. **Remove workflow** appears only on workflows your organization owns.

The workflow details have these tabs:

| Tab            | Shows                                                                                                                       |
| -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Diagram**    | A visual graph of the workflow's steps. Shown only if your provider turned on the workflow diagram; otherwise the details open on Executions. |
| **Executions** | Run history for this workflow, one row per run with its status, duration and time                                           |
| **Errors**     | Errors with a count badge. Each shows a short explanation or its category (user\_data, configuration, dependency, system, Unknown Outcome), the message, and the time |
| **Test Cases** | The test scenarios for the workflow, with a count badge                                                                     |

***

### Where to look for what

| You want to know...                              | Look at...                                                       |
| ------------------------------------------------ | ---------------------------------------------------------------- |
| Overall health (runs, successes, failures)       | **⋯** → Insights → Runs and Records processed                    |
| Which workflows ran and how often                | **⋯** → Insights → workflows list                                |
| What's currently failing or needs action         | **⋯** → Insights → **N needs attention**                         |
| Whether a connection is healthy or broken        | **⋯** → Insights → Connections                                   |
| The full run history of one workflow             | Open the integration → click the workflow → Executions           |
| Why a specific workflow failed                   | Open the integration → click the workflow → Errors               |
| What a workflow does, visually                   | Open the integration → click the workflow → Diagram (if enabled) |

***

### Reading timestamps

Run times appear as relative timestamps ("40m ago", "14h ago", "2d ago") rather than absolute dates.

***

### A connected app's status

In the integrations list, each integration's status line shows its connection state (for example "Connected" or "1 of 2 connected") but not sync activity or errors. For sync status, open **Insights** from the **⋯** menu, where the Connections section shows each connection's state, or open the integration to see its Activity.

***

### What you've learned

* How to read overall sync health from the Insights panels
* How to find which workflows ran and how often
* How to see what needs attention and why, including error categories
* How to open a workflow's run history, errors and diagram from the integration's detail view
* Where connection state is shown (Insights and the integration's status line)
