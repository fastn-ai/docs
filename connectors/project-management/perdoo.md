---
description: "Perdoo OKR platform GraphQL API."
hidden: true
---

# Perdoo

<img src="../../.gitbook/assets/connectors/lg/perdoo.png" alt="Perdoo logo">

Read objectives, key results, initiatives, KPIs, KPI targets, goals, progress updates, teams, users, cadences and company settings, and create, update or delete progress updates and check-ins.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [perdoo.com](https://perdoo.com) |
| **Authentication** | Bearer token |
| **Slug** | `perdoo` |

## Use it

Add Perdoo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.perdoo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check Email Availability</td><td><code>emailAvailability</code></td><td>Check whether an email address is still available for a new Perdoo account.</td></tr><tr><td>Create Or Update Check-In</td><td><code>upsertCheckIn</code></td><td>Create a new check-in, or update an existing one by passing its ID.</td></tr><tr><td>Create Or Update Progress Update</td><td><code>upsertCommit</code></td><td>Create a new progress update (commit) on a Key Result, KPI or goal, or update an existing one by passing its ID.</td></tr><tr><td>Delete Check-In</td><td><code>deleteCheckIn</code></td><td>Delete a check-in by its ID.</td></tr><tr><td>Delete Progress Update</td><td><code>deleteCommit</code></td><td>Delete a progress update (commit) by its ID.</td></tr><tr><td>Get Cadence</td><td><code>cadence</code></td><td>Retrieve a single cadence, including its interval and timeframe configuration, by its ID.</td></tr><tr><td>Get Company</td><td><code>company</code></td><td>Retrieve a single company by its ID, including plan, framework and check-in settings.</td></tr><tr><td>Get Current Company</td><td><code>currentCompany</code></td><td>Retrieve the company that the authenticated token belongs to, including plan, framework and check-in settings.</td></tr><tr><td>Get Current User</td><td><code>me</code></td><td>Retrieve the user account that owns the API token used for this connection.</td></tr><tr><td>Get Goal</td><td><code>goal</code></td><td>Retrieve a single Perdoo goal (Objective, Key Result, Initiative, KPI or Strategic Pillar) by its ID.</td></tr></tbody></table>

<details>

<summary>View 20 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Key Result</td><td><code>result</code></td><td>Retrieve a single Key Result or Initiative by its ID.</td></tr><tr><td>Get KPI</td><td><code>kpi</code></td><td>Retrieve a single KPI by its ID.</td></tr><tr><td>Get KPI Target</td><td><code>kpiTarget</code></td><td>Retrieve a single KPI target by its ID.</td></tr><tr><td>Get Objective</td><td><code>objective</code></td><td>Retrieve a single Objective by its ID.</td></tr><tr><td>Get Progress Update</td><td><code>commit</code></td><td>Retrieve a single progress update (commit) by its ID.</td></tr><tr><td>Get Recommended Goal Status</td><td><code>recommendedGoalStatus</code></td><td>Return the status Perdoo recommends for a goal given a value on a specific date.</td></tr><tr><td>Get Team</td><td><code>group</code></td><td>Retrieve a single team (group) by its ID.</td></tr><tr><td>Get User</td><td><code>user</code></td><td>Retrieve a single user by their ID.</td></tr><tr><td>Get Welcome Link Status</td><td><code>welcomeLinkStatus</code></td><td>Check whether a Perdoo welcome or invitation link token is still valid.</td></tr><tr><td>List Goals</td><td><code>goals</code></td><td>List Perdoo goals across every goal type, with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>List Initiatives</td><td><code>initiatives</code></td><td>List Initiatives with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>List Key Results</td><td><code>keyResults</code></td><td>List Key Results with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>List KPI Targets</td><td><code>allKpiTargets</code></td><td>List KPI targets, optionally restricted to targets active within a date range.</td></tr><tr><td>List KPIs</td><td><code>allKpis</code></td><td>List KPIs with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>List Objectives</td><td><code>objectives</code></td><td>List Objectives with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>List Progress Updates</td><td><code>allCommits</code></td><td>List progress updates (commits) recorded against goals, filtered by user, date window or team.</td></tr><tr><td>List Results</td><td><code>results</code></td><td>List Key Results with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>List Teams</td><td><code>allGroups</code></td><td>List teams (groups) with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>List Users</td><td><code>allUsers</code></td><td>List users in the company with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>Validate Password</td><td><code>passwordValidator</code></td><td>Score a candidate password against Perdoo password policy and return improvement recommendations.</td></tr></tbody></table>

</details>
