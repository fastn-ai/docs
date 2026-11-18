---
description: "Anthropic Claude API connector."
hidden: true
---

# Anthropic (Claude)

<img src="../../.gitbook/assets/connectors/lg/anthropic-claude.png" alt="Anthropic (Claude) logo">

Anthropic Claude API connector. Messages (create, count tokens), Models (list, get), Message Batches (create, list, get, results, cancel, delete), and Files API (upload, list, get, delete, download). Base URL https://api.anthropic.com/v1. API-key auth via x-api-key + anthropic-version header.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [anthropic.com](https://anthropic.com) |
| **Authentication** | API key |
| **Slug** | `anthropicClaude` |

## Use it

Add Anthropic (Claude) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.anthropicClaude.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Message Batch | `cancelMessageBatch` | Cancel a Message Batch that is in progress. Requests already in progress may still complete. POST /v1/messages/batches/{message_batch_id}/cancel. |
| Count Tokens | `countTokens` | Count the number of input tokens a Messages API request would use, without creating the message. POST /v1/messages/count_tokens. |
| Create Message | `createMessage` | Send a structured list of input messages and Claude generates the next message. The primary chat/completion endpoint. POST /v1/messages. |
| Create Message Batch | `createMessageBatch` | Send a batch of Message creation requests for asynchronous processing at 50% cost. POST /v1/messages/batches. |
| Delete File | `deleteFile` | Delete a file by id. Beta endpoint. DELETE /v1/files/{file_id}. |
| Delete Message Batch | `deleteMessageBatch` | Delete a Message Batch. Can only delete batches that have finished processing. DELETE /v1/messages/batches/{message_batch_id}. |
| Download File | `downloadFile` | Download the contents of a file (only files created by tools like code execution are downloadable). Beta endpoint. GET /v1/files/{file_id}/content. |
| Get File Metadata | `getFileMetadata` | Get metadata for a file by id. Beta endpoint. GET /v1/files/{file_id}. |
| Get Message Batch | `getMessageBatch` | Retrieve the status and metadata of a Message Batch. GET /v1/messages/batches/{message_batch_id}. |
| Get Message Batch Results | `getMessageBatchResults` | Stream the results of a Message Batch as a .jsonl file (one result per line), available once processing has ended. GET /v1/messages/batches/{message_batch_id}/results. |
| Get Model | `getModel` | Get details of a specific model by id. GET /v1/models/{model_id}. |
| List Files | `listFiles` | List files within a Workspace, most recently uploaded first. Beta endpoint. GET /v1/files. |
| List Message Batches | `listMessageBatches` | List all Message Batches within a Workspace, most recently created first. GET /v1/messages/batches. |
| List Models | `listModels` | List available models, most recently released first. GET /v1/models. |
| Upload File | `uploadFile` | Upload a file for use in Messages API requests (referenced later by file_id). Beta endpoint. POST /v1/files (multipart/form-data). |
