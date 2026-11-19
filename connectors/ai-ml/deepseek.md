---
description: "DeepSeek AI API connector (OpenAI-compatible)."
hidden: true
---

# DeepSeek

<img src="../../.gitbook/assets/connectors/lg/deepseek.png" alt="DeepSeek logo">

Chat completions with deepseek-v4-flash / deepseek-v4-pro models (thinking mode, reasoning_content), FIM beta completions, model listing, and account balance. Bearer-token authenticated.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [deepseek.com](https://deepseek.com) |
| **Authentication** | Bearer token |
| **Slug** | `deepseek` |

## Use it

Add DeepSeek from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.deepseek.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Chat Completion</td><td><code>createChatCompletion</code></td><td>Create a model response for a chat conversation (POST /chat/completions). Models: deepseek-flash, deepseek-v4-pro. Supports thinking mode (thinking.type, reasoning_effort), tool calling, JSON mode and streaming. Docs: https://api-docs.deepseek.com/api/create-chat-completion</td></tr><tr><td>Create FIM Completion (Beta)</td><td><code>createCompletion</code></td><td>Fill-In-the-Middle (FIM) text completion via the beta endpoint. Provide a prompt and optional suffix; the model completes between them. Uses base path /beta.</td></tr><tr><td>Create Response</td><td><code>createResponse</code></td><td>Create a model response with the Responses API (POST /responses). Give input (a string or a list of input items) and/or instructions. Streaming is not supported by this action. Docs: https://api-docs.deepseek.com/api/create-response</td></tr><tr><td>Delete File</td><td><code>deleteFile</code></td><td>Delete a file (DELETE /files/{file_id}). Docs: https://api-docs.deepseek.com/api/delete-file</td></tr><tr><td>Fetch Web Page</td><td><code>webFetch</code></td><td>Fetch a web page and return its title and Markdown content (POST /v1/tools/fetch). Billed per call by DeepSeek. Docs: https://api-docs.deepseek.com/api/fetch</td></tr><tr><td>Get User Balance</td><td><code>getUserBalance</code></td><td>Get the account's available balance(s) and whether it is sufficient for API calls.</td></tr><tr><td>List Files</td><td><code>listFiles</code></td><td>List uploaded files with cursor pagination (GET /files). Docs: https://api-docs.deepseek.com/api/list-files</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>List the models currently available through the DeepSeek API, with their ownership info.</td></tr><tr><td>Retrieve File</td><td><code>retrieveFile</code></td><td>Get a file's metadata (GET /files/{file_id}). Docs: https://api-docs.deepseek.com/api/retrieve-file</td></tr><tr><td>Web Search</td><td><code>webSearch</code></td><td>Search the web and return ranked results (POST /v1/tools/search). Billed per call by DeepSeek. Docs: https://api-docs.deepseek.com/api/search</td></tr></tbody></table>
