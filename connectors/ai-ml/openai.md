---
description: "OpenAI API connector — chat completions, responses, embeddings, models, files, images, audio, moderations, fine-tuning, batches, vector stores, and the…"
hidden: true
---

# OpenAI

OpenAI API connector — chat completions, responses, embeddings, models, files, images, audio, moderations, fine-tuning, batches, vector stores, and the assistants/threads/messages/runs beta. Auth via Bearer API key.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [openai.com](https://openai.com) |
| **Authentication** | Bearer token |
| **Actions** | 44 |
| **Events** | 15 |
| **Slug** | `openai` |

## Use it

Add OpenAI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openai.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Batch | `cancelBatch` | Cancels an in-progress batch. POST /batches/{batch_id}/cancel. |
| Cancel Fine-tuning Job | `cancelFineTuningJob` | Immediately cancel a fine-tune job. POST /fine_tuning/jobs/{fine_tuning_job_id}/cancel. |
| Cancel Vector Store File Batch | `cancelVectorStoreFileBatch` | Cancel a vector store file batch (files in progress will be cancelled). POST /vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel. |
| Create Batch | `createBatch` | Creates and executes a batch from an uploaded file of requests. POST /batches. |
| Create Chat Completion | `createChatCompletion` | Create a model response for the given chat conversation. POST /chat/completions. |
| Create Embeddings | `createEmbeddings` | Creates an embedding vector representing the input text. POST /embeddings. |
| Create Fine-tuning Job | `createFineTuningJob` | Creates a fine-tuning job which begins the process of training a model from a dataset. POST /fine_tuning/jobs. |
| Create Image | `createImage` | Creates an image given a text prompt. POST /images/generations. |
| Create Image Edit | `createImageEdit` | Creates an edited or extended image given source image(s) and a prompt. POST /images/edits (multipart/form-data). |
| Create Moderation | `createModeration` | Classifies if text and/or image inputs are potentially harmful. POST /moderations. |
| Create Response | `createResponse` | Create a model response using the Responses API. POST /responses. |
| Create Speech | `createSpeech` | Generates audio from the input text (text-to-speech). POST /audio/speech. Returns binary audio. |
| Create Transcription | `createTranscription` | Transcribes audio into the input language. POST /audio/transcriptions (multipart/form-data). |
| Create Translation | `createTranslation` | Translates audio into English. POST /audio/translations (multipart/form-data). |
| Create Vector Store | `createVectorStore` | Create a vector store. POST /vector_stores. |
| Create Vector Store File | `createVectorStoreFile` | Attach a file to a vector store. POST /vector_stores/{vector_store_id}/files. |
| Create Vector Store File Batch | `createVectorStoreFileBatch` | Create a vector store file batch to attach multiple files at once. POST /vector_stores/{vector_store_id}/file_batches. |
| Delete File | `deleteFile` | Delete a file. DELETE /files/{file_id}. |
| Delete Model | `deleteModel` | Delete a fine-tuned model (requires Owner role). DELETE /models/{model}. |
| Delete Response | `deleteResponse` | Delete a model response with the given ID. DELETE /responses/{response_id}. |
| Delete Vector Store | `deleteVectorStore` | Delete a vector store. DELETE /vector_stores/{vector_store_id}. |
| Delete Vector Store File | `deleteVectorStoreFile` | Delete a vector store file (removes association; does not delete the file). DELETE /vector_stores/{vector_store_id}/files/{file_id}. |
| Get Batch | `getBatch` | Retrieves a batch. GET /batches/{batch_id}. |
| Get File | `getFile` | Returns information about a specific file. GET /files/{file_id}. |
| Get File Content | `getFileContent` | Returns the contents of the specified file. GET /files/{file_id}/content. |
| Get Fine-tuning Job | `getFineTuningJob` | Get info about a fine-tuning job. GET /fine_tuning/jobs/{fine_tuning_job_id}. |
| Get Model | `getModel` | Retrieves a model instance by ID. GET /models/{model}. |
| Get Response | `getResponse` | Retrieve a model response with the given ID. GET /responses/{response_id}. |
| Get Vector Store | `getVectorStore` | Retrieves a vector store. GET /vector_stores/{vector_store_id}. |
| Get Vector Store File | `getVectorStoreFile` | Retrieves a vector store file. GET /vector_stores/{vector_store_id}/files/{file_id}. |
| Get Vector Store File Batch | `getVectorStoreFileBatch` | Retrieves a vector store file batch. GET /vector_stores/{vector_store_id}/file_batches/{batch_id}. |
| List Batches | `listBatches` | List your organization's batches. GET /batches. |
| List Files | `listFiles` | Returns a list of files. GET /files. |
| List Fine-tuning Checkpoints | `listFineTuningCheckpoints` | List checkpoints for a fine-tuning job. GET /fine_tuning/jobs/{fine_tuning_job_id}/checkpoints. |
| List Fine-tuning Events | `listFineTuningEvents` | Get status updates for a fine-tuning job. GET /fine_tuning/jobs/{fine_tuning_job_id}/events. |
| List Fine-tuning Jobs | `listFineTuningJobs` | List your organization's fine-tuning jobs. GET /fine_tuning/jobs. |
| List Models | `listModels` | Lists the currently available models. GET /models. |
| List Response Input Items | `listResponseInputItems` | Returns a list of input items for a given response. GET /responses/{response_id}/input_items. |
| List Vector Store File Batch Files | `listVectorStoreFileBatchFiles` | Returns a list of files in a vector store file batch. GET /vector_stores/{vector_store_id}/file_batches/{batch_id}/files. |
| List Vector Store Files | `listVectorStoreFiles` | Returns a list of vector store files. GET /vector_stores/{vector_store_id}/files. |
| List Vector Stores | `listVectorStores` | Returns a list of vector stores. GET /vector_stores. |
| Search Vector Store | `searchVectorStore` | Search a vector store for relevant chunks based on a query. POST /vector_stores/{vector_store_id}/search. |
| Update Vector Store | `updateVectorStore` | Modifies a vector store. POST /vector_stores/{vector_store_id}. |
| Upload File | `uploadFile` | Upload a file that can be used across endpoints (assistants, fine-tuning, batch, vision). POST /files (multipart/form-data). |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Batch Cancelled | `batch.cancelled` | A batch job was cancelled. |
| Batch Completed | `batch.completed` | A batch job completed. |
| Batch Expired | `batch.expired` | A batch job expired before completing. |
| Batch Failed | `batch.failed` | A batch job failed. |
| Eval Run Canceled | `eval.run.canceled` | An evaluation run was canceled. |
| Eval Run Failed | `eval.run.failed` | An evaluation run failed. |
| Eval Run Succeeded | `eval.run.succeeded` | An evaluation run completed successfully. |
| Fine-tuning Job Cancelled | `fine_tuning.job.cancelled` | A fine-tuning job was cancelled. |
| Fine-tuning Job Failed | `fine_tuning.job.failed` | A fine-tuning job failed. |
| Fine-tuning Job Succeeded | `fine_tuning.job.succeeded` | A fine-tuning job completed successfully. |
| Realtime Call Incoming | `realtime.call.incoming` | An incoming Realtime SIP call was received. |
| Response Cancelled | `response.cancelled` | A background Response request was cancelled. |
| Response Completed | `response.completed` | A background Response request completed successfully. |
| Response Failed | `response.failed` | A background Response request failed. |
| Response Incomplete | `response.incomplete` | A background Response request finished incomplete. |
