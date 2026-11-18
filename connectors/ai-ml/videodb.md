---
description: "VideoDB is a video database for AI: upload video, audio and image media, index spoken word and scenes, run semantic/keyword/agentic search over media,…"
hidden: true
---

# VideoDB

<img src="../../.gitbook/assets/connectors/lg/videodb.png" alt="VideoDB logo">

VideoDB is a video database for AI: upload video, audio and image media, index spoken word and scenes, run semantic/keyword/agentic search over media, generate streams, clips, thumbnails, dubs and subtitles, run real-time streams (RTStream), record meetings, and manage collections. Wraps the VideoDB REST API at https://api.videodb.io.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [videodb.io](https://videodb.io) |
| **Authentication** | API key |
| **Slug** | `videodb` |

## Use it

Add VideoDB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.videodb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Subtitles To Video | `addSubtitlesToVideo` | Burn styled subtitles onto a video from its transcript and return a new stream. Requires the video to be transcribed or spoken-word indexed first. |
| Aggregate Collection Index | `aggregateCollectionIndex` | Group and aggregate the records of a collection-level V2 index by a field, returning counts or another metric per group. |
| Aggregate Video Index | `aggregateVideoIndex` | Group and aggregate the records of one video's V2 index by a field, returning counts or another metric per group. |
| Ask Collection | `askCollection` | Ask a natural-language question across a whole collection and get an LLM answer grounded in its Search V2 indexes, optionally with the source shots. Billed as an LLM call. |
| Ask Video | `askVideo` | Ask a natural-language question about one video and get an LLM answer grounded in its Search V2 indexes, optionally with the source shots. Billed as an LLM call. |
| Compile Editor Timeline | `compileEditorTimeline` | Compile a VideoDB Editor timeline (tracks of video, audio, image and text clips with transitions) into a playable stream and player URL. Pass timeline_url instead of the inline timeline when the JSON is very large. |
| Compile Shots Into Stream | `compileShots` | Compile one selected shot of a video into a playable stream. The VideoDB endpoint takes a JSON array of shot descriptors; this action sends exactly one shot per call. |
| Compile Timeline | `compileTimeline` | Compile a multi-asset VideoDB timeline (inline video assets plus audio, image and text overlays) into a single playable stream. |
| Connect Real-Time Stream | `createRtstream` | Connect a live RTSP or HLS source to VideoDB as a real-time stream so it can be indexed, transcribed and searched continuously. Billed per hour of real-time compute and storage; VideoDB has no route to delete a stream, only to stop it. |
| Control Real-Time Stream Transcription | `startRtstreamTranscription` | Start or stop continuous speech-to-text on a real-time stream. The stream must have been created with audio in media_types. Billed per minute transcribed while running. |
| Create Capture Session | `createCaptureSession` | Open a real-time capture session in a collection so a browser or device client can stream microphone, screen and system audio into VideoDB over its WebSocket. |
| Create Collection | `createCollection` | Create a new VideoDB collection to group videos, audio files and images. Returns the new collection id. |
| Create Real-Time Index Alert | `createRtstreamIndexAlert` | Register an alert on a real-time stream index using the legacy /index path, so VideoDB calls your webhook whenever indexed content matches an event prompt. |
| Create Real-Time Stream Index | `createRtstreamIndex` | Build a Search V2 index over a real-time stream's understanding output so its live content becomes searchable. |
| Create Real-Time Stream Index Alert | `createRtstreamV2IndexAlert` | Register an alert on a real-time stream's Search V2 index so VideoDB POSTs your webhook whenever live content matches the event prompt. This is the outbound event mechanism for VideoDB real-time streams. |
| Create Real-Time Stream Scene Index | `createRtstreamSceneIndex` | Start a continuous scene index on a real-time stream so each sampled frame is described by a vision model and becomes searchable. Billed per scene indexed for as long as it runs. |
| Create Real-Time Understanding Run | `createRtstreamUnderstanding` | Start a continuous understanding run on a real-time stream with one or more analyzers, producing structured artifacts that stream indexes are built from. |
| Create Sandbox | `createSandbox` | Provision a dedicated GPU sandbox so scene indexing, image generation and LLM calls can run on warm models. Billed per sandbox hour; a sandbox can only be stopped, never deleted. |
| Create Stream Event | `createRtstreamEvent` | Define a named real-time event in natural language (for example 'a person enters the frame'). The returned event id is what an alert on a stream index watches for, and it is the first step in wiring a VideoDB outbound webhook. |
| Create Video Index | `createVideoIndex` | Build a Search V2 index over a video from an understanding artifact, declaring which retrieval capabilities (semantic, query, aggregate) it serves and which artifact fields map to them. |
| Create Video Understanding Run | `createVideoUnderstanding` | Start an understanding run over a video with one or more analyzers (for example spoken_words or visual description), producing structured artifacts that V2 indexes can be built from. Asynchronous. |
| Create Voice Clone | `createVoiceClone` | Clone a voice from a stored reference audio file so it can be used by voice generation. Only clone voices you have the speaker's consent to reproduce. |
| Delete Audio File | `deleteAudio` | Permanently delete a stored audio file from VideoDB. |
| Delete Collection | `deleteCollection` | Permanently delete a VideoDB collection and everything stored inside it. The account default collection cannot be deleted. |
| Delete Image | `deleteImage` | Permanently delete a stored image from VideoDB. |
| Delete Video | `deleteVideo` | Permanently delete a video and all of its derived indexes, scenes and streams from VideoDB. |
| Delete Video Index | `deleteVideoIndex` | Delete a Search V2 index from a video. The source video and its understanding artifacts are kept. |
| Delete Video Scene Collection | `deleteVideoSceneCollection` | Delete an extracted scene collection and its stored frames from a video. |
| Delete Video Scene Index | `deleteVideoSceneIndex` | Delete a scene index from a video, removing its stored scene descriptions and search records. |
| Delete Video Storage | `deleteVideoStorage` | Delete only the stored source file of a video, freeing media storage while keeping the video record and its indexes in VideoDB. |
| Delete Video Understanding Run | `deleteVideoUnderstanding` | Delete an understanding run of a video and the analyzer artifacts it produced. |
| Delete Voice Clone | `deleteVoiceClone` | Permanently delete a cloned voice from the account. |
| Describe Video Frame | `describeVideoFrame` | Run a vision model over a single extracted frame of a video and return a natural-language description of it. Billed as an LLM call. |
| Describe Video Scene | `describeVideoScene` | Run a vision model over a single extracted scene of a video and return a natural-language description of it. Billed as an LLM call. |
| Download Stream As File | `downloadStream` | Render a VideoDB HLS stream link into a downloadable MP4 file and return the download URL. |
| Dub Video Into Language | `dubVideo` | Produce a dubbed copy of a stored video with its speech re-voiced in another language, saved as a new video in the collection. Billed per minute of dubbing. |
| Export Capture Session | `exportCaptureSession` | Turn a finished real-time capture session into a stored video in the collection. The session must have received media over its WebSocket first; a session still in the 'created' state is rejected with 400 'Cannot export session in created state'. |
| Export Editor Timeline | `exportEditorTimeline` | Render a VideoDB Editor timeline into a downloadable MP4 and return a signed download URL. The stream_url must be one produced by Compile Editor Timeline (POST /editor); a stream from Compile Shots Into Stream or Compile Timeline returns 500 'Internal server error timelinev2 download'. The returned URL is unauthenticated. |
| Export Real-Time Stream Segment | `exportRtstreamSegment` | Export a recorded time window of a real-time stream into a stored video in the collection. |
| Extract Video Scenes | `extractVideoScenes` | Split a video into scenes by shot change, fixed time window or transcript boundary, and store the result as a named scene collection. Asynchronous; poll the returned job id. |
| Generate Audio From Prompt | `generateAudio` | Generate music, a sound effect, or spoken voice audio and store it in the collection. Set audio_type to 'music' or 'sound_effect' with a prompt, or to 'voice' with text and a voice name. Billed per generation. |
| Generate Audio Signed URL | `generateAudioSignedUrl` | Issue a time-limited signed URL for downloading or streaming a stored audio file. Treat the returned URL as sensitive: anyone holding it can fetch the audio without an API key. |
| Generate Capture Client Token | `generateCaptureClientToken` | Mint a short-lived client token that lets an untrusted browser or device client drive capture sessions without holding the account API key. SECURITY: the response contains a live bearer credential, so handle and log it as a secret. |
| Generate Clip From Prompt | `generateClipFromPrompt` | Ask a model to assemble a highlight clip from a video by describing what the clip should contain, and return the resulting shots and stream. Billed as an LLM call. |
| Generate Image From Prompt | `generateImage` | Generate an image from a text prompt and store it in the collection. Billed per image generated. |
| Generate Image Signed URL | `generateImageSignedUrl` | Issue a time-limited signed URL for downloading a stored image. Treat the returned URL as sensitive: anyone holding it can fetch the image without an API key. |
| Generate Text From Prompt | `generateText` | Run a prompt through a VideoDB-hosted LLM in the context of a collection and return the generated text or structured JSON. Billed per LLM call at the selected model tier. |
| Generate Video From Prompt | `generateVideo` | Generate a short video from a text prompt and store it in the collection. Billed per video generated. |
| Generate Video Stream | `generateVideoStream` | Build an HLS stream for a video, optionally limited to selected start/end segments of the timeline. Returns the .m3u8 stream URL and a player URL. Billed as a programmable or simple stream. |
| Generate Video Thumbnail | `generateVideoThumbnail` | Capture a thumbnail image from a video at a given timestamp and store it as an image asset in the collection. |
| Get Async Response | `getAsyncResponse` | Poll a long-running VideoDB job (upload, indexing, transcoding, generation) by its async job id. Returns status 'processing' until the job finishes, then the completed job payload. |
| Get Audio File | `getAudio` | Fetch one stored audio file by id, returning its name and duration. |
| Get Audio Transcript | `getAudioTranscript` | Return the stored transcript of an audio file as timed word or sentence segments. |
| Get Billing Usage | `getBillingUsage` | Return the account's VideoDB plan, subscription status, remaining credit balance, credits consumed, the per-unit credit cost of every billable operation, and usage counters for each operation type. |
| Get Capture Session | `getCaptureSession` | Fetch one real-time capture session by id, with its status, metadata, attached streams and export state. |
| Get Collection | `getCollection` | Fetch a single VideoDB collection by id. Pass the literal value 'default' to fetch the account's default collection. |
| Get Collection WebSocket URL | `getCollectionWebsocketUrl` | Return the signed WebSocket endpoint used for VideoDB real-time capture sessions on a collection. The fastn REST engine cannot hold the WebSocket itself; this action only issues the URL for a client that can. |
| Get Current User | `getCurrentUser` | Retrieve the VideoDB account that the API key belongs to, including user id, name, email, default organization id, default collection id and the list of all collection ids the account can access. |
| Get Download Job | `getDownloadJob` | Poll a stream-to-file download job by the id returned from Download Stream As File, and return the signed download URL once rendering has finished. The returned URL is unauthenticated: anyone holding it can fetch the file. |
| Get Image | `getImage` | Fetch one stored image by id, returning its name and storage URL. |
| Get Job Status | `getJobStatus` | Return the status and result of any VideoDB background job by its job id. Answers 404 with 'Job not found' for an id that does not exist. |
| Get Legacy Video Index | `getLegacyVideoIndex` | Read back the records of a legacy spoken-word or scene index on a video, as built by Index Spoken Words. |
| Get Meeting Recording | `getMeetingRecording` | Fetch the status and metadata of a meeting recording bot run, including bot name, meeting title, status and speaker timeline. |
| Get Presigned Upload URL | `getUploadUrl` | Issue a presigned URL for uploading raw file bytes into a collection. Upload the bytes to that URL with a multipart POST, then pass the same URL to Upload Media From URL to register the file with VideoDB. |
| Get Real-Time Stream | `getRtstream` | Fetch one real-time stream by id, returning its name, sample rate, status, collection and creation time. |
| Get Real-Time Stream Index | `getRtstreamIndexLegacy` | Fetch one index of a real-time stream by id using the legacy /index path, returning its configuration and status. |
| Get Real-Time Stream Index Records | `getRtstreamIndexRecords` | Page through the records stored in a real-time stream's Search V2 index, optionally limited to a time window. |
| Get Real-Time Stream Scene Index Records | `getRtstreamSceneIndexRecords` | Page through the scene description records produced by a real-time stream's scene index, optionally limited to a time window. |
| Get Real-Time Stream Segment | `getRtstreamSegment` | Return a playable stream URL for a recorded time window of a real-time stream. |
| Get Real-Time Stream Transcript | `getRtstreamTranscript` | Page through the rolling transcript of a real-time stream, optionally limited to a time window. |
| Get Real-Time Stream V2 Index | `getRtstreamIndex` | Fetch one Search V2 index of a real-time stream by id, returning its configuration, field schema and status. |
| Get Real-Time Understanding Records | `getRtstreamUnderstandingRecords` | Page through the analyzer output records produced by an understanding run on a real-time stream. |
| Get Real-Time Understanding Run | `getRtstreamUnderstanding` | Fetch one understanding run of a real-time stream, returning its analyzers, segmentation config, outputs and status. |
| Get Reframe Result | `getReframeResult` | Poll a reframe job by its reframe id and return the reframed video once it is ready, including its new video id, duration and stream URL. |
| Get Sandbox | `getSandbox` | Fetch one GPU sandbox by id, returning its tier, status, loaded models, region and expiry. |
| Get Transcode Job | `getTranscodeJob` | Return the status and, once finished, the output URL of a transcoding job by its job id. |
| Get Video | `getVideo` | Fetch one stored video by id, returning its name, description, duration, stream URL, player URL and thumbnail URL. |
| Get Video Index | `getVideoIndex` | Fetch one Search V2 index of a video, returning its status, record count, field schema and supported operators. |
| Get Video Index Records | `getVideoIndexRecords` | Page through the raw records stored in one Search V2 index of a video, returning each record with its segment timings and a cursor for the next page. |
| Get Video Meeting Details | `getVideoMeetingDetails` | For a video produced by a meeting recording bot, return the originating meeting's title, URL, bot name, status and speaker timeline. Returns success=false with 'No meeting associated with this video.' for an ordinary uploaded video. |
| Get Video Scene Collection | `getVideoSceneCollection` | Fetch one scene collection of a video, returning every detected scene with its start time, end time and extracted frames. |
| Get Video Scene Index Records | `getVideoSceneIndexRecords` | Return the per-scene description records stored in one scene index of a video. |
| Get Video Thumbnail | `getVideoThumbnail` | Return the default thumbnail URL VideoDB generated for a video at ingest time. |
| Get Video Transcript | `getVideoTranscript` | Return the stored transcript of a video as timed word or sentence segments. Requires that the video has already been transcribed or spoken-word indexed. |
| Get Video Understanding Run | `getVideoUnderstanding` | Fetch one understanding run of a video, including per-analyzer status and, once finished, the analyzer output artifacts. Pass an analyzer name to narrow the response to that analyzer. |
| Get Voice Clone | `getVoiceClone` | Fetch one cloned voice by id, returning its name, description, language and reference audio id. |
| Index Spoken Words | `indexSpokenWords` | Build a spoken-word (transcript) index over a video so it becomes searchable by what is said in it. Asynchronous; poll the returned job id. Billed per minute of spoken indexing. |
| Index Video Scenes | `indexVideoScenes` | Run a vision model over a video's scenes to produce searchable scene descriptions, creating a named scene index. Asynchronous; poll the returned job id. Billed per scene indexed. |
| List Audio Files | `listAudios` | List every audio file stored in a VideoDB collection, with id, name and duration for each. |
| List Capture Sessions | `listCaptureSessions` | List the real-time capture sessions created in a collection, with their status, end user and attached real-time streams. |
| List Collections | `listCollections` | List every VideoDB collection the account can access, and report which collection id is the account default. |
| List Images | `listImages` | List every image stored in a VideoDB collection, including thumbnails and generated images, with the id and URL of each. |
| List Invoices | `listInvoices` | List the billing invoices raised against the VideoDB account. Free-plan accounts return an empty list. |
| List Real-Time Index Alerts | `listRtstreamIndexAlerts` | List the alerts registered on a real-time stream index using the legacy /index path, with their event and enabled state. |
| List Real-Time Stream Index Alerts | `listRtstreamV2IndexAlerts` | List the alerts registered on a real-time stream's Search V2 index, with their event, callback URL and enabled state. Use this to confirm an alert subscription exists in VideoDB. |
| List Real-Time Stream Indexes | `listRtstreamIndexes` | List the Search V2 indexes built over a real-time stream, with their name, status and record counts. |
| List Real-Time Stream Scene Indexes | `listRtstreamSceneIndexes` | List the scene indexes running on a real-time stream, with their name, prompt, extraction config and status. |
| List Real-Time Streams | `listRtstreams` | List the real-time streams (RTStreams) connected to the account, with their name, sample rate, status and collection. |
| List Real-Time Understanding Runs | `listRtstreamUnderstandings` | List the understanding runs attached to a real-time stream, with the analyzers and status of each. |
| List Sandboxes | `listSandboxes` | List the GPU sandboxes provisioned on the account, with tier, status, region and lifecycle timestamps, paginated. |
| List Stream Events | `listRtstreamEvents` | List every real-time event definition on the account, with its id, label and detection prompt. |
| List Video Indexes | `listVideoIndexes` | List the Search V2 indexes built over a video, optionally filtered by retrieval capability, with record counts and field schemas. |
| List Video Scene Collections | `listVideoSceneCollections` | List every scene collection that has been extracted from a video, with the extraction config used for each. |
| List Video Scene Indexes | `listVideoSceneIndexes` | List every scene index built over a video, with the id, name and status of each. |
| List Video Thumbnails | `listVideoThumbnails` | List every thumbnail image that has been captured from a video, with the id and URL of each. |
| List Video Understanding Runs | `listVideoUnderstandings` | List every understanding run created for a video, with the analyzers each run used and its current status. |
| List Videos | `listVideos` | List every video stored in a VideoDB collection, with id, name, length, stream URL, player URL and thumbnail URL for each. |
| List Voice Clones | `listVoiceClones` | List the cloned voices on the account, with name, language and reference audio for each, paginated. |
| Query Collection Index | `queryCollectionIndex` | Run a structured, non-semantic filter query against a collection-level V2 index and return the matching records. |
| Query Video Index | `queryVideoIndex` | Run a structured, non-semantic filter query against one video's V2 index and return the matching records in sorted order. |
| Record Meeting | `recordMeeting` | Send a VideoDB recording bot to join a live video meeting and store the recording in a collection. The bot appears as a visible participant to everyone in the meeting, so only use it on meetings you are entitled to record. Billed per minute recorded. |
| Reframe Video | `reframeVideo` | Re-crop a video (or a segment of it) to a different aspect ratio, optionally using smart subject tracking, and return the reframed stream. Asynchronous. |
| Search Collection | `searchCollection` | Run a legacy semantic or keyword search across every indexed video in a collection and return the matching shots with their source video and timings. Billed per search query. |
| Search Collection Titles | `searchCollectionTitles` | Use an LLM to find the videos in a collection whose titles best match a description, without searching their contents. Billed as an LLM call. |
| Search Collection V2 | `searchCollectionV2` | Run a Search V2 natural-language query across every V2 index in a collection and return ranked shots plus any server warnings. |
| Search Real-Time Stream | `searchRtstream` | Search the indexed scenes and transcript of a single real-time stream and return matching moments with their timestamps. |
| Search Real-Time Streams In Collection | `searchCollectionRtstreams` | Search across every indexed real-time stream in a collection at once and return matching moments with the stream and scene index they came from. |
| Search Video | `searchVideo` | Run a legacy semantic or keyword search inside one video's spoken-word or scene index and return the matching shots with start/end times and scores. Billed per search query. |
| Search Video V2 | `searchVideoV2` | Run a Search V2 natural-language query against one video's V2 indexes. Returns ranked shots plus any server warnings about missing indexes. |
| Search Web Videos | `searchWebVideos` | Search public web video platforms (such as YouTube) from inside a collection and return matching results that can then be ingested. Billed per web search. |
| Semantic Search Collection | `semanticSearchCollection` | Run a vector similarity search across a collection's V2 indexes, optionally restricted by index and field filters, and return the closest records. |
| Semantic Search Video | `semanticSearchVideo` | Run a vector similarity search over one video's V2 indexes, optionally filtered by index name or id and by field filters, and return the closest records. |
| Set Real-Time Index Alert Status | `setRtstreamIndexAlertStatus` | Enable or disable an alert on a real-time stream index using the legacy /index path. VideoDB has no route to delete an alert, only to disable it. |
| Set Real-Time Scene Index Status | `setRtstreamSceneIndexStatus` | Start or stop a running scene index on a real-time stream. Stopping it halts its per-scene billing. |
| Set Real-Time Stream Index Alert Status | `setRtstreamV2IndexAlertStatus` | Enable or disable an alert on a real-time stream's Search V2 index. Disabling is how an alert subscription is cancelled; VideoDB exposes no delete route for alerts. |
| Set Real-Time Stream Index Status | `setRtstreamIndexStatus` | Start or stop a Search V2 index on a real-time stream, halting or resuming its ongoing indexing cost. |
| Set Real-Time Stream Status | `setRtstreamStatus` | Start or stop ingestion of a real-time stream. Stopping is the only way to halt its hourly compute cost. |
| Set Real-Time Understanding Status | `setRtstreamUnderstandingStatus` | Start or stop a continuous understanding run on a real-time stream, halting or resuming its analyzer cost. |
| Start Transcode Job | `startTranscodeJob` | Transcode a source media URL to different resolution, quality, framerate or aspect ratio and return a job id. Billed per transcoding job, which is one of the most expensive VideoDB operations. |
| Stop Sandbox | `stopSandbox` | Stop a running GPU sandbox so it stops accruing hourly cost, optionally after a grace period. VideoDB has no route to delete a sandbox record. |
| Transcribe Audio | `transcribeAudio` | Start speech-to-text transcription of a stored audio file. Asynchronous; poll the returned job id. Billed per minute of transcription. |
| Transcribe Video | `transcribeVideo` | Start speech-to-text transcription of a video. The job is asynchronous; poll the returned async job id with Get Async Response. Billed per minute of transcription. |
| Translate Video Transcript | `translateVideoTranscript` | Translate a video's transcript into another language and return the translated segments. Billed per minute of translation. |
| Update Collection | `updateCollection` | Rename a VideoDB collection, change its description, or toggle whether it is publicly readable. |
| Update Video | `updateVideo` | Change the stored name or description of a video in VideoDB. |
| Upload Media From URL | `uploadMedia` | Ingest a video, audio file or image into a VideoDB collection from a publicly reachable URL (direct file link or a supported platform link). Ingestion is asynchronous: the response carries an async job id that Get Async Response polls until the media id is available. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Job Completed Callback | `job.callback` | VideoDB POSTs here when a long-running job finishes, for any call that was given a callback_url: Upload Media From URL, Index Spoken Words, Index Video Scenes, Extract Video Scenes, Create Video Understanding Run, Create Video Index, Reframe Video, Translate Video Transcript, Dub Video Into Language, Generate Image/Audio/Video/Text, Start Transcode Job, Record Meeting and Create Sandbox. There is no central registration call: the customer passes the fastn trigger URL as callback_url on whichever action they want notified. PAYLOAD SCHEMA IS MODELLED on the completed async-response envelope observed from GET /async-response/{id}; it was not captured from a live callback delivery. |
| Real-Time Stream Alert | `rtstream.alert` | VideoDB POSTs here when a real-time stream's scene index matches an event prompt registered as an alert (for example 'a person walks into the frame'). Subscription registers a VideoDB event definition and an alert on the chosen stream index; unsubscription disables that alert, because VideoDB exposes no delete route for alerts. PAYLOAD SCHEMA IS MODELLED from the alert fields VideoDB returns on List Real-Time Stream Index Alerts and the scene-index record shape; it was not captured from a live delivery, because delivery requires a publicly reachable callback plus a real detection on the stream. |
