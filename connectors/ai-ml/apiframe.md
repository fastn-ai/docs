---
description: "Apiframe is a single REST API for 70+ generative media models, including Midjourney, Flux, Nano Banana, Ideogram, Imagen, GPT Image, Kling, Veo, Sora, Suno,…"
---

# Apiframe

Apiframe is a single REST API for 70+ generative media models, including Midjourney, Flux, Nano Banana, Ideogram, Imagen, GPT Image, Kling, Veo, Sora, Suno, Udio and Topaz. This connector covers the complete Apiframe v2 API: image, video and music generation, image and video upscaling and editing, background removal, Midjourney, Suno and Udio follow-up actions, Udio lyrics and audio uploads, asynchronous job tracking, the model catalog, media assets, short-lived file uploads, personal LoRA training and account information.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [apiframe.ai](https://apiframe.ai) |
| **Authentication** | Credentials you enter |
| **Actions** | 24 |
| **Events** | 3 |
| **Slug** | `apiframe` |

## Use it

Add Apiframe from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.apiframe.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive LoRA | `archiveLora` | Soft-deletes a personal Flux LoRA by flipping its status to ARCHIVED so it no longer appears in listings, and makes a best-effort cleanup of the trained model upstream. Idempotent: archiving an already-archived LoRA also succeeds with no content. |
| Create Asset | `createAsset` | Downloads the media at a public URL and stores it permanently in Apiframe storage. Creation is synchronous: the asset is immediately Active and can be referenced as asset://{assetId} in any media URL field of a generation request. Unlike short-lived uploads, assets do not expire and there is no delete endpoint. Limits: 25 MB for images and audio, 50 MB for video; the declared type must match the file contents. |
| Create LoRA | `createLora` | Uploads 15 to 30 subject photos as multipart form data and queues a personal Flux LoRA training run. Deducts 2 credits up front (refunded if training later fails). The returned id becomes the loraId to pass in fluxLoraParams when generating images with the flux-lora model; poll Get LoRA until status is READY. |
| Edit Image | `editImage` | Submits an asynchronous inpaint or outpaint job with Flux Fill Pro: repaint a masked region of an image from a prompt, or extend the canvas in a chosen direction. Returns a jobId immediately; poll Get Job or supply a webhookUrl to receive the result. |
| Edit Video | `editVideo` | Submits an asynchronous instruction-based video edit job with Wan 2.7 VideoEdit: restyle, replace or transform an existing clip from a text prompt, optionally anchored by a reference image. Returns a jobId immediately; poll Get Job or supply a webhookUrl to receive the result. |
| Generate Image | `generateImage` | Submits an asynchronous image generation job for any supported image model (Midjourney, Nano Banana, Flux, Seedream, Ideogram, Stable Diffusion, Imagen, DALL-E, GPT Image, Kling Image, Qwen, Wan, Grok, Reve or a trained Flux LoRA). The model value selects which model-specific parameter block applies; only that block is read. Returns a jobId immediately; poll Get Job or supply a webhookUrl to receive the result. Credits are charged per model. |
| Generate Music | `generateMusic` | Submits an asynchronous music generation job for Suno, Udio, Producer, Lyria 3, ElevenLabs Music or Mureka, from a description or your own lyrics. The model value selects which model-specific parameter block applies; only that block is read. Returns a jobId immediately; poll Get Job or supply a webhookUrl to receive the tracks. Credits are charged per model. |
| Generate Video | `generateVideo` | Submits an asynchronous video generation job for any supported video model (Kling, Sora, Seedance, Midjourney Video, Veo, Grok Imagine, Hailuo, Luma Ray, Wan, HappyHorse, Runway or Flux 3), from a text prompt and optionally start/end frames or reference media. The model value selects which model-specific parameter block applies; only that block is read. Returns a jobId immediately; poll Get Job or supply a webhookUrl to receive the result. Credits are charged per model and duration. |
| Get Account Info | `getAccountInfo` | Returns the authenticated user, their team with its remaining credit balance and subscription plan, and the API key used for the request. Useful for verifying credentials and checking credits before submitting jobs. |
| Get Asset | `getAsset` | Returns a stored media asset by id with its status, URL, media type, content type and size. Assets are Active as soon as creation succeeds and can be referenced as asset://{assetId} in generation requests. Only assets created by the caller's team are accessible. |
| Get Job | `getJob` | Returns the current status, progress, submitted input and, once completed, the result of a single generation job. Poll this after submitting a job, or use a webhook instead. |
| Get LoRA | `getLora` | Returns a single personal Flux LoRA by id, including its training status, readiness and trigger word. Poll this to follow a training run started with Create LoRA. |
| List Jobs | `listJobs` | Returns a cursor-paginated list of generation jobs, newest first. Defaults to the caller's own jobs; team admins can pass scope=team to see every job in the team. Filter by status or model, or look up a single job id with search. |
| List LoRAs | `listLoras` | Returns a cursor-paginated list of the personal Flux LoRAs trained by the caller's team, with their training status and readiness. Archived LoRAs are hidden unless includeArchived is true. |
| List Models | `listModels` | Returns the curated catalog of generation models with their identifier, label, modality, description, pricing mode and credit cost range. Optionally filter to image, video or music models. The model id is the value to pass as model when submitting a job. |
| Remove Image Background | `removeImageBackground` | Submits an asynchronous background-removal job using Bria (RMBG 2.0, state-of-the-art alpha matte) or 851-labs (cheap, fast, with cutout and background-style options). Returns a jobId immediately; poll Get Job or supply a webhookUrl to receive the result. |
| Run Midjourney Action | `runMidjourneyAction` | Runs a follow-up action on a completed Midjourney job. Grid actions upsample (U1 to U4) and variation (V1 to V4) act on a grid-producing parent and use index to pick one of the four images; inpaint (Vary Region, with a base64 mask and optional prompt), outpaint (Zoom Out with zoomRatio 1.5 or 2) and pan (direction) act on a completed upsample job. Upsample returns a single image; every other action returns a fresh four-image grid. Returns 409 when the action is not available for the parent job. |
| Run Suno Action | `runSunoAction` | Runs a follow-up action on a completed Suno job: extend continues a track from a timestamp, cover re-generates it in a new style while keeping the core melody, add_vocals layers AI vocals onto an instrumental track (prompt holds the lyrics), and stems splits a track into separate vocal and instrumental files. Select the source track with index (1 or 2) or trackId. Returns a jobId immediately; poll Get Job or supply a webhookUrl. |
| Run Udio Action | `runUdioAction` | Runs a follow-up action on a completed Udio job: extend adds up to 32 seconds of new audio before or after the song (placement, output_length, lyrics options), and remix generates the song again a chosen distance from the original (remix_strength, crop_range). Select the source track with index (1 or 2) or trackId. Songs made with a udio130 model cannot be extended. Returns a jobId immediately; poll Get Job or supply a webhookUrl. |
| Upload Audio to Udio | `uploadAudioToUdio` | Copies audio from a public URL onto Udio's storage so later Udio generations can reference it. The job result is { url }; pass that URL as udioParams.style_ref.file (generate in its style) or udioParams.voice.file (sing with its voice) on as many generations as you like. Uploads are fingerprinted and refused when the copyright check does not clear. |
| Upload File | `uploadFile` | Uploads a single image, video or audio file as multipart form data to short-lived Apiframe CDN storage (max 25 MB for images and audio, 50 MB for video; the content type is detected from the file bytes) and returns a CDN URL that can be used in any image, video or audio input field of a generation request. Files are purged after roughly one to two hours; use Create Asset for permanent storage. |
| Upscale Image | `upscaleImage` | Submits an asynchronous image upscale job using Topaz Image Upscale (photo-realistic, forensic enlargement) or Clarity Upscaler (creative enhancement that invents detail from a steering prompt). Returns a jobId immediately; poll Get Job or supply a webhookUrl to receive the result. |
| Upscale Video | `upscaleVideo` | Submits an asynchronous video upscale and frame-interpolation job with Topaz Video Upscale, up to 4K and 60 fps. Returns a jobId immediately; poll Get Job or supply a webhookUrl to receive the result. Credits are charged per second of output. |
| Write Udio Lyrics | `writeUdioLyrics` | Has Udio write song lyrics from a description without generating any audio. The job settles in seconds and its result is { lyrics, instrumental, tempo }. Pass duration to match the song you intend to generate, or lyrics to have Udio rewrite existing words. Feed the result back as udioParams.lyrics on Generate Music. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Job Completed | `completed` | Fires when a generation job finishes successfully; the payload carries the job result (images, video or tracks, depending on the modality) and the credits charged. Apiframe has no webhook registration API: deliveries are requested per job. To receive this event, copy this trigger's webhook URL and pass it as webhookUrl (with webhookEvents including "completed") on any Apiframe generation, upscale, edit or follow-up action in this connector. Terminal events are retried up to 10 times with exponential backoff starting at 5 seconds. Payload modelled from the vendor's documented sample (no live delivery was possible on a zero-credit account). |
| Job Failed | `failed` | Fires when a generation job fails; the payload carries the error message. Apiframe has no webhook registration API: deliveries are requested per job. To receive this event, copy this trigger's webhook URL and pass it as webhookUrl (with webhookEvents including "failed") on any Apiframe generation, upscale, edit or follow-up action in this connector. Terminal events are retried up to 10 times with exponential backoff. Payload modelled from the vendor's documented sample (no live delivery was possible on a zero-credit account). |
| Job Progress | `progress` | Fires each time a job's progress percentage updates while it is processing. Apiframe has no webhook registration API: deliveries are requested per job. To receive this event, copy this trigger's webhook URL and pass it as webhookUrl with webhookEvents including "progress" on any Apiframe generation, upscale, edit or follow-up action in this connector. Progress deliveries are best-effort with a single attempt. Payload modelled from the vendor's documented sample (no live delivery was possible on a zero-credit account). |
