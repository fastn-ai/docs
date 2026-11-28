---
description: "Clay is a data platform for finding and enriching companies and people. Run searches, query tables and workflow runs, and check credits."
hidden: true
---

# Clay

<img src="../../.gitbook/assets/connectors/lg/clay.png" alt="Clay logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [clay.com](https://clay.com) |
| **Authentication** | API key |
| **Slug** | `clay` |

## Setup

Your customers enter their API key for Clay when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Clay from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Clay**.
2. Select **Connect** on the Clay card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Clay's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Batch Upload URL</td><td><code>createBatchUploadUrl</code></td><td>Creates a presigned PUT URL and file id for uploading a JSONL input file for a batch routine run. Upload the file to upload_url, then call Start Batch Routine Run with the file id.</td></tr><tr><td>Create Filters Search</td><td><code>createFiltersSearch</code></td><td>Deprecated by Clay in favor of Create Query Search. Starts a new Clay search from a source type and structured filter fields (see List Search Filter Fields); page results with Run Filters Search.</td></tr><tr><td>Create Query Search</td><td><code>createQuerySearch</code></td><td>Starts a new Clay search of the people or company database from a Clay advanced search query. The source type is detected from the query and returned with the search id; page through results with Run Query Search. Count-mode and jobs queries are not supported.</td></tr><tr><td>Get Authenticated User</td><td><code>getAuthenticatedUser</code></td><td>Returns the Clay user and workspace associated with the API key. Used to verify the connection.</td></tr><tr><td>Get Batch Routine Run Results</td><td><code>getBatchRoutineRunResults</code></td><td>Returns the status of a batch routine run: in_progress with progress counts, complete with a result file URL, or validation_failed / processing_failed with error details.</td></tr><tr><td>Get Credit Balance</td><td><code>getCreditBalance</code></td><td>Returns the current data credit and action balances for the workspace associated with the API key. Reading balances does not consume credits.</td></tr><tr><td>Get Routine Run Results</td><td><code>getRoutineRunResults</code></td><td>Returns the status and paginated per-item results of an inline routine run.</td></tr><tr><td>Get Search Query Reference</td><td><code>getSearchQueryReference</code></td><td>Returns the Clay advanced search query reference as markdown, covering the queryable people and company fields and the query grammar. Use it to author a query before creating a query-mode search.</td></tr><tr><td>Get Workflow Run Query Reference</td><td><code>getWorkflowRunQueryReference</code></td><td>Returns the Clay workflow-run query reference (beta) as markdown, covering queryable run fields, node predicates, content search and the query grammar.</td></tr><tr><td>List Search Filter Fields</td><td><code>listSearchFilterFields</code></td><td>Deprecated by Clay in favor of query-mode search. Returns every filter field accepted by Create Filters Search for a source type, with type, description, allowed values and usage guidance.</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Query Tables</td><td><code>queryTables</code></td><td>Runs a structured query across one to five known Clay tables (Enterprise plans) with selected fields or aggregates, filters, joins, grouping and ordering, returning records with per-cell status and field metadata. Page with the returned cursor; custom-ordered, grouped or aggregated queries do not paginate.</td></tr><tr><td>Query Workflow Runs</td><td><code>queryWorkflowRuns</code></td><td>Executes a Clay workflow-run query (beta). A select query returns matching runs newest first with a cursor; a count query returns the number of matching runs. Results come from an eventually-consistent replica. See Get Workflow Run Query Reference for the grammar.</td></tr><tr><td>Run Filters Search</td><td><code>runFiltersSearch</code></td><td>Deprecated by Clay; remains available to page searches created in filters mode. Returns the next page of records for an existing filters-mode search; call again while has_more is true.</td></tr><tr><td>Run Query Search</td><td><code>runQuerySearch</code></td><td>Returns the next page of people or company records for an existing query-mode search. The search is a stateful iterator: call again while has_more is true. Results count against the workspace search result limits for its plan.</td></tr><tr><td>Run Routine</td><td><code>runRoutine</code></td><td>Starts an asynchronous run of a Clay-managed or custom function routine against 1 to 100 input items and returns the routine run id. Fetch results with Get Routine Run Results, or pass a registered webhook id to be notified when the run finishes. Runs consume Clay credits.</td></tr><tr><td>Start Batch Routine Run</td><td><code>startBatchRoutineRun</code></td><td>Starts an asynchronous batch routine run over a previously uploaded JSONL file and returns the routine run id. Fetch progress with Get Batch Routine Run Results. Runs consume Clay credits.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Routine Run Finished</td><td><code>routine_run.finished</code></td><td>Clay POSTs this payload when a routine run is ready to read. Clay has no webhook registration API: register the webhook with the Clay CLI, `clay webhooks create &lt;this trigger URL&gt;` (store the whsec signing secret it returns once), then pass the returned webhook id as webhook_id on the Run Routine or Start Batch Routine Run action. The payload carries no event-type field and no run results - read data.routine_run_id and call Get Routine Run Results or Get Batch Routine Run Results. Clay signs the raw body with the webhook signing secret and sends it as X-Clay-Signature: sha256=&lt;hex HMAC-SHA256&gt;; this per-webhook secret cannot be configured in the platform's verification block today, so verify downstream. Delivery is not guaranteed - keep polling the run as a fallback. Docs: https://developers.clay.com/public-api/webhooks</td></tr></tbody></table>
