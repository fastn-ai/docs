---
description: "SeekTable is a self-service BI tool for pivot tables, charts and reports over CSV files, SQL databases, MongoDB, ElasticSearch and OLAP cubes."
hidden: true
---

# SeekTable

<img src="../../.gitbook/assets/connectors/seektable.png" alt="SeekTable logo" width="64">

SeekTable is a self-service BI tool for pivot tables, charts and reports over CSV files, SQL databases, MongoDB, ElasticSearch and OLAP cubes. This connector covers the SeekTable web API for cloud and self-hosted installations: reports (list, get, export, share by email), cubes (list, get, CSV upload), dashboards (list, export), account backup, and the self-hosted user accounts and team management API.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [seektable.com](https://seektable.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `seektable` |

## Use it

Add SeekTable from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.seektable.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Team Group Members | `addTeamGroupMembers` | Self-hosted SeekTable only: adds existing team members, by case-sensitive email, to a team group and returns the number added. Emails that are not team members are ignored. Requires an admin API key allowed for account management. |
| Add Team Members | `addTeamMembers` | Self-hosted SeekTable only: adds login emails to a team owned by a user with Team sharing, even if no accounts exist for them yet. Returns which emails were added, were duplicates or were skipped. Requires an admin API key allowed for account management. |
| Assign Groups to Team Members | `assignTeamMemberGroups` | Self-hosted SeekTable only: sets the exact group membership for one or more team members in a single all-or-nothing operation; each member ends up in only the listed groups. Returns the number processed, or HTTP 500 if any email or group ID does not exist. Requires an admin API key allowed for account management. |
| Backup Account Data | `backupAccountData` | Downloads a backup of the API key owner's account data - cubes and reports, plus optionally workspaces, dashboards and team sharing settings - as a single XML file or a ZIP of configuration files. Requires a Full access API key, which needs Advanced publishing or Team sharing. |
| Backup User Account Data (Admin) | `backupUserAccountData` | Self-hosted admin API: download a backup of another account's cubes, reports, dashboards and team settings (GET /api/account/{account_id}/backup). Needs an admin API key whose email is listed in SeekTable_ST__Api__AccountBackupAllowedForEmail. |
| Create Team Group | `createTeamGroup` | Self-hosted SeekTable only: creates a group in a user's team, optionally with fixed report parameter values applied to its members. Requires an admin API key allowed for account management. |
| Create User Account | `createUserAccount` | Self-hosted SeekTable only: creates a user account with a login email and optional name, Team sharing and Advanced publishing roles. Such accounts sign in only through the embedded app view or SSO. Requires an admin API key allowed for account management. |
| Delete Team Group | `deleteTeamGroup` | Self-hosted SeekTable only: deletes a group from a user's team by group ID. Requires an admin API key allowed for account management. |
| Delete User Account | `deleteUserAccount` | Self-hosted SeekTable only: deletes a user account by ID. Requires an admin API key allowed for account management. |
| Export Dashboard | `exportDashboard` | Exports a dashboard to Excel or PDF, optionally with report parameter values (Advanced publishing). The chosen export must be enabled on the dashboard, and the Dashboards capability must be available. Returns a file. |

<details>

<summary>See 17 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Export Report | `exportReport` | Generates a saved report exactly as the in-app export does, in HTML, PDF, CSV, Excel, Excel pivot table, JSON or PNG. Optional report parameters (Advanced publishing), inline HTML styles, chart-only rendering, value formatting and JSON row mode. PDF, Excel and PNG exports return a file. |
| Get Cube | `getCube` | Retrieves metadata for one cube (data source) by its ID, including name, source type, source file and permissions. |
| Get Report | `getReport` | Retrieves metadata for one saved report by its ID, including name, report type (pivot or table) and its JSON configuration. |
| Get User Account | `getUserAccount` | Self-hosted SeekTable only: retrieves one user account by its numeric ID. Requires an admin API key allowed for account management. |
| List Cubes | `listCubes` | Retrieves metadata for every cube (data source) in the SeekTable account, optionally limited to one source type such as CSV file cubes. |
| List Dashboards | `listDashboards` | Retrieves metadata for every dashboard accessible in the SeekTable account. Available only where the Dashboards capability is enabled. |
| List Reports | `listReports` | Retrieves metadata for every report saved in the SeekTable account. |
| List Team Group Members | `listTeamGroupMembers` | Self-hosted SeekTable only: lists the members of one group in a user's team. Requires an admin API key allowed for account management. |
| List Team Groups | `listTeamGroups` | Self-hosted SeekTable only: lists the groups in a user's team with their report override parameters. Requires an admin API key allowed for account management. |
| List Team Members | `listTeamMembers` | Self-hosted SeekTable only: lists the members of a user's team with their account IDs and assigned group IDs, optionally one member by email. Requires an admin API key allowed for account management. |
| List User Accounts | `listUserAccounts` | Self-hosted SeekTable only: lists user accounts, optionally only the account with a given login email, with offset and limit paging. Requires an admin API key whose email is allowed for account management. |
| Remove Team Group Members | `removeTeamGroupMembers` | Self-hosted SeekTable only: removes team members, by case-sensitive email, from a team group and returns the number removed. Requires an admin API key allowed for account management. |
| Remove Team Members | `removeTeamMembers` | Self-hosted SeekTable only: removes login emails (case-sensitive) from a user's team and returns the number removed. Requires an admin API key allowed for account management. |
| Restore User Account Data (Admin) | `restoreUserAccountData` | Self-hosted admin API: restore cubes/reports/dashboards/team settings into an account from an XML backup (POST /api/account/{account_id}/restore). Needs an admin key listed in SeekTable_ST__Api__AccountRestoreAllowedForEmail. Can overwrite data when mode=allowUpdate. |
| Share Report by Email | `shareReportByEmail` | Emails a saved report to a recipient with a subject and optional message, embedding the report HTML in the email body by default and optionally attaching PDF, CSV or Excel exports. This sends a real email. On self-hosted SeekTable, SMTP must be configured. |
| Update User Account | `updateUserAccount` | Self-hosted SeekTable only: updates a user account's email, name or roles by ID. Only the fields you pass are changed. Requires an admin API key allowed for account management. |
| Upload CSV File | `uploadCsvFile` | Uploads CSV data to SeekTable. With a Cube ID it refreshes that existing CSV cube with the new data; without one it creates a new CSV cube. Returns the created or refreshed cube's metadata. SeekTable's API has no cube delete, so new cubes must be removed in the SeekTable app. |

</details>
