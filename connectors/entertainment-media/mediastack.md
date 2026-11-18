---
description: "Mediastack by APILayer delivers real-time and historical worldwide news data in JSON format, aggregated from over 7,500 sources across 50 countries."
---

# Mediastack

Mediastack by APILayer delivers real-time and historical worldwide news data in JSON format, aggregated from over 7,500 sources across 50 countries. Endpoints cover live news (with a 30-minute delay on the Free plan), historical news by date or date range, and a searchable directory of supported news sources, with filtering by source, category, country, language, and keyword.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [mediastack.com](https://mediastack.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 3 |
| **Events** | 0 |
| **Slug** | `mediastack` |

## Use it

Add Mediastack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mediastack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Historical News | `getHistoricalNews` | Returns past news articles for a specific historical date or date range, optionally filtered by source, category, country, language, or keyword. Historical lookups are documented as a Standard-plan feature; on the connected Free-plan account this call was live-verified to succeed. |
| Get Live News | `getLiveNews` | Returns the most recent real-time news articles from Mediastack's worldwide sources, optionally filtered by source, category, country, language, or keyword. Free-plan accounts receive live news with a 30-minute publication delay. |
| Search News Sources | `searchNewsSources` | Searches Mediastack's directory of supported news sources by keyword, optionally filtered by country, language, or category. Returns source metadata including the source code used to filter live and historical news requests. |
