---
description: "OpenRouter unified LLM API (https://openrouter.ai/api/v1) — OpenAI-compatible access to hundreds of models from many providers behind one API."
hidden: true
---

# OpenRouter

<img src="../../.gitbook/assets/connectors/lg/openrouter.png" alt="OpenRouter logo">

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

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Chat Completion</td><td><code>createChatCompletion</code></td><td>POST /api/v1/chat/completions — OpenAI-compatible chat completion. Send a messages array and a model id; returns the assistant message, finish_reason, and token usage. For zero-cost validation use a FREE model id (':free' suffix), e.g. meta-llama/llama-3.2-3b-instruct:free. Set stream=false for a single JSON response.</td></tr><tr><td>Create Completion</td><td><code>createCompletion</code></td><td>POST /api/v1/completions — legacy OpenAI-compatible text completion. Send a single 'prompt' string and a model id; returns generated text. Use a FREE model (':free' suffix) for zero-cost validation.</td></tr><tr><td>Get API Key Info</td><td><code>getKey</code></td><td>GET /api/v1/key — return metadata about the current API key: label, usage (all-time + daily/weekly/monthly), spend limit and remaining limit, and free-tier flag.</td></tr><tr><td>Get Credits</td><td><code>getCredits</code></td><td>GET /api/v1/credits — return total purchased credits and total usage for the account tied to the API key.</td></tr><tr><td>Get Generation Stats</td><td><code>getGeneration</code></td><td>GET /api/v1/generation?id= — fetch request and usage metadata for a completed generation: total_cost, token counts (native + normalized), latency, generation_time, provider, and finish reason. Pass the 'id' returned by a chat/text completion.</td></tr><tr><td>List Model Endpoints</td><td><code>listModelEndpoints</code></td><td>GET /api/v1/models/{author}/{slug}/endpoints — list every provider endpoint serving a given model, with per-provider pricing, context_length, quantization, max_completion_tokens, supported_parameters, and status.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>GET /api/v1/models — list all models available on OpenRouter with pricing, context_length, architecture, and supported parameters. Free models have a ':free' suffix in their id. Optional filters narrow the catalog.</td></tr></tbody></table>
