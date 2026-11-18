---
description: "World News API provides unified access to global news from thousands of sources in 86+ languages and 210+ countries, with full text, summaries, sentiment and…"
hidden: true
---

# World News API

World News API provides unified access to global news from thousands of sources in 86+ languages and 210+ countries, with full text, summaries, sentiment and entity analysis. This connector covers the complete World News API: keyword and semantic news search with date, language, country, category, author, sentiment and geo-radius filters, clustered top news by country, newspaper front pages, article retrieval by id, article and link extraction from any URL, news source lookup and suggestion, website-to-RSS conversion, and geocoding of location names. Every request consumes points from your daily quota.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [worldnewsapi.com](https://worldnewsapi.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 10 |
| **Events** | 0 |
| **Slug** | `worldNewsApi` |

## Use it

Add World News API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.worldNewsApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert Website To RSS Feed | `convertWebsiteToRssFeed` | Turns any page of a news website into an RSS 2.0 feed of the latest news links on that page. Optionally extracts each article to add description, publish date and image to every item. Returns XML. Costs points from your daily quota. |
| Extract News | `extractNews` | Extracts a news article from any URL, returning its title, text, summary, image, video, publish date and authors. Optionally analyzes the article to add entities and sentiment. Costs points from your daily quota. |
| Extract News Links | `extractNewsLinks` | Extracts the news article links found on a news website page such as a homepage or section page. Optionally restrict links to a prefix and include sub-domains. Costs points from your daily quota. |
| Get Geo Coordinates | `getGeoCoordinates` | Returns the latitude and longitude of a location name or address, for use in the location-filter parameter of Search News. Costs 1 point. |
| Get Top News | `getTopNews` | Returns the top news of a country in a given language for a specific date, clustered from multiple sources; clusters with more articles rank higher. Results for the current day are updated frequently. Costs points from your daily quota. |
| Retrieve News | `retrieveNews` | Retrieves one or more news articles by their ids, as returned by Search News or Get Top News, including full text, summary, image, authors, category, language, source country and sentiment. Costs points from your daily quota. |
| Retrieve Newspaper Front Page | `retrieveNewspaperFrontPage` | Returns the front page image of a newspaper for a given date, from more than 6,000 publications in 125 countries. Leave the filters empty for a random front page; the earliest available date is 2024-07-09. Costs points from your daily quota. |
| Search News | `searchNews` | Searches and filters news articles by text, publish date, location, category, language, source, author, entities and sentiment. Returns matching articles with title, full text, summary, image, video, publish date, authors, category, language, source country and sentiment. At least one filter must be set. Costs 1 point plus 0.01 points per returned article. |
| Search News Sources | `searchNewsSources` | Searches the news sources monitored by World News API by (partial) name, to check whether a publication is available in the API. Costs points from your daily quota. |
| Suggest News Source | `suggestNewsSource` | Suggests a news website to be monitored by World News API. Check with Search News Sources first whether it is already covered; providing a feed URL makes approval much more likely. Not available on the free plan, and suggestions may or may not be approved. |
