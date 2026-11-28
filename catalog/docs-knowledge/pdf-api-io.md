---
description: "PDF-API.io generates PDFs from templates. List templates, render a template with your data, and merge templates into one PDF."
hidden: true
---

# PDF-API.io

<img src="../../.gitbook/assets/connectors/lg/pdf-api-io.png" alt="PDF-API.io logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [pdf-api.io](https://pdf-api.io) |
| **Authentication** | API key |
| **Slug** | `pdfApiIo` |

## Setup

Your customers enter their API key for PDF-API.io when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect PDF-API.io from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **PDF-API.io**.
2. Select **Connect** on the PDF-API.io card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use PDF-API.io's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Template</td><td><code>getTemplate</code></td><td>Retrieves a single PDF template from your PDF-API.io account by its identifier. Returns the template's id, name and the placeholder variables it defines. Find the identifier with List Templates or on the template index page of the PDF-API.io web app.</td></tr><tr><td>List Templates</td><td><code>listTemplates</code></td><td>Lists every PDF template in your PDF-API.io account. Returns an array of templates, each with its identifier and name. Use the returned id with Get Template, Render Template To PDF or Merge Templates. Templates themselves are authored in the PDF-API.io web editors; the API is read-only for templates.</td></tr><tr><td>Merge Templates</td><td><code>mergeTemplates</code></td><td>Generates a single PDF document by rendering several PDF-API.io templates with their own data and concatenating them in the order supplied. Returns a JSON envelope {status, data}: when output is 'pdf' (the default) the data field holds the merged PDF base64-encoded; when output is 'url' it holds a temporary download URL valid for 15 minutes. This call consumes your plan's PDF generation quota.</td></tr><tr><td>Render Template To PDF</td><td><code>renderTemplateToPdf</code></td><td>Generates a PDF document from one of your PDF-API.io templates, substituting the supplied data into the template's placeholders. Returns a JSON envelope {status, data}: when output is 'pdf' (the default) the data field holds the PDF file base64-encoded; when output is 'url' the data field holds a temporary download URL that expires after 15 minutes, after which the file is deleted from PDF-API.io's servers. This call consumes your plan's PDF generation quota.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>PDF Created</td><td><code>pdf.created</code></td><td>Fires when a new PDF is generated from one of your templates. REGISTRATION IS MANUAL - PDF-API.io exposes no webhook API, so the endpoint must be registered in the web app: sign in at https://pdf-api.io/en/login, open the Webhooks page, choose Create, set Event to 'pdf.created', paste this trigger's URL into the URL field, optionally pick a single Template to scope the notifications to one template, and save. Delete the same entry on that page to stop delivery. PDF-API.io retries a failing endpoint up to 3 times with exponential backoff.</td></tr></tbody></table>
