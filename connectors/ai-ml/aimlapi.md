---
description: "AI/ML API (aimlapi.com) gives access to hundreds of AI models from one OpenAI-compatible endpoint."
hidden: true
---

# AI/ML API

AI/ML API (aimlapi.com) gives access to hundreds of AI models from one OpenAI-compatible endpoint. This connector covers the full AI/ML API surface: the model catalogue and deprecations, model performance metrics, account balance, billing details and transactions, API key management and usage, request logs, chat completions, the Responses API, Anthropic-style messages and message batches, image generation and editing, video generation, music and audio generation, text to speech, speech to text, OCR and embeddings.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [aimlapi.com](https://aimlapi.com) |
| **Authentication** | Bearer token |
| **Actions** | 33 |
| **Events** | 0 |
| **Slug** | `aimlapi` |

## Use it

Add AI/ML API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.aimlapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Message Batch | `cancelMessageBatch` | Cancels an in-progress Anthropic message batch by id. Requests already completed keep their results. |
| Create API Key | `createApiKey` | Creates a new API key on the account with an optional name, spending limit and model access scopes. The full key value is returned only in this response. The calling key must have the key-management endpoint permission enabled at https://aimlapi.com/app/keys. |
| Create Chat Completion | `createChatCompletion` | Generates a chat completion from any chat model in the catalogue using the OpenAI-compatible chat completions API. Supports system, user, assistant and tool messages, sampling controls, stop sequences, JSON response formats and tool calling. Billed against the account balance. Streaming is not used through this action. |
| Create Embeddings | `createEmbeddings` | Creates vector embeddings for input text with any embedding model in the catalogue using the OpenAI-compatible embeddings API. Billed against the account balance. |
| Create Message | `createMessage` | Generates a reply from an Anthropic Claude model using the Anthropic-style Messages API with a system prompt, message history, tools, stop sequences and optional extended thinking. Billed against the account balance. |
| Create Message Batch | `createMessageBatch` | Submits a batch of Anthropic Messages requests for asynchronous processing. Each request carries a custom_id and the message parameters. Poll the batch with Get Message Batch. Billed against the account balance. |
| Create Response | `createResponse` | Generates a model response using the OpenAI-compatible Responses API, which accepts text, image or file input, instructions, tools, reasoning configuration and multi-turn continuation through previous_response_id. Billed against the account balance. |
| Create Speech | `createSpeech` | Converts text to speech with any text-to-speech model in the catalogue and returns the audio URL. Voice, format and other model-specific settings are passed as documented per model at docs.aimlapi.com. Billed against the account balance. |
| Create Transcription | `createTranscription` | Starts an asynchronous speech-to-text transcription of an audio file given by URL with any speech-to-text model in the catalogue. Returns a generation id; poll Get Transcription for the result, which is kept for one hour. Billed against the account balance. |
| Delete API Key | `deleteApiKey` | Permanently deletes an API key identified by its 8-character prefix. The calling key must have the key-management endpoint permission enabled. |
| Edit Image | `editImage` | Edits one or more existing images according to a text prompt using an image-editing model, optionally with a mask marking the region to change. Images are passed as public URLs. Billed against the account balance. |
| Generate Audio | `generateAudio` | Starts an asynchronous music or audio generation from a text prompt, optionally with lyrics, a reference audio URL or a preprocessed cover feature id. Returns a generation id and status; poll Get Audio Generation until completed. Billed against the account balance. |
| Generate Image | `generateImage` | Generates one or more images from a text prompt with any image model in the catalogue (also used for 3D-generating models). Returns image URLs or base64 data. Model-specific parameters beyond the common ones are documented per model at docs.aimlapi.com. Billed against the account balance. |
| Generate Video | `generateVideo` | Starts an asynchronous video generation from a text prompt, optionally seeded with reference images, a source video or audio. Returns a generation id and status; poll Get Video Generation until the status is completed. Model-specific parameters are documented per model at docs.aimlapi.com. Billed against the account balance. |
| Get Account Balance (Legacy) | `getAccountBalanceLegacy` | Legacy balance endpoint. Returns the credit balance associated with the API key, the low-balance flag and threshold, the auto top-up status and the plan status. Prefer Get Balance for new integrations. |
| Get API Key Usage | `getApiKeyUsage` | Returns the total spend and charged request count of an API key over a time window given as a relative period or an explicit start and end. Defaults to the calling key. |
| Get API Key Usage Detail | `getApiKeyUsageDetail` | Returns an API key's spend and request count over a window broken down per model, optionally grouped by day, by model or by both, with a configurable time zone for day boundaries. |
| Get Audio Generation | `getAudioGeneration` | Returns the status of a music or audio generation and, once completed, the URL of the generated audio file. |
| Get Balance | `getBalance` | Returns the account's current balance in USD. |
| Get Billing Details | `getBillingDetails` | Returns detailed billing information for the account: user id, email, current balance and auto top-up settings. |
| Get Current API Key | `getCurrentApiKey` | Returns the details of the API key used for the request: its name, prefix, enabled state, model access scopes, spending limit and timestamps. |
| Get Message Batch | `getMessageBatch` | Returns the processing status, request counts and results URL of an Anthropic message batch by id. |
| Get Model Metrics | `getModelMetrics` | Returns recent performance percentiles (latency, time to first token, throughput) per model over a sliding window, computed from successful requests. Optionally restrict to specific model aliases. |
| Get Transcription | `getTranscription` | Returns the status of a speech-to-text task and, once finished, the transcription result. Results are stored for one hour after creation. |
| Get Video Generation | `getVideoGeneration` | Returns the status of a video generation and, once completed, the URL of the generated video. |
| List API Keys | `listApiKeys` | Lists all API keys on the account with their prefix, name, enabled state, scopes and spending limits. The calling key must have the key-management endpoint permission enabled. |
| List Billing Transactions | `listBillingTransactions` | Returns the account's balance ledger (payments, bonuses, refunds, adjustments, model usage charges and expired credits) with cursor pagination and optional date, direction and type filters. |
| List Model Deprecations | `listModelDeprecations` | Returns models that are deprecated, superseded or withdrawn, newest first, with their deprecation and shutdown dates and the recommended replacement. |
| List Models | `listModels` | Returns the AI/ML API model catalogue with each model's id, aliases, endpoint type, identity and tags. Filter by id, endpoint type, tags, modalities or capabilities and attach pricing, modality or capability sections with include. |
| List Usage Logs | `listUsageLogs` | Returns the individual requests made with an API key over a window, with model, outcome, origin, cost and token counts, filterable by model and status and paginated by limit and offset. |
| Preprocess Reference Audio | `preprocessReferenceAudio` | Analyses a reference audio track for a music-cover model and returns a cover feature id (valid 24 hours) plus the recognised, formatted lyrics, to be passed to Generate Audio. Billed against the account balance. |
| Run OCR | `runOcr` | Extracts text from a document or image with an OCR model, returning page-level Markdown, extracted images and optional structured annotations driven by JSON schemas. Billed against the account balance. |
| Update API Key | `updateApiKey` | Updates an API key identified by its 8-character prefix: rename it, enable or disable it, change its spending limit or its model access scopes. Only the fields sent are changed. The calling key must have the key-management endpoint permission enabled. |
