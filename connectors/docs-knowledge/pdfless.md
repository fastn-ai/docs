---
description: "Pdfless generates PDF documents from HTML/CSS templates designed in the Pdfless web app, merged with JSON payload data."
hidden: true
---

# Pdfless

<img src="../../.gitbook/assets/connectors/lg/pdfless.png" alt="Pdfless logo">

This connector wraps the public Pdfless REST API v1 (https://api.pdfless.com/v1): list the workspace's document templates, read the workspace's PDF generation quota, and generate a PDF from a template with optional encryption and permission settings.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [pdfless.com](https://pdfless.com) |
| **Authentication** | API key |
| **Slug** | `pdfless` |

## Use it

Add Pdfless from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pdfless.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate PDF</td><td><code>generatePdf</code></td><td>Generate a PDF document from a Pdfless document template, merging in the supplied JSON payload, and optionally encrypt it and restrict what readers may do with it. Returns data.download_url, a temporary pre-signed link to the generated PDF that expires about 10 minutes after creation (data.expires). SECURITY: that download_url is unauthenticated - anyone holding it can fetch the document until it expires - so do not log, store or forward the response outside your system. Each successful call consumes one PDF from the workspace quota (see Get Workspace).</td></tr><tr><td>Get Workspace</td><td><code>getWorkspace</code></td><td>Retrieve the Pdfless workspace that the API key belongs to, including its name, active flag, creation and modification timestamps, and its PDF generation quota. This is also the quota/credit endpoint: 'quota' is the total number of PDFs the plan allows and 'remainingQuota' is how many PDF generations are still available. Call it before Generate PDF to check the remaining balance.</td></tr><tr><td>List Document Templates</td><td><code>listDocumentTemplates</code></td><td>List the HTML/CSS document templates available in the Pdfless workspace, with optional paging. Each template's id is the value passed as template_id to Generate PDF. Templates are authored in the Pdfless web app (app.pdfless.com); the public API has no route to create, update or delete them, so this action is read-only.</td></tr></tbody></table>
