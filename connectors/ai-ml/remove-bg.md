---
description: "remove.bg Background Removal API (https://api.remove.bg/v1.0)."
hidden: true
---

# remove.bg

<img src="../../.gitbook/assets/connectors/lg/remove-bg.png" alt="remove.bg logo">

remove.bg Background Removal API (https://api.remove.bg/v1.0). Removes the background from JPG/PNG/WebP images supplied by URL or as a base64-encoded file, returning the cut-out either as a base64 string or as binary image data, with full control over output size, foreground type detection, output format, region of interest, cropping, scaling, positioning, alpha channel, AI shadows, semitransparency and solid-colour or image backgrounds. Also fetches the account credit balance and remaining free API calls, and submits images to the remove.bg Improvement Program. Authentication is an API key sent in the X-Api-Key header.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [remove.bg](https://remove.bg) |
| **Authentication** | API key |
| **Slug** | `removeBg` |

## Use it

Add remove.bg from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.removeBg.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Account Info</td><td><code>getAccountInfo</code></td><td>Fetches the remove.bg account credit balance and the number of free API calls remaining. Returns the subscription, pay-as-you-go, enterprise and total credit amounts together with the monthly free API call allowance. Balance changes can be delayed by several seconds, so remove.bg recommends calling this only on initial load or a manual refresh and otherwise tracking the balance locally using the X-Credits-Charged response header of each background removal. The 'sizes' field is always 'all' and is deprecated.</td></tr><tr><td>Remove Image Background</td><td><code>removeImageBackground</code></td><td>Removes the background from a JPG, PNG or WebP image and returns the cut-out as a base64-encoded string together with the foreground bounding box. Supply exactly one image source: image_url or image_file_b64. Input limits are 22 MB file size and 50 megapixels. Output size 'preview' (up to 0.25 MP) is free and consumes one of the monthly free API calls; 'full' (up to 25 MP) and 'auto' consume account credits. Supports foreground type hints, output format, region of interest, cropping, scaling, positioning, alpha-only output, AI shadows, semitransparency and solid-colour or image backgrounds. Errors are returned as an 'errors' array; no credits are charged on 4xx.</td></tr><tr><td>Remove Image Background As Binary File</td><td><code>removeImageBackgroundBinary</code></td><td>Same POST /v1.0/removebg endpoint as Remove Image Background, but requests the raw image bytes instead of the JSON envelope. remove.bg returns the cut-out as a binary PNG, JPG, WebP or ZIP file; the fastn engine wraps those bytes as a file envelope with name, mime, size and base64 'data'. Use this when you want to hand the result straight to a file store or upload step; use Remove Image Background instead when you also need the foreground bounding box. Supply exactly one image source: image_url or image_file_b64. Output size 'preview' is free; 'full' and 'auto' charge account credits.</td></tr><tr><td>Submit Image To Improvement Program</td><td><code>submitImageToImprovementProgram</code></td><td>Submits an image to the remove.bg Improvement Program so remove.bg can train on images it currently handles poorly and produce better results for similar images in future. Returns the id of the submitted image. Supply exactly one image source: image_url or image_file_b64. Limits are 22 MB file size, 50 megapixels input resolution and 100 files per day. Submitting through the API constitutes agreement to the Improvement Program Conditions at https://www.remove.bg/ipc; submissions are used on a best-effort basis and improvements typically take several weeks to take effect. This call consumes no credits.</td></tr></tbody></table>
