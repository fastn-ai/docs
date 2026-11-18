---
description: "Contractbook contract lifecycle management (CLM)."
hidden: true
---

# Contractbook

<img src="../../.gitbook/assets/connectors/contractbook.png" alt="Contractbook logo" width="64">

Contractbook contract lifecycle management (CLM). Wraps the Contractbook Public API v3 (https://api.contractbook.com/v3) for documents/contracts, templates, spaces, automations and attachment uploads. Authenticates with a Contractbook API Access Key sent as an Authorization: Bearer header.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [contractbook.com](https://contractbook.com) |
| **Authentication** | API key |
| **Slug** | `contractbook` |

## Use it

Add Contractbook from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.contractbook.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Child Space | `createChildSpace` | Creates a new space nested under the parent space identified by the given UUID. Spaces organise documents and templates into a hierarchy. NOTE: Contractbook's Public API v3 exposes no endpoint to rename or delete a space, so a space created here can only be removed from the Contractbook web app. |
| Create Document From Template | `createDocumentFromTemplate` | Creates a new Contractbook document draft from a contract template, optionally pre-filling its title, language, tags, data fields, parties and attachments. The document is created as a draft only - nothing is sent for signature until Send Document For Signature is called. Returns HTTP 201 with the created document, including its id and version. |
| Delete Document | `deleteDocument` | Permanently deletes a Contractbook document (draft or contract) by its UUID. Returns HTTP 204 with an empty body on success. This cannot be undone - Contractbook has no restore endpoint. |
| Get Document | `getDocument` | Retrieves a single Contractbook document (contract or draft) by its UUID, including its parties and signees, data fields, attachments, tags, state, current version identifier and sharing visibilities. |
| Get Document PDF | `getDocumentPdf` | Generates a PDF copy of a Contractbook document and returns a short-lived, pre-signed download URL in the 'location' field. The link expires after a few minutes, so download it immediately. |
| Get Space Tree | `getSpaceTree` | Returns the space (workspace) identified by the given UUID together with its descendant spaces as a tree. Spaces organise documents and templates into a hierarchy; the id of a document's space is exposed as document.workspace. |
| Get Template | `getTemplate` | Retrieves a single Contractbook contract template by its UUID, including the rich-text template body, its data field definitions, party placeholders, default signing order and default message. |
| List Automations | `listAutomations` | Lists the Contractbook automations configured for the organisation that start from a given trigger type. Automations are authored in the Contractbook web app's Automation Builder; the API only reads and runs them. trigger_type is mandatory - Contractbook rejects the request with HTTP 422 'Missing field: trigger_type' without it. |
| List Documents | `listDocuments` | Returns a cursor-paginated list of Contractbook documents (drafts, contracts and stored contracts) visible to the API key. Supports filtering by context, title, state, type, tag, ownership, signed/updated date ranges and integration object id, plus sorting and page size. Returns 'documents' and 'pagination_meta.cursor' for the next page. |
| List Templates | `listTemplates` | Returns every contract template available to the API key, including Contractbook's standard library and the organisation's own templates. Each entry carries the template id needed by Create Document From Template. |

<details>

<summary>See 6 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Run Automation | `runAutomation` | Runs a Contractbook automation by id, passing it the CRM object that triggered it. WARNING: an automation can create contracts and send them for signature to real people, depending on how it was built in the Automation Builder - review the automation before running it. Obtain the id from List Automations. |
| Send Document For Signature | `sendDocumentForSignature` | Sends a Contractbook draft to its signees for electronic signature. WARNING: this delivers real signature-request emails to every signee on the document and moves the document from draft to pending - it cannot be recalled through the API. Set autosign to control whether the API key owner's own signature is applied automatically during sending (only possible when the owner is a signee and their signing method is SMS or sign-with-a-click). |
| Share Document | `shareDocument` | Shares a Contractbook document with another user by email and grants them a collaboration role (manager, editor, filler or reviewer). Contractbook emails the recipient an invitation. Returns HTTP 204 with an empty body; confirm the result by reading the document's 'visibilities' array with Get Document. |
| Unshare Document | `unshareDocument` | Revokes a user's access to a Contractbook document by email, removing them from the document's sharing visibilities. Returns HTTP 204 with an empty body; confirm with Get Document that the 'visibilities' array no longer contains the address. |
| Update Document | `updateDocument` | Updates a Contractbook document (draft or contract) in place. The document.version returned by Get Document must be supplied so Contractbook can detect concurrent edits; the call fails if it does not match the latest version. Returns the full updated document. |
| Upload Attachment | `uploadAttachment` | Uploads a text-based file to Contractbook's attachment store and returns a pre-signed 'original' URL that can be passed to Create Document From Template or Update Document as a document attachment. Accepted MIME types are application/msword, application/pdf, application/vnd.ms-excel, the OpenXML spreadsheet and word types, application/zip, image/jpeg, image/png, text/csv and text/plain. Only text-based payloads can be supplied here because the file part is sent as UTF-8 text. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Contract Signed | `contract_signed` | A contract was signed. MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Contract signed' -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'contract_signed' and 'document_id' -&gt; Save -&gt; activate. |
| Contract Verified By AI | `contract_verified_ai` | Contractbook's AI verification finished for a contract. MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Contract verified (AI)' -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'contract_verified_ai' and 'document_id' -&gt; Save -&gt; activate. |
| Contract Viewed | `contract_viewed` | A party opened the contract. MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Contract viewed' -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'contract_viewed' and 'document_id' -&gt; Save -&gt; activate. |
| Data Field Date Reached | `data_field_date_reached` | A date stored in a document data field arrived (renewal or expiry reminders). MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Data field date reached' (pick the date field and offset) -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'data_field_date_reached' and 'document_id' -&gt; Save -&gt; activate. |
| Data Field Updated | `data_field_updated` | A data field value on a document changed. MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Data field updated' (pick the field) -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'data_field_updated' and 'document_id' -&gt; Save -&gt; activate. |
| Document Sent For Signature | `sent_for_signature` | A document left draft state and was sent to its signees. MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Sent for signature' -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'sent_for_signature' and 'document_id' -&gt; Save -&gt; activate. |
| Draft Created | `draft_created` | A Contractbook draft was created. MANUAL REGISTRATION (Contractbook has no webhook API): Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Draft created' -&gt; Add step -&gt; 'Send a webhook request' -&gt; Method POST, URL = the fastn trigger URL -&gt; in the payload builder add a field named exactly 'eventType' with the literal value 'draft_created' and a field named 'document_id' holding the document id -&gt; Save -&gt; toggle the automation Active. Verify by creating a draft and checking the automation run log. |
| Draft Updated | `draft_updated` | A Contractbook draft was updated. MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Draft updated' -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'draft_updated' and 'document_id' -&gt; Save -&gt; activate. |
| Drafter Questionnaire Completed | `drafter_questionnaire_completed` | Someone finished a Contractbook drafter questionnaire. MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Drafter questionnaire completed' -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'drafter_questionnaire_completed' and 'document_id' -&gt; Save -&gt; activate. |
| HubSpot Contractbook Automation Triggered | `hubspot_contractbook_automation_triggered` | A HubSpot workflow invoked a Contractbook automation. Requires the Contractbook HubSpot integration. MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'HubSpot Contractbook automation triggered' -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'hubspot_contractbook_automation_triggered' -&gt; Save -&gt; activate. |

<details>

<summary>See 7 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| HubSpot Deal Stage Changed | `hubspot_deal_stage_changed` | A HubSpot Deal linked to Contractbook moved stage. Requires the Contractbook HubSpot integration. MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'HubSpot deal stage changed' -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'hubspot_deal_stage_changed' -&gt; Save -&gt; activate. |
| Inbound Webhook Trigger Fired | `webhook_trigger` | A generic automation that starts from Contractbook's own inbound webhook URL (https://api.contractbook.com/automations/webhooks/contractbook/&lt;random&gt;). MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Webhook' (copy the generated request URL Contractbook shows) -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'webhook_trigger' and 'document_id' where one applies -&gt; Save -&gt; activate. |
| Pipedrive Deal Stage Changed | `pipedrive_deal_stage_changed` | A Pipedrive Deal linked to Contractbook moved stage. Requires the Contractbook Pipedrive integration. MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Pipedrive deal stage changed' -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'pipedrive_deal_stage_changed' -&gt; Save -&gt; activate. |
| Salesforce Flow Executed | `salesforce_flow_executed` | A Salesforce Flow completed and called Contractbook. Requires the Contractbook Salesforce integration. MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Salesforce flow is completed' -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'salesforce_flow_executed' -&gt; Save -&gt; activate. |
| Salesforce Opportunity Stage Changed | `salesforce_opportunity_stage_changed` | A Salesforce Opportunity linked to Contractbook moved stage. Requires the Contractbook Salesforce integration. MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Salesforce opportunity stage changed' -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'salesforce_opportunity_stage_changed' -&gt; Save -&gt; activate. |
| Task Completed | `task_is_done` | A Contractbook task was marked done. MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Task is done' -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'task_is_done' and 'document_id' -&gt; Save -&gt; activate. |
| Task Due Date Reached | `task_due_date_reached` | A Contractbook task reached its due date. MANUAL REGISTRATION: Contractbook web app -&gt; Automations -&gt; Create automation -&gt; Trigger: 'Task due date reached' -&gt; Add step -&gt; 'Send a webhook request' -&gt; POST to the fastn trigger URL -&gt; payload must contain 'eventType' = 'task_due_date_reached' and 'document_id' -&gt; Save -&gt; activate. |

</details>
