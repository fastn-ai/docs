---
description: "Cognito Forms is a free online form builder for collecting submissions, managing entries, and generating documents."
---

# Cognito Forms

Cognito Forms is a free online form builder for collecting submissions, managing entries, and generating documents. This connector covers the REST API: listing forms, reading a form's field schema, creating/reading/updating/deleting entries (submissions), and retrieving generated entry documents (PDFs).

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [cognitoforms.com](https://cognitoforms.com) |
| **Authentication** | Bearer token |
| **Actions** | 14 |
| **Events** | 0 |
| **Slug** | `cognitoforms` |

## Use it

Add Cognito Forms from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cognitoforms.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Entry | `createEntry` | Creates (submits) a new entry on a form. POST /api/forms/{form}/entries. All inputs other than form/entry ids are sent as the entry's field values (top-level JSON keys by field name, e.g. {"Name":{"First":"Jane","Last":"Doe"},"Email":"a@b.com"}). Use getFormSchema with input=true to see the settable fields. Returns the entry data. |
| Delete Entry | `deleteEntry` | Deletes an entry. DELETE /api/forms/{form}/entries/{entryId}. No output. |
| Get Entry | `getEntry` | Gets an entry. GET /api/forms/{form}/entries/{entryId}. Fails if the entry does not exist. |
| Get Entry Document | `getEntryDocument` | Generates and returns an entry document from a template. GET /api/forms/{form}/entries/{entry}/documents/{templateNumber}. Returns file data, metadata and a temporary link. |
| Get File | `getFile` | Gets a stored file by id. GET /api/files/{id}. Returns file data, metadata and a temporary link. |
| Get Form Fields | `getFormFields` | Returns the fields of a form (name, path, type, choices). GET /api/forms/{form}/fields. |
| Get Form Schema | `getFormSchema` | Returns the JSON schema of a form's entry. GET /api/forms/{form}/schema. input=true excludes read-only properties (use for create/update); includeLinks adds link properties for files, signatures and documents. |
| Get Import Status | `getImportStatus` | Gets the status and success/failure counts of an import. GET /api/forms/{form}/import-status/{importId}. |
| Import Entries | `importEntries` | Creates, updates or deletes entries from a CSV file. POST /api/forms/{form}/import-entries (multipart/form-data). Text (CSV) content only - binary .xlsx cannot be sent by this action. Returns {Id, Status, ErrorMessage}; poll getImportStatus. The optional Email and MatchEntriesUsing parts are not offered: the engine would send them as empty multipart parts when omitted. |
| List Forms | `listForms` | Lists the forms in the organization (archived forms excluded). GET /api/forms. Returns an array of {Id, Name, InternalName}. |
| List View Entries | `listViewEntries` | Gets all entries of a form view (OData). GET /api/odata/Forms({form})/Views({viewId})/Entries. $count=true adds the total; $select=Id returns only entry ids. |
| Set Form Availability | `setFormAvailability` | Sets the form's public link availability window. POST /api/forms/{form}/public-link-availability. Leave start and end empty to make the form always available. Returns {availabilityStart, availabilityEnd, notAvailableMessage}. |
| Update Entry | `updateEntry` | Updates an existing entry. PATCH /api/forms/{form}/entries/{entryId}. All inputs other than form/entry ids are sent as the entry's field values (top-level JSON keys by field name, e.g. {"Name":{"First":"Jane","Last":"Doe"},"Email":"a@b.com"}). Use getFormSchema with input=true to see the settable fields. Fails if the entry includes a paid order or does not exist. |
| Upload File | `uploadFile` | Uploads a file for use in form entries. POST /api/files (multipart/form-data, field File). Text content only - binary files cannot be sent by this action. Returns {Id, Name, ContentType, Size}. |
