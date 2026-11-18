---
description: "cloro extracts structured data from AI answer engines and search results - ChatGPT, Google Gemini, Grok, Microsoft Copilot, Perplexity, Google AI Mode, Google…"
hidden: true
---

# cloro

<img src="../../.gitbook/assets/connectors/cloro.png" alt="cloro logo" width="64">

cloro extracts structured data from AI answer engines and search results - ChatGPT, Google Gemini, Grok, Microsoft Copilot, Perplexity, Google AI Mode, Google Search (with AI Overview) and Google News - geo-targeted to any supported country. This connector covers the full cloro v1 API: synchronous monitoring endpoints, Google redirect resolution, asynchronous tasks and batches, queue status and clearing, credit balance, and supported countries and states.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [cloro.dev](https://cloro.dev) |
| **Authentication** | Bearer token |
| **Slug** | `cloro` |

## Use it

Add cloro from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cloro.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Clear Async Queue | `clearAsyncQueue` | Deletes every QUEUED async task for your organization and returns how many were removed. Tasks already processing keep running, completed history is kept, and no credits are charged or refunded. |
| Create Async Task | `createAsyncTask` | Submits a monitoring request as an asynchronous task for background processing and returns its task id and reserved credits. Poll it with Get Async Task or supply a webhook URL to be notified on completion. Async tasks cost the provider's base credits with no synchronous surcharge. |
| Create Batch Async Tasks | `createBatchAsyncTasks` | Submits up to 500 asynchronous monitoring tasks in one request. Each task is validated independently, so one invalid task does not block the rest, and the response lists a per-task success or failure result in the original order. The request body is a JSON array, so the tasks are supplied as a JSON-encoded array string. |
| Get Async Queue Status | `getAsyncQueueStatus` | Returns organization-wide async queue metrics: queued and processing task counts, queued tasks per priority level and current concurrency usage. |
| Get Async Task | `getAsyncTask` | Returns the status of an asynchronous task (QUEUED, PROCESSING, COMPLETED or FAILED), its credit accounting and, once completed, the full structured provider result. |
| Get Credit Balance | `getCreditBalance` | Returns your organization's remaining cloro credits, the credits granted per billing cycle and when the current cycle resets. |
| List Countries | `listCountries` | Returns every ISO 3166-1 alpha-2 country code cloro supports for geo-targeting, optionally filtered to the countries available for one AI provider or search model. |
| List States | `listStates` | Returns the US states supported for state-level geo-targeting on the ChatGPT, Gemini, Grok, Copilot and Perplexity endpoints. Only the United States is supported; other countries return an empty list. |
| Monitor ChatGPT | `monitorChatGpt` | Sends a prompt to ChatGPT from the chosen country and returns the structured answer: response text, cited sources, citation pills, brand entities and map entries, and optionally shopping cards, inline products, ads, query fan-out, Markdown, HTML and the raw response. Costs 5 credits (+2 for any of raw response, fan-out, ads or shopping; +2 for state targeting) plus a 2 credit synchronous surcharge. |
| Monitor Gemini | `monitorGemini` | Sends a prompt to Google Gemini from the chosen country and returns the structured answer text, cited sources, citation pills and place cards, with optional Markdown, HTML and raw response. Costs 4 credits (+2 for state targeting) plus a 2 credit synchronous surcharge. |

<details>

<summary>See 7 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Monitor Google AI Mode | `monitorAiMode` | Sends a prompt to Google AI Mode and returns the structured answer text, sources, citation pills, places, shopping cards, ads, inline products, videos and map data, optionally with expanded merchant product results. Costs 4 credits (+1 per expanded product cluster) plus a 2 credit synchronous surcharge. |
| Monitor Google News | `monitorGoogleNews` | Runs a Google News search and returns structured news articles with titles, links, snippets, sources, dates and thumbnails across up to 10 result pages. Costs 3 credits for page one, +2 per extra page, plus a 2 credit synchronous surcharge. |
| Monitor Google Search | `monitorGoogleSearch` | Runs a Google web search and returns structured results: organic results, People Also Ask, related searches, sponsored ads, shopping cards, local pack, Knowledge Graph and, when requested, the AI Overview. Costs 3 credits for page one, +2 per extra page, +2 for AI Overview, plus a 2 credit synchronous surcharge. |
| Monitor Grok | `monitorGrok` | Sends a prompt to Grok from the chosen country and returns the answer text, cited sources (including X/Twitter references) and query fan-out, with optional Markdown, HTML and raw response. Costs 4 credits (+2 for state targeting) plus a 2 credit synchronous surcharge. cloro currently lists Grok as temporarily unavailable, so calls fail with a 500 until the provider is restored. |
| Monitor Microsoft Copilot | `monitorCopilot` | Sends a prompt to Microsoft Copilot from the chosen country and returns the structured answer text, cited sources, citation pills, shopping cards, map entries and query fan-out, with optional Markdown, HTML and raw response. Costs 5 credits (+2 for state targeting) plus a 2 credit synchronous surcharge. |
| Monitor Perplexity | `monitorPerplexity` | Sends a prompt to Perplexity from the chosen country and returns the structured answer text, cited sources, citation pills, related queries, videos, images, hotels, places and shopping cards, with optional Markdown, HTML and raw response. Costs 4 credits (+2 for state targeting) plus a 2 credit synchronous surcharge. |
| Resolve Google Redirect Link | `resolveGoogleRedirectLink` | Resolves a Google /goto or /url redirect link (as returned in the redirectLink fields of Google Search, Google News and AI Mode results) to its final destination URL. |

</details>
