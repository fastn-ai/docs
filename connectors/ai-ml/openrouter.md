---
description: "OpenRouter unified LLM API (https://openrouter.ai/api/v1) — OpenAI-compatible access to hundreds of models from many providers behind one API."
hidden: true
---

# OpenRouter

<img src="../../.gitbook/assets/connectors/openrouter.png" alt="OpenRouter logo" width="64">

OpenRouter unified LLM API (https://openrouter.ai/api/v1) — OpenAI-compatible access to hundreds of models from many providers behind one API. Covers chat completions, legacy text completions, model catalog (with pricing/context_length/supported params), per-model provider endpoints, generation cost/token stats, account credits, and current API key info. Bearer API key auth. Free models use the ':free' suffix (e.g. meta-llama/llama-3.2-3b-instruct:free) for zero-cost validation.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [openrouter.ai](https://openrouter.ai) |
| **Authentication** | Bearer token |
| **Slug** | `openrouter` |

## Use it

Add OpenRouter from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openrouter.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Chat Completion | `createChatCompletion` | POST /api/v1/chat/completions — OpenAI-compatible chat completion. Send a messages array and a model id; returns the assistant message, finish_reason, and token usage. For zero-cost validation use a FREE model id (':free' suffix), e.g. meta-llama/llama-3.2-3b-instruct:free. Set stream=false for a single JSON response. |
| Create Completion | `createCompletion` | POST /api/v1/completions — legacy OpenAI-compatible text completion. Send a single 'prompt' string and a model id; returns generated text. Use a FREE model (':free' suffix) for zero-cost validation. |
| Get API Key Info | `getKey` | GET /api/v1/key — return metadata about the current API key: label, usage (all-time + daily/weekly/monthly), spend limit and remaining limit, and free-tier flag. |
| Get Credits | `getCredits` | GET /api/v1/credits — return total purchased credits and total usage for the account tied to the API key. |
| Get Generation Stats | `getGeneration` | GET /api/v1/generation?id= — fetch request and usage metadata for a completed generation: total_cost, token counts (native + normalized), latency, generation_time, provider, and finish reason. Pass the 'id' returned by a chat/text completion. |
| List Model Endpoints | `listModelEndpoints` | GET /api/v1/models/{author}/{slug}/endpoints — list every provider endpoint serving a given model, with per-provider pricing, context_length, quantization, max_completion_tokens, supported_parameters, and status. |
| List Models | `listModels` | GET /api/v1/models — list all models available on OpenRouter with pricing, context_length, architecture, and supported parameters. Free models have a ':free' suffix in their id. Optional filters narrow the catalog. |
