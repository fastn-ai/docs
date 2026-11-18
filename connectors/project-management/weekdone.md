---
description: "Weekdone is a team OKR, weekly progress reporting, and check-in platform."
hidden: true
---

# Weekdone

<img src="../../.gitbook/assets/connectors/weekdone.png" alt="Weekdone logo" width="64">

Weekdone is a team OKR, weekly progress reporting, and check-in platform. This connector wraps the Weekdone REST API v1 (https://api.weekdone.com/1) covering weekly report items and their comments, likes and ordering, weekly reports, teams, users, report item types, tags, Objectives and Key Results, KPIs, and company configuration.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [weekdone.com](https://weekdone.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `weekdone` |

## Use it

Add Weekdone from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.weekdone.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Key Result | `addObjectiveResult` | Add a key result to an objective. Docs: https://weekdone.com/developer |
| Add Objective Comment | `addObjectiveComment` | Add a comment to an objective. Docs: https://weekdone.com/developer |
| Add Report Item Comment | `addItemComment` | Adds a comment from the authenticated user to a report item. |
| Assign Report Item | `assignItem` | Reassigns an existing report item to another user within a team. The item moves to that user's weekly report and records the assigning user. Both the target user and their team must be supplied - the API rejects the call with "Missing required parameter: team_id" if the team is omitted, even though the published documentation lists only user_id as required. |
| Create KPI | `createKpi` | Create a KPI. Omit team_id and department_id for a company KPI. Docs: https://weekdone.com/developer |
| Create Objective | `createObjective` | Creates an Objective at company, department, team or personal level. A department Objective also requires department_id, a team Objective requires team_id, and a personal Objective requires both team_id and user_id. |
| Create Report Item | `createItem` | Adds a new item to a weekly report under the given category. Defaults to the current reporting week, the authenticated user, and that user's primary team when those fields are omitted. |
| Delete Key Result | `deleteObjectiveResult` | Delete a key result from an objective. Docs: https://weekdone.com/developer |
| Delete KPI | `deleteKpi` | Delete a KPI. Docs: https://weekdone.com/developer |
| Delete Objective | `deleteObjective` | Permanently deletes an Objective together with its Key Results and comments. |

<details>

<summary>See 27 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Objective Comment | `deleteObjectiveComment` | Delete a comment on an objective. Docs: https://weekdone.com/developer |
| Delete Report Item | `deleteItem` | Permanently deletes a report item and everything attached to it, including its comments and likes. |
| Delete Report Item Comment | `deleteItemComment` | Permanently deletes a single comment from a report item. |
| Get Company Details | `getCompany` | Retrieves the Weekdone company account configuration, including which Objective levels are enabled, whether all teams share one schedule and template, the report delivery and reminder schedule, and the company's departments, teams and users. |
| Get Tag | `getTag` | Get a single tag by id. Docs: https://weekdone.com/developer |
| Get Weekly Report | `getReport` | Retrieves the weekly report for a reporting week, grouped by team and then by user, with each user's report items, weekly rating and review feedback. Optionally narrowed to a single user or team. |
| Like Report Item | `addItemLike` | Records a like on a report item from the authenticated user. |
| List KPIs | `listKpis` | Get all KPIs (company, department or team level). Docs: https://weekdone.com/developer |
| List Objective Comments | `listObjectiveComments` | List comments on an objective. Docs: https://weekdone.com/developer |
| List Objectives | `listObjectives` | Lists Objectives and their Key Results, optionally narrowed to a level (company, department, team or user), a specific department, team or user, or a period. Objective progress is calculated from its Key Results and cannot be set directly. |
| List Report Item Comments | `listItemComments` | Lists the comments posted on a report item, in the order they were added. |
| List Report Item Likes | `listItemLikes` | Lists the users who have liked a report item. |
| List Report Item Types | `listTypes` | Lists the report item categories (types) configured for the company, such as Progress, Plans and Problems plus any custom categories, together with their carryover and overdue behaviour. Use the returned type IDs when creating or moving report items. |
| List Report Items | `listItems` | Searches weekly report items, optionally narrowed to a single user, a single team, or a specific reporting week. Report items are the Progress, Plans and Problems entries that make up a Weekdone weekly report. |
| List Tags | `listTags` | Get all tags; each may carry an optional status (status text, updated, user_id). Docs: https://weekdone.com/developer |
| List Teams | `listTeams` | Lists every team in the Weekdone company account with its report privacy setting, owning department, archive state, and any external email addresses that receive the team's reports. |
| List Users | `listUsers` | Lists every user in the Weekdone company account, including each user's primary team, company-admin flag, and the full set of teams they belong to with their per-team observer and admin roles. |
| Sort Report Items | `sortItems` | Reorders the report items within one category for a reporting week. The list parameter gives the item IDs in their desired order as a comma-separated string. |
| Unlike Report Item | `deleteItemLike` | Removes the authenticated user's like from a report item. |
| Update Key Result | `updateObjectiveResult` | Update a key result's description and/or its progress in the current period. Docs: https://weekdone.com/developer |
| Update KPI | `updateKpi` | Update a KPI's description. Docs: https://weekdone.com/developer |
| Update KPI Value | `updateKpiValue` | Record a new KPI value. Docs: https://weekdone.com/developer |
| Update Objective | `updateObjective` | Update an objective's description. Docs: https://weekdone.com/developer |
| Update Objective Comment | `updateObjectiveComment` | Update a comment on an objective. Docs: https://weekdone.com/developer |
| Update Report Item | `updateItem` | Updates an existing report item. Only the fields supplied are changed. When moving an item to a different category with type_id, the target reporting week must also be supplied in period. |
| Update Tag Priority | `updateTagPriority` | Mark a tag as priority or not. Docs: https://weekdone.com/developer |
| Update Tag Status | `updateTagStatus` | Set the status text of a tag. Docs: https://weekdone.com/developer |

</details>
