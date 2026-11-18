---
description: "Parsio extracts structured data from emails, PDFs and other documents."
hidden: true
---

# Parsio

<img src="../../.gitbook/assets/connectors/lg/parsio.png" alt="Parsio logo">

Parsio extracts structured data from emails, PDFs and other documents. This connector covers the Parsio public API: mailboxes, document import and parsing, parsed data, extraction templates, webhooks, collected email addresses and account settings.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [parsio.io](https://parsio.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `parsio` |

## Use it

Add Parsio from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.parsio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Clone Templates | `cloneTemplates` | Copies the given Parsio extraction templates into another mailbox. Parsio answers HTTP 201 for both success and failure, so check the Error field in the response rather than the status code. |
| Create Document | `createDocument` | Creates a document in a Parsio mailbox from plain text or HTML and starts parsing in the background. Returns the new document id immediately; fetch the parsed result later with Get Document or receive it through a webhook. Supply at least one of HTML Content or Text Content. |
| Create Document And Wait For Parsing | `createDocumentSync` | Creates a document from plain text or HTML and waits for the parsed result in the same response. Supported only by template-based and GPT-powered mailboxes. Parsio holds the request for up to about 60 seconds; if parsing has not finished it returns Parsing In Progress true and you fetch the result later with Get Document. |
| Create Mailbox | `createMailbox` | Creates a new Parsio mailbox. Parsio derives the inbound email prefix from the name; use Update Mailbox afterwards to change the prefix or any other setting. |
| Create Webhook | `createWebhook` | Registers a webhook on a Parsio mailbox so Parsio posts document events to your URL. Parsio's backend requires Enabled and Table Field ID on every create, even for events that have no table: send Table Field ID as an empty string unless the event is table.parsed. |
| Delete Mailbox | `deleteMailbox` | Permanently deletes a Parsio mailbox together with its documents, templates and parsed data. This cannot be undone. |
| Delete Templates | `deleteTemplates` | Permanently deletes the given Parsio extraction templates. Documents already parsed keep their extracted data. |
| Delete Webhooks | `deleteWebhooks` | Permanently deletes the given Parsio webhooks so Parsio stops posting events to them. |
| Disable Templates | `disableTemplates` | Disables the given Parsio extraction templates so they are no longer used when parsing new documents. |
| Disable Webhooks | `disableWebhooks` | Disables the given Parsio webhooks so Parsio stops posting events to them without deleting them. This endpoint is live on the Parsio API but is not listed in their published reference. |
| Enable Templates | `enableTemplates` | Enables the given Parsio extraction templates so they are used when parsing new documents. |
| Enable Webhooks | `enableWebhooks` | Enables the given Parsio webhooks so Parsio resumes posting events to them. This endpoint is live on the Parsio API but is not listed in their published reference. |
| Get Account Settings | `getAccountSettings` | Returns the Parsio account profile settings: display name, timezone, time format and weekly digest preference. Note that Parsio also returns the account's own API key in this response. This endpoint is live on the Parsio API but is not listed in their published reference. |
| Get Billing Details | `getBillingDetails` | Returns the Parsio account's billing address, saved payment cards and VAT rate. This endpoint is live on the Parsio API but is not listed in their published reference. |
| Get Current User | `getCurrentUser` | Returns the Parsio account the API key belongs to, with its role, verification state and the mailboxes it owns. This endpoint is live on the Parsio API but is not listed in their published reference. |
| Get Document | `getDocument` | Retrieves a parsed Parsio document by id. The response uses the same JSON shape Parsio sends to webhooks, so use it to collect the result of an asynchronous import. |
| Get Mailbox | `getMailbox` | Retrieves one Parsio mailbox by id, with its full parser settings, field configuration and document statistics. |
| Get Parsed Data | `getParsedData` | Returns the extracted data for the documents in a Parsio mailbox, one record per parsed document, optionally limited to a date range. |
| Get Template | `getTemplate` | Retrieves one Parsio extraction template by id, including the fields it extracts and the document it was built from. |
| Get Webhook | `getWebhook` | Retrieves one Parsio webhook by id, with its target URL, subscribed event and enabled state. |
| List Collected Emails | `listCollectedEmails` | Lists the email addresses Parsio has collected from documents received by a mailbox. Only populated when the mailbox has Collect Email Addresses enabled. |
| List Documents | `listDocuments` | Lists the documents in a Parsio mailbox, newest first, with optional filtering by date range, name search and document status. |
| List Mailbox Integrations | `listMailboxIntegrations` | Lists the data-export integrations configured on a Parsio mailbox, such as Google Sheets exports and the Zapier, Make, n8n and Pabbly connections. This endpoint is live on the Parsio API but is not listed in their published reference. |
| List Mailboxes | `listMailboxes` | Lists every Parsio mailbox available to the authenticated account, with each mailbox's parser settings, extracted-field configuration and document statistics. |
| List Table Fields | `listTableFields` | Lists the table fields configured on a Parsio mailbox. Table fields hold repeating rows such as invoice line items, and their ids are what the table.parsed webhook event is bound to. |
| List Templates | `listTemplates` | Lists the extraction templates defined on a Parsio mailbox. Templates map the layout of an incoming document to the fields Parsio extracts. |
| List Webhooks | `listWebhooks` | Lists the webhooks registered on a Parsio mailbox, with the URL and event each one is subscribed to. |
| Reparse Document | `reparseDocument` | Queues a Parsio document to be parsed again, for example after changing the mailbox's templates or extraction fields. |
| Skip Documents | `skipDocuments` | Marks the given Parsio documents as skipped so they are not parsed and do not consume parsing credits. |
| Update Account Settings | `updateAccountSettings` | Updates the Parsio account profile: display name, timezone, time format and weekly digest preference. Parsio answers HTTP 201 for both success and validation failure, so check Is Error in the response. This endpoint is live on the Parsio API but is not listed in their published reference. |
| Update Mailbox | `updateMailbox` | Updates a Parsio mailbox. This is a full replace of the mailbox settings, not a partial patch: any boolean you omit is reset to false, so send every setting you want to keep. Name and Email Prefix are both required. |
| Update Webhook | `updateWebhook` | Updates an existing Parsio webhook: its name, target URL, subscribed event or enabled state. The webhook id goes in the body as Webhook ID, not in the path. Parsio requires Enabled and Table Field ID on every update; send Table Field ID as an empty string unless the event is table.parsed. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Document Parsed | `doc.parsed` | Fires when Parsio finishes extracting data from a document. The payload object carries the extracted fields, nested as the mailbox's template defines them. Envelope captured from a real Parsio delivery; the payload contents are the mailbox's own fields. |
| Document Parsed (Flat) | `doc.parsed.flat` | Same as Document Parsed but the extracted data is flattened to a single level, which suits destinations that cannot handle nested objects. Envelope captured from a real Parsio delivery; the payload contents are the mailbox's own fields. |
| Document Parsing Failed | `doc.fail` | Fires when Parsio could not parse a document, for example when no template matches it. Payload schema captured from a real Parsio delivery. |
| Document Received | `doc.received` | Fires as soon as Parsio accepts a new document into the mailbox, before parsing. Payload schema captured from a real Parsio delivery. |
| Table Rows Parsed | `table.parsed` | Fires once per parsed table field, carrying the extracted rows. Set the Table ID input to the table field this trigger watches, from List Table Fields. Envelope captured from a real Parsio delivery; the payload contents are the table's own rows. |
