---
description: "OCR Web Service (OCR.space) converts images and PDFs into machine-readable text."
hidden: true
---

# OCR Web Service

<img src="../../.gitbook/assets/connectors/lg/ocr-web-service.png" alt="OCR Web Service logo">

OCR Web Service (OCR.space) converts images and PDFs into machine-readable text. This connector wraps the complete OCR.space OCR API surface — the two endpoints the service exposes, GET /parse/imageurl and POST /parse/image — as typed actions: parse an image or PDF from a public URL, parse a base64-encoded image or PDF, extract tabular layout, and produce a searchable PDF with an embedded text layer. Every documented option is exposed: OCR engine 1/2/3, 28 recognition languages plus auto-detect, word-level text overlay coordinates, orientation detection, image upscaling, table mode and file-type override.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [ocr.space](https://ocr.space) |
| **Authentication** | Credentials you enter |
| **Slug** | `ocrWebService` |

## Use it

Add OCR Web Service from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ocrWebService.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Parse Image Or PDF From Base64 | `parseImageBase64` | Runs OCR on an image or PDF supplied inline as a base64 data URI, through POST /parse/image. Use this for local or private files that have no public URL — nothing has to be hosted anywhere. The value must be a full data URI such as 'data:image/png;base64,iVBORw0KGgo...' or 'data:application/pdf;base64,JVBERi0...'; a bare base64 string without the data: prefix is rejected. Free tier limits: 1 MB decoded file and 3 PDF pages. Each successful call consumes one request from the account quota. |
| Parse Image Or PDF From URL (GET) | `parseImageUrlGet` | Runs OCR on an image or PDF that is reachable at a public URL, using the lightweight GET endpoint (GET /parse/imageurl). Returns the recognised text per page in ParsedResults[].ParsedText, plus optional word-level bounding boxes. Use this when the file is already hosted somewhere public; use Parse Image Or PDF From Base64 for local files. Each successful call consumes one request from the account quota (free tier: 25,000/month, 500/day per IP). |
| Parse Image Or PDF From URL (POST) | `parseImageByUrl` | Runs OCR on an image or PDF hosted at a public URL through the main POST /parse/image endpoint. Functionally the same recognition as the GET variant, but the options travel in a JSON body instead of the query string, which avoids URL-length limits on long signed URLs. Set Create Searchable PDF to also receive a SearchablePDFURL download link. Each successful call consumes one request from the account quota. |
