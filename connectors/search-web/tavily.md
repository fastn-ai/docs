---
description: "Tavily web search, extract, crawl, and map API for AI agents."
hidden: true
---

# Tavily

<img src="../../.gitbook/assets/connectors/lg/tavily.png" alt="Tavily logo">

Tavily web search, extract, crawl, and map API for AI agents. Real-time web search optimized for LLMs, content extraction from URLs, site crawling, and URL mapping. Base URL https://api.tavily.com.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [tavily.com](https://tavily.com) |
| **Authentication** | Bearer token |
| **Slug** | `tavily` |

## Use it

Add Tavily from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.tavily.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Crawl | `crawl` | Crawl a website starting from a root URL and extract content from discovered pages (beta). Returns extracted content per crawled URL. Cost scales with pages crawled; instructions and advanced extract_depth increase credit cost. |
| Extract | `extract` | Extract cleaned page content from one or more URLs (max 20). extract_depth 'basic' = 1 credit per 5 URLs; 'advanced' = 2 credits per 5 URLs and pulls tables/embedded content. Returns raw_content per URL plus any failed URLs. |
| Get Usage | `getUsage` | Get credit usage for the API key and account (no credit cost). Returns per-key and account-level usage, plan limits, pay-as-you-go allocation, and per-endpoint breakdown. |
| Map | `map` | Map a website's URL structure starting from a root URL (beta). Returns a list of discovered URLs without extracting page content. Cheaper than crawl; instructions raise cost to 2 credits per 10 pages. |
| Search | `search` | Execute a real-time web search optimized for LLMs/AI agents. Use search_depth 'basic' (1 credit) for credit-safe runs; 'advanced' (2 credits) for deeper retrieval. Returns ranked results, an optional LLM answer, and optional images. |
