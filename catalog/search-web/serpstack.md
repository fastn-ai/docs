---
description: "Serpstack returns Google search results as structured data. Run Google searches and look up supported locations."
hidden: true
---

# Serpstack

<img src="../../.gitbook/assets/connectors/lg/serpstack.png" alt="Serpstack logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [serpstack.com](https://serpstack.com) |
| **Authentication** | API key |
| **Slug** | `serpstack` |

## Setup

Your customers enter their API key for Serpstack when they connect. Nothing else needs setting up.

## Use it

Add Serpstack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.serpstack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Google Results</td><td><code>searchGoogleResults</code></td><td>Runs a real-time Google search and returns structured SERP data: organic results, local results, answer box, related searches and questions, and pagination. Supports web, image, and news search modes plus device, location, language, and date-range targeting. Output can be returned as JSON or CSV.</td></tr><tr><td>Search Locations</td><td><code>searchLocations</code></td><td>Looks up canonical Serpstack location strings matching a free-text place name, for use as the location parameter on Search Google Results. Returns each match's display name, canonical name, country code, target type, and reach.</td></tr></tbody></table>

## Events

Serpstack has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
