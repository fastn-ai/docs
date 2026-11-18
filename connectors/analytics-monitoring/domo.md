---
description: "Domo is a cloud business intelligence platform for connecting, visualizing, and acting on data."
hidden: true
---

# Domo

<img src="../../.gitbook/assets/connectors/lg/domo.png" alt="Domo logo">

Domo is a cloud business intelligence platform for connecting, visualizing, and acting on data. This connector covers Domo's public v1 REST API: DataSets (create, query, import, export, PDP policies), Streams, the Simple API, Accounts, Users, Groups, Pages and Page Collections, Cards, Embed tokens, Projects and Tasks, and the Activity Log.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [domo.com](https://domo.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `domo` |

## Use it

Add Domo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.domo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Abort Stream Execution | `abortStreamExecution` | Aborts an entire Stream execution, discarding any uploaded data parts. |
| Add Drill View | `addDrillView` | Adds a new drill-down view definition to an existing card. Note: left untested by policy since it would mutate a real, existing dashboard card and Domo's public API has no way to remove a drill view. |
| Add Task Attachment | `addTaskAttachment` | Adds a file as an attachment to a task, sent as multipart/form-data. Left untested by policy: Domo's live Create Task endpoint (PUT documented, 500s on POST) currently cannot produce a real task ID to attach a file to on this instance, and binary/multipart file uploads are not reliably certifiable through this execution engine in any case. |
| Add User To Group | `addUserToGroup` | Adds a user to a group in your Domo instance. |
| Commit Stream Execution | `commitStreamExecution` | Commits a Stream execution, importing the combined set of data parts that were successfully uploaded into the DataSet. |
| Create Account | `createAccount` | Creates a new data source Account. The account type's specific credential properties vary by type; use Get Account Type to discover the required properties for a given type ID first. |
| Create Chart Card | `createChartCard` | Creates a new chart card to visualize data from an existing DataSet. Note: Domo's public API has no card-delete endpoint, so this action is left untested to avoid creating a permanent, un-removable card. |
| Create DataSet | `createDataSet` | Creates a new, empty DataSet in your Domo instance. Once created, data can be imported into it with Import Data Into DataSet. |
| Create DataSet (Simple API) | `createSimpleDataSet` | Creates a new DataSet using the Simple API, a lightweight convenience wrapper for JSON-based imports. Once created, use Import JSON Data to load rows. The created DataSet can also be managed through the standard DataSet API. |
| Create Embed Token (Cards) | `createCardEmbedToken` | Creates an authentication token for embedding one or more cards in an external application. |

<details>

<summary>See 77 more actions</summary>

