---
description: "Chartly renders Chart.js configurations into PNG or SVG chart images over a simple HTTP API, for embedding charts in emails, Slack messages, PDFs and low-code…"
hidden: true
---

# Chartly

Chartly renders Chart.js configurations into PNG or SVG chart images over a simple HTTP API, for embedding charts in emails, Slack messages, PDFs and low-code tools. This connector covers the whole Chartly v1 API: rendering a chart from a full Chart.js config by GET or POST, creating permanent signed short URLs and resolving them, the public watermarked open-render endpoint, the four simplified bar, line, pie and multi-series chart builders, the health check, and anonymous trial key provisioning.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [chartly.dev](https://chartly.dev) |
| **Authentication** | Credentials you enter |
| **Actions** | 11 |
| **Events** | 0 |
| **Slug** | `chartly` |

## Use it

Add Chartly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.chartly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Bar Chart | `createBarChart` | Builds a bar chart from plain labels and values without writing any Chart.js configuration, and returns a URL to the rendered image. |
| Create Chart Short URL | `createChartShortUrl` | Stores a Chart.js configuration and returns a permanent signed short URL that renders it, so the chart can be pasted anywhere without exposing your API key. |
| Create Line Chart | `createLineChart` | Builds a line chart from plain labels and values without writing any Chart.js configuration, which suits time series and trends, and returns a URL to the rendered image. |
| Create Multi-Series Chart | `createMultiSeriesChart` | Builds a bar or line chart comparing up to three data series over the same labels, and returns a URL to the rendered image. |
| Create Pie Chart | `createPieChart` | Builds a pie chart from plain labels and values without writing any Chart.js configuration, which suits proportions and distributions, and returns a URL to the rendered image. |
| Create Trial API Key | `createTrialApiKey` | Provisions an anonymous Chartly trial API key. No authentication is required, and Chartly allows only one trial key per IP address every 30 days. |
| Get API Status | `getApiStatus` | Checks that the Chartly rendering service is healthy and reports its current build and cache latency. |
| Get Chart Image By ID | `getChartImageById` | Resolves a stored chart by its id and returns the cached chart image. The id is the chart_id returned by the bar, line, pie and multi-series builders, or the trailing path segment of the url returned by Create Chart Short URL. No API key is needed. The response is binary, so it arrives as a file reference rather than JSON. |
| Render Chart | `renderChart` | Renders a full Chart.js configuration into a PNG or SVG image and returns the image itself. Use this for large configurations or ones containing JavaScript functions. The response is binary, so it arrives as a file reference rather than JSON. |
| Render Chart From URL Config | `renderChartFromUrlConfig` | Renders a chart whose Chart.js configuration is passed as a URL-encoded JSON string rather than a request body. This is the fastest option for emails and Slack integrations. The response is binary, so it arrives as a file reference rather than JSON. |
| Render Open Chart | `renderOpenChart` | Renders a chart through Chartly's public endpoint, which needs no API key but watermarks every image and is rate limited per IP address. Supply either a full Chart.js config or the type, labels and data shortcut. |
