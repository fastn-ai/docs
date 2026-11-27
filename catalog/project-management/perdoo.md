---
description: "Perdoo is an OKR and goal management platform. Read objectives, KPIs, targets, progress updates, teams and users, and delete check-ins."
hidden: true
---

# Perdoo

<img src="../../.gitbook/assets/connectors/lg/perdoo.png" alt="Perdoo logo">

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [perdoo.com](https://perdoo.com) |
| **Authentication** | Access token |
| **Slug** | `perdoo` |

## Setup

Your customers enter their access token for Perdoo when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Perdoo from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Perdoo**.
2. Select **Connect** on the Perdoo card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Perdoo's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check Email Availability</td><td><code>emailAvailability</code></td><td>Check whether an email address is still available for a new Perdoo account.</td></tr><tr><td>Create Or Update Check-In</td><td><code>upsertCheckIn</code></td><td>Create a new check-in, or update an existing one by passing its ID.</td></tr><tr><td>Create Or Update Progress Update</td><td><code>upsertCommit</code></td><td>Create a new progress update (commit) on a Key Result, KPI or goal, or update an existing one by passing its ID.</td></tr><tr><td>Delete Check-In</td><td><code>deleteCheckIn</code></td><td>Delete a check-in by its ID.</td></tr><tr><td>Delete Progress Update</td><td><code>deleteCommit</code></td><td>Delete a progress update (commit) by its ID.</td></tr><tr><td>Get Cadence</td><td><code>cadence</code></td><td>Retrieve a single cadence, including its interval and timeframe configuration, by its ID.</td></tr><tr><td>Get Company</td><td><code>company</code></td><td>Retrieve a single company by its ID, including plan, framework and check-in settings.</td></tr><tr><td>Get Current Company</td><td><code>currentCompany</code></td><td>Retrieve the company that the authenticated token belongs to, including plan, framework and check-in settings.</td></tr><tr><td>Get Current User</td><td><code>me</code></td><td>Retrieve the user account that owns the API token used for this connection.</td></tr><tr><td>Get Goal</td><td><code>goal</code></td><td>Retrieve a single Perdoo goal (Objective, Key Result, Initiative, KPI or Strategic Pillar) by its ID.</td></tr></tbody></table>

<details>

<summary>View 20 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Key Result</td><td><code>result</code></td><td>Retrieve a single Key Result or Initiative by its ID.</td></tr><tr><td>Get KPI</td><td><code>kpi</code></td><td>Retrieve a single KPI by its ID.</td></tr><tr><td>Get KPI Target</td><td><code>kpiTarget</code></td><td>Retrieve a single KPI target by its ID.</td></tr><tr><td>Get Objective</td><td><code>objective</code></td><td>Retrieve a single Objective by its ID.</td></tr><tr><td>Get Progress Update</td><td><code>commit</code></td><td>Retrieve a single progress update (commit) by its ID.</td></tr><tr><td>Get Recommended Goal Status</td><td><code>recommendedGoalStatus</code></td><td>Return the status Perdoo recommends for a goal given a value on a specific date.</td></tr><tr><td>Get Team</td><td><code>group</code></td><td>Retrieve a single team (group) by its ID.</td></tr><tr><td>Get User</td><td><code>user</code></td><td>Retrieve a single user by their ID.</td></tr><tr><td>Get Welcome Link Status</td><td><code>welcomeLinkStatus</code></td><td>Check whether a Perdoo welcome or invitation link token is still valid.</td></tr><tr><td>List Goals</td><td><code>goals</code></td><td>List Perdoo goals across every goal type, with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>List Initiatives</td><td><code>initiatives</code></td><td>List Initiatives with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>List Key Results</td><td><code>keyResults</code></td><td>List Key Results with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>List KPI Targets</td><td><code>allKpiTargets</code></td><td>List KPI targets, optionally restricted to targets active within a date range.</td></tr><tr><td>List KPIs</td><td><code>allKpis</code></td><td>List KPIs with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>List Objectives</td><td><code>objectives</code></td><td>List Objectives with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>List Progress Updates</td><td><code>allCommits</code></td><td>List progress updates (commits) recorded against goals, filtered by user, date window or team.</td></tr><tr><td>List Results</td><td><code>results</code></td><td>List Key Results with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>List Teams</td><td><code>allGroups</code></td><td>List teams (groups) with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>List Users</td><td><code>allUsers</code></td><td>List users in the company with filtering, ordering and cursor or offset pagination.</td></tr><tr><td>Validate Password</td><td><code>passwordValidator</code></td><td>Score a candidate password against Perdoo password policy and return improvement recommendations.</td></tr></tbody></table>

</details>

