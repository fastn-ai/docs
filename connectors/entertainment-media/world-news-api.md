---
description: "World News API provides news from thousands of sources worldwide. Search and get top news, extract articles and read newspaper front pages."
hidden: true
---

# World News API

<img src="../../.gitbook/assets/connectors/lg/world-news-api.png" alt="World News API logo">

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [worldnewsapi.com](https://worldnewsapi.com) |
| **Authentication** | API key |
| **Slug** | `worldNewsApi` |

## Setup

Your customers enter their API key for World News API when they connect. Nothing else needs setting up.

## Use it

Add World News API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.worldNewsApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Convert Website To RSS Feed</td><td><code>convertWebsiteToRssFeed</code></td><td>Turns any page of a news website into an RSS 2.0 feed of the latest news links on that page. Optionally extracts each article to add description, publish date and image to every item. Returns XML. Costs points from your daily quota.</td></tr><tr><td>Extract News</td><td><code>extractNews</code></td><td>Extracts a news article from any URL, returning its title, text, summary, image, video, publish date and authors. Optionally analyzes the article to add entities and sentiment. Costs points from your daily quota.</td></tr><tr><td>Extract News Links</td><td><code>extractNewsLinks</code></td><td>Extracts the news article links found on a news website page such as a homepage or section page. Optionally restrict links to a prefix and include sub-domains. Costs points from your daily quota.</td></tr><tr><td>Get Geo Coordinates</td><td><code>getGeoCoordinates</code></td><td>Returns the latitude and longitude of a location name or address, for use in the location-filter parameter of Search News. Costs 1 point.</td></tr><tr><td>Get Top News</td><td><code>getTopNews</code></td><td>Returns the top news of a country in a given language for a specific date, clustered from multiple sources; clusters with more articles rank higher. Results for the current day are updated frequently. Costs points from your daily quota.</td></tr><tr><td>Retrieve News</td><td><code>retrieveNews</code></td><td>Retrieves one or more news articles by their ids, as returned by Search News or Get Top News, including full text, summary, image, authors, category, language, source country and sentiment. Costs points from your daily quota.</td></tr><tr><td>Retrieve Newspaper Front Page</td><td><code>retrieveNewspaperFrontPage</code></td><td>Returns the front page image of a newspaper for a given date, from more than 6,000 publications in 125 countries. Leave the filters empty for a random front page; the earliest available date is 2024-07-09. Costs points from your daily quota.</td></tr><tr><td>Search News</td><td><code>searchNews</code></td><td>Searches and filters news articles by text, publish date, location, category, language, source, author, entities and sentiment. Returns matching articles with title, full text, summary, image, video, publish date, authors, category, language, source country and sentiment. At least one filter must be set. Costs 1 point plus 0.01 points per returned article.</td></tr><tr><td>Search News Sources</td><td><code>searchNewsSources</code></td><td>Searches the news sources monitored by World News API by (partial) name, to check whether a publication is available in the API. Costs points from your daily quota.</td></tr><tr><td>Suggest News Source</td><td><code>suggestNewsSource</code></td><td>Suggests a news website to be monitored by World News API. Check with Search News Sources first whether it is already covered; providing a feed URL makes approval much more likely. Not available on the free plan, and suggestions may or may not be approved.</td></tr></tbody></table>

## Events

World News API has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
