---
description: "OpenRouter is a gateway to hundreds of AI models. Create chat completions, list models and providers, and check credits and usage stats."
hidden: true
---

# OpenRouter

<img src="../../.gitbook/assets/connectors/lg/openrouter.png" alt="OpenRouter logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [openrouter.ai](https://openrouter.ai) |
| **Authentication** | Access token |
| **Slug** | `openrouter` |

## Setup

Your customers enter their access token for OpenRouter when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect OpenRouter from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **OpenRouter**.
2. Select **Connect** on the OpenRouter card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use OpenRouter's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Chat Completion</td><td><code>createChatCompletion</code></td><td>OpenAI-compatible chat completion. Send a messages array and a model id; returns the assistant message, finish_reason, and token usage. For zero-cost validation use a FREE model id (':free' suffix), e.g. meta-llama/llama-3.2-3b-instruct:free. Set stream=false for a single JSON response.</td></tr><tr><td>Create Completion</td><td><code>createCompletion</code></td><td>legacy OpenAI-compatible text completion. Send a single 'prompt' string and a model id; returns generated text. Use a FREE model (':free' suffix) for zero-cost validation.</td></tr><tr><td>Get API Key Info</td><td><code>getKey</code></td><td>return metadata about the current API key: label, usage (all-time + daily/weekly/monthly), spend limit and remaining limit, and free-tier flag.</td></tr><tr><td>Get Credits</td><td><code>getCredits</code></td><td>return total purchased credits and total usage for the account tied to the API key.</td></tr><tr><td>Get Generation Stats</td><td><code>getGeneration</code></td><td>fetch request and usage metadata for a completed generation: total_cost, token counts (native + normalized), latency, generation_time, provider, and finish reason. Pass the 'id' returned by a chat/text completion.</td></tr><tr><td>List Model Endpoints</td><td><code>listModelEndpoints</code></td><td>list every provider endpoint serving a given model, with per-provider pricing, context_length, quantization, max_completion_tokens, supported_parameters, and status.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>list all models available on OpenRouter with pricing, context_length, architecture, and supported parameters. Free models have a ':free' suffix in their id. Optional filters narrow the catalog.</td></tr></tbody></table>

