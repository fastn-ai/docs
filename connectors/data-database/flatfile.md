---
description: "Flatfile is a data onboarding and import platform."
hidden: true
---

# Flatfile

<img src="../../.gitbook/assets/connectors/lg/flatfile.png" alt="Flatfile logo">

Flatfile is a data onboarding and import platform. This connector covers the Flatfile REST API v1: account and environment management, spaces and their documents, guidance and drafts, workbooks, sheets, records and cell values, files and uploads, jobs and their execution plans, agents and agent logs, events and event acknowledgement, secrets, apps and app constraints, actions, guests and users with their roles, views, snapshots, commits, mapping programs and rules, data clips, data retention policies, canvas areas, routines, runbooks, flags, entitlements and assistant prompts.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [flatfile.com](https://flatfile.com) |
| **Authentication** | Bearer token |
| **Slug** | `flatfile` |

## Use it

Add Flatfile from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.flatfile.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Acknowledge Event | `acknowledgeEvent` | Acknowledges an event so it is no longer returned as outstanding by List Events. |
| Acknowledge Job | `acknowledgeJob` | Acknowledges a job that is ready to run, moving it into the executing state and optionally reporting progress. |
| Acknowledge Job Outcome | `acknowledgeJobOutcome` | Marks a finished job's outcome as seen, dismissing the outcome dialog shown to the user. |
| Add Records To Data Clip | `addRecordsToDataClip` | Adds further records from the source sheet into an existing data clip. |
| Archive Space | `archiveSpace` | Archives a space so it no longer appears in the active space list. Archived spaces can be restored with Unarchive Space. |
| Assign Agent Role | `assignAgentRole` | Assigns a role to an agent for a given resource, granting the agent that role's permissions. |
| Assign Guest Role | `assignGuestRole` | Assigns a role to a guest for a given resource, granting them that role's permissions. |
| Assign User Role | `assignUserRole` | Assigns a role to a dashboard user for a given resource, granting them that role's permissions. |
| Bulk Create Space Actions | `bulkCreateActions` | Creates several space actions in one request. The request body is a JSON array of action definitions, supplied as a pre-serialised JSON string. |
| Bulk Mutate Workbook Flags | `bulkMutateFlags` | Applies, updates, replaces or removes a flag across many records at once, selected by id list, search or filter. Runs as a job and returns its job id. |

<details>

<summary>See 212 more actions</summary>

* **Bulk Update Records** `bulkUpdateRecords`: Applies the same field values to every record matching the given filter, search or FFQL query, in the manner of a SQL UPDATE.
* **Cancel Job** `cancelJob`: Cancels a job that has not yet finished, optionally recording the reason.
* **Clone File** `cloneFile`: Creates a copy of an uploaded file in the same space, optionally with a custom name prefix. Flatfile requires the environment and space ids in the body even though its reference omits them.
* **Complete Commit** `completeCommit`: Marks a commit version complete, acknowledging that its changes have been applied to the sheet.
* **Complete Job** `completeJob`: Marks a job complete and sets the outcome message shown to the user when it finishes.
* **Create Agent** `createAgent`: Deploys an agent into an environment. An agent is server-side JavaScript that subscribes to Flatfile event topics and runs whenever a matching event fires.
* **Create And Invite User** `createAndInviteUser`: Creates a dashboard user with the given roles and emails them an invitation to join the account. Sends real email to the address named.
* **Create App** `createApp`: Creates an app in the account, defining the entity customers import, the namespace its spaces use, and the app type.
* **Create App Constraint** `createAppConstraint`: Creates a custom validation constraint on an app, which can then be attached to blueprint fields.
* **Create Assistant Prompt** `createAssistantPrompt`: Saves an AI assistant prompt against a space, for reuse in AI Assist or constraint generation.
* **Create Canvas Area** `createCanvasArea`: Creates a canvas area on a canvas, defining a pane of the space layout such as a sheet, document, form or iframe.
* **Create Data Clip** `createDataClip`: Creates a data clip from a sheet so named collaborators can review and resolve a subset of its records.
* **Create Data Retention Policy** `createDataRetentionPolicy`: Creates a data retention policy on an environment, setting how long spaces are kept before automatic deletion.
* **Create Environment** `createEnvironment`: Creates a new environment in the account. Environments isolate spaces, agents, secrets and data between production and development.
* **Create Event** `createEvent`: Publishes a custom event onto the Flatfile event bus so agents subscribed to its topic run.
* **Create Guests** `createGuest`: Creates one or more guests and grants them access to the named spaces. The request body is a JSON array of guest configurations, supplied as a pre-serialised JSON string.
* **Create Guide** `createGuide`: Creates a guide in an environment from a set of content blocks.
* **Create Job** `createJob`: Creates a job to run an operation against a file, workbook, sheet, space or app, such as extracting, mapping, exporting or deleting data.
* **Create Mapping Program** `createMappingProgram`: Creates a mapping program by generating mapping rules between a source schema and a destination schema.
* **Create Mapping Rules** `createMappingRules`: Adds mapping rules to a program. The request body is a JSON array of rule configurations, supplied as a pre-serialised JSON string.
* **Create Routine** `createRoutine`: Adds a routine step to a runbook, at the given position in its sequence.
* **Create Runbook** `createRunbook`: Creates a runbook in a space so a sequence of routines can be recorded and replayed.
* **Create Snapshot** `createSnapshot`: Takes a snapshot of a sheet's current records so they can be compared or restored later.
* **Create Space** `createSpace`: Creates a new space, optionally from an existing space configuration or app template, with its own settings, actions, labels and guest access.
* **Create Space Action** `createAction`: Creates a custom action in a space. The action appears as a button mounted on the chosen target and triggers a job when clicked.
* **Create Space Document** `createSpaceDocument`: Adds a markdown document to a space, optionally with treatments and mounted actions.
* **Create Space Draft** `createSpaceDraft`: Creates a draft copy of a space so its configuration can be changed and reviewed before being merged back.
* **Create Space Guidance** `createSpaceGuidance`: Attaches a guide to a space as guidance, specifying the target element, trigger and display type. The target must name a real canvas element in the space; Flatfile rejects unknown targets with "Guidance target X is not valid".
* **Create Version ID** `createVersionId`: Creates a new version id, optionally scoped to a sheet and parented to an existing version. Version ids group record changes into a single commit.
* **Create View** `createView`: Saves a named view on a sheet, storing a filter, sort and search combination.
* **Create Workbook** `createWorkbook`: Creates a workbook in a space, defining its sheets, their field blueprints and any mounted actions.
* **Create Workbook Flag** `createWorkbookFlag`: Creates a record flag on a workbook with a slug, label and colour.
* **Delete Agent** `deleteAgent`: Permanently deletes an agent so it stops reacting to events in its environment.
* **Delete Agent Export** `deleteAgentExport`: Permanently deletes an agent export bundle so it can no longer be downloaded.
* **Delete All Mapping History** `deleteAllMappingHistory`: Deletes every mapping program created by the authenticated actor in an environment. This cannot be undone.
* **Delete App** `deleteApp`: Deletes an app from the account. Spaces already created from the app are not removed.
* **Delete App Constraint** `deleteAppConstraint`: Permanently deletes a custom constraint from an app.
* **Delete Assistant Prompt** `deleteAssistantPrompt`: Deletes a saved AI assistant prompt.
* **Delete Canvas Area** `deleteCanvasArea`: Deletes a canvas area, removing that pane from the space layout.
* **Delete Data Clip** `deleteDataClip`: Deletes a data clip and revokes its shared link.
* **Delete Data Retention Policy** `deleteDataRetentionPolicy`: Deletes a data retention policy so its environment is no longer subject to automatic deletion.
* **Delete Environment** `deleteEnvironment`: Permanently deletes an environment and everything inside it, including its spaces, workbooks, agents and secrets.
* **Delete File** `deleteFile`: Permanently deletes an uploaded file from a space.
* **Delete Guest** `deleteGuest`: Deletes a guest entirely, or removes their access to one space when a Space ID is supplied.
* **Delete Guide** `deleteGuide`: Deletes a guide from an environment.
* **Delete Job** `deleteJob`: Deletes a job. Work already performed by the job is not undone.
* **Delete Mapping Program** `deleteMappingProgram`: Deletes a mapping program and the rules it contains.
* **Delete Mapping Rule** `deleteMappingRule`: Deletes a single mapping rule from a mapping program.
* **Delete Mapping Rules** `deleteMappingRules`: Deletes several mapping rules from a program in one request, by rule id.
* **Delete Records** `deleteRecords`: Deletes records from a sheet by id. A maximum of 100 record ids may be supplied per request.
* **Delete Routine** `deleteRoutine`: Deletes a routine step from its runbook. Flatfile documents this endpoint, but as of September 2026 the live API does not route DELETE /routines/{routineId} and returns its generic not-found response; deleting the runbook removes its routines.
* **Delete Runbook** `deleteRunbook`: Deletes a runbook and the routines it contains.
* **Delete Secret** `deleteSecret`: Deletes a secret from its environment or space by id.
* **Delete Sheet** `deleteSheet`: Permanently deletes a sheet and all of its records from a workbook.
* **Delete Snapshot** `deleteSnapshot`: Deletes a snapshot of a sheet. The sheet's current records are unaffected.
* **Delete Space** `deleteSpace`: Permanently deletes a space and all of its workbooks, files and records.
* **Delete Space Action** `deleteAction`: Deletes a custom action from a space so its button no longer appears.
* **Delete Space Document** `deleteSpaceDocument`: Deletes a document from a space.
* **Delete Space Guidance** `deleteSpaceGuidance`: Removes a guidance entry from a space so the guide no longer appears there.
* **Delete Spaces By ID** `bulkDeleteSpaces`: Permanently deletes a space and all of its workbooks, files and records, using the bulk delete endpoint. Flatfile expects one spaceIds value per space and rejects a comma-separated list, so pass a single space id per call.
* **Delete User** `deleteUser`: Removes a dashboard user from the Flatfile account, revoking their access.
* **Delete View** `deleteView`: Deletes a saved view from a sheet.
* **Delete Workbook** `deleteWorkbook`: Permanently deletes a workbook and all of the record data it contains.
* **Delete Workbook Flag** `deleteWorkbookFlag`: Deletes a record flag from a workbook.
* **Detect File Header** `detectFileHeader`: Detects which row of a tabular data sample is the header row, using the chosen detection algorithm.
* **Download Agent Export** `downloadAgentExport`: Downloads the contents of an agent export bundle as a binary file.
* **Download File** `downloadFile`: Downloads the raw contents of an uploaded file.
* **Download Sheet Records As CSV** `downloadSheetRecordsAsCsv`: Downloads a sheet's records as a CSV file, with the same filtering, searching and sorting options as List Records.
* **Duplicate Sheet** `duplicateSheet`: Copies a sheet, including all of its data, into the same workbook.
* **Execute Job** `executeJob`: Starts execution of a job that was created with a manual trigger.
* **Fail Job** `failJob`: Marks a job as failed and sets the failure message shown to the user.
* **Find And Replace Records** `findAndReplaceRecords`: Finds every value matching the Find text in a sheet, globally or within one field, and replaces it. Wrap Find in double quotes for an exact match. Returns the commit id for the updated records.
* **Get Agent** `getAgent`: Retrieves a single agent by its id, including its source, compiler, subscribed event topics, template and namespace.
* **Get Agent Export** `getAgentExport`: Retrieves a single agent export bundle by its id, including its export format and the agent it was generated from.
* **Get Agent Log** `getAgentLog`: Retrieves the agent execution log produced for a single event, including the captured console output and timings.
* **Get App** `getApp`: Retrieves a single app by its id, including its namespace, entity naming, blueprint and environment filters.
* **Get App Constraint** `getAppConstraint`: Retrieves a single app constraint by its id, including its validator, function source and options.
* **Get App Constraint Version** `getAppConstraintVersion`: Retrieves one specific saved version of an app constraint.
* **Get Assistant Prompt** `getAssistantPrompt`: Retrieves a single saved AI assistant prompt by its id.
* **Get Canvas Area** `getCanvasArea`: Retrieves a single canvas area by its id, including its type, position, layout and configuration.
* **Get Commit** `getCommit`: Retrieves a commit version, which represents one batch of changes applied to a sheet's records.
* **Get Current Account** `getCurrentAccount`: Retrieves the Flatfile account that the secret key belongs to, including its name, primary domain, dashboard version and embedded domain whitelist.
* **Get Data Clip** `getDataClip`: Retrieves a single data clip by its id, including its status and guest link.
* **Get Data Clip Resolution Index** `getDataClipResolutionIndex`: Returns the position of one record within a data clip's resolution list, for the given column and conflict filter.
* **Get Data Retention Policy** `getDataRetentionPolicy`: Retrieves a single data retention policy by its id.
* **Get Environment** `getEnvironment`: Retrieves a single environment by its id, including its production flag, guest authentication methods, namespaces and metadata.
* **Get Environment Event Subscription Token** `getEnvironmentEventToken`: Returns the PubNub subscribe key and token needed to stream every event in an environment in real time.
* **Get Event** `getEvent`: Retrieves a single platform event by its id, including its topic, context and payload.
* **Get File** `getFile`: Retrieves a single uploaded file by its id, including its extraction status and linked workbook.
* **Get Guest** `getGuest`: Retrieves a single guest by id, including the spaces, workbooks and sheets they can access.
* **Get Guest Token** `getGuestToken`: Returns an access token that authenticates a guest into a space, for embedding the space in your own application.
* **Get Guide** `getGuide`: Retrieves a single guide by its id, including its content blocks and version history.
* **Get Guide Version** `getGuideVersion`: Retrieves one specific saved version of a guide, including its rendered content.
* **Get Job** `getJob`: Retrieves a single job by its id, including its status, progress, configuration and outcome.
* **Get Job Execution Plan** `getJobExecutionPlan`: Returns a job's execution plan, including the field mappings between source and destination and any unmapped fields.
* **Get Mapping Program** `getMappingProgram`: Retrieves a single mapping program by its id, including its rules and field keys.
* **Get Mapping Rule** `getMappingRule`: Retrieves a single mapping rule from a program, including its configuration and confidence score.
* **Get Publishable Key** `getPublishableKey`: Retrieves the publishable (pk_) key for an environment, which is safe to use in browser-embedded Flatfile experiences.
* **Get Record Indices** `getRecordIndices`: Returns the row index of each named record within a sheet, for the current sort and filter.
* **Get Routine** `getRoutine`: Retrieves a single routine by its id. Flatfile documents this endpoint, but as of September 2026 the live API does not route GET /routines/{routineId} and returns its generic not-found response; List Routines returns the same data.
* **Get Runbook** `getRunbook`: Retrieves a single runbook by its id, including its status, type and configuration.
* **Get SFTP Credentials** `getSftpCredentials`: Retrieves the SFTP host, username and password that can be used to drop files directly into a Flatfile space.
* **Get Sheet** `getSheet`: Retrieves a single sheet by its id, including its blueprint configuration and record counts.
* **Get Sheet Cell Values** `getSheetCellValues`: Returns the distinct cell values in a sheet, grouped by field, optionally with a count of each value. Distinct must be set to true.
* **Get Sheet Record Counts** `getSheetRecordCounts`: Returns the number of total, valid and error records in a sheet, optionally broken down by field.
* **Get Snapshot** `getSnapshot`: Retrieves a single snapshot by its id, optionally including a summary of what changed since it was taken.
* **Get Space** `getSpace`: Retrieves a single space by its id, including its environment, app, settings, counts and guest link.
* **Get Space Action** `getAction`: Retrieves a single space action by its id, including its label, operation, mount point and constraints.
* **Get Space Document** `getSpaceDocument`: Retrieves a single document from a space, including its markdown body and mounted actions.
* **Get Space Event Subscription Token** `getEventSubscriptionToken`: Returns the PubNub subscribe key and token needed to stream events for a space in real time.
* **Get Space Guidance** `getSpaceGuidance`: Retrieves a single guidance entry from a space by its id.
* **Get User** `getUser`: Retrieves a single dashboard user by id, including their email, identity provider and last seen time.
* **Get View** `getView`: Retrieves a single saved view by its id, including its stored query configuration.
* **Get Workbook** `getWorkbook`: Retrieves a single workbook by its id, including its sheets, actions and settings.
* **Get Workbook Flag** `getWorkbookFlag`: Retrieves a single workbook flag by its slug.
* **Insert Records** `insertRecords`: Adds new records to a sheet. The request body is a JSON array of records, supplied as a pre-serialised JSON string.
* **Invite Guests** `inviteGuests`: Emails space invitations to existing guests. The request body is a JSON array of invites, supplied as a pre-serialised JSON string. Sends real email to the addresses named.
* **List Agent Exports** `listAgentExports`: Lists the agent export bundles generated for an environment, which package agent source for download.
* **List Agent Logs** `listAgentLogs`: Lists the execution logs for a single agent, including the triggering event, success flag, duration, memory use and captured console output.
* **List Agent Roles** `listAgentRoles`: Lists the roles assigned to an agent, showing which resources the agent is permitted to act on.
* **List Agent Versions** `listAgentVersions`: Lists every deployed version of an agent, so an earlier version can be inspected or reverted to.
* **List Agents** `listAgents`: Lists the agents deployed in a Flatfile environment. An agent is server-side code that subscribes to event topics and reacts to them.
* **List App Constraint Versions** `listAppConstraintVersions`: Lists every saved version of an app constraint, so an earlier definition can be inspected.
* **List App Constraints** `listAppConstraints`: Lists the validation constraints defined for an app, optionally including the built-in constraints Flatfile provides.
* **List Apps** `listApps`: Lists the apps configured in the Flatfile account. An app defines the entity being imported, its namespace and its blueprint.
* **List Assistant Prompts** `listAssistantPrompts`: Lists saved AI assistant prompts, optionally filtered by prompt type, with pagination.
* **List Canvas Areas** `listCanvasAreas`: Lists canvas areas, filtered by canvas, parent area, space or environment. Canvas areas define the panes that make up a Flatfile space layout.
* **List Data Clip Resolutions** `listDataClipResolutions`: Lists the resolutions in a data clip, showing how each record's proposed changes compare with the source sheet, optionally limited to conflicts.
* **List Data Clips** `listDataClips`: Lists data clips, filtered by space, sheet or status. A data clip is a shareable subset of a sheet's records that collaborators can resolve.
* **List Data Retention Policies** `listDataRetentionPolicies`: Lists the data retention policies on the account, optionally filtered to one environment. Policies control how long imported data is kept.
* **List Entitlements** `listEntitlements`: Lists the plan entitlements granted to a resource, such as the features and limits available to an account or environment.
* **List Environment Agent Executions** `listEnvironmentAgentExecutions`: Lists agent executions across an environment with their timings, request counts and memory usage, for monitoring agent performance.
* **List Environment Agent Logs** `listEnvironmentAgentLogs`: Lists agent execution logs across every agent in an environment, optionally filtered by space or by whether the execution succeeded.
* **List Environments** `listEnvironments`: Lists the environments in the account, with pagination. Environments separate production from development data and hold their own spaces, agents and secrets.
* **List Events** `listEvents`: Lists platform events, filtered by environment, space, domain, topic or timestamp. This is the polling interface to Flatfile's event stream.
* **List Files** `listFiles`: Lists the files uploaded to a space, with their extraction status, size and linked workbook.
* **List Guest Roles** `listGuestRoles`: Lists the roles assigned to a guest. Flatfile documents this endpoint, but as of September 2026 the live API answers GET /guests/{guestId}/roles with 405 Method Not Allowed; use Assign Guest Role's response to capture actor-role ids instead.
* **List Guests** `listGuests`: Lists the guests with access to a space, optionally filtered by email address. Guests are external collaborators who can upload and edit data in that space only.
* **List Guides** `listGuides`: Lists the guides defined in an environment. Guides are versioned block-based walkthroughs shown to users in a space.
* **List Jobs** `listJobs`: Lists jobs, filtered by environment, space, workbook, file, parent job or source, with sorting and pagination. Jobs are the units of asynchronous work Flatfile runs.
* **List Mapping Programs** `listMappingPrograms`: Lists mapping programs, which hold the rules that map an incoming schema onto a destination schema. Filter by environment, job, family, namespace, creator or creation date.
* **List Mapping Rules** `listMappingRules`: Lists the mapping rules in a mapping program, with their type, configuration and confidence score.
* **List Records** `listRecords`: Returns the records in a sheet, with filtering by validity, free-text search, FFQL query, field selection, sorting and pagination.
* **List Roles** `listRoles`: Lists the roles available in the account. Role ids are required when assigning roles to users, guests or agents.
* **List Routines** `listRoutines`: Lists the routines in a runbook. A routine is one ordered step of a recorded runbook.
* **List Runbooks** `listRunbooks`: Lists runbooks, filtered by app, environment or space. A runbook is a recorded sequence of routines that can be replayed.
* **List Secrets** `listSecrets`: Lists the secrets stored for an environment, optionally narrowed to a space or actor. Either an Environment ID or a Space ID must be supplied.
* **List Sheet Calculations** `getSheetCalculations`: Returns the calculated aggregate values, such as sums and averages, defined on a sheet's fields.
* **List Sheet Commits** `listSheetCommits`: Lists the commit versions recorded against a sheet, optionally filtered to completed or outstanding commits.
* **List Sheets** `listSheets`: Lists the sheets in a workbook, with their field configuration and record counts.
* **List Snapshot Records** `listSnapshotRecords`: Returns the records captured in a snapshot, optionally filtered to those created, updated or deleted since it was taken.
* **List Snapshots** `listSnapshots`: Lists the snapshots taken of a sheet. A snapshot preserves the sheet's records at a point in time so they can be restored.
* **List Space Actions** `listActions`: Lists the custom actions mounted in a space. Actions appear as buttons in the Flatfile UI and trigger jobs when clicked.
* **List Space Documents** `listSpaceDocuments`: Lists the markdown documents attached to a space. Documents render as pages in the space sidebar.
* **List Space Drafts** `listSpaceDrafts`: Lists the draft copies that exist for a space, with their merge status.
* **List Space Guidance** `listSpaceGuidance`: Lists the guidance attached to a space. Guidance binds a guide to a target element and a trigger in the space UI.
* **List Spaces** `listSpaces`: Lists spaces in the account, filtered by environment, app, namespace, archived state or search text, with pagination and sorting. A space is the workspace a customer imports data into.
* **List User Roles** `listUserRoles`: Lists the roles assigned to a dashboard user, showing which resources they are permitted to act on.
* **List Users** `listUsers`: Lists the dashboard users on the Flatfile account, with search, sorting and pagination.
* **List Views** `listViews`: Lists the saved views on a sheet. A view stores a filter, sort and search combination users can return to.
* **List Workbook Commits** `listWorkbookCommits`: Lists the commit versions recorded across all sheets in a workbook, optionally filtered to completed or outstanding commits.
* **List Workbook Flags** `listWorkbookFlags`: Lists the record flags defined on a workbook. Flags are coloured labels users apply to records.
* **List Workbooks** `listWorkbooks`: Lists the workbooks in an account or space, optionally filtered by name, namespace, label or treatment.
* **Lock Sheet** `lockSheet`: Locks a sheet so its records cannot be edited until it is unlocked.
* **Merge Space Draft** `mergeSpaceDraft`: Merges a draft space back into its source space, applying the configuration changes made in the draft.
* **Preview Job Mutation** `previewJobMutation`: Runs a JavaScript mutation function against a sample of a sheet's records and returns the mutated records, without saving anything.
* **Preview Space Draft Merge** `getSpaceDraftMerge`: Returns the changes a draft space would apply to its source space, grouped by resource type, without merging anything.
* **Refresh Data Clip Resolutions** `refreshDataClipResolutions`: Recomputes a data clip's resolutions against the current state of the source sheet.
* **Remove Agent Role** `deleteAgentRole`: Removes a previously assigned role from an agent, revoking the permissions it granted.
* **Remove Guest Role** `deleteGuestRole`: Removes a previously assigned role from a guest, revoking the permissions it granted.
* **Remove User Role** `deleteUserRole`: Removes a previously assigned role from a dashboard user, revoking the permissions it granted.
* **Replace Job Execution Plan** `replaceJobExecutionPlan`: Replaces a job's entire execution plan, setting the full field mapping and the unmapped source and destination fields.
* **Replay Commit** `replayCommit`: Re-emits the commit:created event for a commit version so agents listening for it run again.
* **Resend User Invite** `resendUserInvite`: Resends the account invitation email to a user who has not yet accepted it. Sends real email to that user.
* **Restore Snapshot** `restoreSnapshot`: Restores a sheet from a snapshot, choosing which classes of change to roll back: records created, updated or deleted since the snapshot.
* **Retry Job** `retryJob`: Retries a job that previously failed, restarting it from the beginning.
* **Revert Agent Version** `revertAgentVersion`: Reverts an agent back to one of its earlier deployed versions, making that version the live one. The Agent Version ID is the bare id returned by List Agent Versions.
* **Split Job** `splitJob`: Splits a job into the given number of parts, optionally running them in parallel.
* **Unarchive Space** `unarchiveSpace`: Restores a previously archived space so it appears again in the active space list.
* **Unlock Sheet** `unlockSheet`: Removes the lock from a sheet so its records can be edited again.
* **Update App** `updateApp`: Updates an app's name, namespace, entity naming, icon, metadata, blueprint, environment filters or activation date.
* **Update App Constraint** `updateAppConstraint`: Updates an app constraint's label, description, function source or options. Each update creates a new constraint version.
* **Update Assistant Prompt** `updateAssistantPrompt`: Updates the text of a saved AI assistant prompt.
* **Update Canvas Area** `updateCanvasArea`: Updates a canvas area's type, position, visibility, layout, overlay, configuration or parent.
* **Update Current Account** `updateCurrentAccount`: Updates the current Flatfile account's name or its default app.
* **Update Data Clip** `updateDataClip`: Updates a data clip's name, description, status, collaborators or shared link access.
* **Update Data Clip Resolutions** `updateDataClipResolution`: Records how each conflicting record in a data clip should be resolved.
* **Update Data Retention Policy** `updateDataRetentionPolicy`: Updates a data retention policy's type, period or environment.
* **Update Environment** `updateEnvironment`: Updates an environment's name, production flag, guest authentication methods, namespaces, metadata or localisation settings.
* **Update File** `updateFile`: Updates an uploaded file's name, status, storage mode, attached actions or the workbook it extracts into.
* **Update Guest** `updateGuest`: Updates a guest's name, email address, environment or the spaces they can access.
* **Update Guide** `updateGuide`: Updates a guide's title, slug, description, metadata or content blocks.
* **Update Job** `updateJob`: Updates a job's status, progress, configuration, status text, metadata or outcome acknowledgement time.
* **Update Job Execution Plan** `updateJobExecutionPlan`: Updates individual fields on a job's execution plan without replacing the whole plan.
* **Update Mapping Program** `updateMappingProgram`: Updates a mapping program's source or destination schema, family, namespace or rules.
* **Update Mapping Rule** `updateMappingRule`: Updates a single mapping rule's name, type, configuration, metadata or acceptance state.
* **Update Mapping Rules** `updateMappingRules`: Updates several mapping rules in a program at once. The request body is a JSON array of rules, supplied as a pre-serialised JSON string.
* **Update Records** `updateRecords`: Updates existing records in a sheet. The request body is a JSON array of records, each carrying its record id, supplied as a pre-serialised JSON string.
* **Update Routine** `updateRoutine`: Updates a routine's name, configuration, position or type. Flatfile documents this endpoint, but as of September 2026 the live API does not route PATCH /routines/{routineId} and returns its generic not-found response.
* **Update Runbook** `updateRunbook`: Updates a runbook's name, status or configuration.
* **Update Sheet** `updateSheet`: Updates a sheet's name, slug or metadata.
* **Update Space** `updateSpace`: Updates a space: its name, labels, metadata, settings, mounted actions, primary workbook, app assignment, guest authentication or archived state.
* **Update Space Action** `updateAction`: Updates a space action's label, operation, mode, mount point, messaging or constraints. Only the fields supplied are changed.
* **Update Space Document** `updateSpaceDocument`: Updates a space document's title and body, and optionally its treatments and mounted actions.
* **Update Space Guidance** `updateSpaceGuidance`: Updates the display options of a guidance entry: its target element, trigger, type or role.
* **Update User** `updateUser`: Updates a dashboard user's display name or the dashboard version they see.
* **Update View** `updateView`: Updates a saved view's name or stored query configuration.
* **Update Workbook** `updateWorkbook`: Updates a workbook's name, labels, namespace, sheets, actions, settings or metadata. Updating an existing sheet requires its config object; adding a new sheet does not.
* **Update Workbook Flag** `updateWorkbookFlag`: Updates a workbook flag's label, colour or slug.
* **Upload File** `uploadFile`: Uploads a text file (such as CSV, TSV or JSON) into a space so Flatfile extracts it into a workbook. The request is sent as multipart/form-data. Binary formats such as XLSX cannot be uploaded through this action because the connector engine does not preserve non-UTF-8 bytes.
* **Upsert Secret** `upsertSecret`: Creates or updates a secret by name, scoped to an environment or to a single space. Agents read these at run time.
* **Validate Sheet** `validateSheet`: Re-runs data hooks and validation across every record in a sheet.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Action Created | `action:created` |  |
| Action Deleted | `action:deleted` |  |
| Action Updated | `action:updated` |  |
| Agent Created | `agent:created` |  |
| Agent Deleted | `agent:deleted` |  |
| Agent Updated | `agent:updated` |  |
| Canvas Area Created | `canvas-area:created` |  |
| Canvas Area Deleted | `canvas-area:deleted` |  |
| Canvas Area Updated | `canvas-area:updated` |  |
| Canvas Created | `canvas:created` |  |

<details>

<summary>See 72 more events</summary>

* **Canvas Deleted** `canvas:deleted`
* **Canvas Updated** `canvas:updated`
* **Commit Completed** `commit:completed`
* **Commit Created** `commit:created`
* **Commit Updated** `commit:updated`
* **Cron 5 Minutes** `cron:5-minutes`
* **Cron Daily** `cron:daily`
* **Cron Hourly** `cron:hourly`
* **Cron Weekly** `cron:weekly`
* **Data Clip Collaborator Updated** `data-clip:collaborator-updated`
* **Data Clip Created** `data-clip:created`
* **Data Clip Deleted** `data-clip:deleted`
* **Data Clip Resolutions Created** `data-clip:resolutions-created`
* **Data Clip Resolutions Refreshed** `data-clip:resolutions-refreshed`
* **Data Clip Resolutions Updated** `data-clip:resolutions-updated`
* **Data Clip Updated** `data-clip:updated`
* **Document Created** `document:created`
* **Document Deleted** `document:deleted`
* **Document Updated** `document:updated`
* **Environment Autobuild Created** `environment:autobuild-created`
* **Environment Created** `environment:created`
* **Environment Deleted** `environment:deleted`
* **Environment Updated** `environment:updated`
* **File Created** `file:created`
* **File Deleted** `file:deleted`
* **File Expired** `file:expired`
* **File Updated** `file:updated`
* **Flag Created** `flag:created`
* **Flag Deleted** `flag:deleted`
* **Flag Updated** `flag:updated`
* **Job Completed** `job:completed`
* **Job Created** `job:created`
* **Job Deleted** `job:deleted`
* **Job Failed** `job:failed`
* **Job Outcome Acknowledged** `job:outcome-acknowledged`
* **Job Parts Completed** `job:parts-completed`
* **Job Ready** `job:ready`
* **Job Scheduled** `job:scheduled`
* **Job Updated** `job:updated`
* **Layer Created** `layer:created`
* **Program Created** `program:created`
* **Program Recomputed** `program:recomputed`
* **Program Recomputing** `program:recomputing`
* **Program Updated** `program:updated`
* **Records Created** `records:created`
* **Records Deleted** `records:deleted`
* **Records Updated** `records:updated`
* **Secret Created** `secret:created`
* **Secret Deleted** `secret:deleted`
* **Secret Updated** `secret:updated`
* **Sheet Calculation Updated** `sheet:calculation-updated`
* **Sheet Counts Updated** `sheet:counts-updated`
* **Sheet Created** `sheet:created`
* **Sheet Deleted** `sheet:deleted`
* **Sheet Updated** `sheet:updated`
* **Snapshot Created** `snapshot:created`
* **Space Archived** `space:archived`
* **Space Created** `space:created`
* **Space Deleted** `space:deleted`
* **Space Expired** `space:expired`
* **Space Guest Added** `space:guestAdded`
* **Space Guest Removed** `space:guestRemoved`
* **Space Unarchived** `space:unarchived`
* **Space Updated** `space:updated`
* **Thread Created** `thread:created`
* **Thread Deleted** `thread:deleted`
* **Thread Updated** `thread:updated`
* **Workbook Created** `workbook:created`
* **Workbook Deleted** `workbook:deleted`
* **Workbook Expired** `workbook:expired`
* **Workbook Thawed** `workbook:thawed`
* **Workbook Updated** `workbook:updated`

</details>
