---
description: "Elai is an AI video generation platform that turns text, presentations and outlines into avatar-presented videos."
hidden: true
---

# Elai

<img src="../../.gitbook/assets/connectors/elai.png" alt="Elai logo" width="64">

Elai is an AI video generation platform that turns text, presentations and outlines into avatar-presented videos. This connector covers the complete Elai public API v1 at https://apis.elai.io/api/v1: videos (create, list, retrieve, update, delete, copy, translate, render, personalized batch rendering, text/HTML/URL and PPTX import, player payload, exports, SCORM packages, brand kits, edit history), story tools, outlines and LLM speech generation, quizzes, avatars, voices and voice previews, custom voices and voice customizations, media library uploads and folders, slide templates, live avatar streams, users, SSO, workspace API configuration and webhooks. Video rendering consumes plan minutes.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [elai.io](https://elai.io) |
| **Authentication** | Bearer token |
| **Slug** | `elai` |

## Use it

Add Elai from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.elai.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Answer Stream Offer | `answerStreamOffer` | Submit the client's SDP answer to complete the WebRTC handshake for a stream. The endpoint returns 200 even if the GPU host rejects the answer, so check the stream status afterwards. |
| Append Slides From HTML | `appendSlidesFromHtml` | Parse an HTML fragment into slide-sized chunks with speech text and append them to an existing video (or insert them after activeSlideId). The language of the video's first slide is reused. Returns the whole updated video. |
| Apply Brand Kit To Video | `applyBrandKit` | Apply brand colours and/or a logo from a workspace brand kit to a video, either to every slide or to one slide. With persist false the modified video is returned without being saved. Brand kits are plan-gated. |
| Apply Template To Story | `applyTemplateToStory` | Change a story video's slide visuals to those of another template. |
| Build Quiz Question Canvas | `buildQuizQuestion` | Test endpoint: turn quiz question parameters into the canvas object that would be drawn on a slide, returned with a generated (non-persisted) slide id. The response shape is documented as unstable. |
| Build Video From Outline | `buildVideoFromOutline` | Turn an outline into a draft video, optionally with a template, brand kit, folder and mode (video for render-ready slides, story for story-mode slides). Counts against the video creation limit; render the result with Render Video. |
| Check Upload Usage | `checkUploadUsage` | Given a list of asset URLs (stored url values, not signed URLs), report which of them are referenced by at least one video in the workspace. Use it before deleting assets. |
| Close Stream | `closeStream` | Close a live-avatar stream, release its GPU host and finalise the minutes charge. Closing an unknown id returns 200; closing an already-closed stream is an error. |
| Confirm Upload | `confirmUpload` | Confirm that a file was uploaded to a signed URL (or supply the file inline as base64) and register it as a media-library asset, optionally filed into a folder or registered as an avatar frame, logo, brand-kit asset, hidden asset or screen recording. |
| Copy Video | `copyVideo` | Duplicate a video or template, optionally into a folder, or turn a video into a template (and vice versa) with createTemplate. |

<details>

