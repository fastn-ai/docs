---
description: "Parallel web research APIs on api.parallel.ai: Search and Extract, Task runs and Task Groups (deep research and enrichment), Responses (OpenAI-compatible),…"
---

# Parallel

Parallel web research APIs on api.parallel.ai: Search and Extract, Task runs and Task Groups (deep research and enrichment), Responses (OpenAI-compatible), Chat Completions, FindAll entity discovery and Entity Search, Monitors for continuous web change tracking, and Memory. Authenticates with an API key sent as x-api-key.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Authentication** | API key |
| **Actions** | 35 |
| **Events** | 10 |
| **Slug** | `parallel` |

## Use it

Add Parallel from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.parallel.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Task Group Runs | `addTaskGroupRuns` | Starts up to 1,000 task runs inside a Task Group, each with its own input and processor and an optional shared default task spec. Returns the new run ids and stream cursors. |
| Cancel FindAll Run | `cancelFindAllRun` | Stops a FindAll run early to control costs. Results gathered so far remain retrievable. |
| Cancel Monitor | `cancelMonitor` | Cancels a monitor so it stops future executions. Returns the monitor with status cancelled. |
| Clear Memory | `clearMemory` | Clears every entry from the selected memory scope without deleting the underlying tasks, monitors or FindAll runs. Omit memory_scope_key to clear personal memory. |
| Create Chat Completion | `createChatCompletion` | OpenAI-compatible chat completion grounded in live web research (beta). Returns the assistant message plus a basis with citations. Non-streaming; set stream false. Sampling parameters are accepted but unsupported. |
| Create FindAll Run | `createFindAllRun` | Starts an asynchronous FindAll run that discovers and verifies entities matching the objective and match conditions. Use generator preview for a cheap sample; base, core and pro are billed per run plus per match, with match_limit 5 to 1000. Optional webhook receives findall run and candidate events. |
| Create Monitor | `createMonitor` | Creates a monitor that continuously watches the web: type event_stream tracks a natural-language query for new material changes, type snapshot watches a task run's output for changes. Runs once immediately, then on the frequency (1h to 30d). Optional webhook receives monitor.event.detected, monitor.execution.completed and monitor.execution.failed. $3 to $10 per 1,000 checks. |
| Create Response | `createResponse` | Answers a question with live web research using the OpenAI-compatible Responses API. Model is always parallel; reasoning.effort low, medium or high selects the research depth. Supports structured output via text.format and multi-turn via previous_response_id. $10 to $250 per 1,000 requests by tier. |
| Create Task Group | `createTaskGroup` | Creates a Task Group to batch and track many task runs, with optional metadata. |
| Create Task Run | `createTaskRun` | Starts an asynchronous web-research task run with a processor (lite, base, core, pro, ultra and their -fast variants), an input and an optional task spec, webhook and metadata. Returns 202 with the run id; poll Get Task Run Result. Billed per successful run by processor ($5 per 1,000 for lite). |
| Enrich FindAll Run | `enrichFindAllRun` | Adds an enrichment (a JSON output schema evaluated per matched candidate by a Task processor) to an existing FindAll run. Enrichments are billed per candidate at the processor's Task rate. |
| Entity Search | `entitySearch` | Fast synchronous search for people or companies matching a natural-language objective, returning a ranked entity set. $5 per 1,000 requests including 100 results. |
| Evict From Memory | `evictMemory` | Removes one task run, monitor or FindAll run from the selected memory without deleting the original resource. |
| Extend FindAll Run | `extendFindAllRun` | Raises the match limit of an existing FindAll run by the given number of additional matches so it keeps searching without changing the query. |
| Extract | `extract` | Extracts clean, LLM-optimized content and excerpts from up to 20 public URLs, optionally focused by an objective and search queries. Synchronous; $1 per 1,000 URLs. |
| Get FindAll Run | `getFindAllRun` | Retrieves the status and candidate metrics of a FindAll run. |
| Get FindAll Run Events | `getFindAllRunEvents` | Streams FindAll run and candidate events as server-sent events. The stream stays open while the run is active; pass a short timeout (seconds) to get a bounded response, and last_event_id to resume. |
| Get FindAll Run Result | `getFindAllRunResult` | Retrieves the FindAll run result at the time of the request: the run status plus every evaluated candidate with match status, conditions and enrichments. |
| Get FindAll Run Schema | `getFindAllRunSchema` | Retrieves the spec of a FindAll run: objective, entity type, match conditions, enrichments, generator and match limit. |
| Get Monitor | `getMonitor` | Retrieves a monitor by id including its settings, webhook, metadata and (for snapshot monitors) current output. |
| Get Task Group | `getTaskGroup` | Retrieves aggregated status across all runs in a Task Group. |
| Get Task Group Events | `getTaskGroupEvents` | Streams Task Group status updates and run completions as server-sent events. The stream stays open while runs are active; pass a short timeout (seconds) to get a bounded response. |
| Get Task Group Run | `getTaskGroupRun` | Retrieves the status of one run inside a Task Group. |
| Get Task Run | `getTaskRun` | Retrieves the status of a task run by run id. |
| Get Task Run Events | `getTaskRunEvents` | Streams progress events for a task run as server-sent events (requires enable_events on the run). The stream stays open while the run is active (up to 570 seconds) and closes with a final task_run.state event once the run is non-active, so call it on a completed run to get a bounded response. |
| Get Task Run Input | `getTaskRunInput` | Retrieves the original input, task spec and settings of a task run by run id. |
| Get Task Run Result | `getTaskRunResult` | Retrieves the result of a task run, blocking until the run completes or the timeout elapses. Returns the run object plus the output with its research basis. |
| Ingest FindAll Objective | `ingestFindAllObjective` | Transforms a natural-language search objective into a structured FindAll spec (entity type, match conditions, generator, match limit) that can be passed to Create FindAll Run. |
| List Monitor Events | `listMonitorEvents` | Lists a monitor's events newest first (event_stream, snapshot, completion, error), optionally for one execution via event_group_id, with cursor paging. Pass include_completions to include no-change runs. |
| List Monitors | `listMonitors` | Lists monitors newest first, optionally filtered by type and status, with cursor paging. |
| List Task Group Runs | `listTaskGroupRuns` | Returns a snapshot of the runs in a Task Group as a server-sent event stream (one task_run.state event per run, then the stream closes), optionally including each run's input and output and filtered by status. Resume with last_event_id. |
| Retrieve Memory | `retrieveMemory` | Retrieves relevant or recent past task, monitor and FindAll runs from the selected memory. Provide a query to rank by relevance; leave it empty for the most recent runs. |
| Search | `search` | Searches the web with natural-language objective and keyword queries and returns LLM-optimized page excerpts ranked by relevance. Synchronous; $1 to $5 per 1,000 requests depending on mode. |
| Trigger Monitor Run | `triggerMonitorRun` | Triggers an immediate execution of a monitor outside its schedule. Counts as one check. |
| Update Monitor | `updateMonitor` | Updates a monitor's frequency, processor, webhook, metadata or (event_stream only, with type set) settings such as the query. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| FindAll Candidate Enriched | `findall.candidate.enriched` | Enrichment data was extracted for a FindAll candidate. Delivered per run via the webhook on Create FindAll Run. Payload shape from docs. |
| FindAll Candidate Generated | `findall.candidate.generated` | A new FindAll candidate was generated and queued for evaluation. Delivered per run via the webhook on Create FindAll Run. Payload shape from docs. |
| FindAll Candidate Matched | `findall.candidate.matched` | A FindAll candidate matched all match conditions. Delivered per run via the webhook on Create FindAll Run. Payload shape from docs (data carries output and basis). |
| FindAll Run Cancelled | `findall.run.cancelled` | A FindAll run was cancelled. Delivered per run via the webhook on Create FindAll Run. Payload captured from a real delivery. |
| FindAll Run Completed | `findall.run.completed` | A FindAll run reached completed. Delivered per run: pass this trigger's webhook URL on Create FindAll Run with event_types [findall.run.completed]. Payload shape from docs.parallel.ai/findall-api/features/findall-webhook (same shape as the captured findall.run.cancelled delivery). |
| FindAll Run Failed | `findall.run.failed` | A FindAll run failed. Delivered per run via the webhook on Create FindAll Run. Payload shape from docs. |
| Monitor Event Detected | `monitor.event.detected` | A monitor run detected one or more material events. Subscribing creates a Parallel event_stream monitor from the monitorQuery, monitorFrequency and monitorProcessor inputs; fetch the events with List Monitor Events using data.event.event_group_id. Payload shape from docs.parallel.ai/monitor-api/monitor-webhooks; delivery headers webhook-id, webhook-timestamp, webhook-signature (Standard Webhooks HMAC-SHA256 over id.timestamp.body with the base64-decoded whsec_ account secret; not verifiable by the platform's header HMAC options, so verification is off). |
| Monitor Execution Completed | `monitor.execution.completed` | A monitor run completed with no new detections. Subscribing creates a Parallel event_stream monitor. Payload shape from docs.parallel.ai/monitor-api/monitor-webhooks. |
| Monitor Execution Failed | `monitor.execution.failed` | A monitor run failed due to an error. Subscribing creates a Parallel event_stream monitor. Payload shape from docs.parallel.ai/monitor-api/monitor-webhooks. |
| Task Run Status | `task_run.status` | A task run completed (success or failure). Delivered per run: pass this trigger's webhook URL as webhook.url with event_types [task_run.status] on Create Task Run or Add Task Group Runs; subscribing here does not register anything. Payload captured from a real delivery (data is the full Task Run object). |
