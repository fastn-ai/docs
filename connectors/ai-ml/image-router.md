---
description: "ImageRouter is a unified, OpenAI-compatible API for AI image, video and text generation across dozens of providers (FLUX, Gemini, Imagen, GPT Image, Ideogram,…"
---

# ImageRouter

ImageRouter is a unified, OpenAI-compatible API for AI image, video and text generation across dozens of providers (FLUX, Gemini, Imagen, GPT Image, Ideogram, Qwen, Seedream, Midjourney and more) behind one API key. This connector covers the complete ImageRouter API at https://api.imagerouter.io: image generation and editing, video generation, chat completions and responses for text models, the model catalog (v1 and v2 listings plus single-model lookup), credit balance and per-key usage, API key validation, and management-key API key creation.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [imagerouter.io](https://imagerouter.io) |
| **Authentication** | Bearer token |
| **Actions** | 11 |
| **Events** | 0 |
| **Slug** | `imageRouter` |

## Use it

Add ImageRouter from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.imageRouter.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create API Key | `createApiKey` | Creates a new normal API key for the account, optionally with a spend cap, a spend-limit reset period and an expiry. This endpoint accepts only a management API key (generated in the ImageRouter API keys dashboard), so the connection used must be a management key; normal keys receive a 401. The generated key value is returned once and never shown again. |
| Create Chat Completion | `createChatCompletion` | Sends a conversation to a text (LLM) model through ImageRouter's OpenAI-compatible chat/completions endpoint and returns the model's reply. Requests are proxied to LLMGateway and billed at true cost from your credit balance. Only non-streaming responses are supported. When the balance is too low the API returns an insufficient-credits error. |
| Create Response | `createResponse` | Generates a model response from a text input through ImageRouter's OpenAI-compatible responses endpoint. Requests are proxied to LLMGateway and billed at true cost from your credit balance. Only non-streaming responses are supported. When the balance is too low the API returns an insufficient-credits error. |
| Edit Image | `editImage` | Runs the unified images/edits endpoint, which shares its handler with Generate Image and accepts the same JSON parameters (prompt, model, quality, size, response format, output format). Returns the resulting image URL or base64 data, latency and cost in USD. Image-to-image and inpainting require uploading source image and mask files as multipart/form-data, which this connector cannot send; use this action for text-to-image only. When the account balance is too low the API answers HTTP 200 with an error object, so check the error field. |
| Generate Image | `generateImage` | Generates one image from a text prompt with any ImageRouter image model (OpenAI-compatible images/generations endpoint). Returns the generated image as a hosted URL or base64 data, plus latency and the cost charged in USD. Use List Models to discover model ids; models ending in ":free" and the "test/test" dummy model cost nothing. Note: when the account balance is too low the API answers HTTP 200 with an error object instead of image data, so check the error field. |
| Generate Video | `generateVideo` | Generates a video from a text prompt with any ImageRouter video model (OpenAI-compatible videos/generations endpoint). Returns the generated video as a hosted URL or base64 data, plus latency and the cost charged in USD. Use List Models with type "video" to discover model ids; the "ir/test-video" dummy model costs nothing. Image-to-video requires a multipart file upload, which this connector cannot send. When the account balance is too low the API answers HTTP 200 with an error object, so check the error field. |
| Get Credits | `getCredits` | Returns the account's remaining credit balance, total credit usage and total deposits in USD. Optionally includes a per-API-key breakdown of usage, request counts, spend limits and expiry. |
| Get Model | `getModel` | Retrieves a single model by its full id (for example "google/gemini-2.5-flash" or "test/test"), returning its providers and pricing, release date, supported inputs (text, image, mask, quality, allowed sizes or seconds) and output types. Returns a 404 with code model_not_found when the id is unknown. |
| List Models | `listModels` | Lists the models available on ImageRouter as an object keyed by model id (e.g. "openai/gpt-image-1"), with providers and pricing, release date, output types and supported parameters. Supports filtering by output type, provider, free tier and name, plus sorting and limiting. No authentication is required for this catalog. |
| List Models V2 | `listModelsV2` | Lists the models available on ImageRouter using the v2 catalog format: a JSON array of model objects, each with its id, provider prefix, release date, output types, supported inputs (including allowed sizes) and an aggregated price range (min, average, max USD) across providers. Filter by provider, free tier or name, and sort or limit the result. To restrict by output type (image or video) use List Models, which supports the type filter. No authentication is required for this catalog. |
| Test API Key | `testApiKey` | Verifies that the connected ImageRouter API key is valid and active. Returns a success flag and the account's remaining credit balance in internal units (1/10000 USD). Useful as a connection health check. |
