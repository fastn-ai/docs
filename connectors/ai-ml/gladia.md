---
description: "Gladia is a speech-to-text and audio intelligence API for pre-recorded and real-time transcription with diarization, translation, summarization, subtitles,…"
hidden: true
---

# Gladia

<img src="../../.gitbook/assets/connectors/lg/gladia.png" alt="Gladia logo">

Gladia is a speech-to-text and audio intelligence API for pre-recorded and real-time transcription with diarization, translation, summarization, subtitles, named entity recognition, sentiment analysis, PII redaction and custom vocabulary. This connector covers the Gladia v2 API: file upload from a URL, pre-recorded transcription jobs (initiate, get result, list, delete), live transcription sessions (initiate, get, list, delete), job history and the available models catalogue, plus the account-level webhook events.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [gladia.io](https://gladia.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `gladia` |

## Use it

Add Gladia from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.gladia.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Live Session | `deleteLiveSession` | Deletes a live transcription session and all of its data (the recorded audio file and the transcription). Returns an empty 202 Accepted response; the deletion is processed asynchronously. |
| Delete Pre-recorded Transcription | `deletePreRecordedTranscription` | Deletes a pre-recorded transcription job and all of its data (the audio file and the transcription result). Returns an empty 202 Accepted response; the deletion is processed asynchronously. |
| Download Live Session Audio File | `downloadLiveSessionAudioFile` | Downloads the audio file recorded during a live transcription session. Returns the raw audio bytes as a file reference (name, MIME type, size and base64 data). Returns 404 when no audio was recorded for the session. |
| Download Pre-recorded Audio File | `downloadPreRecordedAudioFile` | Downloads the audio file used for a pre-recorded transcription job. Returns the raw audio bytes as a file reference (name, MIME type, size and base64 data). |
| Get Live Session | `getLiveSession` | Retrieves a live (real-time) transcription session by id, including its status (queued, processing, done or error), the session parameters, recorded file metadata and, once the session has ended, the full transcript with utterances and any enabled add-on results. |
| Get Pre-recorded Transcription | `getPreRecordedTranscription` | Retrieves a pre-recorded transcription job by id, including its status (queued, processing, done or error), the submitted parameters, file metadata and, once done, the full transcript with utterances, word timings, detected languages and any enabled add-on results such as diarization, translation, summarization, subtitles, sentiment analysis or named entities. |
| Initiate Live Session | `initiateLiveSession` | Creates a real-time transcription session in Gladia's default region and returns its id and a WebSocket URL (with a temporary token) to stream audio to. Configure the audio format (encoding, bit depth, sample rate, channels), language detection, endpointing, real-time add-ons (custom vocabulary, spelling, translation, named entities, sentiment), post-processing summarization, which WebSocket messages to receive and an optional callback URL. To pin the session to a specific region use Initiate Live Session In Region. |
| Initiate Live Session In Region | `initiateLiveSessionInRegion` | Creates a real-time transcription session pinned to a specific Gladia region (us-west or eu-west) and returns its id and a WebSocket URL (with a temporary token) to stream audio to. Accepts the same session configuration as Initiate Live Session: audio format, language detection, endpointing, real-time add-ons, post-processing summarization, WebSocket message selection and an optional callback URL. |
| Initiate Pre-recorded Transcription | `initiatePreRecordedTranscription` | Starts an asynchronous pre-recorded transcription job for an audio or video file reachable by URL (a Gladia upload URL or any public URL). Optional audio-intelligence add-ons include speaker diarization, translation, summarization, subtitles, named entity recognition, sentiment analysis, PII redaction, custom vocabulary and spelling, audio-to-LLM prompts and a per-job callback. Returns the job id and result URL; poll Get Pre-recorded Transcription until the status is done. |
| List Job History | `listJobHistory` | Lists the history of all your jobs across kinds (pre-recorded and live) with offset pagination and optional filters by kind, status, creation date and custom metadata. Returns the page items plus first, current and next page URLs. |
| List Live Sessions | `listLiveSessions` | Lists your live (real-time) transcription sessions with offset pagination and optional filters by status, creation date and custom metadata. Returns the page items plus first, current and next page URLs. Each item has the same shape as Get Live Session. |
| List Models | `listModels` | Lists Gladia's available transcription models with their supported modalities, pricing, readiness and datacenter locations, in the OpenRouter model-catalogue format. Requires no input; useful as a connection health check. |
| List Pre-recorded Transcriptions | `listPreRecordedTranscriptions` | Lists your pre-recorded transcription jobs with offset pagination and optional filters by status, creation date and custom metadata. Returns the page items plus first, current and next page URLs. Each item has the same shape as Get Pre-recorded Transcription. |
| Upload Audio File | `uploadAudioFile` | Imports an audio or video file into Gladia from a publicly reachable URL and returns a Gladia-hosted audio_url plus detected metadata (filename, extension, size, duration, channels). Use the returned audio_url in Initiate Pre-recorded Transcription. Direct multipart file upload is not supported by this action; provide a URL. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Live Recording Ended | `live.end_recording` | Fires when audio recording ends on a live session. Registration is manual: sign in at https://app.gladia.io/webhooks, add a webhook with this connector's shared URL and enable the event. Payload schema modelled from the vendor OpenAPI webhooks definition. |
| Live Recording Started | `live.start_recording` | Fires when audio recording starts on a live session. Registration is manual: sign in at https://app.gladia.io/webhooks, add a webhook with this connector's shared URL and enable the event. Payload schema modelled from the vendor OpenAPI webhooks definition. |
| Live Session Ended | `live.end_session` | Fires when a live transcription session ends and its result is available. Registration is manual: sign in at https://app.gladia.io/webhooks, add a webhook with this connector's shared URL and enable the event. The payload carries the session id; fetch the result with Get Live Session. Payload schema modelled from the vendor OpenAPI webhooks definition. |
| Live Session Started | `live.start_session` | Fires when a live transcription session starts. Registration is manual: sign in at https://app.gladia.io/webhooks, add a webhook with this connector's shared URL and enable the event. The payload carries the session id; fetch details with Get Live Session. Payload schema modelled from the vendor OpenAPI webhooks definition. |
| Pre-recorded Transcription Created | `transcription.created` | Fires when a pre-recorded transcription job is created. Registration is manual: sign in at https://app.gladia.io/webhooks, add a webhook with this connector's shared URL and enable the event. The payload carries the job id; fetch details with Get Pre-recorded Transcription. Payload schema modelled from the vendor OpenAPI webhooks definition. |
| Pre-recorded Transcription Failed | `transcription.error` | Fires when a pre-recorded transcription job fails. Registration is manual: sign in at https://app.gladia.io/webhooks, add a webhook with this connector's shared URL and enable the event. The payload carries the job id; read error_code with Get Pre-recorded Transcription. Payload schema modelled from the vendor OpenAPI webhooks definition. |
| Pre-recorded Transcription Succeeded | `transcription.success` | Fires when a pre-recorded transcription job completes successfully. Registration is manual: sign in at https://app.gladia.io/webhooks, add a webhook with this connector's shared URL and enable the event. The payload carries the job id; fetch the result with Get Pre-recorded Transcription. Payload schema modelled from the vendor OpenAPI webhooks definition. |
