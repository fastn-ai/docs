---
description: >-
  Check what's syncing, view execution history, spot errors, and know when to
  contact support.
---

# Viewing Sync Status & History

Once your integrations are connected and running, the widget shows you how they're doing, what's running, what's succeeded or failed, and what needs attention. This information lives mainly on the **Insights** tab, with per-workflow run history available on the **Workflows** tab.

**Prerequisites:** At least one app connected via the widget. See [Connecting Apps via Widget](https://claude.ai/fastn/tutorials/end-user/connecting-apps-via-widget).

***

### The Insights tab

Open the **Insights** tab in the widget. This is where most of your sync and health information lives. A time-range selector in the top-right lets you switch between **7 days**, **30 days**, and **90 days** (7 days is selected by default).

#### Summary cards

Three cards across the top give you an at-a-glance view:

| Card                  | Shows                                                                              |
| --------------------- | ---------------------------------------------------------------------------------- |
| **Runs Today**        | Total runs today, broken into successful and failed (e.g., "1.2k ok · 251 failed") |
| **Records Processed** | How many records moved, split into synced, failed, and skipped                     |
| **Needs Attention**   | How many workflows need action                                                     |

#### Workflows table

Below the cards, a table lists your workflows with these columns:

| Column   | Shows                                                                  |
| -------- | ---------------------------------------------------------------------- |
| NAME     | The workflow name                                                      |
| LAST RUN | When it last ran, as a relative time (e.g., "40m ago", "2d ago")       |
| STATUS   | The latest status (e.g., "failed", or blank if the last run was clean) |
| RUNS     | Total number of runs                                                   |
| AVG      | Average run duration (e.g., "20.2s")                                   |

A footer summarizes activity, such as "5/13 active" and "8 not run in 30d".

#### Connectors

A **Connectors** section shows summary tiles ("Connected" and "Broken" counts) and a per-connector row with a status dot and a short status — for example, "Slack" with "no sync yet" if it hasn't run a sync yet.

#### Needs Attention

A **Needs Attention** list surfaces recent errors. Each entry shows:

* A category badge (CONNECTION, CONFIGURATION, USER\_DATA, or DATA)
* A short error summary
* The workflow it came from
* A relative timestamp

This is the fastest place to see what's gone wrong and which integration it affects.

***

### Per-workflow history (Workflows tab)

The **Workflows** tab lists your workflows as cards. Each card shows the workflow's title and a short description of what it does and when it runs. The card itself doesn't show run times or status — those are on the Insights tab and in the detail view.

Each card has a run button, a remove button, and a **chevron** that opens a detail view with four tabs:

| Tab            | Shows                                                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Diagram**    | A visual node-graph of the workflow's logic                                                                            |
| **Executions** | Run history — each row has a status badge (COMPLETED or FAILED), an execution ID, a duration, and a relative timestamp |
| **Errors**     | Errors with a count badge — each shows an error-type badge (e.g., CONNECTION), the message, and a timestamp            |
| **Test Cases** | The test scenarios for the workflow, with a count badge                                                                |

The **Executions** tab is where you see the full run-by-run history for a single workflow.

***

### Where to look for what

| You want to know...                              | Look at...                               |
| ------------------------------------------------ | ---------------------------------------- |
| Overall health today (runs, successes, failures) | Insights → summary cards                 |
| Which workflows ran and when                     | Insights → workflows table               |
| What's currently failing or needs action         | Insights → Needs Attention               |
| Whether a connector is connected or broken       | Insights → Connectors                    |
| The full run history of one workflow             | Workflows tab → open a card → Executions |
| Why a specific workflow failed                   | Workflows tab → open a card → Errors     |
| What a workflow does, visually                   | Workflows tab → open a card → Diagram    |

***

### Reading timestamps

Run times appear as relative timestamps ("40m ago", "14h ago", "2d ago") rather than absolute dates. "Last run" on the Insights table and the timestamps in the Executions list both use this format.

***

### A connected app's status

On the **Apps** tab, a connected integration shows its connection state — the name, a status dot, and a connection count (e.g., "1/2 connected") — but not sync activity or errors. For sync status, go to the **Insights** tab, where the Connectors section shows each connector's sync state.

***

### What you've learned

* How to read overall sync health from the Insights summary cards
* How to find which workflows ran, when, and how often
* How to see what needs attention and why, including error categories
* How to open a workflow's full run history, errors, and diagram from the Workflows tab
* Where connector sync state is shown (Insights, not the Apps tab)
