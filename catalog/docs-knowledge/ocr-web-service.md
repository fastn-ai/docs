---
description: "OCR.space reads text from images and PDFs. Extract text from an uploaded file or a link."
hidden: true
---

# OCR Web Service

<img src="../../.gitbook/assets/connectors/lg/ocr-web-service.png" alt="OCR Web Service logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [ocr.space](https://ocr.space) |
| **Authentication** | API key |
| **Slug** | `ocrWebService` |

## Setup

Your customers enter their API key for OCR Web Service when they connect. Nothing else needs setting up.

## Use it

Add OCR Web Service from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ocrWebService.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Parse Image Or PDF From Base64</td><td><code>parseImageBase64</code></td><td>Runs OCR on an image or PDF supplied inline as a base64 data URI, through Use this for local or private files that have no public URL — nothing has to be hosted anywhere. The value must be a full data URI such as 'data:image/png;base64,iVBORw0KGgo...' or 'data:application/pdf;base64,JVBERi0...'; a bare base64 string without the data: prefix is rejected. Free tier limits: 1 MB decoded file and 3 PDF pages. Each successful call consumes one request from the account quota.</td></tr><tr><td>Parse Image Or PDF From URL (GET)</td><td><code>parseImageUrlGet</code></td><td>Runs OCR on an image or PDF that is reachable at a public URL, using the lightweight GET endpoint Returns the recognised text per page in ParsedResults[].ParsedText, plus optional word-level bounding boxes. Use this when the file is already hosted somewhere public; use Parse Image Or PDF From Base64 for local files. Each successful call consumes one request from the account quota (free tier: 25,000/month, 500/day per IP).</td></tr><tr><td>Parse Image Or PDF From URL (POST)</td><td><code>parseImageByUrl</code></td><td>Runs OCR on an image or PDF hosted at a public URL through the main endpoint. Functionally the same recognition as the GET variant, but the options travel in a JSON body instead of the query string, which avoids URL-length limits on long signed URLs. Set Create Searchable PDF to also receive a SearchablePDFURL download link. Each successful call consumes one request from the account quota.</td></tr></tbody></table>

## Events

OCR Web Service has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
