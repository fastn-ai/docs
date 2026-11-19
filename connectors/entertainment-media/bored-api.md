---
description: "Connect Bored API to your product with fastn."
hidden: true
---

# Bored API

The Bored API (hosted by The App Brewery) suggests things to do when you are bored: get a random activity, filter activities by type and number of participants, or look one up by key. Free with no API key; limited to 100 requests per 15 minutes.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [bored-api.appbrewery.com](https://bored-api.appbrewery.com) |
| **Authentication** | No authentication |
| **Slug** | `boredApi` |

## Use it

Add Bored API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.boredApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Filter Activities</td><td><code>filterActivities</code></td><td>List activities filtered by type and/or number of participants (GET /filter). Returns 404 'Activities not found for the given filter.' when nothing matches. Docs: https://bored-api.appbrewery.com/</td></tr><tr><td>Get Activity</td><td><code>getActivity</code></td><td>Get one activity by its key (GET /activity/{key}). Unknown keys return 404 'Activity not found'. Docs: https://bored-api.appbrewery.com/</td></tr><tr><td>Get Random Activity</td><td><code>getRandomActivity</code></td><td>Get one randomly selected activity suggestion (GET /random). Docs: https://bored-api.appbrewery.com/</td></tr></tbody></table>
