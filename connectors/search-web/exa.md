---
description: "Exa AI web search API — neural/keyword/auto search, content extraction, find similar links, LLM answers with citations, and Websets (async agentic search…"
hidden: true
---

# Exa

Exa AI web search API — neural/keyword/auto search, content extraction, find similar links, LLM answers with citations, and Websets (async agentic search collections with webhooks).

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [exa.ai](https://exa.ai) |
| **Authentication** | API key |
| **Actions** | 46 |
| **Events** | 19 |
| **Slug** | `exa` |

## Use it

Add Exa from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.exa.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Answer | `answer` | Get an LLM-generated answer to a natural-language question, grounded in Exa web search with citations. Optionally returns full source text and structured output via outputSchema. |
| Cancel Enrichment | `cancelEnrichment` | Cancel a running Webset enrichment. Requires an Exa Pro plan. |
| Cancel Webset | `cancelWebset` | Cancel a running Webset's operations. Requires an Exa Pro plan. |
| Cancel Webset Search | `cancelWebsetSearch` | Cancel a running search within a Webset. Requires an Exa Pro plan. |
| Create Enrichment | `createEnrichment` | Create an enrichment task on a Webset. Requires a description. Requires an Exa Pro plan. |
| Create Import | `createImport` | Create an import to bring external records (CSV) into Websets. Requires an Exa Pro plan. |
| Create Monitor | `createMonitor` | Create a monitor that re-runs a Webset on a cadence. Requires websetId, cadence, and behavior. Requires an Exa Pro plan. |
| Create Research | `createResearch` | Create an async Exa Agent run. Provide instructions (the research task) and optionally effort and outputSchema. Returns an agent_run_... id; poll Get Research for completion. REPOINTED 2026-09-01: Exa retired the Research API (POST https://api.exa.ai/research/v1 now returns HTTP 410 tag RESEARCH_RETIRED) and replaced it with the Agent API, so this action now calls POST https://api.exa.ai/agent/runs. The slug and the instructions input name are unchanged - instructions is mapped to the Agent API query field by the body template. The old model enum (exa-research-fast/exa-research/exa-research-pro) no longer exists and is replaced by effort. Verified live 2026-09-01: HTTP 200, run completed with a real answer. |
| Create Webhook | `createWebhook` | Register a Websets webhook. Provide a delivery URL and the events to subscribe to. Returns the webhook including a secret (only shown on creation) for signature verification. |
| Create Webset | `createWebset` | Create a Webset — an async agentic search collection. Provide a search object (query, count, entity, criteria) and optional enrichments, externalId, and metadata. Status progresses from pending to idle as items are found. |
| Create Webset Search | `createWebsetSearch` | Add a new search to an existing Webset. Requires query and count. Requires an Exa Pro plan. |
| Delete Enrichment | `deleteEnrichment` | Delete a Webset enrichment by ID. Requires an Exa Pro plan. |
| Delete Import | `deleteImport` | Delete an import by ID. Requires an Exa Pro plan. |
| Delete Monitor | `deleteMonitor` | Delete a monitor by ID. Requires an Exa Pro plan. |
| Delete Webhook | `deleteWebhook` | Delete a Websets webhook by ID. |
| Delete Webset | `deleteWebset` | Delete a Webset by ID. Requires an Exa Pro plan. |
| Delete Webset Item | `deleteWebsetItem` | Delete a single item within a Webset. Requires an Exa Pro plan. |
| Find Similar | `findSimilar` | Find links semantically similar to a given URL. Supports domain/date/text filters, excludeSourceDomain, category, and inline content extraction. |
| Get Contents | `getContents` | Retrieve page contents (text, highlights, summary, extras) for a list of URLs or Exa document IDs. Supports livecrawl freshness via maxAgeHours and subpage crawling. |
| Get Enrichment | `getEnrichment` | Retrieve a Webset enrichment by ID. Requires an Exa Pro plan. |
| Get Event | `getEvent` | Retrieve a Websets event by ID. Requires an Exa Pro plan. |
| Get Import | `getImport` | Retrieve an import by ID. Requires an Exa Pro plan. |
| Get Monitor | `getMonitor` | Retrieve a monitor by ID. Requires an Exa Pro plan. |
| Get Monitor Run | `getMonitorRun` | Retrieve a specific monitor run by ID. Requires an Exa Pro plan. |
| Get Research | `getResearch` | Retrieve an Exa Agent run by id, including status and (when complete) output.text / output.structured. REPOINTED 2026-09-01: Exa retired the Research API (GET https://api.exa.ai/research/v1/{id} now returns HTTP 410 tag RESEARCH_RETIRED) and replaced it with the Agent API, so this action now calls GET https://api.exa.ai/agent/runs/{id}. The slug and the researchId input name are unchanged; pass the agent_run_... id returned by Create Research. The old events query param is gone - the Agent API has no equivalent. Verified live 2026-09-01: HTTP 200 on a real agent_run id. |
| Get Team Info | `getTeamInfo` | Get information about the current Websets team (plan, usage). Requires an Exa Pro plan. |
| Get Webhook | `getWebhook` | Retrieve a single Websets webhook by ID. |
| Get Webset | `getWebset` | Retrieve a Webset by ID, including its status, searches, enrichments, and metadata. |
| Get Webset Item | `getWebsetItem` | Retrieve a single item within a Webset by ID. Requires an Exa Pro plan. |
| Get Webset Search | `getWebsetSearch` | Retrieve a specific search within a Webset. Requires an Exa Pro plan. |
| List Events | `listEvents` | List Websets platform events. Paginate with cursor and limit, filter by types. Requires an Exa Pro plan. |
| List Imports | `listImports` | List imports. Paginate with cursor and limit. Requires an Exa Pro plan. |
| List Monitor Runs | `listMonitorRuns` | List runs for a monitor. Paginate with cursor and limit. Requires an Exa Pro plan. |
| List Monitors | `listMonitors` | List monitors. Paginate with cursor and limit, optionally filter by websetId. Requires an Exa Pro plan. |
| List Research | `listResearch` | List Exa Agent runs (formerly research requests). Paginate with limit and cursor. REPOINTED 2026-09-01: Exa retired the Research API (GET https://api.exa.ai/research/v1 now returns HTTP 410 tag RESEARCH_RETIRED) and replaced it with the Agent API, so this action now calls GET https://api.exa.ai/agent/runs. The slug and inputs are unchanged. Verified live 2026-09-01: HTTP 200 returning the agent_run list. |
| List Webhook Attempts | `listWebhookAttempts` | List delivery attempts for a Websets webhook. Paginate with cursor and limit. Requires an Exa Pro plan. |
| List Webhooks | `listWebhooks` | List registered Websets webhooks. Paginate with cursor and limit. |
| List Webset Items | `listWebsetItems` | List the items found in a Webset, including enrichment results. Paginate with cursor and limit. |
| List Websets | `listWebsets` | List all Websets in the account. Paginate with cursor and limit. |
| Preview Webset | `previewWebset` | Preview the entity and criteria Exa detects for a Webset search before creating it. Requires an Exa Pro plan. |
| Search | `search` | Search the web with Exa. Supports neural/keyword/auto/fast/deep search types, category filters, domain and date filters, and inline content extraction (text, highlights, summary). |
| Update Enrichment | `updateEnrichment` | Update a Webset enrichment's description/format/metadata. Requires an Exa Pro plan. |
| Update Import | `updateImport` | Update an import's title or metadata. Requires an Exa Pro plan. |
| Update Monitor | `updateMonitor` | Update a monitor's status, cadence, behavior, or metadata. Requires an Exa Pro plan. |
| Update Webhook | `updateWebhook` | Update a Websets webhook's url, events, or metadata. Requires an Exa Pro plan. |
| Update Webset | `updateWebset` | Update a Webset's title and/or metadata. Requires an Exa Pro plan. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Import Completed | `import.completed` | An import completed. |
| Import Created | `import.created` | An import was created. |
| Monitor Created | `monitor.created` | A Webset monitor was created. |
| Monitor Deleted | `monitor.deleted` | A Webset monitor was deleted. |
| Monitor Run Completed | `monitor.run.completed` | A scheduled monitor run completed. |
| Monitor Run Created | `monitor.run.created` | A scheduled monitor run started. |
| Monitor Updated | `monitor.updated` | A Webset monitor was updated. |
| Webset Created | `webset.created` | A new Webset was created. |
| Webset Deleted | `webset.deleted` | A Webset was deleted. |
| Webset Export Completed | `webset.export.completed` | A Webset export completed and is ready for download. |
| Webset Export Created | `webset.export.created` | A Webset export was created. |
| Webset Idle | `webset.idle` | A Webset finished processing and is now idle. |
| Webset Item Created | `webset.item.created` | A new item was found and added to a Webset. |
| Webset Item Enriched | `webset.item.enriched` | A Webset item finished enrichment. |
| Webset Paused | `webset.paused` | A Webset was paused. |
| Webset Search Canceled | `webset.search.canceled` | A Webset search was canceled. |
| Webset Search Completed | `webset.search.completed` | A Webset search completed. |
| Webset Search Created | `webset.search.created` | A search within a Webset was created. |
| Webset Search Updated | `webset.search.updated` | A Webset search progress was updated. |
