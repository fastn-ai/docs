---
description: "DeepSeek provides AI language models. Create chat and code completions, search and fetch web pages, manage files and check your balance."
hidden: true
---

# DeepSeek

<img src="../../.gitbook/assets/connectors/lg/deepseek.png" alt="DeepSeek logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [deepseek.com](https://deepseek.com) |
| **Authentication** | Access token |
| **Slug** | `deepseek` |

## Setup

Your customers enter their access token for DeepSeek when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect DeepSeek from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **DeepSeek**.
2. Select **Connect** on the DeepSeek card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use DeepSeek's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Chat Completion</td><td><code>createChatCompletion</code></td><td>Create a model response for a chat conversation Models: deepseek-flash, deepseek-v4-pro. Supports thinking mode (thinking.type, reasoning_effort), tool calling, JSON mode and streaming. Docs: https://api-docs.deepseek.com/api/create-chat-completion</td></tr><tr><td>Create FIM Completion (Beta)</td><td><code>createCompletion</code></td><td>Fill-In-the-Middle (FIM) text completion via the beta endpoint. Provide a prompt and optional suffix; the model completes between them. Uses base path /beta.</td></tr><tr><td>Create Response</td><td><code>createResponse</code></td><td>Create a model response with the Responses API Give input (a string or a list of input items) and/or instructions. Streaming is not supported by this action. Docs: https://api-docs.deepseek.com/api/create-response</td></tr><tr><td>Delete File</td><td><code>deleteFile</code></td><td>Delete a file Docs: https://api-docs.deepseek.com/api/delete-file</td></tr><tr><td>Fetch Web Page</td><td><code>webFetch</code></td><td>Fetch a web page and return its title and Markdown content Billed per call by DeepSeek. Docs: https://api-docs.deepseek.com/api/fetch</td></tr><tr><td>Get User Balance</td><td><code>getUserBalance</code></td><td>Get the account's available balance(s) and whether it is sufficient for API calls.</td></tr><tr><td>List Files</td><td><code>listFiles</code></td><td>List uploaded files with cursor pagination Docs: https://api-docs.deepseek.com/api/list-files</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>List the models currently available through the DeepSeek API, with their ownership info.</td></tr><tr><td>Retrieve File</td><td><code>retrieveFile</code></td><td>Get a file's metadata Docs: https://api-docs.deepseek.com/api/retrieve-file</td></tr><tr><td>Web Search</td><td><code>webSearch</code></td><td>Search the web and return ranked results Billed per call by DeepSeek. Docs: https://api-docs.deepseek.com/api/search</td></tr></tbody></table>

