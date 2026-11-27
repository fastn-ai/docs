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

Your customers sign in to Google Cloud Trace through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Cloud Trace from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Cloud Trace**.
2. Select **Connect** on the Google Cloud Trace card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Cloud Trace and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Cloud Trace's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Write Spans</td><td><code>batchWriteSpans</code></td><td>Writes one new span to a new or existing trace in a Google Cloud project using the Cloud Trace v2 batchWrite API, for example a demo span named 'fastn-demo'. Spans cannot be updated; writing the same span ID again stores another copy. The span then appears in List Traces and Get Trace. Returns an empty object on success. Requires the https://www.googleapis.com/auth/trace.append scope.</td></tr><tr><td>Get Trace</td><td><code>getTrace</code></td><td>Gets a single trace by its trace ID, including all of its spans (name, span ID, parent span ID, kind, start and end time and labels), using the Cloud Trace v1 API. Read-only; requires the https://www.googleapis.com/auth/trace.readonly scope.</td></tr><tr><td>List Traces</td><td><code>listTraces</code></td><td>Lists traces collected in a Google Cloud project during a time interval, using the Cloud Trace v1 API. Use a small pageSize; view MINIMAL returns only trace IDs, ROOTSPAN adds root spans and COMPLETE returns all spans. Supports a trace filter and ordering. Read-only; requires the https://www.googleapis.com/auth/trace.readonly scope.</td></tr></tbody></table>

