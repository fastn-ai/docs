---
description: "Google Cloud Monitoring collects metrics from Google Cloud. List metrics and time series, write time series and manage custom metrics."
hidden: true
---

# Google Cloud Monitoring

<img src="../../.gitbook/assets/connectors/lg/google-cloud-monitoring.png" alt="Google Cloud Monitoring logo">

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [monitoring.googleapis.com](https://monitoring.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleCloudMonitoring` |

## Setup

Your customers sign in to Google Cloud Monitoring through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Cloud Monitoring from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudMonitoring.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Custom Metric Descriptor</td><td><code>createCustomMetricDescriptor</code></td><td>Creates a custom GAUGE metric descriptor with DOUBLE values, of type custom.googleapis.com/&lt;customMetricName&gt;, in a Google Cloud project. Use it to set up a harmless demo metric, write a point with Create Time Series, then remove it with Delete Custom Metric Descriptor. Returns the created descriptor. Requires the https://www.googleapis.com/auth/monitoring.write scope (monitoring also works).</td></tr><tr><td>Create Time Series</td><td><code>createTimeSeries</code></td><td>Writes one DOUBLE data point to the custom metric custom.googleapis.com/&lt;customMetricName&gt; on the 'global' monitored resource of a Google Cloud project. The end time must be within the last 25 hours and points for the same series must be at least 5 seconds apart. Returns an empty object on success. Requires the https://www.googleapis.com/auth/monitoring.write scope (monitoring also works).</td></tr><tr><td>Delete Custom Metric Descriptor</td><td><code>deleteCustomMetricDescriptor</code></td><td>Deletes the custom metric descriptor custom.googleapis.com/&lt;customMetricName&gt; from a Google Cloud project, together with its time series data. Only custom metrics can be deleted. Use it to clean up after Create Custom Metric Descriptor. Returns an empty object on success. Requires the https://www.googleapis.com/auth/monitoring scope.</td></tr><tr><td>Get Custom Metric Descriptor</td><td><code>getCustomMetricDescriptor</code></td><td>Gets one custom metric descriptor of type custom.googleapis.com/&lt;customMetricName&gt; from a Google Cloud project, for example to confirm that Create Custom Metric Descriptor succeeded. Returns the descriptor's type, kind, value type, unit and labels. Read-only; requires the https://www.googleapis.com/auth/monitoring.read scope (monitoring or monitoring.write also work).</td></tr><tr><td>List Metric Descriptors</td><td><code>listMetricDescriptors</code></td><td>Lists the metric descriptors (built-in and custom metric types) available in a Google Cloud project. Use a small pageSize and an optional monitoring filter such as metric.type = starts_with("custom.googleapis.com/") to narrow the results. Returns each descriptor's type, kind, value type, unit and labels. Read-only; requires the https://www.googleapis.com/auth/monitoring.read scope (monitoring or monitoring.write also work).</td></tr><tr><td>List Time Series</td><td><code>listTimeSeries</code></td><td>Lists time series data points of one metric type in a Google Cloud project over a time interval (full view). The filter must name exactly one metric type, for example metric.type = "compute.googleapis.com/instance/cpu/utilization" or metric.type = "custom.googleapis.com/fastn_demo_metric". Use a small pageSize. Returns the matching time series with their metric, monitored resource and points. Read-only; requires the https://www.googleapis.com/auth/monitoring.read scope (monitoring also works).</td></tr></tbody></table>

## Events

Google Cloud Monitoring has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
