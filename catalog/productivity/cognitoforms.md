---
description: "Cognito Forms is an online form builder. List forms, read form fields, and create, update and delete entries."
hidden: true
---

# Cognito Forms

<img src="../../.gitbook/assets/connectors/lg/cognitoforms.png" alt="Cognito Forms logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [cognitoforms.com](https://cognitoforms.com) |
| **Authentication** | Access token |
| **Slug** | `cognitoforms` |

## Setup

Your customers enter their access token for Cognito Forms when they connect. Nothing else needs setting up.

## Use it

Add Cognito Forms from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cognitoforms.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Entry</td><td><code>createEntry</code></td><td>Creates (submits) a new entry on a form. All inputs other than form/entry ids are sent as the entry's field values (top-level JSON keys by field name, e.g. {"Name":{"First":"Jane","Last":"Doe"},"Email":"a@b.com"}). Use getFormSchema with input=true to see the settable fields. Returns the entry data.</td></tr><tr><td>Delete Entry</td><td><code>deleteEntry</code></td><td>Deletes an entry. No output.</td></tr><tr><td>Get Entry</td><td><code>getEntry</code></td><td>Gets an entry. Fails if the entry does not exist.</td></tr><tr><td>Get Entry Document</td><td><code>getEntryDocument</code></td><td>Generates and returns an entry document from a template. Returns file data, metadata and a temporary link.</td></tr><tr><td>Get File</td><td><code>getFile</code></td><td>Gets a stored file by id. Returns file data, metadata and a temporary link.</td></tr><tr><td>Get Form Fields</td><td><code>getFormFields</code></td><td>Returns the fields of a form (name, path, type, choices).</td></tr><tr><td>Get Form Schema</td><td><code>getFormSchema</code></td><td>Returns the JSON schema of a form's entry. input=true excludes read-only properties (use for create/update); includeLinks adds link properties for files, signatures and documents.</td></tr><tr><td>Get Import Status</td><td><code>getImportStatus</code></td><td>Gets the status and success/failure counts of an import.</td></tr><tr><td>Import Entries</td><td><code>importEntries</code></td><td>Creates, updates or deletes entries from a CSV file. (multipart/form-data). Text (CSV) content only - binary.xlsx cannot be sent by this action. Returns {Id, Status, ErrorMessage}; poll getImportStatus. The optional Email and MatchEntriesUsing parts are not offered: the engine would send them as empty multipart parts when omitted.</td></tr><tr><td>List Forms</td><td><code>listForms</code></td><td>Lists the forms in the organization (archived forms excluded). Returns an array of {Id, Name, InternalName}.</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List View Entries</td><td><code>listViewEntries</code></td><td>Gets all entries of a form view (OData). /Views({viewId})/Entries. $count=true adds the total; $select=Id returns only entry ids.</td></tr><tr><td>Set Form Availability</td><td><code>setFormAvailability</code></td><td>Sets the form's public link availability window. Leave start and end empty to make the form always available. Returns {availabilityStart, availabilityEnd, notAvailableMessage}.</td></tr><tr><td>Update Entry</td><td><code>updateEntry</code></td><td>Updates an existing entry. All inputs other than form/entry ids are sent as the entry's field values (top-level JSON keys by field name, e.g. {"Name":{"First":"Jane","Last":"Doe"},"Email":"a@b.com"}). Use getFormSchema with input=true to see the settable fields. Fails if the entry includes a paid order or does not exist.</td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td>Uploads a file for use in form entries. (multipart/form-data, field File). Text content only - binary files cannot be sent by this action. Returns {Id, Name, ContentType, Size}.</td></tr></tbody></table>

</details>

## Events

Cognito Forms has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
