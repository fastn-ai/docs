---
description: "Photoroom AI image editing API."
hidden: true
---

# Photoroom

<img src="../../.gitbook/assets/connectors/lg/photoroom.png" alt="Photoroom logo">

Photoroom AI image editing API. Removes backgrounds, generates AI backgrounds, shadows, relighting, text removal, flat lay, ghost mannequin, virtual model and virtual try-on, upscaling and uncropping, and returns the edited image. Covers the Image Editing API v2 (image-api.photoroom.com), the legacy v1 render endpoint, the Remove Background API v1 (sdk.photoroom.com), Visual QA, and account/credit balance. Authenticates with an x-api-key header; prefix the key with sandbox_ to use Photoroom's free watermarked sandbox mode.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [photoroom.com](https://photoroom.com) |
| **Authentication** | API key |
| **Slug** | `photoroom` |

## Use it

Add Photoroom from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.photoroom.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Analyze Image With Visual QA | `analyzeImageWithVisualQa` | Runs Photoroom's Visual QA checks on an image referenced by URL and returns the analysis. Visual QA detects AI generation artefacts, hallucinations, unwanted text and, optionally, distinct clothing, footwear and accessory items, so a generated or edited image can be screened before it is published. Visual QA is an enterprise-plan feature; accounts without that entitlement receive a vendor entitlement error rather than an analysis. |
| Edit Image From URL | `editImageFromUrl` | Runs the Photoroom Image Editing API v2 on an image referenced by URL and returns the edited image. This single endpoint drives every Photoroom v2 capability through its parameters: background removal, AI backgrounds from a prompt or reference image, background blur, static background colour, AI shadows, relighting, AI text removal, flat lay, ghost mannequin, virtual model and virtual try-on, AI expand and uncrop, AI upscale, AI ironing, beautify, text-guided segmentation, subject outline, positioning, padding and margins, smart cropping, output size, DPI, colour space and export format. Each render consumes one image from the account balance; prefix the API key with sandbox_ to test for free with a watermark. |
| Edit Image With Explicit Options | `editImagePost` | Runs the Photoroom Image Editing API v2 through its POST multipart endpoint, sending the source image URL and the five most common render options as explicit form fields. Use Edit Image From URL when you need the full parameter surface; use this action when a caller must always state background removal, background colour, output size and export format explicitly. Photoroom's POST endpoint also accepts a raw imageFile upload, which the fastn engine cannot emit (see the connector notes). Each render consumes one image from the account balance; prefix the API key with sandbox_ to test for free with a watermark. |
| Fetch Image Through Photoroom Proxy | `fetchImageThroughProxy` | Fetches an image from an arbitrary URL through Photoroom's own image proxy and returns the bytes. This is the undocumented endpoint Photoroom uses to build the pr-edit-further-url link it returns on every v2 edit response. SECURITY NOTE: this endpoint requires no API key at all, so any URL passed to it is fetched by Photoroom's infrastructure and served back to anyone who holds the resulting link. Do not pass URLs to private or internal resources. |
| Generate Segmentation Mask (Undocumented) | `generateSegmentationMask` | Calls the undocumented /v1/mask route on sdk.photoroom.com, which sits in the same service as the Remove Background endpoint and answers with the same error envelope. Photoroom publishes no contract for it, so the exact name of its upload field is unknown: eleven candidate names were probed and all returned missing_image. Included so the route is represented; use Remove Background From Upload with Channels set to alpha to obtain a segmentation mask through a documented endpoint. |
| Get Account Credit Balance (Legacy v1) | `getAccountCreditBalanceV1` | Returns the Photoroom account's remaining credit balance using the legacy v1 account endpoint: credits still available and credits granted by the current subscription. Prefer Get Account Image Balance for new integrations; this endpoint is kept for callers still on the v1 credit model. |
| Get Account Image Balance | `getAccountImageBalance` | Returns the Photoroom account's remaining image allowance for the Image Editing API v2: how many images are still available, how many the current subscription grants, and the plan name. Call this before running a batch of edits to check whether the account still has quota, because every render consumes one image from the balance. |
| Get API Specification | `getApiSpecification` | Returns Photoroom's live OpenAPI 3.1 specification, listing every endpoint the API exposes together with the full parameter set, enums, defaults and response schemas. Useful for discovering parameters Photoroom has added since this connector was built, and for confirming which features an endpoint currently supports. |
| Inpaint Image (Undocumented) | `inpaintImage` | Calls the undocumented /v1/inpaint route on sdk.photoroom.com, which sits in the same service as the Remove Background endpoint and answers with the same error envelope. Photoroom publishes no contract for it, so the exact name of its upload field is unknown: eleven candidate names were probed and all returned missing_image. Included so the route is represented; use Edit Image From URL with Edit With AI Mode or Text Removal Mode for documented inpainting-style edits. |
| Remove Background From Upload (Basic Plan v1) | `removeBackgroundV1` | Removes the background from an uploaded image using Photoroom's Remove Background API v1 on sdk.photoroom.com, the remove.bg-compatible endpoint, and returns the cutout. KNOWN LIMITATION: this endpoint only accepts the image as raw binary bytes in an image_file upload part, and the fastn engine cannot emit binary multipart parts, so the request reaches Photoroom but the image cannot be decoded. To remove a background from fastn today, use Edit Image From URL with Remove Background enabled, which performs the same segmentation from an image URL and returns a real result. |
| Render Template From Upload (Legacy v1) | `renderTemplateFromUploadV1` | Renders an image into a saved Photoroom template through the legacy v1 render POST endpoint, sending the template id and the source image URL as multipart form fields, and returns the rendered image. Deprecated by Photoroom in favour of the v2 edit endpoint. Photoroom's POST form also accepts a raw imageFile upload, which the fastn engine cannot emit; supply the image by URL instead. Each render consumes one image from the account balance. |
| Render Template From URL (Legacy v1) | `renderTemplateFromUrlV1` | Renders an image into a saved Photoroom template using the legacy v1 render endpoint and returns the rendered image. Deprecated by Photoroom in favour of the v2 edit endpoint, which offers the same functionality plus the AI features; kept for existing integrations that still address templates by id. Each render consumes one image from the account balance. |
