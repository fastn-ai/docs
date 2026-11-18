---
description: "KoboToolbox is an open-source platform for field data collection."
hidden: true
---

# KoboToolbox

KoboToolbox is an open-source platform for field data collection. This connector covers the KoboToolbox KPI v2 API: projects and forms, form content and versions, deployment, submissions and their validation statuses, exports and export settings, media files, paired data, permission assignments, REST service hooks, organizations and members, project views, tags, imports, usage reporting and account logs.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [kobotoolbox.org](https://kobotoolbox.org) |
| **Authentication** | Credentials you enter |
| **Actions** | 81 |
| **Events** | 1 |
| **Slug** | `kobotoolbox` |

## Use it

Add KoboToolbox from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.kobotoolbox.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Delete Submissions | `bulkDeleteSubmissions` | Permanently removes many submissions from a form in a single request. This cannot be undone. |
| Bulk Set Submission Validation Statuses | `bulkSetSubmissionValidationStatuses` | Sets the same review state on many submissions at once. Target specific records by listing their identifiers, or every record by confirming the all flag. |
| Bulk Update Submissions | `bulkUpdateSubmissions` | Applies the same answer values to many submissions at once, for correcting a field across a set of records. Each updated submission gains a new version in its edit history. |
| Create Asset | `createAsset` | Creates a new project, form, block, question, template or collection. Supply the form definition in the content field, or create an empty draft and fill it in with Update Asset. |
| Create Asset File | `createAssetFile` | Attaches a file to a form by supplying its contents as a base64 data URI, for adding form media or an external choice list that questions reference by filename. |
| Create Asset Snapshot | `createAssetSnapshot` | Creates a preview snapshot of a form's current content and returns an Enketo preview address, letting a form be checked in the browser before it is deployed. |
| Create Asset Subscription | `createAssetSubscription` | Subscribes the account to a public collection so its questions and blocks appear in the form builder library. |
| Create Export | `createExport` | Starts generating a data export of a form's submissions in CSV, XLSX, SPSS or GeoJSON. The export runs in the background, so poll Get Export until its status is complete and then download the result. |
| Create Export Setting | `createExportSetting` | Saves a reusable export configuration on a form and returns stable CSV and XLSX download addresses that always reflect the latest submissions. |
| Create Hook | `createHook` | Registers a REST service on a form so every new submission is posted to an external address. This is how a webhook subscription is created on KoboToolbox. |
| Create Paired Data | `createPairedData` | Pairs another project's submissions into this form as a dynamic data source under a chosen filename. The source project must have data sharing enabled and grant this account access. |
| Create Permission Assignment | `createPermissionAssignment` | Grants one user a single permission on a form, for example letting a colleague view or add submissions. Granting a permission to the AnonymousUser account shares the project publicly. |
| Delete Asset | `deleteAsset` | Permanently removes a project, form, block, question, template or collection and all of its submissions. This cannot be undone. |
| Delete Asset File | `deleteAssetFile` | Removes a file from a form. Questions that reference the file by name will no longer resolve it, so redeploy the form after removing media it depends on. |
| Delete Asset Subscription | `deleteAssetSubscription` | Unsubscribes the account from a public collection so its content no longer appears in the form builder library. |
| Delete Export | `deleteExport` | Removes a generated export and its downloadable file. The submissions themselves are not affected. |
| Delete Export Setting | `deleteExportSetting` | Removes a saved export configuration from a form, which also invalidates its stable download addresses. |
| Delete Hook | `deleteHook` | Removes a REST service from a form so submissions stop being forwarded to its endpoint. This is how a webhook subscription is cancelled on KoboToolbox. |
| Delete Paired Data | `deletePairedData` | Removes a paired-data source from a form so it no longer pulls in the other project's submissions. |
| Delete Permission Assignment | `deletePermissionAssignment` | Revokes one permission assignment on a form, removing that user's access. The owner's own assignment cannot be revoked. |
| Delete Submission | `deleteSubmission` | Permanently removes one submission and its attachments from a form. This cannot be undone. |
| Delete Submission Validation Status | `deleteSubmissionValidationStatus` | Clears the review state of one submission, returning it to the unreviewed state. |
| Deploy Asset | `deployAsset` | Deploys a form for the first time, publishing it so data collectors can submit to it and returning the Enketo web form links. Use Redeploy Asset for subsequent deployments. |
| Duplicate Submission | `duplicateSubmission` | Creates a copy of one submission with a fresh identifier and submission time, useful for repeating a record that differs only slightly from an existing one. |
| Get Asset | `getAsset` | Returns one project, form, block, question, template or collection in full, including its form content, deployment state, sharing links, permissions and the addresses of its sub-resources. |
| Get Asset Deployment | `getAssetDeployment` | Returns the current deployment of a form, including the backend in use, whether it is accepting submissions, the deployed version and the full asset record. |
| Get Asset File | `getAssetFile` | Returns one file attached to a form, with its metadata and the address its contents can be downloaded from. |
| Get Asset Reports | `getAssetReports` | Returns aggregated statistics for each question in a deployed form, giving the answer frequencies and totals used to build the project's report charts. |
| Get Asset Snapshot | `getAssetSnapshot` | Returns one form preview snapshot, with its render status, any validation warnings and the Enketo preview address. |
| Get Asset Valid Content | `getAssetValidContent` | Returns the validated, normalised form definition of an asset, with the schema version applied and invalid rows removed. Use it to read the form structure the server actually recognises. |
| Get Asset Version | `getAssetVersion` | Returns one saved version of a form, including the full form content as it stood at that point, for comparing or restoring an earlier definition. |
| Get Current User | `getCurrentUser` | Returns the account the API token belongs to, including username, email, organization, server time and account extra details. Use it to confirm a connection works and to discover the username other endpoints need. |
| Get Environment | `getEnvironment` | Returns the server's public configuration, including the interface languages, sector and country choice lists, submission and storage limits and support links. Useful for populating pickers with the values this server accepts. |
| Get Export | `getExport` | Returns one export by identifier. Poll it after starting an export until the status reaches complete, then download the file from the result address. |
| Get Export Setting | `getExportSetting` | Returns one saved export configuration, including its stored options and its stable CSV and XLSX download addresses. |
| Get Hook | `getHook` | Returns one REST service on a form, including its endpoint, delivery format and its running success, failure and pending counts. |
| Get Import | `getImport` | Returns one XLSForm import job. Poll it after starting an import until the status reaches complete, then read the created asset identifier from the messages. |
| Get Organization | `getOrganization` | Returns one organization by identifier, with its name, type, website, the calling account's role in it and the addresses of its member, project and usage endpoints. |
| Get Service Usage | `getServiceUsage` | Returns the account's usage against its plan limits: submission counts, file storage and speech-to-text and translation consumption for the current billing period and all time. |
| Get Submission | `getSubmission` | Returns one submission by its numeric identifier, with the answers keyed by question name alongside the submission metadata. |
| Get Submission Attachment | `getSubmissionAttachment` | Returns the media file attached to one submission at a given question, identified by its XPath in the form. The xpath parameter is required. |
| Get Submission Edit Link | `getSubmissionEditLink` | Returns a single-use Enketo web address for editing one submission in the browser, so a reviewer can correct answers in the original form. |
| Get Submission Validation Status | `getSubmissionValidationStatus` | Returns the review state of one submission, showing which reviewer set it and when. An empty object means no review state has been assigned yet. |
| Get Submission View Link | `getSubmissionViewLink` | Returns a read-only Enketo web address for viewing one submission rendered in its original form layout. |
| Get User | `getUser` | Returns the public profile of a KoboToolbox user by username, including their public collections and the date they joined. Use it to resolve the user address needed when granting permissions. |
| List Access Logs | `listAccessLogs` | Returns the sign-in history for every account on the server. Only a superuser may read it; other accounts receive a permission error. |
| List Asset Files | `listAssetFiles` | Returns the files attached to a form, such as the media and external choice lists that questions reference by filename. |
| List Asset Subscriptions | `listAssetSubscriptions` | Returns the public collections the account has subscribed to, which make their questions and blocks available in the form builder library. |
| List Asset Usage | `listAssetUsage` | Returns usage broken down per project, showing each project's submission count, attachment storage and language-processing consumption. |
| List Asset Versions | `listAssetVersions` | Returns the saved versions of a form's content, showing when each was created and which ones have been deployed. |
| List Assets | `listAssets` | Returns the projects, forms, blocks, questions, templates and collections the account can access, with paging. Use the search query to filter and the ordering parameter to sort. |
| List Audit Logs | `listAuditLogs` | Returns the server-wide audit trail of account and project activity. Only a superuser may read it; other accounts receive a permission error. |
| List Export Settings | `listExportSettings` | Returns the saved export configurations on a form. Each one stores a reusable set of export options and exposes ready-made download addresses in every supported format. |
| List Exports | `listExports` | Returns the data exports generated for a form, each with its status and, once complete, the address the file can be downloaded from. |
| List Hook Logs | `listHookLogs` | Returns the delivery log of a REST service, showing each attempt to forward a submission with its status code, message and retry count. Use it to diagnose failing webhook deliveries. |
| List Hooks | `listHooks` | Returns the REST services registered on a form. Each hook forwards every new submission to an external address, and this is the list to check when confirming a webhook registration. |
| List Imports | `listImports` | Returns the XLSForm import jobs the account has started, each with its processing status and the asset it produced. |
| List Languages | `listLanguages` | Returns the languages KoboToolbox recognises for form translations and for transcription and machine translation, with their codes and supported services. |
| List My Access Logs | `listMyAccessLogs` | Returns the sign-in history of the account the token belongs to, with the time, source address and authentication method of each session. |
| List Organization Assets | `listOrganizationAssets` | Returns the projects owned by an organization, giving an administrator a view across the whole organization rather than only their own projects. |
| List Organization Invites | `listOrganizationInvites` | Returns the outstanding invitations to join an organization, each with the invited address, the offered role and the invitation's current status. |
| List Organization Members | `listOrganizationMembers` | Returns the members of an organization with their role, contact details and when they joined. |
| List Organizations | `listOrganizations` | Returns the organizations the account belongs to, with the organization identifier the member, asset and usage endpoints need. |
| List Paired Data | `listPairedData` | Returns the paired-data sources attached to a form. Pairing lets a project pull another project's submissions in as a dynamic data source. |
| List Permission Assignments | `listPermissionAssignments` | Returns who can do what on a form, listing each user and the permission granted. Sharing with the anonymous user makes a project publicly accessible. |
| List Permissions | `listPermissions` | Returns every permission KoboToolbox supports, with the codename and API address needed when granting access to a form. |
| List Project History Logs | `listProjectHistoryLogs` | Returns the audit trail of changes made to the organization's projects, recording who changed what and when. Reading it requires organization administrator rights. |
| List Project Ownership Invites | `listProjectOwnershipInvites` | Returns the pending project ownership transfers involving the account, each listing the projects offered and the transfer's current status. |
| List Project Views | `listProjectViews` | Returns the project views the account can use. A project view gives an administrator a curated cross-organization window onto a set of projects and their data. |
| List Submissions | `listSubmissions` | Returns the submissions collected by a deployed form. Each row carries the answers keyed by question name alongside submission metadata. Use query to filter with MongoDB syntax, fields to select columns and sort to order the results. |
| List Tags | `listTags` | Returns the tags used across the account's projects, for building tag filters or offering existing tags when labelling a project. |
| List Terms Of Service | `listTermsOfService` | Returns the terms of service documents published on the server, with their text and the date each was last changed. |
| List Transcription Services | `listTranscriptionServices` | Returns the speech-to-text providers available for transcribing audio answers, with the codes used when requesting a transcription. |
| List Translation Services | `listTranslationServices` | Returns the machine-translation providers available for translating transcripts and text answers, with the codes used when requesting a translation. |
| List User Reports | `listUserReports` | Returns the abuse and misuse reports raised about accounts on the server. Reading it requires server administrator rights. |
| Redeploy Asset | `redeployAsset` | Redeploys an already-deployed form so that content changes reach data collectors, and switches a deployment between accepting submissions and archived. Set active to false to archive the project. |
| Replace Permission Assignments | `replacePermissionAssignments` | Replaces every permission assignment on a form in one request. Any assignment not present in the list is revoked, so send the complete intended set. |
| Retry Hook Deliveries | `retryHookDeliveries` | Queues every failed delivery of a REST service to be attempted again, for recovering submissions that were missed while the endpoint was unavailable. |
| Set Submission Validation Status | `setSubmissionValidationStatus` | Sets the review state of one submission, marking it approved, not approved or on hold so reviewers can track which records have been checked. |
| Update Asset | `updateAsset` | Partially updates a project, form or collection. Only the fields supplied are changed, so a form's questions can be replaced without touching its name or settings. Redeploy the form afterwards for content changes to reach data collectors. |
| Update Hook | `updateHook` | Partially updates a REST service on a form. Only the fields supplied are changed, so a hook can be paused by setting active to false without disturbing its endpoint or settings. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| New Submission | `submission` | Fires when a deployed KoboToolbox form receives a new submission. Registration creates a REST Service on the chosen form, and KoboToolbox then posts each submission to the fastn trigger address. The payload is the submission record itself: the answers keyed by question name alongside the submission metadata. Note that KoboToolbox REST Services offer only this one event; submission edits and deletions are not delivered. |
