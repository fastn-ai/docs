---
description: "NewsAPI collects articles and headlines from news sources and blogs worldwide. Search articles, get top headlines and list sources."
hidden: true
---

# NewsAPI

<img src="../../.gitbook/assets/connectors/lg/newsapi.png" alt="NewsAPI logo">

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [newsapi.org](https://newsapi.org) |
| **Authentication** | API key |
| **Slug** | `newsapi` |

## Setup

Your customers enter their API key for NewsAPI when they connect. Nothing else needs setting up.

## Use it

Add NewsAPI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.newsapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List News Sources</td><td><code>listNewsSources</code></td><td>Lists the news publishers available through NewsAPI, optionally narrowed by category, language or country. Use the returned identifiers in the sources input of the other actions.</td></tr><tr><td>List Top Headlines</td><td><code>listTopHeadlines</code></td><td>Retrieves breaking-news headlines for a country, category or set of sources. The sources input cannot be combined with country or category, and at least one of country, category, sources or the search query must be supplied.</td></tr><tr><td>Search All Articles</td><td><code>searchEverything</code></td><td>Searches every article NewsAPI has indexed from over 150,000 publishers, with full-text keyword search, source and domain filters, a date range and sorting. At least one of the query, title query, sources or domains inputs must be supplied or the API returns a parametersMissing error.</td></tr></tbody></table>

## Events

NewsAPI has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
