---
description: "ElevenLabs AI audio API — text-to-speech, speech-to-text, voice changer (speech-to-speech), sound effects, voice design, voices/models/user management,…"
hidden: true
---

# ElevenLabs

<img src="../../.gitbook/assets/connectors/lg/elevenlabs.png" alt="ElevenLabs logo">

ElevenLabs AI audio API — text-to-speech, speech-to-text, voice changer (speech-to-speech), sound effects, voice design, voices/models/user management, history, dubbing, pronunciation dictionaries, and usage stats. Base URL https://api.elevenlabs.io.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [elevenlabs.io](https://elevenlabs.io) |
| **Authentication** | API key |
| **Slug** | `elevenlabs` |

## Use it

Add ElevenLabs from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.elevenlabs.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Pronunciation Dictionary from File | `addPronunciationDictionaryFromFile` | Create a pronunciation dictionary from a .pls lexicon file. Send multipart/form-data. FREE: no character cost. Returns the new dictionary metadata. |
| Add Voice (Clone) | `addVoice` | Create a new instant voice clone from audio samples. Send multipart/form-data with name and audio files. FREE of character cost but consumes a voice slot. Returns { voice_id, requires_verification }. |
| Create Dubbing | `createDubbing` | Start a dubbing job that translates and re-voices a media file or URL into a target language. Send multipart/form-data. COST: charges based on media duration. Returns { dubbing_id, expected_duration_sec }. |
| Create Voice (from Preview) | `createVoice` | Save a designed voice preview as a permanent voice using a generated_voice_id from Design Voice. FREE of character cost but consumes a voice slot. Returns the new voice object. |
| Delete Dubbing | `deleteDubbing` | Delete a dubbing job by ID. FREE: no character cost. Returns { status }. |
| Delete History Item | `deleteHistoryItem` | Delete a history item by ID. FREE: no character cost. Returns { status }. |
| Delete Voice | `deleteVoice` | Delete a voice by ID. FREE: no character cost. Returns { status }. |
| Design Voice (Text to Voice Preview) | `designVoice` | Generate candidate voice previews from a text description (voice design). Returns base64 audio previews + generated_voice_id values to use with Create Voice. COST: charges credits/characters for the preview generation. Keep text short to validate cheaply. |
| Download History | `downloadHistory` | Download one or more history items as audio. A single ID returns one audio file; multiple IDs return a zip. FREE: no character cost. Returns binary. |
| Edit Voice | `editVoice` | Update an existing voice's name, description, labels, or replace its sample files. Send multipart/form-data. FREE: no character cost. Returns { status }. |

<details>

<summary>See 22 more actions</summary>

* **Edit Voice Settings** `editVoiceSettings`: Update the default settings (stability, similarity_boost, style, speed, use_speaker_boost) for a voice. FREE: no character cost. Returns { status }.
* **Get Character Usage Stats** `getCharacterUsageStats`: Get character/credit usage metrics over a time window, optionally broken down by voice/model/etc. FREE: no character cost. start_unix/end_unix are UTC milliseconds.
* **Get Dubbed Audio** `getDubbedAudio`: Download the dubbed audio/video for a completed dubbing job in a given language. FREE: no character cost. Returns binary.
* **Get Dubbing** `getDubbing`: Get the status and metadata of a dubbing job. FREE: no character cost. Poll until status is 'dubbed'.
* **Get History Item** `getHistoryItem`: Get metadata for a single history item by ID. FREE: no character cost.
* **Get History Item Audio** `getHistoryItemAudio`: Download the audio for a previously generated history item. FREE: no character cost (replays existing audio). Returns binary audio.
* **Get Pronunciation Dictionary** `getPronunciationDictionary`: Get a pronunciation dictionary and its rules by ID. FREE: no character cost.
* **Get User** `getUser`: Get the authenticated user's profile and subscription summary. FREE: no character cost.
* **Get User Subscription** `getUserSubscription`: Get the authenticated user's detailed subscription info, including character usage/limits, invoices and pending changes. FREE: no character cost. Use this to check remaining character quota before TTS.
* **Get Voice** `getVoice`: Get metadata and settings for a single voice by ID. FREE: no character cost.
* **Get Voice Settings** `getVoiceSettings`: Get the stability/similarity/style/speed settings for a voice. FREE: no character cost.
* **List History** `listHistory`: List generated speech history items (TTS/STS) with metadata. FREE: no character cost. Paginated via start_after_history_item_id.
* **List Models** `listModels`: List all available TTS/STT/STS models with capability flags and cost factors. FREE: no character cost. Useful to discover model_id values (e.g. eleven_flash_v2_5).
* **List Pronunciation Dictionaries** `listPronunciationDictionaries`: List pronunciation dictionaries in your workspace. FREE: no character cost. Cursor-paginated.
* **List Shared Voices** `listSharedVoices`: Browse the public Voice Library of shared community/professional voices. FREE: no character cost. Paginated by page/page_size.
* **List Voices** `listVoices`: List all voices available to your account (v2, paginated). FREE: no character cost. Returns voice_id, name, category, labels, settings and pagination tokens.
* **Sound Generation (Sound Effects)** `soundGeneration`: Generate a sound effect from a text prompt. Returns binary audio (MP3 default). COST: charges credits/characters. Keep duration_seconds small (e.g. 0.5) when validating to minimize cost.
* **Speech to Speech (Voice Changer)** `speechToSpeech`: Transform source audio into a target voice while preserving delivery/emotion. Send multipart/form-data with an audio file. Returns binary audio. COST: charges characters/credits based on audio length.
* **Speech to Text (Transcribe)** `speechToText`: Transcribe audio to text with the Scribe model. Send multipart/form-data with a file or a source_url. Returns JSON with text, detected language and word-level timing. COST: charges per minute of audio.
* **Text to Speech (Convert)** `textToSpeech`: Convert text into speech audio with a chosen voice. Returns binary audio (application/octet-stream). Billed per character. COST: charges characters. To minimize cost when validating, use the cheapest model eleven_flash_v2_5 and a 1-2 word text (e.g. 'Hi').
* **Text to Speech Stream** `textToSpeechStream`: Stream synthesized speech as it is generated (text/event-stream of audio chunks). Lower time-to-first-byte for real-time playback. COST: charges characters. Cheapest model eleven_flash_v2_5; use a 1-2 word text to validate cheaply.
* **Text to Speech with Timestamps** `textToSpeechWithTimestamps`: Convert text to speech and return JSON with base64 audio plus character-level timing alignment. Useful for captions/lip-sync. COST: charges characters. Cheapest model eleven_flash_v2_5; validate with a 1-2 word text.

</details>
