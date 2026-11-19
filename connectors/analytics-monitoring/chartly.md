---
description: "Connect Chartly to your product with fastn."
hidden: true
---

# Chartly

<img src="../../.gitbook/assets/connectors/lg/chartly.png" alt="Chartly logo">

Chartly renders Chart.js configurations into PNG or SVG chart images over a simple HTTP API, for embedding charts in emails, Slack messages, PDFs and low-code tools. This connector covers the whole Chartly v1 API: rendering a chart from a full Chart.js config by GET or POST, creating permanent signed short URLs and resolving them, the public watermarked open-render endpoint, the four simplified bar, line, pie and multi-series chart builders, the health check, and anonymous trial key provisioning.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [chartly.dev](https://chartly.dev) |
| **Authentication** | Credentials you enter |
| **Slug** | `chartly` |

## Use it

Add Chartly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.chartly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Bar Chart</td><td><code>createBarChart</code></td><td>Builds a bar chart from plain labels and values without writing any Chart.js configuration, and returns a URL to the rendered image.</td></tr><tr><td>Create Chart Short URL</td><td><code>createChartShortUrl</code></td><td>Stores a Chart.js configuration and returns a permanent signed short URL that renders it, so the chart can be pasted anywhere without exposing your API key.</td></tr><tr><td>Create Line Chart</td><td><code>createLineChart</code></td><td>Builds a line chart from plain labels and values without writing any Chart.js configuration, which suits time series and trends, and returns a URL to the rendered image.</td></tr><tr><td>Create Multi-Series Chart</td><td><code>createMultiSeriesChart</code></td><td>Builds a bar or line chart comparing up to three data series over the same labels, and returns a URL to the rendered image.</td></tr><tr><td>Create Pie Chart</td><td><code>createPieChart</code></td><td>Builds a pie chart from plain labels and values without writing any Chart.js configuration, which suits proportions and distributions, and returns a URL to the rendered image.</td></tr><tr><td>Create Trial API Key</td><td><code>createTrialApiKey</code></td><td>Provisions an anonymous Chartly trial API key. No authentication is required, and Chartly allows only one trial key per IP address every 30 days.</td></tr><tr><td>Get API Status</td><td><code>getApiStatus</code></td><td>Checks that the Chartly rendering service is healthy and reports its current build and cache latency.</td></tr><tr><td>Get Chart Image By ID</td><td><code>getChartImageById</code></td><td>Resolves a stored chart by its id and returns the cached chart image. The id is the chart_id returned by the bar, line, pie and multi-series builders, or the trailing path segment of the url returned by Create Chart Short URL. No API key is needed. The response is binary, so it arrives as a file reference rather than JSON.</td></tr><tr><td>Render Chart</td><td><code>renderChart</code></td><td>Renders a full Chart.js configuration into a PNG or SVG image and returns the image itself. Use this for large configurations or ones containing JavaScript functions. The response is binary, so it arrives as a file reference rather than JSON.</td></tr><tr><td>Render Chart From URL Config</td><td><code>renderChartFromUrlConfig</code></td><td>Renders a chart whose Chart.js configuration is passed as a URL-encoded JSON string rather than a request body. This is the fastest option for emails and Slack integrations. The response is binary, so it arrives as a file reference rather than JSON.</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Render Open Chart</td><td><code>renderOpenChart</code></td><td>Renders a chart through Chartly's public endpoint, which needs no API key but watermarks every image and is rate limited per IP address. Supply either a full Chart.js config or the type, labels and data shortcut.</td></tr></tbody></table>

</details>
