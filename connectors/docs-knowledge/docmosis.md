---
description: "Docmosis Cloud (DWS4) document generation API."
hidden: true
---

# Docmosis

<img src="../../.gitbook/assets/connectors/docmosis.png" alt="Docmosis logo" width="64">

Docmosis Cloud (DWS4) document generation API. Render DOCX/ODT/PDF/RTF/HTML/TXT documents from stored templates and JSON data, manage the template and image libraries, convert files between formats, and read environment, render-queue and render-tag usage statistics.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [docmosis.com](https://docmosis.com) |
| **Authentication** | API key |
| **Slug** | `docmosis` |

## Use it

Add Docmosis from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.docmosis.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Template Batch | `uploadTemplateBatchCancel` | Cancels a bulk template upload job that is still running, identified by the job id supplied when it was started. Templates already uploaded by the job remain in place. |
| Convert File | `convert` | Converts a document, spreadsheet, presentation or drawing file from one format to another with no template involved. The target format is taken from the extension of the output name, for example 'result.pdf'. The file body is supplied as text, so text-based sources such as .txt, .csv and .fodt are supported; binary sources cannot be sent through this action because the fastn engine cannot carry binary multipart parts. |
| Copy Image | `copyImage` | Copies a stored image to a new name, leaving the original in place. Undocumented Docmosis Cloud route, verified live. Note the service answers HTTP 500 rather than 400 when the source image does not exist. |
| Copy Template | `copyTemplate` | Copies a stored template to a new name, leaving the original in place. Undocumented Docmosis Cloud route, verified live. The new name may include a different folder path. |
| Create Image Folder | `createImageFolder` | Creates an empty folder in the Docmosis Cloud image area so stored images can be organised by project or brand. Undocumented Docmosis Cloud route, verified live. |
| Create Template Folder | `createTemplateFolder` | Creates an empty folder in the Docmosis Cloud template area so templates can be organised by project or customer. Undocumented Docmosis Cloud route, verified live. |
| Delete Image | `deleteImage` | Permanently deletes one or more images from the Docmosis Cloud image area. This cannot be undone; templates that reference a deleted image will render without it. |
| Delete Image Folder | `deleteImageFolder` | Deletes a folder from the Docmosis Cloud image area together with every image inside it. Undocumented Docmosis Cloud route, verified live. This is irreversible. The service reports a non-zero deleted count even for a folder that never existed, so confirm with List Images. |
| Delete Stored Files | `deleteFiles` | Deletes documents from the Docmosis file storage area. Undocumented Docmosis Cloud route, verified live. WARNING: unlike every other Docmosis delete route this one does not require a name, and a call with no file name returns success with a non-zero deleted count. Always supply an explicit file name and confirm the result with List Stored Files. |
| Delete Template | `deleteTemplate` | Permanently deletes one or more templates from the Docmosis Cloud template area. This cannot be undone; any integration that renders from the named template will start failing. Pass every template name to remove in a single call. |

<details>

<summary>See 27 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Template Folder | `deleteTemplateFolder` | Deletes a folder from the Docmosis Cloud template area together with every template inside it. Undocumented Docmosis Cloud route, verified live. This is irreversible. Note that the service reports a non-zero deleted count even for a folder that never existed, so treat the count as advisory and confirm with List Templates. |
| Download Image File | `getImage` | Downloads one or more stored images from the Docmosis Cloud image area. A single image is returned as its own binary stream; supplying several names returns a ZIP archive. The response is application/octet-stream, not JSON. |
| Download Stored File | `getFile` | Downloads a document from the Docmosis file storage area by name. Undocumented Docmosis Cloud route, verified live. Requires the file storage entitlement; without it the service answers 'Docmosis file storage not permitted'. |
| Download Template File | `getTemplate` | Downloads one or more stored template files. A single template is returned as its own binary stream; supplying several names returns a ZIP archive containing them. The response is application/octet-stream, not JSON. |
| Get Environment Ready | `getEnvironmentReady` | Checks that the Docmosis Cloud environment identified by the access key is activated, enabled and ready to accept render requests. Returns { succeeded, shortMsg }. Use it to validate an access key without consuming page quota. |
| Get Environment Summary | `getEnvironmentSummary` | Returns a summary of the Docmosis Cloud environment behind the access key: account name, environment name and activation state, plan name, and the page quota with the number of pages used and the percentage consumed. Use it to check remaining render capacity before generating documents. |
| Get Render Queue | `getRenderQueue` | Reports the current load on the render queue for your environment as { availablePct, delaySeconds }. A low availablePct or a non-zero delaySeconds means renders are being throttled; poll this before submitting a large batch. |
| Get Render Tags | `getRenderTags` | Returns monthly page-count and document-count statistics for renders that were recorded against one or more user-defined tags (set with the tags parameter on Render Document). Useful for per-customer or per-feature usage reporting. |
| Get Service Status | `getServiceStatus` | Undocumented Docmosis Cloud health route. Returns the readiness of the regional Docmosis service as { message, ready }. Unlike Get Environment Ready it reports on the service itself rather than on your environment. |
| Get Template Batch Status | `uploadTemplateBatchStatus` | Reports the progress of a bulk template upload job started by Upload Template Batch, identified by the job id you supplied. Returns whether the job is still running, how many templates were processed and any per-template errors. |
| Get Template Details | `getTemplateDetails` | Returns stored metadata for a single template: its full name, size in bytes, last-modified timestamps, MD5 checksum, description and whether Docmosis detected errors in it during upload. |
| Get Template Sample Data | `getSampleData` | Generates a ready-to-use sample data payload for a stored template, in JSON or XML, matching every field and repeating section the template declares. Feed the result straight into Render Document as a starting point. |
| Get Template Structure | `getTemplateStructure` | Analyses a stored template and returns the tree of Docmosis mark-up it contains: fields, repeating sections, conditional sections and images, each with the data references it binds to. Use it to discover exactly which data keys a template expects before rendering. |
| List Images | `listImages` | Lists the images stored in the Docmosis Cloud image area, optionally restricted to a folder and optionally including sub-folders. Stored images can be referenced from templates by name. |
| List Stored Files | `listFiles` | Lists the documents held in the Docmosis file storage area for your environment. Undocumented Docmosis Cloud route, verified live. File storage is a paid entitlement: the sibling read and write routes answer 'Docmosis file storage not permitted' on plans without it. |
| List Templates | `listTemplates` | Lists the templates stored in the Docmosis Cloud template area, optionally restricted to a folder and optionally including sub-folders. Each entry carries the template name, size, last-modified timestamps and whether it is a system template. Supports paging for large libraries. |
| Ping Service | `ping` | Lightweight availability check against the Docmosis Cloud region. Returns HTTP 200 with an empty JSON object when the service is reachable. Requires no access key, so it is safe to use as a heartbeat. |
| Put Stored File | `putFile` | Uploads a document into the Docmosis file storage area. Undocumented Docmosis Cloud route, verified live; it accepts multipart form data only and rejects a JSON body with 'Request media type not supported on this endpoint.'. Requires the file storage entitlement. |
| Rename Image | `renameImage` | Renames or moves a stored image. Undocumented Docmosis Cloud route, verified live. The new name may include a different folder path, which moves the image. |
| Rename Image Folder | `renameImageFolder` | Renames a folder in the Docmosis Cloud image area, moving every image inside it to the new path. Undocumented Docmosis Cloud route, verified live. |
| Rename Template | `renameTemplate` | Renames or moves a stored template. Undocumented Docmosis Cloud route, verified live. The new name may include a different folder path, which moves the template. Fails with 'Source file/folder not found' if the template does not exist. |
| Rename Template Folder | `renameTemplateFolder` | Renames a folder in the Docmosis Cloud template area, moving every template inside it to the new path. Undocumented Docmosis Cloud route, verified live. |
| Render Document | `render` | Generates a document from a stored template and a JSON data payload. Supports PDF, DOCX, ODT, RTF, HTML and TXT output, PDF watermarking, password protection, PDF/A archive mode and accessibility tagging. Set streamResultInResponse to 'true' to receive the document base64-encoded inside the JSON response. WARNING: each render consumes pages from the account page quota, and setting storeTo to a 'mailto:' destination sends the finished document by email to real recipients. |
| Render Document From Form | `renderForm` | Undocumented form-encoded variant of the render service, verified live. It renders a stored template exactly as Render Document does but accepts the request as multipart form fields, with the template data supplied as a JSON string. Use Render Document for the full parameter set; this action exposes the core fields. Each call consumes pages from the account page quota. |
| Upload Image | `uploadImage` | Uploads an image into the Docmosis Cloud image area so templates can reference it by name. The image body is supplied as text, which covers ASCII-safe image formats such as SVG and Netpbm PPM. Binary formats (PNG, JPEG, GIF, BMP) cannot be sent through this action because the fastn engine cannot carry binary multipart parts; upload those through the Docmosis Cloud Console or a direct multipart call. |
| Upload Template | `uploadTemplate` | Uploads a single plain-text template into the Docmosis Cloud template area and analyses it for mark-up errors. The template body is supplied as text, so this action covers text-based templates (.txt). Binary Word and OpenDocument templates (.docx, .doc, .odt) cannot be sent through this action because the fastn engine cannot carry binary multipart parts; upload those through the Docmosis Cloud Console or a direct multipart call. |
| Upload Template Batch | `uploadTemplateBatch` | Starts an asynchronous bulk upload of many templates supplied as a single ZIP archive, optionally into a named folder. Returns a job identifier that Get Template Batch Status polls. The ZIP is binary, so this action cannot be driven through the fastn engine, which carries text multipart parts only; call it directly or use the Docmosis Cloud Console for bulk uploads. |

</details>
