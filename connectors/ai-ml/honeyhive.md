---
description: "HoneyHive is an AI observability and evaluation platform for tracing, evaluating and monitoring LLM applications and agents."
hidden: true
---

# HoneyHive

<img src="../../.gitbook/assets/connectors/lg/honeyhive.png" alt="HoneyHive logo">

HoneyHive is an AI observability and evaluation platform for tracing, evaluating and monitoring LLM applications and agents. This connector covers the HoneyHive Data Plane API: sessions and trace events, event search, datasets and datapoints, evaluators (metrics) and metric versions, experiment runs with summaries and comparisons, annotation queues, charts and configurations.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [honeyhive.ai](https://honeyhive.ai) |
| **Authentication** | Credentials you enter |
| **Slug** | `honeyhive` |

## Use it

Add HoneyHive from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.honeyhive.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Datapoints To Dataset | `addDatapointsToDataset` | Creates new datapoints from raw data objects and adds them to a dataset, using a field mapping that says which keys of each object become inputs, history and ground truth. Returns the new datapoint IDs. |
| Add Events To Session | `addEventsToSession` | Adds a batch of trace events to an existing session. The session_id in the URL overrides any session_id inside the events. Each event needs event_type and inputs; unknown fields are rejected. |
| Compare Experiment Run Events | `compareRunEvents` | Retrieves paired events from two experiment runs, matched by datapoint, for detailed side-by-side comparison. Filter by event name or type and paginate. |
| Compare Experiment Runs | `compareRuns` | Compares the aggregated metrics and results of a new experiment run against an old one, returning per-metric differences, common datapoints and event details. |
| Create Annotation Queue | `createQueue` | Creates an annotation queue with a name, optional description, event filters, enabled flag and an initial set of event IDs to review. |
| Create Chart | `createChart` | Creates a saved chart that aggregates a metric over time with a bucketing granularity, an optional aggregation function, group-by field, date range and query filters. |
| Create Configuration | `createConfiguration` | Creates an LLM or pipeline configuration with its provider, model call parameters, environments and tags. HoneyHive marks the configurations endpoints as deprecated in its OpenAPI spec; they remain functional. Returns the inserted configuration ID. |
| Create Datapoint | `createDatapoint` | Creates a single datapoint with inputs, conversation history, ground truth and metadata, optionally linked to a source event and to datasets. Returns the inserted datapoint ID. |
| Create Datapoints From Events | `createDatapointsBatch` | Creates datapoints from existing trace events, using a field mapping of dotted event paths (e.g. inputs.chat_history, outputs.content) that become datapoint inputs, history and ground truth. List the event IDs in events and mark each selected one true in checkState (events without a checkState entry are skipped), or select by filters/dateRange with selectAll; optionally add the new datapoints to a dataset. |
| Create Dataset | `createDataset` | Creates a dataset with an optional name, description and initial list of datapoint IDs. Returns the inserted dataset ID. |
| Create Event | `createEvent` | Creates a single trace event (span) of type model, tool, chain or session, with its inputs and optional outputs, configuration, timing, metadata, feedback and metrics. The server generates event_id, session_id and parent_id when omitted. Events cannot be deleted through the API. |
| Create Events Batch | `createEventsBatch` | Creates multiple trace events in one request. Each event needs event_type and inputs. Set single_session to true to put all events into one new session described by session_properties. Returns the created event IDs and session ID. |
| Create Experiment Run | `createRun` | Creates an experiment (evaluation) run to track an evaluation against a dataset, with a name, status, configuration, metadata, results and the linked event, session and datapoint IDs. Returns the run. |
| Create Metric | `createMetric` | Creates an evaluator (metric) in the project: a Python evaluator, an LLM-judged evaluator or a human feedback field, with its criteria, return type, production sampling settings and optional event filters. For PYTHON evaluators the criteria is a script that assigns the score to a variable named result (inputs, outputs and metadata are available as globals). A float return type requires scale. Returns the new metric ID. |
| Create Metric Version | `createMetricVersion` | Snapshots a metric definition as a new version of an evaluator, with a commit-style message. The version is created as a draft unless deploy_immediately is true, in which case it also becomes the live version. |
| Delete Annotation Queue | `deleteQueue` | Soft-deletes an annotation queue by ID. |
| Delete Chart | `deleteChart` | Deletes a saved chart by ID. |
| Delete Configuration | `deleteConfiguration` | Permanently deletes a configuration by ID. HoneyHive marks the configurations endpoints as deprecated in its OpenAPI spec; they remain functional. |
| Delete Datapoint | `deleteDatapoint` | Permanently deletes a datapoint by ID. |
| Delete Dataset | `deleteDataset` | Permanently deletes a dataset by ID (its datapoints are not deleted). |
| Delete Experiment Run | `deleteRun` | Permanently deletes an experiment run by run ID. |
| Delete Metric | `deleteMetric` | Deletes an evaluator (metric) by ID. |
| Deploy Metric Version | `deployMetricVersion` | Marks a named version of an evaluator as the live version, un-deploying any previously deployed version. |
| Get Annotation Queue | `getQueue` | Retrieves a single annotation queue by ID. |
| Get Chart | `getChart` | Retrieves a single saved chart by ID. |
| Get Datapoint | `getDatapoint` | Retrieves a single datapoint by ID. The API returns it inside a one-element datapoint array. |
| Get Event | `getEvent` | Retrieves a single trace event by its ID. |
| Get Experiment Run | `getRun` | Retrieves the full details of a single experiment run by run ID. |
| Get Experiment Run Metrics | `getRunMetrics` | Returns the per-event metric values recorded for an experiment run, optionally limited by a date range and filters. |
| Get Experiment Run Schema | `getRunSchema` | Returns the events schema (fields, datasets and field mappings) for a single experiment run, optionally limited to a date range. |
| Get Experiment Run Summary | `getRunSummary` | Computes the evaluation summary of an experiment run: pass/fail results, aggregated metrics, per-datapoint results, event details and the run object. Choose the aggregation function and optional filters. |
| Get Project Runs Schema | `getRunsSchema` | Returns the aggregated events schema (fields, datasets and field mappings) across all experiment runs in the project, optionally limited to a date range. |
| List Annotation Queues | `listQueues` | Lists the project's annotation queues. Set enabled to true to return only enabled queues; omit it to return all queues. (HoneyHive treats any enabled value, including false, as true, so disabled-only filtering is not available via the API.) |
| List Charts | `listCharts` | Lists all saved charts (metric visualizations) in the project. |
| List Configurations | `listConfigurations` | Lists the project's LLM and pipeline configurations, optionally filtered by name, environment or tags. HoneyHive marks the configurations endpoints as deprecated in its OpenAPI spec; they remain functional. |
| List Datapoints | `listDatapoints` | Lists datapoints in the project, optionally restricted to one datapoint ID or to the datapoints of a named dataset. (The API's multi-ID filter uses repeated datapoint_ids query keys, which cannot be expressed here; pass one ID at a time or use Get Datapoint.) |
| List Datasets | `listDatasets` | Lists the project's datasets, optionally filtered by dataset ID or name. Each dataset carries the IDs of its datapoints. |
| List Experiment Runs | `listRuns` | Lists experiment runs with optional filtering by dataset, status, name, date range or a specific run ID, with pagination and sorting. (The API's multi-ID filter uses repeated run_ids query keys, which cannot be expressed here; pass one run ID at a time.) |
| List Metric Versions | `listMetricVersions` | Lists all snapshot versions of an evaluator's definition, oldest first, including which version is currently deployed. |
| List Metrics | `listMetrics` | Lists the evaluators (metrics) defined in the project, optionally filtered by metric type or a specific metric ID. |
| Remove Datapoint From Dataset | `removeDatapointFromDataset` | Removes a datapoint from a dataset without deleting the datapoint itself. |
| Run Metric | `runMetric` | Executes an evaluator definition (LLM or PYTHON) against a single ad-hoc event and returns the computed result and explanation, without storing anything. LLM evaluators use the workspace's configured model provider credentials. |
| Search Events | `searchEvents` | Searches the project's trace events with field filters, a date range, pagination and an optional experiment run ID. Results are ordered by start time descending. This is the primary way to retrieve events. |
| Start Session | `startSession` | Starts a new trace session in the project and returns the created session event. Every field is optional; the server generates a session_id when omitted. Sessions and events cannot be deleted through the API. |
| Update Annotation Queue | `updateQueue` | Updates an annotation queue's name, description, filters or enabled status, and adds or removes events from it. Only the fields you pass are modified. |
| Update Chart | `updateChart` | Updates a saved chart's editable fields (name, description, metric, aggregation, group-by, bucketing, date range, query filters, owner). Only the fields you pass are modified. |
| Update Configuration | `updateConfiguration` | Updates a configuration's name, provider, parameters, environments, tags or user properties. HoneyHive marks the configurations endpoints as deprecated in its OpenAPI spec; they remain functional. |
| Update Datapoint | `updateDatapoint` | Updates a datapoint's inputs, history, ground truth, metadata, linked event or linked datasets. Only the fields you pass are modified. |
| Update Dataset | `updateDataset` | Updates a dataset's name, description or list of datapoint IDs. Only the fields you pass are modified. |
| Update Event | `updateEvent` | Updates an existing trace event: merges metadata, feedback, metrics, config and user properties, replaces outputs, and sets duration, end time or child event IDs. Only the fields you pass are modified. |
| Update Experiment Run | `updateRun` | Updates an experiment run's name, description, status, metadata, results, configuration, linked IDs, evaluators or passing ranges. Only the fields you pass are modified. |
| Update Metric | `updateMetric` | Updates an evaluator (metric) by ID. Only the fields you pass are modified. |
