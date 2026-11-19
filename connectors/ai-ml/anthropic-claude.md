---
description: "Anthropic Claude API connector."
hidden: true
---

# Anthropic (Claude)

<img src="../../.gitbook/assets/connectors/lg/anthropic-claude.png" alt="Anthropic (Claude) logo">

Messages (create, count tokens), Models (list, get), Message Batches (create, list, get, results, cancel, delete), and Files API (upload, list, get, delete, download). Base URL https://api.anthropic.com/v1. API-key auth via x-api-key + anthropic-version header.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [anthropic.com](https://anthropic.com) |
| **Authentication** | API key |
| **Slug** | `anthropicClaude` |

## Use it

Add Anthropic (Claude) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.anthropicClaude.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Cancel Message Batch</td><td><code>cancelMessageBatch</code></td><td>Cancel a Message Batch that is in progress. Requests already in progress may still complete. POST /v1/messages/batches/{message_batch_id}/cancel.</td></tr><tr><td>Count Tokens</td><td><code>countTokens</code></td><td>Count the number of input tokens a Messages API request would use, without creating the message. POST /v1/messages/count_tokens.</td></tr><tr><td>Create Message</td><td><code>createMessage</code></td><td>Send a structured list of input messages and Claude generates the next message. The primary chat/completion endpoint. POST /v1/messages.</td></tr><tr><td>Create Message Batch</td><td><code>createMessageBatch</code></td><td>Send a batch of Message creation requests for asynchronous processing at 50% cost. POST /v1/messages/batches.</td></tr><tr><td>Delete File</td><td><code>deleteFile</code></td><td>Delete a file by id. Beta endpoint. DELETE /v1/files/{file_id}.</td></tr><tr><td>Delete Message Batch</td><td><code>deleteMessageBatch</code></td><td>Delete a Message Batch. Can only delete batches that have finished processing. DELETE /v1/messages/batches/{message_batch_id}.</td></tr><tr><td>Download File</td><td><code>downloadFile</code></td><td>Download the contents of a file (only files created by tools like code execution are downloadable). Beta endpoint. GET /v1/files/{file_id}/content.</td></tr><tr><td>Get File Metadata</td><td><code>getFileMetadata</code></td><td>Get metadata for a file by id. Beta endpoint. GET /v1/files/{file_id}.</td></tr><tr><td>Get Message Batch</td><td><code>getMessageBatch</code></td><td>Retrieve the status and metadata of a Message Batch. GET /v1/messages/batches/{message_batch_id}.</td></tr><tr><td>Get Message Batch Results</td><td><code>getMessageBatchResults</code></td><td>Stream the results of a Message Batch as a .jsonl file (one result per line), available once processing has ended. GET /v1/messages/batches/{message_batch_id}/results.</td></tr></tbody></table>

<details>

<summary>View 5 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Model</td><td><code>getModel</code></td><td>Get details of a specific model by id. GET /v1/models/{model_id}.</td></tr><tr><td>List Files</td><td><code>listFiles</code></td><td>List files within a Workspace, most recently uploaded first. Beta endpoint. GET /v1/files.</td></tr><tr><td>List Message Batches</td><td><code>listMessageBatches</code></td><td>List all Message Batches within a Workspace, most recently created first. GET /v1/messages/batches.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>List available models, most recently released first. GET /v1/models.</td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td>Upload a file for use in Messages API requests (referenced later by file_id). Beta endpoint. POST /v1/files (multipart/form-data).</td></tr></tbody></table>

</details>
