---
description: "Easy-Peasy.AI generative content API."
hidden: true
---

# Easy-Peasy.AI

<img src="../../.gitbook/assets/connectors/lg/easy-peasy-ai.png" alt="Easy-Peasy.AI logo">

Easy-Peasy.AI generative content API. Text generation from 100+ presets/templates, image generation and editing, video and talking-video generation, music and sound-effect generation, audio transcription with speaker detection, AI content from transcriptions, text-to-speech with 150+ voices, an OpenAI-compatible chat completions endpoint, and custom bot chat on the separate bots.easy-peasy.ai host. Authentication is a single x-api-key header. METERED: most generation routes consume account credits and word quota.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [easy-peasy.ai](https://easy-peasy.ai) |
| **Authentication** | API key, OAuth 2.0 |
| **Slug** | `easyPeasyAi` |

## Use it

Add Easy-Peasy.AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.easyPeasyAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Chat Completions | `chatCompletions` | OpenAI-compatible chat completions. Accepts the standard messages array plus model, temperature, max_tokens, top_p, stop and stream, and returns an OpenAI-shaped choices response. Tool calling, response_format and n are not supported. METERED: consumes the account's model token allowance. Note this route also accepts Authorization: Bearer in place of x-api-key. |
| Chat With Bot | `chatWithBot` | Send a message to one of the account's custom AI bots and receive its reply. Runs on the SEPARATE host bots.easy-peasy.ai (a Fastify server, exact-match routing) and uses the same x-api-key. public_url is the bot's identifier from the bot's Integrations then API page in the dashboard - there is no API that lists bots, so it must be copied from the web app. VENDOR QUIRK PROVEN LIVE: an unknown public_url returns 500 {"message":"Internal Server Error"}, not the 404 the vendor documents, so treat a 500 here as a likely bad bot identifier. METERED: consumes the account model token allowance. |
| Create Transcription | `createTranscription` | Start an AI transcription of an audio or video file supplied by URL, optionally with speaker detection and enhanced quality. Asynchronous: returns a uuid to poll with Get Transcription Result. METERED and PAID-PLAN ONLY: free accounts receive 403 {"error":"Subscription required. Please upgrade your plan to access transcription API."}. Submitting again creates another billable job - keep the uuid on a local timeout. |
| Generate Audio | `generateAudio` | Generate speech audio from text. UNDOCUMENTED route discovered by live sweep - absent from the vendor OpenAPI spec. Proven live to be an alias of Generate Text To Speech: same voiceID plus text inputs, and a byte-identical {uuid, url, used_characters, status} response from the same media host. METERED: consumes the account text-to-speech character allowance. SECURITY: the returned MP3 URL is publicly reachable without authentication. |
| Generate Audio Content | `generateAudioContent` | Generate AI content from a completed transcription - summary, title, action items, key points and similar - depending on the recording's audio_type. Pass the transcription UUID as audio_id, and optionally the exact field names to produce. METERED: each requested field consumes generation quota; force re-runs fields that already exist and bills again. |
| Generate Image | `generateImage` | Generate images from a text prompt, or edit supplied images, using an exact model name such as Nano Banana 2 Lite, GPT Image, FLUX or Seedream. Returns image_url values. Set action to 'Edit Image with AI' with image/images plus editModel to edit. METERED and PAID-PLAN ONLY: free accounts receive 401 {"error":"Please upgrade your plan."}. Each output image costs credits. |
| Generate Music | `generateMusic` | Generate AI music from a text description. UNDOCUMENTED route found by live sweep (absent from the vendor OpenAPI spec, docs and sitemap). PROVEN TO EXIST: POST-only, other verbs return 405 "Method not allowed" while a nonsense sibling path returns a 404 HTML page. LIMITATION PROVEN LIVE: a fully-formed POST with a valid x-api-key returns 401 {"error":"Unauthorized"} - byte-distinct from the API-key rejection {"error":"Invalid API key"} - so this route belongs to the Easy-Peasy.AI web app's browser-SESSION auth realm and is not reachable with an API key. Kept for coverage and for the day the vendor opens it to API keys. METERED if enabled. |
| Generate Song | `generateSong` | Generate an AI song from a description or lyrics. UNDOCUMENTED route found by live sweep (absent from the vendor OpenAPI spec, docs and sitemap). PROVEN TO EXIST: POST-only, other verbs return 405 "Method not allowed" while a nonsense sibling path returns a 404 HTML page. LIMITATION PROVEN LIVE: a fully-formed POST with a valid x-api-key returns 401 {"error":"Unauthorized"} - byte-distinct from the API-key rejection {"error":"Invalid API key"} - so this route belongs to the Easy-Peasy.AI web app's browser-SESSION auth realm and is not reachable with an API key. Kept for coverage and for the day the vendor opens it to API keys. METERED if enabled. |
| Generate Sound Effect | `generateSound` | Generate an AI sound effect from a text description using ElevenLabs. Synchronous: the audio URL is returned immediately. METERED: each call consumes sound-generation credits. SECURITY: the returned audio URL is publicly reachable. |
| Generate Talking Video | `generateTalkingVideo` | Animate a face image or video so it speaks. Supply either text plus voiceID to synthesise the speech, or your own audio file URL. Asynchronous: poll the returned id with Get Video. METERED and expensive: avatar video consumes a large credit allowance, and the premium avatarModel costs more than standard. |

<details>

<summary>See 11 more actions</summary>

* **Generate Text** `generateText`: Generate text with one of the Easy-Peasy.AI templates. Pass the preset slug from List Presets plus that preset's fields; call Get Preset Details first to learn which extra1..extra14 fields a preset expects. RESPONSE SHAPE: the vendor returns a TOP-LEVEL JSON ARRAY of generation objects, one per requested output, each {id, text} - it is exposed here as items because the platform rejects a bare-array output contract. METERED: every call consumes the account word quota and API token allowance, and each extra output bills again.
* **Generate Text To Speech** `generateTextToSpeech`: Convert text to speech with one of the 150+ AI voices. Pass a voiceID from Get Text To Speech Voices. The generated audio is returned as a URL. METERED: consumes the account's text-to-speech character allowance. SECURITY: the returned audio URL is publicly reachable without authentication.
* **Generate Video** `generateVideo`: Start an asynchronous video generation from text, a first/last frame image, or reference media, using an exact model title such as Veo 3.1 Fast, MiniMax H3 Max, Seedance 2.5, Kling or WAN 3.0 (see the vendor's video model reference for supported durations and resolutions). Returns an id to poll with Get Video. METERED and expensive: video is the highest credit cost on the platform, and resubmitting after a local timeout creates a second billable job.
* **Get Account** `getAccount`: Return the account that the API key belongs to: user id, email, first and last name. Useful as a credential-verification / whoami call. UNDOCUMENTED route discovered by live sweep (not in the vendor OpenAPI spec). FREE: consumes no credits. Note this route returns the account holder's email address; it does NOT return the API key.
* **Get Image** `getImage`: Retrieve a previously generated media record by its numeric id. Read image_url at the top level; used_credits reports what that generation cost. Images and videos share one record table on this vendor, so a video id is also accepted here and returns an empty image_url. FREE: retrieving an existing record consumes no generation credits. SECURITY: image_url, when populated, is a publicly reachable unauthenticated URL to account content.
* **Get Preset Details** `getPreset`: Retrieve the full configuration of one text-generation preset by slug, including every input field (keywords, extra1..extra14), its label, type, options and constraints. Call this before Generate Text to learn which fields the preset needs. FREE: consumes no credits.
* **Get Text To Speech Configuration** `getTtsConfig`: Retrieve the filter options available for text-to-speech voices: the list of supported languages, accents, genders and use cases. Use the values it returns to filter Get Text To Speech Voices. FREE: consumes no credits.
* **Get Text To Speech Voices** `getTtsVoices`: List the text-to-speech voices available to the account, each with its id, name, description, language, accent and gender. Pass the returned id as voiceID to Generate Text To Speech. Set include_custom to true to include the account's own custom and cloned voices. FREE: consumes no credits.
* **Get Transcription Result** `getTranscription`: Retrieve a transcription by its UUID. Fields are returned at the top level (there is no audio wrapper). Poll every 15-30 seconds while processing: transcription_status 'done' means complete, including a no-speech result with empty content; 'failed' means stop polling. FREE: reading an existing transcription consumes no credits.
* **Get Video** `getVideo`: Retrieve the status and result of a video generation job. Video generation is asynchronous and typically takes 1-5 minutes: poll every 15-30 seconds until status is completed and the url field holds the video URL. FREE: polling consumes no generation credits. SECURITY: the returned url is a publicly reachable link to account content.
* **List Presets** `listPresets`: List every available text-generation preset (template) with its slug, title, description, categories and isFree flag. Use the returned slug with Generate Text. Optionally filter by category. FREE: this route consumes no credits.

</details>
