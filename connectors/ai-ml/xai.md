---
description: "xAI Grok API — OpenAI-compatible and Anthropic-compatible inference (chat completions, messages, responses, deferred completions, legacy completions), image…"
hidden: true
---

# xAI (Grok)

xAI Grok API — OpenAI-compatible and Anthropic-compatible inference (chat completions, messages, responses, deferred completions, legacy completions), image generation, model discovery (models + language-models), text tokenization, and API key info. Base https://api.x.ai/v1. Auth: Authorization: Bearer xai- key.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [x.ai](https://x.ai) |
| **Authentication** | Bearer token |
| **Actions** | 62 |
| **Events** | 0 |
| **Slug** | `xai` |

## Use it

Add xAI (Grok) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.xai.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Document To Collection | `addDocumentToCollection` | Add a file that is already stored in the xAI Files API to a document collection so it is indexed and searchable. The API requires the collection and file identifiers in the request body as well as the path, and requires a Metadata Fields object even when it is empty. |
| Add Requests To Batch | `addRequestsToBatch` | Add one or more chat completion requests to an existing batch job for asynchronous processing. Each entry wraps a standard chat completion request body. |
| Batch Get Collection Documents | `batchGetCollectionDocuments` | Retrieve the metadata of several documents in a collection in a single request. Known xAI defect: the endpoint declares File IDs as a query parameter but its deserializer rejects every query encoding of a list, so this route currently returns 400 for any input. Use Get Collection Document per file until xAI fixes it. |
| Cancel Batch | `cancelBatch` | Cancel processing of every request still pending in a batch job. |
| Compact Response | `compactResponse` | Compact a long conversation into a shorter equivalent through the Responses API, reducing the token footprint of subsequent turns. Supply the conversation as Input, optionally anchored to a stored response. |
| Create Batch | `createBatch` | Create a new batch job that requests can subsequently be added to for asynchronous processing at a reduced rate. |
| Create Chat Completion | `createChatCompletion` | Create a chat completion from a conversation of messages, using the OpenAI-compatible endpoint. Supports tool calling, structured outputs, reasoning effort and deferred execution. The legacy search_parameters field is not exposed: xAI retired it with 410 Gone in favour of the Agent Tools API. |
| Create Collection | `createCollection` | Create a document collection that groups uploaded files so Grok can search across them. Field Definitions declares the metadata schema documents in this collection carry, and is required even when empty. |
| Create Completion (Legacy) | `createCompletion` | Create a legacy text completion from a single prompt string using the OpenAI-compatible Completions endpoint. Prefer Create Chat Completion for new work. The OpenAI echo and suffix parameters are not exposed because xAI rejects them with "Argument not supported". |
| Create Embeddings | `createEmbeddings` | Create embedding vectors for one or more input strings using an xAI embedding model, for semantic search and retrieval. |
| Create Message (Anthropic-compatible) | `createMessage` | Create a model response for a conversation using the Anthropic-compatible Messages endpoint. Maximum Tokens is required. Supports system prompts, tool use and stop sequences. The Anthropic top_k parameter is not exposed because xAI rejects it with "Argument not supported". |
| Create Realtime Client Secret | `createRealtimeClientSecret` | Mint a short-lived client secret that a browser or mobile client can use to open a Realtime voice session directly, without exposing the account API key. |
| Create Response | `createResponse` | Create a model response through the Responses API. Supports conversation persistence via Store, system-level Instructions, tool calling and structured outputs. |
| Create Text Completion (Anthropic-compatible) | `createTextCompletionAnthropic` | Create a legacy text completion from a single prompt string using the Anthropic-compatible endpoint. Not supported by reasoning models; prefer Create Chat Completion for new work. |
| Delete Collection | `deleteCollection` | Delete a document collection by its identifier. The files themselves remain in the Files API; only the collection and its index are removed. |
| Delete Custom Voice | `deleteCustomVoice` | Delete a custom text-to-speech voice owned by the team. Speech requests referencing the deleted voice identifier will stop working. |
| Delete File | `deleteFile` | Delete a file from the xAI Files API by its identifier. After deletion the file no longer appears in List Files, its content download returns 404, and the identifier can no longer be referenced in chat attachments. |
| Delete Response | `deleteResponse` | Delete a stored response by its identifier, removing it from the Responses API. |
| Download File Content | `downloadFileContent` | Download the raw content of a file stored in the xAI Files API. Binary content is returned as a file reference; text content is returned inline. |
| Edit Image | `editImage` | Edit an existing image from a text prompt using an xAI image generation model. Supply either a single source image or a list of reference images, by public URL, base64 data URL, or an xAI Files API file id. |
| Edit Video | `editVideo` | Edit an existing video from a text prompt. This is an asynchronous operation: it returns a request id which Get Video Result polls until the edited video is ready. |
| Extend Video | `extendVideo` | Extend an existing video by generating continuation content from a prompt. This is an asynchronous operation: it returns a request id which Get Video Result polls until the extended video is ready. |
| Generate Image | `generateImage` | Generate one or more images from a text prompt using an xAI image generation model, returned as temporary URLs or inline base64. |
| Generate Speech | `generateSpeech` | Convert text into speech audio using an xAI voice. Supports inline speech tags such as [pause] and [laugh] and wrapping style tags such as &lt;whisper&gt; and &lt;emphasis&gt;. |
| Generate Video | `generateVideo` | Generate a video from a text prompt and optionally a reference image. This is an asynchronous operation: it returns a request id which Get Video Result polls until the video is ready. |
| Get API Key Info | `getApiKeyInfo` | Retrieve information about the authenticating API key: redacted key, name, status, permissions (acls), and the users/team that created or modified it (/api-key). |
| Get Batch | `getBatch` | Retrieve a single batch job by its identifier, including how many of its requests are pending, successful, failed or cancelled. |
| Get Collection | `getCollection` | Retrieve a single document collection by its identifier, including its name, owning team and timestamps. |
| Get Collection Document | `getCollectionDocument` | Retrieve a single document within a collection by its file identifier, including its indexing status and metadata. |
| Get Custom Voice | `getCustomVoice` | Retrieve a single custom text-to-speech voice owned by the team, by its voice identifier. |
| Get Custom Voice Audio | `getCustomVoiceAudio` | Download the reference audio clip that a custom text-to-speech voice was created from. |
| Get Deferred Chat Completion | `getDeferredChatCompletion` | Retrieve the result of a deferred (asynchronously started) chat completion by its request id. Returns 200 with the completion when ready, or 202 while still pending. |
| Get Embedding Model | `getEmbeddingModel` | Retrieve the full details of a single embedding model by its identifier. |
| Get File | `getFile` | Retrieve the metadata of a single file stored in the xAI Files API, including its filename, size, purpose and expiry. |
| Get Image Generation Model | `getImageGenerationModel` | Retrieve the full details of a single image generation model by its identifier, including modalities, pricing and aliases. |
| Get Language Model | `getLanguageModel` | Get full details (modalities, pricing, fingerprint, aliases) for a single language model by id (/language-models/{model_id}). |
| Get Model | `getModel` | Get metadata for a single model by id (OpenAI-compatible /models/{model_id}). |
| Get Response | `getResponse` | Retrieve a previously generated and stored response by its id (Responses API). |
| Get Text To Speech Voice | `getTextToSpeechVoice` | Retrieve a single built-in text-to-speech voice by its identifier. |
| Get Video Generation Model | `getVideoGenerationModel` | Retrieve the full details of a single video generation model by its identifier, including modalities, pricing and aliases. |
| Get Video Result | `getVideoResult` | Retrieve the result of a deferred video generation request by its request id. Returns the finished video while the job is complete, or the current status while it is still running. |
| List Batch Requests | `listBatchRequests` | List the metadata of every request that has been added to a batch job. |
| List Batch Results | `listBatchResults` | List the processing results for a batch job, one entry per completed request. |
| List Batches | `listBatches` | List the batch jobs belonging to the current team, with their state counts and timestamps. |
| List Collection Documents | `listCollectionDocuments` | List the documents that have been added to a document collection, with their indexing status and metadata. |
| List Collections | `listCollections` | List the document collections belonging to the authenticating team. Collections group uploaded files so they can be searched together by Grok. |
| List Custom Voices | `listCustomVoices` | List the custom text-to-speech voices owned by the authenticating team. |
| List Embedding Models | `listEmbeddingModels` | List the embedding models available to the authenticating API key, with their modalities and pricing. |
| List Files | `listFiles` | List the files stored in the xAI Files API for the authenticating team, with their size, filename and expiry. |
| List Image Generation Models | `listImageGenerationModels` | List all image-generation models available to the API key with details and pricing (/image-generation-models). |
| List Language Models | `listLanguageModels` | List all chat and image-understanding language models available to the API key with full details: modalities, pricing, fingerprint and aliases (/language-models). |
| List Models | `listModels` | List all models available to the authenticating API key (OpenAI-compatible /models). |
| List Response Input Items | `listResponseInputItems` | List the input items that were supplied to a stored response, in the order the model received them. |
| List Text To Speech Voices | `listTextToSpeechVoices` | List the built-in text-to-speech voices available to the API key, with their identifier, display name and language. |
| List Video Generation Models | `listVideoGenerationModels` | List every video generation model available to the authenticating API key, with its modalities, pricing and aliases. |
| Remove Document From Collection | `removeDocumentFromCollection` | Remove a document from a collection so it is no longer indexed or searchable there. The underlying file remains in the xAI Files API. |
| Search Documents | `searchDocuments` | Search the indexed documents of one or more collections for chunks relevant to a query. Results can be filtered on document metadata with AIP-160 filter syntax and grouped by metadata keys. |
| Tokenize Text | `tokenizeText` | Tokenize text for a given model and return token ids with their string representations and token bytes (/tokenize-text). |
| Transcribe Audio | `transcribeAudio` | Transcribe an audio file to text by supplying a publicly reachable URL that xAI downloads server-side. Supports speaker diarization, per-channel transcription and text formatting. Uploading raw audio bytes directly requires a multipart request, which this connector cannot send; use the URL form instead. |
| Update Collection | `updateCollection` | Rename a document collection and add, change or remove entries in its metadata field schema. The API requires the collection identifier in the request body as well as the path, and requires a Field Definition Updates list even when it is empty. |
| Update Collection Document | `updateCollectionDocument` | Update the user-defined metadata fields stored against a document inside a collection. These fields drive the metadata filters available in Search Documents. The API requires the collection and file identifiers in the request body as well as the path. |
| Update Custom Voice | `updateCustomVoice` | Update the descriptive labels of a custom text-to-speech voice, such as its display name, description, gender, accent, age and language. |
