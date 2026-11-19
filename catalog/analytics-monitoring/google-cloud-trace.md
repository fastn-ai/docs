---
description: "Google Cloud Trace records request traces from your applications. List and read traces and write new spans."
hidden: true
---

# Google Cloud Trace

<img src="../../.gitbook/assets/connectors/lg/google-cloud-trace.png" alt="Google Cloud Trace logo">

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [cloudtrace.googleapis.com](https://cloudtrace.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleCloudTrace` |

## Setup

Your customers sign in to Google Cloud Trace through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Cloud Trace from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudTrace.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Write Spans</td><td><code>batchWriteSpans</code></td><td>Writes one new span to a new or existing trace in a Google Cloud project using the Cloud Trace v2 batchWrite API, for example a demo span named 'fastn-demo'. Spans cannot be updated; writing the same span ID again stores another copy. The span then appears in List Traces and Get Trace. Returns an empty object on success. Requires the https://www.googleapis.com/auth/trace.append scope.</td></tr><tr><td>Get Trace</td><td><code>getTrace</code></td><td>Gets a single trace by its trace ID, including all of its spans (name, span ID, parent span ID, kind, start and end time and labels), using the Cloud Trace v1 API. Read-only; requires the https://www.googleapis.com/auth/trace.readonly scope.</td></tr><tr><td>List Traces</td><td><code>listTraces</code></td><td>Lists traces collected in a Google Cloud project during a time interval, using the Cloud Trace v1 API. Use a small pageSize; view MINIMAL returns only trace IDs, ROOTSPAN adds root spans and COMPLETE returns all spans. Supports a trace filter and ordering. Read-only; requires the https://www.googleapis.com/auth/trace.readonly scope.</td></tr></tbody></table>

## Events

Google Cloud Trace has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
