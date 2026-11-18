---
description: "Templated (templated.io) generates images, PDFs and videos from reusable design templates."
hidden: true
---

# Templated

Templated (templated.io) generates images, PDFs and videos from reusable design templates. This connector covers the full Templated public v1 REST API: templates and their layers, pages, tags, versions and clones; the gallery; folders; renders (single, multi-template, merged, duplicated and downloaded); uploads and fonts; asynchronous download jobs; AI template generation from a prompt or HTML; and imports from Bannerbear, Canva and Polotno.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [templated.io](https://templated.io) |
| **Authentication** | Bearer token |
| **Actions** | 60 |
| **Events** | 3 |
| **Slug** | `templated` |

## Use it

Add Templated from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.templated.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Template Tags | `addTemplateTags` | Adds one or more tags to a template, keeping any tags already present. The endpoint takes a bare JSON array, so supply the tags as a JSON array string such as ["invoice","q4"]. Returns the updated template. |
| Clone Template | `cloneTemplate` | Creates a linked clone of an existing template. A clone keeps a reference to its source template so later changes to the source can be tracked, and counts towards the account template limit. |
| Convert HTML File To Template | `convertHtmlFileToTemplate` | Uploads an HTML document as a file and converts it into an editable template. The document is sent as a multipart form part named html and must contain a root container element with an explicit pixel width and height. Counts towards the account template limit. |
| Count Clone Templates | `countCloneTemplates` | Returns how many clones exist for one source template. The source template identifier is mandatory; without it Templated answers 400 with "Source template ID is required". |
| Create Folder | `createFolder` | Creates a new folder for grouping templates and renders. Returns the folder with its generated identifier. |
| Create Render | `createRender` | Renders a template to an image, PDF or video, overriding any layer's text, image, colour or visibility for this run. Each render consumes one credit from the plan quota. Set Async to true to return immediately with a PENDING render and receive the finished file at Webhook URL; leave it false to wait for the finished URL. Supply either Template for a single template or Templates for a batch. |
| Create Template | `createTemplate` | Creates a new design template in the account from a canvas size and a list of layers. Free plans are capped at three templates. Tags and canvas background are ignored on creation by Templated - set them afterwards with Update Template or Add Template Tags. Returns the created template including its generated identifier. |
| Create Template From Render | `createTemplateFromRender` | Turns a finished render back into a reusable template, carrying over the layer values that produced it. Counts towards the account template limit. |
| Delete Folder | `deleteFolder` | Deletes a folder. Templates and renders inside it are not deleted; they are simply no longer assigned to a folder. |
| Delete Fonts | `deleteFonts` | Removes one or more custom fonts the team uploaded. The parameter takes font NAMES, not identifiers, and Templated answers 400 with a not_found list when no uploaded font matches. Bundled Google Fonts cannot be deleted, so this action only has an effect on accounts that can upload custom fonts (a paid feature). |
| Delete Render | `deleteRender` | Removes a stored render and its generated file from the account. The credit already spent on the render is not refunded. |
| Delete Template | `deleteTemplate` | Permanently removes a template from the account by its identifier. Renders already produced from the template are not deleted. |
| Delete Uploads | `deleteUploads` | Deletes one or more files from the account's asset library by identifier. Templates still pointing at a deleted file will render with a missing image. |
| Download Job Result | `downloadJobResult` | Downloads the finished archive produced by an asynchronous template download job. Call it only once Get Download Job Status reports the job complete. |
| Download Render | `downloadRender` | Downloads the file bytes of a finished render. The render must already be COMPLETED; this does not consume a further render credit. |
| Download Template | `downloadTemplate` | Exports a template in the requested format and returns the resulting render record, including the URL of the finished file. Consumes one render credit. |
| Duplicate Render | `duplicateRender` | Re-runs an existing render with the same template and layer values, producing a new render record. Consumes one render credit. |
| Duplicate Template | `duplicateTemplate` | Creates an independent copy of a template, with no link back to the original. Use Clone Template instead when the copy should stay associated with its source. |
| Forward Analytics Event | `forwardAnalyticsEvent` | Forwards a privacy-friendly page-view or custom analytics event through Templated's first-party analytics proxy. Used by Templated's own web app and embeds; it returns 202 with the body "ok". |
| Generate Template From HTML | `generateTemplateFromHtml` | Builds an editable template out of an HTML snippet, or out of a prompt describing the markup, using Templated's AI converter. The HTML must contain a single root container element with an explicit pixel width and height (for example a div styled width:400px;height:200px;position:relative), otherwise Templated answers 500 "No root container found in HTML". At least one of HTML or Prompt is required. |
| Generate Template With AI | `generateTemplateWithAi` | Creates a new template from a natural-language prompt using Templated's AI designer, optionally guided by a reference image. Set Async to true to get a job id back and poll Get AI Generation Status. The generated template counts towards the account template limit; Templated answers 403 "You've reached your template limit" when it is full. |
| Get Account Usage | `getAccount` | Retrieves the Templated account behind the API key: the owner's name and email, the team name, the current plan, and the API render usage against the plan quota. Use it to check remaining render credits before submitting renders. |
| Get AI Generation Status | `getAiGenerationStatus` | Returns the state of an asynchronous AI template generation job and the generated template once it is ready. Answers 404 with "Generation job not found" for an unknown job id. |
| Get Download Job Status | `getDownloadJobStatus` | Returns the progress of one asynchronous template download job, including how many pages have been processed and the result URL once it finishes. |
| Get Render | `getRender` | Retrieves a single render by identifier, including its processing status and the URL of the finished file. Poll this after an asynchronous Create Render until Status is COMPLETED. |
| Get Template | `getTemplate` | Retrieves a single template by its identifier, optionally including its layer and page definitions. |
| Import Template From Bannerbear | `importTemplateFromBannerbear` | Imports a Bannerbear template into Templated. Templated expects the template's exported HTML page containing the Bannerbear canvas element, not the Bannerbear JSON API payload: a document without that element is rejected with 500 "Could not find BannerBear canvas element in HTML". Export the page from the Bannerbear template editor and pass its markup here. |
| Import Template From Canva | `importTemplateFromCanva` | Imports a Canva design into Templated from its public share link. The import runs asynchronously: Templated creates the template immediately with status PROCESSING and fills in its layers when the Canva design has been fetched. Answers 400 "Canva URL is required" when the link is missing and 403 when the account template limit is full. |
| Import Template From Polotno | `importTemplateFromPolotno` | Imports a Polotno design into Templated from its exported JSON and returns the created template. Templated answers 400 with "Polotno JSON is required" when the design JSON is missing. Counts towards the account template limit. |
| List Clone Templates | `listCloneTemplates` | Lists templates that were created as clones, optionally narrowed to the clones of one source template or to a caller-supplied external id. |
| List Download Jobs | `listDownloadJobs` | Lists the team's asynchronous template download jobs with their progress and result URLs. VENDOR BLOCKER: this route and both of its siblings (Get Download Job Status, Download Job Result) currently answer 500 Internal Server Error for every request, including an empty list, reproduced directly against the API. |
| List Folder Renders | `listFolderRenders` | Lists the renders filed in one folder, newest first. |
| List Folder Templates | `listFolderTemplates` | Lists the templates stored in one folder, with the same search, tag and size filters as List Templates. |
| List Folders | `listFolders` | Lists the folders in the account used to organise templates and renders, optionally filtered by a name search. |
| List Fonts | `listFonts` | Lists every font available to the account: the Google Fonts catalogue Templated bundles plus any custom fonts the team has uploaded. Use the returned names in a text layer's Font Family. |
| List Gallery Fonts | `listGalleryFonts` | Searches Templated's bundled font gallery by name, returning the font family names that can be used in a text layer. |
| List Gallery Templates | `listGalleryTemplates` | Browses Templated's public template gallery, with search, category, tag and size filters. Gallery templates can be copied into the account with Clone Template or Duplicate Template. |
| List Renders | `listRenders` | Lists every render in the account, newest first. VENDOR DEFECT: the External ID filter on this endpoint always returns an empty list, even for a render that carries that external id (reproduced directly against the API); use List Template Renders, whose External ID filter works correctly. |
| List Sample External Assets | `listSampleExternalAssets` | Returns Templated's set of sample image and video URLs, provided for trying out image and video layers without supplying your own assets. |
| List Template Layers | `listTemplateLayers` | Lists every layer of a template with its name, type, position, size and styling. The layer names returned here are the keys used to override content when creating a render. |
| List Template Pages | `listTemplatePages` | Lists the pages of a multi-page template, each with its own dimensions and layer map. Single-page templates return one page named page-1. |
| List Template Renders | `listTemplateRenders` | Lists the renders produced from one template, newest first, optionally filtered to a single caller-supplied external id. |
| List Templates | `listTemplates` | Lists the templates in the authenticated account, newest first, with optional full-text search, tag, size and external id filters and optional inclusion of each template's layers and pages. Returns an array of template objects. |
| List Uploads | `listUploads` | Lists the files in the account's asset library, with optional name search and tag filtering. |
| Merge Renders | `mergeRenders` | Combines several finished renders into one multi-page PDF, returned as file bytes rather than a stored render. Supply the render identifiers in the order the pages should appear. Templated answers 500 if the field is named anything other than ids or if any identifier is unknown. |
| Move Render To Folder | `moveRenderToFolder` | Files an existing render into a folder, moving it out of any folder it was in before. Templated answers 200 with an empty body; confirm with List Folder Renders. |
| Move Template To Folder | `moveTemplateToFolder` | Files an existing template into a folder, moving it out of any folder it was in before. Templated answers 200 with an empty body; confirm with List Folder Templates. |
| Parse Google Merchant Feed | `parseGoogleMerchantFeed` | Parses a Google Merchant Center product feed into the product rows Templated uses for bulk catalogue renders, optionally previewing them against a template. The feed is sent as a multipart form part. |
| Parse Meta Product Feed | `parseMetaProductFeed` | Parses a Meta (Facebook and Instagram) commerce product feed into the rows Templated uses for bulk catalogue renders. VENDOR BLOCKER: this endpoint currently answers 500 for every well-formed feed tried (CSV, TSV and Google-style XML, with and without a template id) while the sibling Parse Google Merchant Feed accepts the same XML; use that action until Templated fixes this route. |
| Proxy Image | `proxyImage` | Fetches an external image through Templated's proxy so it can be used in a template without cross-origin restrictions. Answers 502 with "Received HTML instead of image from source" when the URL does not serve an image. |
| Remove Template Tags | `removeTemplateTags` | Removes the listed tags from a template, leaving its other tags in place. The endpoint takes a bare JSON array, so supply the tags as a JSON array string. Returns the updated template. |
| Render Template To Image URL | `renderTemplateToImage` | Renders a template in a single GET request and returns the image bytes directly, for use as an img src. Layer overrides are passed as a compact JSON string. Consumes one render credit. SECURITY NOTE: Templated requires the API key as the apiKey query parameter on this route and rejects the Authorization header with 400, so the key appears in the recorded request URL. Prefer Create Render, which authenticates by header. |
| Replace Template Tags | `replaceTemplateTags` | Replaces the whole tag list of a template with the tags supplied, discarding any tags not in the list. The endpoint takes a bare JSON array, so supply the tags as a JSON array string. Returns the updated template. |
| Send Test Webhook | `sendTestWebhook` | Asks Templated to post a sample render-completed payload to the endpoint you supply, so you can verify a receiver before wiring it to a real render. The endpoint takes the target URL as a bare JSON string body and returns an empty 200. |
| Test Authentication | `testAuthentication` | Validates the API key and returns the authenticated user and team profile, including plan status, render count, template limit and team role. SECURITY NOTE: the response also contains the account's own API key in the apiKey field, so anyone who can run this action receives the credential. |
| Update Folder | `updateFolder` | Renames an existing folder. Returns the folder as stored after the change. |
| Update Template | `updateTemplate` | Updates an existing template's name, description, canvas size, background, tags or layers. Set Replace Layers to true to swap the whole layer list for the one supplied; leave it false to merge layers by name. |
| Upload Asset | `uploadAsset` | Uploads a file to the account's asset library so it can be referenced from image layers. The file is sent as a multipart form part built from the file name, content type and contents. Text-based assets such as SVG, CSV or JSON round-trip correctly; binary assets are re-encoded by the request engine and should be referenced by public URL instead. |
| Upload Font | `uploadFont` | Uploads a custom font file (TTF, OTF, WOFF or WOFF2) to the team so it can be used in text layers. The file is sent as a multipart form part. Custom fonts are a paid feature: free accounts receive 403 "Please upgrade your account to a paid plan to upload fonts." Font files are also binary, which the fastn request engine re-encodes as UTF-8, so on a paid plan prefer uploading fonts from the Templated dashboard. |
| Upload Public Asset | `uploadPublicAsset` | Uploads a file to Templated's public asset bucket without attaching it to the account library, returning a URL usable in image layers. Same multipart form as Upload Asset; text-based files round-trip correctly. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Template Created | `create` | Fires when a user creates a new template in the Templated embedded editor. REGISTRATION IS UI-ONLY: sign in at https://app.templated.io, open Embed Setup, expand Advanced Settings, paste the fastn webhook URL into the Webhook URL field and press Save. Templated exposes no API-key-authenticated registration route: POST /webhook-config/ answers 401 {"message":"Full authentication is required to access this resource","status":401} to a valid API key because that surface is session-authenticated for the web app only. |
| Template Downloaded | `download` | Fires when a user downloads a template from the Templated embedded editor. REGISTRATION IS UI-ONLY: sign in at https://app.templated.io, open Embed Setup, expand Advanced Settings, paste the fastn webhook URL into the Webhook URL field and press Save. Templated exposes no API-key-authenticated registration route: POST /webhook-config/ answers 401 {"message":"Full authentication is required to access this resource","status":401} to a valid API key. |
| Template Saved | `save` | Fires when a user saves a template in the Templated embedded editor. REGISTRATION IS UI-ONLY: sign in at https://app.templated.io, open Embed Setup, expand Advanced Settings, paste the fastn webhook URL into the Webhook URL field and press Save. Templated exposes no API-key-authenticated registration route: POST /webhook-config/ answers 401 {"message":"Full authentication is required to access this resource","status":401} to a valid API key. |
