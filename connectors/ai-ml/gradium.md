---
description: "Gradium is a low-latency speech API for text-to-speech, speech-to-text, voice design and voice cloning."
hidden: true
---

# Gradium

<img src="../../.gitbook/assets/connectors/gradium.png" alt="Gradium logo" width="64">

Gradium is a low-latency speech API for text-to-speech, speech-to-text, voice design and voice cloning. This connector covers the Gradium REST API: text-to-speech synthesis, voice library and custom voices, voice design candidates, pronunciation dictionaries, short-lived WebSocket tokens and credit balance.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [gradium.ai](https://gradium.ai) |
| **Authentication** | Credentials you enter |
| **Slug** | `gradium` |

## Use it

Add Gradium from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.gradium.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Pronunciation Dictionary | `createPronunciationDictionary` | Creates a pronunciation dictionary for the authenticated organization with language-specific rewrite rules. Each rule replaces an original spelling with a rewrite that the text-to-speech model pronounces correctly. Pronunciation dictionaries are applied to WebSocket text-to-speech sessions via pronunciation_id. |
| Create Voice From Candidate | `createVoiceFromCandidate` | Keeps a generated voice design candidate as a permanent custom Gradium voice. Returns the new voice's uid, which is the stable voice_id to use for synthesis. |
| Create WebSocket Token | `createWebSocketToken` | Generates a short-lived, single-use token that browser or mobile clients can pass as ?token= when opening a Gradium WebSocket (text-to-speech, speech-to-text or speech-to-speech) without exposing the API key. Issue one token per connection; it is consumed when verified. |
| Delete Pronunciation Dictionary | `deletePronunciationDictionary` | Permanently deletes a pronunciation dictionary and its rewrite rules by dictionary UID. |
| Delete Voice | `deleteVoice` | Permanently deletes a custom Gradium voice by its voice UID. Catalog voices cannot be deleted. |
| Delete Voice Candidate | `deleteVoiceCandidate` | Removes a generated voice design candidate that you are not keeping, by its embedding_id. |
| Generate Speech | `generateSpeech` | Converts a complete block of text to speech in one request (text-to-speech REST endpoint). With only_audio true the response is the raw audio file in the requested output format; otherwise the response is a newline-delimited JSON stream of ready, audio (base64 chunks), text (word timestamps) and error messages. Pronunciation dictionaries do not apply here; use json_config.rewrite_rules for text normalization. Consumes credits. |
| Generate Voice Candidates | `generateVoiceCandidates` | Samples one or more candidate voices from a written description (voice design). Each candidate gets an embedding_id (prefixed vox_emb_) that can be auditioned as a voice_id in text-to-speech and kept permanently with Create Voice From Candidate. Candidates expire 30 days after creation unless kept. |
| Get Credits | `getCredits` | Returns the current Gradium credit balance for the authenticated subscription, including remaining and allocated credits, the billing period and the plan name. |
| Get Pronunciation Dictionary | `getPronunciationDictionary` | Retrieves a pronunciation dictionary and its rewrite rules by dictionary UID. |

<details>

<summary>See 6 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Voice | `getVoice` | Retrieves the metadata of a single Gradium voice (catalog or custom) by its voice UID, including name, description, language and tags. |
| List Pronunciation Dictionaries | `listPronunciationDictionaries` | Lists the pronunciation dictionaries of the authenticated organization, optionally filtered by language, with limit and offset pagination. Returns the dictionaries with their rewrite rules and the total count. |
| List Voice Candidates | `listVoiceCandidates` | Lists the voice design candidates of the authenticated organization, newest first, or checks whether a single candidate is ready by passing its embedding_id. An id the organization does not hold returns an empty list. |
| List Voices | `listVoices` | Lists the voices available to the authenticated organization. By default only your custom voices are returned; set include_catalog to true to also include the Gradium voice library. Returns each voice's uid (the voice_id used for synthesis), name, language and tags. |
| Update Pronunciation Dictionary | `updatePronunciationDictionary` | Updates a pronunciation dictionary's name, description, language or rewrite rules by dictionary UID. Only the fields you pass are changed; when rules are passed they replace the existing rule set. |
| Update Voice | `updateVoice` | Updates the metadata of an existing custom Gradium voice, such as its name, description, language, sample start offset, tags or rank. Only the fields you pass are changed. Catalog voices cannot be updated. |

</details>
