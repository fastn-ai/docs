---
description: "Parseur is an AI-powered document parser that extracts structured data from emails, PDFs and spreadsheets."
hidden: true
---

# Parseur

<img src="../../.gitbook/assets/connectors/lg/parseur.png" alt="Parseur logo">

Parseur is an AI-powered document parser that extracts structured data from emails, PDFs and spreadsheets. This connector covers the Parseur REST API: parsers (mailboxes), documents and their processing lifecycle, templates, extraction schemas, export configurations, webhooks, account and subscription details.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [parseur.com](https://parseur.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `parseur` |

## Use it

Add Parseur from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.parseur.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Attach Webhook To Parser | `attachWebhookToParser` | Attaches an existing webhook to a parser so that the parser's documents start firing it. Until a webhook is attached it exists on the account but receives nothing. |
| Copy Document To Parser | `copyDocument` | Starts an asynchronous copy of a document into another parser, where it is queued for parsing against that parser's templates. Returns a notification immediately, not the new document - the copy appears in List Parser Documents for the target parser a few seconds later and consumes a credit. |
| Copy Parser | `copyParser` | Starts an asynchronous copy of a parser, including its fields and templates but not its documents. Returns a notification immediately, not the new parser - the copy appears in List Parsers a few minutes later with its own inbound email address. |
| Copy Template To Parser | `copyTemplate` | Copies a template into another parser. The target parser must already define the fields the template captures. |
| Create Export Config | `createExportConfig` | Creates a custom download on a parser, selecting which columns appear in its CSV and Excel exports. Use type PARSER for a document-level export, or PARSER_FIELD with a Parser Field ID to export the rows of one table field. |
| Create Invitation | `createInvitation` | Invites a person to join the Parseur account by email, which sends them a real invitation email. Requires an identity holding the create_destroy_invitation permission; API-key identities without it are refused with a 400 permission error. This endpoint is live on the Parseur API but is not covered by the published OpenAPI specification. |
| Create Parser | `createParser` | Creates a new parser (mailbox). Only Name is required; Parseur generates the inbound email prefix and applies plan defaults for everything else. Attached webhooks and parser fields are managed by their own actions, not here. |
| Create Template | `createTemplate` | Creates a template on a parser. Parser ID is required - omitting it makes Parseur return a 500 rather than a validation error. Supplying Status also requires all three field-set arrays to be present (send empty arrays for a blank template). Engine OCR is rejected by Parseur with a 500 even when every field it asks for is supplied, so only TXT templates can be created through the API. Template names must be unique within the account; a duplicate is refused with 409. This endpoint is live on the Parseur API but is not covered by the published OpenAPI specification. |
| Create Webhook | `createWebhook` | Creates a webhook that Parseur will POST to when the chosen event fires. Creating it only defines the webhook - attach it to a parser with Attach Webhook To Parser before it receives anything. Always supply a Target URL: Parseur silently substitutes an unrelated default target when the field is omitted. |
| Delete Document | `deleteDocument` | Permanently deletes a document and its parsed result. The credits already consumed by the document are not refunded. |
| Delete Export Config | `deleteExportConfig` | Permanently deletes a custom download from a parser. The parser's documents and standard downloads are unaffected. |
| Delete Parser | `deleteParser` | Starts an asynchronous delete of a parser together with all of its documents, templates and fields. Returns a notification immediately; the parser disappears from List Parsers once the delete completes. This cannot be undone. |
| Delete Template | `deleteTemplate` | Permanently deletes a template. Documents already parsed with it keep their results, but future documents will no longer match it. |
| Delete Webhook | `deleteWebhook` | Permanently deletes a webhook and detaches it from every parser it was attached to. |
| Detach Webhook From Parser | `detachWebhookFromParser` | Detaches a webhook from a parser so the parser's documents stop firing it. The webhook itself is kept on the account - use Delete Webhook to remove it entirely. |
| Get Bootstrap Config | `getBootstrap` | Returns the reference data Parseur's own app loads at start-up: the allowed values for every enumerated field (document statuses, webhook events, template engines, field formats and more) with their human-readable labels. Use it to populate pickers instead of hard-coding enum values. |
| Get Current User | `getCurrentUser` | Returns the user the API token belongs to, together with the accounts they can reach and the current account's plan, billing period and credit allowance. This endpoint is live on the Parseur API but is not covered by the published OpenAPI specification. |
| Get Document | `getDocument` | Returns a single document by id, including its processing status, credit usage, download URLs, extracted text content and parsed samples. |
| Get Document Logs | `getDocumentLogs` | Returns the processing and export log entries recorded for one document, including webhook delivery attempts and their payloads. |
| Get Parser | `getParser` | Returns a single parser (mailbox) by id, including its document counts by status, attached webhooks, available webhooks, tables and the many per-field toggles that control which metadata Parseur exports. |
| Get Parser Schema | `getParserSchema` | Returns a JSON Schema describing the shape of the parsed result this parser produces, derived from its configured fields and tables. Use it to map Parseur output onto downstream systems. |
| Get Subscription | `getSubscription` | Returns the account's paid subscription and billing details. Requires an account on a paid plan with billing permissions; Free-plan tokens are refused. This endpoint is live on the Parseur API but is not covered by the published OpenAPI specification. |
| Get Template | `getTemplate` | Returns a single template by id, including the fields it captures, its static fields, the parser fields it leaves uncaptured and how many documents have matched it. |
| List Documents | `listDocuments` | Returns every document on the account across all parsers, with paging. This endpoint is live on the Parseur API but is not covered by the published OpenAPI specification. |
| List Export Configs | `listExportConfigs` | Returns the custom downloads (export configurations) defined on a parser. Each one selects a subset of fields and exposes its own CSV and Excel download URL. |
| List Invitations | `listInvitations` | Returns the pending invitations to join the Parseur account. Requires an identity holding the create_destroy_invitation permission; API-key identities without it are refused with a 400 permission error. This endpoint is live on the Parseur API but is not covered by the published OpenAPI specification. |
| List Parser Documents | `listParserDocuments` | Returns the documents received by one parser, newest first, with paging and filters for status, received date range, free-text search and ordering. Set With Result to true to include each document's parsed result inline. |
| List Parser Templates | `listParserTemplates` | Returns the templates defined on one parser. Templates tell Parseur where each field sits in an incoming document. |
| List Parsers | `listParsers` | Returns the parsers (mailboxes) on the account with paging, search and ordering. Each entry is a summary: it carries the document counts, attached and available webhooks and the export toggles, but not the parser secret or the unauthenticated download URLs - use Get Parser for those. |
| List Templates | `listTemplates` | Returns every template on the account across all parsers, with paging. This endpoint is live on the Parseur API but is not covered by the published OpenAPI specification. |
| List Webhooks | `listWebhooks` | Returns every webhook defined on the account, whether or not it is attached to a parser. This endpoint is live on the Parseur API but is not covered by the published OpenAPI specification. |
| Reprocess Document | `reprocessDocument` | Queues a document to be parsed again, for example after its template or fields have changed. Returns a notification immediately, not the document - read the document back with Get Document to see the new status and result. Reprocessing may consume another credit. |
| Skip Document | `skipDocument` | Marks a document as SKIPPED so Parseur stops trying to parse it. Use this to clear documents that will never match a template. |
| Update Current User | `updateCurrentUser` | Updates the profile of the user the API token belongs to, and switches which account subsequent API calls act on. Fields left blank are not sent and keep their current value. This endpoint is live on the Parseur API but is not covered by the published OpenAPI specification. |
| Update Export Config | `updateExportConfig` | Updates a custom download on a parser. Fields left blank are not sent and keep their current value. |
| Update Parser | `updateParser` | Updates a parser's settings. Fields left blank are not sent and keep their current value. Attached webhooks and parser fields are managed by their own actions, not here. |
| Update Template | `updateTemplate` | Updates a template. Fields left blank are not sent and keep their current value. Supplying Status also requires all three field-set arrays to be present. This endpoint is live on the Parseur API but is not covered by the published OpenAPI specification. |
| Upload Email Document | `uploadEmailDocument` | Submits an email or text document to Parseur for parsing. Recipient must be the full inbound address of the target parser (its Email Prefix followed by @in.parseur.com). Each accepted document consumes one credit from the account's plan. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Document Export Failed | `document.export_failed` | Fires when Parseur parsed a document but could not deliver it to a configured export destination. Use it to catch broken downstream integrations. Set the Parser ID input to the parser to watch. Payload schema is modelled from the Parseur document object, not captured live. |
| Document Processed | `document.processed` | Fires when Parseur finishes parsing a document and the extracted fields are ready. Set the Parser ID input to the parser (mailbox) whose documents should trigger this. Payload schema is modelled from the Parseur document object; no live delivery was captured because the sandbox account has no parsing credits to spend. |
| Document Processed (Flattened) | `document.processed.flattened` | Same as Document Processed but with nested table data flattened into a single level, which is easier to map into spreadsheet-shaped destinations. Set the Parser ID input to the parser whose documents should trigger this. Payload schema is modelled from the Parseur document object, not captured live. |
| Table Processed | `table.processed` | Fires once per extracted table row rather than once per document, for documents whose template defines a table. Set the Parser ID input to the parser to watch. Payload schema is modelled from the Parseur table row shape, not captured live. |
| Template Needed | `document.template_needed` | Fires when a document arrives that no existing template matches, so a human needs to create one. Use it to alert an operator. Set the Parser ID input to the parser to watch. Payload schema is modelled from the Parseur document object, not captured live. |
