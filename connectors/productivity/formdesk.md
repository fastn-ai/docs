---
description: "Formdesk online forms platform."
hidden: true
---

# Formdesk

Formdesk online forms platform. Manage forms, form entries (results), uploaded files, Formdesk user accounts and form visitors through the Formdesk REST API v1. Formdesk uses a two-step host discovery: GET /connect on www.formdesk.com returns the regional host (e.g. fd7.formdesk.com) that all other calls must use, so the host is supplied as a connection field.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [formdesk.com](https://formdesk.com) |
| **Authentication** | API key |
| **Slug** | `formdesk` |

## Use it

Add Formdesk from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.formdesk.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Form Entry | `addFormEntries` | Adds one result entry to a form. Supply the entry's answers as top-level properties whose names are the form's item Identifiers (see List Form Items); a file upload item takes an object {filename, content} with base64 content. Set process_messages to true to have Formdesk send the form's email and SMS messages for the new entry, which delivers real messages to real people. Costs 1 Formdesk API credit. |
| Add User | `addUser` | Creates a new Formdesk user account. Requires Supervisor rights. Use type 'internal' for a user with Formdesk credentials, 'external' for an OpenID Connect user (only type, external_userid and external_provider are required; other fields are filled from the claims on first login) or 'api' for a dedicated API user, for which Formdesk generates an API Key when apikey is omitted. Costs 1 Formdesk API credit. |
| Add Visitor | `addVisitor` | Creates a new form visitor. Requires Supervisor rights. For an OpenID Connect visitor only type='external', external_userid and external_provider are required. When password is omitted for an internal visitor Formdesk generates a random 10-character password. Costs 1 Formdesk API credit. |
| Delete All Form Files | `deleteAllFormFiles` | DESTRUCTIVE: permanently removes every file uploaded with any result entry of the given form, across all of that form's entries. The entries are kept; the files cannot be recovered. List All Form Files first to see what would be lost. |
| Delete Form Entry Files | `deleteFormEntryFiles` | Permanently removes every file uploaded with one form result entry, identified by entry id. The entry itself is kept; the files cannot be recovered. |
| Export Form Results | `exportFormResults` | Exports the result entries of a form to a file in Excel, XML, text or CSV format and returns the download. The same query filters as List Form Entry IDs apply. Entries already flagged with Set Entry To Processed are excluded. COST: this call consumes one Formdesk credit per completed form in the download, not one per call. |
| Get API Key From Credentials | `connectWithCredentials` | SECURITY WARNING: this endpoint exchanges a Formdesk username and password for the account's API Key and returns that key in clear text. Do not log, store or forward the response. Use it only to bootstrap a connection when the API Key is not yet known. Free of charge (costs no Formdesk credits). |
| Get Connect Host | `getConnectHost` | SECURITY WARNING: the response of this endpoint contains the account's own Formdesk API Key in clear text. Do not log, store or forward the response. Determines which Formdesk server hosts the account: always call it on www.formdesk.com and use the returned host for every other call. Free of charge (costs no Formdesk credits). |
| Get File | `getFile` | Returns the details (filename, size, location and metadata) of a single stored file by file id. Use Get File Content to download the bytes. Costs 1 Formdesk API credit. |
| Get File Content | `getFileContent` | Downloads the raw binary content of a stored file by file id. The bytes can be written straight to disk without conversion. Obtain the file id from List Files or from a form result. Costs 1 Formdesk API credit. |

<details>

<summary>See 29 more actions</summary>

* **Get Form Entry** `getFormEntry`: Returns all answers and Formdesk system variables of one form result entry by entry id. System variables include _fd_id, _fd_seqno, _fd_source, _fd_status, _fd_add, _fd_edit, _fd_compl and _fd_deleted. Deleted entries are still returned for 30 days, but their uploaded files are gone. Costs 1 Formdesk API credit.
* **Get Form Entry PDF** `getFormEntryPdf`: Generates a PDF copy of a completed form for one result entry and returns it as binary data; the filename is in the Content-Disposition header. Content options control which questions appear, PDF options control paper size, orientation, scaling, margins and password protection. Costs 1 Formdesk API credit.
* **Get User** `getUser`: SECURITY WARNING: if the user is of type 'api' the response includes that user's Formdesk API Key in clear text. Do not log, store or forward it. Returns all properties of a single Formdesk user by numeric user id. Costs 1 Formdesk API credit.
* **Get User By External ID** `getUserByExternalId`: SECURITY WARNING: if the user is of type 'api' the response includes that user's Formdesk API Key in clear text. Returns all properties of a Formdesk user looked up by the external (OpenID Connect) user id instead of the numeric Formdesk id. Costs 1 Formdesk API credit.
* **Get Visitor** `getVisitor`: Returns all properties of a single form visitor by numeric visitor id. Note the response may include the visitor's password when it was not chosen by the visitor themselves. Costs 1 Formdesk API credit.
* **Get Visitor By External ID** `getVisitorByExternalId`: Returns all properties of a form visitor looked up by their external (OpenID Connect) user id instead of the numeric Formdesk visitor id. Costs 1 Formdesk API credit.
* **Increment Form Entry Field** `incrementFormEntryField`: Increments a numeric field of one form result entry by the given amount. Formdesk locks the record during the operation so the resulting value stays unique, which makes this the safe way to allocate sequence or ticket numbers. Costs 1 Formdesk API credit.
* **List All Form Files** `listAllFormFiles`: Lists every file uploaded with any result entry of one form, across all of that form's entries. Costs 1 Formdesk API credit.
* **List Files** `listFiles`: Lists the files stored in the Formdesk account: files attached to form result entries and files uploaded in the account such as images used on forms or attachments on emails. Costs 1 Formdesk API credit.
* **List Form Entry Files** `listFormEntryFiles`: Lists the files uploaded with one form result entry, identified by entry id. Use Get File Content with a returned file id to download the bytes. Costs 1 Formdesk API credit.
* **List Form Entry IDs** `listFormEntryIds`: Lists the entry ids of the result entries of one form, narrowed by a pre-set filter, a search string, an id or date range, a visitor or a status. Entries already flagged with Set Entry To Processed are not returned. When no status is given only entries with status DONE are returned. Costs 1 Formdesk API credit.
* **List Form Entry Workflows** `listFormEntryWorkflows`: Lists the workflow steps recorded against one form result entry, showing how far the entry has progressed through the form's workflow. Available to Supervisors. Costs 1 Formdesk API credit.
* **List Form Filter Names** `listFormFilterNames`: Lists the names of the pre-set filters defined for a form. Only the names are returned, not the filter definitions; a name can be passed as the 'view' query parameter when listing or exporting form results. Costs 1 Formdesk API credit.
* **List Form Items** `listFormItems`: Lists every item (question) on a form that requires input and has an Identifier, with its type: text, textarea, radiogroup, checkboxgroup, listbox, checkbox, userlist or file. Use it to discover the field identifiers needed to add or update form results. Costs 1 Formdesk API credit.
* **List Forms** `listForms`: Returns every form in the Formdesk account (folder of forms), with each form's identifier, name and metadata. Costs 1 Formdesk API credit.
* **List Users** `listUsers`: SECURITY WARNING: for every user of type 'api' the response includes that user's Formdesk API Key in clear text, so this response contains live credentials for the whole account. Do not log, store or forward it. Lists all Formdesk user accounts with their id, uuid, type, email, username and permission flags. Costs 1 Formdesk API credit.
* **List Visitor Form Entries** `listVisitorFormEntries`: Lists the entry ids of every login form entry belonging to one form visitor, identified by numeric visitor id. Costs 1 Formdesk API credit.
* **List Visitors** `listVisitors`: Lists all Formdesk visitor accounts. Visitors are people who log in to a form; the form setting 'Visitor must be able to manage own form entries' must be enabled. Costs 1 Formdesk API credit.
* **Park Form Data** `parkFormData`: Parks prefill data in Formdesk and returns a 32-character parking ticket. Pass the ticket to a form as ?ticket=... and Formdesk prefills the form with the parked values, so data never has to travel in the form URL. Costs 1 Formdesk API credit.
* **Remove File** `removeFile`: Permanently removes a stored file by file id. A file attached to a form result entry is lost and cannot be retrieved afterwards.
* **Remove Form Entry** `removeFormEntry`: Removes one result entry of a form by entry id. The entry remains retrievable through Get Form Entry for 30 days with _fd_deleted set, but any files uploaded with it are permanently lost. Costs 1 Formdesk API credit.
* **Remove User** `removeUser`: Permanently removes a Formdesk user account by numeric user id. Requires Supervisor rights and cannot be undone. WARNING: removing the user that owns the API Key this connection authenticates with will lock the connection out of the account.
* **Remove Visitor** `removeVisitor`: Permanently removes a form visitor by numeric visitor id. Requires Supervisor rights and cannot be undone.
* **Set Form Entry To Processed** `setFormEntryProcessed`: Sets the synchronisation status of one form result entry to Processed (P). Processed entries are skipped by List Form Entry IDs and Export Form Results, which is how a synchronisation job marks entries it has already pulled. Costs 1 Formdesk API credit.
* **Single Sign-On User** `singleSignOnUser`: SECURITY WARNING: returns a single sign-on URL that grants access to the Formdesk account without a password. Treat the response as a credential. Signs an internal Formdesk user on without them entering a username and password. Identify the user by username, email or id; supplying password is optional but is validated when present. Requires Supervisor rights. Costs 1 Formdesk API credit.
* **Single Sign-On Visitor** `singleSignOnVisitor`: SECURITY WARNING: returns a single sign-on URL that opens the form as the given visitor without a password. Treat the response as a credential. Signs a visitor on to a specific login form without them entering a username and password. Identify the visitor by username, email or id; password is optional and validated when supplied. Costs 1 Formdesk API credit.
* **Update Form Entry** `updateFormEntry`: Updates the answers of one form result entry by entry id. Supply the answers to change as top-level properties whose names are the form's item Identifiers; a file upload item takes an object {filename, content} with base64 content. Set process_messages to true to have Formdesk send the form's email and SMS messages after the update, which delivers real messages to real people. Costs 1 Formdesk API credit.
* **Update User** `updateUser`: Updates properties of an existing Formdesk user by numeric user id. Requires Supervisor rights. Only the properties supplied are changed. Costs 1 Formdesk API credit.
* **Update Visitor** `updateVisitor`: Updates properties of an existing form visitor by numeric visitor id. Requires Supervisor rights. Only the properties supplied are changed. Costs 1 Formdesk API credit.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Form Entry Submitted | `form.entry.submitted` | Fires when a visitor completes and submits a Formdesk form. REGISTRATION IS MANUAL - the Formdesk REST API v1 has no webhook CRUD endpoint, so the subscription must be created once in the Formdesk web application. Click path: log in to https://www.formdesk.com/&lt;your domain&gt;/ , open the form, choose Edit form, open the Webhooks section (under the form's integration/notification settings), click Add webhook, set Method to POST and URL to the fastn trigger URL shown above, optionally set Sending criteria so the webhook only fires for matching submissions, then save and publish the form. In the webhook's request body add a literal field named 'event' with the value 'form.entry.submitted' (this connector routes on that field) and a field named '_fd_id' mapped to the Formdesk entry id, then add any form item identifiers you want delivered. Formdesk lets you compose the body yourself, so the payload schema below is the recommended shape, not a fixed vendor contract. Formdesk supports GET, POST, PUT, PATCH and DELETE over HTTPS and can store the receiving system's response back into a form field. |
