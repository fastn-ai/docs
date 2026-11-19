---
description: "PDF Munk creates and edits PDFs and images. Generate PDFs from HTML or a web page, render charts, compress files and add watermarks."
hidden: true
---

# PDF Munk

<img src="../../.gitbook/assets/connectors/lg/pdf-munk.png" alt="PDF Munk logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [pdfmunk.com](https://pdfmunk.com) |
| **Authentication** | API key |
| **Slug** | `pdfMunk` |

## Setup

Your customers enter their API key for PDF Munk when they connect. Nothing else needs setting up.

## Use it

Add PDF Munk from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pdfMunk.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Watermark To PDF</td><td><code>addWatermark</code></td><td>Stamp a text watermark across every page of a PDF supplied as a URL or a base64 string. The endpoint responds with the watermarked PDF bytes directly (Content-Type application/pdf), not with a JSON link. Undocumented endpoint, verified live against the production API.</td></tr><tr><td>Compress Image</td><td><code>compressImage</code></td><td>Compress a JPEG or PNG image supplied as a URL or as a base64 string, with an adjustable quality level. Maximum input size is 3 MB. Returns the compressed image as a hosted URL or base64 together with original and compressed sizes and the percentage saved.</td></tr><tr><td>Compress PDF</td><td><code>compressPdf</code></td><td>Reduce the file size of a PDF supplied as a URL or a base64 string. The endpoint responds with the compressed PDF bytes directly (Content-Type application/pdf), not with a JSON link. Undocumented endpoint, verified live against the production API.</td></tr><tr><td>Create Template</td><td><code>createTemplate</code></td><td>Save a reusable HTML template that Generate PDF can render later by template_id. Placeholders written as double-brace tokens are filled from default_params or from the dynamic_params passed at render time. Returns the new template_id. Undocumented endpoint, verified live against the production API.</td></tr><tr><td>Delete Template</td><td><code>deleteTemplate</code></td><td>Permanently delete a saved template by id. Returns deleted true with the id that was removed. Undocumented endpoint, verified live against the production API.</td></tr><tr><td>Fetch Rendered HTML From URL</td><td><code>urlToHtml</code></td><td>Load a webpage in a real browser and return its fully rendered HTML. Supports a navigation wait condition, a CSS selector to wait for, extra wait time, viewport size, a custom user agent and custom request headers. Returns the HTML string with the resolved URL and a fetch timestamp.</td></tr><tr><td>Generate Chart</td><td><code>generateChart</code></td><td>Render a Chart.js chart as a PNG image. Supply the chart type, a Chart.js data object with labels and datasets, and optional Chart.js options. Returns a hosted chart_url and/or a base64 chart image.</td></tr><tr><td>Generate Image</td><td><code>generateImage</code></td><td>Render a PNG image from raw HTML/CSS or by screenshotting a live URL. Provide either html_content or url (not both). Returns a hosted image_url and/or a base64 image depending on output_format, plus file size, deletion date, request id and execution time.</td></tr><tr><td>Generate PDF</td><td><code>generatePdf</code></td><td>Create a PDF from raw HTML/CSS, from a live URL, or from a saved PDF Munk template. Supports paper size, orientation, custom paper dimensions, viewport, Google Fonts and dynamic placeholder substitution. Returns a hosted pdf_url plus file size and deletion date.</td></tr><tr><td>Get PDF Info</td><td><code>getPdfInfo</code></td><td>Inspect a PDF and return its page count, file size, encryption state and document metadata. Supply the PDF as a URL or as a base64 string. Undocumented endpoint, verified live against the production API.</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Template</td><td><code>getTemplate</code></td><td>Retrieve one saved template in full, including its html_content and css_content. SECURITY WARNING: the PDF Munk API currently echoes the account's own live API key back in the api_key field of this response. Do not log, store or forward the raw response, and strip api_key before passing it anywhere. Use List Templates instead where the body is not needed. Undocumented endpoint, verified live against the production API.</td></tr><tr><td>List Templates</td><td><code>listTemplates</code></td><td>List every reusable HTML template saved on the account, with its id, name, default parameters, metadata and timestamps. Undocumented endpoint, verified live against the production API.</td></tr><tr><td>Lock PDF With Password</td><td><code>lockPdf</code></td><td>Apply password protection to a PDF supplied as a URL or a base64 string. The endpoint responds with the encrypted PDF bytes directly (Content-Type application/pdf), not with a JSON link. Undocumented endpoint, verified live against the production API.</td></tr><tr><td>Merge PDFs</td><td><code>mergePdfs</code></td><td>Merge between 2 and 15 PDFs, given as publicly reachable URLs, into a single document in the order supplied. Limits are 200 pages per input PDF and 500 pages combined. Returns the hosted merged_pdf_url with the total page and input counts.</td></tr><tr><td>Replace Template</td><td><code>replaceTemplate</code></td><td>Replace a saved template in full with new name, HTML, CSS, default parameters and metadata. Use Update Template Fields when only some fields should change. Undocumented endpoint, verified live against the production API.</td></tr><tr><td>Split PDF</td><td><code>splitPdf</code></td><td>Extract a page range from a PDF into a new document. The pages value accepts a single page (3), a range (1-5), several ranges (1-3,5,7-10) or an open-ended range (10-). Maximum 200 pages per PDF. Returns split_urls, an array of hosted PDFs, plus a split_zip_url containing all of them and the list of pages selected.</td></tr><tr><td>Unlock PDF</td><td><code>unlockPdf</code></td><td>Remove password protection from a PDF, given the PDF as a URL or a base64 string together with its user or owner password. Maximum input size is 10 MB. Returns the unlocked PDF as a hosted link or as PDF bytes.</td></tr><tr><td>Update Template Fields</td><td><code>updateTemplate</code></td><td>Partially update a saved template. Only the fields supplied are changed; every other field, including default_params and metadata, is preserved. Undocumented endpoint, verified live against the production API.</td></tr></tbody></table>

</details>

## Events

PDF Munk has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
