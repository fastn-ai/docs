---
description: "Vtiger is a CRM platform. Create, read, update, delete and query records in any module, convert leads and manage tags."
hidden: true
---

# Vtiger

<img src="../../.gitbook/assets/connectors/lg/vtiger.png" alt="Vtiger logo">

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [vtiger.com](https://vtiger.com) |
| **Authentication** | Username and access key |
| **Slug** | `vtiger` |

## Setup

Your customers enter their username and access key for Vtiger when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Vtiger from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Vtiger**.
2. Select **Connect** on the Vtiger card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Vtiger's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Related Record</td><td><code>addRelatedRecord</code></td><td>Establish a relationship between two existing records. Endpoint</td></tr><tr><td>Add Tags</td><td><code>addTags</code></td><td>Add one or more tags to a record. Endpoint</td></tr><tr><td>Convert Lead</td><td><code>convertLead</code></td><td>Convert a Lead into Contact / Account (Organization) / Potential (Deal) records. Returns the webservice ids of the created records keyed by module. Endpoint</td></tr><tr><td>Create Record</td><td><code>createRecord</code></td><td>Create a record in any module. Send ALL mandatory field values (use Describe Module to discover them; e.g. Cases require title, description, casestatus, casepriority, contact_id). Works for Contacts, Leads, Accounts (Organizations), Potentials (Deals), Cases, Products, Services, Documents, Events, etc. Endpoint</td></tr><tr><td>Delete Record</td><td><code>deleteRecord</code></td><td>Delete an existing record by webservice id (any module). Endpoint</td></tr><tr><td>Delete Related Record</td><td><code>deleteRelatedRecord</code></td><td>Break an existing relationship between two records (does not delete the records). Endpoint</td></tr><tr><td>Delete Tags</td><td><code>deleteTags</code></td><td>Remove tag(s) from a record, or delete a tag across all records with delete_all. Endpoint</td></tr><tr><td>Describe Module</td><td><code>describeModule</code></td><td>Get full metadata of a module: fields (name, label, mandatory, type, picklist values, references), permissions (createable/updateable/deleteable/retrieveable), idPrefix and label fields. Endpoint</td></tr><tr><td>Get Account Hierarchy</td><td><code>getAccountHierarchy</code></td><td>Get the parent/child hierarchy an Account (Organization) belongs to. Endpoint</td></tr><tr><td>Get Current User</td><td><code>getMe</code></td><td>Get the logged-in user profile (id, name, email, role, currency and locale preferences). Useful to obtain the user id (e.g. 19x1) for assigned_user_id fields.</td></tr></tbody></table>

<details>

<summary>View 14 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Picklist Dependency</td><td><code>getPicklistDependency</code></td><td>Get the value dependency mapping between two picklist fields of a module (e.g. Contacts contacttype -&gt; contactstatus). Endpoint</td></tr><tr><td>List Modules</td><td><code>listModules</code></td><td>List all accessible CRM modules (types) with basic metadata (isEntity, label, singular). Endpoint</td></tr><tr><td>List Related Types</td><td><code>listRelatedTypes</code></td><td>Get the modules related to a given module, with relationship labels and allowed actions (add/select). Use the returned names/labels for Add Related Record, Retrieve Related Records and Query Related Records. Endpoint</td></tr><tr><td>Lookup Records</td><td><code>lookupRecords</code></td><td>Search records by phone number or email across modules and fields. Endpoint</td></tr><tr><td>Query Records</td><td><code>queryRecords</code></td><td>Run a VTQL query (SQL-like) against one module. Supports WHERE with =, &lt;, &gt;, &lt;=, &gt;=, !=, in (...), like 'pattern', ORDER BY, LIMIT (max 100 rows per call; use LIMIT offset, count for paging). Example: SELECT id, lastname FROM Contacts WHERE email like '%@x.com' LIMIT 0, 50;. Endpoint</td></tr><tr><td>Query Related Records</td><td><code>queryRelatedRecords</code></td><td>Fetch related records of a source record matching a VTQL criteria. Endpoint</td></tr><tr><td>Reopen Record</td><td><code>reopenRecord</code></td><td>Reopen a closed record (isclosed=1, e.g. a Closed Won/Lost Deal or a closed Case). Endpoint</td></tr><tr><td>Retrieve Files</td><td><code>retrieveFiles</code></td><td>Download the base64 content of an attached file/image resource (e.g. a Document attachment or Contact image). Get the resource id from the record's imageattachmentids field. Endpoint</td></tr><tr><td>Retrieve Record</td><td><code>retrieveRecord</code></td><td>Retrieve a single record by its webservice id (works across all modules). Endpoint</td></tr><tr><td>Retrieve Related Records</td><td><code>retrieveRelatedRecords</code></td><td>Get records related to a source record via a relationship label. Endpoint</td></tr><tr><td>Retrieve Tags</td><td><code>retrieveTags</code></td><td>Fetch the tags applied to a record. Endpoint</td></tr><tr><td>Revise Record</td><td><code>reviseRecord</code></td><td>Partial update of an existing record — only send the id and the fields to change (mandatory fields do NOT need to be re-stated). Closed records cannot be revised (400 'record is closed'); use Reopen Record first. Endpoint</td></tr><tr><td>Sync Records</td><td><code>syncRecords</code></td><td>Fetch records created/updated/deleted since a UNIX timestamp for incremental sync. Does not work for Users or non-entity modules (Currency, Groups). Endpoint</td></tr><tr><td>Update Record</td><td><code>updateRecord</code></td><td>Full update of an existing record. IMPORTANT: all mandatory fields of the module must be re-stated in element along with the id, otherwise the call fails. For partial updates use Revise Record instead. Endpoint</td></tr></tbody></table>

</details>

