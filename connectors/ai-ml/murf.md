---
description: "Murf AI — text-to-speech, voice changer, translation, instant voice cloning and Murf Dub automation."
hidden: true
---

# Murf

Murf AI — text-to-speech, voice changer, translation, instant voice cloning and Murf Dub automation. Wraps the Murf REST API at https://api.murf.ai (OpenAPI 3.1). Authenticates with the account api-key header.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [murf.ai](https://murf.ai) |
| **Authentication** | API key |
| **Actions** | 19 |
| **Events** | 1 |
| **Slug** | `murf` |

## Use it

Add Murf from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.murf.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Change Voice In Audio | `changeVoiceInAudio` | METERED — consumes the account's character quota. Voice conversion: re-speak an existing recording, supplied as a publicly reachable file_url, in a Murf stock voice. Returns audio_file (a presigned, UNAUTHENTICATED download URL), audio_length_in_seconds, optional transcription and remaining_character_count. Only file_url is supported here; direct binary file upload is not carried by the fastn multipart engine. |
| Create Dub Job | `createDubJob` | METERED — consumes dubbing credits. Submit a standalone dubbing job for a media file given as file_url, into one or more target locales. Returns job_id; poll Get Dub Job Status, or set webhook_url and webhook_secret to receive the DUB_JOB completion webhook instead. Requires a Murf Dub API key. Binary file upload is not carried by the fastn multipart engine, so use file_url. |
| Create Dub Job In Project | `createDubJobInProject` | METERED — consumes dubbing credits. Submit a dubbing job inside an existing Murf Dub project, inheriting that project's dubbing type and target locales. Supply the media as file_url. Returns job_id for Get Dub Job Status. Requires a Murf Dub API key. |
| Create Dub Project | `createDubProject` | Create a Murf Dub project that groups dubbing jobs under one name, dubbing type (AUTOMATED or QA) and set of target locales. Returns project_id for Create Dub Job In Project. Requires a Murf Dub API key. |
| Create Instant Voice Clone | `createInstantVoiceClone` | CONSENT REQUIRED — only clone a voice you own or have explicit recorded permission to clone. Creates an instant voice clone from a reference recording (WAV/MP3/FLAC/ALAW/ULAW, max 40 MB) and returns a requestId to poll with Get Voice Clone Creation Status. The reference audio must be sent as a real binary multipart part, which the fastn multipart engine does not carry, so this action is wired for the endpoint's text fields only. Requires the Instant Voice Cloning entitlement. |
| Delete Cloned Voice | `deleteClonedVoice` | Permanently delete one instant voice clone by its voiceId. Irreversible — the clone must be recreated from the original reference audio. Requires the Instant Voice Cloning entitlement. |
| Generate Auth Token | `generateAuthToken` | SECURITY WARNING — the response body contains a LIVE bearer token for this Murf account. Anything that receives this action's output can call the whole Murf API as you. Exchanges the api-key for a short-lived token (expiryInEpochMillis) for client-side or WebSocket use. Do not log, store or forward the result. |
| Get Dub Job Status | `getDubJobStatus` | Poll a dubbing job by job_id: overall status, per-locale download_details with download_url and download_srt_url, credits_used, credits_remaining and any failure_reason. This is the same payload Murf delivers on the DUB_JOB webhook. Requires a Murf Dub API key. |
| Get Voice Clone Creation Status | `getVoiceCloneCreationStatus` | Poll the status of an instant voice clone created by Create Instant Voice Clone, using the requestId that call returned. Requires the Instant Voice Cloning entitlement; accounts without it receive 403 {"error_message":"HTTP 403 Forbidden"}. |
| List Cloned Voices | `listClonedVoices` | List the instant voice clones owned by this account, with their voiceId, tag and display name. Requires the Instant Voice Cloning entitlement; accounts without it receive 403 {"error_message":"HTTP 403 Forbidden"}. |
| List Dub Destination Languages | `listDubDestinationLanguages` | List the target locales Murf Dub can dub INTO, for use as target_locales on a dub job or project. Requires a Murf Dub API key; a TTS key returns 403 "Invalid 'api-key' header passed, this may be tts api key pls pass dub api key instead". |
| List Dub Projects | `listDubProjects` | List the Murf Dub projects on the account with their project_id, name, dubbing_type and target_locales. Requires a Murf Dub API key; a TTS key returns 403 "Invalid 'api-key' header passed, this may be tts api key pls pass dub api key instead". |
| List Dub Source Languages | `listDubSourceLanguages` | List the source locales Murf Dub can dub FROM. Murf Dub Automation is a separate product with its own API key: connect this connector with a Dub API key to use the dubbing family. A TTS key returns 403 "Invalid 'api-key' header passed, this may be tts api key pls pass dub api key instead". |
| List Voices | `listVoices` | List every Murf stock voice available to the account: voiceId, displayName, locale, gender, accent, available styles and supported locales. Optional `model` filter (GEN2 or FALCON-2). Free — consumes no characters. Use the returned voiceId with Synthesize Speech, Stream Speech or Change Voice In Audio. |
| List Voices For Model | `listVoicesForModel` | Undocumented path-parameter variant of the voice catalogue: GET /v1/speech/voices/{model}. Returns the voice list for one TTS model (GEN2 or FALCON-2); the two catalogues differ. Free — consumes no characters. |
| Stream Speech | `streamSpeech` | METERED — consumes the account's character quota. Low-latency streaming synthesis: returns the raw audio bytes of the spoken text (chunked transfer, no JSON envelope) using a Murf stock voice. Prefer Synthesize Speech when you want a downloadable file and the remaining-quota figure. |
| Synthesize Speech | `synthesizeSpeech` | METERED — consumes the account's character quota. Convert text to a finished audio file with a Murf stock voice. Returns audioFile (a presigned, UNAUTHENTICATED download URL valid ~3 days), audioLengthInSeconds, wordDurations, consumedCharacterCount and remainingCharacterCount. remainingCharacterCount is the only place the API exposes the account balance. |
| Translate Text | `translateText` | METERED — consumes the account's character quota. Translate one or more strings into a target language, returning the source and translated text per entry plus the character counts consumed and remaining. Pair with Synthesize Speech to voice the translation. |
| Update Dub Project | `updateDubProject` | Change the target locales of an existing Murf Dub project, identified by project_id from List Dub Projects. Requires a Murf Dub API key. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Dub Job Finished | `DUB_JOB` | Murf's only webhook. Fires when a Murf Dub job completes, fails or partially completes. THERE IS NO SUBSCRIBE OR UNSUBSCRIBE API: registration is per job. To receive it, pass this trigger's URL as webhook_url (and a shared secret as webhook_secret) on the Create Dub Job or Create Dub Job In Project action; that job is then the only source of deliveries, and you stop them by not passing webhook_url on the next job. Murf signs each delivery with X-Signature-Timestamp and X-HMAC-Signature = HMAC-SHA256(webhook_secret, compact-JSON payload + timestamp); verify it and reject stale timestamps. Requires a Murf Dub API key. payloadSchema is MODELLED from Murf's published webhook documentation and its Get Dub Job Status response shape - no live delivery was capturable because the account's TTS key is refused by the dubbing product. |
