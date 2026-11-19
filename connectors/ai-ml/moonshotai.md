---
description: "Moonshot AI Kimi API (kimi-k2, kimi-latest, moonshot-v1) — OpenAI-compatible LLM platform."
hidden: true
---

# Moonshot AI (Kimi)

<img src="../../.gitbook/assets/connectors/lg/moonshotai.png" alt="Moonshot AI (Kimi) logo">

Chat completions, models, files (extract/QA), context caching, token estimation, and account balance. Base URL https://api.moonshot.ai/v1. Bearer API key auth.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [moonshot.ai](https://moonshot.ai) |
| **Authentication** | Bearer token |
| **Slug** | `moonshotai` |

## Use it

Add Moonshot AI (Kimi) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.moonshotai.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Cancel Batch</td><td><code>cancelBatch</code></td><td>Cancel Batch. Cancel an in-progress batch task. The status will change to cancelling and then to cancelled. Only tasks in validating, in_progress, or finalizing status can be cancelled.</td></tr><tr><td>Check Balance</td><td><code>checkBalance</code></td><td>Check Balance. REST API to check your available, voucher, and cash balances on Kimi OpenPlatform.</td></tr><tr><td>Create a model response</td><td><code>createResponse</code></td><td>Create a model response. Creates a model response. Provide text or image inputs to generate text or JSON outputs. Have the model call the function tools you define. When `stream` is `true`, the response is delivered as a stream of SSE events.</td></tr><tr><td>Create Batch</td><td><code>createBatch</code></td><td>Create Batch. Create a batch task. You need to first upload a JSONL file with purpose="batch" via the Files API, then use the returned file_id to create the task.</td></tr><tr><td>Create Chat Completion</td><td><code>createChatCompletion</code></td><td>Create Chat Completion. Creates a completion for the chat message. Supports standard chat, Partial Mode, and Tool Use (Function Calling).</td></tr><tr><td>Delete File</td><td><code>deleteFile</code></td><td>Delete File. Deletes a previously uploaded file.</td></tr><tr><td>Estimate Token Count</td><td><code>estimateTokenCount</code></td><td>Estimate Token Count. Estimates the number of tokens that would be used for a given set of messages and model. The input structure is almost identical to that of chat completion.</td></tr><tr><td>List Batches</td><td><code>listBatches</code></td><td>List Batches. List batch tasks for your organization.</td></tr><tr><td>List Files</td><td><code>listFiles</code></td><td>List Files. Lists all files uploaded by the current user.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>List Models. List all currently available models.</td></tr></tbody></table>

<details>

<summary>View 9 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Messages API</td><td><code>createAnthropicMessage</code></td><td>Messages API. Call Kimi models with an Anthropic Messages API compatible format, supporting streaming, tool use, image input, thinking, and structured output.</td></tr><tr><td>Retrieve Batch</td><td><code>getBatch</code></td><td>Retrieve Batch. Retrieve the status and details of a specific batch task.</td></tr><tr><td>Retrieve File</td><td><code>retrieveFile</code></td><td>Get File Information. Retrieves metadata for a specific uploaded file.</td></tr><tr><td>Retrieve File Content</td><td><code>retrieveFileContent</code></td><td>Get File Content. Retrieves the extracted content for files uploaded with purpose `file-extract`, returned as Markdown-formatted text.</td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td>Upload a text file (POST /v1/files, multipart) for file-extract or batch. Docs: https://platform.kimi.ai/docs</td></tr><tr><td>URL Fetch</td><td><code>webFetch</code></td><td>URL Fetch. Fetch the content of a URL and get the page title and body text in Markdown (text and images concatenated in order). Only http and https URLs are supported. You are charged once per successful call that extracts content; failed or empty-content calls are free. See [WebSearch Pricing](/pricing/tools).</td></tr><tr><td>Verify Request Signature</td><td><code>verifySignature</code></td><td>Verify Request Signature. Verifies a request signature returned in the response headers of the Chat Completions, Responses, or Messages API, proving that the request was handled by the Kimi API for the specified model rather than routed elsewhere. Submit the nonce used in the call, the timestamp from the response headers, the request's model, and the signature; the endpoint returns `valid: true` when the signature matches these three attributes exactly, and `valid: false` otherwise.</td></tr><tr><td>Web Search Basic</td><td><code>webSearch</code></td><td>Web Search Basic. Run a web search and get structured results with title, snippet, site, and URL. You are charged once per successful call that returns at least one result; failed or empty-result calls are free. See [WebSearch Pricing](/pricing/tools).</td></tr><tr><td>Web Search Pro</td><td><code>webSearchPro</code></td><td>Web Search Pro. Web Search Basic with site and time-range constraints, plus structured content chunks (`chunks`) for each result. You are charged once per successful call that returns at least one result; failed or empty-result calls are free. See [WebSearch Pricing](/pricing/tools).</td></tr></tbody></table>

</details>
