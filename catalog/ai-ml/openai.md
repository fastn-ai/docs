---
description: "OpenAI provides GPT and other AI models. Create chat completions, embeddings, images and moderations, and manage files, batches and fine-tuning jobs."
hidden: true
---

# OpenAI

<img src="../../.gitbook/assets/connectors/lg/openai.png" alt="OpenAI logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [openai.com](https://openai.com) |
| **Authentication** | Access token |
| **Slug** | `openai` |

## Setup

Your customers enter their access token for OpenAI when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect OpenAI from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **OpenAI**.
2. Select **Connect** on the OpenAI card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use OpenAI's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Cancel Batch</td><td><code>cancelBatch</code></td><td>Cancels an in-progress batch.</td></tr><tr><td>Cancel Fine-tuning Job</td><td><code>cancelFineTuningJob</code></td><td>Immediately cancel a fine-tune job.</td></tr><tr><td>Cancel Vector Store File Batch</td><td><code>cancelVectorStoreFileBatch</code></td><td>Cancel a vector store file batch (files in progress will be cancelled).</td></tr><tr><td>Create Batch</td><td><code>createBatch</code></td><td>Creates and executes a batch from an uploaded file of requests.</td></tr><tr><td>Create Chat Completion</td><td><code>createChatCompletion</code></td><td>Create a model response for the given chat conversation.</td></tr><tr><td>Create Embeddings</td><td><code>createEmbeddings</code></td><td>Creates an embedding vector representing the input text.</td></tr><tr><td>Create Fine-tuning Job</td><td><code>createFineTuningJob</code></td><td>Creates a fine-tuning job which begins the process of training a model from a dataset.</td></tr><tr><td>Create Image</td><td><code>createImage</code></td><td>Creates an image given a text prompt.</td></tr><tr><td>Create Image Edit</td><td><code>createImageEdit</code></td><td>Creates an edited or extended image given source image(s) and a prompt. (multipart/form-data).</td></tr><tr><td>Create Moderation</td><td><code>createModeration</code></td><td>Classifies if text and/or image inputs are potentially harmful.</td></tr></tbody></table>

<details>

