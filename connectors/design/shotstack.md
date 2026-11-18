---
description: "Shotstack cloud video, image and audio editing API."
---

# Shotstack

Shotstack cloud video, image and audio editing API. Covers the Edit API (render edits, templates, media probe, AI asset generation and generation models), the Serve API (hosted asset lookup, transfer and delete) and the Ingest API (fetch/upload and manage source files). Renders are asynchronous: submit, then poll the render status endpoint for the output URL.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [shotstack.io](https://shotstack.io) |
| **Authentication** | API key |
| **Actions** | 22 |
| **Events** | 2 |
| **Slug** | `shotstack` |

## Use it

Add Shotstack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.shotstack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Template | `createTemplate` | Edit API: save a reusable edit as a named template. Returns the new template id. |
| Create Upload URL | `createUploadUrl` | Ingest API: request a short-lived pre-signed S3 URL to upload a file directly to Shotstack. Send the binary file to the returned url with a separate HTTP PUT (that second step is not part of this connector). SECURITY: the response contains a live AWS SigV4 signature and security token valid for 1 hour - treat the whole response as a secret, do not log or forward it. Track the returned id with "Get Source". |
| Delete Asset | `deleteAsset` | Serve API: permanently delete a hosted asset and remove it from the Shotstack CDN. DESTRUCTIVE and irreversible - the media file and its public URL are gone. Confirm with "Get Asset by Render ID". |
| Delete Source | `deleteSource` | Ingest API: permanently delete an ingested source file and all of its renditions. DESTRUCTIVE and irreversible - any edit still referencing the stored source URL will fail afterwards. Confirm with "List Sources". |
| Delete Template | `deleteTemplate` | Edit API: permanently delete a saved template by id. DESTRUCTIVE and irreversible - renders already produced from the template are unaffected, but the template itself cannot be recovered. Confirm with "List Templates". |
| Fetch Source | `fetchSource` | Ingest API: queue a source video, image, audio or font file to be fetched from a URL and stored by Shotstack near the render engine. Optionally request output renditions and extra destinations. Returns 201 with a source id; poll "Get Source" until status is 'ready'. |
| Generate Asset | `generateAsset` | Edit API: generate a single AI image, video or audio asset from a text prompt, without rendering a full edit. BILLED IN CREDITS per asset (see "List Generation Models" for per-model pricing); identical repeat requests resolve from the cache free of charge. Returns 202 with a job id when queued, or 200 when served from cache - poll "Get Generation Status" for the asset URL. |
| Get Asset | `getAsset` | Serve API: look up a hosted asset by its Serve asset id. Returns the provider, region, originating render id, filename, filesize, hosting status and the public CDN url. NOTE: that url is publicly readable without an API key. |
| Get Asset by Render ID | `getAssetByRenderId` | Serve API: list every hosted asset produced by a given render id - the video or image plus any poster and thumbnail. This is the bridge from an Edit API render id to the Serve API asset id needed by "Get Asset" and "Delete Asset". |
| Get Generation Model | `getGenerationModel` | Edit API: get one AI generation model by its id, including credit pricing and the JSON Schema of the options it accepts (aspectRatio, resolution, seed, systemPrompt, voice, duration and so on). Use this to build a valid options object for "Generate Asset". |
| Get Generation Status | `getGenerationStatus` | Edit API: poll an AI generation job by id. Returns HTTP 202 with status queued/processing while running, and HTTP 200 with status 'done' plus the generated asset url when finished, or status 'failed' with an error string. |
| Get Render Status | `getRenderStatus` | Edit API: get the status of a render by its id. Poll this after "Render Asset" or "Render Template". status is one of queued, fetching, rendering, saving, done, failed. When status is 'done' the response carries the public output url, and duration/billable seconds. |
| Get Source | `getSource` | Ingest API: get one ingested source file by id - its original input URL, the Shotstack-hosted source URL to use in an edit, processing status, extension, dimensions, duration and filesize, plus any renditions. |
| Inspect Media | `inspectMedia` | Edit API: run a hosted FFprobe against any publicly reachable image, video or audio URL and return its metadata - width, height, duration, codec, bitrate, frame rate, rotation. Useful for sizing clips before building an edit. |
| List Generation Models | `listGenerationModels` | Edit API: list every AI generation model available for text-to-image, text-to-video, image-to-video and text-to-speech, with its type, description and credit pricing. Read this before calling "Generate Asset" so the credit cost of a prompt is known in advance. |
| List Sources | `listSources` | Ingest API: list the ingested source files stored against the account for the current environment, with their input URL, stored source URL, status, dimensions and filesize. Paginated via meta.next. |
| List Templates | `listTemplates` | Edit API: list every template saved against the account for the current environment (stage or v1). Returns the account owner id and an array of {id, name}. |
| Render Asset | `renderAsset` | Edit API: queue a video, image or audio render from a JSON edit (timeline + output). ASYNCHRONOUS - returns 201 with a render id only. Poll "Get Render Status" with that id until status is 'done' to obtain the output URL. Sandbox (stage) output is watermarked. |
| Render Template | `renderTemplate` | ASYNCHRONOUS - returns 201 with a render id; poll "Get Render Status" for the output URL. |
| Retrieve Template | `retrieveTemplate` | Edit API: retrieve a single saved template by id, including its full stored edit (timeline and output) and any merge placeholders. |
| Transfer Asset | `transferAsset` | Serve API: fetch a file from any publicly available URL and transfer it to one or more Serve API destinations (shotstack CDN hosting, s3, mux, googleDrive, vimeo, tiktok, azure, gcs, akamai). Returns 200 with status 'queued'. The id you supply is stored as the asset's renderId, NOT as its asset id - confirm the transfer with "Get Asset by Render ID" passing that same id, which returns the generated Serve asset id and the public CDN url. |
| Update Template | `updateTemplate` | Edit API: replace a saved template by id with a new name and edit. This is a full replacement, not a patch - send the complete template body. Confirm with "Retrieve Template". |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Render or ingest completed | `done` | Shotstack POSTs this when an asynchronous job finishes successfully. For an Edit API render, type is 'edit', action is 'render' and url is the finished media file. Fired for renders submitted via Render Asset or Render Template, and for sources submitted via Fetch Source. |
| Render or ingest failed | `failed` | Shotstack POSTs this when an asynchronous job fails. The error property carries the reason. Same payload shape as the 'done' event with status 'failed' and no url. |
