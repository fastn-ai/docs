---
description: "Moonshot AI Kimi API (kimi-k2, kimi-latest, moonshot-v1) — OpenAI-compatible LLM platform."
hidden: true
---

# Moonshot AI (Kimi)

Moonshot AI Kimi API (kimi-k2, kimi-latest, moonshot-v1) — OpenAI-compatible LLM platform. Chat completions, models, files (extract/QA), context caching, token estimation, and account balance. Base URL https://api.moonshot.ai/v1. Bearer API key auth.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [moonshot.ai](https://moonshot.ai) |
| **Authentication** | Bearer token |
| **Actions** | 19 |
| **Events** | 0 |
| **Slug** | `moonshotai` |

## Use it

Add Moonshot AI (Kimi) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.moonshotai.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Batch | `cancelBatch` | Cancel Batch. Cancel an in-progress batch task. The status will change to cancelling and then to cancelled. Only tasks in validating, in_progress, or finalizing status can be cancelled. |
| Check Balance | `checkBalance` | Check Balance. REST API to check your available, voucher, and cash balances on Kimi OpenPlatform. |
| Create a model response | `createResponse` | Create a model response. Creates a model response. Provide text or image inputs to generate text or JSON outputs. Have the model call the function tools you define. When `stream` is `true`, the response is delivered as a stream of SSE events. |
| Create Batch | `createBatch` | Create Batch. Create a batch task. You need to first upload a JSONL file with purpose="batch" via the Files API, then use the returned file_id to create the task. |
| Create Chat Completion | `createChatCompletion` | Create Chat Completion. Creates a completion for the chat message. Supports standard chat, Partial Mode, and Tool Use (Function Calling). |
| Delete File | `deleteFile` | Delete File. Deletes a previously uploaded file. |
| Estimate Token Count | `estimateTokenCount` | Estimate Token Count. Estimates the number of tokens that would be used for a given set of messages and model. The input structure is almost identical to that of chat completion. |
| List Batches | `listBatches` | List Batches. List batch tasks for your organization. |
| List Files | `listFiles` | List Files. Lists all files uploaded by the current user. |
| List Models | `listModels` | List Models. List all currently available models. |
| Messages API | `createAnthropicMessage` | Messages API. Call Kimi models with an Anthropic Messages API compatible format, supporting streaming, tool use, image input, thinking, and structured output. |
| Retrieve Batch | `getBatch` | Retrieve Batch. Retrieve the status and details of a specific batch task. |
| Retrieve File | `retrieveFile` | Get File Information. Retrieves metadata for a specific uploaded file. |
| Retrieve File Content | `retrieveFileContent` | Get File Content. Retrieves the extracted content for files uploaded with purpose `file-extract`, returned as Markdown-formatted text. |
| Upload File | `uploadFile` | Upload a text file (POST /v1/files, multipart) for file-extract or batch. Docs: https://platform.kimi.ai/docs |
| URL Fetch | `webFetch` | URL Fetch. Fetch the content of a URL and get the page title and body text in Markdown (text and images concatenated in order). Only http and https URLs are supported. You are charged once per successful call that extracts content; failed or empty-content calls are free. See [WebSearch Pricing](/pricing/tools). |
| Verify Request Signature | `verifySignature` | Verify Request Signature. Verifies a request signature returned in the response headers of the Chat Completions, Responses, or Messages API, proving that the request was handled by the Kimi API for the specified model rather than routed elsewhere. Submit the nonce used in the call, the timestamp from the response headers, the request's model, and the signature; the endpoint returns `valid: true` when the signature matches these three attributes exactly, and `valid: false` otherwise. |
| Web Search Basic | `webSearch` | Web Search Basic. Run a web search and get structured results with title, snippet, site, and URL. You are charged once per successful call that returns at least one result; failed or empty-result calls are free. See [WebSearch Pricing](/pricing/tools). |
| Web Search Pro | `webSearchPro` | Web Search Pro. Web Search Basic with site and time-range constraints, plus structured content chunks (`chunks`) for each result. You are charged once per successful call that returns at least one result; failed or empty-result calls are free. See [WebSearch Pricing](/pricing/tools). |
