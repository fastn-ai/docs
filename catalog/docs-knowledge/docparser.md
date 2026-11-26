---
description: "Docparser extracts data from PDFs and scanned documents. Upload documents, check parsing status and read the results."
hidden: true
---

# Docparser

<img src="../../.gitbook/assets/connectors/lg/docparser.png" alt="Docparser logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [docparser.com](https://docparser.com) |
| **Authentication** | Username and password |
| **Slug** | `docparser` |

## Setup

Your customers enter their username and password for Docparser when they connect. Nothing else needs setting up.

## Use it

Add Docparser from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.docparser.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Fetch Document From URL</td><td><code>fetchDocumentFromUrl</code></td><td>Imports a document into a Document Parser by giving Docparser a publicly accessible URL to fetch it from. The fetch is asynchronous: Docparser schedules the download and returns immediately with the document identifier, so poll Get Document Status to know when it has finished importing and parsing.</td></tr><tr><td>Get Document Data</td><td><code>getDocumentData</code></td><td>Returns the parsed data extracted from one document, keyed by the field names configured on the Document Parser. For a steady stream of results Docparser recommends its webhook integration over polling this endpoint. Rate limited to 60 calls per minute.</td></tr><tr><td>Get Document Status</td><td><code>getDocumentStatus</code></td><td>Returns the full processing state of one document: whether it is still importing, being processed or dispatching webhooks, the timestamps for each stage, and any jobs that failed. Poll this after importing a document to know when its parsed data is ready.</td></tr><tr><td>List Document Parsers</td><td><code>listParsers</code></td><td>Returns every Document Parser linked to the account, each with its identifier and label. The identifier is what every other action in this connector needs. Document Parsers themselves can only be created in the Docparser web app; there is no API to create one.</td></tr><tr><td>List Parser Model Layouts</td><td><code>listParserModels</code></td><td>Returns every Model Layout configured on one Document Parser. Layouts are the templates Docparser matches an incoming document against to decide how to extract its fields.</td></tr><tr><td>List Parser Results</td><td><code>listParserResults</code></td><td>Returns the parsed data for many documents on one Document Parser - by default the last 100 uploaded, newest first. Use the list mode together with a date to pull everything imported or parsed after a point in time, which is the usual way to sync incrementally. Rate limited to 30 calls per minute, and capped at 10,000 documents.</td></tr><tr><td>Ping API</td><td><code>pingApi</code></td><td>Verifies that the configured Docparser API key is valid by pinging the API. Returns the message 'pong' on success. This is the check Docparser documents for confirming authentication.</td></tr><tr><td>Re-Integrate Documents</td><td><code>reintegrateDocuments</code></td><td>Puts documents back on the integration queue so their parsed data is pushed again to the downstream integrations and webhooks configured on the Document Parser. Use it to replay deliveries that failed. Docparser expects repeated document_ids[] form fields, and Fastn can only send one value per request, so call this once per document.</td></tr><tr><td>Re-Parse Documents</td><td><code>reparseDocuments</code></td><td>Schedules documents to be parsed again, which is what you want after changing the parsing rules on a Document Parser so existing documents pick up the new rules. Docparser expects repeated document_ids[] form fields, and Fastn can only send one value per request, so call this once per document.</td></tr><tr><td>Upload Document</td><td><code>uploadDocument</code></td><td>Imports a document into a Document Parser by sending its contents Base64-encoded, and returns the new document identifier plus the account's parsing quota. Use this for documents you hold in memory; use Fetch Document From URL when the file is already reachable at a public URL. Binary files must be Base64-encoded by the caller before being passed in.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Document Parsed</td><td><code>document.parsed</code></td><td>Fires when Docparser finishes parsing a document, pushing that document's extracted data to your URL. REGISTRATION IS MANUAL - Docparser has no webhook API, so the Fastn trigger URL must be pasted into the Docparser app by hand, once per Document Parser. Click path: log in to app.docparser.com, open the Document Parser you want events from, go to Integrations in the left-hand menu, choose Advanced Webhook, click Add New Integration (or Connect), paste the Fastn trigger URL into the Target URL / Webhook URL field, leave the method as POST, save, then send a test document through the parser to confirm delivery. Repeat for every Document Parser, because the webhook is configured per parser and not per account. The payload is the parsed document data: the fixed fields below plus one property per field configured on that Document Parser, so the exact shape differs per parser.</td></tr></tbody></table>
