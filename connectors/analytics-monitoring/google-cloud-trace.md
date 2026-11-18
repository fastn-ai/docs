---
description: "Google Cloud Trace API (https://cloudtrace.googleapis.com)."
hidden: true
---

# Google Cloud Trace

<img src="../../.gitbook/assets/connectors/google-cloud-trace.png" alt="Google Cloud Trace logo" width="64">

Google Cloud Trace API (https://cloudtrace.googleapis.com). List and read traces with the v1 API and write new spans with the v2 batchWrite API. OAuth 2.0 (Google) authorization-code auth with the trace.readonly and trace.append scopes.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [cloudtrace.googleapis.com](https://cloudtrace.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleCloudTrace` |

## Use it

Add Google Cloud Trace from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudTrace.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Write Spans | `batchWriteSpans` | Writes one new span to a new or existing trace in a Google Cloud project using the Cloud Trace v2 batchWrite API, for example a demo span named 'fastn-demo'. Spans cannot be updated; writing the same span ID again stores another copy. The span then appears in List Traces and Get Trace. Returns an empty object on success. Requires the https://www.googleapis.com/auth/trace.append scope. |
| Get Trace | `getTrace` | Gets a single trace by its trace ID, including all of its spans (name, span ID, parent span ID, kind, start and end time and labels), using the Cloud Trace v1 API. Read-only; requires the https://www.googleapis.com/auth/trace.readonly scope. |
| List Traces | `listTraces` | Lists traces collected in a Google Cloud project during a time interval, using the Cloud Trace v1 API. Use a small pageSize; view MINIMAL returns only trace IDs, ROOTSPAN adds root spans and COMPLETE returns all spans. Supports a trace filter and ordering. Read-only; requires the https://www.googleapis.com/auth/trace.readonly scope. |
