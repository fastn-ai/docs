---
description: "PDFgen generates PDFs from templates, HTML or Markdown. Generate PDFs, manage templates and review usage logs."
hidden: true
---

# PDFgen

<img src="../../.gitbook/assets/connectors/lg/pdfgen.png" alt="PDFgen logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [pdfgen.com](https://pdfgen.com) |
| **Authentication** | API key |
| **Slug** | `pdfgen` |

## Setup

Your customers enter their API key for PDFgen when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect PDFgen from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **PDFgen**.
2. Select **Connect** on the PDFgen card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use PDFgen's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check Service Health</td><td><code>checkServiceHealth</code></td><td>Checks whether the PDFgen service and its database are reachable. Returns an overall status, the database status and the server time. This endpoint is undocumented and requires no API key; use it for uptime monitoring before submitting a generation job.</td></tr><tr><td>Create PDF From Template (Legacy)</td><td><code>createPdfFromTemplateLegacy</code></td><td>Legacy endpoint that renders a saved template and forwards to the current generate endpoint. Kept for compatibility with older PDFgen integrations - prefer Generate PDF for new work. METERED: successful generations consume PDF credits at 1 credit per 5 pages.</td></tr><tr><td>Create Template</td><td><code>createTemplate</code></td><td>Creating templates does not count against your PDF quota.</td></tr><tr><td>Delete Template</td><td><code>deleteTemplate</code></td><td>Permanently deletes a saved PDF template by id and returns a confirmation of the form { data: { id, deleted: true } }. This cannot be undone and any integration still passing that template_id to Generate PDF will start receiving 404 not_found. Does not count against your PDF quota.</td></tr><tr><td>Generate PDF</td><td><code>generatePdf</code></td><td>Renders a PDF from exactly one source: a saved template (template_id), raw HTML (html), Markdown (markdown), or a plain-English AI prompt (prompt). With export_type "url" the response is { url } - a link to the rendered PDF. With export_type "file" (the API default) the PDF binary is returned and this connector surfaces it as { name, mime, size, data } where data is base64. METERED: successful generations cost credits at 1 credit per 5 pages, doubled for the prompt source; check Get Account for remaining quota first. SECURITY: the returned URL is an object in a public Amazon S3 bucket - it is readable by anyone with the path even after the signature expires, so treat it as a public link.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Returns the PDFgen account behind the API key, including the user id and email, the organization, the current plan and the monthly PDF credit usage (used vs limit). Useful for verifying a connection and for checking remaining quota before generating PDFs. Does not count against the PDF quota.</td></tr><tr><td>Get Template</td><td><code>getTemplate</code></td><td>Retrieves one saved PDF template by id, including its full HTML content and templating engine. Templates are scoped to your account; a template you do not own Reading templates does not count against your PDF quota.</td></tr><tr><td>Get Usage Log Entry</td><td><code>getUsageLogEntry</code></td><td>Retrieves a single PDFgen usage log entry by its id, as returned by List Usage Logs. The detail view is richer than the list row: it adds the organization and user ids, the caller's IP address and user agent, and requestParams - a verbatim copy of the JSON body that was sent. Note that requestParams therefore stores whatever the original call contained, so treat it as sensitive. This route is undocumented but live; an unknown id</td></tr><tr><td>List Templates</td><td><code>listTemplates</code></td><td>Lists the saved PDF templates in your PDFgen account, newest first, with paging. Each row carries the template id, name, templating engine and timestamps but not the HTML content - use Get Template for that. Template management does not count against your PDF quota.</td></tr><tr><td>List Usage Logs</td><td><code>listUsageLogs</code></td><td>Lists recent PDFgen API calls made with your key, newest first, with paging. Each entry records the endpoint, HTTP method, status code, duration, whether the call was billed and the template used. Useful for debugging and for auditing credit spend. Reading logs does not count against your PDF quota.</td></tr></tbody></table>

<details>

<summary>View 3 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Render PDF From HTML (Legacy)</td><td><code>renderPdfFromHtmlLegacy</code></td><td>Legacy endpoint that renders raw HTML and forwards to the current generate endpoint. Kept for compatibility with older PDFgen integrations - prefer Generate PDF for new work. METERED: successful generations consume PDF credits at 1 credit per 5 pages.</td></tr><tr><td>Replace Template</td><td><code>replaceTemplate</code></td><td>Replaces a saved PDF template using HTTP PUT. Accepts any of name, content and engine, and returns the updated template. Use Update Template if you prefer PATCH semantics. Templates are scoped to your account; an unknown id Does not count against your PDF quota.</td></tr><tr><td>Update Template</td><td><code>updateTemplate</code></td><td>Partially updates a saved PDF template using HTTP PATCH. Send only the fields you want to change - any of name, content and engine - and the updated template is returned. Templates are scoped to your account; an unknown id Does not count against your PDF quota.</td></tr></tbody></table>

</details>

