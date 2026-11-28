---
description: "Pdfless generates PDFs from HTML templates and your data. Generate PDFs and list document templates."
hidden: true
---

# Pdfless

<img src="../../.gitbook/assets/connectors/lg/pdfless.png" alt="Pdfless logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [pdfless.com](https://pdfless.com) |
| **Authentication** | API key |
| **Slug** | `pdfless` |

## Setup

Your customers enter their API key for Pdfless when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Pdfless from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Pdfless**.
2. Select **Connect** on the Pdfless card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Pdfless's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate PDF</td><td><code>generatePdf</code></td><td>Generate a PDF document from a Pdfless document template, merging in the supplied JSON payload, and optionally encrypt it and restrict what readers may do with it. Returns data.download_url, a temporary pre-signed link to the generated PDF that expires about 10 minutes after creation (data.expires). SECURITY: that download_url is unauthenticated - anyone holding it can fetch the document until it expires - so do not log, store or forward the response outside your system. Each successful call consumes one PDF from the workspace quota (see Get Workspace).</td></tr><tr><td>Get Workspace</td><td><code>getWorkspace</code></td><td>Retrieve the Pdfless workspace that the API key belongs to, including its name, active flag, creation and modification timestamps, and its PDF generation quota. This is also the quota/credit endpoint: 'quota' is the total number of PDFs the plan allows and 'remainingQuota' is how many PDF generations are still available. Call it before Generate PDF to check the remaining balance.</td></tr><tr><td>List Document Templates</td><td><code>listDocumentTemplates</code></td><td>List the HTML/CSS document templates available in the Pdfless workspace, with optional paging. Each template's id is the value passed as template_id to Generate PDF. Templates are authored in the Pdfless web app (app.pdfless.com); the public API has no route to create, update or delete them, so this action is read-only.</td></tr></tbody></table>

