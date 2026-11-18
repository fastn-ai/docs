---
description: "Capsule CRM (API v2) connector: manage parties (people & organisations), opportunities, cases/projects, tasks, notes/entries, pipelines, milestones, users,…"
hidden: true
---

# Capsule CRM

<img src="../../.gitbook/assets/connectors/lg/capsulecrm.png" alt="Capsule CRM logo">

Capsule CRM (API v2) connector: manage parties (people & organisations), opportunities, cases/projects, tasks, notes/entries, pipelines, milestones, users, teams, tags, custom field definitions, categories, tracks, boards, activity types, and REST hook webhooks. Base URL https://api.capsulecrm.com/api/v2.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [capsulecrm.com](https://capsulecrm.com) |
| **Authentication** | Bearer token |
| **Slug** | `capsulecrm` |

## Use it

Add Capsule CRM from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.capsulecrm.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Pipeline | `archivePipeline` | Archive (soft-delete) a pipeline by id. Returns 200/204. |
| Create Activity Type | `createActivityType` | Create a note/entry activity type. Body wrapped under 'activityType'. |
| Create Case | `createCase` | Create a case (project/kase). Requires party, status, and name. Body wrapped under 'kase'. |
| Create Category | `createCategory` | Create a task category. Body wrapped under 'category'. |
| Create Entry | `createEntry` | Create a note entry attached to a party, opportunity or case. Requires type='note', content, and exactly one of party/opportunity/kase. Body wrapped under 'entry'. |
| Create Field Definition | `createFieldDefinition` | Create a custom field definition for an entity type. Body wrapped under 'definition'. type is one of text, date, boolean, number, list, url, currency. |
| Create Milestone | `createMilestone` | Create an opportunity milestone within a pipeline. Body wrapped under 'milestone'. |
| Create Opportunity | `createOpportunity` | Create a sales opportunity. Requires a linked party and a milestone. Body wrapped under 'opportunity'. |
| Create Party | `createParty` | Create a person or organisation. For type=person supply firstName/lastName; for type=organisation supply name. Body is wrapped under 'party'. |
| Create Pipeline | `createPipeline` | Create a sales pipeline with its milestones. Body wrapped under 'pipeline'. |

<details>

<summary>See 72 more actions</summary>

