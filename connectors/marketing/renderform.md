---
description: "RenderForm generates images, PDFs and videos from reusable templates."
hidden: true
---

# RenderForm

<img src="../../.gitbook/assets/connectors/renderform.png" alt="RenderForm logo" width="64">

RenderForm generates images, PDFs and videos from reusable templates. This connector covers the full v1 and v2 REST surface: template CRUD and HTML content, single and batch rendering, screenshots, URL-to-PDF, render results, uploads, tags, fonts, organization settings, credit usage and webhook registration.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [renderform.io](https://renderform.io) |
| **Authentication** | API key |
| **Slug** | `renderform` |

## Use it

Add RenderForm from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.renderform.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Browse Public Template Gallery | `browsePublicTemplateGallery` | Returns RenderForm's public gallery of ready-made starter templates, with category, editor, dimensions and preview image. Pass a gallery template's identifier to Duplicate Template to copy one into your own account. This legacy route always returns the whole gallery in one array: it accepts no paging parameters and silently ignores page and size if sent. |
| Capture Website Screenshot | `captureWebsiteScreenshot` | Takes a screenshot of any public website at the given viewport size and stores it, returning the image URL. Consumes a render credit. Never point this at an internal or credential-echoing host. |
| Convert Website To PDF | `convertWebsiteToPdf` | Renders any public web page to a PDF in the chosen paper format and returns the file URL. Optionally sets an automatic expiry after which RenderForm deletes the PDF. Consumes a render credit. |
| Create Image From Template | `createImageFromTemplate` | Renders a template through the legacy v1 images route, an alias of the v1 render route kept for older Zapier and Make scenarios. Returns the output URL. |
| Create Legacy Template | `createLegacyTemplate` | Creates a template through the legacy v1 endpoint, which returns the full template record including its raw config, options and sampleData JSON strings. Prefer Create Template unless you need those legacy fields. |
| Create Template | `createTemplate` | Creates a new empty RenderForm template with the given name, canvas size and editor. Tags are created automatically if they do not exist. Returns the new template including its identifier, which is used for rendering. |
| Create Webhook | `createWebhook` | Registers a global webhook that RenderForm calls when the chosen action occurs. One webhook carries exactly one action. The destination must be a publicly reachable https URL; RenderForm rejects placeholder domains with 'This URL is not allowed'. |
| Delete Legacy Template | `deleteLegacyTemplate` | Permanently deletes a template through the legacy v1 endpoint. Equivalent to Delete Template but on the v1 route. |
| Delete Render Request | `deleteRenderRequest` | Deletes a render request and its stored output through the legacy v1 route. Equivalent to Delete Render Result on the v2 route. |
| Delete Render Result | `deleteRenderResult` | Permanently deletes a rendered file and its result record by request identifier. Use it to remove output from the public CDN once it is no longer needed. |

<details>

<summary>See 34 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Template | `deleteTemplate` | Permanently deletes a template by its identifier. Renders already produced from the template are not removed. Returns an empty body on success. |
| Delete Template Tag | `deleteTemplateTag` | Removes a tag from the account, detaching it from every template that carries it. The templates themselves are not deleted. |
| Delete Uploaded File | `deleteUploadedFile` | Deletes a file from the upload library by its upload id, which is the UUID segment of the file's fileKey (organisation/uploads/UUID/filename). VENDOR DEFECT: this route is currently broken and answers 500 'Unexpected error' for every identifier, including ids that definitely exist and ids that definitely do not, so uploaded files cannot be removed through the API at present. Verified against the vendor directly, outside fastn. Files must be deleted from the RenderForm web app until the vendor fixes it. |
| Delete Webhook | `deleteWebhook` | Removes a registered global webhook by its identifier so RenderForm stops calling that destination. IMPORTANT: webhook identifiers are not stable. RenderForm reissues a fresh id for every webhook whenever the webhook collection changes, so an id captured before an unrelated create or delete will no longer resolve. Always call List Webhooks immediately before this action and use the id from that response. |
| Duplicate Template | `duplicateTemplate` | Copies an existing template into the account under the name of the original with ' (copy)' appended, and returns the new template. Works on your own templates and on public gallery templates. |
| Get Credit Usage | `getCreditUsage` | Returns the organization's current credit usage, upload storage usage and subscription plan details. Call this before running renders to check how many render credits remain. |
| Get Daily Usage History | `getDailyUsageHistory` | Returns a day-by-day series of render credits consumed by the organization over the recent billing window. Use it to chart consumption or spot usage spikes. |
| Get Legacy Template | `getLegacyTemplate` | Returns a template through the legacy v1 endpoint, including the raw canvas config, editor options and sample data. Works for both your own templates and public gallery templates. |
| Get Organization Settings | `getOrganizationSettings` | Returns the RenderForm organization profile: name, plan, request and template quotas, upload storage limits and billing currency. SECURITY WARNING: this endpoint also returns the organization's own API keys in plaintext in the apiKeys array, so treat its response as a secret and do not log or forward it. |
| Get Render Result | `getRenderResult` | Returns a single render result by its request identifier, including its status, output URL, dimensions and the original request payload. Poll this after an asynchronous video render until the status is done or failed. |
| Get Template | `getTemplate` | Returns a single template by its identifier, including the full list of editable properties. Use each property's key value as a key in the data object of a render request. |
| Get Template HTML Content | `getTemplateHtmlContent` | Returns the raw html, css and sampleData of a template. Supported only for templates that use the html-editor; other editors return an error. |
| Get Template Preview Metadata | `getTemplatePreviewMetadata` | Returns the stored preview metadata for a template. The response is an empty object until a preview image has been generated for that template in the editor. |
| List Available Fonts | `listAvailableFonts` | Returns every font available to the account for use in templates, including Google Fonts and custom fonts uploaded by the organization, with their variants, subsets and category. |
| List My Legacy Templates | `listMyLegacyTemplates` | Lists the account's own templates through the legacy v1 endpoint, which returns a flat array with an href preview field and a modifiedAt timestamp rather than the v2 shape. This route returns every template in one array and ignores paging parameters; use List Templates for the paged v2 view. |
| List Render Batches | `listRenderBatches` | Lists the named render batches in the account. A batch is created by passing batchName on a render request, and groups the renders produced by a bulk job so they can be retrieved together. |
| List Render Requests | `listRenderRequests` | Returns the account's render requests as a flat legacy array, each with its status, output URL, type and originating template. This route returns every request in one array and ignores paging parameters; use List Render Results for the paged v2 view with filtering. |
| List Render Results | `listRenderResults` | Lists every image, PDF and video the account has rendered, newest first, in a paged envelope. Can be narrowed to a single template or a named render batch. |
| List Stored Files Paged | `listStoredFilesPaged` | Lists the files uploaded to the RenderForm asset library in a paged envelope. This is the v2 view of the upload library; use List Uploaded Files for the flat v1 array. |
| List Template Tags | `listTemplateTags` | Lists every tag used across the account's templates together with how many templates carry each tag. Tags are created implicitly when a template is saved with them. |
| List Templates | `listTemplates` | Lists the account's own RenderForm templates with metadata and preview links. Supports filtering by name, tags and source template, and paging with page and size (size max 50). |
| List Uploaded Files | `listUploadedFiles` | Returns a flat array of the files in the account's upload library, each with its public URL, storage key, byte size and type. |
| List Webhooks | `listWebhooks` | Lists the global webhooks registered on the RenderForm organization. Up to 10 global webhooks can exist; each fires for every request made with the account's API key. Note that the id of each webhook is reissued whenever the webhook collection changes, so treat the ids in this response as valid only until the next create or delete. |
| Rename Template Tag | `renameTemplateTag` | Renames a tag across every template that carries it. The tag is addressed by its current name and the response body is empty, so confirm the change with List Template Tags. |
| Render Image By Direct URL | `renderImageByDirectUrl` | Renders a template through RenderForm's direct image URL. The route answers a 308 redirect to the rendered file on the public CDN, which this action follows, so the response is the image itself as base64 data with its name, mime type and size. SECURITY: this route accepts the API key only as a query parameter (the X-API-KEY and Authorization headers are both rejected with 'Missing apiKey or authCode'), so the key is recorded in the request URL of every execution. Prefer Render Image Or PDF unless you specifically need the direct URL form. |
| Render Image Or PDF | `renderImageOrPdf` | Renders a template into an image, PDF or video and returns the URL of the rendered file. Each fresh render consumes credits (video renders cost 10 credits per started second). An identical request for the same template returns the cached file for free unless cache is set to false. Video renders answer 202 with status pending; poll Get Render Result until the status is done. |
| Render Signed Image | `renderSignedImage` | Renders a template through RenderForm's signed-request URL, which needs no API key because the changes are authenticated by an HMAC-SHA256 signature. The fastn engine cannot compute HMAC, so the caller must supply the base64 changes and the signature, generated on their own server with the account's API key as the secret. The route answers a 308 redirect to the rendered file on the public CDN, which this action follows, so the response is the image itself as base64 data. |
| Render Template Legacy | `renderTemplateLegacy` | Renders a template through the legacy v1 render route and returns the output URL. Kept for integrations still pointed at v1; new work should use Render Image Or PDF. |
| Render Template To File | `renderTemplateToFile` | Renders a template and asks RenderForm to hand back the file rather than a JSON envelope, by calling the render endpoint with output=image. KNOWN LIMITATION: the vendor answers 308 Permanent Redirect to the rendered file on the public CDN, and because a 308 preserves the original method the fastn engine re-sends the POST to the CDN, which rejects it with 405 Method Not Allowed. The render itself succeeds and is billed, and the file is reachable at the redirect target, but this action cannot return it. Use Render Image Or PDF to get the file URL, or Render Image By Direct URL to get the bytes. |
| Replace Legacy Template | `replaceLegacyTemplate` | Updates a template through the legacy v1 endpoint. Unlike Update Template Metadata this call has replace semantics: name, width and height are all mandatory even when only one of them changes. |
| Update Organization Name | `updateOrganizationName` | Renames the RenderForm organization. The name is the only editable organization field and is required: an empty body returns 'name: must not be empty' and any other field returns 'Unknown property'. VENDOR DEFECT: with a valid name the route answers 500 'Unexpected error' rather than applying the change. Verified against the vendor directly, outside fastn. Rename the organization from the RenderForm web app until the vendor fixes it. |
| Update Template HTML Content | `updateTemplateHtmlContent` | Replaces the html, css and sampleData of an html-editor template and returns what was persisted. Merge fields written as double curly braces in the html become renderable properties on the template. |
| Update Template Metadata | `updateTemplateMetadata` | Updates the name, canvas size, output format and/or tags of an existing template. Only the fields supplied are changed, except tags, which replaces the whole tag set when provided. |
| Upload File | `uploadFile` | Uploads a text-based asset (SVG, CSV, JSON, plain text) to the RenderForm upload library and returns its public URL, which can then be used as an image source inside a template. Supply the file body as text; binary formats such as PNG or JPEG cannot be sent through this action. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Render Complete | `RENDER_COMPLETE` | Fires when a rendered image, PDF or video is finished and ready to download. Payload schema is modelled from RenderForm's published sample at https://renderform.io/docs/api/webhooks, not from a captured delivery. |
| Template Created | `TEMPLATE_CREATE` | Fires when a new template is created in the account. Payload schema is modelled from RenderForm's published sample at https://renderform.io/docs/api/webhooks, not from a captured delivery. |
| Template Deleted | `TEMPLATE_DELETE` | Fires when a template is deleted. Payload schema is modelled from RenderForm's published sample at https://renderform.io/docs/api/webhooks, not from a captured delivery. |
| Template Updated | `TEMPLATE_UPDATE` | Fires when an existing template is changed. Payload schema is modelled from RenderForm's published sample at https://renderform.io/docs/api/webhooks, not from a captured delivery. |
