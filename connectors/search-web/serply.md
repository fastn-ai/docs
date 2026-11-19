---
description: "Serply returns search results and scrapes pages. Search Google, Bing and eBay, read Reddit posts and comments, and scrape URLs."
hidden: true
---

# Serply

<img src="../../.gitbook/assets/connectors/lg/serply.png" alt="Serply logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [serply.io](https://serply.io) |
| **Authentication** | API key |
| **Slug** | `serply` |

## Setup

Your customers enter their API key for Serply when they connect. Nothing else needs setting up.

## Use it

Add Serply from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.serply.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Reddit Comments</td><td><code>getRedditComments</code></td><td>Retrieves a Reddit post together with its full comment thread. The response data array holds two listings: the post first and then its comment tree.</td></tr><tr><td>Get Reddit Post</td><td><code>getRedditPost</code></td><td>Retrieves a single Reddit post by its id, unwrapped from Reddit's listing envelope, with an option to include the post's comment tree.</td></tr><tr><td>Get Subreddit Details</td><td><code>getSubredditDetails</code></td><td>Retrieves metadata describing a subreddit, such as its title, public description, subscriber count and creation date, in Reddit's own format.</td></tr><tr><td>List Reddit User Posts</td><td><code>listRedditUserPosts</code></td><td>Lists a Reddit user's post history in Reddit's own listing format, with sort order, time window, page size and cursor pagination.</td></tr><tr><td>List Subreddit Posts</td><td><code>listSubredditPosts</code></td><td>Lists posts from a subreddit in Reddit's own listing format, with sort order, time window, page size and cursor pagination.</td></tr><tr><td>Scrape URL</td><td><code>scrapeUrl</code></td><td>Fetches any URL through Serply's servers with automatic captcha bypass and returns the page either as full HTML with upstream status, headers and resolved request, or as markdown text suitable for AI and LLM processing.</td></tr><tr><td>Search Bing</td><td><code>searchBing</code></td><td>Runs a Bing web search and returns organic results together with text advertisements and shopping ads shown on the results page. Supports Bing search operators, proxy location and device type.</td></tr><tr><td>Search eBay</td><td><code>searchEbay</code></td><td>Searches eBay listings and returns each result's title, link, position, price, previous price, condition, image, seller, seller feedback and shipping attributes.</td></tr><tr><td>Search Google</td><td><code>searchGoogle</code></td><td>Runs a Google web search and returns organic results along with any SERP features Google shows for the query, such as ads, answer boxes, knowledge panels, related searches and local places. Supports search operators, page size and offset pagination, proxy location and device type.</td></tr><tr><td>Search Google Images</td><td><code>searchGoogleImages</code></td><td>Runs a Google Images search and returns up to 20 images, each with Google-hosted thumbnails, the page the image was found on, and the original image URL, dimensions and file format. This endpoint has no pagination.</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Google Jobs</td><td><code>searchGoogleJobs</code></td><td>Searches Google Jobs for listings matching a position title and optional location, returning employer, location, apply link and posting date for each job. Currently only jobs in North America are supported.</td></tr><tr><td>Search Google Maps</td><td><code>searchGoogleMaps</code></td><td>Searches Google Maps for places matching a location or category query and returns structured place records including name, address, coordinates, rating, categories, phone, website, timezone and opening hours.</td></tr><tr><td>Search Google News</td><td><code>searchGoogleNews</code></td><td>Searches Google News for articles from thousands of sources and returns the news feed metadata and the matching article entries with title, link, publication date, summary and source. Results can be scoped to a country and language edition.</td></tr><tr><td>Search Google Scholar</td><td><code>searchGoogleScholar</code></td><td>Searches scholarly literature for academic papers and articles, returning title, link, authors, open-access document link and citation count for each article. Supports page size up to 200 and offset pagination.</td></tr><tr><td>Search Google Videos</td><td><code>searchGoogleVideos</code></td><td>Runs a Google Video search and returns video results with their titles, links and positions, plus any other SERP features on the page. Supports search operators, page size, offset pagination, proxy location and device type.</td></tr><tr><td>Search Products</td><td><code>searchProducts</code></td><td>Searches Amazon product listings and returns each product's ASIN, title, price, rating, review count, image, Prime eligibility, bestseller flag and sponsored status.</td></tr></tbody></table>

</details>

## Events

Serply has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
