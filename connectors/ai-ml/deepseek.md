---
description: "DeepSeek AI API connector (OpenAI-compatible)."
---

# DeepSeek

DeepSeek AI API connector (OpenAI-compatible). Chat completions with deepseek-v4-flash / deepseek-v4-pro models (thinking mode, reasoning_content), FIM beta completions, model listing, and account balance. Bearer-token authenticated.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [deepseek.com](https://deepseek.com) |
| **Authentication** | Bearer token |
| **Actions** | 10 |
| **Events** | 0 |
| **Slug** | `deepseek` |

## Use it

Add DeepSeek from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.deepseek.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Chat Completion | `createChatCompletion` | Create a model response for a chat conversation (POST /chat/completions). Models: deepseek-flash, deepseek-v4-pro. Supports thinking mode (thinking.type, reasoning_effort), tool calling, JSON mode and streaming. Docs: https://api-docs.deepseek.com/api/create-chat-completion |
| Create FIM Completion (Beta) | `createCompletion` | Fill-In-the-Middle (FIM) text completion via the beta endpoint. Provide a prompt and optional suffix; the model completes between them. Uses base path /beta. |
| Create Response | `createResponse` | Create a model response with the Responses API (POST /responses). Give input (a string or a list of input items) and/or instructions. Streaming is not supported by this action. Docs: https://api-docs.deepseek.com/api/create-response |
| Delete File | `deleteFile` | Delete a file (DELETE /files/{file_id}). Docs: https://api-docs.deepseek.com/api/delete-file |
| Fetch Web Page | `webFetch` | Fetch a web page and return its title and Markdown content (POST /v1/tools/fetch). Billed per call by DeepSeek. Docs: https://api-docs.deepseek.com/api/fetch |
| Get User Balance | `getUserBalance` | Get the account's available balance(s) and whether it is sufficient for API calls. |
| List Files | `listFiles` | List uploaded files with cursor pagination (GET /files). Docs: https://api-docs.deepseek.com/api/list-files |
| List Models | `listModels` | List the models currently available through the DeepSeek API, with their ownership info. |
| Retrieve File | `retrieveFile` | Get a file's metadata (GET /files/{file_id}). Docs: https://api-docs.deepseek.com/api/retrieve-file |
| Web Search | `webSearch` | Search the web and return ranked results (POST /v1/tools/search). Billed per call by DeepSeek. Docs: https://api-docs.deepseek.com/api/search |
