---
description: "Serpstack is a real-time Google Search Results (SERP) scraping API by APILayer."
hidden: true
---

# Serpstack

<img src="../../.gitbook/assets/connectors/lg/serpstack.png" alt="Serpstack logo">

Serpstack is a real-time Google Search Results (SERP) scraping API by APILayer. It returns structured JSON or CSV data for organic search results, images, local results, answer boxes, related searches, and pagination, and includes a Locations lookup helper for resolving canonical geographic targeting strings.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [serpstack.com](https://serpstack.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `serpstack` |

## Use it

Add Serpstack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.serpstack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Google Results</td><td><code>searchGoogleResults</code></td><td>Runs a real-time Google search and returns structured SERP data: organic results, local results, answer box, related searches and questions, and pagination. Supports web, image, and news search modes plus device, location, language, and date-range targeting. Output can be returned as JSON or CSV.</td></tr><tr><td>Search Locations</td><td><code>searchLocations</code></td><td>Looks up canonical Serpstack location strings matching a free-text place name, for use as the location parameter on Search Google Results. Returns each match's display name, canonical name, country code, target type, and reach.</td></tr></tbody></table>
