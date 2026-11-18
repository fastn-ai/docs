---
description: "AssemblyAI speech-to-text and audio intelligence API (https://api.assemblyai.com/v2)."
---

# AssemblyAI

AssemblyAI speech-to-text and audio intelligence API (https://api.assemblyai.com/v2). Upload audio, create/get/list/delete transcripts, retrieve sentences, paragraphs, word-search, SRT/VTT subtitles, and redacted audio. Audio Intelligence: speaker labels, sentiment analysis, entity detection, content safety, PII redaction, auto highlights, topic detection. LeMUR LLM framework (task, summary, question-answer, action-items) over transcripts. Auth: raw API key in the Authorization header (no Bearer prefix).

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [assemblyai.com](https://assemblyai.com) |
| **Authentication** | API key |
| **Actions** | 11 |
| **Events** | 0 |
| **Slug** | `assemblyai` |

## Use it

Add AssemblyAI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.assemblyai.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Transcript | `createTranscript` | Submit an audio_url for transcription. Returns a transcript queued for processing; poll getTranscript until status is completed. Optional Audio Intelligence flags enable speaker labels, sentiment analysis, entity detection, PII redaction, etc. |
| Delete Transcript | `deleteTranscript` | Permanently delete a transcript. Removes the text and all derived data; the record remains with redacted fields. Irreversible. |
| Get Paragraphs | `getParagraphs` | Get a completed transcript split into semantic paragraphs with per-paragraph timing, confidence, and words. Free read. |
| Get Redacted Audio | `getRedactedAudio` | Get the URL of the PII-redacted audio file for a transcript created with redact_pii_audio=true. Free read. |
| Get Sentences | `getSentences` | Get a completed transcript split into semantic sentences with per-sentence timing, confidence, and words. Free read. |
| Get SRT Subtitles | `getSrtSubtitles` | Export a completed transcript as SRT subtitles (text/plain). Optionally limit characters per caption. Free read. |
| Get Transcript | `getTranscript` | Retrieve a transcript by ID, including status and (once completed) text, words, utterances, and any Audio Intelligence results. Free read; poll this until status is completed or error. |
| Get VTT Subtitles | `getVttSubtitles` | Export a completed transcript as WebVTT subtitles (text/plain). Optionally limit characters per caption. Free read. |
| List Transcripts | `listTranscripts` | List your transcripts (paginated, newest first). Free read. Filter by status or date; use before_id/after_id to page. |
| Upload Audio File | `uploadAudioFile` | Upload a local audio/video file (raw binary) to AssemblyAI. Returns an upload_url usable as audio_url in createTranscript. Pass the file bytes as input.file. |
| Word Search | `wordSearch` | Search a completed transcript for one or more keywords and get match counts plus timestamps. Free read. |