<summary>See 87 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Copy Video By Template (Legacy) | `copyVideoByTemplate` | Deprecated legacy alias of Copy Video (the same handler is mounted at /videos/byTemplate). Kept for older integrations; use Copy Video in new work. |
| Create Outline | `createOutline` | Create an outline either from a topic prompt (8-400 characters) or from an existing video; send exactly one of prompt or videoId. Returns the new outline id. Counts against the account's video creation limit. |
| Create SSO Integration | `createSsoIntegration` | Create the workspace's single SSO integration (Enterprise plans only; a second create returns 409). The protocol-specific config is validated per provider and the redirect URL must be a secure URL on an allowed host. Returns the generated 16-character integrationId used in SSO login URLs. |
| Create Upload Folder | `createUploadFolder` | Create a media-library folder, optionally nested under a parent folder. Names must be unique within the same parent; only root-level folders count against the plan's folder limit. |
| Create Video | `createVideo` | Create a new draft video from a name and an initial set of slides (each with speech, language, voice, voice provider, animation and optional avatar and canvas). The video is not rendered until Render Video is called; videos created over the API always carry the tag api. |
| Create Video From Presentation | `createVideoFromPresentation` | Create a new video from a PPTX or PDF presentation uploaded as a multipart file, optionally applying a template, brand kit, preferred avatar and LLM enhancements. Returns the new video id. |
| Create Video From Text | `createVideoFromText` | Generate a new story-mode video from plain text, an HTML fragment or a public URL. The type path segment selects the parser (html also handles URLs; anything else is read as plain text) and becomes the video's tag unless tags are supplied. |
| Create Voice Customization | `createVoiceCustomization` | Create a named bundle of TTS settings for a voice (ElevenLabs provider only). For a standard voice send language and locale; for a custom voice send customVoiceId instead. Sending both forms, or neither, is rejected. |
| Delete SSO Integration | `deleteSsoIntegration` | Delete the workspace's SSO integration and unlink every user tied to it, so those users fall back to email and password sign-in. |
| Delete Upload | `deleteUpload` | Permanently delete one media-library asset and its stored file. Videos referencing it are not updated. |
| Delete Upload Folder | `deleteUploadFolder` | Recursively and permanently delete a media-library folder, every descendant folder and every asset inside, returning signed URLs of the deleted assets captured just before deletion. Videos referencing those assets are not updated. |
| Delete Uploads | `deleteUploads` | Permanently delete several media-library assets and their stored files. Videos referencing them are not updated; check usage first with Check Upload Usage. |
| Delete User | `deleteUser` | Remove a user from the workspace. All of the user's assets are reassigned to the workspace admin. |
| Delete Video | `deleteVideo` | Completely delete a video. Returns an empty body on success. |
| Delete Voice Customization | `deleteVoiceCustomization` | Delete a voice customization. Slides referencing it are cleared and their cached audio invalidated so they re-synthesise with plain voice settings on the next render. |
| Download SCORM Package | `downloadScormPackage` | Build a SCORM package (2004v4 or 1.2) for a rendered video and return it as a zip file. passingScore and completionRate are mutually exclusive percentages. |
| Generate Outline Chapters | `generateOutlineChapters` | Expand a topic into an ordered set of chapters (title plus bullet points) written onto the outline's drafts. Uses the LLM and is rate limited for API callers. |
| Generate Outline Quiz | `generateOutlineQuiz` | Generate quiz questions from an outline's speeches and add them as quiz drafts. quizSettings, when supplied, overrides the persisted settings for this call only. |
| Generate Outline Script | `generateOutlineScript` | Expand every chapter draft of an outline into a voice-over script and move the outline's status to script. Destructive: re-running replaces every draft's speech. Takes no body. |
| Generate Quiz From Video | `generateQuizFromVideo` | Read the speech of the selected slides and generate quiz questions with an LLM. Nothing is saved: the questions are returned for you to place on slides with Update Video. Requires LLM features on the workspace (409 otherwise). |
| Generate Slide Speech | `generateSlideSpeech` | Write speech for the named slides of a video from their on-canvas content, following free-form enhancement instructions. Use it for slides that have no speech yet; the speech is saved server-side unless fromEditor is true. |
| Generate Slides From Story | `generateSlidesFromStory` | Convert a story video's texts into rendered slide visuals so the video can be rendered. With fixWithLlm true an LLM pass first fills missing text and shortens over-long speech. |
| Get API Configuration | `getApiConfig` | Retrieve the workspace's API configuration (API token presence and outgoing webhook settings: URL, enabled flag, failure counter, technical email) together with the name and email of the workspace admin the token authenticates as. |
| Get Avatar | `getAvatar` | Retrieve a single avatar with its variants. Readable when the avatar belongs to your organization, is in the public catalog, or your workspace is on its allowlist. |
| Get Current User | `getCurrentUser` | Retrieve the identity the API token resolves to (the workspace admin) together with its workspace and organization: plan, minute balance, seat limit, brand kits, pronunciation dictionary and current usage limits. Use it to check remaining minutes before rendering. |
| Get Outline | `getOutline` | Retrieve an outline with its drafts, including any chapters, speeches and quiz questions generated so far. |
| Get Speech Duration | `getSpeechDuration` | Estimate how long a piece of text will take to speak with a given voice before rendering. Provider names are lowercase and the body is validated strictly. |
| Get SSO Integration | `getSsoIntegration` | Retrieve the workspace's SSO integration, or null when SSO has never been configured. The client secret is always returned masked. |
| Get Stream Chat Reply | `getStreamChatReply` | Run Elai's built-in demo conversational agent over a message history and return its reply for a stream. The reply is returned, not spoken; pass it to Speak On Stream to have the avatar say it. The persona is fixed server-side. |
| Get Template | `getTemplate` | Retrieve a single slide template with its full slide content and signed asset URLs, enough to create a video from it with Copy Video. Private templates are readable only by the owning workspace. |
| Get Upload Folder | `getUploadFolder` | Retrieve one media-library folder with its immediate children populated and its ancestor chain (parentUploadFolders) from the root down. A POST despite being a read, because the child sort travels in the body. |
| Get Upload Folder Breadcrumbs | `getUploadFolderBreadcrumbs` | Retrieve the path from the media-library root to a folder, ready to render as breadcrumbs. The first entry is always the synthetic root (Media library, id null). |
| Get Upload Folder Info | `getUploadFolderInfo` | Report how many assets a media-library folder's whole subtree contains and which of them are still referenced by videos; the confirmation step before a recursive delete. |
| Get Upload Signed URL | `getUploadSignedUrl` | Retrieve a signed URL for uploading an image or video directly to Elai storage. PUT the file bytes to the returned URL, then call Confirm Upload with the same URL. |
| Get Video | `getVideo` | Retrieve a video's full document including its slides and rendering status. Once status is ready the url field holds the rendered MP4; on error, data.internalError explains the failure. |
| Get Video Edit History | `getVideoEditHistory` | Retrieve a video's name and its edit-history entries, each with the user who made the change. Note: on an internal failure this endpoint may hang instead of returning an error; treat a timeout as a failure. |
| Get Video Player Payload | `getVideoPlayerPayload` | Retrieve a video shaped for the embedded interactive player: playable slide data, interactivity and signed media URLs. Deleted videos are refused with 403. |
| Get Video Source Links | `getVideoSourceLinks` | For a video generated as an AI summary of a Panopto session, return the original session's name and viewer URL plus the containing folder. Any other video returns 404. |
| Inspect Presentation | `inspectPresentation` | Upload a PPTX or PDF as a multipart file and report how many slides it has and how many lack speaker notes, as a pre-flight check before Create Video From Presentation. Nothing is created and no minutes are consumed. |
| Interrupt Stream Speech | `interruptStreamSpeech` | Stop the avatar's playback immediately and clear anything queued on the stream (barge-in when a viewer starts talking). |
| Invite User | `inviteUser` | Invite a user to your Elai workspace. The invitee receives an email with instructions to set a password. A reviewer can browse, watch and comment on videos but cannot create or edit anything. |
| List Avatar Frames | `listAvatarFrames` | List the decorative frame assets that can be placed around an avatar. Frames are shared catalog content, so this returns every frame in the installation, with optional name search and pagination. |
| List Avatars | `listAvatars` | List all avatars available to the workspace (public catalog plus your organization's custom avatars) with their variants. Set realtime to true to return only avatars that support live streaming. |
| List Custom Voices | `listCustomVoices` | List the cloned or custom voices visible to the caller (organization, workspace or personal). Standard catalog voices are not included; use List Voices for those. |
| List Music Tracks | `listMusicTracks` | List up to 100 background-music (audio) assets of the workspace, most recently updated first. Not paginated. |
| List Streams | `listStreams` | List the workspace's live-avatar streams, newest first, 50 per page, optionally filtered by state (open or closed). |
| List Templates | `listTemplates` | List the slide templates available to the workspace: its own private templates first, then the shared public catalog (about 290 entries, roughly 2.8 MB). Templates are video documents with template settings; thumbnails are signed URLs. |
| List Upload Folder Names | `listUploadFolderNames` | List just the names of every media-library folder in the workspace at any depth, for checking name collisions before creating a folder. |
| List Uploads | `listUploads` | List the workspace's media-library assets (frames, audio and logos excluded). Without a folder, search or type filter only root-level assets are returned; with any of them the search spans all folders. Returned URLs are time-limited signed URLs. |
| List Users | `listUsers` | List the users in your Elai workspace with their role, status and last sign-in time. |
| List Video Exports | `listVideoExports` | List the times a video was exported to an external system (default target panopto), newest first, with the user who exported it. |
| List Videos | `listVideos` | List the workspace's videos with filtering by status, tags, deleted state and template type, sorting and pagination (100 per page maximum). Each slide in the list has avatar, speech and internal data removed; fetch a single video for the full document. |
| List Voice Customizations | `listVoiceCustomizations` | List every saved voice customization in the workspace: named bundles of TTS settings (stability, speed, similarity, style) bound to one voice and referenced from slides via voiceVariantId. |
| List Voices | `listVoices` | List all supported languages with their male and female voices (about 90 language groups, 11 MB). Use the language group name as the slide language and a voice's voice id and voiceProvider when creating slides or synthesising speech. The response is very large; it exceeds what the fastn execute path can return, so call this endpoint out-of-band when the full catalog is needed. |
| Move Upload Folder To Root | `moveUploadFolderToRoot` | Move a media-library folder to the top level of the media library (sends parentUploadFolderId null, as the API requires for the root). Note: the API responds with the folder document as it was before the move; read it back with Get Upload Folder to see the new location. To move it under another folder or rename it, use Update Upload Folder. |
| Move Upload To Folder | `moveUpload` | Move a single media-library asset into a folder, or back to the root when uploadFolderId is omitted. |
| Move Uploads To Folder | `moveUploads` | Move several media-library assets into a folder, or back to the root when uploadFolderId is omitted. Validation is all-or-nothing: a malformed, missing or foreign asset id moves nothing. |
| Open Stream | `openStream` | Allocate a GPU host, start a live-avatar WebRTC session and return the SDP offer to answer. Requires an avatar with real-time support (List Avatars with realtime true). Streaming minutes are billed at half the normal rate; a workspace with no minutes left is rejected with 429. |
| Preview Voice Customization | `previewVoiceCustomization` | Synthesise a fixed sample sentence (translated to the requested locale) with the supplied stability and speed so a voice customization can be auditioned before it is saved. Returns base64 MP3 and its duration. |
| Regenerate Outline Quiz | `regenerateOutlineQuiz` | Replace the questions on the named quiz drafts of an outline, optionally steering the model away from topics already covered by other questions. |
| Regenerate Outline Speech | `regenerateOutlineSpeech` | Regenerate the speech on the named outline drafts, applying a free-form enhancement instruction. Drafts with a chapter are regenerated from that chapter; drafts without one from the linked video's matching slide. |
| Regenerate Quiz Question | `regenerateQuizQuestion` | Rephrase (improve wording, keeping type and answer count; use instructions) or regenerate (reshape via quizType and answersCount; instructions rejected) one quiz question. Stateless: nothing is persisted. |
| Render Personalized Batch | `renderPersonalizedBatch` | Create (and by default render) a batch of up to 200 personalized videos from a template video whose text and media carry tags. Each templateData row maps tag names to replacement values or media URLs. A 200 means the batch was queued; outcomes arrive per video through the video_ready and video_error webhooks. Rendering consumes plan minutes. |
| Render Video | `renderVideo` | Queue rendering of an existing video (or re-render a failed one). A 200 means the render was accepted, not completed: validation runs afterwards and failures arrive as a video_error webhook or as status error on Get Video. Rendering consumes plan minutes. |
| Renegotiate Stream | `renegotiateStream` | Ask the GPU host for a fresh SDP offer for an already-open stream, to recover a dropped peer connection without losing the session. Answer it with Answer Stream Offer. |
| Revoke API Token | `revokeApiToken` | Clear the workspace's entire API configuration: the API token and the configured outgoing webhook (URL, secret, technical email). Warning: self-revoking and not recoverable through the API; access can only be restored from the Elai web app. |
| Rewrite Outline Speech | `rewriteOutlineSpeech` | Rewrite the speech on the named outline drafts following explicit free-form instructions. |
| Rewrite Slide Speech | `rewriteSlideSpeech` | Rewrite the existing speech on the named slides of a video following free-form enhancement instructions. The result is saved server-side unless fromEditor is true. |
| Rotate API Token | `generateApiToken` | Generate a new 32-character API token for the workspace and return it. Warning: this rotates the token used to make the call, so the connection's stored token stops working immediately and must be replaced with the returned value. |
| Search Upload Folders | `searchUploadFolders` | List media-library folders matching a filter (always scoped to your workspace). Without match.parentUploadFolderId only root-level folders are returned; pass it to list a folder's children. On lower plans each folder carries an isLimited flag. |
| Send Stream ICE Candidate | `sendStreamCandidate` | Forward one trickle-ICE candidate to the stream's GPU host. Call it once per candidate the browser emits. |
| Set Webhook Secret | `setWebhookSecret` | Set the shared secret Elai signs each webhook delivery with. Once set, every delivery carries Elai-Timestamp and Elai-Signature (HMAC-SHA256 hex of '&lt;timestamp&gt;.&lt;raw body&gt;'). Subscribe first: the secret is only stored while a webhook is enabled, and a new secret replaces the old one immediately. Confirm with Get API Configuration. |
| Speak On Stream | `speakOnStream` | Synthesise text and stream the avatar speaking it over the open WebRTC connection. Queued behind anything already playing; use Interrupt Stream Speech to cut in. |
| Submit Custom Voice Recording | `submitCustomVoiceRecording` | Attach a recording link to an existing custom Voice document, name it and submit it to the Elai team for manual voice creation. Requires an organization admin. |
| Subscribe Webhook | `subscribeWebhook` | Subscribe the workspace to the video_ready and video_error webhook events, or replace the URL of the existing subscription. There is one webhook per workspace: posting again overwrites it. The URL must be HTTPS and must not contain localhost. Deliveries are a single attempt with a 10-second timeout; after 10 failed deliveries the webhook is disabled. |
| Synthesize Speech Preview | `synthesizeSpeech` | Render text with a voice and return the audio inline as base64 MP3 plus its duration and, when available, word timings. When videoId and slideId are supplied the result is written into that slide's audio cache. Long text and premium voices depend on the plan. |
| Translate Video | `translateVideo` | Translate a video into another language, producing a new video. Both the language code (locale, e.g. so-So) and the language name (e.g. Somali) are required and are not interchangeable; optional male and female Azure voices can be pinned. |
| Unsubscribe Webhook | `unsubscribeWebhook` | Deactivate the workspace's active webhook so video_ready and video_error events are no longer delivered. |
| Update Avatar | `updateAvatar` | Set a custom avatar's name and code, and supply its footage: a link to a folder with video footage for studio and selfie avatars, or base64 image files for mascot avatars. |
| Update Outline | `updateOutline` | Edit an outline in place: replace its chapters or its drafts (mutually exclusive), change the quiz settings or the status. At least one field is required and unknown fields are rejected. |
| Update SSO Integration | `updateSsoIntegration` | Replace the SSO integration's protocol, invite-only flag, anonymize flag and redirect URL, and merge the supplied config over the stored one. Send the masked clientSecret back unchanged to keep it. Returns 404 when the workspace has no integration yet. |
| Update Upload Folder | `updateUploadFolder` | Rename a media-library folder, or move it under a different parent (omit the parent id, or pass an empty value, for the top level). Rename wins: when name is present the parent change is ignored, so send two requests to do both. |
| Update User | `updateUser` | Change a workspace user's role. Role descriptions are on the Workspace Settings page; a reviewer can browse, watch and comment on videos but cannot create or edit anything. |
| Update Video | `updateVideo` | Update a video's name, slides, tags, public flag, render settings, folder or template settings. Only the fields you pass are sent. |
| Update Voice Customization | `updateVoiceCustomization` | Rename a voice customization and/or replace its settings. At least one of name or settings is required; settings is replaced wholesale, so send all four values. |
| Upload Custom Voice For Slide | `uploadCustomVoice` | Upload an MP3 file as the voice-over of a specific slide (multipart part named file). Rate limited to 20 requests per minute and 200 per hour. |
| Upload Music Track | `uploadMusicTrack` | Upload an audio file (multipart part named file) as a background-music asset for a video. Non-MP3 input is transcoded to MP3; a file whose name already exists in the workspace overwrites that asset's record. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Video Error | `video_error` | Fires when a video hits a validation or rendering error (render failures never surface as an HTTP error on the render call). The error field summarises what went wrong. Same single-attempt delivery and per-workspace subscription as Video Ready. Payload modelled from the vendor's documented example; no failing render was provoked on this account. |
| Video Ready | `video_ready` | Fires when a video's status changes to ready after rendering (also for each video of a personalized batch). Elai delivers one POST per event with a single attempt and a 10-second timeout, no retries; after 10 failed deliveries the workspace webhook is disabled. There is exactly one webhook per workspace, so subscribing replaces any previously registered URL. Payload modelled from the vendor's documented example (https://elai.readme.io/reference/webhooks-overview); no render was run on this free account (renders consume minutes). Deliveries carry Delivery-ID, and Elai-Timestamp plus Elai-Signature (HMAC-SHA256 hex of '&lt;timestamp&gt;.&lt;raw body&gt;') when a secret is set with Set Webhook Secret. |
