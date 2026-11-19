---
description: "Groq API connector — ultra-fast LLM inference over an OpenAI-compatible API (base https://api.groq.com/openai/v1)."
hidden: true
---

# Groq

<img src="../../.gitbook/assets/connectors/lg/groq.png" alt="Groq logo">

Covers chat completions, responses, model management, audio transcription/translation/speech (TTS), and the Batch + Files APIs. Auth is a Bearer API key (gsk_ prefix).

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [groq.com](https://groq.com) |
| **Authentication** | Bearer token |
| **Slug** | `groq` |

## Use it

Add Groq from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.groq.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Cancel Batch</td><td><code>cancelBatch</code></td><td>Cancel an in-progress batch job by ID.</td></tr><tr><td>Create Batch</td><td><code>createBatch</code></td><td>Create a batch job from an uploaded input file. endpoint is /v1/chat/completions. completion_window 24h to 7d.</td></tr><tr><td>Create Chat Completion</td><td><code>createChatCompletion</code></td><td>Generate a chat completion (OpenAI-compatible) on Groq. Returns the assistant message and token usage. Example model: openai/gpt-oss-20b.</td></tr><tr><td>Create Response</td><td><code>createResponse</code></td><td>Generate a model response via the Groq Responses API (beta). Returns structured output items and token usage. Example model: openai/gpt-oss-20b.</td></tr><tr><td>Create Speech</td><td><code>createSpeech</code></td><td>Generate speech audio (TTS) from text with a Groq Orpheus model. Returns the audio file (wav) as base64 data.</td></tr><tr><td>Create Transcription</td><td><code>createTranscription</code></td><td>Transcribe audio to text in the input language. Provide either a file (multipart) or a url. Models: whisper-large-v3-turbo (cheapest/fastest) or whisper-large-v3.</td></tr><tr><td>Create Translation</td><td><code>createTranslation</code></td><td>Translate audio into English text. Provide either a file (multipart) or a url. Models: whisper-large-v3-turbo (cheapest) or whisper-large-v3.</td></tr><tr><td>Delete File</td><td><code>deleteFile</code></td><td>Delete an uploaded file by ID.</td></tr><tr><td>Delete Model</td><td><code>deleteModel</code></td><td>Delete a fine-tuned/custom model by ID. Only applies to deletable models owned by your org.</td></tr><tr><td>Download File Content</td><td><code>downloadFileContent</code></td><td>Download the raw content of an uploaded or output file (e.g. batch results JSONL) by ID.</td></tr></tbody></table>

<details>

<summary>View 7 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Batches</td><td><code>listBatches</code></td><td>List all batch jobs for your organization.</td></tr><tr><td>List Files</td><td><code>listFiles</code></td><td>List all uploaded files for your organization.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>List all models available to your account, including context window and max completion tokens.</td></tr><tr><td>Retrieve Batch</td><td><code>retrieveBatch</code></td><td>Retrieve a single batch job by ID, including status and output/error file IDs.</td></tr><tr><td>Retrieve File</td><td><code>retrieveFile</code></td><td>Retrieve metadata for a single uploaded file by ID.</td></tr><tr><td>Retrieve Model</td><td><code>retrieveModel</code></td><td>Retrieve metadata for a single model by ID.</td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td>Upload a JSONL file (max 100 MB) for batch processing. purpose must be 'batch'.</td></tr></tbody></table>

</details>
