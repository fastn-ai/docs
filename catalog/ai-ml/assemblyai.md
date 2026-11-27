---
description: "AssemblyAI is a speech-to-text service. Upload audio, create and list transcripts, and get paragraphs, sentences, subtitles and redacted audio."
hidden: true
---

# AssemblyAI

<img src="../../.gitbook/assets/connectors/lg/assemblyai.png" alt="AssemblyAI logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [assemblyai.com](https://assemblyai.com) |
| **Authentication** | API key |
| **Slug** | `assemblyai` |

## Setup

Your customers enter their API key for AssemblyAI when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect AssemblyAI from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AssemblyAI**.
2. Select **Connect** on the AssemblyAI card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AssemblyAI's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Transcript</td><td><code>createTranscript</code></td><td>Submit an audio_url for transcription. Returns a transcript queued for processing; poll getTranscript until status is completed. Optional Audio Intelligence flags enable speaker labels, sentiment analysis, entity detection, PII redaction, etc.</td></tr><tr><td>Delete Transcript</td><td><code>deleteTranscript</code></td><td>Permanently delete a transcript. Removes the text and all derived data; the record remains with redacted fields. Irreversible.</td></tr><tr><td>Get Paragraphs</td><td><code>getParagraphs</code></td><td>Get a completed transcript split into semantic paragraphs with per-paragraph timing, confidence, and words. Free read.</td></tr><tr><td>Get Redacted Audio</td><td><code>getRedactedAudio</code></td><td>Get the URL of the PII-redacted audio file for a transcript created with redact_pii_audio=true. Free read.</td></tr><tr><td>Get Sentences</td><td><code>getSentences</code></td><td>Get a completed transcript split into semantic sentences with per-sentence timing, confidence, and words. Free read.</td></tr><tr><td>Get SRT Subtitles</td><td><code>getSrtSubtitles</code></td><td>Export a completed transcript as SRT subtitles (text/plain). Optionally limit characters per caption. Free read.</td></tr><tr><td>Get Transcript</td><td><code>getTranscript</code></td><td>Retrieve a transcript by ID, including status and (once completed) text, words, utterances, and any Audio Intelligence results. Free read; poll this until status is completed or error.</td></tr><tr><td>Get VTT Subtitles</td><td><code>getVttSubtitles</code></td><td>Export a completed transcript as WebVTT subtitles (text/plain). Optionally limit characters per caption. Free read.</td></tr><tr><td>List Transcripts</td><td><code>listTranscripts</code></td><td>List your transcripts (paginated, newest first). Free read. Filter by status or date; use before_id/after_id to page.</td></tr><tr><td>Upload Audio File</td><td><code>uploadAudioFile</code></td><td>Upload a local audio/video file (raw binary) to AssemblyAI. Returns an upload_url usable as audio_url in createTranscript. Pass the file bytes as input.file.</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Word Search</td><td><code>wordSearch</code></td><td>Search a completed transcript for one or more keywords and get match counts plus timestamps. Free read.</td></tr></tbody></table>

</details>

