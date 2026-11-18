---
description: "PDFShift is an HTML/URL to PDF, PNG, JPEG, and WEBP conversion API."
hidden: true
---

# PDFShift

<img src="../../.gitbook/assets/connectors/pdfshift.jpg" alt="PDFShift logo" width="64">

PDFShift is an HTML/URL to PDF, PNG, JPEG, and WEBP conversion API. This connector covers document conversion, reusable templates, account and API key management, credit usage, request logs, and invoices.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [pdfshift.io](https://pdfshift.io) |
| **Authentication** | API key |
| **Slug** | `pdfshift` |

## Use it

Add PDFShift from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pdfshift.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert to JPEG | `convertToJpeg` | Converts an HTML document or a URL into a JPEG screenshot. Supports full-page capture, CSS-selector cropping, custom viewport, and DPI scaling. |
| Convert to PDF | `convertToPdf` | Converts an HTML document or a URL into a PDF file. Supports page layout, headers/footers, watermarking, password protection, custom JavaScript/CSS injection, and webhook-based async delivery. |
| Convert to PNG | `convertToPng` | Converts an HTML document or a URL into a PNG screenshot. Supports full-page capture, CSS-selector cropping, custom viewport, and DPI scaling. |
| Convert to WEBP | `convertToWebp` | Converts an HTML document or a URL into a WEBP screenshot. Supports full-page capture, CSS-selector cropping, custom viewport, and DPI scaling. |
| Create API Key | `createApiKey` | Creates a new secondary API key on the authenticated PDFShift account. Requires a master-level API key. Newly created keys have basic-level privileges, not master access. |
| Create Template | `createTemplate` | Creates a reusable HTML template that can later be rendered to HTML, PDF, PNG, JPEG, or WEBP via Generate Document From Template. |
| Delete Template | `deleteTemplate` | Permanently deletes a saved template, identified by its slug. |
| Disable API Key | `disableApiKey` | Disables an existing non-master API key on the account, identified by its secret token. At least one active key must always remain, and master keys can only be disabled from the Dashboard. |
| Enable API Key | `enableApiKey` | Re-enables a previously disabled non-master API key on the account, identified by its secret token. |
| Generate Document From Template | `generateFromTemplate` | Renders a saved template into a final document. The output format is selected by extension: html returns the rendered markup, and pdf, png, jpeg, or webp return the corresponding rendered file. |

<details>

<summary>See 9 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Account Details | `getAccountDetails` | Returns the authenticated PDFShift account's profile, billing plan, and subscription details. |
| Get Credits Usage | `getCreditsUsage` | Returns the current billing period's credit usage for the authenticated PDFShift account, including total, used, remaining, and base credit allowances. |
| Get Log by Request ID | `getLogByRequestId` | Retrieves the full log entry for a single API request, identified by its unique request ID. |
| Get Template HTML | `getTemplateHtml` | Returns the raw HTML markup stored for a template, identified by its slug. |
| List Invoices | `listInvoices` | Lists billing invoices issued for the authenticated PDFShift account. |
| List Recent Logs | `listLogs` | Lists recent API request logs for the authenticated account, with optional filtering by status, API key, and time, and cursor-based pagination. |
| List Templates | `listTemplates` | Lists the reusable templates saved on the authenticated PDFShift account. |
| Update API Key | `updateApiKey` | Renames an existing API key on the account, identified by its secret token. Requires a master-level API key to call. |
| Update Template | `updateTemplate` | Updates the HTML content and optionally the display name of an existing template, identified by its slug. |

</details>
