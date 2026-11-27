---
description: "Tempo is a time tracking and resource planning tool for Jira. Manage worklogs, accounts, plans, teams, holiday schemes and workload schemes."
hidden: true
---

# Tempo

<img src="../../.gitbook/assets/connectors/lg/tempo.png" alt="Tempo logo">

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [tempo.io](https://tempo.io) |
| **Authentication** | Access token |
| **Slug** | `tempo` |

## Setup

Your customers enter their access token for Tempo when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Tempo from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Tempo**.
2. Select **Connect** on the Tempo card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Tempo's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Team Member</td><td><code>addTeamMember</code></td><td>Adds a member to a Tempo Team.</td></tr><tr><td>Create Account</td><td><code>createAccount</code></td><td>Creates a new Tempo Account for financial/budget tracking.</td></tr><tr><td>Create Holiday Scheme</td><td><code>createHolidayScheme</code></td><td>Creates a new Holiday Scheme.</td></tr><tr><td>Create Plan</td><td><code>createPlan</code></td><td>Creates a new Tempo Plan allocating planned hours for a user against an issue over a date range.</td></tr><tr><td>Create Team</td><td><code>createTeam</code></td><td>Creates a new Tempo Team.</td></tr><tr><td>Create Workload Scheme</td><td><code>createWorkloadScheme</code></td><td>Creates a new Workload Scheme.</td></tr><tr><td>Create Worklog</td><td><code>createWorklog</code></td><td>Creates a new worklog against a Jira issue, logging time spent by a user on a given date.</td></tr><tr><td>Delete Account</td><td><code>deleteAccount</code></td><td>Deletes a Tempo Account by its key.</td></tr><tr><td>Delete Holiday Scheme</td><td><code>deleteHolidayScheme</code></td><td>Deletes a Holiday Scheme by its numeric ID.</td></tr><tr><td>Delete Plan</td><td><code>deletePlan</code></td><td>Deletes a Tempo Plan by its numeric ID.</td></tr></tbody></table>

<details>

<summary>View 31 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Team</td><td><code>deleteTeam</code></td><td>Deletes a Tempo Team by its numeric ID.</td></tr><tr><td>Delete Workload Scheme</td><td><code>deleteWorkloadScheme</code></td><td>Deletes a Workload Scheme by its numeric ID.</td></tr><tr><td>Delete Worklog</td><td><code>deleteWorklog</code></td><td>Deletes a worklog by its Tempo worklog ID.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Fetch a single Tempo Account by its key.</td></tr><tr><td>Get Holiday Scheme</td><td><code>getHolidayScheme</code></td><td>Fetch a single Holiday Scheme by its numeric ID.</td></tr><tr><td>Get Plan</td><td><code>getPlan</code></td><td>Fetch a single Tempo Plan by its numeric ID.</td></tr><tr><td>Get Team</td><td><code>getTeam</code></td><td>Fetch a single Tempo Team by its numeric ID.</td></tr><tr><td>Get User Schedule</td><td><code>getUserSchedule</code></td><td>Returns a user's required working schedule (combining their workload and holiday schemes) for a date range.</td></tr><tr><td>Get Workload Scheme</td><td><code>getWorkloadScheme</code></td><td>Fetch a single Workload Scheme by its numeric ID.</td></tr><tr><td>Get Worklog</td><td><code>getWorklog</code></td><td>Fetch a single worklog by its Tempo worklog ID.</td></tr><tr><td>List Account Categories</td><td><code>listAccountCategories</code></td><td>Returns the list of Account Categories used to classify Tempo Accounts.</td></tr><tr><td>List Account Category Types</td><td><code>listAccountCategoryTypes</code></td><td>Returns the list of Account Category Types (groupings for account categories).</td></tr><tr><td>List Accounts</td><td><code>listAccounts</code></td><td>Returns a paginated list of Tempo Accounts (used for financial/cost tracking and budgeting against Jira work).</td></tr><tr><td>List Holiday Schemes</td><td><code>listHolidaySchemes</code></td><td>Returns a paginated list of Holiday Schemes.</td></tr><tr><td>List Holidays in Scheme</td><td><code>listHolidaysInScheme</code></td><td>Returns the individual holiday dates configured within a Holiday Scheme.</td></tr><tr><td>List Plans</td><td><code>listPlans</code></td><td>Returns a paginated list of Tempo Plans (resource/capacity planning allocations against issues, projects, or users).</td></tr><tr><td>List Plans by User</td><td><code>listPlansByUser</code></td><td>Returns Tempo Plans allocated to a specific user within an optional date range.</td></tr><tr><td>List Team Members</td><td><code>listTeamMembers</code></td><td>Returns the members of a Tempo Team.</td></tr><tr><td>List Teams</td><td><code>listTeams</code></td><td>Returns a paginated list of Tempo Teams.</td></tr><tr><td>List Workload Schemes</td><td><code>listWorkloadSchemes</code></td><td>Returns a paginated list of Workload Schemes (define each user's expected working hours per weekday).</td></tr><tr><td>List Worklogs</td><td><code>listWorklogs</code></td><td>Returns a paginated list of worklogs across the whole Jira instance, optionally filtered by date range and last-updated timestamp.</td></tr><tr><td>List Worklogs by Issue</td><td><code>listWorklogsByIssue</code></td><td>Returns a paginated list of worklogs for a specific Jira issue, identified by issue key or numeric issue id.</td></tr><tr><td>List Worklogs by Project</td><td><code>listWorklogsByProject</code></td><td>Returns a paginated list of worklogs for a specific Jira project, identified by project key or numeric project id.</td></tr><tr><td>List Worklogs by User</td><td><code>listWorklogsByUser</code></td><td>Returns a paginated list of worklogs logged by a specific user, identified by Atlassian account ID.</td></tr><tr><td>Remove Team Member</td><td><code>removeTeamMember</code></td><td>Removes a member's team membership record from a Tempo Team.</td></tr><tr><td>Update Account</td><td><code>updateAccount</code></td><td>Updates an existing Tempo Account identified by its key.</td></tr><tr><td>Update Holiday Scheme</td><td><code>updateHolidayScheme</code></td><td>Updates the name or description of an existing Holiday Scheme.</td></tr><tr><td>Update Plan</td><td><code>updatePlan</code></td><td>Updates an existing Tempo Plan's dates or planned duration.</td></tr><tr><td>Update Team</td><td><code>updateTeam</code></td><td>Updates an existing Tempo Team's name or summary.</td></tr><tr><td>Update Workload Scheme</td><td><code>updateWorkloadScheme</code></td><td>Updates the name or description of an existing Workload Scheme.</td></tr><tr><td>Update Worklog</td><td><code>updateWorklog</code></td><td>Updates an existing worklog identified by its Tempo worklog ID.</td></tr></tbody></table>

</details>

