---
description: "Serply provides real-time search engine results and web scraping over a simple REST API."
hidden: true
---

# Serply

<img src="../../.gitbook/assets/connectors/serply.png" alt="Serply logo" width="64">

Serply provides real-time search engine results and web scraping over a simple REST API. This connector covers the full Serply API: Google Search, Google Video, Google Images, Google Jobs, Google Scholar, Google News, Google Maps, Bing Search, Amazon product search, eBay search, Reddit subreddits, users, posts and comment threads, and the URL scraping Request endpoint that returns full HTML or markdown.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [serply.io](https://serply.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `serply` |

## Use it

Add Serply from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.serply.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Reddit Comments | `getRedditComments` | Retrieves a Reddit post together with its full comment thread. The response data array holds two listings: the post first and then its comment tree. |
| Get Reddit Post | `getRedditPost` | Retrieves a single Reddit post by its id, unwrapped from Reddit's listing envelope, with an option to include the post's comment tree. |
| Get Subreddit Details | `getSubredditDetails` | Retrieves metadata describing a subreddit, such as its title, public description, subscriber count and creation date, in Reddit's own format. |
| List Reddit User Posts | `listRedditUserPosts` | Lists a Reddit user's post history in Reddit's own listing format, with sort order, time window, page size and cursor pagination. |
| List Subreddit Posts | `listSubredditPosts` | Lists posts from a subreddit in Reddit's own listing format, with sort order, time window, page size and cursor pagination. |
| Scrape URL | `scrapeUrl` | Fetches any URL through Serply's servers with automatic captcha bypass and returns the page either as full HTML with upstream status, headers and resolved request, or as markdown text suitable for AI and LLM processing. |
| Search Bing | `searchBing` | Runs a Bing web search and returns organic results together with text advertisements and shopping ads shown on the results page. Supports Bing search operators, proxy location and device type. |
| Search eBay | `searchEbay` | Searches eBay listings and returns each result's title, link, position, price, previous price, condition, image, seller, seller feedback and shipping attributes. |
| Search Google | `searchGoogle` | Runs a Google web search and returns organic results along with any SERP features Google shows for the query, such as ads, answer boxes, knowledge panels, related searches and local places. Supports search operators, page size and offset pagination, proxy location and device type. |
| Search Google Images | `searchGoogleImages` | Runs a Google Images search and returns up to 20 images, each with Google-hosted thumbnails, the page the image was found on, and the original image URL, dimensions and file format. This endpoint has no pagination. |

<details>

<summary>See 6 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Search Google Jobs | `searchGoogleJobs` | Searches Google Jobs for listings matching a position title and optional location, returning employer, location, apply link and posting date for each job. Currently only jobs in North America are supported. |
| Search Google Maps | `searchGoogleMaps` | Searches Google Maps for places matching a location or category query and returns structured place records including name, address, coordinates, rating, categories, phone, website, timezone and opening hours. |
| Search Google News | `searchGoogleNews` | Searches Google News for articles from thousands of sources and returns the news feed metadata and the matching article entries with title, link, publication date, summary and source. Results can be scoped to a country and language edition. |
| Search Google Scholar | `searchGoogleScholar` | Searches scholarly literature for academic papers and articles, returning title, link, authors, open-access document link and citation count for each article. Supports page size up to 200 and offset pagination. |
| Search Google Videos | `searchGoogleVideos` | Runs a Google Video search and returns video results with their titles, links and positions, plus any other SERP features on the page. Supports search operators, page size, offset pagination, proxy location and device type. |
| Search Products | `searchProducts` | Searches Amazon product listings and returns each product's ASIN, title, price, rating, review count, image, Prime eligibility, bestseller flag and sponsored status. |

</details>
