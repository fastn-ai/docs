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

Your customers sign in to Google Cloud Monitoring through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Cloud Monitoring from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Cloud Monitoring**.
2. Select **Connect** on the Google Cloud Monitoring card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Cloud Monitoring and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Cloud Monitoring's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Custom Metric Descriptor</td><td><code>createCustomMetricDescriptor</code></td><td>Creates a custom GAUGE metric descriptor with DOUBLE values, of type custom.googleapis.com/&lt;customMetricName&gt;, in a Google Cloud project. Use it to set up a harmless demo metric, write a point with Create Time Series, then remove it with Delete Custom Metric Descriptor. Returns the created descriptor. Requires the https://www.googleapis.com/auth/monitoring.write scope (monitoring also works).</td></tr><tr><td>Create Time Series</td><td><code>createTimeSeries</code></td><td>Writes one DOUBLE data point to the custom metric custom.googleapis.com/&lt;customMetricName&gt; on the 'global' monitored resource of a Google Cloud project. The end time must be within the last 25 hours and points for the same series must be at least 5 seconds apart. Returns an empty object on success. Requires the https://www.googleapis.com/auth/monitoring.write scope (monitoring also works).</td></tr><tr><td>Delete Custom Metric Descriptor</td><td><code>deleteCustomMetricDescriptor</code></td><td>Deletes the custom metric descriptor custom.googleapis.com/&lt;customMetricName&gt; from a Google Cloud project, together with its time series data. Only custom metrics can be deleted. Use it to clean up after Create Custom Metric Descriptor. Returns an empty object on success. Requires the https://www.googleapis.com/auth/monitoring scope.</td></tr><tr><td>Get Custom Metric Descriptor</td><td><code>getCustomMetricDescriptor</code></td><td>Gets one custom metric descriptor of type custom.googleapis.com/&lt;customMetricName&gt; from a Google Cloud project, for example to confirm that Create Custom Metric Descriptor succeeded. Returns the descriptor's type, kind, value type, unit and labels. Read-only; requires the https://www.googleapis.com/auth/monitoring.read scope (monitoring or monitoring.write also work).</td></tr><tr><td>List Metric Descriptors</td><td><code>listMetricDescriptors</code></td><td>Lists the metric descriptors (built-in and custom metric types) available in a Google Cloud project. Use a small pageSize and an optional monitoring filter such as metric.type = starts_with("custom.googleapis.com/") to narrow the results. Returns each descriptor's type, kind, value type, unit and labels. Read-only; requires the https://www.googleapis.com/auth/monitoring.read scope (monitoring or monitoring.write also work).</td></tr><tr><td>List Time Series</td><td><code>listTimeSeries</code></td><td>Lists time series data points of one metric type in a Google Cloud project over a time interval (full view). The filter must name exactly one metric type, for example metric.type = "compute.googleapis.com/instance/cpu/utilization" or metric.type = "custom.googleapis.com/fastn_demo_metric". Use a small pageSize. Returns the matching time series with their metric, monitored resource and points. Read-only; requires the https://www.googleapis.com/auth/monitoring.read scope (monitoring also works).</td></tr></tbody></table>

