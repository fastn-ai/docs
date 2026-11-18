---
description: "ServiceNow ITSM platform connector."
hidden: true
---

# ServiceNow

<img src="../../.gitbook/assets/connectors/servicenow.png" alt="ServiceNow logo" width="64">

ServiceNow ITSM platform connector. Full CRUD over the Table API (incident, problem, change_request, sc_request, task, sys_user, and any generic table), plus Attachment API, Aggregate/Stats API, dictionary field management, and Business-Rule-based outbound webhooks. Base URL https://{instance}.service-now.com/api/now

| | |
| --- | --- |
| **Category** | [IT and service management](README.md) |
| **Website** | [servicenow.com](https://servicenow.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `servicenow` |

## Use it

Add ServiceNow from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.servicenow.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Custom Field | `addCustomField` | Add a custom column/field to a table by creating a sys_dictionary entry. Returns the created dictionary record. |
| Create Asset | `createAsset` | Create an asset record in the Asset table (alm_asset). Supply the model as a sys_id from the product model tables. Returns the created asset including its sys_id. |
| Create Business Rule | `createBusinessRule` | Create a Business Rule (sys_script) on a table. Used to register outbound webhooks: an after-insert/update/delete rule whose script posts a payload to an external URL via sn_ws.RESTMessageV2. Returns the created rule including sys_id. |
| Create Change Request | `createChangeRequest` | Create a new change request in the change_request table. Returns the created record including sys_id and number (CHGxxxxxxx). |
| Create Event | `createEvent` | Create an Event Management event (em_event) so ServiceNow can correlate it into an alert. Requires the Event Management plugin to be active on the instance. |
| Create Hardware Asset | `createHardware` | Create a hardware asset record in the Hardware table (alm_hardware). Supply the model as a sys_id from the hardware product model table. Returns the created record including its sys_id. |
| Create Hardware Model | `createModel` | Create a hardware product model (cmdb_hardware_product_model) that assets and hardware records can reference. Returns the created model including its sys_id. |
| Create Incident | `createIncident` | Create a new incident record in the ServiceNow incident table. Returns the created record including its sys_id and auto-generated number (INCxxxxxxx). |
| Create Problem | `createProblem` | Create a new problem record in the problem table. Returns the created record including sys_id and number (PRBxxxxxxx). |
| Create Service Request | `createServiceRequest` | Create a new service request (REQ) record in the sc_request table. Returns the created record including sys_id and number (REQxxxxxxx). |

<details>

<summary>See 65 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create System Property | `createSystemProperty` | Create a new system property (sys_properties) on the instance. System properties change how the instance behaves, so only create properties owned by your own integration and use a clearly namespaced name. |
| Create Table Record | `createTableRecord` | Create a record in ANY ServiceNow table. Pass the field name/value pairs as the 'fields' object. Generic Table API insert. |
| Create Task | `createTask` | Create a generic task record in the task table. Returns the created record including sys_id and number (TASKxxxxxxx). |
| Create User | `createUser` | Create a new user record in the sys_user table. Returns the created record including sys_id. |
| Delete Asset | `deleteAsset` | Delete an asset record from the Asset table (alm_asset) by sys_id. Returns HTTP 204 with no body on success. |
| Delete Attachment | `deleteAttachment` | Delete an attachment by its sys_id via the Attachment API. Returns HTTP 204 with no body on success. |
| Delete Business Rule | `deleteBusinessRule` | Delete a Business Rule (sys_script) by sys_id. Used to unregister a webhook. Returns HTTP 204 with no body on success. |
| Delete Change Request | `deleteChangeRequest` | Delete a change request by sys_id. Returns HTTP 204 with no body on success. |
| Delete Event | `deleteEvent` | Delete an Event Management event (em_event) by sys_id. Returns HTTP 204 with no body on success. Requires the Event Management plugin to be active on the instance. |
| Delete Hardware Asset | `deleteHardware` | Delete a hardware asset from the Hardware table (alm_hardware) by sys_id. Returns HTTP 204 with no body on success. |
| Delete Hardware Model | `deleteModel` | Delete a hardware product model (cmdb_hardware_product_model) by sys_id. Returns HTTP 204 with no body on success. Models referenced by existing assets should not be removed. |
| Delete Incident | `deleteIncident` | Delete an incident by sys_id. Returns HTTP 204 with no body on success. |
| Delete Problem | `deleteProblem` | Delete a problem by sys_id. Returns HTTP 204 with no body on success. |
| Delete Service Request | `deleteServiceRequest` | Delete a service request by sys_id. Returns HTTP 204 with no body on success. |
| Delete System Property | `deleteSystemProperty` | Remove a system property (sys_properties) from the instance by sys_id. Returns HTTP 204 with no body on success. Removing a property that other code reads can change instance behaviour, so only remove properties your integration created. |
| Delete Table Record | `deleteTableRecord` | Delete a record by sys_id from ANY ServiceNow table. Returns HTTP 204 with no body on success. |
| Delete Task | `deleteTask` | Delete a task by sys_id. Returns HTTP 204 with no body on success. |
| Delete User | `deleteUser` | Delete a user by sys_id from the sys_user table. Returns HTTP 204 with no body on success. |
| Get Aggregate Stats | `getAggregateStats` | Run aggregate computations (count, sum, avg, min, max, group by) over any table using the Aggregate API at /api/now/stats. Useful for dashboards and reporting. |
| Get Asset | `getAsset` | Retrieve a single asset record from the Asset table (alm_asset) by its sys_id. |
| Get Attachment | `getAttachment` | Get the metadata for a single attachment by its sys_id via the Attachment API. |
| Get Business Rule | `getBusinessRule` | Retrieve a single Business Rule (sys_script) by sys_id. |
| Get Change Request | `getChangeRequest` | Retrieve a single change request by sys_id. |
| Get Event | `getEvent` | Retrieve a single Event Management event (em_event) by its sys_id. Requires the Event Management plugin to be active on the instance. |
| Get Hardware Asset | `getHardware` | Retrieve a single hardware asset from the Hardware table (alm_hardware) by its sys_id. |
| Get Hardware Model | `getModel` | Retrieve a single hardware product model (cmdb_hardware_product_model) by its sys_id. |
| Get Incident | `getIncident` | Retrieve a single incident by its sys_id from the incident table. |
| Get KB Article | `getKBArticle` | Retrieve a single Knowledge Base article (kb_knowledge) by sys_id. Defaults sysparm_display_value=all so reference fields (knowledge base, category, author) are returned with resolved display names as well as sys_ids. |
| Get KB Article Feedback | `getKBArticleFeedback` | Retrieve user feedback (kb_feedback) for a knowledge article by its sys_id - ratings, helpful flag and comments. Useful for surfacing the most helpful articles. Returns an array of feedback rows (empty if the article has no feedback). Note: aggregate view/helpful counts also live directly on the article (sys_view_count, helpful_count, use_count, rating) via getKBArticle. |
| Get Problem | `getProblem` | Retrieve a single problem by sys_id from the problem table. |
| Get Service Request | `getServiceRequest` | Retrieve a single service request by sys_id from the sc_request table. |
| Get System Property | `getSystemProperty` | Retrieve a single ServiceNow system property (sys_properties) by its sys_id, including its current value and description. |
| Get Table Field Definitions | `getTableFieldDefinitions` | List the column/field definitions of a table by querying sys_dictionary. Returns element name, label, type, mandatory flag, max length and reference table for each field. |
| Get Table Record | `getTableRecord` | Retrieve a single record by sys_id from ANY ServiceNow table (cmdb_ci, kb_knowledge, sys_user_group, etc.). Generic Table API getter. |
| Get Task | `getTask` | Retrieve a single task by sys_id from the task table. |
| Get User | `getUser` | Retrieve a single user by sys_id from the sys_user table. |
| List Assets | `listAssets` | List asset records from the ServiceNow Asset table (alm_asset) with an optional encoded query, field selection and pagination. |
| List Attachments | `listAttachments` | List attachment metadata records via the Attachment API. Filter by table_name/table_sys_id using an encoded query. |
| List Business Rules | `listBusinessRules` | Query Business Rules (sys_script) with an encoded query, field selection and pagination. Use to find webhook registration rules. |
| List Change Requests | `listChangeRequests` | Query change_request records with optional encoded query, field selection, and pagination. |
| List Events | `listEvents` | List Event Management events (em_event) with an optional encoded query, field selection and pagination. Requires the Event Management plugin to be active on the instance. |
| List Hardware Assets | `listHardwares` | List hardware asset records from the Hardware table (alm_hardware) with an optional encoded query, field selection and pagination. |
| List Hardware Models | `listModels` | List hardware product models (cmdb_hardware_product_model) with an optional encoded query, field selection and pagination. Models are the catalogue entries that assets and hardware records reference. |
| List Incidents | `listIncidents` | Query incident records with optional encoded query, field selection, pagination and display-value options. Returns an array of incidents. |
| List KB Categories | `listKBCategories` | List categories (kb_category) for browsing/filtering. Pass parent_id (a knowledge base sys_id) to list the categories within that base. Supports pagination. |
| List Knowledge Bases | `listKnowledgeBases` | List all Knowledge Base containers (kb_knowledge_base). Needed to discover which bases exist before searching or browsing articles. Supports optional filtering and pagination. |
| List Problems | `listProblems` | Query problem records with optional encoded query, field selection, and pagination. |
| List Service Requests | `listServiceRequests` | Query sc_request records with optional encoded query, field selection, and pagination. |
| List System Properties | `listSystemProperties` | List ServiceNow system properties (sys_properties) with an optional encoded query, field selection and pagination. System properties control instance behaviour, so treat the results as configuration data. |
| List Table Records | `listTableRecords` | Query records from ANY ServiceNow table with an encoded query, field selection, and pagination. Generic Table API list. |
| List Tasks | `listTasks` | Query task records with optional encoded query, field selection, and pagination. |
| List Users | `listUsers` | Query sys_user records with optional encoded query, field selection, and pagination. |
| Search KB Articles | `searchKBArticles` | Keyword search across Knowledge Base articles (kb_knowledge) using ServiceNow full-text search, with optional filters for knowledge base, category, workflow state and active flag. Cleaner than building a raw sysparm_query. Returns an array of matching articles. |
| Update Business Rule | `updateBusinessRule` | Partially update a Business Rule (sys_script) by sys_id. Pass only the columns you want to change in the 'fields' JSON-object string; all other fields on the record are left untouched (PATCH). Used to enable/disable or re-point a webhook registration rule. Returns the full updated rule. |
| Update Change Request | `updateChangeRequest` | Partially update an existing change request by sys_id. Pass only the columns you want to change in the 'fields' JSON-object string; all other fields on the record are left untouched (PATCH). Returns the full updated change request. |
| Update Event | `updateEvent` | Partially update an Event Management event (em_event) by sys_id. Only the fields you supply are changed. Requires the Event Management plugin to be active on the instance. |
| Update Incident | `updateIncident` | Partially update an existing incident by sys_id. Pass only the columns you want to change in the 'fields' JSON-object string; all other fields on the record are left untouched (PATCH). Returns the full updated incident. |
| Update Incident (Typed) | `updateIncidentTyped` | Partially update an incident by sys_id with typed fields (PATCH /table/incident/{sys_id}). Only the fields provided are sent; all others are left unchanged. Returns the full updated incident under result. |
| Update Problem | `updateProblem` | Partially update an existing problem by sys_id. Pass only the columns you want to change in the 'fields' JSON-object string; all other fields on the record are left untouched (PATCH). Returns the full updated problem. |
| Update Service Request | `updateServiceRequest` | Partially update an existing service request (sc_request) by sys_id. Pass only the columns you want to change in the 'fields' JSON-object string; all other fields on the record are left untouched (PATCH). Returns the full updated service request. |
| Update System Property | `updateSystemProperty` | Partially update a system property (sys_properties) by sys_id. Only the fields you supply are changed. Changing a property alters instance behaviour, so update only properties your integration owns. |
| Update Table Record | `updateTableRecord` | Update a record in ANY ServiceNow table by sys_id. Pass changed field name/value pairs as the 'fields' object. Generic Table API PATCH (partial update). |
| Update Task | `updateTask` | Partially update an existing task by sys_id. Pass only the columns you want to change in the 'fields' JSON-object string; all other fields on the record are left untouched (PATCH). Returns the full updated task. |
| Update User | `updateUser` | Partially update an existing user (sys_user) by sys_id. Pass only the columns you want to change in the 'fields' JSON-object string; all other fields on the record are left untouched (PATCH). Returns the full updated user. |
| Upload Attachment | `uploadAttachment` | Attach a file to a record on any table via the Attachment API (/api/now/attachment/file). The raw file content goes in the request body; table name, target record sys_id and file name are query params. Returns attachment metadata. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Change Request Created | `change_request.created` | Fires when a new change request is inserted. |
| Change Request Updated | `change_request.updated` | Fires when a change request is updated. |
| Incident Created | `incident.created` | Fires when a new incident is inserted. |
| Incident Deleted | `incident.deleted` | Fires when an incident is deleted. |
| Incident Resolved | `incident.resolved` | Fires when an incident transitions to a resolved state (state=6). |
| Incident Updated | `incident.updated` | Fires when an incident is updated. |
| Knowledge Article Created | `kb_knowledge.created` | Fires when a new knowledge article (kb_knowledge) is inserted. |
| Knowledge Article Deleted | `kb_knowledge.deleted` | Fires when a knowledge article is deleted. |
| Knowledge Article Published | `kb_knowledge.published` | Fires when a knowledge article transitions to workflow_state=published. |
| Knowledge Article Updated | `kb_knowledge.updated` | Fires when a knowledge article is updated. |

<details>

<summary>See 7 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Problem Created | `problem.created` | Fires when a new problem is inserted. |
| Problem Updated | `problem.updated` | Fires when a problem is updated. |
| Service Request Created | `sc_request.created` | Fires when a new service request (REQ) is inserted. |
| Service Request Updated | `sc_request.updated` | Fires when a service request is updated. |
| Task Created | `task.created` | Fires when a new task is inserted. |
| Task Updated | `task.updated` | Fires when a task is updated. |
| User Created | `sys_user.created` | Fires when a new user is created. |

</details>