* **Create REST Hook** `createRestHook`: Subscribe a REST hook (webhook). When the event fires, Capsule POSTs a payload to targetUrl. Body wrapped under 'restHook'. Max 20 hooks per account.
* **Create Tag** `createTag`: Create a tag definition for an entity type. Body wrapped under 'tag'.
* **Create Task** `createTask`: Create a task, optionally linked to a party, opportunity or case. Requires description. Body wrapped under 'task'.
* **Delete Activity Type** `deleteActivityType`: Delete an activity type by id. Returns 204.
* **Delete Case** `deleteCase`: Delete a case (kase) by id. Returns 204.
* **Delete Category** `deleteCategory`: Delete a task category by id. Returns 204.
* **Delete Entry** `deleteEntry`: Delete a note entry by id. Returns 204.
* **Delete Field Definition** `deleteFieldDefinition`: Delete a custom field definition by id for an entity type. Returns 204.
* **Delete Milestone** `deleteMilestone`: Delete a milestone by id. Returns 204.
* **Delete Opportunity** `deleteOpportunity`: Delete an opportunity by id. Returns 204.
* **Delete Party** `deleteParty`: Delete a party by id. Returns 204 No Content.
* **Delete REST Hook** `deleteRestHook`: Unsubscribe (delete) a REST hook by id. Returns 204.
* **Delete Tag** `deleteTag`: Delete a tag definition by id for an entity type. Returns 204/202.
* **Delete Task** `deleteTask`: Delete a task by id. Returns 204.
* **Duplicate Pipeline** `duplicatePipeline`: Duplicate an existing pipeline (including its milestones) by id.
* **Get Activity Type** `getActivityType`: Retrieve a single activity type by id.
* **Get Board** `getBoard`: Retrieve a single board by id.
* **Get Case** `getCase`: Retrieve a single case (kase) by id.
* **Get Category** `getCategory`: Retrieve a single task category by id.
* **Get Current User** `getCurrentUser`: Retrieve the user associated with the current API token. Useful for connection validation.
* **Get Entry** `getEntry`: Retrieve a single entry (note) by id.
* **Get Field Definition** `getFieldDefinition`: Retrieve a single custom field definition by id for an entity type.
* **Get Milestone** `getMilestone`: Retrieve a single milestone by id.
* **Get Opportunity** `getOpportunity`: Retrieve a single opportunity by id.
* **Get Party** `getParty`: Retrieve a single party (person or organisation) by id.
* **Get Pipeline** `getPipeline`: Retrieve a single sales pipeline by id. Use List Milestones to get its milestones.
* **Get REST Hook** `getRestHook`: Retrieve a single REST hook subscription by id.
* **Get Tag** `getTag`: Retrieve a single tag definition by id for an entity type.
* **Get Task** `getTask`: Retrieve a single task by id.
* **Get Team** `getTeam`: Retrieve a single team by id.
* **Get Track** `getTrack`: Retrieve a single track definition by id.
* **Get User** `getUser`: Retrieve a single user by id.
* **List Activity Type Icons** `listActivityTypeIcons`: List available icons for activity types.
* **List Activity Types** `listActivityTypes`: List all note/entry activity types on the account.
* **List Boards** `listBoards`: List all boards (case/project boards) on the account.
* **List Cases** `listCases`: List all cases (projects/kases) on the account.
* **List Cases By Party** `listCasesByParty`: List all cases associated with the given party.
* **List Categories** `listCategories`: List all task categories on the account.
* **List Deleted Cases** `listDeletedCases`: List cases deleted after a given time ('since', ISO8601). Capsule does not page this endpoint; all matching ids are returned.
* **List Deleted Opportunities** `listDeletedOpportunities`: List opportunities deleted after a given time ('since', ISO8601). Capsule does not page this endpoint; all matching ids are returned.
* **List Deleted Parties** `listDeletedParties`: List parties deleted after a given time ('since', ISO8601). Capsule does not page this endpoint; all matching ids are returned.
* **List Entries** `listEntries`: List all entries (notes, emails and history) across the account, most recent first. Supports paging and embedding related records.
* **List Entries For Entity** `listEntriesForParty`: List entries (notes/history) for a specific entity. entity is one of parties, opportunities, kases.
* **List Field Definitions** `listFieldDefinitions`: List custom field definitions for an entity type. entity is one of parties, opportunities, kases.
* **List Milestones** `listMilestones`: List all opportunity milestones on the account.
* **List Opportunities** `listOpportunities`: List all sales opportunities on the account.
* **List Opportunities By Party** `listOpportunitiesByParty`: List all opportunities associated with the given party.
* **List Parties** `listParties`: List all parties (people and organisations) on the Capsule account. Supports pagination and embed.
* **List Party Employees** `listPartyEmployees`: List people who are employees of the given organisation party.
* **List Pipelines** `listPipelines`: List all sales pipelines on the account. Set includeDeleted to also return archived pipelines.
* **List REST Hooks** `listRestHooks`: List all REST hook (webhook) subscriptions on the account.
* **List Tags** `listTags`: List tag definitions for an entity type. entity is one of parties, opportunities, kases.
* **List Tasks** `listTasks`: List tasks on the account. Filter by status (OPEN, COMPLETED, PENDING).
* **List Teams** `listTeams`: List all teams on the Capsule account.
* **List Tracks For Entity** `listTracks`: List tracks applied to a specific entity. entity is one of parties, opportunities, kases.
* **List Users** `listUsers`: List all users on the Capsule account.
* **Restore Pipeline** `restorePipeline`: Restore a previously archived pipeline by id.
* **Run Party Filter** `runPartyFilter`: Run a structured filter query against parties (POST /parties/filters/results). Use conditions such as {field:'type', operator:'is', value:'organisation'|'person'} to return only organisations or only people. Returns the same shape as List Parties: { parties: [...] }.
* **Search Cases** `searchCases`: Search cases (kases) by free-text query.
* **Search Opportunities** `searchOpportunities`: Search opportunities by free-text query.
* **Search Parties** `searchParties`: Search parties by free-text query (name, email, phone, etc.).
* **Update Activity Type** `updateActivityType`: Update an activity type by id. Body wrapped under 'activityType'.
* **Update Case** `updateCase`: Update a case (kase) by id. Only supplied fields change. Body wrapped under 'kase'.
* **Update Category** `updateCategory`: Update a task category by id. Body wrapped under 'category'.
* **Update Entry** `updateEntry`: Update a note entry by id. Body wrapped under 'entry'.
* **Update Field Definition** `updateFieldDefinition`: Update a custom field definition by id for an entity type. Body wrapped under 'definition'.
* **Update Milestone** `updateMilestone`: Update a milestone by id. Body wrapped under 'milestone'.
* **Update Opportunity** `updateOpportunity`: Update an opportunity by id. Only supplied fields change. Body wrapped under 'opportunity'.
* **Update Party** `updateParty`: Update a party by id. Only supplied fields change. Nested arrays support {id,_delete:true} to remove items. Body wrapped under 'party'.
* **Update Pipeline** `updatePipeline`: Update a pipeline by id. Body wrapped under 'pipeline'.
* **Update Tag** `updateTag`: Update a tag definition by id for an entity type. Body wrapped under 'tag'.
* **Update Task** `updateTask`: Update a task by id. Set status to COMPLETED to mark it done. Body wrapped under 'task'.

</details>
