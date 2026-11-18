---
description: "FuseDesk help desk and messaging platform."
hidden: true
---

# FuseDesk

<img src="../../.gitbook/assets/connectors/lg/fusedesk.png" alt="FuseDesk logo">

FuseDesk help desk and messaging platform. Manage cases, case notes, case tags, contacts, companies, departments, reps, emails, chats, automations, snippets, integrations, webhooks, activity and reports in your FuseDesk app.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [fusedesk.com](https://fusedesk.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `fusedesk` |

## Use it

Add FuseDesk from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fusedesk.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Case Note | `addCaseNote` | Add an internal note or a logged phone call to a FuseDesk case. Notes are visible to reps only and are never emailed to the contact. |
| Apply Case Tag | `applyCaseTag` | Apply an existing case tag to a FuseDesk case. Both the case ID and the case tag ID are required. |
| Archive Department | `archiveDepartment` | Archive a FuseDesk department so it no longer appears in the active department list. Archived departments can be brought back with Restore Department. |
| Authenticate As Rep | `authenticateAsRep` | Exchange a FuseDesk rep's email and password for a session and, when Request Token is true, a JWT bearer token. SECURITY WARNING: the response carries a live credential, so never log or forward it. If the supplied login is wrong but the API key is valid, FuseDesk still answers 200 with a FuseDesk System placeholder user and a token that does not authenticate. |
| Bulk Update Cases | `bulkUpdateCases` | Apply the same change to many FuseDesk cases at once: set a status, move them to a department, snooze them, merge them, or fire a CRM automation or CRM tag. To reassign a rep or apply a FuseDesk case tag in bulk, use Update Case or Apply Case Tag per case - the equivalent bulk fields are broken on FuseDesk's side. |
| Close Chat | `closeChat` | Close and resolve a FuseDesk chat. Optionally supply a rep, department and status to open a case from the chat transcript at the same time. |
| Create Automation | `createAutomation` | Create a FuseDesk automation rule. The API key must belong to a rep with admin rights, otherwise FuseDesk refuses the call. |
| Create Case | `createCase` | Create a new case in FuseDesk. Requires the name of who opened the case, a summary, details and the department the case belongs to. |
| Create Case Tag | `createCaseTag` | Create a new case tag in FuseDesk so it can be applied to cases. |
| Create Contact | `createContact` | Create a new contact in FuseDesk. At least one field must be supplied; an entirely empty contact is rejected. |
| Create Department | `createDepartment` | Create a new department in FuseDesk so cases can be routed to it. |
| Create Department (API v2) | `createDepartmentV2` | Create a new FuseDesk department using the v2 API. KNOWN VENDOR ISSUE: as of September 2026 this route returns a 500 database error for every request; use Create Department (the v1 route) instead, which works. |
| Create Integration | `createIntegration` | Create a third-party integration record in FuseDesk. Platform must be one FuseDesk recognises; unknown values are rejected with a platform is invalid error. |
| Create Integration (API v2) | `createIntegrationV2` | Create a third-party integration record in FuseDesk using the v2 API. Platform must be one FuseDesk recognises. Note that this route intermittently returns a 500 from FuseDesk; retry, or use Create Integration on the v1 route. |
| Create Or Update Chat | `updateChat` | Create or update a FuseDesk chat. Supplying a chat UUID that does not exist creates a new chat on the given integration; supplying an existing one renames it, transfers it to another rep or department, relinks its contact, links it to a case or marks messages as seen. |
| Create Snippet | `createSnippet` | Create a saved reply snippet in FuseDesk and choose which channels it is offered in: chat, email and case notes. |
| Create Webhook | `createWebhook` | Register an outbound webhook in FuseDesk. FuseDesk validates the URL by calling it first and rejects any URL that does not answer 2xx. SECURITY WARNING: the response echoes your FuseDesk API key in plaintext as createdByApiKey, so never log or forward it. |
| Delete Attachment | `deleteAttachment` | Delete an uploaded FuseDesk attachment by the stored file name that Upload Attachment returned. |
| Delete Automation | `deleteAutomation` | Delete a FuseDesk automation rule by its ID. The API key must belong to a rep with admin rights. |
| Delete Case | `deleteCase` | Permanently delete a FuseDesk case by its case ID. This cannot be undone, so confirm the case ID before calling. |
| Delete Case Tag | `deleteCaseTag` | Delete a case tag from FuseDesk by its tag ID. The tag is removed from every case that carried it. |
| Delete Contact | `deleteContact` | Delete a FuseDesk contact by its contact UUID. Cases previously linked to the contact remain, but the contact record is removed. |
| Delete Email | `deleteEmail` | Permanently delete an email message from FuseDesk by its email ID. The message is removed from its case history, so confirm the ID before calling. |
| Delete Integration | `deleteIntegration` | Delete a FuseDesk integration by its ID, disconnecting that third-party platform from your app. |
| Delete Integration (API v2) | `deleteIntegrationV2` | Delete a FuseDesk integration by ID using the v2 API. |
| Delete Rep | `deleteRep` | Remove a rep from your FuseDesk app. DANGER: deleting the rep your API key belongs to, or the last remaining rep, can lock you out of the app permanently and FuseDesk offers no API recovery. Always check List Reps first and never pass your own user ID. |
| Delete Snippet | `deleteSnippet` | Delete a saved reply snippet from FuseDesk by its snippet UUID. |
| Delete Webhook | `deleteWebhook` | Remove a registered outbound webhook from FuseDesk by its webhook ID, stopping further deliveries. |
| Disable Case Feedback | `disableCaseFeedback` | Stop FuseDesk from asking the contact for feedback on this case when it is closed. |
| Enable Case Feedback | `enableCaseFeedback` | Allow FuseDesk to ask the contact for feedback on this case when it is closed, reversing a previous Disable Case Feedback call. |
| Get Account | `getAccount` | Retrieve your FuseDesk account details, including billing information, the current plan, seat counts and app-wide options. |
| Get API Key Scopes | `getApiKeyScopes` | Return the app name, company name and the list of permission scopes granted to the API key in use. Note that the response also echoes the last four characters of that key. |
| Get Automation | `getAutomation` | Retrieve a single FuseDesk automation rule by its ID, with its full condition and action definitions. |
| Get Automation Rule (Rules Alias) | `getRule` | Retrieve one FuseDesk automation rule through the /rules alias, which returns the same record as Get Automation. |
| Get Case | `getCase` | Retrieve a single FuseDesk case by its case ID, including its summary, details, status, assigned rep, department, tags and history. |
| Get Case (API v2) | `getCaseV2` | Retrieve a single FuseDesk case by ID using the v2 API, which returns camelCase field names such as caseNumber, crmContactId and departmentId. |
| Get Case Feedback | `getCaseFeedback` | Retrieve the customer satisfaction rating and written feedback recorded against a FuseDesk case, together with the dates feedback was requested and given. |
| Get Chat | `getChat` | Retrieve a single FuseDesk chat conversation by its chat ID, including its messages and the contact it belongs to. |
| Get Contact | `getContact` | Retrieve a single FuseDesk contact by its contact UUID, including contact details, billing address and case counts. |
| Get Contact By CRM ID | `getContactByCrmId` | Retrieve a contact through the FuseDesk v1 API using its numeric contact ID from a connected CRM such as Keap or Infusionsoft. Use Get Contact if you have the FuseDesk contact UUID instead. |
| Get Department | `getDepartment` | Retrieve a single FuseDesk department by its department ID, with its assigned reps, templates and case ageing thresholds. |
| Get Department (API v2) | `getDepartmentV2` | Retrieve a single FuseDesk department by ID using the v2 API, which returns camelCase field names and the department's header and footer HTML. |
| Get Email | `getEmail` | Retrieve a single FuseDesk email message by its email ID, including its subject, body, sender and the case it belongs to. |
| Get Integration | `getIntegration` | Retrieve a single FuseDesk integration by its ID, including its platform, name and configuration. |
| Get Integration (API v2) | `getIntegrationV2` | Retrieve a single FuseDesk integration by ID using the v2 API. |
| Get Rep | `getRep` | Retrieve a single FuseDesk rep by their user ID, including name, email, signature, default department and last login. |
| Get Rep (API v2) | `getRepV2` | Retrieve a single FuseDesk rep by user ID using the v2 API. WARNING: the meta object in this response can include the rep's outstanding password-reset key, so treat the result as sensitive. |
| Global Search | `globalSearch` | Search FuseDesk for cases matching a free-text query. The endpoint returns every match and ignores paging parameters, so cap the result set in your own code. |
| List Active Departments | `listDepartments` | List the active departments in your FuseDesk app, with each department's reps, reply template, stale thresholds and feedback settings. |
| List Active Departments (API v2) | `listDepartmentsV2` | List the active FuseDesk departments using the v2 API, which returns camelCase field names and richer template settings. |
| List Activity | `listActivity` | List the whole activity feed for your FuseDesk app: case transfers, notes, emails, chats and other timeline entries. The endpoint returns the complete feed and ignores any filter parameters, so filter the result in your own code. |
| List All Departments | `listAllDepartments` | List every FuseDesk department, including archived ones, not just the currently active departments. |
| List All Departments (API v2) | `listAllDepartmentsV2` | List every FuseDesk department including archived ones using the v2 API. |
| List API Keys | `listApiKeys` | List the API keys configured in your FuseDesk app. SECURITY WARNING: the response may contain live credentials, so do not log or forward it. The calling key needs the apikeys scope, which FuseDesk does not grant to ordinary API keys. |
| List Archived Departments | `listArchivedDepartments` | List only the FuseDesk departments that have been archived, so they can be reviewed or restored. |
| List Automation Rules (Rules Alias) | `listRules` | List FuseDesk automation rules through the /rules alias, which returns the same records as List Automations. The endpoint returns all rules and accepts no filters. |
| List Automations | `listAutomations` | List every automation rule in your FuseDesk app, each with its trigger type, conditions and the actions it performs. The endpoint returns all rules; filter by trigger type in your own code. |
| List Case Tags | `listCaseTags` | List every case tag defined in your FuseDesk app, with each tag's ID, name, hidden flag and the number of cases carrying it. |
| List Cases (API v2) | `listCasesV2` | List FuseDesk cases using the v2 API, which returns camelCase field names such as caseNumber and crmContactId. Use Search Cases for the richer v1 filter set. |
| List Chats | `listChats` | List the live chat conversations in your FuseDesk app. |
| List Companies | `listCompanies` | List the companies in your FuseDesk app. This endpoint requires the companies scope on your API key; without it FuseDesk answers with a not-authorized error. |
| List Emails | `listEmails` | List all email messages in FuseDesk, optionally limited to a single case. Use Body Limit to control how much of each message body is returned. |
| List Integrations | `listIntegrations` | List the third-party integrations configured in your FuseDesk app, such as chat, SMS and CRM connections. |
| List Integrations (API v2) | `listIntegrationsV2` | List the third-party integrations configured in your FuseDesk app using the v2 API. |
| List Reports | `listReports` | List the reports available in your FuseDesk app, with each report's short name, category, chart type and which groupings and filters it supports. Use the short name with Run Report. |
| List Reps | `listReps` | List every support rep (user) in your FuseDesk app, with their name, email, signature, default department, timezone and notification preferences. |
| List Reps (API v2) | `listRepsV2` | List every FuseDesk rep using the v2 API, which returns camelCase field names such as userId, firstName and emailAddress. |
| List Snippets | `listSnippets` | List the saved reply snippets in your FuseDesk app, with the channels each snippet is available in. |
| List Trashed Emails | `listTrashedEmails` | List the email messages currently sitting in the FuseDesk trash. |
| List Unassigned Emails | `listUnassignedEmails` | List inbound emails that have arrived in FuseDesk but have not yet been turned into a case, so they can be triaged. |
| List Webhooks | `listWebhooks` | List the outbound webhooks registered in your FuseDesk app, with the object type, action and target URL each one fires on. SECURITY WARNING: each row echoes the FuseDesk API key that created it in plaintext as createdByApiKey, so never log or forward this response. |
| Remove Case Tag | `removeCaseTag` | Remove a case tag from a FuseDesk case. The tag itself is not deleted, only its link to this case. |
| Reply To Case By Email | `replyToCase` | Send an email reply on a FuseDesk case. CAUTION: this delivers a real email to the recipients you supply. Leave the To line empty to reply to the case contact's own email address. |
| Request Case Feedback Now | `requestCaseFeedback` | Immediately email the case contact a request to rate this FuseDesk case. CAUTION: this sends a real email to the contact. |
| Restore Department | `restoreDepartment` | Restore a previously archived FuseDesk department back into the active department list. |
| Run Report | `runReport` | Run one FuseDesk report by its short name and return its columns and data rows. Short names come from List Reports, for example emails, caseload, resolution or teamactivity. |
| Search Cases | `searchCases` | Search and list FuseDesk cases. All filters are optional; combine them to narrow the result set. Returns an array of case objects. |
| Search Companies | `searchCompanies` | Search FuseDesk companies by name using the v2 API. The search term must be at least two characters long, and the API key needs the companies scope. |
| Search Contacts | `searchContacts` | Search FuseDesk contacts by name, email address, phone number or company. The search term must be at least two characters long. |
| Search Contacts (API v1) | `findContactV1` | Search contacts through the FuseDesk v1 API, which looks up contacts synced from a connected CRM such as Keap or Infusionsoft. Apps with no CRM connected get a no matching contacts response; use Search Contacts for FuseDesk-native contacts. |
| Snooze Case | `snoozeCase` | Snooze a FuseDesk case until a given date and time, hiding it from the active case queue until then. |
| Update Account Options | `updateAccountOptions` | Update your FuseDesk app-wide options: whether inbound emails are linked to contacts automatically, and the minimum length required for case note titles and bodies. |
| Update Automation | `updateAutomation` | Update a FuseDesk automation rule's name, conditions, actions, order or active flag. The API key must belong to a rep with admin rights. |
| Update Case | `updateCase` | Update an existing FuseDesk case: change its summary or details, move its status, transfer it to another rep or department, or relink it to a different contact or company. |
| Update Case Tag | `updateCaseTag` | Rename an existing FuseDesk case tag. Every case already carrying the tag keeps it under the new name. |
| Update Contact | `updateContact` | Update an existing FuseDesk contact. Only the fields you supply are changed; omitted fields keep their current values. |
| Update Department | `updateDepartment` | Update a FuseDesk department's reps, default reply template, case ageing thresholds and customer feedback settings. |
| Update Department (API v2) | `updateDepartmentV2` | Update a FuseDesk department using the v2 API: its reps, default reply template, case ageing thresholds and customer feedback settings. |
| Update Integration | `updateIntegration` | Rename an existing FuseDesk integration. The platform an integration connects to cannot be changed after creation. |
| Update Rep | `updateRep` | Update a FuseDesk rep's profile: their name, email signature, timezone, default department or daily update preference. |
| Update Scheduled Email | `updateScheduledEmail` | Edit an email that a rep has composed but FuseDesk has not sent yet, for example to change its recipients, its wording or when it goes out. FuseDesk refuses any email that has already been sent or that was not created by a rep. |
| Update Snippet | `updateSnippet` | Update a saved reply snippet's text or the channels it is available in. |
| Update Webhook | `updateWebhook` | Point an existing FuseDesk webhook at a different target URL. Only the URL can be changed; to watch a different object type or action, delete the webhook and create a new one. FuseDesk validates the new URL by calling it and rejects one that does not answer 2xx. Note that the response body is a snapshot taken before the change, so re-read with List Webhooks to see the new URL. SECURITY WARNING: the response echoes your FuseDesk API key in plaintext. |
| Upload Attachment | `uploadCaseAttachment` | Upload a text file to FuseDesk so it can be attached to a case reply. Returns the stored file name and its download URL. Only text content is supported through this action; binary uploads are not. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Case Closed | `case.close` | Fires when a case is closed in FuseDesk. Payload schema is MODELLED from the live GET /api/v2/cases/{id} response shape, not captured from a real delivery. |
| Case Created | `case.create` | Fires when a new case is opened in FuseDesk. The payload schema below is MODELLED from the live GET /api/v2/cases/{id} response shape, not captured from a real delivery. |
| Case Status Changed | `case.status` | Fires when a case moves between the new, open and closed statuses. Payload schema is MODELLED from the live GET /api/v2/cases/{id} response shape, not captured from a real delivery. |
| Case Transferred | `case.transfer` | Fires when a case is reassigned to a different rep or department. Payload schema is MODELLED from the live GET /api/v2/cases/{id} response shape, not captured from a real delivery. |
| Case Updated | `case.update` | Fires when a case is changed in FuseDesk. Payload schema is MODELLED from the live GET /api/v2/cases/{id} response shape, not captured from a real delivery. |
| Contact Created | `contact.create` | Fires when a new contact is added to FuseDesk. Payload schema is MODELLED from the live GET /api/v2/contacts/{id} response shape, not captured from a real delivery. |
| Contact Updated | `contact.update` | Fires when a contact record is changed in FuseDesk. Payload schema is MODELLED from the live GET /api/v2/contacts/{id} response shape, not captured from a real delivery. |
| Department Created | `department.create` | Fires when a new department is created in FuseDesk. Payload schema is MODELLED from the live GET /api/v2/departments/{id} response shape, not captured from a real delivery. |
| Department Updated | `department.update` | Fires when a department's settings change in FuseDesk. Payload schema is MODELLED from the live GET /api/v2/departments/{id} response shape, not captured from a real delivery. |
| Rep Created | `rep.create` | Fires when a new rep (support user) is added to FuseDesk. Payload schema is MODELLED from the live GET /api/v2/reps/{id} response shape, not captured from a real delivery. |
| Rep Updated | `rep.update` | Fires when a rep's profile changes in FuseDesk. Payload schema is MODELLED from the live GET /api/v2/reps/{id} response shape, not captured from a real delivery. |
