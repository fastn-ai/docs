---
description: "Groq runs AI models with fast inference. Create chat completions, speech, transcriptions and translations, and manage batches, files and models."
hidden: true
---

# Groq

<img src="../../.gitbook/assets/connectors/lg/groq.png" alt="Groq logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [groq.com](https://groq.com) |
| **Authentication** | Access token |
| **Slug** | `groq` |

## Setup

Your customers enter their access token for Groq when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Groq from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Groq**.
2. Select **Connect** on the Groq card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Groq's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Cancel Batch</td><td><code>cancelBatch</code></td><td>Cancel an in-progress batch job by ID.</td></tr><tr><td>Create Batch</td><td><code>createBatch</code></td><td>Create a batch job from an uploaded input file. endpoint is /v1/chat/completions. completion_window 24h to 7d.</td></tr><tr><td>Create Chat Completion</td><td><code>createChatCompletion</code></td><td>Generate a chat completion (OpenAI-compatible) on Groq. Returns the assistant message and token usage. Example model: openai/gpt-oss-20b.</td></tr><tr><td>Create Response</td><td><code>createResponse</code></td><td>Generate a model response via the Groq Responses API (beta). Returns structured output items and token usage. Example model: openai/gpt-oss-20b.</td></tr><tr><td>Create Speech</td><td><code>createSpeech</code></td><td>Generate speech audio (TTS) from text with a Groq Orpheus model. Returns the audio file (wav) as base64 data.</td></tr><tr><td>Create Transcription</td><td><code>createTranscription</code></td><td>Transcribe audio to text in the input language. Provide either a file (multipart) or a url. Models: whisper-large-v3-turbo (cheapest/fastest) or whisper-large-v3.</td></tr><tr><td>Create Translation</td><td><code>createTranslation</code></td><td>Translate audio into English text. Provide either a file (multipart) or a url. Models: whisper-large-v3-turbo (cheapest) or whisper-large-v3.</td></tr><tr><td>Delete File</td><td><code>deleteFile</code></td><td>Delete an uploaded file by ID.</td></tr><tr><td>Delete Model</td><td><code>deleteModel</code></td><td>Delete a fine-tuned/custom model by ID. Only applies to deletable models owned by your org.</td></tr><tr><td>Download File Content</td><td><code>downloadFileContent</code></td><td>Download the raw content of an uploaded or output file (e.g. batch results JSONL) by ID.</td></tr></tbody></table>

<details>

<summary>View 7 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Batches</td><td><code>listBatches</code></td><td>List all batch jobs for your organization.</td></tr><tr><td>List Files</td><td><code>listFiles</code></td><td>List all uploaded files for your organization.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>List all models available to your account, including context window and max completion tokens.</td></tr><tr><td>Retrieve Batch</td><td><code>retrieveBatch</code></td><td>Retrieve a single batch job by ID, including status and output/error file IDs.</td></tr><tr><td>Retrieve File</td><td><code>retrieveFile</code></td><td>Retrieve metadata for a single uploaded file by ID.</td></tr><tr><td>Retrieve Model</td><td><code>retrieveModel</code></td><td>Retrieve metadata for a single model by ID.</td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td>Upload a JSONL file (max 100 MB) for batch processing. purpose must be 'batch'.</td></tr></tbody></table>

</details>

