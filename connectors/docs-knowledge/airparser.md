---
description: "Airparser is an AI-powered document and email parser that extracts structured data from PDFs, emails, images and spreadsheets."
hidden: true
---

# Airparser

Airparser is an AI-powered document and email parser that extracts structured data from PDFs, emails, images and spreadsheets. This connector covers the Airparser public API: inboxes, extraction schemas, documents and parsed results, post-processing, document review, integrations (webhooks, Zapier, Make, n8n, Google Sheets), team, account settings and billing information.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [airparser.com](https://airparser.com) |
| **Authentication** | API key |
| **Actions** | 62 |
| **Events** | 3 |
| **Slug** | `airparser` |

## Use it

Add Airparser from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.airparser.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Approve Document Review | `approveDocumentReview` | Approves a document that is waiting in the human review queue, optionally applying corrections to the extracted data, and releases it to the inbox's integrations. |
| Clone Extraction Schema | `cloneExtractionSchema` | Copies the extraction schema of one inbox onto another inbox, replacing the destination inbox's current schema. |
| Create Inbox | `createInbox` | Creates a new Airparser inbox. An inbox groups documents that share one extraction schema and receives documents by email forwarding or API upload. |
| Create Webhook | `createWebhook` | Registers a webhook on an Airparser inbox. Airparser posts the parsed document JSON to the target URL whenever the selected event occurs. |
| Delete Documents | `deleteDocuments` | Permanently deletes the named documents from an Airparser inbox. |
| Delete Google Sheets Integrations | `deleteGoogleSheetsIntegrations` | Permanently removes the named Google Sheets integrations from Airparser. |
| Delete Inbox | `deleteInbox` | Permanently deletes an Airparser inbox together with every document it contains. This cannot be undone. |
| Delete Webhooks | `deleteWebhooks` | Permanently removes the named webhooks from Airparser. At least one webhook id must be supplied. |
| Disable Make Integrations | `disableMakeIntegrations` | Switches the named Make subscriptions off so they stop receiving parsed documents. |
| Disable n8n Integrations | `disableN8nIntegrations` | Switches the named n8n subscriptions off so they stop receiving parsed documents. |
| Disable Webhooks | `disableWebhooks` | Switches the named webhooks off so they stop delivering parsed documents, without deleting them. |
| Disable Zapier Integrations | `disableZapierIntegrations` | Switches the named Zapier subscriptions off so they stop receiving parsed documents. |
| Enable Google Sheets Integration | `enableGoogleSheetsIntegration` | Switches one Google Sheets integration on or off without deleting it. |
| Enable Make Integrations | `enableMakeIntegrations` | Switches the named Make subscriptions on so they resume receiving parsed documents. |
| Enable n8n Integrations | `enableN8nIntegrations` | Switches the named n8n subscriptions on so they resume receiving parsed documents. |
| Enable Post-Processing | `enablePostProcessing` | Turns the inbox's post-processing Python script on or off. When enabled, the script runs on every parsed document before the data reaches integrations. |
| Enable Webhooks | `enableWebhooks` | Switches the named webhooks on so they resume delivering parsed documents. |
| Enable Zapier Integrations | `enableZapierIntegrations` | Switches the named Zapier subscriptions on so they resume receiving parsed documents. |
| Exchange Google Sheets Authorization Code | `exchangeGoogleSheetsAuthCode` | Exchanges the authorization code Google returns after consent for a stored Google account in Airparser, which can then be used by Google Sheets integrations. |
| Generate Extraction Schema | `generateExtractionSchema` | Uses AI to propose and apply an extraction schema for an inbox based on one sample document already uploaded to that inbox, and returns the generated field definitions. The sample document must belong to the named inbox. |
| Generate Post-Processing Script | `generatePostProcessingScript` | Uses AI to write a post-processing Python snippet from a plain-English instruction, using one document's extracted data as the example input. This feature requires a paid Airparser plan; on the free trial the endpoint answers 403 'This feature requires a paid plan.' |
| Get Account Settings | `getAccountSettings` | Returns the Airparser account's preferences, including time zone, time and date formats and notification settings. |
| Get Billing Details | `getBillingDetails` | Returns the billing address, VAT identifier and saved payment cards recorded on the Airparser account. |
| Get Current User | `getCurrentUser` | Returns the Airparser account the API key belongs to, including the owner's name, email, role, credit balance and the inboxes they can access. |
| Get Document | `getDocument` | Returns a parsed document in the compact webhook-style format, including its processing status and the extracted JSON data. |
| Get Document Extended | `getDocumentExtended` | Returns the full detail record for a document, including the raw extracted text, page count, preview image, sibling document ids and the extracted JSON. Set Source to 'parsed' to receive the original parser output instead of the post-processed data. |
| Get Document Integration Payload | `getDocumentIntegrations` | Returns the document exactly as the inbox's integrations would receive it, after post-processing and metadata fields are applied. Set Unwind Rows to true to flatten list fields into dotted keys such as line_items.0.description, which is what row-per-item destinations receive. |
| Get Document Logs | `getDocumentLogs` | Returns the processing log entries recorded for a document, covering import, conversion, extraction and integration delivery steps. |
| Get Document Post-Processed Data | `getDocumentPostProcessedData` | Returns the document with the inbox's saved post-processing script applied to its extracted data, without changing the stored document. Use it to preview what integrations would receive. |
| Get Google Sheets Access Token | `getGoogleSheetsAccessToken` | Returns a short-lived Google access token for a connected Google account, used by the Airparser app's Google Picker. Only the account owner may request it. |
| Get Google Sheets Authorization URL | `getGoogleSheetsAuthUrl` | Returns the Google consent URL a user must open to connect a Google account for the Google Sheets integration. The response is the URL as a bare string. |
| Get Google Sheets Integration | `getGoogleSheetsIntegration` | Returns one Google Sheets integration by its integration id, including the Google account, spreadsheet and worksheet it writes to. Use List Inbox Integrations to find the ids of entries of type 'sheets'. |
| Get Inbox | `getInbox` | Returns a single Airparser inbox by id, including its parsing configuration, PDF splitting and page-processing rules, review settings and the current extraction schema. |
| Get Inbox Activity Sparklines | `getInboxActivitySparklines` | Returns recent per-day document volume for every inbox in the account, keyed by inbox id, for dashboard activity charts. |
| Get Inbox Integration Stats | `getInboxIntegrationStats` | Returns counts of the integrations configured on an inbox, broken down by webhook and Zapier connections. |
| Get Inbox Table Fields | `getInboxTableFields` | Returns the list-type fields of an inbox's extraction schema, which are the fields that can be expanded into one row per item by row-based destinations such as Google Sheets. |
| Get Make Integration | `getMakeIntegration` | Returns one Make (Integromat) subscription by its integration id. Make subscriptions are created from the Make app itself, not through this API; use List Inbox Integrations to discover their ids. |
| Get n8n Integration | `getN8nIntegration` | Returns one n8n subscription by its integration id. n8n subscriptions are created from the n8n Airparser node, not through this API; use List Inbox Integrations to discover their ids. |
| Get Post-Processing Script | `getPostProcessingScript` | Returns the post-processing Python script configured on an inbox and whether it is currently enabled. |
| Get Webhook | `getWebhook` | Returns one Airparser webhook by id, including its target URL, event, enabled state and signing secret. To list every webhook on an inbox, use List Inbox Integrations. |
| Get Zapier Integration | `getZapierIntegration` | Returns one Zapier subscription by its integration id. Zapier subscriptions are created from the Zapier app itself, not through this API; use List Inbox Integrations to discover their ids. |
| List Documents | `listDocuments` | Returns a paginated list of documents in an Airparser inbox, optionally filtered by processing status, received date range or a free-text search over the document name and contents. |
| List Google Sheets Accounts | `listGoogleSheetsAccounts` | Returns the Google accounts connected to Airparser for the Google Sheets integration. |
| List Google Spreadsheet Worksheets | `listGoogleSheetsWorksheets` | Returns the worksheet tabs of one Google spreadsheet, using a Google account already connected to Airparser. |
| List Google Worksheet Columns | `listGoogleSheetsWorksheetColumns` | Returns the header columns of one worksheet tab, so extracted fields can be mapped onto them. |
| List Inbox Integrations | `listInboxIntegrations` | Returns every integration configured on an inbox across all types: webhooks, Zapier, Make, n8n and Google Sheets. |
| List Inboxes | `listInboxes` | Returns every inbox in the connected Airparser account, including each inbox's name, forwarding email prefix, parsing engine, retention, document statistics and extraction schema configuration. |
| List Invoices | `listInvoices` | Returns the billing invoices issued for the Airparser account. |
| List Pricing Plans | `listPricingPlans` | Returns the Airparser subscription plans available to the account, with their price, currency and included document credits. |
| List Team Members | `listTeamMembers` | Returns everyone with access to the Airparser account, with their role and which inboxes they can see. |
| List Webhook Delivery Logs | `listWebhookLogs` | Returns a paginated history of delivery attempts for one webhook, including the payload sent and the response status returned by the target URL. |
| Refresh Extraction Schema | `refreshExtractionSchema` | Rebuilds an inbox's extraction schema from the fields present in its most recently parsed documents. Returns true when the schema changed. |
| Reparse Documents | `reparseDocuments` | Re-runs extraction on the named documents in an inbox using the inbox's current extraction schema. Each reparse consumes credits. |
| Request Document Review | `requestDocumentReview` | Sends a parsed document to the human review queue so a person can correct the extracted data before it is delivered to integrations. |
| Resend Webhook Delivery | `resendWebhookDelivery` | Re-sends one past webhook delivery to its target URL, which is useful after a receiving endpoint was temporarily down. |
| Run Post-Processing Script | `runPostProcessingScript` | Runs a post-processing Python snippet against one document's extracted data and returns the transformed result, so the script can be tested before it is saved. The script receives the extracted data as the dict 'data' and must return it. Running a script also saves it as the inbox's post-processing code. |
| Set Extraction Schema | `setExtractionSchema` | Creates or replaces the extraction schema of an inbox. The schema defines which fields Airparser extracts from every document in that inbox. Each entry is a scalar, list, object or enum field definition. |
| Set Inbox Metadata Fields | `setInboxMetadataFields` | Chooses which built-in document metadata fields, such as sender, subject or page count, are added to the extracted data of every document in an inbox. Any field set to false is omitted. This call replaces the whole selection. |
| Update Inbox | `updateInbox` | Updates an Airparser inbox's settings. This endpoint replaces the inbox configuration, so every required field must be supplied on each call - read the current values with Get Inbox first and send them back alongside your changes. The parsing engine cannot be changed here; it is fixed when the inbox is created. The response is a status envelope, not the updated inbox. |
| Update Webhook | `updateWebhook` | Updates an existing Airparser webhook's name, target URL, event or enabled state. |
| Upload Document | `uploadDocument` | Uploads a document to an Airparser inbox and returns its id immediately; parsing continues in the background. Accepts EML, PDF, HTML, TXT, MD, DOCX, XLSX, CSV, JPG, PNG, BMP and ZIP files up to 20 MB. The endpoint requires a multipart/form-data body, which the fastn HTTP engine cannot emit today, so this action cannot currently send a real file. |
| Upload Document And Wait | `uploadDocumentSync` | Uploads a document to an Airparser inbox, waits up to about 60 seconds for parsing to finish and returns the extracted data in the same response. ZIP files are not supported in this mode. The endpoint requires a multipart/form-data body, which the fastn HTTP engine cannot emit today, so this action cannot currently send a real file. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Document Failed | `doc.fail` | Fires when Airparser cannot process a document, for example an unsupported file or an exhausted credit balance. Set the inboxId input to the Airparser inbox this trigger should watch. The envelope shown here is the one captured from real doc.parsed and doc.received deliveries; this event's own body is modelled from it, because no failure could be provoked on the test account. |
| Document Parsed | `doc.parsed` | Fires when Airparser finishes extracting data from a document. Set the inboxId input to the Airparser inbox this trigger should watch. Payload schema captured from a real delivery. Airparser signs each delivery with an airparser-signature header holding base64(HMAC-SHA256(raw body, webhook secret)); the secret is unique per registration and is returned by the subscription, so the receiver must verify it. |
| Document Received | `doc.received` | Fires as soon as a document arrives in the inbox, before parsing starts. Payload schema captured from a real delivery: it carries only the inbox id, the document id and the event name, with no payload object, because nothing has been extracted yet. Fetch the result later with Get Document, or use Document Parsed instead. Set the inboxId input to the Airparser inbox this trigger should watch. |
