---
description: "Mistral AI provides AI language models. Create chat completions, embeddings, classifications and moderations, and manage agents, batches and fine-tuning."
hidden: true
---

# Mistral AI

<img src="../../.gitbook/assets/connectors/lg/mistralai.png" alt="Mistral AI logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [mistral.ai](https://mistral.ai) |
| **Authentication** | Access token |
| **Slug** | `mistralai` |

## Setup

Your customers enter their access token for Mistral AI when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Mistral AI from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Mistral AI**.
2. Select **Connect** on the Mistral AI card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Mistral AI's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Append To Conversation</td><td><code>appendToConversation</code></td><td>Append entries to an existing conversation and get the model's response.</td></tr><tr><td>Archive Fine-Tuned Model</td><td><code>archiveFineTunedModel</code></td><td>Archive a fine-tuned model.</td></tr><tr><td>Cancel Batch Job</td><td><code>cancelBatchJob</code></td><td>Request cancellation of a batch job.</td></tr><tr><td>Create Agent</td><td><code>createAgent</code></td><td>Create a reusable agent (beta Agents API). Requires model + name.</td></tr><tr><td>Create Batch Job</td><td><code>createBatchJob</code></td><td>Create an asynchronous batch job. input_files are JSONL file IDs uploaded with purpose=batch; endpoint targets the inference route (e.g. /v1/chat/completions).</td></tr><tr><td>Create Chat Classification</td><td><code>createChatClassification</code></td><td>Run a classifier model on conversation messages.</td></tr><tr><td>Create Chat Completion</td><td><code>createChatCompletion</code></td><td>Generate a chat completion. Provide model + messages. For lowest cost use the cheapest chat model 'ministral-3b-latest'. Other models: mistral-small-latest, mistral-large-latest, ministral-8b-latest, codestral-latest, pixtral-large-latest, magistral-medium-latest.</td></tr><tr><td>Create Chat Moderation</td><td><code>createChatModeration</code></td><td>Classify conversation messages against safety policies. Model: mistral-moderation-latest. input is a list of chat messages.</td></tr><tr><td>Create Classification</td><td><code>createClassification</code></td><td>Run a classifier model on raw text. Requires a classifier model (e.g. a fine-tuned classifier).</td></tr><tr><td>Create Embeddings</td><td><code>createEmbeddings</code></td><td>Create embedding vectors for input text. Model: mistral-embed (text) or codestral-embed (code).</td></tr></tbody></table>

<details>

<summary>View 25 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create FIM Completion</td><td><code>createFimCompletion</code></td><td>Fill-in-the-middle code completion. Use a code model such as codestral-latest. Provide prompt (prefix) and optional suffix.</td></tr><tr><td>Create Moderation</td><td><code>createModeration</code></td><td>Classify raw text against safety policies. Model: mistral-moderation-latest. Returns per-category booleans and scores.</td></tr><tr><td>Delete File</td><td><code>deleteFile</code></td><td>Delete an uploaded file.</td></tr><tr><td>Delete Model</td><td><code>deleteModel</code></td><td>Delete a fine-tuned model.</td></tr><tr><td>Get Agent</td><td><code>getAgent</code></td><td>Retrieve an agent. Optional agent_version query.</td></tr><tr><td>Get Batch Job</td><td><code>getBatchJob</code></td><td>Retrieve a batch job.</td></tr><tr><td>Get Conversation</td><td><code>getConversation</code></td><td>Retrieve a conversation's metadata.</td></tr><tr><td>Get Conversation History</td><td><code>getConversationHistory</code></td><td>Retrieve all entries of a conversation in chronological order.</td></tr><tr><td>Get Conversation Messages</td><td><code>getConversationMessages</code></td><td>Retrieve only the message entries of a conversation.</td></tr><tr><td>Get File Signed URL</td><td><code>getFileSignedUrl</code></td><td>Get a temporary signed download URL for a file. expiry in hours (1-168, default 24).</td></tr><tr><td>List Agents</td><td><code>listAgents</code></td><td>List agents. Returns a JSON array of agent objects (wrapped under 'data' in this contract).</td></tr><tr><td>List Batch Jobs</td><td><code>listBatchJobs</code></td><td>List batch jobs. Filter by model, status, metadata, created_after, created_by_me.</td></tr><tr><td>List Conversations</td><td><code>listConversations</code></td><td>List conversations sorted by creation time.</td></tr><tr><td>List Files</td><td><code>listFiles</code></td><td>List uploaded files. Supports pagination and filtering by purpose/source/sample_type/search.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>List all models available to your account (base + fine-tuned).</td></tr><tr><td>Process OCR</td><td><code>processOcr</code></td><td>Run OCR on a document or image. Model: mistral-ocr-latest. Provide document as {document_url} (DocumentURLChunk), {image_url} (ImageURLChunk), or {file_id} (FileChunk).</td></tr><tr><td>Restart Conversation</td><td><code>restartConversation</code></td><td>Restart a conversation from a given entry.</td></tr><tr><td>Retrieve File</td><td><code>retrieveFile</code></td><td>Retrieve metadata for an uploaded file.</td></tr><tr><td>Retrieve Model</td><td><code>retrieveModel</code></td><td>Retrieve a single model's metadata and capabilities.</td></tr><tr><td>Start Conversation</td><td><code>startConversation</code></td><td>Start a conversation (beta Conversations API). Provide inputs plus either model or agent_id.</td></tr><tr><td>Unarchive Fine-Tuned Model</td><td><code>unarchiveFineTunedModel</code></td><td>Unarchive a fine-tuned model.</td></tr><tr><td>Update Agent</td><td><code>updateAgent</code></td><td>Update an agent (creates a new version).</td></tr><tr><td>Update Agent Version</td><td><code>updateAgentVersion</code></td><td>Switch an agent's active version.</td></tr><tr><td>Update Fine-Tuned Model</td><td><code>updateFineTunedModel</code></td><td>Update name/description of a fine-tuned model.</td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td>Upload a file (max 512MB) for fine-tune, batch, or ocr purposes. (multipart/form-data). Pass the file via input.file and purpose.</td></tr></tbody></table>

</details>

