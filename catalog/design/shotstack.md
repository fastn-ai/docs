---
description: "Shotstack is a cloud video, image and audio editing service. Render edits, manage templates and generate and manage assets."
hidden: true
---

# Shotstack

<img src="../../.gitbook/assets/connectors/lg/shotstack.png" alt="Shotstack logo">

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [shotstack.io](https://shotstack.io) |
| **Authentication** | API key |
| **Slug** | `shotstack` |

## Setup

Your customers enter their API key for Shotstack when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Shotstack from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Shotstack**.
2. Select **Connect** on the Shotstack card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Shotstack's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Template</td><td><code>createTemplate</code></td><td>Edit API: save a reusable edit as a named template. Returns the new template id.</td></tr><tr><td>Create Upload URL</td><td><code>createUploadUrl</code></td><td>Ingest API: request a short-lived pre-signed S3 URL to upload a file directly to Shotstack. Send the binary file to the returned url with a separate HTTP PUT (that second step is not part of this connector). SECURITY: the response contains a live AWS SigV4 signature and security token valid for 1 hour - treat the whole response as a secret, do not log or forward it. Track the returned id with "Get Source".</td></tr><tr><td>Delete Asset</td><td><code>deleteAsset</code></td><td>Serve API: permanently delete a hosted asset and remove it from the Shotstack CDN. DESTRUCTIVE and irreversible - the media file and its public URL are gone. Confirm with "Get Asset by Render ID".</td></tr><tr><td>Delete Source</td><td><code>deleteSource</code></td><td>Ingest API: permanently delete an ingested source file and all of its renditions. DESTRUCTIVE and irreversible - any edit still referencing the stored source URL will fail afterwards. Confirm with "List Sources".</td></tr><tr><td>Delete Template</td><td><code>deleteTemplate</code></td><td>Edit API: permanently delete a saved template by id. DESTRUCTIVE and irreversible - renders already produced from the template are unaffected, but the template itself cannot be recovered. Confirm with "List Templates".</td></tr><tr><td>Fetch Source</td><td><code>fetchSource</code></td><td>Ingest API: queue a source video, image, audio or font file to be fetched from a URL and stored by Shotstack near the render engine. Optionally request output renditions and extra destinations.</td></tr><tr><td>Generate Asset</td><td><code>generateAsset</code></td><td>Edit API: generate a single AI image, video or audio asset from a text prompt, without rendering a full edit. BILLED IN CREDITS per asset (see "List Generation Models" for per-model pricing); identical repeat requests resolve from the cache free of charge.</td></tr><tr><td>Get Asset</td><td><code>getAsset</code></td><td>Serve API: look up a hosted asset by its Serve asset id. Returns the provider, region, originating render id, filename, filesize, hosting status and the public CDN url. NOTE: that url is publicly readable without an API key.</td></tr><tr><td>Get Asset by Render ID</td><td><code>getAssetByRenderId</code></td><td>Serve API: list every hosted asset produced by a given render id - the video or image plus any poster and thumbnail. This is the bridge from an Edit API render id to the Serve API asset id needed by "Get Asset" and "Delete Asset".</td></tr><tr><td>Get Generation Model</td><td><code>getGenerationModel</code></td><td>Edit API: get one AI generation model by its id, including credit pricing and the JSON Schema of the options it accepts (aspectRatio, resolution, seed, systemPrompt, voice, duration and so on). Use this to build a valid options object for "Generate Asset".</td></tr></tbody></table>

<details>

<summary>View 12 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Generation Status</td><td><code>getGenerationStatus</code></td><td>Edit API: poll an AI generation job by id.</td></tr><tr><td>Get Render Status</td><td><code>getRenderStatus</code></td><td>Edit API: get the status of a render by its id. Poll this after "Render Asset" or "Render Template". status is one of queued, fetching, rendering, saving, done, failed. When status is 'done' the response carries the public output url, and duration/billable seconds.</td></tr><tr><td>Get Source</td><td><code>getSource</code></td><td>Ingest API: get one ingested source file by id - its original input URL, the Shotstack-hosted source URL to use in an edit, processing status, extension, dimensions, duration and filesize, plus any renditions.</td></tr><tr><td>Inspect Media</td><td><code>inspectMedia</code></td><td>Edit API: run a hosted FFprobe against any publicly reachable image, video or audio URL and return its metadata - width, height, duration, codec, bitrate, frame rate, rotation. Useful for sizing clips before building an edit.</td></tr><tr><td>List Generation Models</td><td><code>listGenerationModels</code></td><td>Edit API: list every AI generation model available for text-to-image, text-to-video, image-to-video and text-to-speech, with its type, description and credit pricing. Read this before calling "Generate Asset" so the credit cost of a prompt is known in advance.</td></tr><tr><td>List Sources</td><td><code>listSources</code></td><td>Ingest API: list the ingested source files stored against the account for the current environment, with their input URL, stored source URL, status, dimensions and filesize. Paginated via meta.next.</td></tr><tr><td>List Templates</td><td><code>listTemplates</code></td><td>Edit API: list every template saved against the account for the current environment (stage or v1). Returns the account owner id and an array of {id, name}.</td></tr><tr><td>Render Asset</td><td><code>renderAsset</code></td><td>Edit API: queue a video, image or audio render from a JSON edit (timeline + output). ASYNCHRONOUS - Poll "Get Render Status" with that id until status is 'done' to obtain the output URL. Sandbox (stage) output is watermarked.</td></tr><tr><td>Render Template</td><td><code>renderTemplate</code></td><td>ASYNCHRONOUS</td></tr><tr><td>Retrieve Template</td><td><code>retrieveTemplate</code></td><td>Edit API: retrieve a single saved template by id, including its full stored edit (timeline and output) and any merge placeholders.</td></tr><tr><td>Transfer Asset</td><td><code>transferAsset</code></td><td>Serve API: fetch a file from any publicly available URL and transfer it to one or more Serve API destinations (shotstack CDN hosting, s3, mux, googleDrive, vimeo, tiktok, azure, gcs, akamai). The id you supply is stored as the asset's renderId, NOT as its asset id - confirm the transfer with "Get Asset by Render ID" passing that same id, which returns the generated Serve asset id and the public CDN url.</td></tr><tr><td>Update Template</td><td><code>updateTemplate</code></td><td>Edit API: replace a saved template by id with a new name and edit. This is a full replacement, not a patch - send the complete template body. Confirm with "Retrieve Template".</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Render or ingest completed</td><td><code>done</code></td><td>Shotstack POSTs this when an asynchronous job finishes successfully. For an Edit API render, type is 'edit', action is 'render' and url is the finished media file. Fired for renders submitted via Render Asset or Render Template, and for sources submitted via Fetch Source.</td></tr><tr><td>Render or ingest failed</td><td><code>failed</code></td><td>Shotstack POSTs this when an asynchronous job fails. The error property carries the reason. Same payload shape as the 'done' event with status 'failed' and no url.</td></tr></tbody></table>
