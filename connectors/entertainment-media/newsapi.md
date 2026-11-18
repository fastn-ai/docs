---
description: "NewsAPI indexes articles and breaking headlines from over 150,000 news sources and blogs worldwide."
---

# NewsAPI

NewsAPI indexes articles and breaking headlines from over 150,000 news sources and blogs worldwide. It exposes full-text article search with date, language, source and domain filters, country and category top headlines, and a catalogue of available publishers. Requests authenticate with an API key sent in the X-Api-Key header.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [newsapi.org](https://newsapi.org) |
| **Authentication** | Credentials you enter |
| **Actions** | 3 |
| **Events** | 0 |
| **Slug** | `newsapi` |

## Use it

Add NewsAPI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.newsapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| List News Sources | `listNewsSources` | Lists the news publishers available through NewsAPI, optionally narrowed by category, language or country. Use the returned identifiers in the sources input of the other actions. |
| List Top Headlines | `listTopHeadlines` | Retrieves breaking-news headlines for a country, category or set of sources. The sources input cannot be combined with country or category, and at least one of country, category, sources or the search query must be supplied. |
| Search All Articles | `searchEverything` | Searches every article NewsAPI has indexed from over 150,000 publishers, with full-text keyword search, source and domain filters, a date range and sorting. At least one of the query, title query, sources or domains inputs must be supplied or the API returns a parametersMissing error. |
