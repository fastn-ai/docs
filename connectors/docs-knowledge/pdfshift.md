---
description: "PDFShift converts HTML or web pages to PDF and images. Convert pages, generate documents from templates and manage API keys."
hidden: true
---

# PDFShift

<img src="../../.gitbook/assets/connectors/lg/pdfshift.png" alt="PDFShift logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [pdfshift.io](https://pdfshift.io) |
| **Authentication** | API key |
| **Slug** | `pdfshift` |

## Setup

Your customers enter their API key for PDFShift when they connect. Nothing else needs setting up.

## Use it

Add PDFShift from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pdfshift.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Convert to JPEG</td><td><code>convertToJpeg</code></td><td>Converts an HTML document or a URL into a JPEG screenshot. Supports full-page capture, CSS-selector cropping, custom viewport, and DPI scaling.</td></tr><tr><td>Convert to PDF</td><td><code>convertToPdf</code></td><td>Converts an HTML document or a URL into a PDF file. Supports page layout, headers/footers, watermarking, password protection, custom JavaScript/CSS injection, and webhook-based async delivery.</td></tr><tr><td>Convert to PNG</td><td><code>convertToPng</code></td><td>Converts an HTML document or a URL into a PNG screenshot. Supports full-page capture, CSS-selector cropping, custom viewport, and DPI scaling.</td></tr><tr><td>Convert to WEBP</td><td><code>convertToWebp</code></td><td>Converts an HTML document or a URL into a WEBP screenshot. Supports full-page capture, CSS-selector cropping, custom viewport, and DPI scaling.</td></tr><tr><td>Create API Key</td><td><code>createApiKey</code></td><td>Creates a new secondary API key on the authenticated PDFShift account. Requires a master-level API key. Newly created keys have basic-level privileges, not master access.</td></tr><tr><td>Create Template</td><td><code>createTemplate</code></td><td>Creates a reusable HTML template that can later be rendered to HTML, PDF, PNG, JPEG, or WEBP via Generate Document From Template.</td></tr><tr><td>Delete Template</td><td><code>deleteTemplate</code></td><td>Permanently deletes a saved template, identified by its slug.</td></tr><tr><td>Disable API Key</td><td><code>disableApiKey</code></td><td>Disables an existing non-master API key on the account, identified by its secret token. At least one active key must always remain, and master keys can only be disabled from the Dashboard.</td></tr><tr><td>Enable API Key</td><td><code>enableApiKey</code></td><td>Re-enables a previously disabled non-master API key on the account, identified by its secret token.</td></tr><tr><td>Generate Document From Template</td><td><code>generateFromTemplate</code></td><td>Renders a saved template into a final document. The output format is selected by extension: html returns the rendered markup, and pdf, png, jpeg, or webp return the corresponding rendered file.</td></tr></tbody></table>

<details>

<summary>View 9 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Account Details</td><td><code>getAccountDetails</code></td><td>Returns the authenticated PDFShift account's profile, billing plan, and subscription details.</td></tr><tr><td>Get Credits Usage</td><td><code>getCreditsUsage</code></td><td>Returns the current billing period's credit usage for the authenticated PDFShift account, including total, used, remaining, and base credit allowances.</td></tr><tr><td>Get Log by Request ID</td><td><code>getLogByRequestId</code></td><td>Retrieves the full log entry for a single API request, identified by its unique request ID.</td></tr><tr><td>Get Template HTML</td><td><code>getTemplateHtml</code></td><td>Returns the raw HTML markup stored for a template, identified by its slug.</td></tr><tr><td>List Invoices</td><td><code>listInvoices</code></td><td>Lists billing invoices issued for the authenticated PDFShift account.</td></tr><tr><td>List Recent Logs</td><td><code>listLogs</code></td><td>Lists recent API request logs for the authenticated account, with optional filtering by status, API key, and time, and cursor-based pagination.</td></tr><tr><td>List Templates</td><td><code>listTemplates</code></td><td>Lists the reusable templates saved on the authenticated PDFShift account.</td></tr><tr><td>Update API Key</td><td><code>updateApiKey</code></td><td>Renames an existing API key on the account, identified by its secret token. Requires a master-level API key to call.</td></tr><tr><td>Update Template</td><td><code>updateTemplate</code></td><td>Updates the HTML content and optionally the display name of an existing template, identified by its slug.</td></tr></tbody></table>

</details>

## Events

PDFShift has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
