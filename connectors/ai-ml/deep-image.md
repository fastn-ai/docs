---
description: "Deep-Image.ai is an AI image enhancement and generation API."
hidden: true
---

# Deep Image

<img src="../../.gitbook/assets/connectors/lg/deep-image.png" alt="Deep Image logo">

This connector covers the full Deep Image REST API: synchronous and scheduled image processing (AI upscaling, denoise, deblur, face enhancement, light and color correction, background removal and generation, prompt-based editing, inpainting and outpainting, print sizing, captions, presets), job result retrieval, result deletion, and account information including remaining credits.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [deep-image.ai](https://deep-image.ai) |
| **Authentication** | API key |
| **Slug** | `deepImage` |

## Use it

Add Deep Image from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.deepImage.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Job Result</td><td><code>deleteJobResult</code></td><td>Deletes the stored result images of a completed processing job by its job id. After deletion, Get Job Result for that job reports the image as deleted (status complete, message 'Image deleted').</td></tr><tr><td>Get Account Information</td><td><code>getAccountInformation</code></td><td>Retrieves the authenticated Deep Image account profile, including the remaining credit balance, username, email, language, account-level webhook settings and billing address.</td></tr><tr><td>Get Job Result</td><td><code>getJobResult</code></td><td>Retrieves the status and result of an image processing job by its job id. While the job is queued or running the status is received, not_started or in_progress; when it is complete the response includes the result_url of the processed image (or a results array for multi-image jobs). Poll this action until the job completes.</td></tr><tr><td>Process Image</td><td><code>processImage</code></td><td>Processes an image (upscale, enhance, remove or generate background, edit, inpaint or outpaint, resize, print sizing, captions, presets) and waits up to 25 seconds for the result. If processing finishes in time the response status is complete and includes the result_url; otherwise it returns the job id so you can poll Get Job Result. Each successfully processed image consumes account credits.</td></tr><tr><td>Schedule Image Processing</td><td><code>scheduleImageProcessing</code></td><td>Schedules an asynchronous image processing job (upscale, enhance, remove or generate background, edit, inpaint or outpaint, resize, print sizing, captions, presets) and returns the job id immediately. Poll Get Job Result with the returned job id until the status is complete, or supply a webhooks.complete URL to be notified. Each successfully processed image consumes account credits.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Image Processing Completed</td><td><code>complete</code></td><td>Fired by Deep Image when a processing job finishes. Deep Image has no webhook registration API, so the delivery URL must be supplied in one of two ways: (1) per request - pass this trigger's webhook URL as webhooks.complete in the Schedule Image Processing or Process Image action (the recommended, self-service path), or (2) account-wide - email support@deep-image.ai and ask them to set the URL as your account webhook (visible under 'webhooks' in Get Account Information). Deliveries are unsigned JSON POSTs containing status='complete', the job id, the original request parameters as data, the result_url and (for multi-image jobs) results.</td></tr></tbody></table>
