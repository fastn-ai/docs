---
description: "Future AGI Agent Command Center gateway (https://gateway.futureagi.com): an OpenAI-compatible LLM gateway with routing, caching, guardrails and cost tracking."
hidden: true
---

# Future AGI

<img src="../../.gitbook/assets/connectors/lg/futureagi.png" alt="Future AGI logo">

Future AGI Agent Command Center gateway (https://gateway.futureagi.com): an OpenAI-compatible LLM gateway with routing, caching, guardrails and cost tracking. Covers chat and text completions, token counting, embeddings, reranking, search, OCR, audio (TTS, transcription, translation), image and video generation, files and vector stores, the Assistants API (assistants, threads, messages, runs, steps), the Responses API, async and scheduled jobs, Anthropic and Google native pass-through, model listing, MCP and A2A, plus the admin (/-/) endpoints for virtual keys, org config, provider key rotation, batches, health and MCP management.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [futureagi.com](https://futureagi.com) |
| **Authentication** | Bearer token |
| **Slug** | `futureagi` |

## Use it

Add Future AGI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.futureagi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add API Key Credits (Admin) | `addApiKeyCredits` | Add a USD credit amount to a managed virtual key's balance (POST /-/keys/{key_id}/credits). Requires an admin token. |
| Add Vector Store File | `addVectorStoreFile` | Attach an uploaded file to a vector store for indexing (POST /v1/vector_stores/{id}/files). |
| Bulk Load Org Configs (Admin) | `bulkLoadOrgConfigs` | Load several organization configurations in one call (POST /-/orgs/configs/bulk). Requires an admin token. |
| Cancel Async Job | `cancelAsyncJob` | Cancel a pending or running async inference job (DELETE /v1/async/{job_id}). |
| Cancel Batch (Admin) | `cancelBatch` | Cancel an in-progress batch job (POST /-/batches/{batch_id}/cancel). Requires an admin token. |
| Cancel Run | `cancelRun` | Cancel a run that is in_progress (POST /v1/threads/{id}/runs/{run_id}/cancel). |
| Cancel Scheduled Job | `cancelScheduledJob` | Cancel a scheduled completion job (DELETE /v1/scheduled/{job_id}). |
| Cancel Video | `cancelVideo` | Cancel a queued or in-progress video generation job (DELETE /v1/videos/{video_id}). |
| Count Anthropic Tokens | `countAnthropicTokens` | Count input tokens for an Anthropic-format message request (POST /v1/messages/count_tokens) without generating a response. |
| Count Tokens | `countTokens` | Count the tokens a set of chat messages would consume for a given model, and how much of the model's context window remains (POST /v1/count_tokens). Does not call the model. |
| Create Anthropic Message | `createAnthropicMessage` | Anthropic Messages API in native format via the gateway (POST /v1/messages): model, max_tokens, messages, optional system prompt, tools, thinking and sampling settings. |
| Create API Key (Admin) | `createApiKey` | Create a virtual API key with model/provider/IP/tool restrictions, rate limits, expiry and metadata (POST /-/keys). Requires an admin token. The raw key value is returned only once. |
| Create Assistant | `createAssistant` | Create an assistant with instructions, an OpenAI model and optional tools (POST /v1/assistants). Threads and runs are stored on OpenAI, so the model must be an OpenAI model. |
| Create Async Chat Completion | `createAsyncChatCompletion` | Submit a chat completion as an async job (POST /v1/chat/completions with x-agentcc-async: true). Returns immediately with a job id; poll Get Async Job for the result or cancel it with Cancel Async Job. |
| Create Batch (Admin) | `createBatch` | Submit a batch job from an uploaded JSONL input file (POST /-/batches): input_file_id, endpoint and completion_window as in the OpenAI Batch API. Requires an admin token. |
| Create Chat Completion | `createChatCompletion` | Generate a chat completion through the gateway (OpenAI-compatible POST /v1/chat/completions). Supports any routed provider model, function calling, vision content parts, structured outputs and unknown provider-specific fields passed through. Optional x-agentcc-* headers control session/trace tracking, metadata, caching, provider lock and guardrail policy. Set stream=true only if your client can consume SSE. |
| Create Embeddings | `createEmbeddings` | Generate vector embeddings for one or more texts (POST /v1/embeddings). Pass an array to embed in batch; optionally reduce dimensions or request base64 encoding. |
| Create Response | `createResponse` | Generate a model response with the OpenAI Responses API (POST /v1/responses): text or structured input items, optional instructions, tools and previous_response_id for multi-turn state. |
| Create Run | `createRun` | Run an assistant on a thread (POST /v1/threads/{id}/runs). Poll Get Run until status is completed or requires_action. |
| Create Scheduled Completion | `createScheduledCompletion` | Schedule a chat completion request to run at a future time (POST /v1/scheduled). Requires scheduled completions to be enabled for your organization. |
| Create Speech | `createSpeech` | Convert text to spoken audio (POST /v1/audio/speech). Returns raw audio bytes in the requested format (mp3 by default) using models such as tts-1, tts-1-hd or gpt-4o-mini-tts. |
| Create Speech Stream | `createSpeechStream` | Streaming text-to-speech (POST /v1/audio/speech/stream): same parameters as Create Speech, but audio bytes are streamed as they are generated. Best consumed by a streaming client. |
| Create Text Completion | `createCompletion` | Legacy text completion (POST /v1/completions): send a prompt string and receive generated text choices from the selected model. |
| Create Thread | `createThread` | Create a conversation thread (POST /v1/threads), optionally seeded with initial messages, tool resources and metadata. |
| Create Thread And Run | `createThreadAndRun` | Create a thread and start a run on it in one call (POST /v1/threads/runs). |
| Create Thread Message | `createThreadMessage` | Add a message to a thread (POST /v1/threads/{id}/messages). |
| Create Transcription | `createTranscription` | Transcribe an audio file to text (POST /v1/audio/transcriptions, multipart/form-data) with whisper-1, gpt-4o-transcribe or gpt-4o-mini-transcribe. Supports mp3, mp4, mpeg, mpga, m4a, wav and webm; optional language hint, prompt, output format, temperature and timestamp granularities. |
| Create Translation | `createTranslation` | Translate spoken audio in any supported language into English text (POST /v1/audio/translations, multipart/form-data). Same parameters as transcription, output is always English. |
| Create Vector Store | `createVectorStore` | Create a vector store (POST /v1/vector_stores) that indexes uploaded files for semantic search and the Assistants file_search tool. Stored on the upstream OpenAI provider. |
| Create Vector Store File Batch | `createVectorStoreFileBatch` | Attach several uploaded files to a vector store in one call (POST /v1/vector_stores/{id}/file_batches). |
| Create Video | `createVideo` | Submit a video generation job (POST /v1/videos) with a video model such as sora-2 and a prompt. Returns 202 with a queued job; poll Get Video for progress and cancel with Cancel Video. |
| Delete Assistant | `deleteAssistant` | Delete an assistant (DELETE /v1/assistants/{id}). |
| Delete File | `deleteFile` | Delete an uploaded file (DELETE /v1/files/{file_id}). |
| Delete Org Config (Admin) | `deleteOrgConfig` | Delete an organization's gateway configuration (DELETE /-/orgs/{org_id}/config). Requires an admin token. |
| Delete Response | `deleteResponse` | Delete a stored response (DELETE /v1/responses/{id}). |
| Delete Thread | `deleteThread` | Delete a thread and its messages (DELETE /v1/threads/{id}). |
| Delete Thread Message | `deleteThreadMessage` | Delete a message from a thread (DELETE /v1/threads/{id}/messages/{msg_id}). |
| Delete Vector Store | `deleteVectorStore` | Delete a vector store (DELETE /v1/vector_stores/{id}). |
| Generate Content (Google) | `generateContent` | Google GenAI native generateContent via the gateway (POST /v1beta/models/{model}:generateContent) with contents, optional systemInstruction, generationConfig, tools and safetySettings. |
| Generate Image | `generateImage` | Generate images from a text prompt (POST /v1/images/generations) with dall-e-2, dall-e-3 or gpt-image-1. Returns temporary URLs (1 hour) or base64 data when response_format is b64_json. |
| Get A2A Agent Card | `getAgentCard` | Fetch the gateway's Agent-to-Agent (A2A) agent card describing its capabilities and skills (GET /.well-known/agent.json). Available only on gateways with A2A enabled. |
| Get API Key (Admin) | `getApiKey` | Get a virtual API key's details and restrictions (GET /-/keys/{key_id}). Requires an admin token. |
| Get Assistant | `getAssistant` | Retrieve an assistant by id (GET /v1/assistants/{id}). |
| Get Async Job | `getAsyncJob` | Get the status and, when completed, the chat completion result of an async inference job (GET /v1/async/{job_id}). Statuses: queued, running, completed, failed, cancelled. Note: async workers resolve the model by provider/model name (e.g. vertex_ai/gemini-2.5-flash-lite); the provider-lock header does not apply to the background execution. |
| Get Batch (Admin) | `getBatch` | Get the status and request counts of a batch job (GET /-/batches/{batch_id}). Requires an admin token. |
| Get File | `getFile` | Get metadata for an uploaded file (GET /v1/files/{file_id}). Returns 404 file_not_found for unknown ids. |
| Get File Content | `getFileContent` | Download the raw content of an uploaded file (GET /v1/files/{file_id}/content). Returns the file bytes. |
| Get MCP Status (Admin) | `getMcpStatus` | MCP server status: session count, tool/resource/prompt counts and upstream server statuses (GET /-/mcp/status). Requires an admin token. |
| Get Metrics (Admin) | `getMetrics` | Prometheus-format metrics for the gateway (GET /-/metrics). Requires an admin token; available on self-hosted deployments (the hosted gateway returns 404 not_found). |
| Get Model | `getModel` | Retrieve details for a single model by its ID (e.g. gpt-4o-mini, claude-sonnet-4-6). Returns 404 model_not_found for unknown IDs. |
| Get Org Config (Admin) | `getOrgConfig` | Get an organization's gateway configuration: providers, routing, cache, guardrails, rate limits, budgets, IP ACL (GET /-/orgs/{org_id}/config). Requires an admin token. |
| Get Org Provider Health (Admin) | `getOrgProviderHealth` | Provider health status scoped to one organization (GET /-/health/providers/{org_id}). Requires an admin token. |
| Get Provider Health (Admin) | `getProviderHealth` | Health status of all configured LLM providers (GET /-/health/providers). Requires an admin token. |
| Get Provider Key Rotation Status (Admin) | `getProviderKeyRotation` | Get the status of an in-progress provider key rotation (GET /-/admin/providers/{id}/rotation). Requires an admin token. |
| Get Response | `getResponse` | Retrieve a stored response by id (GET /v1/responses/{id}). Returns 404 response_not_found for unknown ids. |
| Get Run | `getRun` | Retrieve a run's status and required actions (GET /v1/threads/{id}/runs/{run_id}). |
| Get Run Step | `getRunStep` | Retrieve one step of a run (GET /v1/threads/{id}/runs/{run_id}/steps/{step_id}). |
| Get Scheduled Job | `getScheduledJob` | Retrieve a scheduled completion job (GET /v1/scheduled/{job_id}). |
| Get Server Config (Admin) | `getServerConfig` | Summary of the running gateway configuration (GET /-/config). Requires an admin token. |
| Get Shadow Stats (Admin) | `getShadowStats` | Statistics for shadow (A/B) experiments that mirror traffic to a candidate model (GET /-/shadow/stats). Requires an admin token. |
| Get Thread | `getThread` | Retrieve a thread by id (GET /v1/threads/{id}). |
| Get Thread Message | `getThreadMessage` | Retrieve a single message from a thread (GET /v1/threads/{id}/messages/{msg_id}). |
| Get Vector Store | `getVectorStore` | Retrieve a vector store by id (GET /v1/vector_stores/{id}). |
| Get Video | `getVideo` | Get the status and progress of a video generation job (GET /v1/videos/{video_id}). Returns 404 video_not_found for unknown ids. |
| Health Check | `healthCheck` | Gateway liveness probe (GET /healthz). Returns {status: ok}. |
| List A2A Agents | `listA2aAgents` | List downstream A2A agents registered with the gateway (GET /v1/agents). Available only on gateways with A2A enabled. |
| List API Keys (Admin) | `listApiKeys` | List virtual API keys and their restrictions (GET /-/keys). Requires an admin token. |
| List Assistants | `listAssistants` | List assistants (GET /v1/assistants) with cursor paging. |
| List Cluster Nodes (Admin) | `listClusterNodes` | List the gateway cluster's nodes (GET /-/cluster/nodes). Requires an admin token; self-hosted clustered deployments (the hosted gateway returns 404 not_found). |
| List Files | `listFiles` | List uploaded files (GET /v1/files), optionally filtered by purpose. |
| List MCP Prompts (Admin) | `listMcpPrompts` | List all prompts registered on the gateway MCP server (GET /-/mcp/prompts). Requires an admin token. |
| List MCP Resources (Admin) | `listMcpResources` | List all resources registered on the gateway MCP server (GET /-/mcp/resources). Requires an admin token. |
| List MCP Tools (Admin) | `listMcpTools` | List all tools registered on the gateway MCP server (GET /-/mcp/tools). Requires an admin token. |
| List Models | `listModels` | List every model available through your Agent Command Center key, with provider, context limits, pricing and capabilities where known. |
| List Org Configs (Admin) | `listOrgConfigs` | List the gateway configurations of all organizations (GET /-/orgs/configs). Requires an admin token. |
| List Run Steps | `listRunSteps` | List the steps (message creations, tool calls) of a run (GET /v1/threads/{id}/runs/{run_id}/steps). |
| List Runs | `listRuns` | List the runs of a thread (GET /v1/threads/{id}/runs) with cursor paging. |
| List Scheduled Jobs | `listScheduledJobs` | List scheduled completion jobs (GET /v1/scheduled). Requires scheduled completions to be enabled for your organization. |
| List Thread Messages | `listThreadMessages` | List the messages in a thread (GET /v1/threads/{id}/messages) with cursor paging and optional run_id filter. |
| List Vector Store Files | `listVectorStoreFiles` | List the files attached to a vector store (GET /v1/vector_stores/{id}/files), optionally filtered by indexing status. |
| List Vector Stores | `listVectorStores` | List vector stores (GET /v1/vector_stores) with cursor paging (limit, order, after, before). |
| List Videos | `listVideos` | List video generation jobs for your key (GET /v1/videos) with limit/offset paging. |
| Liveness Check | `livenessCheck` | Gateway liveness probe alias (GET /livez). Returns {status: ok}. |
| Open MCP Event Stream | `openMcpEventStream` | Open the MCP server-sent-events channel (GET /mcp) for an initialized MCP session. Requires the Mcp-Session-Id issued by the initialize response header. This is an unbounded stream intended for streaming MCP clients. |
| Promote Rotated Provider Key (Admin) | `promoteProviderKeyRotation` | Promote the staged provider key to primary and finish the rotation (POST /-/admin/providers/{id}/rotate/promote). Requires an admin token. |
| Readiness Check | `readinessCheck` | Gateway readiness probe (GET /readyz). Returns {status: ready} when the gateway can serve traffic. |
| Reload Config (Admin) | `reloadConfig` | Reload the gateway configuration from file (POST /-/reload). Requires an admin token; mainly for self-hosted deployments. |
| Remove Vector Store File | `removeVectorStoreFile` | Detach a file from a vector store (DELETE /v1/vector_stores/{id}/files/{file_id}). The underlying file is not deleted. |
| Rerank Documents | `rerankDocuments` | Rerank a list of text documents by relevance to a query using a reranking model such as rerank-v3.5 (POST /v1/rerank). Optionally limit to the top N and include document text in results. |
| Revoke API Key (Admin) | `revokeApiKey` | Revoke a virtual API key immediately across all gateway replicas (DELETE /-/keys/{key_id}). Requires an admin token. |
| Rollback Provider Key Rotation (Admin) | `rollbackProviderKeyRotation` | Abort an in-progress provider key rotation and keep the current key (POST /-/admin/providers/{id}/rotate/rollback). Requires an admin token. |
| Run OCR | `runOcr` | Extract text from a document or image with an OCR-capable model (POST /v1/ocr). Provide the model and a document reference (image or document URL / data URI). |
| Search | `search` | Run a web/search-provider query through the gateway Search API (POST /v1/search). Requires a query and a search_provider configured for your organization (e.g. perplexity); the provider must be allowed on your key. |
| Search Vector Store | `searchVectorStore` | Semantic search over the indexed files of a vector store (POST /v1/vector_stores/{id}/search), outside of an assistant run. |
| Send A2A Message | `sendA2aMessage` | Send an A2A protocol JSON-RPC request (e.g. message/send, tasks/get) to the gateway acting as an A2A agent (POST /a2a). Available only on gateways with A2A enabled. |
| Send MCP Request | `sendMcpRequest` | Send a JSON-RPC 2.0 request to the gateway's MCP server endpoint (POST /mcp), e.g. initialize, tools/list, tools/call, resources/list, prompts/get. The gateway aggregates tools from configured upstream MCP servers. |
| Set Org Config (Admin) | `setOrgConfig` | Set (replace) an organization's gateway configuration (PUT /-/orgs/{org_id}/config): providers, routing, cache, guardrails, rate limits, budget and IP ACL sections. Requires an admin token. |
| Start Provider Key Rotation (Admin) | `startProviderKeyRotation` | Begin rotating a provider's API key: stage a new key alongside the current one (POST /-/admin/providers/{id}/rotate). Requires an admin token. |
| Stream Generate Content (Google) | `streamGenerateContent` | Google GenAI native streaming generation via the gateway (POST /v1beta/models/{model}:streamGenerateContent). Same body as Generate Content; the response is a stream of candidate chunks (returned as raw text when not consumed by a streaming client). |
| Submit Tool Outputs | `submitToolOutputs` | Submit the outputs of the tool calls a run is waiting on (POST /v1/threads/{id}/runs/{run_id}/submit_tool_outputs) so the run can continue. |
| Test MCP Tool (Admin) | `testMcpTool` | Execute a registered MCP tool by name with arguments for testing (POST /-/mcp/test). Requires an admin token. |
| Update API Key (Admin) | `updateApiKey` | Update a virtual API key's name, restrictions, rate limits, expiry or metadata (PUT /-/keys/{key_id}). Requires an admin token. |
| Update Assistant | `updateAssistant` | Modify an assistant's model, name, instructions, tools or metadata (POST /v1/assistants/{id}). |
| Update Run | `updateRun` | Modify a run's metadata (POST /v1/threads/{id}/runs/{run_id}). |
| Update Thread | `updateThread` | Modify a thread's tool resources or metadata (POST /v1/threads/{id}). |
| Update Thread Message | `updateThreadMessage` | Modify a message's metadata (POST /v1/threads/{id}/messages/{msg_id}). |
| Update Vector Store | `updateVectorStore` | Update a vector store's name, expiry policy or metadata (POST /v1/vector_stores/{id}). |
| Upload File | `uploadFile` | Upload a file (POST /v1/files, multipart/form-data) for use with assistants, fine-tuning or batch processing. Max 512 MB; the file is stored on the upstream provider (OpenAI). |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Batch Completed | `batch.completed` | A batch processing job finished. Register in the dashboard: Gateway &gt; Webhooks &gt; + Create Webhook, paste this fastn URL and select 'batch.completed'. Payload modelled from docs. |
| Budget Exceeded | `budget.exceeded` | Spend crossed a configured budget limit for an org or key. Register in the dashboard: Gateway &gt; Webhooks &gt; + Create Webhook, paste this fastn URL and select 'budget.exceeded'. Payload modelled from docs. |
| Error Occurred | `error.occurred` | A gateway-level error occurred (provider failure, timeout, internal error). Register in the dashboard: Gateway &gt; Webhooks &gt; + Create Webhook, paste this fastn URL and select 'error.occurred'. Payload modelled from docs. |
| Guardrail Triggered | `guardrail.triggered` | A guardrail rule fired on a request (pre or post stage). Register in the dashboard: Gateway &gt; Webhooks &gt; + Create Webhook, paste this fastn URL and select 'guardrail.triggered'. Payload modelled from docs. |
| Request Completed | `request.completed` | A gateway request finished (success or error). Registration is UI-only: in the Future AGI dashboard go to Gateway &gt; Webhooks &gt; + Create Webhook, enter this fastn webhook URL, an optional HMAC secret, and tick 'request.completed' under Event Subscriptions. Payload modelled from docs; the top-level 'event' field carries the event type. Signature: X-AgentCC-Signature = 'sha256=' + hex HMAC-SHA256(secret, raw body). |
