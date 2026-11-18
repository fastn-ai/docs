---
description: "1CRM all-in-one CRM and ERP via the 1CRM REST API."
hidden: true
---

# 1CRM

<img src="../../.gitbook/assets/connectors/lg/one-crm.png" alt="1CRM logo">

1CRM all-in-one CRM and ERP via the 1CRM REST API. Work with any 1CRM module (accounts, contacts, leads, opportunities, cases, quotes, invoices, projects and more) through generic record, relationship, search and metadata endpoints, plus calendars, files, reports, dashboards, audit logs and webhooks.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [1crm.com](https://1crm.com) |
| **Authentication** | Basic auth |
| **Slug** | `oneCrm` |

## Use it

Add 1CRM from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.oneCrm.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add dashlet to dashboard | `addDashlet` | Add a dashlet of a given class to a dashboard. |
| Add or remove record from favorites | `toggleFavorite` | Toggle a record in the current user's favorites. |
| Add recently viewed item | `addRecentItem` | Add an entry to the current user's recently viewed items. |
| Add related records | `addRelatedRecords` | Link related records to a record via a link, by id list (records) or with join-table data (records_with_data). |
| Assign case to current user | `assignCaseToCurrentUser` | Assign the next available case to the current user (MyCases dashlet behaviour). |
| Authorization grant for contact | `grantContactAccessToken` | OAuth 2.0 token endpoint for portal contacts (client credentials, password, authorization code, refresh token or MFA grants). |
| Authorization grant for user | `grantUserAccessToken` | OAuth 2.0 token endpoint for users (client credentials, password, authorization code, refresh token or MFA grants). |
| Authorization request for contact | `authorizeContact` | OAuth 2.0 authorization request for a portal contact. |
| Authorization request for user | `authorizeUser` | OAuth 2.0 authorization request for a 1CRM user. |
| Authorize card in Stripe | `authorizeStripeCard` | Authorize a credit card with Stripe for an account (payment processing). |

<details>

<summary>See 131 more actions</summary>

* **Charge credit card** `chargeCreditCard`: Charge a credit card through the configured payment gateway (moves money).
* **Create ListView layout** `createListViewLayout`: Create a new ListView layout for a module.
* **Create PDF for signing** `createPdfForSigning`: Create PDF documents for records and prepare them for e-signing (may send signing requests).
* **Create portal access token** `createPortalAccessToken`: Create an access token for portal access on behalf of a contact (admin only; not available with Basic authentication).
* **Create record** `createRecord`: Create a record of the specified model.
* **Create supported products** `createSupportedProducts`: Create supported product records for an initiator record.
* **Create theme preset** `createThemePreset`: Create a new theme preset for the application.
* **Create user access token with password** `createUserAccessTokenWithPassword`: Create an access token for a user from username and password; supports multi-factor authentication.
* **Create webhook** `createWebhook`: Create a webhook that calls a URL when records of a model are created and/or updated.
* **Delete dashboard** `deleteDashboard`: Delete a dashboard by id.
* **Delete dashlet** `deleteDashlet`: Remove a dashlet from a dashboard.
* **Delete ListView layout** `deleteListViewLayout`: Delete an existing ListView layout.
* **Delete record** `deleteRecord`: Delete a record of a model by id.
* **Delete report archived runs** `deleteReportArchivedRuns`: Delete archived run data of a report; all runs are deleted when no IDs are given.
* **Delete webhook** `deleteWebhook`: Delete a webhook by id.
* **Download file** `downloadFile`: Download a Document (latest revision), DocumentRevision or Note attachment file; response is raw file data.
* **Download update package** `downloadUpdatePackage`: Download an update package into the instance upgrades directory.
* **Download vCard or iCal** `downloadVcard`: Download a contact vCard or a call/meeting iCal; response is raw file data.
* **Erase personal data** `erasePersonalData`: Erase selected personal data fields from a record (irreversible).
* **Export list records** `exportListRecords`: Return a file with exported records of a model. Filters are passed as extra inputs named filters[key].
* **Export target list CSV** `exportTargetListCsv`: Download a CSV file with the exported targets of a target list.
* **Generate job invoices** `generateJobInvoices`: Generate prepared invoices for outstanding approved booked hours.
* **Generate statement PDF email drafts** `generateStatementEmailDrafts`: Generate statement PDFs and attach them to draft emails (drafts only; sending is a separate action).
* **Get 1CRM version** `getVersion`: Return the 1CRM version and whether the request is authenticated; useful to validate credentials.
* **Get about page info** `getAboutInfo`: Get edition, version and license info for the About page.
* **Get application strings** `getAppStrings`: Get translated application strings and dropdown options for a language.
* **Get calendar settings** `getCalendarSettings`: Retrieve calendar system settings and view parameters for the current or a given user.
* **Get Current User** `getCurrentUser`: Returns information about the authenticated 1CRM user, including name, role, admin flag, timezone and profile photo.
* **Get dashboard** `getDashboard`: Retrieve dashboard metadata by id.
* **Get dashlets initial data** `getDashletsInitData`: Retrieve initial data for all ListView dashlets on a dashboard.
* **Get DetailView metadata** `getDetailViewMetadata`: Retrieve DetailView metadata (sections, fields, buttons) for a model and layout.
* **Get Dropbox link** `getDropboxLink`: Get a direct link to a Dropbox file.
* **Get employee leave** `getEmployeeLeave`: Retrieve vacation and sick days for an employee in a fiscal year.
* **Get external dashlet data** `getDashletExternalData`: Get data for an external dashlet. Params are passed as extra inputs named params[key].
* **Get file info** `getFileInfo`: Get metadata (name, MIME type, size, temporary URL) for a Document or Note attachment.
* **Get generic module layouts** `getGenericModuleLayouts`: Generic module metadata: default list, detail and popup layouts.
* **Get import data** `getImportDbData`: Get the data needed to import module records for an import step and profile.
* **Get license info** `getLicenseInfo`: Get license and vendor info.
* **Get ListView editor metadata** `getListViewEditorMetadata`: Retrieve ListView editor metadata for a module.
* **Get ListView editor sources** `getListViewEditorSources`: Retrieve available field sources for the ListView editor of a module.
* **Get ListView metadata** `getListViewMetadata`: Retrieve ListView metadata (columns, filters, layouts) for a model.
* **Get locale settings** `getLocale`: Retrieve how 1CRM formats dates, numbers, names, addresses and currencies.
* **Get login page message** `getLoginMessage`: Get the customised or default login page message.
* **Get menu shortcuts** `getMenuShortcuts`: Get menu shortcuts for a module.
* **Get metadata versions** `getMetadataVersions`: Get metadata cache versions grouped by category; versions change whenever the cache is updated.
* **Get MFA data** `getMfaSettings`: Get multi-factor authentication data (recovery codes, secret, QR code URI) for the current user.
* **Get model fields** `getModelFields`: Return field definitions and available filters for a model.
* **Get module info** `getModuleInfo`: Information about a module: primary bean, default tab group, web actions and PDF templates.
* **Get module strings** `getModuleStrings`: Get translated module strings and dropdown options for a language.
* **Get opportunities forecast** `getOpportunitiesForecast`: Get opportunities revenue or product forecast data.
* **Get opportunities forecast (POST)** `postOpportunitiesForecast`: Get opportunities forecast data using POST with query parameters.
* **Get PDF signing data** `getPdfSigningData`: Get the PDF document signing data for a template and record.
* **Get PDF template config fields** `getPdfTemplateConfigFields`: Get fields for PDF template configuration of a model.
* **Get personal data** `getPersonalData`: Get personal (GDPR) data fields from a record.
* **Get record** `getRecord`: Retrieve a single record of a model by id; fields depend on model. Init params are passed as extra inputs named init_params[key].
* **Get record audit logs** `getRecordAuditLogs`: Retrieve audit logs of a specific record.
* **Get record carousel list** `getRecordCarousel`: Get the carousel list (history items) of a record.
* **Get record history** `getRecordHistory`: Retrieve the audit history of a record (summary or account total history).
* **Get report data** `getReportData`: Retrieve report data of an archived run.
* **Get server public key** `getPublicKey`: Get the server public key.
* **Get sub panels initial data** `getSubPanelsInitialData`: Get initial data for all ListView sub panels of a detail layout at once.
* **Get sub panels metadata** `getSubPanelsMetadata`: Retrieve sub panels metadata for a model and detail layout.
* **Get sub panels order** `getSubPanelsOrder`: Return the list of sub panels for a module layout.
* **Get supported products data** `getSupportedProducts`: Get supported products, sub-contracts, projects and contract types for an initiator record.
* **Get tally object** `getTallyRecord`: Get a tally object (record with grouped totals) by model and id.
* **Get updates summary** `getUpdatesSummary`: Return the number of unread and new emails and activities for the current user.
* **Get web form HTML** `getWebFormHtml`: Generate the HTML and CSRF token of a web form.
* **Get webhook** `getWebhook`: Get a webhook by id.
* **Import module records** `importModuleRecords`: Import module records from an uploaded data file, step by step.
* **Import vCard from uploaded file** `importVcard`: Create a record by importing a previously uploaded vCard/iCal file.
* **Issue purpose-scoped one-time token** `issueOtp`: Issue a short-lived one-time token for a purpose: download (download.php via dt parameter) or cross_login.
* **List all linked records** `listAllLinkedRecords`: Retrieve all related records of a model via a link, across parent records.
* **List audit logs** `listAuditLogs`: Retrieve audit logs for a model.
* **List available app updates** `listAppUpdates`: Return available application updates, optionally refreshing the check.
* **List available dashlets** `listDashlets`: Retrieve available dashlets for a dashboard grouped by category.
* **List booked hours by timesheet** `listTimesheetHours`: Retrieve booked hours for a date range by timesheet.
* **List calendar activities** `listCalendarActivities`: Retrieve calendar activities (calls, meetings, tasks, marketing events, vacations) for a date range.
* **List calendar events** `listCalendarEvents`: Retrieve events within a date range, grouped by type and sorted by date (max 200 per type).
* **List Dropbox files** `listDropboxFiles`: List Dropbox files at a path via the connected Dropbox integration.
* **List editor images** `listEditorImages`: List images in the visual editor global directory (files/editor/global/).
* **List free/busy lines** `listFreeBusy`: Retrieve dates when a user, contact, lead or resource is busy.
* **List holidays** `listHolidays`: Retrieve holidays for a country and year.
* **List languages** `listLanguages`: Retrieve all available languages.
* **List main menu tab groups** `listTabGroups`: Retrieve available tab groups for the main menu.
* **List meetings by resource** `listMeetingsByResource`: Retrieve meetings by resource for a date range.
* **List meetings by users and resources** `listDayResources`: Retrieve meetings for selected user IDs and resource IDs in a date range.
* **List modules** `listModules`: Return all available modules.
* **List project tasks** `listProjectTasks`: Retrieve project tasks for a date range, optionally by project and assigned user.
* **List recently viewed items** `listRecentItems`: Retrieve items recently viewed by the current user. Filters are passed as extra inputs named filters[key].
* **List records** `listRecords`: Retrieve a list of records of a model (Account, Contact, Lead, Opportunity, Case, Invoice and more). Filters are passed as extra inputs named filters[key], for example filters[account_type]; see model metadata for available filters.
* **List related records** `listRelatedRecords`: Retrieve related records of a record via a link. Filters are passed as extra inputs named filters[key].
* **List report archived runs** `listReportArchivedRuns`: Retrieve archived runs of a report.
* **List reports** `listReports`: Retrieve reports of a model. Filters are passed as extra inputs named filters[key].
* **List states** `listStates`: Get states grouped by country.
* **List team users** `listTeamUsers`: Retrieve users of a calendar team by team ID.
* **List theme presets** `listThemePresets`: Get available theme presets for the application.
* **List webhooks** `listWebhooks`: List configured webhooks.
* **Log client error** `logClientError`: Add a client-side error entry to the 1CRM log.
* **Mass update records** `massUpdateRecords`: Run a mass action (update, delete, trash, campaign actions) on a list of records. Campaign actions send emails.
* **Print activity summary PDF** `printSummaryPdf`: Print a PDF with the activity summary of a record.
* **Print calendar day PDF** `printCalendarDayPdf`: Print the events of a day as PDF.
* **Print MFA recovery codes PDF** `printMfaRecoveryCodesPdf`: Print the current user's multi-factor authentication recovery codes as PDF.
* **Print personal data PDF** `printPersonalDataPdf`: Print a PDF with the personal data of a record (models with personal data enabled).
* **Print record PDF** `printRecordPdf`: Print a PDF for a record using a PDF template; returns PDF content or a Note ID.
* **Print screen layout PDF** `printScreenLayoutPdf`: Print a PDF of a record using its DetailView screen layout.
* **Print service subcontract PDF** `printSubcontractPdf`: Print service subcontract details as PDF.
* **Process license key or file** `processLicense`: Apply a license key or uploaded license file to update the instance license.
* **Remove related record** `removeRelatedRecord`: Remove the relationship between two records.
* **Request password recovery email** `requestPasswordRecovery`: Request a password recovery email for a user name. Sends an email to the user.
* **Request startup license** `requestStartupLicense`: Submit a Startup license request to 1CRM (sends company contact details to the vendor).
* **Reset DAV sync token** `resetDavToken`: Reset CardDAV and CalDAV sync tokens of a user to force a resync.
* **Restore DetailView layout** `restoreDetailViewLayout`: Restore the default or backup version of a DetailView layout.
* **Restore record from audit log** `restoreRecord`: Restore a record to the state recorded in an audit log entry.
* **Run report** `runReport`: Run a report and return the data ID and report data.
* **Search records** `searchRecords`: Global search across models by query string (minimum 2 characters).
* **Send statement PDF emails** `sendStatementEmails`: Send draft emails with attached statement PDFs to recipients. Sends email outward.
* **Submit web form** `submitWebForm`: Submit web form data to create a record in the form's target module.
* **Test email connection** `testEmailConnection`: Check a mail server connection. Connection fields are passed as extra inputs named fields[key].
* **Update dashboard layout** `updateDashboardLayout`: Update a dashboard's column layout and display options.
* **Update dashlet settings** `updateDashletSettings`: Update or reset the settings of a dashlet.
* **Update DetailView tabs** `updateDetailViewTabs`: Update order, visibility and names of DetailView tabs for a model, or reset them.
* **Update list view tabs preference** `updateListViewTabs`: Update the current user's list tabs preference for a model.
* **Update ListView layout** `updateListViewLayout`: Update an existing ListView layout.
* **Update MFA settings** `updateMfaSettings`: Disable MFA or verify an MFA code for a user.
* **Update record** `updateRecord`: Update a record of a model by id; only fields in data are modified.
* **Update sub panels order** `updateSubPanelsOrder`: Update or reset the sub panels order for a module layout.
* **Update theme preset** `updateThemePreset`: Update a theme preset by id.
* **Update user password or timezone** `updateCurrentUserPassword`: Update a user's password (or force change on next login) and timezone.
* **Update webhook** `updateWebhook`: Update a webhook's trigger type, URL, model and filters.
* **Upload file (binary)** `uploadFile`: Upload raw binary file content to a temporary location; the returned file ID can be used for file_ref or image fields.
* **Upload small file (base64)** `uploadFileBase64`: Upload a small base64-encoded file to a temporary location; the returned file ID can be used for file_ref or image fields.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Record created | `create` |  |
| Record created or updated | `create_update` |  |
| Record updated | `update` |  |
