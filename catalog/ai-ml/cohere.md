---
description: "Cohere provides AI language models. Chat, create embeddings, rerank and classify text, tokenize, and manage datasets, batches and embed jobs."
hidden: true
---

# Cohere

<img src="../../.gitbook/assets/connectors/lg/cohere.png" alt="Cohere logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [cohere.com](https://cohere.com) |
| **Authentication** | Access token |
| **Slug** | `cohere` |

## Setup

Your customers enter their access token for Cohere when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Cohere from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Cohere**.
2. Select **Connect** on the Cohere card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Cohere's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Cancel a batch</td><td><code>cancelBatch</code></td><td>Cancel a batch. Cancels an in-progress batch</td></tr><tr><td>Cancel Embed Job</td><td><code>cancelEmbedJob</code></td><td>Cancel an Embed Job. This API allows users to cancel an active embed job. Once invoked, the embedding process will be terminated, and users will be charged for the embeddings processed up to the cancellation point. It's important to note that partial results will not be available to users after cancellation.</td></tr><tr><td>Chat</td><td><code>chat</code></td><td>Chat API (v2). Generates a text response to a user message. To learn how to use the Chat API and RAG follow our [Text Generation guides](https://docs.cohere.com/v2/docs/chat-api). Follow the [Migration Guide](https://docs.cohere.com/v2/docs/migrating-v1-to-v2) for instructions on moving from API v1 to API v2.</td></tr><tr><td>Chat API (v1)</td><td><code>chatV1</code></td><td>Chat API (v1). Generates a streamed text response to a user message. To learn how to use the Chat API and RAG follow our [Text Generation guides](https://docs.cohere.com/docs/chat-api).</td></tr><tr><td>Check API Key</td><td><code>checkApiKey</code></td><td>Check API key. Checks that the api key in the Authorization header is valid and active</td></tr><tr><td>Create a batch</td><td><code>createBatch</code></td><td>Create a batch. Creates and executes a batch from an uploaded dataset of requests</td></tr><tr><td>Create Dataset</td><td><code>createDataset</code></td><td>Create a dataset by uploading a text file (multipart/form-data, field 'data'). Returns the dataset id; poll getDataset until validation_status is validated before using it in an embed job.</td></tr><tr><td>Create Embed Job</td><td><code>createEmbedJob</code></td><td>Create an Embed Job. This API launches an async Embed job for a [Dataset](https://docs.cohere.com/docs/datasets) of type `embed-input`. The result of a completed embed job is new Dataset of type `embed-output`, which contains the original text entries and the corresponding embeddings.</td></tr><tr><td>Delete Dataset</td><td><code>deleteDataset</code></td><td>Delete a Dataset. Delete a dataset by ID. Datasets are automatically deleted after 30 days, but they can also be deleted manually.</td></tr><tr><td>Detokenize</td><td><code>detokenize</code></td><td>Detokenize. This endpoint takes tokens using byte-pair encoding and returns their text representation. To learn more about tokenization and byte pair encoding, see the tokens page.</td></tr></tbody></table>

<details>

<summary>View 15 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Embed</td><td><code>embed</code></td><td>Embed API (v2). This endpoint returns text embeddings. An embedding is a list of floating point numbers that captures semantic information about the text that it represents. Embeddings can be used to create text classifiers as well as empower semantic search. To learn more about embeddings, see the embedding page. If you want to learn more how to use the embedding model, have a look at the [Semantic Search Guide](https://docs.cohere.com/docs/semantic-search).</td></tr><tr><td>Embed API (v1)</td><td><code>embedV1</code></td><td>Embed API (v1). This endpoint returns text and image embeddings. An embedding is a list of floating point numbers that captures semantic information about the content that it represents. Embeddings can be used to create classifiers as well as empower semantic search. To learn more about embeddings, see the embedding page. If you want to learn more how to use the embedding model, have a look at the [Semantic Search Guide](https://docs.cohere.com/docs/semantic-search).</td></tr><tr><td>Get Dataset</td><td><code>getDataset</code></td><td>Get a Dataset. Retrieve a dataset by ID. See ['Datasets'](https://docs.cohere.com/docs/datasets) for more information.</td></tr><tr><td>Get Dataset Usage</td><td><code>getDatasetUsage</code></td><td>Get Dataset Usage. View the dataset storage usage for your Organization. Each Organization can have up to 10GB of storage across all their users.</td></tr><tr><td>Get Embed Job</td><td><code>getEmbedJob</code></td><td>Fetch an Embed Job. This API retrieves the details about an embed job started by the same user.</td></tr><tr><td>Get Model</td><td><code>getModel</code></td><td>Get a Model. Returns the details of a model, provided its name.</td></tr><tr><td>List batches</td><td><code>listBatches</code></td><td>List batches. List the batches for the current user</td></tr><tr><td>List Datasets</td><td><code>listDatasets</code></td><td>List Datasets. List datasets that have been created.</td></tr><tr><td>List Embed Jobs</td><td><code>listEmbedJobs</code></td><td>List Embed Jobs. The list embed job endpoint allows users to view all embed jobs history for that specific user.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>List Models. Returns a list of models available for use.</td></tr><tr><td>Parse API (v2)</td><td><code>parseDocument</code></td><td>Parse API (v2). Parse a document image into structured output. Use `output_format` to select blocks or markdown (default). Currently supports `document.type = image_url` only (data URI or remote http(s) image URL). PDF / file URL inputs are not yet supported. Image limits: 20 MB file size; 50 megapixels or 200 MB decoded (whichever is exceeded first).</td></tr><tr><td>Rerank</td><td><code>rerank</code></td><td>Rerank API (v2). This endpoint takes in a query and a list of texts and produces an ordered array with each text assigned a relevance score.</td></tr><tr><td>Rerank API (v1)</td><td><code>rerankV1</code></td><td>Rerank API (v1). This endpoint takes in a query and a list of texts and produces an ordered array with each text assigned a relevance score.</td></tr><tr><td>Retrieve a batch</td><td><code>getBatch</code></td><td>Retrieve a batch. Retrieves a batch</td></tr><tr><td>Tokenize</td><td><code>tokenize</code></td><td>Tokenize. This endpoint splits input text into smaller units called tokens using byte-pair encoding (BPE). To learn more about tokenization and byte pair encoding, see the tokens page.</td></tr></tbody></table>

</details>

