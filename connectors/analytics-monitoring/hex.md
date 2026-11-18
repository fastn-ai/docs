---
description: "Hex is a collaborative data workspace for notebooks, data apps and AI agents."
---

# Hex

Hex is a collaborative data workspace for notebooks, data apps and AI agents. This connector covers the Hex public API: projects and project runs, notebook cells and chart images, collections, groups and users, data connections, semantic models, guides, agent threads, suggestions and embedded app URLs.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [hex.tech](https://hex.tech) |
| **Authentication** | Credentials you enter |
| **Actions** | 57 |
| **Events** | 0 |
| **Slug** | `hex` |

## Use it

Add Hex from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.hex.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Run | `cancelRun` | Cancels a pending or running project run, stopping its compute. |
| Continue Thread | `continueThread` | Sends a follow-up prompt to an existing Hex agent thread, optionally attaching further data connections, tables, semantic datasets, semantic views or projects as context. |
| Create Cell | `createCell` | Adds a code, SQL or markdown cell to a project's notebook. Provide the contents variant matching the cell type, and optionally a location to place the cell after another cell or inside a section. |
| Create Collection | `createCollection` | Creates a collection in the workspace with an optional description and initial sharing for users, groups and the workspace. |
| Create Data Connection | `createDataConnection` | Creates a data connection to a warehouse, with its connection details, workspace and group sharing, schema refresh access and schedule, and optional schema filters. |
| Create Embed URL | `createEmbedUrl` | Creates a single-use signed URL for embedding a Hex app in your own product, with optional user attributes, default input values, extra export permissions, display options and an expiry. Use test mode to validate the call without running the app or consuming embedding usage. |
| Create Group | `createGroup` | Creates a user group in the workspace, optionally adding up to 100 users as initial members. |
| Create Project | `createProject` | Creates a new Hex project in the workspace with the given title and optional description. Rate limited by the hex-api group, by default 30 requests per minute. |
| Create Thread | `createThread` | Starts a Hex agent thread from a prompt, optionally attaching data connections, tables, semantic datasets, semantic views or projects as context, and running it against an existing project or a new one. |
| Deactivate User | `deactivateUser` | Deactivates a workspace user, revoking their access to Hex. This is an administrative action that cannot be undone through the API. |
| Delete Cell | `deleteCell` | Deletes a notebook cell from its project. This cannot be undone through the API. |
| Delete Group | `deleteGroup` | Deletes a user group from the workspace. Members keep their individual access; only the group and its group-level access are removed. |
| Delete Guide Draft | `deleteGuideDraft` | Deletes the draft version of a guide file by its guide file id. |
| Edit Collection | `editCollection` | Renames a collection, updates its description, or upserts sharing for users, groups and the workspace. Only the supplied fields are changed. |
| Edit Data Connection | `editDataConnection` | Updates a data connection's sharing, schema refresh access and schema refresh schedule. Only the supplied fields are changed. |
| Edit Group | `editGroup` | Renames a user group and adds or removes up to 100 member users per request. Only the supplied fields are changed. |
| Edit Project Sharing For Collections | `editProjectSharingForCollections` | Adds or updates the access a project grants through collections, up to 25 collections per request. |
| Edit Project Sharing For Groups | `editProjectSharingForGroups` | Adds or updates per-group access to a project, up to 25 groups per request. |
| Edit Project Sharing For Users | `editProjectSharingForUsers` | Adds or updates per-user access to a project, up to 25 users per request. |
| Edit Project Workspace And Public Sharing | `editProjectWorkspaceAndPublicSharing` | Sets the access that everyone in the workspace, and the public web, has to a project. Omit a field to leave that level of sharing unchanged. |
| Export Project | `exportProject` | Exports a project's full definition as YAML, for the current draft, a specific version number, or the latest published app version. |
| Get Cell | `getCell` | Retrieves a single notebook cell by id, including its type, label, attached data connection and contents. |
| Get Cell Output | `getCellOutput` | Returns the most recent output of a notebook cell, such as the value, dataframe preview or error produced when the cell last ran. |
| Get Chart Image From Cell | `getChartImageFromCell` | Renders the chart produced by a notebook cell as an image, at an optional width and height and with an optional chart title. |
| Get Chart Image From Run | `getChartImageFromRun` | Renders the chart produced by a specific cell during a specific project run as an image, at an optional width and height and with an optional chart title. |
| Get Collection | `getCollection` | Retrieves a single collection by id, including its name, description, creator and sharing configuration. |
| Get Current User | `getCurrentUser` | Returns the Hex user that owns the API token, including their role, workspace and token expiry. |
| Get Data Connection | `getDataConnection` | Retrieves a single data connection by id, including its warehouse type, connection details, sharing and schema refresh configuration. |
| Get Group | `getGroup` | Retrieves a single user group by id, including its members. |
| Get Project | `getProject` | Retrieves a single Hex project by id, including its owner, status, categories, analytics, schedules and optionally its sharing configuration. |
| Get Run Status | `getRunStatus` | Returns the status of a single project run, including its trigger, timings and links. Set Expanded Statistics to 'true' to also receive the kernel and run state transitions. The value is sent both as the enable-expanded-stats header the API reads and as a query parameter, which the API ignores. |
| Get Suggestion | `getSuggestion` | Retrieves a single agent context suggestion by id, including its status and the changes it proposes. |
| Get Thread | `getThread` | Retrieves a single Hex agent thread by id, including its prompt, source and linked project. |
| Get Thread Messages | `getThreadMessages` | Lists the messages exchanged in a Hex agent thread with cursor pagination, optionally returning the full message payloads. |
| Ingest Semantic Model | `ingestSemanticModel` | Syncs a semantic model's definitions into Hex, optionally returning per-component detail and debug information, or validating without writing using a dry run. |
| List Cells | `listCells` | Lists the notebook cells of a project in order, with cursor pagination. Returns each cell's id, static id, type, label and contents. |
| List Collections | `listCollections` | Lists the collections in the Hex workspace with cursor pagination, including each collection's sharing configuration. |
| List Data Connections | `listDataConnections` | Lists the workspace's data connections with cursor pagination, including connection type, connection details, sharing and schema refresh settings. |
| List Draft Guides | `listDraftGuides` | Lists the draft guide files in the workspace with cursor pagination, optionally filtered to guides synced from a given external source. |
| List Groups | `listGroups` | Lists the user groups in the Hex workspace with cursor pagination. |
| List Project Runs | `listProjectRuns` | Lists the runs of a project with offset pagination, optionally filtered by run status or by what triggered the run. |
| List Projects | `listProjects` | Lists the Hex projects visible to the token, newest first by default, with filters for archived, trashed and component projects, status, category, creator, owner and collection, plus cursor pagination. |
| List Queried Tables | `listQueriedTables` | Lists the warehouse tables a project queries, with cursor pagination. Requires a Hex Enterprise workspace. |
| List Suggestions | `listSuggestions` | Lists the agent context suggestions in the workspace with cursor pagination, optionally filtered by status. |
| List Threads | `listThreads` | Lists Hex agent threads with cursor pagination and filters for source, user, type, recency, feedback, warnings, topics and referenced resources. |
| List Topics | `listTopics` | Lists the agent context topics defined in the workspace, with cursor pagination. |
| List Users | `listUsers` | Lists the users in the Hex workspace with cursor pagination, optionally filtered to a group or to specific user ids. |
| Publish Guide Drafts | `publishGuideDrafts` | Publishes draft guides so they become the live context guides, either a named list of guide files or every draft guide in the workspace. |
| Run Project | `runProject` | Starts a run of a published Hex app, optionally passing input parameter values, updating the published results, controlling SQL result caching and sending completion notifications. Returns the run id and status URLs. Use dryRun to validate the request without consuming compute. |
| Trigger Suggestion Review | `triggerSuggestionReview` | Starts a review run for an agent context suggestion, asking Hex to re-evaluate the proposed changes. |
| Update Cell | `updateCell` | Updates the contents of a notebook cell, and optionally the data connection attached to a SQL cell. Only the supplied fields are changed. |
| Update Data Connection Schema | `updateDataConnectionSchema` | Applies status labels to databases, schemas or tables in a data connection's schema, or clears a status by passing null. |
| Update Project | `updateProject` | Updates a project's status. Pass a status name to apply it, or null to remove the project's current status. |
| Update Semantic Model | `updateSemanticModel` | Applies status labels to datasets and views in a semantic model, or clears a status by passing null. |
| Update Suggestion | `updateSuggestion` | Changes the status of an agent context suggestion, with an optional rejection reason when dismissing it. |
| Update Suggestion Change | `updateSuggestionChange` | Accepts or dismisses one proposed change within an agent context suggestion, for either a guide file update or a data warehouse update. |
| Upsert Guide Draft | `upsertGuideDraft` | Creates or updates draft guide files from their file path and contents, so agent context guides can be synced from an external source such as a git repository. |
