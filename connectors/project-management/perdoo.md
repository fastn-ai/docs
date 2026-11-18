---
description: "Perdoo OKR platform GraphQL API."
hidden: true
---

# Perdoo

Perdoo OKR platform GraphQL API. Read objectives, key results, initiatives, KPIs, KPI targets, goals, progress updates, teams, users, cadences and company settings, and create, update or delete progress updates and check-ins.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [perdoo.com](https://perdoo.com) |
| **Authentication** | Bearer token |
| **Actions** | 30 |
| **Events** | 0 |
| **Slug** | `perdoo` |

## Use it

Add Perdoo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.perdoo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Email Availability | `emailAvailability` | Check whether an email address is still available for a new Perdoo account. |
| Create Or Update Check-In | `upsertCheckIn` | Create a new check-in, or update an existing one by passing its ID. |
| Create Or Update Progress Update | `upsertCommit` | Create a new progress update (commit) on a Key Result, KPI or goal, or update an existing one by passing its ID. |
| Delete Check-In | `deleteCheckIn` | Delete a check-in by its ID. |
| Delete Progress Update | `deleteCommit` | Delete a progress update (commit) by its ID. |
| Get Cadence | `cadence` | Retrieve a single cadence, including its interval and timeframe configuration, by its ID. |
| Get Company | `company` | Retrieve a single company by its ID, including plan, framework and check-in settings. |
| Get Current Company | `currentCompany` | Retrieve the company that the authenticated token belongs to, including plan, framework and check-in settings. |
| Get Current User | `me` | Retrieve the user account that owns the API token used for this connection. |
| Get Goal | `goal` | Retrieve a single Perdoo goal (Objective, Key Result, Initiative, KPI or Strategic Pillar) by its ID. |
| Get Key Result | `result` | Retrieve a single Key Result or Initiative by its ID. |
| Get KPI | `kpi` | Retrieve a single KPI by its ID. |
| Get KPI Target | `kpiTarget` | Retrieve a single KPI target by its ID. |
| Get Objective | `objective` | Retrieve a single Objective by its ID. |
| Get Progress Update | `commit` | Retrieve a single progress update (commit) by its ID. |
| Get Recommended Goal Status | `recommendedGoalStatus` | Return the status Perdoo recommends for a goal given a value on a specific date. |
| Get Team | `group` | Retrieve a single team (group) by its ID. |
| Get User | `user` | Retrieve a single user by their ID. |
| Get Welcome Link Status | `welcomeLinkStatus` | Check whether a Perdoo welcome or invitation link token is still valid. |
| List Goals | `goals` | List Perdoo goals across every goal type, with filtering, ordering and cursor or offset pagination. |
| List Initiatives | `initiatives` | List Initiatives with filtering, ordering and cursor or offset pagination. |
| List Key Results | `keyResults` | List Key Results with filtering, ordering and cursor or offset pagination. |
| List KPI Targets | `allKpiTargets` | List KPI targets, optionally restricted to targets active within a date range. |
| List KPIs | `allKpis` | List KPIs with filtering, ordering and cursor or offset pagination. |
| List Objectives | `objectives` | List Objectives with filtering, ordering and cursor or offset pagination. |
| List Progress Updates | `allCommits` | List progress updates (commits) recorded against goals, filtered by user, date window or team. |
| List Results | `results` | List Key Results with filtering, ordering and cursor or offset pagination. |
| List Teams | `allGroups` | List teams (groups) with filtering, ordering and cursor or offset pagination. |
| List Users | `allUsers` | List users in the company with filtering, ordering and cursor or offset pagination. |
| Validate Password | `passwordValidator` | Score a candidate password against Perdoo password policy and return improvement recommendations. |
