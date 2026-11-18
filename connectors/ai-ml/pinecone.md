---
description: "Pinecone vector database connector (API version 2026-04)."
hidden: true
---

# Pinecone

<img src="../../.gitbook/assets/connectors/pinecone.png" alt="Pinecone logo" width="64">

Pinecone vector database connector (API version 2026-04). Wraps the Database control plane (indexes, collections, backups, restore jobs), Database data plane (vectors upsert/query/fetch/update/delete/list, namespaces, records, bulk imports), Inference API (embed, rerank, models), and Assistant API (assistants, files, chat, context). Auth via Api-Key header. Data-plane and assistant-data calls target a per-resource host supplied per request.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [pinecone.io](https://pinecone.io) |
| **Authentication** | API key |
| **Slug** | `pinecone` |

## Use it

Add Pinecone from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pinecone.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Assistant Chat Completions (OpenAI-compatible) | `assistantChatCompletions` | Chat with an assistant through an OpenAI-compatible Chat Completion interface. Useful for inline citations / OpenAI-compatible responses but with limited functionality vs the standard chat interface. Assistant data-plane operation; requires assistant_host. |
| Cancel Bulk Import | `cancelBulkImport` | Cancel an import operation if it is not yet finished. No effect if already finished. Data-plane: requires the index host. |
| Chat With Assistant | `chatAssistant` | Chat with an assistant and get back citations in structured form. The recommended way to chat with an assistant, offering more control and functionality than the OpenAI-compatible interface. Assistant data-plane operation; requires assistant_host. |
| Configure Index | `configureIndex` | Configure an existing index (scaling, read capacity, deletion protection, tags, or integrated embedding). All body fields are optional; only send the ones you want to change. Control-plane PATCH endpoint. |
| Create Assistant | `createAssistant` | Create a Pinecone assistant. Specify the assistant name, optional instructions, optional metadata, and the deployment region (us or eu). |
| Create Backup | `createBackup` | Create a backup of an index. Optional name and description. |
| Create Collection | `createCollection` | Create a Pinecone collection from a source index. Serverless indexes do not support collections. |
| Create Index | `createIndex` | Create a Pinecone index. Specify name, dimension, metric, vector_type, deletion_protection, tags, and the deployment spec (serverless/pod/byoc). The spec is a nested object passed as a templated object input. Control-plane endpoint. |
| Create Index For Model | `createIndexForModel` | Create an index with integrated embedding. Pinecone uses a hosted embedding model to convert source text automatically during upsert and search. Provide name, cloud, region, and embed config. Control-plane endpoint. |
| Create Index From Backup | `createIndexFromBackup` | Create an index from a backup. Returns the restore job id and the new index id. |

<details>

<summary>See 45 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Namespace | `createNamespace` | Create a namespace in a serverless index. Data-plane: requires the index host. |
| Delete Assistant | `deleteAssistant` | Delete an existing Pinecone assistant by its name. |
| Delete Assistant File | `deleteAssistantFile` | Delete an uploaded file from an assistant. Asynchronous; returns an operation id (202) or empty body (204 for files that previously failed processing). Assistant data-plane operation; requires assistant_host. |
| Delete Backup | `deleteBackup` | Delete a backup by backup_id. |
| Delete Collection | `deleteCollection` | Delete an existing collection by name. Serverless indexes do not support collections. |
| Delete Index | `deleteIndex` | Delete an existing index by name. Returns 202 Accepted with no body. Fails with 403 if deletion protection is enabled. Control-plane endpoint. |
| Delete Namespace | `deleteNamespace` | Delete a namespace from a serverless index. Irreversible; all data in the namespace is permanently deleted. Data-plane: requires the index host. |
| Delete Vectors | `deleteVectors` | Delete records by id, by metadata filter, or all records from a single namespace. ids is mutually exclusive with filter and deleteAll. Data-plane operation; requires index_host. |
| Describe Assistant File | `describeAssistantFile` | Get the current status and metadata of a file uploaded to an assistant. Optionally include the signed URL. Assistant data-plane operation; requires assistant_host. |
| Describe Assistant Operation | `describeAssistantOperation` | Get the status of a single operation on an assistant by operation_id. Assistant data-plane operation; requires assistant_host. |
| Describe Backup | `describeBackup` | Get a description of a backup by backup_id. |
| Describe Bulk Import | `describeBulkImport` | Return details of a specific import operation. Data-plane: requires the index host. |
| Describe Collection | `describeCollection` | Get a description of a collection by name. Serverless indexes do not support collections. |
| Describe Index | `describeIndex` | Get a description of an index by name, including its host (needed for data-plane calls), dimension, metric, spec, and status. Control-plane endpoint. |
| Describe Index Stats | `describeIndexStats` | Return statistics about the contents of an index, including vector count per namespace, number of dimensions, and index fullness. Data-plane operation; requires index_host. Optional metadata filter limits stats to matching vectors. |
| Describe Model | `getModel` | Get a description of a single model hosted by Pinecone by its name. GET /models/{model_name}. |
| Describe Namespace | `describeNamespace` | Describe a namespace in a serverless index, including the total number of vectors. Data-plane: requires the index host. |
| Describe Restore Job | `describeRestoreJob` | Get a description of a restore job by job_id. |
| Fetch Vectors | `fetchVectors` | Look up and return records by ID from a single namespace. Returned records include vector data and/or metadata. GET with query params; ids is repeated. Data-plane operation; requires index_host. |
| Fetch Vectors By Metadata | `fetchVectorsByMetadata` | Look up and return records by metadata from a single namespace. Returned records include vector data and metadata. Data-plane operation; requires index_host. |
| Generate Embeddings | `embed` | Generate vector embeddings for input data using Pinecone's hosted embedding models. POST /embed. Provide the embedding model name and a list of text inputs. |
| Get Assistant | `getAssistant` | Get the status and configuration of a Pinecone assistant by its name. |
| List Assistant Files | `listAssistantFiles` | List all files in an assistant, with an option to filter files with metadata. Assistant data-plane operation; requires the per-assistant host (assistant_host) returned by describe_assistant .host. |
| List Assistant Operations | `listAssistantOperations` | List all operations for an assistant (in progress, recently completed, or failed). Successful and failed operations are retained 30 days. Filter by operation_type and status. Assistant data-plane operation; requires assistant_host. |
| List Assistants | `listAssistants` | List all assistants in a Pinecone project. Supports pagination via limit and pagination_token. Returns the assistants array and a pagination object. |
| List Available Models | `listModels` | List the embedding and reranking models hosted by Pinecone. GET /models. Optionally filter by type and vector_type. |
| List Bulk Imports | `listBulkImports` | List all recent and ongoing import operations. Data-plane: requires the index host. Supports pagination. |
| List Collections | `listCollections` | List all collections in a project. Serverless indexes do not support collections. |
| List Index Backups | `listIndexBackups` | List all backups for a specific index. |
| List Indexes | `listIndexes` | List all indexes in a Pinecone project. Returns an array of index descriptions including name, host, dimension, metric, spec, and status. Control-plane endpoint. |
| List Namespaces | `listNamespaces` | List all namespaces in a serverless index. Data-plane: requires the index host. Supports pagination and prefix filtering. |
| List Project Backups | `listProjectBackups` | List all backups for all indexes in a project. |
| List Restore Jobs | `listRestoreJobs` | List all restore jobs for a project. |
| List Vector IDs | `listVectors` | List the IDs of records in a single namespace of a serverless index. Optional prefix limits results to IDs with a common prefix. Returns up to 100 IDs at a time by default with a pagination_token. GET with query params. Data-plane operation; requires index_host. Serverless indexes only. |
| Query Vectors | `queryVectors` | Search a namespace using a query vector or vector id. Retrieves the ids of the most similar items in a namespace, along with their similarity scores. Data-plane operation; requires the per-index host (index_host from describe_index .host). |
| Rerank Results | `rerank` | Rerank documents according to their relevance to a query using a Pinecone hosted reranking model. POST /rerank. |
| Retrieve Assistant Context | `retrieveAssistantContext` | Retrieve context snippets from an assistant to use as part of RAG or any agentic flow. Provide exactly one of query or messages. Assistant data-plane operation; requires assistant_host. |
| Search Records | `searchRecords` | Search a namespace with a query text, query vector, or record ID and return the most similar records with similarity scores. Optionally rerank. Searching with text requires an index with integrated embedding. Data-plane: requires the index host. |
| Start Bulk Import | `startBulkImport` | Start an asynchronous import of vectors from object storage into an index. Data-plane: requires the index host. |
| Update Assistant | `updateAssistant` | Update an existing Pinecone assistant. You can modify the assistant's instructions and/or metadata. |
| Update Vector | `updateVector` | Update records by ID or by metadata filter in a namespace. Updating by ID changes the vector and/or metadata of a single record. If set_metadata is included, only the specified metadata fields are modified. Data-plane operation; requires index_host. |
| Upload Assistant File | `uploadAssistantFile` | Upload a file to the specified assistant (multipart/form-data). An identifier is generated automatically. Asynchronous; the response includes an operation id to poll via describe_operation. Assistant data-plane operation; requires assistant_host. |
| Upsert Assistant File | `upsertAssistantFile` | Create or replace a file in the specified assistant by assistant_file_id (multipart/form-data). If the file exists it is replaced; otherwise a new one is created with that id. Asynchronous; returns an operation id. Assistant data-plane operation; requires assistant_host. |
| Upsert Records | `upsertRecords` | Upsert text records into a namespace; Pinecone converts text to vectors using the index's hosted embedding model. Body is newline-delimited JSON (application/x-ndjson): one record per line. Each record must include an _id field plus a field matching the index field_map (e.g. chunk_text); other fields are stored as metadata. Supported only for indexes with integrated embedding. Data-plane: requires the index host. |
| Upsert Vectors | `upsertVectors` | Upsert records into a namespace. If a new value is upserted for an existing record ID, it overwrites the previous value. Data-plane operation; requires the per-index host (index_host). |

</details>
