---
description: "Clay is a GTM data platform for finding, enriching and acting on companies and people."
hidden: true
---

# Clay

Clay is a GTM data platform for finding, enriching and acting on companies and people. This connector wraps the Clay Public API v0: advanced query-mode search of Clay's people and company database (with the query reference and result paging), legacy filters-mode search, running Clay-managed and custom function routines inline or as JSONL batches and fetching their results, structured queries across Clay tables (Enterprise), Clay workflow-run queries, workspace credit balances and the authenticated user. Routine runs can notify a Clay webhook when they finish. Authenticates with a Clay API key sent in the clay-api-key header.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [clay.com](https://clay.com) |
| **Authentication** | API key |
| **Actions** | 16 |
| **Events** | 1 |
| **Slug** | `clay` |

## Use it

Add Clay from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.clay.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Batch Upload URL | `createBatchUploadUrl` | Creates a presigned PUT URL and file id for uploading a JSONL input file for a batch routine run. Upload the file to upload_url, then call Start Batch Routine Run with the file id. |
| Create Filters Search | `createFiltersSearch` | Deprecated by Clay in favor of Create Query Search. Starts a new Clay search from a source type and structured filter fields (see List Search Filter Fields); page results with Run Filters Search. |
| Create Query Search | `createQuerySearch` | Starts a new Clay search of the people or company database from a Clay advanced search query. The source type is detected from the query and returned with the search id; page through results with Run Query Search. Count-mode and jobs queries are not supported. |
| Get Authenticated User | `getAuthenticatedUser` | Returns the Clay user and workspace associated with the API key. Used to verify the connection. |
| Get Batch Routine Run Results | `getBatchRoutineRunResults` | Returns the status of a batch routine run: in_progress with progress counts, complete with a result file URL, or validation_failed / processing_failed with error details. |
| Get Credit Balance | `getCreditBalance` | Returns the current data credit and action balances for the workspace associated with the API key. Reading balances does not consume credits. |
| Get Routine Run Results | `getRoutineRunResults` | Returns the status and paginated per-item results of an inline routine run. Answers 202 with status in_progress while running and 200 with status complete and data once finished; page with cursor. |
| Get Search Query Reference | `getSearchQueryReference` | Returns the Clay advanced search query reference as markdown, covering the queryable people and company fields and the query grammar. Use it to author a query before creating a query-mode search. |
| Get Workflow Run Query Reference | `getWorkflowRunQueryReference` | Returns the Clay workflow-run query reference (beta) as markdown, covering queryable run fields, node predicates, content search and the query grammar. |
| List Search Filter Fields | `listSearchFilterFields` | Deprecated by Clay in favor of query-mode search. Returns every filter field accepted by Create Filters Search for a source type, with type, description, allowed values and usage guidance. |
| Query Tables | `queryTables` | Runs a structured query across one to five known Clay tables (Enterprise plans) with selected fields or aggregates, filters, joins, grouping and ordering, returning records with per-cell status and field metadata. Page with the returned cursor; custom-ordered, grouped or aggregated queries do not paginate. |
| Query Workflow Runs | `queryWorkflowRuns` | Executes a Clay workflow-run query (beta). A select query returns matching runs newest first with a cursor; a count query returns the number of matching runs. Results come from an eventually-consistent replica. See Get Workflow Run Query Reference for the grammar. |
| Run Filters Search | `runFiltersSearch` | Deprecated by Clay; remains available to page searches created in filters mode. Returns the next page of records for an existing filters-mode search; call again while has_more is true. |
| Run Query Search | `runQuerySearch` | Returns the next page of people or company records for an existing query-mode search. The search is a stateful iterator: call again while has_more is true. Results count against the workspace search result limits for its plan. |
| Run Routine | `runRoutine` | Starts an asynchronous run of a Clay-managed or custom function routine against 1 to 100 input items and returns the routine run id. Fetch results with Get Routine Run Results, or pass a registered webhook id to be notified when the run finishes. Runs consume Clay credits. |
| Start Batch Routine Run | `startBatchRoutineRun` | Starts an asynchronous batch routine run over a previously uploaded JSONL file and returns the routine run id. Fetch progress with Get Batch Routine Run Results. Runs consume Clay credits. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Routine Run Finished | `routine_run.finished` | Clay POSTs this payload when a routine run is ready to read. Clay has no webhook registration API: register the webhook with the Clay CLI, `clay webhooks create &lt;this trigger URL&gt;` (store the whsec signing secret it returns once), then pass the returned webhook id as webhook_id on the Run Routine or Start Batch Routine Run action. The payload carries no event-type field and no run results - read data.routine_run_id and call Get Routine Run Results or Get Batch Routine Run Results. Clay signs the raw body with the webhook signing secret and sends it as X-Clay-Signature: sha256=&lt;hex HMAC-SHA256&gt;; this per-webhook secret cannot be configured in the platform's verification block today, so verify downstream. Delivery is not guaranteed - keep polling the run as a fallback. Docs: https://developers.clay.com/public-api/webhooks |
