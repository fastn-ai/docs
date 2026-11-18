---
description: "Google Gemini Developer API (generativelanguage.googleapis.com/v1beta)."
---

# Google Gemini

Google Gemini Developer API (generativelanguage.googleapis.com/v1beta). Generate content (text/multimodal), streaming generation, token counting, embeddings, model discovery, the Files API, context caching (cachedContents), and Batch Mode generation. Auth via Gemini API key sent in the x-goog-api-key header.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [ai.google.dev](https://ai.google.dev) |
| **Authentication** | API key, OAuth 2.0 |
| **Actions** | 29 |
| **Events** | 0 |
| **Slug** | `googleGemini` |

## Use it

Add Google Gemini from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleGemini.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Embed Contents | `batchEmbedContents` | Generate embeddings for multiple inputs in one call. Each request mirrors embedContent (content, taskType, title, outputDimensionality) and must include model: models/{id}. |
| Batch Generate Content | `batchGenerateContent` | Submit an asynchronous Batch Mode job that runs many generateContent requests at ~50% cost with a ~24h SLA. Provide inlined requests or a file (files/{id}) as input. Returns a long-running operation; poll with getBatch. |
| Cancel Batch | `cancelBatch` | Cancel a running Batch Mode job by id (batches/{id}:cancel). |
| Count Tokens | `countTokens` | Count the tokens for a given input under a model. Accepts either contents[] or a full generateContentRequest (mutually exclusive). Returns totalTokens and modality breakdowns. |
| Create Cached Content | `createCachedContent` | Create a context cache (cachedContents) holding contents/tools/systemInstruction for a specific model, reusable across generateContent calls to reduce input token cost. Set expiry via ttl ('3600s') or expireTime. |
| Create Corpus | `createCorpus` | Creates an empty semantic retrieval corpus (Gemini API v1beta corpora.create) owned by the signed-in user; a project can hold up to 10 corpora. If no ID is given, Google derives one from displayName plus a random suffix. Requires a Google OAuth 2.0 connection; Google scope: generative-language.retriever. Remove it with Delete Corpus. Returns the created Corpus with its name. |
| Delete Batch | `deleteBatch` | Delete a Batch Mode job by id (batches/{id}). |
| Delete Cached Content | `deleteCachedContent` | Delete a context cache by id (cachedContents/{id}). Returns an empty body on success. |
| Delete Corpus | `deleteCorpus` | Deletes a semantic retrieval corpus (Gemini API v1beta corpora.delete). Without force=true Google refuses (FAILED_PRECONDITION) if the corpus still contains documents. Requires a Google OAuth 2.0 connection; Google scope: generative-language.retriever. Returns an empty body on success. |
| Delete File | `deleteFile` | Delete an uploaded file by name (files/{id}). Returns an empty body on success. |
| Delete Tuned Model | `deleteTunedModel` | Permanently deletes one of the signed-in user's Gemini tuned models (Gemini API v1beta tunedModels.delete). Irreversible. Requires a Google OAuth 2.0 connection; Google scope: generative-language.tuning. Returns an empty body on success. |
| Embed Content | `embedContent` | Generate a text embedding vector from input content using an embedding model (e.g. gemini-embedding-001, text-embedding-004). Supports taskType, title, and outputDimensionality. |
| Generate Content | `generateContent` | Generate a model response from a list of Content inputs (text and multimodal). Supports system instructions, tools/function-calling, safety settings, and generationConfig (temperature, topK, topP, maxOutputTokens, responseMimeType, responseSchema, thinkingConfig). Returns candidates with content parts, finishReason, safetyRatings, plus usageMetadata. |
| Generate Content (OAuth) | `generateContentOAuth` | Generates a text answer from a Gemini model for a single prompt (Gemini API v1beta models.generateContent) using the signed-in user's Google OAuth token instead of an API key, so usage counts against that user's per-user quota. Requires a Google OAuth 2.0 connection; Google scope: generative-language.peruserquota. Use the API-key Generate Content action for the full request body. Returns candidates[] with content.parts[].text, finishReason and usageMetadata. |
| Get Batch | `getBatch` | Get the status/result of a Batch Mode job by id (batches/{id}). When done is true, response contains the inlined or file output. |
| Get Cached Content | `getCachedContent` | Get a single context cache by id (cachedContents/{id}). |
| Get Corpus | `getCorpus` | Gets one semantic retrieval corpus by ID (Gemini API v1beta corpora.get). Read-only. Requires a Google OAuth 2.0 connection; Google scope: generative-language.retriever.readonly (or generative-language.retriever). Returns the Corpus (name, displayName, createTime, updateTime). |
| Get File | `getFile` | Get metadata for a single uploaded file by name (files/{id}), including its processing state and uri. |
| Get Model | `getModel` | Get metadata for a specific model (token limits, supported generation methods, default sampling params). |
| Get Tuned Model | `getTunedModel` | Gets one Gemini tuned model by ID (Gemini API v1beta tunedModels.get), including its base model, state, tuning task and hyperparameters. Read-only. Requires a Google OAuth 2.0 connection; Google scope: generative-language.tuning.readonly (or generative-language.tuning). Returns the TunedModel. |
| List Batches | `listBatches` | List Batch Mode jobs for the API key's project. Paginated. |
| List Cached Contents | `listCachedContents` | List the context caches (cachedContents) for the API key's project. Paginated. |
| List Corpora | `listCorpora` | Lists the semantic retrieval corpora (document collections) owned by the signed-in user (Gemini API v1beta corpora.list). Read-only. Requires a Google OAuth 2.0 connection; Google scope: generative-language.retriever.readonly (or generative-language.retriever). Returns corpora[] (name, displayName, createTime, updateTime) and nextPageToken. |
| List Files | `listFiles` | List the files uploaded via the Gemini Files API for the API key's project. Paginated. |
| List Models | `listModels` | List the models available through the Gemini Developer API, with their token limits and supported generation methods. Paginated. |
| List Tuned Models | `listTunedModels` | Lists the Gemini tuned (fine-tuned) models the signed-in user owns or can access (Gemini API v1beta tunedModels.list). Read-only. Requires a connection made with the Google OAuth 2.0 auth method; Google scope: generative-language.tuning.readonly (or generative-language.tuning). Returns tunedModels[] (name, displayName, baseModel, state, createTime) and nextPageToken; an empty object when the user has none. |
| Stream Generate Content | `streamGenerateContent` | Streaming variant of generateContent. Returns incremental GenerateContentResponse chunks server-sent. Same request body as generateContent. Use alt=sse query param for server-sent events framing. |
| Update Cached Content | `updateCachedContent` | Update a context cache's expiry (only ttl or expireTime are mutable). Pass updateMask to indicate which field changes. |
| Upload File (metadata) | `uploadFile` | Upload a text file to the Gemini Files API in one multipart request (metadata + content). Binary files are not supported by the engine. |
