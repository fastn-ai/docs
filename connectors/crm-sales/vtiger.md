---
description: "Vtiger CRM Cloud REST API connector."
hidden: true
---

# Vtiger

<img src="../../.gitbook/assets/connectors/vtiger.png" alt="Vtiger logo" width="64">

Vtiger CRM Cloud REST API connector. Generic record operations (create, retrieve, update, revise, delete, query with VTQL) across all CRM modules (Contacts, Leads, Organizations/Accounts, Potentials/Deals, Cases, Products, Services, Quotes, SalesOrder, Invoice, Events, Documents...), module metadata (listtypes, describe, picklist dependency), related-record management, tags, lookup, sync, lead conversion, and file retrieval.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [vtiger.com](https://vtiger.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `vtiger` |

## Use it

Add Vtiger from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.vtiger.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Related Record | `addRelatedRecord` | Establish a relationship between two existing records. Endpoint: POST /add_related. |
| Add Tags | `addTags` | Add one or more tags to a record. Endpoint: POST /tags_add. |
| Convert Lead | `convertLead` | Convert a Lead into Contact / Account (Organization) / Potential (Deal) records. Returns the webservice ids of the created records keyed by module. Endpoint: POST /convertlead. |
| Create Record | `createRecord` | Create a record in any module. Send ALL mandatory field values (use Describe Module to discover them; e.g. Cases require title, description, casestatus, casepriority, contact_id). Works for Contacts, Leads, Accounts (Organizations), Potentials (Deals), Cases, Products, Services, Documents, Events, etc. Endpoint: POST /create. |
| Delete Record | `deleteRecord` | Delete an existing record by webservice id (any module). Endpoint: POST /delete. |
| Delete Related Record | `deleteRelatedRecord` | Break an existing relationship between two records (does not delete the records). Endpoint: POST /delete_related. |
| Delete Tags | `deleteTags` | Remove tag(s) from a record, or delete a tag across all records with delete_all. Endpoint: POST /tags_delete. |
| Describe Module | `describeModule` | Get full metadata of a module: fields (name, label, mandatory, type, picklist values, references), permissions (createable/updateable/deleteable/retrieveable), idPrefix and label fields. Endpoint: GET /describe. |
| Get Account Hierarchy | `getAccountHierarchy` | Get the parent/child hierarchy an Account (Organization) belongs to. Endpoint: GET /get_account_hierarchy. |
| Get Current User | `getMe` | Get the logged-in user profile (id, name, email, role, currency and locale preferences). Useful to obtain the user id (e.g. 19x1) for assigned_user_id fields. |

<details>

<summary>See 14 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Picklist Dependency | `getPicklistDependency` | Get the value dependency mapping between two picklist fields of a module (e.g. Contacts contacttype -&gt; contactstatus). Endpoint: GET /picklist_dependency. |
| List Modules | `listModules` | List all accessible CRM modules (types) with basic metadata (isEntity, label, singular). Endpoint: GET /listtypes. |
| List Related Types | `listRelatedTypes` | Get the modules related to a given module, with relationship labels and allowed actions (add/select). Use the returned names/labels for Add Related Record, Retrieve Related Records and Query Related Records. Endpoint: GET /relatedtypes. |
| Lookup Records | `lookupRecords` | Search records by phone number or email across modules and fields. Endpoint: GET /lookup. |
| Query Records | `queryRecords` | Run a VTQL query (SQL-like) against one module. Supports WHERE with =, &lt;, &gt;, &lt;=, &gt;=, !=, in (...), like 'pattern', ORDER BY, LIMIT (max 100 rows per call; use LIMIT offset, count for paging). Example: SELECT id, lastname FROM Contacts WHERE email like '%@x.com' LIMIT 0, 50;. Endpoint: GET /query. |
| Query Related Records | `queryRelatedRecords` | Fetch related records of a source record matching a VTQL criteria. Endpoint: GET /query_related. |
| Reopen Record | `reopenRecord` | Reopen a closed record (isclosed=1, e.g. a Closed Won/Lost Deal or a closed Case). Returns 400 'Record is already open' if the record is not closed. Endpoint: POST /reopen. |
| Retrieve Files | `retrieveFiles` | Download the base64 content of an attached file/image resource (e.g. a Document attachment or Contact image). Get the resource id from the record's imageattachmentids field. Endpoint: GET /files_retrieve. |
| Retrieve Record | `retrieveRecord` | Retrieve a single record by its webservice id (works across all modules). Endpoint: GET /retrieve. |
| Retrieve Related Records | `retrieveRelatedRecords` | Get records related to a source record via a relationship label. Endpoint: GET /retrieve_related. |
| Retrieve Tags | `retrieveTags` | Fetch the tags applied to a record. Endpoint: GET /tags_retrieve. |
| Revise Record | `reviseRecord` | Partial update of an existing record — only send the id and the fields to change (mandatory fields do NOT need to be re-stated). Closed records cannot be revised (400 'record is closed'); use Reopen Record first. Endpoint: POST /revise. |
| Sync Records | `syncRecords` | Fetch records created/updated/deleted since a UNIX timestamp for incremental sync. Does not work for Users or non-entity modules (Currency, Groups). Endpoint: GET /sync. |
| Update Record | `updateRecord` | Full update of an existing record. IMPORTANT: all mandatory fields of the module must be re-stated in element along with the id, otherwise the call fails. For partial updates use Revise Record instead. Endpoint: POST /update. |

</details>
