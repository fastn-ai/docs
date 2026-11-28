---
description: "Anthropic builds the Claude family of AI models. Send messages to Claude, count tokens, run message batches and manage uploaded files."
hidden: true
---

# Anthropic (Claude)

<img src="../../.gitbook/assets/connectors/lg/anthropic-claude.png" alt="Anthropic (Claude) logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [anthropic.com](https://anthropic.com) |
| **Authentication** | API key |
| **Slug** | `anthropicClaude` |

## Setup

Your customers enter their API key for Anthropic (Claude) when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Anthropic (Claude) from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Anthropic (Claude)**.
2. Select **Connect** on the Anthropic (Claude) card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Anthropic (Claude)'s actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Cancel Message Batch</td><td><code>cancelMessageBatch</code></td><td>Cancel a Message Batch that is in progress. Requests already in progress may still complete.</td></tr><tr><td>Count Tokens</td><td><code>countTokens</code></td><td>Count the number of input tokens a Messages API request would use, without creating the message.</td></tr><tr><td>Create Message</td><td><code>createMessage</code></td><td>Send a structured list of input messages and Claude generates the next message. The primary chat/completion endpoint.</td></tr><tr><td>Create Message Batch</td><td><code>createMessageBatch</code></td><td>Send a batch of Message creation requests for asynchronous processing at 50% cost.</td></tr><tr><td>Delete File</td><td><code>deleteFile</code></td><td>Delete a file by id. Beta endpoint.</td></tr><tr><td>Delete Message Batch</td><td><code>deleteMessageBatch</code></td><td>Delete a Message Batch. Can only delete batches that have finished processing.</td></tr><tr><td>Download File</td><td><code>downloadFile</code></td><td>Download the contents of a file (only files created by tools like code execution are downloadable). Beta endpoint.</td></tr><tr><td>Get File Metadata</td><td><code>getFileMetadata</code></td><td>Get metadata for a file by id. Beta endpoint.</td></tr><tr><td>Get Message Batch</td><td><code>getMessageBatch</code></td><td>Retrieve the status and metadata of a Message Batch.</td></tr><tr><td>Get Message Batch Results</td><td><code>getMessageBatchResults</code></td><td>Stream the results of a Message Batch as a.jsonl file (one result per line), available once processing has ended.</td></tr></tbody></table>

<details>

<summary>View 5 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Model</td><td><code>getModel</code></td><td>Get details of a specific model by id.</td></tr><tr><td>List Files</td><td><code>listFiles</code></td><td>List files within a Workspace, most recently uploaded first. Beta endpoint.</td></tr><tr><td>List Message Batches</td><td><code>listMessageBatches</code></td><td>List all Message Batches within a Workspace, most recently created first.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>List available models, most recently released first.</td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td>Upload a file for use in Messages API requests (referenced later by file_id). Beta endpoint. (multipart/form-data).</td></tr></tbody></table>

</details>

