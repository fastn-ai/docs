---
description: "Mediastack provides live and historical news from thousands of sources worldwide. Get live and past news and search news sources."
hidden: true
---

# Mediastack

<img src="../../.gitbook/assets/connectors/lg/mediastack.png" alt="Mediastack logo">

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [mediastack.com](https://mediastack.com) |
| **Authentication** | API key |
| **Slug** | `mediastack` |

## Setup

Your customers enter their API key for Mediastack when they connect. Nothing else needs setting up.

## Use it

Add Mediastack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mediastack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Historical News</td><td><code>getHistoricalNews</code></td><td>Returns past news articles for a specific historical date or date range, optionally filtered by source, category, country, language, or keyword. Historical lookups are documented as a Standard-plan feature; on the connected Free-plan account this call was live-verified to succeed.</td></tr><tr><td>Get Live News</td><td><code>getLiveNews</code></td><td>Returns the most recent real-time news articles from Mediastack's worldwide sources, optionally filtered by source, category, country, language, or keyword. Free-plan accounts receive live news with a 30-minute publication delay.</td></tr><tr><td>Search News Sources</td><td><code>searchNewsSources</code></td><td>Searches Mediastack's directory of supported news sources by keyword, optionally filtered by country, language, or category. Returns source metadata including the source code used to filter live and historical news requests.</td></tr></tbody></table>

## Events

Mediastack has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
