---
description: "Streak is a CRM that lives inside Gmail."
hidden: true
---

# Streak

Streak is a CRM that lives inside Gmail. This connector wraps the public Streak REST API (https://api.streak.com/api/v1 and /v2) and covers the full object model: pipelines, boxes, stages, pipeline fields and box field values, contacts, organizations and their team-level field definitions, email threads, tasks, comments, meeting notes and call logs, files, snippets, users, teams, search, newsfeeds, the box timeline, and webhook registration. Authentication is HTTP Basic with the Streak API key sent as the username and an empty password.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [streak.com](https://streak.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 80 |
| **Events** | 20 |
| **Slug** | `streak` |

## Use it

Add Streak from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.streak.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Drive Files To Box | `addDriveFilesToBox` | Attach one or more Google Drive files to a single box. Streak expects a raw JSON array at the request root, with driveBoxKey repeated for every file, so files is passed as a JSON array string. Returns a bare array of the attached file records, wrapped here as items. |
| Add Email To Box | `addEmailToBox` | File a Gmail thread under a box. This endpoint is form-urlencoded, not JSON, and Streak wants the box key both in the path and in the body; this action sends both from the single boxKey input. Verified live 2026-09-16: Streak does NOT validate that threadGmailId exists in Gmail - it creates a GmailThread record for whatever id you send, with numberOfEmails 0 and doesRequestingUserHaveThread false until it resolves real messages. |
| Create Box | `createBox` | Create a box (record) in a pipeline. The box lands in the pipeline's first stage unless stageKey is supplied. Custom field values are set afterwards with Update Box Field Value or Update Box. |
| Create Comment | `createComment` | Post a comment on a box. Comments appear in the box newsfeed and fire the COMMENT_CREATE webhook event. |
| Create Contact | `createContact` | Create a contact in a team. At least one email address is required. Set getIfExisting to true to return the existing contact instead of failing when one already has that email address; with getIfExisting only emailAddresses may be sent. |
| Create Meeting | `createMeeting` | Record a meeting note or call log against a box. This endpoint is form-urlencoded, not JSON. startTimestamp and duration are both in milliseconds. |
| Create Organization | `createOrganization` | Create an organization in a team. At least one of name or domains must be supplied, and domains must be unique across the team. Set getIfExisting to true to return the existing organization matching the domain instead of creating a duplicate; with getIfExisting only domains may be sent. |
| Create Pipeline | `createPipeline` | Create a pipeline in a team. This endpoint is form-urlencoded, not JSON. fieldNames/fieldTypes/stageNames are passed as JSON-array strings of equal length, e.g. fieldNames ["Owner","Close Date"] with fieldTypes ["TEXT_INPUT","DATE"]. Fields and stages can also be changed afterwards with the Field and Stage actions. |
| Create Pipeline Field | `createPipelineField` | Add a custom field to a pipeline. This endpoint is form-urlencoded, not JSON. Streak allocates the field key (1001, 1002, ...) and returns it; that key is what box.fields is keyed by. |
| Create Snippet | `createSnippet` | Create an email snippet (canned response). This endpoint is form-urlencoded, not JSON. Supplying pipelineKey scopes the snippet to that pipeline instead of the user. |
| Create Stage | `createStage` | Add a stage to a pipeline. This endpoint is form-urlencoded, not JSON. Streak allocates the new stage key and appends it; use Update Pipeline with stageOrder to reposition it. |
| Create Task | `createTask` | Create a task on a box. New tasks always start with status NOT_DONE. Streak requires the box key both in the path and as key in the body; this action sends both from the single boxKey input. |
| Create Webhook | `createWebhook` | Register a webhook that POSTs to targetUrl when an event fires. Exactly one of pipelineKey or teamKey must be supplied and it decides the scope: pipelineKey for BOX_*, STAGE_CREATE, COMMENT_CREATE, MEETING_* and TASK_* events, teamKey for CONTACT_* and ORG_* events. The optional token is echoed on every delivery as the X-Streak-Webhook-Token header. Streak deletes the webhook itself if a delivery is answered with 410 Gone, and retries with backoff on anything other than 200 or 410. |
| Delete Box | `deleteBox` | Delete a box (record) and everything attached to it. Irreversible. |
| Delete Comment | `deleteComment` | Delete a comment from its box. Irreversible. |
| Delete Contact | `deleteContact` | Delete a contact from its team. Irreversible. |
| Delete Meeting | `deleteMeeting` | Delete a meeting note or call log from its box. Irreversible. |
| Delete Organization | `deleteOrganization` | Delete an organization from its team. Irreversible. |
| Delete Pipeline | `deletePipeline` | Delete a pipeline and every box inside it. Irreversible. |
| Delete Pipeline Field | `deletePipelineField` | Delete a custom field from a pipeline. Every box's value for that field is lost. Irreversible. |
| Delete Snippet | `deleteSnippet` | Delete an email snippet. Irreversible. |
| Delete Stage | `deleteStage` | Delete a stage from a pipeline. Boxes sitting in that stage are affected, so check the stage is empty first with List Boxes In Pipeline filtered by stageKey. |
| Delete Task | `deleteTask` | Delete a task from its box. Irreversible. |
| Delete Webhook | `deleteWebhook` | Unregister a webhook so Streak stops delivering that event. |
| Find Boxes By Name | `findBoxesByName` | Find boxes by exact name. Unlike Search this matches the box name only, which makes it the right lookup when syncing an external record into a box. |
| Get Box | `getBox` | Get one box (record) by key, including its stage, notes, followers and custom field values keyed by field key. |
| Get Box Field Value | `getBoxFieldValue` | Get the value of one custom field on one box. |
| Get Box Newsfeed | `getBoxNewsfeed` | Get the activity newsfeed for one box: stage changes, field edits, comments and emails. Returns a bare JSON array, wrapped here as items. |
| Get Box Timeline | `getBoxTimeline` | Get the merged timeline of a box: emails, comments, files, call logs, meeting notes and newsfeed entries in one chronological list. Paged with limit and the opaque nextPageToken returned as nextPage; when nextPageToken is supplied no other parameter may be sent. |
| Get Comment | `getComment` | Get one comment by comment key. |
| Get Contact | `getContact` | Get one contact by contact key. |
| Get Current User | `getCurrentUser` | Get the Streak user that owns the API key. Takes no input, so it is the cheapest way to verify a connection works. Returns the user profile including userKey, email and settings. |
| Get File | `getFile` | Get the metadata of one file attached to a box: name, mime type, size and its Drive or Gmail identifiers. |
| Get File Contents | `getFileContents` | Download the contents of a file attached to a box. Streak documents no response body for this endpoint. Binary and redirect-to-CDN responses are a known limitation of fastn's HTTP executor, so if this returns a 502 use Get File and fetch the file out of band from driveUrl instead. |
| Get Multiple Boxes | `getMultipleBoxes` | Batch-fetch several boxes from one pipeline in a single call. Streak expects a raw JSON array at the request root, so boxKeys is passed as a JSON array string, e.g. ["boxKey1","boxKey2"]. Returns a bare array of full box objects, wrapped here as items. |
| Get Newsfeed | `getNewsfeed` | Get the activity newsfeed across every pipeline the API key's user can see. Returns a bare JSON array, wrapped here as items. |
| Get Organization | `getOrganization` | Get one organization by organization key. |
| Get Pipeline | `getPipeline` | Get one pipeline by key, including its custom field definitions, its stage map and the stage order. |
| Get Pipeline Field | `getPipelineField` | Get one custom field definition of a pipeline by field key. |
| Get Pipeline Newsfeed | `getPipelineNewsfeed` | Get the activity newsfeed for one pipeline, covering the pipeline itself and every box inside it. Limited to the 50 most recent events. Returns a bare JSON array, wrapped here as items. |
| Get Snippet | `getSnippet` | Get one email snippet by key. Streak returns it inside a bare single-element array, wrapped here as items. |
| Get Stage | `getStage` | Get one stage of a pipeline by its stage key. |
| Get Task | `getTask` | Get one task by task key. |
| Get Team | `getTeam` | Get one Streak team by team key, including its member list with roles and invite status. |
| Get Thread | `getThread` | Get one email thread by its Streak thread key, including subject, participants and attached files. |
| Get User | `getUser` | Get a specific Streak user by user key. Users cannot be created or modified through the API. |
| Get Webhook | `getWebhook` | Get one registered webhook by key. |
| List Box Comments | `listBoxComments` | List the comments on a box. |
| List Box Field Values | `listBoxFieldValues` | List every custom field value set on a box. Each entry is {key, value} where key is the pipeline field key. Returns a bare JSON array, wrapped here as items. |
| List Box Files | `listBoxFiles` | List the files attached to a box, whether they came from a Gmail attachment or Google Drive. Returns a bare JSON array, wrapped here as items. |
| List Box Meetings | `listBoxMeetings` | List the meeting notes and call logs recorded against a box. |
| List Box Tasks | `listBoxTasks` | List the tasks on a box, with their status and assignees. |
| List Box Threads | `listBoxThreads` | List the Gmail email threads filed under a box, with the participants and the Gmail thread id. Returns a bare JSON array, wrapped here as items. |
| List Boxes In Pipeline | `listBoxesInPipeline` | List the boxes (records) in a pipeline. Supports paging with page (0-indexed) and limit, and an optional stageKey filter. Verified live 2026-09-16: Streak returns a bare JSON array (wrapped here as items) with NO hasNextPage field, contrary to the published docs - detect the end of the list by getting back fewer than limit items. |
| List Contact Fields | `listContactFields` | List the custom field definitions that apply to contacts in a team. The returned field keys are what Update Contact Field Value writes against. Streak returns a bare JSON object keyed by field key, empty when the team has no custom contact fields. Custom contact fields can only be created in the Streak UI, not through the API. |
| List My Teams | `listMyTeams` | List every Streak team the API key's user belongs to. Contacts, organizations and team-wide webhooks are all scoped to a teamKey, so this is the entry point for those resources. |
| List Organization Fields | `listOrganizationFields` | List the custom field definitions that apply to organizations in a team. The returned field keys are what Update Organization Field Value writes against. Streak returns a bare JSON object keyed by field key, empty when the team has no custom organization fields. Custom organization fields can only be created in the Streak UI, not through the API. |
| List Pipeline Fields | `listPipelineFields` | List the custom field definitions of a pipeline. The returned field keys (1001, 1002, ...) are what box.fields is keyed by. Returns a bare JSON array, wrapped here as items. |
| List Pipeline Webhooks | `listPipelineWebhooks` | List every webhook registered against a pipeline. |
| List Pipelines | `listPipelines` | List every pipeline the API key's user can see, including each pipeline's field definitions, stages and stage order. Returns a bare JSON array, wrapped here as items. |
| List Snippets | `listSnippets` | List the email snippets (canned responses) available to the API key's user. Returns a bare JSON array, wrapped here as items. |
| List Stages | `listStages` | List the stages of a pipeline. Streak returns a map keyed by stage key (5001, 5002, ...), each value being an object with name and key, not an array. Use Get Pipeline stageOrder for the display order. |
| List Team Webhooks | `listTeamWebhooks` | List every webhook registered against a team, which is where the CONTACT_* and ORG_* subscriptions live. |
| Move Boxes To Pipeline | `moveBoxesToPipeline` | Move boxes from one pipeline to another. The path takes the SOURCE pipeline key; each entry in the raw JSON array body names the destination. Verified live 2026-09-16: Streak does NOT preserve the box key across a move - each moved box comes back with a new key and a stage key from the destination pipeline, so any stored reference to the old boxKey is dead. Read the new key out of the response. |
| Remove Thread From Box | `removeThreadFromBox` | Unfile an email thread from its box. The Gmail message itself is untouched; only the Streak association is removed. |
| Search | `search` | Full-text search across boxes, contacts and organizations. pipelineKey and stageKey narrow the box results only. |
| Update Box | `updateBox` | Update a box: rename it, change its notes, move it to another stage, change followers, linked boxes, assignees, or its linked contacts and organizations. Only supplied properties are changed. Moving a box between stages is done by sending a new stageKey. |
| Update Box Field Value | `updateBoxFieldValue` | Set the value of one custom field on one box. The value type must match the field type: a string for TEXT_INPUT and DROPDOWN, milliseconds since epoch for DATE, a boolean for CHECKBOX, a user key for PERSON. Use List Pipeline Fields to find the field key and type. |
| Update Comment | `updateComment` | Edit the text of an existing comment. |
| Update Contact | `updateContact` | Update a contact. Only the properties supplied are changed. Array properties such as emailAddresses and addresses are replaced wholesale, so send the complete list you want stored. |
| Update Contact Field Value | `updateContactFieldValue` | Set the value of one custom contact field on a contact. Reconciled live 2026-09-16: Streak answers 200 {"success":true} even when the fieldKey does not exist, and silently discards the write. A 200 is NOT proof the value landed - read the contact back and check its fields map. Custom contact fields can only be created in the Streak UI, not through the API, so fieldKey must come from List Contact Fields. |
| Update Meeting | `updateMeeting` | Update a meeting note or call log. Only the properties supplied are changed. |
| Update Organization | `updateOrganization` | Update an organization. Only the properties supplied are changed. Array properties such as domains and addresses are replaced wholesale, so send the complete list you want stored. |
| Update Organization Field Value | `updateOrganizationFieldValue` | Set the value of one custom organization field on an organization. Reconciled live 2026-09-16: Streak answers 200 {"success":true} even when the fieldKey does not exist, and silently discards the write. A 200 is NOT proof the value landed - read the organization back and check its fields map. Custom organization fields can only be created in the Streak UI, not through the API, so fieldKey must come from List Organization Fields. |
| Update Pipeline | `updatePipeline` | Update a pipeline's name, stage order, sharing scope or ACL. Only the properties supplied are changed; omitted properties are left untouched. |
| Update Pipeline Field | `updatePipelineField` | Rename a pipeline's custom field. The field key and type are unchanged, so existing box values are preserved. |
| Update Snippet | `updateSnippet` | Update an email snippet. Only the properties supplied are changed. |
| Update Stage | `updateStage` | Rename a stage of a pipeline. The stage key never changes, so boxes stay where they are. |
| Update Task | `updateTask` | Update a task: change its text, due date, assignees, or mark it complete by sending status DONE. Only supplied properties are changed. |
| Update Webhook | `updateWebhook` | Update a registered webhook's event, target URL or token. Only supplied properties are changed. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Box changed pipeline | `BOX_CHANGE_PIPELINE` | A box moved to a different pipeline. Read pipelineKey for the new pipeline. Pipeline scoped. |
| Box changed stage | `BOX_CHANGE_STAGE` | A box moved to a different stage. Read stageKey for the new stage. Pipeline scoped. |
| Box created | `BOX_CREATE` | A new box (record) was created in the subscribed pipeline. Pipeline scoped: set pipelineKey on the trigger. |
| Box deleted | `BOX_DELETE` | A box was deleted from the subscribed pipeline. Pipeline scoped. |
| Box edited | `BOX_EDIT` | A custom field, the notes, the assignee or the name changed on a box. Pipeline scoped. |
| Box saw a new email address | `BOX_NEW_EMAIL_ADDRESS` | A new email address was detected on a box, usually from a newly filed Gmail thread. Pipeline scoped. |
| Comment created | `COMMENT_CREATE` | Someone commented on a box in the subscribed pipeline. Pipeline scoped. |
| Contact created | `CONTACT_CREATE` | A contact was created in the subscribed team. Team scoped: set teamKey on the trigger, or leave it empty to use the first team of the connected user. |
| Contact deleted | `CONTACT_DELETE` | A contact was deleted from the subscribed team. Team scoped. |
| Contact updated | `CONTACT_UPDATE` | A contact in the subscribed team changed. Team scoped. |
| Meeting note or call log created | `MEETING_CREATE` | A meeting note or call log was recorded on a box. Pipeline scoped. |
| Meeting note or call log updated | `MEETING_UPDATE` | An existing meeting note or call log changed. Pipeline scoped. |
| Organization created | `ORG_CREATE` | An organization was created in the subscribed team. Team scoped. |
| Organization deleted | `ORG_DELETE` | An organization was deleted from the subscribed team. Team scoped. |
| Organization updated | `ORG_UPDATE` | An organization in the subscribed team changed. Team scoped. |
| Stage created | `STAGE_CREATE` | A new stage was added to the subscribed pipeline. Pipeline scoped. |
| Task completed | `TASK_COMPLETE` | A task was marked done. status is DONE on the delivered object. Pipeline scoped. |
| Task created | `TASK_CREATE` | A task was created on a box. Pipeline scoped. |
| Task due | `TASK_DUE` | A task reached its due date. Pipeline scoped. |
| Task updated | `TASK_UPDATED` | Anything about a task changed: text, due date, status or assignees. Pipeline scoped. |
