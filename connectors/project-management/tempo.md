---
description: "Tempo Cloud REST API v4 for Jira Time Tracking, Resourcing and Financial Management."
hidden: true
---

# Tempo

<img src="../../.gitbook/assets/connectors/lg/tempo.png" alt="Tempo logo">

Tempo Cloud REST API v4 for Jira Time Tracking, Resourcing and Financial Management. Covers worklogs, accounts, plans, teams, holiday schemes, workload schemes, roles, and other Tempo resource families via Bearer token auth (personal/user API token generated in the Tempo app's own Settings &gt; API Integration screen inside Jira Cloud).

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [tempo.io](https://tempo.io) |
| **Authentication** | Bearer token |
| **Slug** | `tempo` |

## Use it

Add Tempo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.tempo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Team Member | `addTeamMember` | Adds a member to a Tempo Team. |
| Create Account | `createAccount` | Creates a new Tempo Account for financial/budget tracking. |
| Create Holiday Scheme | `createHolidayScheme` | Creates a new Holiday Scheme. |
| Create Plan | `createPlan` | Creates a new Tempo Plan allocating planned hours for a user against an issue over a date range. |
| Create Team | `createTeam` | Creates a new Tempo Team. |
| Create Workload Scheme | `createWorkloadScheme` | Creates a new Workload Scheme. |
| Create Worklog | `createWorklog` | Creates a new worklog against a Jira issue, logging time spent by a user on a given date. |
| Delete Account | `deleteAccount` | Deletes a Tempo Account by its key. |
| Delete Holiday Scheme | `deleteHolidayScheme` | Deletes a Holiday Scheme by its numeric ID. |
| Delete Plan | `deletePlan` | Deletes a Tempo Plan by its numeric ID. |

<details>

<summary>See 31 more actions</summary>

* **Delete Team** `deleteTeam`: Deletes a Tempo Team by its numeric ID.
* **Delete Workload Scheme** `deleteWorkloadScheme`: Deletes a Workload Scheme by its numeric ID.
* **Delete Worklog** `deleteWorklog`: Deletes a worklog by its Tempo worklog ID.
* **Get Account** `getAccount`: Fetch a single Tempo Account by its key.
* **Get Holiday Scheme** `getHolidayScheme`: Fetch a single Holiday Scheme by its numeric ID.
* **Get Plan** `getPlan`: Fetch a single Tempo Plan by its numeric ID.
* **Get Team** `getTeam`: Fetch a single Tempo Team by its numeric ID.
* **Get User Schedule** `getUserSchedule`: Returns a user's required working schedule (combining their workload and holiday schemes) for a date range.
* **Get Workload Scheme** `getWorkloadScheme`: Fetch a single Workload Scheme by its numeric ID.
* **Get Worklog** `getWorklog`: Fetch a single worklog by its Tempo worklog ID.
* **List Account Categories** `listAccountCategories`: Returns the list of Account Categories used to classify Tempo Accounts.
* **List Account Category Types** `listAccountCategoryTypes`: Returns the list of Account Category Types (groupings for account categories).
* **List Accounts** `listAccounts`: Returns a paginated list of Tempo Accounts (used for financial/cost tracking and budgeting against Jira work).
* **List Holiday Schemes** `listHolidaySchemes`: Returns a paginated list of Holiday Schemes.
* **List Holidays in Scheme** `listHolidaysInScheme`: Returns the individual holiday dates configured within a Holiday Scheme.
* **List Plans** `listPlans`: Returns a paginated list of Tempo Plans (resource/capacity planning allocations against issues, projects, or users).
* **List Plans by User** `listPlansByUser`: Returns Tempo Plans allocated to a specific user within an optional date range.
* **List Team Members** `listTeamMembers`: Returns the members of a Tempo Team.
* **List Teams** `listTeams`: Returns a paginated list of Tempo Teams.
* **List Workload Schemes** `listWorkloadSchemes`: Returns a paginated list of Workload Schemes (define each user's expected working hours per weekday).
* **List Worklogs** `listWorklogs`: Returns a paginated list of worklogs across the whole Jira instance, optionally filtered by date range and last-updated timestamp.
* **List Worklogs by Issue** `listWorklogsByIssue`: Returns a paginated list of worklogs for a specific Jira issue, identified by issue key or numeric issue id.
* **List Worklogs by Project** `listWorklogsByProject`: Returns a paginated list of worklogs for a specific Jira project, identified by project key or numeric project id.
* **List Worklogs by User** `listWorklogsByUser`: Returns a paginated list of worklogs logged by a specific user, identified by Atlassian account ID.
* **Remove Team Member** `removeTeamMember`: Removes a member's team membership record from a Tempo Team.
* **Update Account** `updateAccount`: Updates an existing Tempo Account identified by its key.
* **Update Holiday Scheme** `updateHolidayScheme`: Updates the name or description of an existing Holiday Scheme.
* **Update Plan** `updatePlan`: Updates an existing Tempo Plan's dates or planned duration.
* **Update Team** `updateTeam`: Updates an existing Tempo Team's name or summary.
* **Update Workload Scheme** `updateWorkloadScheme`: Updates the name or description of an existing Workload Scheme.
* **Update Worklog** `updateWorklog`: Updates an existing worklog identified by its Tempo worklog ID.

</details>
