---
description: "Mistral AI platform API (api.mistral.ai/v1): chat completions, FIM code completion, embeddings, models management, files, fine-tuning jobs, batch jobs, OCR,…"
hidden: true
---

# Mistral AI

<img src="../../.gitbook/assets/connectors/lg/mistralai.png" alt="Mistral AI logo">

Mistral AI platform API (api.mistral.ai/v1): chat completions, FIM code completion, embeddings, models management, files, fine-tuning jobs, batch jobs, OCR, moderation/classification, and the Conversations + Agents APIs. Bearer API-key auth.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [mistral.ai](https://mistral.ai) |
| **Authentication** | Bearer token |
| **Slug** | `mistralai` |

## Use it

Add Mistral AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mistralai.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Append To Conversation | `appendToConversation` | Append entries to an existing conversation and get the model's response. POST /v1/conversations/{conversation_id}. |
| Archive Fine-Tuned Model | `archiveFineTunedModel` | Archive a fine-tuned model. POST /v1/fine_tuning/models/{model_id}/archive. |
| Cancel Batch Job | `cancelBatchJob` | Request cancellation of a batch job. POST /v1/batch/jobs/{job_id}/cancel. |
| Create Agent | `createAgent` | Create a reusable agent (beta Agents API). POST /v1/agents. Requires model + name. |
| Create Batch Job | `createBatchJob` | Create an asynchronous batch job. POST /v1/batch/jobs. input_files are JSONL file IDs uploaded with purpose=batch; endpoint targets the inference route (e.g. /v1/chat/completions). |
| Create Chat Classification | `createChatClassification` | Run a classifier model on conversation messages. POST /v1/chat/classifications. |
| Create Chat Completion | `createChatCompletion` | Generate a chat completion. POST /v1/chat/completions. Provide model + messages. For lowest cost use the cheapest chat model 'ministral-3b-latest'. Other models: mistral-small-latest, mistral-large-latest, ministral-8b-latest, codestral-latest, pixtral-large-latest, magistral-medium-latest. |
| Create Chat Moderation | `createChatModeration` | Classify conversation messages against safety policies. POST /v1/chat/moderations. Model: mistral-moderation-latest. input is a list of chat messages. |
| Create Classification | `createClassification` | Run a classifier model on raw text. POST /v1/classifications. Requires a classifier model (e.g. a fine-tuned classifier). |
| Create Embeddings | `createEmbeddings` | Create embedding vectors for input text. POST /v1/embeddings. Model: mistral-embed (text) or codestral-embed (code). |
| Create FIM Completion | `createFimCompletion` | Fill-in-the-middle code completion. POST /v1/fim/completions. Use a code model such as codestral-latest. Provide prompt (prefix) and optional suffix. |
| Create Moderation | `createModeration` | Classify raw text against safety policies. POST /v1/moderations. Model: mistral-moderation-latest. Returns per-category booleans and scores. |
| Delete File | `deleteFile` | Delete an uploaded file. DELETE /v1/files/{file_id}. |
| Delete Model | `deleteModel` | Delete a fine-tuned model. DELETE /v1/models/{model_id}. |
| Get Agent | `getAgent` | Retrieve an agent. GET /v1/agents/{agent_id}. Optional agent_version query. |
| Get Batch Job | `getBatchJob` | Retrieve a batch job. GET /v1/batch/jobs/{job_id}. |
| Get Conversation | `getConversation` | Retrieve a conversation's metadata. GET /v1/conversations/{conversation_id}. |
| Get Conversation History | `getConversationHistory` | Retrieve all entries of a conversation in chronological order. GET /v1/conversations/{conversation_id}/history. |
| Get Conversation Messages | `getConversationMessages` | Retrieve only the message entries of a conversation. GET /v1/conversations/{conversation_id}/messages. |
| Get File Signed URL | `getFileSignedUrl` | Get a temporary signed download URL for a file. GET /v1/files/{file_id}/url. expiry in hours (1-168, default 24). |
| List Agents | `listAgents` | List agents. GET /v1/agents. Returns a JSON array of agent objects (wrapped under 'data' in this contract). |
| List Batch Jobs | `listBatchJobs` | List batch jobs. GET /v1/batch/jobs. Filter by model, status, metadata, created_after, created_by_me. |
| List Conversations | `listConversations` | List conversations sorted by creation time. GET /v1/conversations. |
| List Files | `listFiles` | List uploaded files. GET /v1/files. Supports pagination and filtering by purpose/source/sample_type/search. |
| List Models | `listModels` | List all models available to your account (base + fine-tuned). GET /v1/models. |
| Process OCR | `processOcr` | Run OCR on a document or image. POST /v1/ocr. Model: mistral-ocr-latest. Provide document as {document_url} (DocumentURLChunk), {image_url} (ImageURLChunk), or {file_id} (FileChunk). |
| Restart Conversation | `restartConversation` | Restart a conversation from a given entry. POST /v1/conversations/{conversation_id}/restart. |
| Retrieve File | `retrieveFile` | Retrieve metadata for an uploaded file. GET /v1/files/{file_id}. |
| Retrieve Model | `retrieveModel` | Retrieve a single model's metadata and capabilities. GET /v1/models/{model_id}. |
| Start Conversation | `startConversation` | Start a conversation (beta Conversations API). POST /v1/conversations. Provide inputs plus either model or agent_id. |
| Unarchive Fine-Tuned Model | `unarchiveFineTunedModel` | Unarchive a fine-tuned model. DELETE /v1/fine_tuning/models/{model_id}/archive. |
| Update Agent | `updateAgent` | Update an agent (creates a new version). PATCH /v1/agents/{agent_id}. |
| Update Agent Version | `updateAgentVersion` | Switch an agent's active version. PATCH /v1/agents/{agent_id}/version. |
| Update Fine-Tuned Model | `updateFineTunedModel` | Update name/description of a fine-tuned model. PATCH /v1/fine_tuning/models/{model_id}. |
| Upload File | `uploadFile` | Upload a file (max 512MB) for fine-tune, batch, or ocr purposes. POST /v1/files (multipart/form-data). Pass the file via input.file and purpose. |
