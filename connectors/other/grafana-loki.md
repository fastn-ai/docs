---
description: "Grafana Loki log aggregation over the Loki HTTP API."
hidden: true
---

# Grafana Loki

<img src="../../.gitbook/assets/connectors/lg/grafana-loki.png" alt="Grafana Loki logo">

Grafana Loki log aggregation over the Loki HTTP API. Push log lines with stream labels and structured metadata, query them back with LogQL (range, instant, legacy and OTLP ingest), read labels, label values, series, detected fields and labels, index stats, volume and shards, manage log deletion requests, and manage Ruler alerting/recording rule groups. Works against self-hosted Loki and Grafana Cloud Logs. Auth is HTTP Basic: for self-hosted, the reverse-proxy username and password; for Grafana Cloud, the numeric instance/user ID as username and an access policy token (logs:write / logs:read) as password.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [grafana.net](https://grafana.net) |
| **Authentication** | Credentials you enter |
| **Slug** | `grafanaLoki` |

## Use it

Add Grafana Loki from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.grafanaLoki.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Delete Request | `cancelDeleteRequest` | Cancels a pending log deletion request by id. Only works while the request is still within the compactor's delete_request_cancel_period and has not started processing; set force=true to cancel a partially processed request. Returns 204 with an empty body. DELETE /loki/api/v1/delete. |
| Create Delete Request | `createDeleteRequest` | Submits a request to delete log entries matching a LogQL selector within a time range. DESTRUCTIVE: once the compactor's cancel period elapses the matching lines are permanently removed. The request can be cancelled with Cancel Delete Request while it is still in status "received". Returns 204 with an empty body. POST /loki/api/v1/delete. |
| Create Or Update Rule Group | `createOrUpdateRuleGroup` | Creates a rule group in a Ruler namespace, or replaces it if the group name already exists. The body is YAML, not JSON - pass the group definition verbatim, e.g. "name: my-group\ninterval: 1m\nrules:\n - alert: HighErrorRate\n expr: sum(rate({job=\"my-app\"} \|= \"error\" [5m])) &gt; 10\n for: 5m\n labels:\n severity: critical\n annotations:\n summary: too many errors". Returns 202 with an empty body. POST /loki/api/v1/rules/{namespace}. |
| Delete Rule Group | `deleteRuleGroup` | Deletes one rule group from a Ruler namespace. Returns 202 with an empty body. DELETE /loki/api/v1/rules/{namespace}/{groupName}. |
| Delete Rule Namespace | `deleteRuleNamespace` | Deletes every rule group in a Ruler namespace. Returns 202 with an empty body. DELETE /loki/api/v1/rules/{namespace}. |
| Format LogQL Query | `formatQuery` | Parses and pretty-prints a LogQL expression, returning the canonical form. Also serves as a syntax check: an invalid expression comes back as 400 with status "invalid-query" and the parse error. GET /loki/api/v1/format_query. |
| Get Build Info | `getBuildInfo` | Returns the Loki build information - version, revision, branch and build date. Cheap, unprivileged call, ideal as a connection health check. GET /loki/api/v1/status/buildinfo. |
| Get Cache Generation Numbers | `getCacheGenerationNumbers` | Returns the tenant's current query-result cache generation number, which Loki bumps whenever a delete request invalidates cached results. The response is a bare JSON string (empty string when no deletion has invalidated the cache), not an object. GET /loki/api/v1/cache/generation_numbers. |
| Get Compactor Ring | `getCompactorRing` | Returns the compactor hash ring status, showing which instance owns compaction and retention. Operational endpoint; the response is an HTML page, not JSON. GET /compactor/ring. |
| Get Detected Fields | `getDetectedFields` | Inspects the log lines matching a selector and returns the structured fields Loki can parse out of them, with type, cardinality, the parsers required and the JSON path. GET /loki/api/v1/detected_fields. |

<details>

<summary>See 29 more actions</summary>

* **Get Detected Labels** `getDetectedLabels`: Returns the stream labels present in the time range together with their cardinality, so a UI can rank labels by usefulness. GET /loki/api/v1/detected_labels.
* **Get Distributor Ring** `getDistributorRing`: Returns the distributor hash ring status - member instances, their state, tokens, zone and last heartbeat. Operational endpoint; the response is an HTML page, not JSON. GET /distributor/ring.
* **Get Index Shards** `getIndexShards`: Returns the shard boundaries Loki would use to split a query, with per-shard stream, chunk, byte and entry statistics. Used to plan parallel query execution. GET /loki/api/v1/index/shards.
* **Get Index Stats** `getIndexStats`: Returns index statistics - stream, chunk, byte and entry counts - for the streams matching a selector over a time range. Useful for sizing a query before running it. GET /loki/api/v1/index/stats.
* **Get Index Volume** `getIndexVolume`: Returns ingested log volume per label set as an instant vector for the matching streams over a time range. GET /loki/api/v1/index/volume.
* **Get Index Volume Range** `getIndexVolumeRange`: Returns ingested log volume per label set as a time series (matrix) bucketed by step over a time range. GET /loki/api/v1/index/volume_range.
* **Get Log Patterns** `getPatterns`: Returns automatically detected log line patterns and their per-bucket counts for the matching streams. Requires the pattern ingester to be enabled on the Loki deployment (pattern_ingester.enabled: true); when it is off Loki answers 404 with an empty body even though the route exists. GET /loki/api/v1/patterns.
* **Get Rule Group** `getRuleGroup`: Returns one rule group's definition (name, interval, rules) as YAML. GET /loki/api/v1/rules/{namespace}/{groupName}.
* **Get Rule Groups By Namespace** `getRuleGroupsByNamespace`: Returns the rule groups in one Ruler namespace, as YAML. 404 with "no rule groups found" means the namespace holds no rules. GET /loki/api/v1/rules/{namespace}.
* **Get Ruler Ring** `getRulerRing`: Returns the ruler hash ring status, showing which instances evaluate rule groups. Operational endpoint; the response is an HTML page, not JSON. GET /ruler/ring.
* **Get Runtime Config** `getConfig`: Returns the Loki server's effective configuration as YAML text (not JSON). Leave mode empty for the effective config, or use defaults for the stock configuration. KNOWN VENDOR BUG: mode=diff returns HTTP 500 "unsupported type &lt;nil&gt;" on Loki 3.6.7 - reproduced with plain curl outside this connector, so it is a Loki defect, not a wiring problem. GET /config.
* **Legacy List Label Names** `legacyListLabels`: DEPRECATED Loki v0 label-names endpoint. Returns {"values": [...]} instead of the v1 {"status","data"} envelope. Prefer List Label Names. GET /api/prom/label.
* **Legacy List Label Values** `legacyListLabelValues`: DEPRECATED Loki v0 label-values endpoint, returning {"values": [...]}. Prefer List Label Values. GET /api/prom/label/{name}/values.
* **Legacy List Series** `legacyListSeries`: DEPRECATED Loki v0 series endpoint. Returns the label sets of matching streams. Sends the selector as the plain match parameter, which Loki accepts alongside the documented repeated form match[]. Prefer List Series. GET /api/prom/series.
* **Legacy Push Logs** `legacyPushLogs`: DEPRECATED Loki v0 ingest endpoint. Streams use the old shape: labels is a formatted selector STRING and entries is a list of {ts, line} objects, e.g. [{"labels":"{job=\"my-app\"}","entries":[{"ts":"2026-09-18T13:00:00Z","line":"hello"}]}]. Prefer Push Log Streams. Returns 204 with an empty body. POST /api/prom/push.
* **Legacy Query** `legacyQuery`: DEPRECATED Loki v0 query endpoint, kept for compatibility with old clients. Returns a "streams" array whose labels are a single formatted string rather than an object. Prefer Query Range. GET /api/prom/query.
* **List Active Alerts** `listPrometheusAlerts`: Returns the alerts currently firing or pending in the Loki Ruler, in Prometheus API format. GET /prometheus/api/v1/alerts.
* **List Delete Requests** `listDeleteRequests`: Lists the tenant's log deletion requests with their status (received, processed, cancelled), selector and time range. Requires the compactor's delete API (deletion_mode filter-and-delete or filter-only). GET /loki/api/v1/delete.
* **List Detected Field Values** `listDetectedFieldValues`: Returns the observed values of one detected (parsed) field in the matching log lines. GET /loki/api/v1/detected_field/{name}/values.
* **List Label Names** `listLabels`: Returns the list of stream label names known to Loki within the given time range. GET /loki/api/v1/labels.
* **List Label Values** `listLabelValues`: Returns every value seen for one stream label within the time range. GET /loki/api/v1/label/{name}/values.
* **List Prometheus Rules** `listPrometheusRules`: Returns the Ruler's loaded rule groups with each rule's current evaluation state, health and last error, in Prometheus API format. Unlike List Rule Groups this returns 200 with an empty groups array when nothing is configured. GET /prometheus/api/v1/rules.
* **List Rule Groups** `listRuleGroups`: Returns every Loki Ruler namespace with its alerting and recording rule groups, as YAML. Loki answers 404 with the plain-text body "no rule groups found" when the tenant has no rules configured - that is an empty state, not an error. GET /loki/api/v1/rules.
* **List Series** `listSeries`: Returns the full label set of every log stream matching a selector in the time range. Loki documents the parameter as the repeated form match[] but also accepts the plain name match, which is what this action sends so that exactly one selector parameter goes on the wire. GET /loki/api/v1/series.
* **Push Log Entry** `pushLogEntry`: Pushes a single log line to Loki with two stream labels (a custom label plus service_name) and three flat structured-metadata fields (Order, error, detected_level). timestampNs must be a nanosecond epoch string - seconds followed by nine zeroes is fine. Loki requires structured metadata to be a FLAT object, which is why only these three metadata fields are supported; use Push Log Streams for arbitrary shapes. Returns HTTP 204 with an empty body on success. POST /loki/api/v1/push.
* **Push Log Streams** `pushLogStreams`: Pushes one or more log streams in Loki's native JSON push format, for arbitrary label sets, multiple entries per call and optional flat structured metadata. Each stream is {"stream": {label: value, ...}, "values": [[nanosecondEpochString, logLine, optional flat metadata object], ...]}. Returns HTTP 204 with an empty body on success. POST /loki/api/v1/push.
* **Push Logs (OTLP)** `pushLogsOtlp`: Ingests logs in OpenTelemetry Protocol JSON form (resourceLogs / scopeLogs / logRecords). Loki maps configured resource attributes such as service.name to stream labels and the rest to structured metadata. Returns 204 with an empty body. POST /otlp/v1/logs.
* **Query Instant** `queryInstant`: Runs a LogQL query at a single point in time. Loki only accepts METRIC queries here (e.g. sum(count_over_time({job=~\".+\"}[5m]))); a plain log-stream selector is rejected with 400 \"log queries are not supported as an instant query type\". Use Query Range for log lines. GET /loki/api/v1/query.
* **Query Range** `queryRange`: Runs a LogQL query over a time range and returns matching log lines (resultType "streams") or metric samples (resultType "matrix"). This is the main read endpoint - use it to verify that a pushed entry is queryable. start and end accept nanosecond epoch strings, RFC3339, or a duration like 5m. GET /loki/api/v1/query_range.

</details>