<summary>View 34 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Response</td><td><code>createResponse</code></td><td>Create a model response using the Responses API.</td></tr><tr><td>Create Speech</td><td><code>createSpeech</code></td><td>Generates audio from the input text (text-to-speech). Returns binary audio.</td></tr><tr><td>Create Transcription</td><td><code>createTranscription</code></td><td>Transcribes audio into the input language. (multipart/form-data).</td></tr><tr><td>Create Translation</td><td><code>createTranslation</code></td><td>Translates audio into English. (multipart/form-data).</td></tr><tr><td>Create Vector Store</td><td><code>createVectorStore</code></td><td>Create a vector store.</td></tr><tr><td>Create Vector Store File</td><td><code>createVectorStoreFile</code></td><td>Attach a file to a vector store.</td></tr><tr><td>Create Vector Store File Batch</td><td><code>createVectorStoreFileBatch</code></td><td>Create a vector store file batch to attach multiple files at once.</td></tr><tr><td>Delete File</td><td><code>deleteFile</code></td><td>Delete a file.</td></tr><tr><td>Delete Model</td><td><code>deleteModel</code></td><td>Delete a fine-tuned model (requires Owner role).</td></tr><tr><td>Delete Response</td><td><code>deleteResponse</code></td><td>Delete a model response with the given ID.</td></tr><tr><td>Delete Vector Store</td><td><code>deleteVectorStore</code></td><td>Delete a vector store.</td></tr><tr><td>Delete Vector Store File</td><td><code>deleteVectorStoreFile</code></td><td>Delete a vector store file (removes association; does not delete the file).</td></tr><tr><td>Get Batch</td><td><code>getBatch</code></td><td>Retrieves a batch.</td></tr><tr><td>Get File</td><td><code>getFile</code></td><td>Returns information about a specific file.</td></tr><tr><td>Get File Content</td><td><code>getFileContent</code></td><td>Returns the contents of the specified file.</td></tr><tr><td>Get Fine-tuning Job</td><td><code>getFineTuningJob</code></td><td>Get info about a fine-tuning job.</td></tr><tr><td>Get Model</td><td><code>getModel</code></td><td>Retrieves a model instance by ID.</td></tr><tr><td>Get Response</td><td><code>getResponse</code></td><td>Retrieve a model response with the given ID.</td></tr><tr><td>Get Vector Store</td><td><code>getVectorStore</code></td><td>Retrieves a vector store.</td></tr><tr><td>Get Vector Store File</td><td><code>getVectorStoreFile</code></td><td>Retrieves a vector store file.</td></tr><tr><td>Get Vector Store File Batch</td><td><code>getVectorStoreFileBatch</code></td><td>Retrieves a vector store file batch.</td></tr><tr><td>List Batches</td><td><code>listBatches</code></td><td>List your organization's batches.</td></tr><tr><td>List Files</td><td><code>listFiles</code></td><td>Returns a list of files.</td></tr><tr><td>List Fine-tuning Checkpoints</td><td><code>listFineTuningCheckpoints</code></td><td>List checkpoints for a fine-tuning job.</td></tr><tr><td>List Fine-tuning Events</td><td><code>listFineTuningEvents</code></td><td>Get status updates for a fine-tuning job.</td></tr><tr><td>List Fine-tuning Jobs</td><td><code>listFineTuningJobs</code></td><td>List your organization's fine-tuning jobs.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>Lists the currently available models.</td></tr><tr><td>List Response Input Items</td><td><code>listResponseInputItems</code></td><td>Returns a list of input items for a given response.</td></tr><tr><td>List Vector Store File Batch Files</td><td><code>listVectorStoreFileBatchFiles</code></td><td>Returns a list of files in a vector store file batch.</td></tr><tr><td>List Vector Store Files</td><td><code>listVectorStoreFiles</code></td><td>Returns a list of vector store files.</td></tr><tr><td>List Vector Stores</td><td><code>listVectorStores</code></td><td>Returns a list of vector stores.</td></tr><tr><td>Search Vector Store</td><td><code>searchVectorStore</code></td><td>Search a vector store for relevant chunks based on a query.</td></tr><tr><td>Update Vector Store</td><td><code>updateVectorStore</code></td><td>Modifies a vector store.</td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td>Upload a file that can be used across endpoints (assistants, fine-tuning, batch, vision). (multipart/form-data).</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Batch Cancelled</td><td><code>batch.cancelled</code></td><td>A batch job was cancelled.</td></tr><tr><td>Batch Completed</td><td><code>batch.completed</code></td><td>A batch job completed.</td></tr><tr><td>Batch Expired</td><td><code>batch.expired</code></td><td>A batch job expired before completing.</td></tr><tr><td>Batch Failed</td><td><code>batch.failed</code></td><td>A batch job failed.</td></tr><tr><td>Eval Run Canceled</td><td><code>eval.run.canceled</code></td><td>An evaluation run was canceled.</td></tr><tr><td>Eval Run Failed</td><td><code>eval.run.failed</code></td><td>An evaluation run failed.</td></tr><tr><td>Eval Run Succeeded</td><td><code>eval.run.succeeded</code></td><td>An evaluation run completed successfully.</td></tr><tr><td>Fine-tuning Job Cancelled</td><td><code>fine_tuning.job.cancelled</code></td><td>A fine-tuning job was cancelled.</td></tr><tr><td>Fine-tuning Job Failed</td><td><code>fine_tuning.job.failed</code></td><td>A fine-tuning job failed.</td></tr><tr><td>Fine-tuning Job Succeeded</td><td><code>fine_tuning.job.succeeded</code></td><td>A fine-tuning job completed successfully.</td></tr></tbody></table>

<details>

<summary>View 5 more events</summary>

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Realtime Call Incoming</td><td><code>realtime.call.incoming</code></td><td>An incoming Realtime SIP call was received.</td></tr><tr><td>Response Cancelled</td><td><code>response.cancelled</code></td><td>A background Response request was cancelled.</td></tr><tr><td>Response Completed</td><td><code>response.completed</code></td><td>A background Response request completed successfully.</td></tr><tr><td>Response Failed</td><td><code>response.failed</code></td><td>A background Response request failed.</td></tr><tr><td>Response Incomplete</td><td><code>response.incomplete</code></td><td>A background Response request finished incomplete.</td></tr></tbody></table>

</details>
