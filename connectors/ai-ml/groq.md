---
description: "Groq API connector — ultra-fast LLM inference over an OpenAI-compatible API (base https://api.groq.com/openai/v1)."
hidden: true
---

# Groq

<img src="../../.gitbook/assets/connectors/lg/groq.png" alt="Groq logo">

Groq API connector — ultra-fast LLM inference over an OpenAI-compatible API (base https://api.groq.com/openai/v1). Covers chat completions, responses, model management, audio transcription/translation/speech (TTS), and the Batch + Files APIs. Auth is a Bearer API key (gsk_ prefix).

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [groq.com](https://groq.com) |
| **Authentication** | Bearer token |
| **Slug** | `groq` |

## Use it

Add Groq from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.groq.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Batch | `cancelBatch` | Cancel an in-progress batch job by ID. |
| Create Batch | `createBatch` | Create a batch job from an uploaded input file. endpoint is /v1/chat/completions. completion_window 24h to 7d. |
| Create Chat Completion | `createChatCompletion` | Generate a chat completion (OpenAI-compatible) on Groq. Returns the assistant message and token usage. Example model: openai/gpt-oss-20b. |
| Create Response | `createResponse` | Generate a model response via the Groq Responses API (beta). Returns structured output items and token usage. Example model: openai/gpt-oss-20b. |
| Create Speech | `createSpeech` | Generate speech audio (TTS) from text with a Groq Orpheus model. Returns the audio file (wav) as base64 data. |
| Create Transcription | `createTranscription` | Transcribe audio to text in the input language. Provide either a file (multipart) or a url. Models: whisper-large-v3-turbo (cheapest/fastest) or whisper-large-v3. |
| Create Translation | `createTranslation` | Translate audio into English text. Provide either a file (multipart) or a url. Models: whisper-large-v3-turbo (cheapest) or whisper-large-v3. |
| Delete File | `deleteFile` | Delete an uploaded file by ID. |
| Delete Model | `deleteModel` | Delete a fine-tuned/custom model by ID. Only applies to deletable models owned by your org. |
| Download File Content | `downloadFileContent` | Download the raw content of an uploaded or output file (e.g. batch results JSONL) by ID. |
| List Batches | `listBatches` | List all batch jobs for your organization. |
| List Files | `listFiles` | List all uploaded files for your organization. |
| List Models | `listModels` | List all models available to your account, including context window and max completion tokens. |
| Retrieve Batch | `retrieveBatch` | Retrieve a single batch job by ID, including status and output/error file IDs. |
| Retrieve File | `retrieveFile` | Retrieve metadata for a single uploaded file by ID. |
| Retrieve Model | `retrieveModel` | Retrieve metadata for a single model by ID. |
| Upload File | `uploadFile` | Upload a JSONL file (max 100 MB) for batch processing. purpose must be 'batch'. |