* **Create Embed Token (Dashboard)** `createDashboardEmbedToken`: Creates an authentication token for embedding a page/dashboard (story) in an external application.
* **Create Group** `createGroup`: Creates a new group in your Domo instance.
* **Create Page** `createPage`: Creates a new page in your Domo instance.
* **Create Page Collection** `createPageCollection`: Creates a new card collection within a page.
* **Create PDP Policy** `createPdpPolicy`: Creates a Personalized Data Permission (PDP) policy that restricts which rows of a DataSet specific users or groups can see.
* **Create Project** `createProject`: Creates a new project in your Domo instance.
* **Create Project List** `createProjectList`: Creates a new task list (swim lane) within a project.
* **Create Stream** `createStream`: Creates a new Stream. As a convenience, this also creates the underlying DataSet using the name, description, and schema you provide. Streams support append and replace (upsert) import methods for high-volume data loads.
* **Create Stream Execution** `createStreamExecution`: Starts a new execution on a Stream, so data parts can then be uploaded and committed.
* **Create Task** `createTask`: Adds a new task to a project list. Known live-API defect (evidenced 2026-08-15): Domo's OpenAPI spec documents this as PUT, which the live API rejects with 405 Method Not Allowed; POST is accepted at the routing level but returns a 500 Internal Server Error for every payload tried (minimal, with priority/ownedBy, against both a default and a custom list). This is a vendor-side defect, not a wiring issue.
* **Create User** `createUser`: Creates a new user in your Domo instance. Note: Domo's public API has no user-delete endpoint, so this action is left untested to avoid creating a permanent, un-removable account.
* **Delete Account** `deleteAccount`: Permanently deletes an Account from your Domo instance. This is destructive and cannot be reversed.
* **Delete DataSet** `deleteDataSet`: Permanently deletes a DataSet from your Domo instance. This is destructive and cannot be reversed.
* **Delete Group** `deleteGroup`: Permanently deletes a group from your Domo instance. This is destructive and cannot be reversed.
* **Delete Page** `deletePage`: Permanently deletes a page from your Domo instance. This is destructive and cannot be reversed.
* **Delete Page Collection** `deletePageCollection`: Permanently deletes a page collection from your Domo instance. This is destructive and cannot be reversed.
* **Delete PDP Policy** `deletePdpPolicy`: Permanently deletes a Personalized Data Permission (PDP) policy from a DataSet. This is destructive and cannot be reversed.
* **Delete Project** `deleteProject`: Permanently deletes a project from your Domo instance, including its lists, tasks, and attachments. This is destructive and cannot be reversed.
* **Delete Project List** `deleteProjectList`: Permanently deletes a list from a project, including any tasks it contains. This is destructive and cannot be reversed.
* **Delete Stream** `deleteStream`: Deletes a Stream from your Domo instance. This does not delete the associated DataSet. This is destructive and cannot be reversed.
* **Delete Task Attachment** `deleteTaskAttachment`: Permanently deletes an attachment from a task. This is destructive and cannot be reversed.
* **Download Task Attachment** `downloadTaskAttachment`: Downloads an individual task attachment given its ID.
* **Export Data From DataSet** `exportDataSetData`: Exports the current data in a DataSet as CSV. Data types are exported as currently stored in the DataSet.
* **Get Account** `getAccount`: Retrieves the details of an existing Account.
* **Get Account Type** `getAccountType`: Retrieves the details of an Account Type, including the template of properties required to create an Account of this type.
* **Get Card** `getCard`: Retrieves the details of an existing card.
* **Get Chart Card Definition** `getCardDefinition`: Retrieves the chart definition for an existing chart card, including its DataSet, chart type, and visualization body.
* **Get DataSet** `getDataSet`: Retrieves the details of an existing DataSet, including its schema and PDP policies.
* **Get Drill Properties** `getDrillProperties`: Retrieves the drill path views configured on a card.
* **Get Group** `getGroup`: Retrieves the details of an existing group.
* **Get Page** `getPage`: Retrieves the details of an existing page.
* **Get PDP Policy** `getPdpPolicy`: Retrieves a single Personalized Data Permission (PDP) policy on a DataSet.
* **Get Project** `getProject`: Retrieves the details of an individual project. Use the special project ID 'me' to return your personal project.
* **Get Project List** `getProjectList`: Retrieves the details of an individual list given a project ID and list ID.
* **Get Stream** `getStream`: Retrieves the details of an existing Stream.
* **Get Stream Execution** `getStreamExecution`: Retrieves the details of an existing Stream execution.
* **Get Task** `getTask`: Retrieves an individual task from a given project and list.
* **Get User** `getUser`: Retrieves the details of an existing user by their Domo user ID.
* **Import Data Into DataSet** `importDataSetData`: Imports CSV-formatted data into an existing DataSet, either replacing all data or appending new rows.
* **Import JSON Data Into DataSet** `importSimpleJsonData`: Imports an array of JSON row objects into a DataSet created via the Simple API, inferring columns from the object keys on first import.
* **List Account Types** `listAccountTypes`: Retrieves a paginated list of all Account Types for which the caller has permissions, e.g. amazon-s3, http, webhook.
* **List Accounts** `listAccounts`: Retrieves a paginated list of all data source Accounts for which the caller has permissions.
* **List Activity Log Entries** `listActivityLogEntries`: Retrieves activity log entries recorded in your Domo instance within a given time window.
* **List All Project Tasks** `listProjectTasks`: Retrieves all tasks across every list within a project.
* **List Cards** `listCards`: Retrieves a paginated list of cards for which the caller has permission.
* **List DataSets** `listDataSets`: Retrieves a paginated list of all DataSets in your Domo instance.
* **List Groups** `listGroups`: Retrieves a paginated list of all groups in your Domo instance.
* **List Page Collections** `listPageCollections`: Retrieves the collections that belong to a page.
* **List Pages** `listPages`: Retrieves a paginated list of all pages in your Domo instance.
* **List PDP Policies** `listPdpPolicies`: Lists the Personalized Data Permission (PDP) policies configured on a DataSet.
* **List Project Lists** `listProjectLists`: Retrieves all task lists (swim lanes) available within a project.
* **List Project Members** `listProjectMembers`: Retrieves the IDs of the users that are members of a project.
* **List Projects** `listProjects`: Retrieves a list of all projects that the connection's client scope has access to.
* **List Stream Executions** `listStreamExecutions`: Returns all Stream Execution objects for a given Stream.
* **List Streams** `listStreams`: Retrieves a paginated list of all Streams for which the caller has view permissions.
* **List Task Attachments** `listTaskAttachments`: Retrieves details about all attachments belonging to a task.
* **List Tasks In List** `listListTasks`: Retrieves all tasks from a given project list.
* **List Users** `listUsers`: Retrieves a paginated list of all users in your Domo instance.
* **List Users In Group** `listGroupUsers`: Lists the IDs of the users that belong to a group in your Domo instance.
* **Query DataSet** `queryDataSet`: Runs a SQL SELECT query against the data stored in a Domo DataSet.
* **Remove User From Group** `removeUserFromGroup`: Removes a user from a group in your Domo instance.
* **Search Streams** `searchStreams`: Returns all Streams that match the given search qualifier, such as by DataSet ID.
* **Share Account** `shareAccount`: Shares an Account with another user, granting them access to it. Note: Domo's OpenAPI spec documents this as a GET, but the live API only accepts POST /v1/accounts/{id}/shares with a {"user":{"id":...}} JSON body; verified live 2026-08-15.
* **Update Account** `updateAccount`: Updates the specified Account's metadata and/or type-specific credential properties. Known live-API defect (evidenced 2026-08-15): Domo's real PATCH /v1/accounts/{id} endpoint returns 400 'Unrecognized token' from its own JSON parser whenever name and type are both present in the body (matching the exact shape documented and accepted by Create Account), and 500 Internal Server Error when only type is sent; a name-only body is accepted for parsing but then rejected with 'accountType is required'. This was reproduced across several request shapes with byte-valid JSON, so it is a vendor-side defect, not a wiring issue.
* **Update Chart Card Definition** `updateChartCardDefinition`: Updates the definition of an existing chart card. Note: left untested by policy since it would mutate a real, existing dashboard card and Domo's public API has no way to restore or delete a card.
* **Update DataSet** `updateDataSet`: Updates the specified DataSet's metadata: name, description, PDP enablement, and/or schema. To import additional rows use Import Data Into DataSet instead.
* **Update Group** `updateGroup`: Updates the specified group's name and/or active status. Any attribute left out is unchanged.
* **Update Page** `updatePage`: Updates the specified page. Any attribute left out of the request is unchanged. Collections cannot be added or removed here, only reordered.
* **Update Page Collection** `updatePageCollection`: Updates the title, description, or card membership of a page collection.
* **Update PDP Policy** `updatePdpPolicy`: Updates an existing Personalized Data Permission (PDP) policy on a DataSet.
* **Update Project** `updateProject`: Updates attributes of an existing project. The id, members, createdBy, and createdDate fields are read-only and cannot be updated with this action; use Update Project Members to change membership.
* **Update Project List** `updateProjectList`: Updates the details of a list given an existing project ID and list ID.
* **Update Project Members** `updateProjectMembers`: Replaces the full set of members assigned to a project.
* **Update Stream** `updateStream`: Updates the specified Stream's data import behavior (update method).
* **Update Task** `updateTask`: Updates the details of a task given an existing project, list, and task ID.
* **Update User** `updateUser`: Updates the specified user's profile attributes. Any attribute left out of the request is unchanged.
* **Upload Stream Execution Data Part** `uploadStreamExecutionPart`: Uploads a chunk of CSV row data as a numbered part of a Stream execution. Parts should be uploaded in increasing sequence.

</details>
