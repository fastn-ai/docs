---
description: "ImageRouter is a gateway to AI image, video and text models. Generate and edit images, generate videos and chat replies, and check credits."
hidden: true
---

# ImageRouter

<img src="../../.gitbook/assets/connectors/lg/image-router.png" alt="ImageRouter logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [imagerouter.io](https://imagerouter.io) |
| **Authentication** | Access token |
| **Slug** | `imageRouter` |

## Setup

Your customers enter their access token for ImageRouter when they connect. Nothing else needs setting up.

## Use it

Add ImageRouter from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.imageRouter.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create API Key</td><td><code>createApiKey</code></td><td>Creates a new normal API key for the account, optionally with a spend cap, a spend-limit reset period and an expiry. This endpoint accepts only a management API key (generated in the ImageRouter API keys dashboard), so the connection used must be a management key; normal keys receive a 401. The generated key value is returned once and never shown again.</td></tr><tr><td>Create Chat Completion</td><td><code>createChatCompletion</code></td><td>Sends a conversation to a text (LLM) model through ImageRouter's OpenAI-compatible chat/completions endpoint and returns the model's reply. Requests are proxied to LLMGateway and billed at true cost from your credit balance. Only non-streaming responses are supported. When the balance is too low the API returns an insufficient-credits error.</td></tr><tr><td>Create Response</td><td><code>createResponse</code></td><td>Generates a model response from a text input through ImageRouter's OpenAI-compatible responses endpoint. Requests are proxied to LLMGateway and billed at true cost from your credit balance. Only non-streaming responses are supported. When the balance is too low the API returns an insufficient-credits error.</td></tr><tr><td>Edit Image</td><td><code>editImage</code></td><td>Runs the unified images/edits endpoint, which shares its handler with Generate Image and accepts the same JSON parameters (prompt, model, quality, size, response format, output format). Returns the resulting image URL or base64 data, latency and cost in USD. Image-to-image and inpainting require uploading source image and mask files as multipart/form-data, which this connector cannot send; use this action for text-to-image only. When the account balance is too low the API answers HTTP 200 with an error object, so check the error field.</td></tr><tr><td>Generate Image</td><td><code>generateImage</code></td><td>Generates one image from a text prompt with any ImageRouter image model (OpenAI-compatible images/generations endpoint). Returns the generated image as a hosted URL or base64 data, plus latency and the cost charged in USD. Use List Models to discover model ids; models ending in ":free" and the "test/test" dummy model cost nothing. Note: when the account balance is too low the API answers HTTP 200 with an error object instead of image data, so check the error field.</td></tr><tr><td>Generate Video</td><td><code>generateVideo</code></td><td>Generates a video from a text prompt with any ImageRouter video model (OpenAI-compatible videos/generations endpoint). Returns the generated video as a hosted URL or base64 data, plus latency and the cost charged in USD. Use List Models with type "video" to discover model ids; the "ir/test-video" dummy model costs nothing. Image-to-video requires a multipart file upload, which this connector cannot send. When the account balance is too low the API answers HTTP 200 with an error object, so check the error field.</td></tr><tr><td>Get Credits</td><td><code>getCredits</code></td><td>Returns the account's remaining credit balance, total credit usage and total deposits in USD. Optionally includes a per-API-key breakdown of usage, request counts, spend limits and expiry.</td></tr><tr><td>Get Model</td><td><code>getModel</code></td><td>Retrieves a single model by its full id (for example "google/gemini-2.5-flash" or "test/test"), returning its providers and pricing, release date, supported inputs (text, image, mask, quality, allowed sizes or seconds) and output types.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>Lists the models available on ImageRouter as an object keyed by model id (e.g. "openai/gpt-image-1"), with providers and pricing, release date, output types and supported parameters. Supports filtering by output type, provider, free tier and name, plus sorting and limiting. No authentication is required for this catalog.</td></tr><tr><td>List Models V2</td><td><code>listModelsV2</code></td><td>Lists the models available on ImageRouter using the v2 catalog format: a JSON array of model objects, each with its id, provider prefix, release date, output types, supported inputs (including allowed sizes) and an aggregated price range (min, average, max USD) across providers. Filter by provider, free tier or name, and sort or limit the result. To restrict by output type (image or video) use List Models, which supports the type filter. No authentication is required for this catalog.</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Test API Key</td><td><code>testApiKey</code></td><td>Verifies that the connected ImageRouter API key is valid and active. Returns a success flag and the account's remaining credit balance in internal units (1/10000 USD). Useful as a connection health check.</td></tr></tbody></table>

</details>

## Events

ImageRouter has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
