---
description: "Zoho Creator is a low-code app builder. Add, read, update and delete records, and list applications and forms."
hidden: true
---

# Zoho Creator

<img src="../../.gitbook/assets/connectors/lg/zoho-creator.png" alt="Zoho Creator logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [zoho.com](https://zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `zohoCreator` |

## Setup

Your customers sign in to Zoho Creator through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Zoho Creator from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Zoho Creator**.
2. Select **Connect** on the Zoho Creator card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Zoho Creator and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Zoho Creator's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Published Records</td><td><code>addPublishedRecords</code></td><td>Adds records to a publicly published Zoho Creator form using the form's private link. Use this for forms shared outside the application rather than the standard Add Records action. Values cannot be set for add notes, formula, auto number, section, file upload, audio, video, signature and AI prediction fields.</td></tr><tr><td>Add Records</td><td><code>addRecords</code></td><td>Adds one or more records to a form in a Zoho Creator application. A maximum of 200 records can be created per request, and each is subject to the form's validations. Record field keys are the form's own field link names, which vary per application; use the List Form Fields action to discover them. Values cannot be set for add notes, formula, auto number, section, file upload, audio, video, signature and AI prediction fields.</td></tr><tr><td>Create Bulk Read Job</td><td><code>createBulkReadJob</code></td><td>Creates an asynchronous bulk read job that exports a large set of records from a Zoho Creator report without consuming the normal record API limits. Returns a job ID; poll the Get Bulk Read Job Status action until the job completes, then call Download Bulk Read Result to retrieve the exported data.</td></tr><tr><td>Delete Records</td><td><code>deleteRecords</code></td><td>Deletes the records in a Zoho Creator report that match a criteria expression. The criteria is mandatory to prevent accidental mass deletion; pass ID!=0 to delete all matching records. This permanently removes the matching records.</td></tr><tr><td>Download Bulk Read Result</td><td><code>downloadBulkReadResult</code></td><td>Downloads the result of a completed Zoho Creator bulk read job. The response is a ZIP archive containing a single CSV file of the exported report data. Call this only once Get Bulk Read Job Status reports the job as completed.</td></tr><tr><td>Download File</td><td><code>downloadFile</code></td><td>Downloads the file stored in a file upload, image, audio, video or signature field of a single Zoho Creator record. Returns the file content itself rather than a JSON payload.</td></tr><tr><td>Get Bulk Read Job Status</td><td><code>getBulkReadJobStatus</code></td><td>Checks the status of an asynchronous Zoho Creator bulk read job using the job ID returned by Create Bulk Read Job. Poll this action at intervals until the job completes; the response then carries a download URL in its result attribute.</td></tr><tr><td>Get Published Records</td><td><code>getPublishedRecords</code></td><td>Fetches records from a publicly published Zoho Creator report using the report's private link. Use this for reports shared outside the application rather than the standard Get Records action.</td></tr><tr><td>Get Records</td><td><code>getRecords</code></td><td>Fetches the records displayed by a Zoho Creator report, optionally filtered by a criteria expression. Returns the data of the report's visible fields. A maximum of 1000 records can be fetched per request; when more records exist, a record cursor is returned in the response header for fetching the next batch. Targets the production environment.</td></tr><tr><td>List Applications</td><td><code>listApplications</code></td><td>Lists every Zoho Creator application the authenticated user owns or has been shared access to, including each application's link name, display name, time zone and the account owner name required by all other actions in this connector. Targets the production environment.</td></tr></tbody></table>

<details>

<summary>View 7 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Form Fields</td><td><code>listFormFields</code></td><td>Lists the meta information of every field in a Zoho Creator form, including each field's link name, display name, data type and whether it is mandatory. Use the returned field link names as the keys when setting values in the Add Records and Update Records actions.</td></tr><tr><td>List Forms</td><td><code>listForms</code></td><td>Lists the meta information of every form in a Zoho Creator application, including each form's display name and link name. Use the returned link name as the form link name in the Add Records, List Form Fields and Add Published Records actions.</td></tr><tr><td>List Pages</td><td><code>listPages</code></td><td>Lists the meta information of every page in a Zoho Creator application, including each page's display name and link name.</td></tr><tr><td>List Reports</td><td><code>listReports</code></td><td>Lists the meta information of every report in a Zoho Creator application, including each report's display name and link name. Use the returned link name as the report link name in the record, file and bulk actions.</td></tr><tr><td>List Sections</td><td><code>listSections</code></td><td>Lists the sections configured in a Zoho Creator application together with the forms, reports and pages grouped under each section. Use this to understand how an application's components are organised in its navigation.</td></tr><tr><td>Update Records</td><td><code>updateRecords</code></td><td>Updates the records in a Zoho Creator report that match a criteria expression. The criteria is mandatory to prevent accidental mass updates; pass ID!=0 to update all matching records. A maximum of 200 records are updated per request, and Process Until Limit must be enabled when more than 200 records match.</td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td>Uploads a file into a file upload, image, audio, video or signature field of an existing Zoho Creator record. The file is sent as multipart form data under the field name file and must not exceed 50 MB. Binary uploads are not reliably supported through the connector engine; text-based files round-trip correctly.</td></tr></tbody></table>

</details>

