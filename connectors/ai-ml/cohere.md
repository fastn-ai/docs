---
description: "Cohere AI platform connector (api.cohere.com)."
---

# Cohere

Cohere AI platform connector (api.cohere.com). Full coverage of v2 chat, embed, rerank and v1 classify, tokenize/detokenize, models, datasets, embed-jobs, and check-api-key. Cheapest chat model: command-r7b-12-2024.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [cohere.com](https://cohere.com) |
| **Authentication** | Bearer token |
| **Actions** | 25 |
| **Events** | 0 |
| **Slug** | `cohere` |

## Use it

Add Cohere from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cohere.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel a batch | `cancelBatch` | Cancel a batch. Cancels an in-progress batch |
| Cancel Embed Job | `cancelEmbedJob` | Cancel an Embed Job. This API allows users to cancel an active embed job. Once invoked, the embedding process will be terminated, and users will be charged for the embeddings processed up to the cancellation point. It's important to note that partial results will not be available to users after cancellation. |
| Chat | `chat` | Chat API (v2). Generates a text response to a user message. To learn how to use the Chat API and RAG follow our [Text Generation guides](https://docs.cohere.com/v2/docs/chat-api). Follow the [Migration Guide](https://docs.cohere.com/v2/docs/migrating-v1-to-v2) for instructions on moving from API v1 to API v2. |
| Chat API (v1) | `chatV1` | Chat API (v1). Generates a streamed text response to a user message. To learn how to use the Chat API and RAG follow our [Text Generation guides](https://docs.cohere.com/docs/chat-api). |
| Check API Key | `checkApiKey` | Check API key. Checks that the api key in the Authorization header is valid and active |
| Create a batch | `createBatch` | Create a batch. Creates and executes a batch from an uploaded dataset of requests |
| Create Dataset | `createDataset` | Create a dataset by uploading a text file (multipart/form-data, field 'data'). POST /v1/datasets. Returns the dataset id; poll getDataset until validation_status is validated before using it in an embed job. |
| Create Embed Job | `createEmbedJob` | Create an Embed Job. This API launches an async Embed job for a [Dataset](https://docs.cohere.com/docs/datasets) of type `embed-input`. The result of a completed embed job is new Dataset of type `embed-output`, which contains the original text entries and the corresponding embeddings. |
| Delete Dataset | `deleteDataset` | Delete a Dataset. Delete a dataset by ID. Datasets are automatically deleted after 30 days, but they can also be deleted manually. |
| Detokenize | `detokenize` | Detokenize. This endpoint takes tokens using byte-pair encoding and returns their text representation. To learn more about tokenization and byte pair encoding, see the tokens page. |
| Embed | `embed` | Embed API (v2). This endpoint returns text embeddings. An embedding is a list of floating point numbers that captures semantic information about the text that it represents. Embeddings can be used to create text classifiers as well as empower semantic search. To learn more about embeddings, see the embedding page. If you want to learn more how to use the embedding model, have a look at the [Semantic Search Guide](https://docs.cohere.com/docs/semantic-search). |
| Embed API (v1) | `embedV1` | Embed API (v1). This endpoint returns text and image embeddings. An embedding is a list of floating point numbers that captures semantic information about the content that it represents. Embeddings can be used to create classifiers as well as empower semantic search. To learn more about embeddings, see the embedding page. If you want to learn more how to use the embedding model, have a look at the [Semantic Search Guide](https://docs.cohere.com/docs/semantic-search). |
| Get Dataset | `getDataset` | Get a Dataset. Retrieve a dataset by ID. See ['Datasets'](https://docs.cohere.com/docs/datasets) for more information. |
| Get Dataset Usage | `getDatasetUsage` | Get Dataset Usage. View the dataset storage usage for your Organization. Each Organization can have up to 10GB of storage across all their users. |
| Get Embed Job | `getEmbedJob` | Fetch an Embed Job. This API retrieves the details about an embed job started by the same user. |
| Get Model | `getModel` | Get a Model. Returns the details of a model, provided its name. |
| List batches | `listBatches` | List batches. List the batches for the current user |
| List Datasets | `listDatasets` | List Datasets. List datasets that have been created. |
| List Embed Jobs | `listEmbedJobs` | List Embed Jobs. The list embed job endpoint allows users to view all embed jobs history for that specific user. |
| List Models | `listModels` | List Models. Returns a list of models available for use. |
| Parse API (v2) | `parseDocument` | Parse API (v2). Parse a document image into structured output. Use `output_format` to select blocks or markdown (default). Currently supports `document.type = image_url` only (data URI or remote http(s) image URL). PDF / file URL inputs are not yet supported. Image limits: 20 MB file size; 50 megapixels or 200 MB decoded (whichever is exceeded first). |
| Rerank | `rerank` | Rerank API (v2). This endpoint takes in a query and a list of texts and produces an ordered array with each text assigned a relevance score. |
| Rerank API (v1) | `rerankV1` | Rerank API (v1). This endpoint takes in a query and a list of texts and produces an ordered array with each text assigned a relevance score. |
| Retrieve a batch | `getBatch` | Retrieve a batch. Retrieves a batch |
| Tokenize | `tokenize` | Tokenize. This endpoint splits input text into smaller units called tokens using byte-pair encoding (BPE). To learn more about tokenization and byte pair encoding, see the tokens page. |
