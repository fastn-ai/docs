---
description: "You.com API — real-time web intelligence for AI apps."
hidden: true
---

# You.com

<img src="../../.gitbook/assets/connectors/youcom.png" alt="You.com logo" width="64">

You.com API — real-time web intelligence for AI apps. Search API (GET https://ydc-index.io/v1/search) returns LLM-optimized web + news results with optional livecrawl full-page content; Contents API (POST https://ydc-index.io/v1/contents) fetches full page HTML/markdown/metadata for given URLs; Research API (POST https://api.you.com/v1/research) is a deep-search agent returning a grounded answer with sources and optional structured (JSON-schema) output. Auth via X-API-Key header.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [you.com](https://you.com) |
| **Authentication** | API key |
| **Slug** | `youcom` |

## Use it

Add You.com from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.youcom.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Contents | `getContents` | Contents API — POST https://ydc-index.io/v1/contents. Fetches full page content for a list of URLs as HTML, markdown, and/or metadata. Useful after a Search to retrieve full article text. |
| Research | `research` | Research API — POST https://api.you.com/v1/research. Deep-search agent that returns a grounded answer with cited sources for a research question. research_effort controls depth/cost (lite/standard/deep/exhaustive). source_control filters domains/freshness/country; output_schema returns structured JSON (requires standard+). This is the MOST EXPENSIVE endpoint — avoid for casual validation. |
| Search | `search` | Search API — GET https://ydc-index.io/v1/search. Returns LLM-optimized web and news results for a query. Supports freshness, country/language, safesearch, domain include/exclude/boost, and optional livecrawl to fetch full-page HTML/markdown. CHEAPEST endpoint ($5/1000 calls) — use this (count=1, no livecrawl) for credit-safe validation. |
