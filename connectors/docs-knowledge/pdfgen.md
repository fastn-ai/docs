---
description: "PDFgen generates pixel-perfect PDFs from saved Handlebars templates, raw HTML, Markdown, or an AI prompt through a single REST call."
hidden: true
---

# PDFgen

<img src="../../.gitbook/assets/connectors/lg/pdfgen.png" alt="PDFgen logo">

PDFgen generates pixel-perfect PDFs from saved Handlebars templates, raw HTML, Markdown, or an AI prompt through a single REST call. This connector covers the full v1 API: PDF generation, template CRUD, account/quota lookup and usage logs.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [pdfgen.com](https://pdfgen.com) |
| **Authentication** | API key |
| **Slug** | `pdfgen` |

## Use it

Add PDFgen from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pdfgen.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Service Health | `checkServiceHealth` | Checks whether the PDFgen service and its database are reachable. Returns an overall status, the database status and the server time. This endpoint is undocumented and requires no API key; use it for uptime monitoring before submitting a generation job. |
| Create PDF From Template (Legacy) | `createPdfFromTemplateLegacy` | Legacy endpoint POST /api/v1/create that renders a saved template and forwards to the current generate endpoint. Kept for compatibility with older PDFgen integrations - prefer Generate PDF for new work. METERED: successful generations consume PDF credits at 1 credit per 5 pages. |
| Create Template | `createTemplate` | Returns 201 with the new template id, which you pass as template_id to Generate PDF. Creating templates does not count against your PDF quota. |
| Delete Template | `deleteTemplate` | Permanently deletes a saved PDF template by id and returns a confirmation of the form { data: { id, deleted: true } }. This cannot be undone and any integration still passing that template_id to Generate PDF will start receiving 404 not_found. Does not count against your PDF quota. |
| Generate PDF | `generatePdf` | Renders a PDF from exactly one source: a saved template (template_id), raw HTML (html), Markdown (markdown), or a plain-English AI prompt (prompt). With export_type "url" the response is { url } - a link to the rendered PDF. With export_type "file" (the API default) the PDF binary is returned and this connector surfaces it as { name, mime, size, data } where data is base64. METERED: successful generations cost credits at 1 credit per 5 pages, doubled for the prompt source; check Get Account for remaining quota first. SECURITY: the returned URL is an object in a public Amazon S3 bucket - it is readable by anyone with the path even after the signature expires, so treat it as a public link. |
| Get Account | `getAccount` | Returns the PDFgen account behind the API key, including the user id and email, the organization, the current plan and the monthly PDF credit usage (used vs limit). Useful for verifying a connection and for checking remaining quota before generating PDFs. Does not count against the PDF quota. |
| Get Template | `getTemplate` | Retrieves one saved PDF template by id, including its full HTML content and templating engine. Templates are scoped to your account; a template you do not own returns 404 not_found. Reading templates does not count against your PDF quota. |
| Get Usage Log Entry | `getUsageLogEntry` | Retrieves a single PDFgen usage log entry by its id, as returned by List Usage Logs. The detail view is richer than the list row: it adds the organization and user ids, the caller's IP address and user agent, and requestParams - a verbatim copy of the JSON body that was sent. Note that requestParams therefore stores whatever the original call contained, so treat it as sensitive. This route is undocumented but live; an unknown id returns 404 not_found. |
| List Templates | `listTemplates` | Lists the saved PDF templates in your PDFgen account, newest first, with paging. Each row carries the template id, name, templating engine and timestamps but not the HTML content - use Get Template for that. Template management does not count against your PDF quota. |
| List Usage Logs | `listUsageLogs` | Lists recent PDFgen API calls made with your key, newest first, with paging. Each entry records the endpoint, HTTP method, status code, duration, whether the call was billed and the template used. Useful for debugging and for auditing credit spend. Reading logs does not count against your PDF quota. |

<details>

<summary>See 3 more actions</summary>

* **Render PDF From HTML (Legacy)** `renderPdfFromHtmlLegacy`: Legacy endpoint POST /api/v1/render that renders raw HTML and forwards to the current generate endpoint. Kept for compatibility with older PDFgen integrations - prefer Generate PDF for new work. METERED: successful generations consume PDF credits at 1 credit per 5 pages.
* **Replace Template** `replaceTemplate`: Replaces a saved PDF template using HTTP PUT. Accepts any of name, content and engine, and returns the updated template. Use Update Template if you prefer PATCH semantics. Templates are scoped to your account; an unknown id returns 404 not_found. Does not count against your PDF quota.
* **Update Template** `updateTemplate`: Partially updates a saved PDF template using HTTP PATCH. Send only the fields you want to change - any of name, content and engine - and the updated template is returned. Templates are scoped to your account; an unknown id returns 404 not_found. Does not count against your PDF quota.

</details>
