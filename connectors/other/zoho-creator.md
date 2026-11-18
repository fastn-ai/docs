---
description: "Zoho Creator is Zoho's low-code application development platform."
hidden: true
---

# Zoho Creator

<img src="../../.gitbook/assets/connectors/lg/zoho-creator.png" alt="Zoho Creator logo">

Zoho Creator is Zoho's low-code application development platform. This connector wraps the Zoho Creator REST API v2.1 (https://www.zohoapis.com/creator/v2.1): Data APIs to fetch, add, update and delete report records; Meta APIs for applications, forms, reports, pages, sections and form fields; File APIs to upload and download file, image, audio, video and signature field content; Bulk APIs for asynchronous large-volume record export; and Publish APIs for records in publicly published forms and reports. All operations are scoped to an account owner name, application link name and form or report link name.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [zoho.com](https://zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `zohoCreator` |

## Use it

Add Zoho Creator from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoCreator.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Published Records | `addPublishedRecords` | Adds records to a publicly published Zoho Creator form using the form's private link. Use this for forms shared outside the application rather than the standard Add Records action. Values cannot be set for add notes, formula, auto number, section, file upload, audio, video, signature and AI prediction fields. |
| Add Records | `addRecords` | Adds one or more records to a form in a Zoho Creator application. A maximum of 200 records can be created per request, and each is subject to the form's validations. Record field keys are the form's own field link names, which vary per application; use the List Form Fields action to discover them. Values cannot be set for add notes, formula, auto number, section, file upload, audio, video, signature and AI prediction fields. |
| Create Bulk Read Job | `createBulkReadJob` | Creates an asynchronous bulk read job that exports a large set of records from a Zoho Creator report without consuming the normal record API limits. Returns a job ID; poll the Get Bulk Read Job Status action until the job completes, then call Download Bulk Read Result to retrieve the exported data. |
| Delete Records | `deleteRecords` | Deletes the records in a Zoho Creator report that match a criteria expression. The criteria is mandatory to prevent accidental mass deletion; pass ID!=0 to delete all matching records. This permanently removes the matching records. |
| Download Bulk Read Result | `downloadBulkReadResult` | Downloads the result of a completed Zoho Creator bulk read job. The response is a ZIP archive containing a single CSV file of the exported report data. Call this only once Get Bulk Read Job Status reports the job as completed. |
| Download File | `downloadFile` | Downloads the file stored in a file upload, image, audio, video or signature field of a single Zoho Creator record. Returns the file content itself rather than a JSON payload. |
| Get Bulk Read Job Status | `getBulkReadJobStatus` | Checks the status of an asynchronous Zoho Creator bulk read job using the job ID returned by Create Bulk Read Job. Poll this action at intervals until the job completes; the response then carries a download URL in its result attribute. |
| Get Published Records | `getPublishedRecords` | Fetches records from a publicly published Zoho Creator report using the report's private link. Use this for reports shared outside the application rather than the standard Get Records action. |
| Get Records | `getRecords` | Fetches the records displayed by a Zoho Creator report, optionally filtered by a criteria expression. Returns the data of the report's visible fields. A maximum of 1000 records can be fetched per request; when more records exist, a record cursor is returned in the response header for fetching the next batch. Targets the production environment. |
| List Applications | `listApplications` | Lists every Zoho Creator application the authenticated user owns or has been shared access to, including each application's link name, display name, time zone and the account owner name required by all other actions in this connector. Targets the production environment. |
| List Form Fields | `listFormFields` | Lists the meta information of every field in a Zoho Creator form, including each field's link name, display name, data type and whether it is mandatory. Use the returned field link names as the keys when setting values in the Add Records and Update Records actions. |
| List Forms | `listForms` | Lists the meta information of every form in a Zoho Creator application, including each form's display name and link name. Use the returned link name as the form link name in the Add Records, List Form Fields and Add Published Records actions. |
| List Pages | `listPages` | Lists the meta information of every page in a Zoho Creator application, including each page's display name and link name. |
| List Reports | `listReports` | Lists the meta information of every report in a Zoho Creator application, including each report's display name and link name. Use the returned link name as the report link name in the record, file and bulk actions. |
| List Sections | `listSections` | Lists the sections configured in a Zoho Creator application together with the forms, reports and pages grouped under each section. Use this to understand how an application's components are organised in its navigation. |
| Update Records | `updateRecords` | Updates the records in a Zoho Creator report that match a criteria expression. The criteria is mandatory to prevent accidental mass updates; pass ID!=0 to update all matching records. A maximum of 200 records are updated per request, and Process Until Limit must be enabled when more than 200 records match. |
| Upload File | `uploadFile` | Uploads a file into a file upload, image, audio, video or signature field of an existing Zoho Creator record. The file is sent as multipart form data under the field name file and must not exceed 50 MB. Binary uploads are not reliably supported through the connector engine; text-based files round-trip correctly. |
