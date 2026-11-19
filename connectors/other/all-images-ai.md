---
description: "All-Images.ai is an AI stock-image platform that generates royalty-free photos with Midjourney and sells ready-made images."
hidden: true
---

# All-Images.ai

<img src="../../.gitbook/assets/connectors/lg/all-images-ai.png" alt="All-Images.ai logo">

All-Images.ai is an AI stock-image platform that generates royalty-free photos with Midjourney and sells ready-made images. This connector covers the complete All-Images.ai v1 API: API key check and credit balance, image search and purchase (direct URL or binary download), previously downloaded images, image display URLs, image generations (create, list, get, update, retry, delete) and webhook endpoint subscriptions for generation status events.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [all-images.ai](https://all-images.ai) |
| **Authentication** | Credentials you enter |
| **Slug** | `allImagesAi` |

## Use it

Add All-Images.ai from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.allImagesAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Buy Image</td><td><code>buyImage</code></td><td>Purchases an image by id and returns direct public download links for it. Requires enough credits; credits are debited only once per image, so buying an already-purchased image is free.</td></tr><tr><td>Check API Key</td><td><code>checkApiKey</code></td><td>Verifies that the connected API key is valid and returns the email address and name of the All-Images.ai user account it belongs to.</td></tr><tr><td>Create Image Generation</td><td><code>createImageGeneration</code></td><td>Starts an image generation that produces a set of four AI images from a text prompt. Simple mode takes a plain description plus optional named parameters (format, weather, time, camera, chaos, stylize, interdiction); advanced mode takes a raw Midjourney prompt. Generation runs asynchronously: poll Get Image Generation or subscribe a webhook to be notified when the status reaches Done (3). Each generation consumes credits.</td></tr><tr><td>Delete Image Generations</td><td><code>deleteImageGenerations</code></td><td>Deletes one or more image generations by id from the connected account.</td></tr><tr><td>Download Image</td><td><code>downloadImage</code></td><td>Purchases an image by id and returns the image file itself as a binary JPEG. Requires enough credits; credits are debited only once per image. Use Buy Image instead when you need a public URL rather than the bytes.</td></tr><tr><td>Get Credits</td><td><code>getCredits</code></td><td>Returns the remaining credit balance of the connected account for every credit type (global, image purchases, generations, upscales, websites and queues), with the renewal total per subscription period.</td></tr><tr><td>Get Image File</td><td><code>getImageFile</code></td><td>Fetches an image's JPEG bytes from its display URL in either the preview or full format. This is the same URL returned in the url and urlFull fields of search, purchase and generation results.</td></tr><tr><td>Get Image Generation</td><td><code>getImageGeneration</code></td><td>Retrieves a single image generation by id, including its current status (0 Create, 1 Pending, 2 Processing, 3 Done, 4 Error), prompt, parameters and the generated images once complete.</td></tr><tr><td>Get Webhook</td><td><code>getWebhook</code></td><td>Retrieves a webhook endpoint registered on the connected API key by its id, returning the endpoint URL and the API key it belongs to.</td></tr><tr><td>List Downloaded Images</td><td><code>listDownloadedImages</code></td><td>Lists the images the connected account has already downloaded or purchased, with direct download links for the preview, full, upscaled and UHD versions. Supports offset pagination and a download-date range.</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Image Generations</td><td><code>listImageGenerations</code></td><td>Lists the connected account's image generations with their status, prompt, parameters and generated images. Supports offset pagination, sorting and filtering by name or tag.</td></tr><tr><td>Retry Image Generation</td><td><code>retryImageGeneration</code></td><td>Restarts an image generation that ended in the Error status, for example after correcting its prompt with Update Image Generation.</td></tr><tr><td>Search Images</td><td><code>searchImages</code></td><td>Searches the All-Images.ai stock library by keywords and returns a page of matching images with preview and full-size URLs. Supports offset pagination and a free-images-only filter.</td></tr><tr><td>Subscribe Webhook</td><td><code>subscribeWebhook</code></td><td>Registers an HTTPS endpoint on the connected API key so All-Images.ai posts image-generation status events to it. Returns the new webhook id, which is needed to look the webhook up or remove it later.</td></tr><tr><td>Unsubscribe Webhook</td><td><code>unsubscribeWebhook</code></td><td>Removes a webhook endpoint from the connected API key by its id so it no longer receives image-generation events.</td></tr><tr><td>Update Image Generation</td><td><code>updateImageGeneration</code></td><td>Updates an existing image generation's name, prompt, mode, parameters, tags or metadata. Only the fields you send are changed. A generation cannot be updated while it is Pending or Processing; update a failed generation and then call Retry Image Generation to run it again.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Image Generation Active</td><td><code>print.active</code></td><td>Sent when an image generation moves into processing (status Pending or Processing).</td></tr><tr><td>Image Generation Completed</td><td><code>print.completed</code></td><td>Sent when an image generation finishes (status Done) and all generated images are available.</td></tr><tr><td>Image Generation Created</td><td><code>print.created</code></td><td>Sent when a new image generation is created (status Create).</td></tr><tr><td>Image Generation Failed</td><td><code>print.failed</code></td><td>Sent when an image generation ends in the Error status; update the generation and call Retry Image Generation to run it again.</td></tr><tr><td>Image Generation Progress</td><td><code>print.progress</code></td><td>Sent each time one image of the generation has been produced.</td></tr></tbody></table>
