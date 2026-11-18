---
description: "AITable.ai Fusion API — datasheets, records, fields, views, nodes, embed links, contacts (members/teams/roles), attachments and AI chat completions."
hidden: true
---

# AITable.ai

AITable.ai Fusion API — datasheets, records, fields, views, nodes, embed links, contacts (members/teams/roles), attachments and AI chat completions. Base https://aitable.ai/fusion. Auth: personal API token sent as Authorization: Bearer.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [aitable.ai](https://aitable.ai) |
| **Authentication** | API key |
| **Actions** | 32 |
| **Events** | 4 |
| **Slug** | `aitable` |

## Use it

Add AITable.ai from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.aitable.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Chat Completion | `createChatCompletion` | Send an OpenAI-compatible chat completion request to an AITable AI agent. aiId is the Bot ID shown at the top of the AI agent's setting panel. This API is whitelist-only: unapproved accounts, and unknown bot ids, get 200 with an AiNotFoundError envelope. |
| Create Datasheet | `createDatasheet` | Create a datasheet in a space. NOTE: AITable's Fusion API has no delete-datasheet/delete-node endpoint — a datasheet created here can only be removed from the AITable web app (right click the node &gt; Delete). Field objects that need a property (e.g. SingleText) must include a property object or the API returns 400 'Invalid value for fields[X].property'. |
| Create Embedded Link | `createEmbedLink` | Create an embedded (public embed) link for a node. Requires a golden-level (paid) space — other spaces get 200 with code 1502 'sorry, it can only be invoked in golden-level space'. |
| Create Field | `createField` | Create a field in a datasheet. Supported types include SingleText, Text, SingleSelect, MultiSelect, Number, Currency, Percent, DateTime, Attachment, Member, Checkbox, Rating, URL, Phone, Email, WorkDoc, OneWayLink, TwoWayLink, MagicLookUp, Formula, AutoNumber, CreatedTime, LastModifiedTime, CreatedBy, LastModifiedBy, Button. Types such as SingleText require a property object. |
| Create Records | `createRecords` | Create up to 10 records in a datasheet in one call. Returns the created records with their recordIds. |
| Create Role | `createRole` | Create a role in a space. Enterprise-plan only — other plans get 200 with code 1503 'This API is only available for the Enterprise plan'. |
| Create Team | `createTeam` | Create a team under a parent team. Enterprise-plan only — other plans get 200 with code 1503 'This API is only available for the Enterprise plan'. |
| Delete Embedded Link | `deleteEmbedLink` | Delete an embedded link from a node by link id. Requires a golden-level (paid) space — other spaces get 200 with code 1502 'sorry, it can only be invoked in golden-level space'. |
| Delete Field | `deleteField` | Delete a field from a datasheet by field id. The primary field cannot be deleted. |
| Delete Member | `deleteMember` | Remove a member from the space by unitId. Enterprise-plan only — other plans get 200 with code 1503 'This API is only available for the Enterprise plan'. |
| Delete Records | `deleteRecords` | Delete up to 10 records from a datasheet. recordIds is a comma separated list of record ids. |
| Delete Role | `deleteRole` | Delete a role by unitId. Enterprise-plan only — other plans get 200 with code 1503 'This API is only available for the Enterprise plan'. |
| Delete Team | `deleteTeam` | Delete a team by unitId. Enterprise-plan only — other plans get 200 with code 1503 'This API is only available for the Enterprise plan'. |
| Get Embedded Links | `getEmbedLinks` | List the embedded links of a node. Requires a golden-level (paid) space — other spaces get 200 with code 1502 'sorry, it can only be invoked in golden-level space'. |
| Get Fields | `getFields` | Get all fields of a datasheet. Optionally restrict to the fields visible in one view. Returns data.fields[] with id, name, type, property, editable, isPrimary. |
| Get Member | `getMember` | Get one space member by unitId. Enterprise-plan only — other plans get 200 with code 1503 'This API is only available for the Enterprise plan'. |
| Get Node Details | `getNodeDetail` | Get details of one node (folder, datasheet, form, dashboard or mirror) in a space. |
| Get Node List | `getNodes` | Get the first-level nodes (folders and files) of a space. Returns data.nodes[] with id, name, type, icon, isFav, permission. |
| Get Records | `getRecords` | Get records from a datasheet (Fusion API v1). Supports paging, view scoping, formula filtering, sorting and field selection. Returns data.total and data.records[] with recordId, fields, createdAt, updatedAt. |
| Get Records (Fusion API v3) | `getRecordsV3` | Get records using the Fusion API v3 data engine. v3 is in vendor internal testing and currently only exposes the get-records route; it is not generally available and returns HTTP 500 for accounts outside the beta. |
| Get Spaces | `getSpaces` | Get the list of spaces the API token's user belongs to. Returns data.spaces[] with id, name and isAdmin. |
| Get Views | `getViews` | Get all views of a datasheet. Returns data.views[] with id, name and type (Grid, Kanban, Gallery, Gantt, Calendar). |
| List Roles | `listRoles` | List all roles in a space. Enterprise-plan only — other plans get 200 with code 1503 'This API is only available for the Enterprise plan'. |
| List Team Members | `listTeamMembers` | List the members of a team. Enterprise-plan only — other plans get 200 with code 1503 'This API is only available for the Enterprise plan'. |
| List Teams | `listSubTeams` | List the child teams of a team. Pass unitId '0' for the root team of the space. Enterprise-plan only — other plans get 200 with code 1503 'This API is only available for the Enterprise plan'. |
| List Units under the Role | `listRoleUnits` | List the members and teams assigned to a role. Enterprise-plan only — other plans get 200 with code 1503 'This API is only available for the Enterprise plan'. |
| Search Nodes | `searchNodes` | Search all nodes in a space by type (Fusion API v2). 'type' is REQUIRED and must be one of Folder, Datasheet, Form, Dashboard, Mirror. Optional 'query' matches the node name and 'permissions' filters by permission level (comma separated, e.g. 0,1). |
| Update Member | `updateMember` | Update a space member (change their teams). Enterprise-plan only — other plans get 200 with code 1503 'This API is only available for the Enterprise plan'. |
| Update Records | `updateRecords` | Update up to 10 existing records in a datasheet in one call. Each item must carry a recordId. |
| Update Role | `updateRole` | Rename or reorder a role. Enterprise-plan only — other plans get 200 with code 1503 'This API is only available for the Enterprise plan'. |
| Update Team | `updateTeam` | Update a team's name, parent, order or roles. Enterprise-plan only — other plans get 200 with code 1503 'This API is only available for the Enterprise plan'. |
| Upload Attachment | `uploadAttachment` | Upload a text file as an attachment to a datasheet. Returns data.token / data.url which you then write into an Attachment field via Create Records or Update Records. Sends a multipart/form-data part named 'file'. Binary payloads are not supported by this action — pass text content only. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Form is Submitted | `form.submitted` | Fires when one of the datasheet's Magic Forms is submitted. AITable has NO webhook registration API — registration is UI-only. Click path: datasheet &gt; 'Automation' &gt; 'Create automation' &gt; Trigger: 'Form is submitted' &gt; select the form &gt; 'Add action' &gt; 'Send web request' &gt; POST to the fastn trigger URL &gt; HTTP Body 'json' containing {"eventType":"form.submitted", ...} &gt; Save &gt; toggle ON. Body is user-composed, so this schema is MODELLED, not captured. |
| Record is Created | `record.created` | Fires when a new record is created in a chosen datasheet. AITable has NO webhook registration API — registration is UI-only. Click path: open the space &gt; open the datasheet &gt; 'Automation' in the top-right toolbar &gt; 'Create automation' &gt; Trigger: 'Record is created' &gt; select the datasheet &gt; 'Add action' &gt; 'Send web request' &gt; Method POST &gt; Request URL: paste the fastn trigger URL &gt; HTTP Body: choose 'json' and compose a body that BEGINS with the literal routing key, e.g. The body is fully user-composed, so the schema below is MODELLED, not captured from a real delivery. |
| Record Matches Conditions | `record.matchesConditions` | Fires when a record starts matching a filter you define (AITable's stand-in for 'record updated'). AITable has NO webhook registration API — registration is UI-only. Click path: datasheet &gt; 'Automation' &gt; 'Create automation' &gt; Trigger: 'Record matches conditions' &gt; pick the datasheet, view and filter conditions &gt; 'Add action' &gt; 'Send web request' &gt; POST to the fastn trigger URL &gt; HTTP Body 'json' containing {"eventType":"record.matchesConditions", ...} &gt; Save &gt; toggle ON. Body is user-composed, so this schema is MODELLED, not captured. |
| Scheduled Time Arrives | `schedule.fired` | Fires on the schedule you configure (AITable's time-based automation trigger). AITable has NO webhook registration API — registration is UI-only. Click path: datasheet &gt; 'Automation' &gt; 'Create automation' &gt; Trigger: 'Scheduled time arrives' &gt; set the schedule &gt; 'Add action' &gt; 'Send web request' &gt; POST to the fastn trigger URL &gt; HTTP Body 'json' containing {"eventType":"schedule.fired", ...} &gt; Save &gt; toggle ON. Body is user-composed, so this schema is MODELLED, not captured. |
