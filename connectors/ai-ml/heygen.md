---
description: "HeyGen is an AI video platform for avatar videos, voice cloning and text-to-speech, lip-sync, video translation and agentic video generation."
hidden: true
---

# HeyGen

<img src="../../.gitbook/assets/connectors/heygen.ico" alt="HeyGen logo" width="64">

HeyGen is an AI video platform for avatar videos, voice cloning and text-to-speech, lip-sync, video translation and agentic video generation. This connector covers the HeyGen v3 API: videos and templates, video batches, Video Agent sessions, HyperFrames renders, avatars and looks, voices and speech, lipsyncs, video translations and proofread sessions, AI clipping, filler-word removal, background removal, assets, brand kits and glossaries, podcasts, workflows, video-quality comparisons, custom agents, users, API keys and webhook endpoints and events.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [heygen.com](https://heygen.com) |
| **Authentication** | API key |
| **Slug** | `heygen` |

## Use it

Add HeyGen from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.heygen.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Append Avatar Realtime Text | `appendAvatarRealtimeText` | Appends a text delta to a text_stream realtime session; the avatar speaks fragments in order. Set final=true on the last delta to close input (further appends return 410). Returns total buffered bytes. |
| Bulk Asset Statuses | `bulkAssetStatuses` | Returns statuses for up to 100 assets in one request, addressed by comma-separated asset_ids and/or batch_ids. Each entry carries its id as video_id; not_found for unknown/unowned ids. |
| Bulk Lipsync Statuses | `bulkLipsyncStatuses` | Returns statuses for up to 100 lipsyncs in one request, addressed by comma-separated lipsync_ids and/or batch_ids. Each entry carries its id as video_id; not_found for unknown/unowned ids. |
| Bulk Video Statuses | `bulkVideoStatuses` | Returns statuses for up to 100 videos in one request, addressed by comma-separated video_ids and/or batch_ids. Statuses: queued, processing, completed, failed, or not_found for unknown/unowned ids. |
| Bulk Video Translation Statuses | `bulkVideoTranslationStatuses` | Returns statuses for up to 100 video translations in one request, addressed by comma-separated video_translation_ids and/or batch_ids. Each entry carries its id as video_id; not_found for unknown/unowned ids. |
| Cancel Avatar Realtime Session | `cancelAvatarRealtimeSession` | Cancels a running streaming avatar session. Idempotent: cancelled is true when this request initiated the cancellation, false when the session was already terminal. |
| Cancel Workflow Run | `cancelWorkflowRun` | Requests cancellation of a workflow run. Idempotent for every state: 200 reflects the settled terminal outcome (canceled, or already finished unchanged); 503 when cancellation cannot be confirmed. |
| Clone Voice | `cloneVoice` | Creates a voice clone from an audio file (URL, uploaded asset ID or base64 data). Returns a voice_clone_id to poll with Get Voice until its status is complete. Consumes a voice-clone slot. |
| Complete Asset Upload | `completeAssetUpload` | Finalizes a direct-to-S3 upload into a reusable asset. Call after the upload PUT returns 200. Idempotent. |
| Complete Asset Upload Batch | `completeAssetBatch` | Finalizes every uploaded file in an asset batch after all PUTs return 200; each file is validated and ingested independently. Returns the batch_id; poll Get Asset Batch. Idempotent. |

<details>

<summary>See 130 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create AI Clipping | `createAiClipping` | Submits a source video for AI clipping and returns a job id immediately (consumes credits). Produces one or more short clips per output_settings. Poll Get AI Clipping or subscribe to ai_clipping.success / ai_clipping.fail webhooks. |
| Create Asset Upload | `createAssetUpload` | Begins a direct-to-S3 upload. Returns an asset_id and presigned upload_url plus headers; PUT the file bytes to upload_url, then call Complete Asset Upload. No bytes flow through the API. |
| Create Asset Upload Batch | `createAssetUploadBatch` | Requests up to 100 presigned direct-to-S3 upload URLs in one call. Returns batch_id and one upload slot per file (asset_id, upload_url, headers). PUT each file, then call Complete Asset Upload Batch. |
| Create Avatar | `createAvatar` | Creates a new avatar from an image (type photo), video footage (type digital_twin) or a text prompt (type prompt). Training is asynchronous; poll the returned look with Get Avatar Look. Variants: prompt requires name and prompt; photo and digital_twin require name and file. Private avatars need a completed consent flow before use. Consumes credits. |
| Create Avatar Consent | `createAvatarConsent` | Initiates the consent flow for an avatar group and returns a URL for the user to complete approval in their browser (expires in 24h, single use). Required before a private avatar can be used for video generation. Optionally pass consent_video (url / asset_id / base64) to submit the consent recording directly; then no url is returned. |
| Create Avatar Looks | `createAvatarLooks` | Generates new looks for an existing avatar from a Look Pack template. reference_look_id is an existing look used as identity reference; new looks are added to its avatar. Billed on acceptance (1 API credit per generated look). Returns new look ids; poll Get Avatar Look until completed or failed. |
| Create Avatar Realtime Session | `createAvatarRealtimeSession` | Starts a low-latency streaming avatar session and returns a stream_id. Modes by type: tts (avatar_id, text, voice_id), audio (avatar_id, audio asset), text_stream (avatar_id, voice_id, initial text; then append deltas via Append Avatar Realtime Text). Poll Get Avatar Realtime Session for status and HLS URL. Consumes credits. |
| Create Background Removal | `createBackgroundRemoval` | Submits a video to remove its background (async, consumes credits). Poll Get Background Removal with the returned id; when completed the job carries presigned URLs for requested layers (foreground, mask, background). request_id is the idempotency key (re-sending returns the original job). |
| Create Brand Glossary | `createBrandGlossary` | Creates a brand glossary (custom pronunciation terms plus Don't Translate / Force Translate rules). name must be unique in the workspace (409 on duplicate). Pass brand_glossary_id when creating videos or translations. |
| Create Brand Kit | `createBrandKit` | Creates a brand kit by importing logos, colors and fonts from a public website. Returns brand_kit_id with status loading; poll Get Brand Kit every 2-5s until completed. You confirm you hold rights to the imported assets. |
| Create Custom Agent Video | `createCustomAgentVideo` | Kicks off a custom-agent run from a topic prompt (consumes credits). Returns a video_id immediately; poll Get Custom Agent Video for status and rendered MP4 URL. Asset URLs come from Create Asset Upload. |
| Create Filler Word Removal | `createFillerWordRemoval` | Submits a video and returns a job id immediately (charged per source minute, 1-minute minimum; auto-refunded if nothing changes). Transcribes, removes filler words and overlong silences, renders one cleaned video. Poll Get Filler Word Removal or use filler_word_removal.success / .fail webhooks. |
| Create Hyperframes Render | `createHyperframesRender` | Renders a HyperFrames composition (HTML+JS+assets project as a .zip supplied by url, asset_id or base64) into a video (consumes credits). Returns render_id; poll Get Hyperframes Render. |
| Create Lipsync | `createLipsync` | Replaces the audio on an existing video and re-animates the speaker's lip movements to match (consumes credits). mode: speed or precision. Returns lipsync_id; poll Get Lipsync. |
| Create Lipsync Batch | `createLipsyncBatch` | Submits up to 100 lipsync payloads (same shape as Create Lipsync) as one batch, each processed independently (consumes credits). Returns batch_id; poll Get Lipsync Batch. |
| Create Or Retrain Audio Voice | `createModelAudioVoice` | Creates a model-backed professional audio voice from recordings (at least 20 minutes of the same speaker), or retrains an existing one when voice_id is supplied. When creating a NEW voice, mode ('professional'), name and language are all required by the API (verified live). PENDING while training; poll Get Audio Voice until ACTIVE or FAILED. Needs a free professional-voice slot (plan-gated: resource_limit_reached otherwise). |
| Create Podcast | `createPodcast` | Generates a multi-avatar conversational podcast video from a topic and/or source files plus host and guest avatars/voices (consumes credits; workspace feature gate may return 403). Poll Get Podcast with the returned podcast_id. |
| Create Proofread Session | `createProofread` | Creates a proofread session that extracts editable subtitles from a video before final translated rendering (consumes credits). Returns one proofread_id per target language; edit the SRT, then Generate Video From Proofread. |
| Create Video | `createVideo` | Creates a video (consumes credits). Discriminated by type: avatar (avatar_id + script/voice_id or audio), image (image asset + script/audio), cinematic_avatar (prompt + avatar_id), studio (scenes[] of avatar_video/image/video). Engines avatar_iii/iv/v via engine.type (default avatar_iv). Returns video_id; poll Get Video or use callback_url / webhooks. |
| Create Video Agent Session | `createVideoAgentSession` | One-shot video generation from a prompt: the agent handles scripting, avatar selection, scene composition and rendering (consumes credits). mode generate (fire-and-forget, default) or chat (multi-turn via Send Video Agent Message). Returns session_id and video_id when available. |
| Create Video Batch | `createVideoBatch` | Submits up to 100 video creation payloads (each identical in shape to Create Video: type avatar/image/cinematic_avatar/studio plus settings) in one request and returns a batch_id immediately (consumes credits). Poll Get Video Batch for per-item video ids and statuses. |
| Create Video Quality Comparison | `createVideoQualityComparison` | Submits one pairwise video quality comparison judged on a question_id. Completed comparisons return 200 with result; still-processing ones return 202 to poll via Get Video Quality Comparison. |
| Create Video Quality Comparison Batch | `createVideoQualityComparisonBatch` | Submits up to 100 pairwise video quality comparisons for asynchronous processing. Returns batch_id; poll Get Video Quality Comparison Batch. |
| Create Video Translation | `createVideoTranslation` | Translates a video into one or more target languages with voice cloning and lip-sync (consumes credits). Returns one video_translation_id per language. mode: speed (default) or precision. Language names from List Supported Translation Languages. |
| Create Video Translation Batch | `createVideoTranslationBatch` | Submits up to 100 video-translation payloads (same shape as Create Video Translation) as one batch; a payload with several output_languages expands to one item per language (consumes credits). Returns batch_id; poll Get Video Translation Batch. |
| Create Webhook Endpoint | `createWebhookEndpoint` | Registers an HTTPS URL to receive webhook event notifications. Returns the endpoint details and a signing secret (HMAC-SHA256 of the raw body, sent in the signature header). The secret is only shown at creation and rotation; store it securely. |
| Create Workflow | `createWorkflow` | Atomically creates a workflow and publishes its product graph as immutable version 1 (validated and compiled first). Invalid graphs return 422 graph_invalid; a duplicate name in the space returns 409. Node types from List Workflow Node Types. |
| Delete AI Clipping | `deleteAiClipping` | Soft-deletes an AI clip job and its clips. |
| Delete Asset | `deleteAsset` | Permanently deletes an asset belonging to the caller's workspace. |
| Delete Audio Voice | `deleteModelAudioVoice` | Deletes a model-backed professional audio voice you own. A voice cannot be deleted while its status is PENDING. Repeating a successful deletion returns the same success response. |
| Delete Avatar Group | `deleteAvatarGroup` | Permanently deletes an avatar group and all its associated looks. Cannot delete public or community groups. Returns the deleted group id. |
| Delete Avatar Look | `deleteAvatarLook` | Deletes an avatar look and its backing resource. Supported types: photo_avatar, digital_twin, and kit-based looks; studio avatar looks cannot be deleted via the API. Warning: deleting the last look in a group also deletes the parent group. |
| Delete Background Removal | `deleteBackgroundRemoval` | Soft-deletes a background removal job. |
| Delete Brand Glossary | `deleteBrandGlossary` | Deletes a brand glossary. Cannot be undone; already-generated videos are unaffected. |
| Delete Brand Kit | `deleteBrandKit` | Deletes a brand kit with its colors, logos and fonts. Cannot be undone; kits shared from another workspace return 403. |
| Delete Hyperframes Render | `deleteHyperframesRender` | Soft-deletes a HyperFrames render. Subsequent GETs return 404. |
| Delete Lipsync | `deleteLipsync` | Permanently deletes a lipsync job and its associated files. This action cannot be undone. |
| Delete Podcast | `deletePodcast` | Soft-deletes a podcast so it no longer appears in get/list. Does not cancel in-flight generation. Idempotent; returns an empty data object. |
| Delete Proofread Session | `deleteProofread` | Deletes a proofread session, removing it from listings and projects. Requires Creator role or higher. Cannot be undone. |
| Delete Video | `deleteVideo` | Permanently deletes a video and its associated files. This action cannot be undone. |
| Delete Video Translation | `deleteVideoTranslation` | Permanently deletes a video translation and its associated files. This action cannot be undone. |
| Delete Voice | `deleteVoice` | Deletes a voice clone you own, freeing a slot against your clone limit. The voice must not be in use by a template. Deleting an unknown or already-deleted voice returns 404 voice_not_found. |
| Delete Webhook Endpoint | `deleteWebhookEndpoint` | Permanently removes a webhook endpoint. Events will no longer be delivered to its URL. This cannot be undone. |
| Design Voice | `designVoice` | Returns up to 3 voices matching a natural-language description (e.g. 'warm, confident female narrator'). Use the seed parameter to get different batches of results. |
| Download Proofread SRT | `downloadProofreadSrt` | Returns presigned download URLs for the edited and original SRT files of a completed proofread session. |
| Generate Model Speech | `generateModelSpeech` | Generates speech with an ACTIVE professional (model-backed) audio voice and returns the URL of one mono PCM16 44.1 kHz WAV file. The request stays open until synthesis finishes. Rate limit 30 requests per minute per workspace member. Consumes credits. |
| Generate Speech | `generateSpeech` | Synthesizes speech audio from text (plain text or SSML) with a starfish-compatible voice and returns a URL to the audio file with its duration and word-level timestamps. Speed range 0.5-2.0x. Consumes credits. |
| Generate Video From Proofread | `generateFromProofread` | Starts final translated video generation using the approved subtitles from a proofread session (consumes credits). Returns a video_translation_id to poll with Get Video Translation. |
| Generate Video From Template | `generateFromTemplate` | Generates a video from a template by replacing its variables (text, image, video, audio, character, voice); consumes credits. scene_ids selects/reorders/repeats existing scenes. Returns the created video object; poll Get Video or use webhooks. |
| Get AI Clipping | `getAiClipping` | Returns the full AI clipping job resource including produced clips, statuses, live progress and presigned download URLs. |
| Get Asset | `getAsset` | Returns metadata for an asset in the caller's workspace including owner, upload timestamp, file type, and a publicly accessible URL. |
| Get Asset Batch | `getAssetBatch` | Returns an asset upload batch's aggregate status and one page of items with their ids (returned as video_id, holding the asset_id) and statuses. |
| Get Audio Voice | `getModelAudioVoice` | Returns one model-backed professional audio voice you own and its lifecycle state: PENDING (queued or training), ACTIVE (ready for inference) or FAILED (terminal, with failure_reason). |
| Get Avatar Group | `getAvatarGroup` | Returns details for a specific avatar group including name, gender, preview URLs, looks count, consent and training status. |
| Get Avatar Look | `getAvatarLook` | Returns details for a specific avatar look including supported engines, preferred orientation, preview URLs, and training status. The look id is the avatar_id to pass to Create Video. |
| Get Avatar Realtime Session | `getAvatarRealtimeSession` | Gets the status of a streaming avatar session: pending, streaming (hls_url live), completed (end_reason), or error (error_message). Poll after Create Avatar Realtime Session until hls_url is present. |
| Get Background Removal | `getBackgroundRemoval` | Returns a background removal job including its status and, once completed, presigned download URLs for the produced layers. |
| Get Brand Glossary | `getBrandGlossary` | Returns one brand glossary with its full term list, Don't Translate terms and Force Translate rules. |
| Get Brand Kit | `getBrandKit` | Returns one brand kit with its colors, logos and fonts and their role assignments. Collections are provisional while status is loading and final once completed (or error on failed import). |
| Get Current API Key | `getCurrentApiKey` | Returns non-secret metadata, expiration, and permission scopes for the API key used to authenticate this request. This endpoint accepts API-key authentication only and does not require the key to grant itself a permission scope. |
| Get Current User | `getCurrentUser` | Returns the authenticated user's profile, remaining credits or balance, and billing details. |
| Get Custom Agent | `getCustomAgent` | Returns metadata for a single custom agent. |
| Get Custom Agent Video | `getCustomAgentVideo` | Returns a custom-agent video run's status and the presigned output MP4 URL once the workflow completes. |
| Get Filler Word Removal | `getFillerWordRemoval` | Returns the filler word removal job: status, progress, and once completed the presigned URL of the cleaned video plus removal statistics (num_cuts, reduction_pct, durations). |
| Get Hyperframes Render | `getHyperframesRender` | Returns full details for a single HyperFrames render, including status and signed video_url when complete. |
| Get Lipsync | `getLipsync` | Returns details for a lipsync job including status, video_url, caption_url, and failure info if applicable. |
| Get Lipsync Batch | `getLipsyncBatch` | Returns a lipsync batch's aggregate status and one page of items with their ids (returned as video_id) and statuses. |
| Get Podcast | `getPodcast` | Returns a podcast's status and, once completed, its video_url, thumbnail_url, and duration. |
| Get Proofread Session | `getProofread` | Returns the status and details of a proofread session. |
| Get Template | `getTemplate` | Returns template details including its variable schema (with current default values) and scenes. Variable defaults are returned in the shape the generate request accepts. Only draft version 4 templates are supported. |
| Get Video | `getVideo` | Returns details for a video including status, video_url, thumbnail_url, duration, and failure info if applicable. |
| Get Video Agent Session | `getVideoAgentSession` | Returns the current status, progress, video_id, and recent chat messages (max 40, newest first) for a video agent session. |
| Get Video Agent Session Resource | `getVideoAgentResource` | Returns a single video agent session resource (image, video, draft, avatar, voice, etc.) by its resource_id. |
| Get Video Batch | `getVideoBatch` | Returns a video batch's aggregate status and one page of items with their video ids and statuses (queued, processing, completed, failed). |
| Get Video Quality Comparison | `getVideoQualityComparison` | Returns the latest state and result or terminal error for one video quality comparison. |
| Get Video Quality Comparison Batch | `getVideoQualityComparisonBatch` | Returns aggregate video quality comparison batch status, counts, and one cursor-paginated page of comparison items. |
| Get Video Scenes | `getVideoScenes` | Returns a video's scenes with the video-level context (title, aspect ratio, resolution, caption, brand glossary), reflecting editor edits. Each scene has background, elements (avatar/image/video, open set) and script (text/audio/silence). Never paginated. |
| Get Video Translation | `getVideoTranslation` | Returns details for a translation job including status, output language, video_url, caption URLs, and failure info if applicable. |
| Get Video Translation Batch | `getVideoTranslationBatch` | Returns a video-translation batch's aggregate status and one page of items with their ids (returned as video_id) and statuses. |
| Get Voice | `getVoice` | Returns details for a specific voice, including clone workflow status when available. Use it to poll a voice clone until its status is complete. |
| Get Workflow | `getWorkflow` | Returns a single workflow definition, including its current mutable draft graph, draft_revision and latest published version. |
| Get Workflow Run | `getWorkflowRun` | Returns a single workflow run: pinned version, timestamps, aggregate node progress, sanitized terminal error, and every declared output (media outputs carry a fresh read-time URL). |
| Get Workflow Version | `getWorkflowVersion` | Returns a single immutable, compiled workflow version, including its product graph and plan summary. |
| List AI Clipping Jobs | `listAiClipping` | Returns a cursor-paginated list of AI clip jobs in the workspace, newest first, each embedding its clips array (default limit 10). |
| List Assets | `listAssets` | Beta. Lists a workspace member's uploaded assets, newest first, cursor-paginated. username (the asset owner value, e.g. from Get Current User) is required while in beta. Optional folder_id narrows to one folder. |
| List Audio Voices | `listModelAudioVoices` | Returns the model-backed professional audio voices in the workspace, newest first, with cursor pagination. |
| List Avatar Groups | `listAvatarGroups` | Returns a paginated list of avatar groups (characters); each group contains one or more looks. Filterable by ownership. |
| List Avatar Looks | `listAvatarLooks` | Returns a paginated list of avatar looks (outfits, poses, styles). Filterable by group_id, avatar_type, and ownership. The look id is the avatar_id to pass when creating a video. Cursor pagination via token/next_token. |
| List Background Removals | `listBackgroundRemovals` | Returns a paginated list of background removal jobs for the account, newest first. |
| List Brand Glossaries | `listBrandGlossaries` | Lists brand glossaries (custom term mappings, a.k.a. brand voices) in the workspace. Pass brand_glossary_id when creating a video or translation. |
| List Brand Kits | `listBrandKits` | Returns brand kits in the workspace (colors, fonts, logos). Use brand_kit_id with Create Video Agent Session for on-brand videos. |
| List Custom Agents | `listCustomAgents` | Returns the installed custom agents. Each entry carries id, name, description, and the internal workflow_type. |
| List Hyperframes Renders | `listHyperframesRenders` | Returns a cursor-paginated list of HyperFrames renders in the account, newest first. |
| List Lipsyncs | `listLipsyncs` | Returns a paginated list of all lipsync jobs in the account. |
| List Podcasts | `listPodcasts` | Returns a paginated list of podcasts in the workspace, newest first (workspace feature gate may return 403). |
| List Proofread Sessions | `listProofreads` | Returns a paginated list of all proofread sessions in the workspace, newest first. |
| List Supported Translation Languages | `listVideoTranslationLanguages` | Returns all supported target language names for video translation (values accepted by Create Video Translation output_languages). |
| List Templates | `listTemplates` | Returns a paginated list of API-ready templates in the workspace. Templates are created in the HeyGen web editor; only templates with variables defined are listed. |
| List Video Agent Session Videos | `listVideoAgentSessionVideos` | Returns all videos produced within a Video Agent session, newest first. |
| List Video Agent Sessions | `listVideoAgentSessions` | Returns a paginated list of video agent sessions for the authenticated user, newest first. |
| List Video Agent Styles | `listVideoAgentStyles` | Returns curated visual style templates for Video Agent sessions (scene composition, pacing, aesthetics). Filter by tag (e.g. cinematic, retro-tech). |
| List Video Translations | `listVideoTranslations` | Returns a paginated list of all video translation jobs in the account. |
| List Videos | `listVideos` | Returns a paginated list of all videos in the account. Filterable by folder_id or title substring. Cursor pagination via token/next_token. |
| List Voices | `listVoices` | Returns a paginated list of voices, filterable by type, engine, language, and gender. Use engine=starfish for voices compatible with the Generate Speech endpoint. |
| List Webhook Endpoints | `listWebhookEndpoints` | Returns a paginated list of registered webhook endpoints. The signing secret is never returned here (only on create and rotate). |
| List Webhook Event Types | `listWebhookEventTypes` | Returns all available webhook event types with human-readable descriptions. |
| List Webhook Events | `listWebhookEvents` | Returns a paginated history of delivered webhook events, filterable by event type or entity ID. |
| List Workflow Node Types | `getWorkflowNodeTypes` | Discovery catalog of authorable workflow node types, grouped by family with per-variant config schema and ports. Publishing a version remains the authoritative validation. |
| List Workflow Run Nodes | `listWorkflowRunNodes` | Paginated per-node diagnostics for one workflow run: node id, node type, status, timestamps, and a sanitized error for failed nodes. |
| List Workflow Runs | `listWorkflowRuns` | Returns a paginated list of runs for the workflow named by the required workflow_id, newest first (compact status rows). |
| List Workflow Versions | `listWorkflowVersions` | Returns a paginated list of immutable, compiled versions for a workflow definition. |
| List Workflows | `listWorkflows` | Returns a paginated list of workflow definitions. |
| Publish Workflow Version | `publishWorkflowVersion` | Compiles the product graph in the request body and persists it as the next immutable version (201; 200 if identical to the latest). The workflow draft is neither read nor modified. Version history is append-only. |
| Rotate Webhook Signing Secret | `rotateWebhookEndpointSecret` | Generates a new signing secret for a webhook endpoint and immediately invalidates the old one. Store the new secret securely; it will not be shown again. |
| Search Audio | `searchAudioSounds` | Semantically searches the audio catalog by natural-language description: type music (default) for background music or type sound_effects for SFX. Returns tracks ranked by similarity, each with a pre-signed download URL, with cursor pagination. |
| Search Stock Assets | `searchAssets` | Semantically searches re-hosted public images and icons (or your personal assets) by natural-language description. Returns assets ranked by similarity with stable URLs, cursor-paginated. |
| Send Video Agent Message | `sendVideoAgentMessage` | Sends a follow-up message to an existing chat-mode video agent session to answer questions, add context, or request edits. Returns a run_id. |
| Start Workflow Run | `createWorkflowRun` | Starts a run of a workflow (latest published version unless version_number given), validating inputs against the frozen plan. Returns the run with pinned version, status, progress counts and declared outputs. Consumes credits for generative nodes. |
| Stop Video Agent Session | `stopVideoAgentSession` | Halts an active video agent run at its next checkpoint. Partial results are preserved. |
| Stream Avatar Realtime Word Timestamps | `streamAvatarRealtimeWords` | Opens the bounded Server-Sent Events stream of per-word timestamps for a realtime session and returns it in full as raw text once it ends. Each data: frame is {"words":[{word,start,end}]} in seconds; ends with an event: end frame. Completed sessions are served from a durable snapshot. |
| Stream Model Speech | `streamModelSpeech` | Generates speech with an ACTIVE professional audio voice as a bounded server-sent-event stream, returned here as raw text: audio events carry ordered base64-encoded WAV parts, alignment events are included when with_timestamps is true, and the stream ends with data: [DONE]. Rate limit 30 requests per minute per workspace member. Consumes credits. |
| Update Avatar Group | `updateAvatarGroup` | Updates an avatar group. Currently supports setting default_voice_id: the voice becomes the avatar's default for video generation and is linked to the group if it was not already. Accepts any voice available to your workspace, including imported voice clones. Only supported for avatars you own; public avatars cannot be updated. |
| Update Avatar Look | `updateAvatarLook` | Updates the display name of an avatar look. Only supported for photo avatar and digital twin look types. |
| Update Brand Glossary | `updateBrandGlossary` | Updates a brand glossary. Each field is replaced independently: omitted fields are untouched, a sent list replaces that list in full, an empty array clears it. Renaming to an existing name returns 409. |
| Update Brand Kit | `updateBrandKit` | Updates a brand kit's name or its role assignments (color_roles, logo_roles, font_roles). Omitted fields are unchanged; each role object sent is replaced in full (send {} to clear). Null values are rejected. |
| Update Lipsync | `updateLipsync` | Updates the display title of a lipsync job. |
| Update Video Translation | `updateVideoTranslation` | Updates the display title of a video translation job. |
| Update Webhook Endpoint | `updateWebhookEndpoint` | Updates the URL and/or subscribed event types of a webhook endpoint. The events array is fully replaced, so include every type you want to keep. |
| Update Workflow Draft | `updateWorkflowDraft` | Replaces a workflow's mutable draft product graph. Rejected with 409 if expected_revision is stale and 422 graph_invalid for unavailable node types; the draft is unchanged in both cases. |
| Upload Proofread SRT | `uploadProofreadSrt` | Replaces the proofread subtitles with an edited SRT file referenced by URL or asset id. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Ai Clipping Fail | `ai_clipping.fail` | Fired when an AI clip job fails terminally; no clips produced. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Ai Clipping Success | `ai_clipping.success` | Fired when an AI clip job completes successfully and all clips are rendered. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Avatar Video Caption Fail | `avatar_video_caption.fail` | Fired when caption generation for an avatar video fails. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Avatar Video Caption Success | `avatar_video_caption.success` | Fired when caption generation for an avatar video completes. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Avatar Video Fail | `avatar_video.fail` | Fired when an avatar video fails to render. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Avatar Video Gif Fail | `avatar_video_gif.fail` | Fired when GIF generation from an avatar video fails. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Avatar Video Gif Success | `avatar_video_gif.success` | Fired when a GIF is generated from an avatar video. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Avatar Video Success | `avatar_video.success` | Fired when an avatar video completes rendering successfully. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Batch Finished | `batch.finished` | Fired when a batch job finishes (all its items have reached a terminal created/failed state). Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Filler Word Removal Fail | `filler_word_removal.fail` | Fired when a filler word removal job fails terminally; the charge is refunded. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |

<details>

<summary>See 24 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Filler Word Removal Success | `filler_word_removal.success` | Fired when a filler word removal job completes. num_cuts=0 means the source was clean (charge auto-refunded). Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Hyperframes Video Fail | `hyperframes_video.fail` | Fired when a HyperFrames render fails. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Hyperframes Video Success | `hyperframes_video.success` | Fired when a HyperFrames render completes successfully. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Instant Avatar Fail | `instant_avatar.fail` | Fired when instant avatar training fails. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Instant Avatar Success | `instant_avatar.success` | Fired when an instant avatar finishes training. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Live Avatar Fail | `live_avatar.fail` | Fired when a live avatar session fails to start. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Live Avatar Success | `live_avatar.success` | Fired when a live avatar session starts successfully. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Personalized Video | `personalized_video` | Fired when a personalized video result is ready. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Photo Avatar Add Motion Fail | `photo_avatar_add_motion.fail` | Fired when adding motion to a photo avatar fails. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Photo Avatar Add Motion Success | `photo_avatar_add_motion.success` | Fired when adding motion to a photo avatar succeeds. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Photo Avatar Generation Fail | `photo_avatar_generation.fail` | Fired when photo avatar generation fails. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Photo Avatar Generation Success | `photo_avatar_generation.success` | Fired when photo avatar generation completes. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Photo Avatar Train Fail | `photo_avatar_train.fail` | Fired when photo avatar training fails. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Photo Avatar Train Success | `photo_avatar_train.success` | Fired when photo avatar training completes. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Podcast Fail | `podcast.fail` | Fired when a podcast job fails terminally; no video produced. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Podcast Success | `podcast.success` | Fired when a podcast job completes rendering successfully. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Proofread Creation Fail | `proofread_creation.fail` | Fired when a proofread creation task fails. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Proofread Creation Success | `proofread_creation.success` | Fired when a proofread creation task completes. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Video Agent Fail | `video_agent.fail` | Fired when a Video Agent video fails to render. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Video Agent Success | `video_agent.success` | Fired when a Video Agent video completes rendering successfully. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Video Translate Fail | `video_translate.fail` | Fired when a video translation fails. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Video Translate Preflight Download Failed | `video_translate.preflight.download_failed` | Fired when the download-and-store phase of a video translation's media preflight fails. Only when media-preflight is enabled. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Video Translate Preflight Validation Failed | `video_translate.preflight.validation_failed` | Fired when the pre-download URL validation phase of a video translation fails (HTTP 4xx/5xx, DNS failure, oversized asset). Only when media-preflight is enabled. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |
| Video Translate Success | `video_translate.success` | Fired when a video translation completes successfully. Schema modelled from docs (no captured delivery); HMAC-SHA256 `signature` header with per-endpoint secret, not verified by the trigger. |

</details>
