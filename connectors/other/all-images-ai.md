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

| Action | Slug | What it does |
| --- | --- | --- |
| Buy Image | `buyImage` | Purchases an image by id and returns direct public download links for it. Requires enough credits; credits are debited only once per image, so buying an already-purchased image is free. |
| Check API Key | `checkApiKey` | Verifies that the connected API key is valid and returns the email address and name of the All-Images.ai user account it belongs to. |
| Create Image Generation | `createImageGeneration` | Starts an image generation that produces a set of four AI images from a text prompt. Simple mode takes a plain description plus optional named parameters (format, weather, time, camera, chaos, stylize, interdiction); advanced mode takes a raw Midjourney prompt. Generation runs asynchronously: poll Get Image Generation or subscribe a webhook to be notified when the status reaches Done (3). Each generation consumes credits. |
| Delete Image Generations | `deleteImageGenerations` | Deletes one or more image generations by id from the connected account. |
| Download Image | `downloadImage` | Purchases an image by id and returns the image file itself as a binary JPEG. Requires enough credits; credits are debited only once per image. Use Buy Image instead when you need a public URL rather than the bytes. |
| Get Credits | `getCredits` | Returns the remaining credit balance of the connected account for every credit type (global, image purchases, generations, upscales, websites and queues), with the renewal total per subscription period. |
| Get Image File | `getImageFile` | Fetches an image's JPEG bytes from its display URL in either the preview or full format. This is the same URL returned in the url and urlFull fields of search, purchase and generation results. |
| Get Image Generation | `getImageGeneration` | Retrieves a single image generation by id, including its current status (0 Create, 1 Pending, 2 Processing, 3 Done, 4 Error), prompt, parameters and the generated images once complete. |
| Get Webhook | `getWebhook` | Retrieves a webhook endpoint registered on the connected API key by its id, returning the endpoint URL and the API key it belongs to. |
| List Downloaded Images | `listDownloadedImages` | Lists the images the connected account has already downloaded or purchased, with direct download links for the preview, full, upscaled and UHD versions. Supports offset pagination and a download-date range. |

<details>

<summary>See 6 more actions</summary>

* **List Image Generations** `listImageGenerations`: Lists the connected account's image generations with their status, prompt, parameters and generated images. Supports offset pagination, sorting and filtering by name or tag.
* **Retry Image Generation** `retryImageGeneration`: Restarts an image generation that ended in the Error status, for example after correcting its prompt with Update Image Generation.
* **Search Images** `searchImages`: Searches the All-Images.ai stock library by keywords and returns a page of matching images with preview and full-size URLs. Supports offset pagination and a free-images-only filter.
* **Subscribe Webhook** `subscribeWebhook`: Registers an HTTPS endpoint on the connected API key so All-Images.ai posts image-generation status events to it. Returns the new webhook id, which is needed to look the webhook up or remove it later.
* **Unsubscribe Webhook** `unsubscribeWebhook`: Removes a webhook endpoint from the connected API key by its id so it no longer receives image-generation events.
* **Update Image Generation** `updateImageGeneration`: Updates an existing image generation's name, prompt, mode, parameters, tags or metadata. Only the fields you send are changed. A generation cannot be updated while it is Pending or Processing; update a failed generation and then call Retry Image Generation to run it again.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Image Generation Active | `print.active` | Sent when an image generation moves into processing (status Pending or Processing). |
| Image Generation Completed | `print.completed` | Sent when an image generation finishes (status Done) and all generated images are available. |
| Image Generation Created | `print.created` | Sent when a new image generation is created (status Create). |
| Image Generation Failed | `print.failed` | Sent when an image generation ends in the Error status; update the generation and call Retry Image Generation to run it again. |
| Image Generation Progress | `print.progress` | Sent each time one image of the generation has been produced. |
