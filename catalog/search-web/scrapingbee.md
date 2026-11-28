---
description: "ScrapingBee is a web scraping service. Extract structured data, run web searches and get Amazon and Walmart product data."
hidden: true
---

# ScrapingBee

<img src="../../.gitbook/assets/connectors/lg/scrapingbee.png" alt="ScrapingBee logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [scrapingbee.com](https://scrapingbee.com) |
| **Authentication** | API key |
| **Slug** | `scrapingbee` |

## Setup

Your customers enter their API key for ScrapingBee when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect ScrapingBee from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **ScrapingBee**.
2. Select **Connect** on the ScrapingBee card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use ScrapingBee's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Ask ChatGPT</td><td><code>askChatgpt</code></td><td>Sends a prompt to ChatGPT (optionally with live web search enabled) and returns its response, without you needing an OpenAI account or API key.</td></tr><tr><td>Ask Gemini</td><td><code>askGemini</code></td><td>Sends a prompt to Google Gemini and returns its response, without you needing a Google AI API key.</td></tr><tr><td>Extract Structured Data</td><td><code>extractStructuredData</code></td><td>Scrapes a webpage and extracts structured data from it using CSS-selector extraction rules (extract_rules) and/or AI-powered extraction (ai_query/ai_extract_rules), returning clean JSON instead of raw HTML. Uses the same underlying scrape endpoint as Scrape Webpage but is a distinct use case since the response shape is structured JSON, not a page body.</td></tr><tr><td>Fast Search</td><td><code>fastSearch</code></td><td>Runs a lightweight, sub-second search and returns results - a faster, cheaper alternative to Search Google for use cases that don't need the full richness of a Google SERP scrape.</td></tr><tr><td>Find Employees (Agentic Search)</td><td><code>findEmployeesAgenticSearch</code></td><td>Runs an AI agent that searches the web for people/employees matching a natural-language description (role, seniority, company, location, etc.) and returns matching candidate profiles. Very high cost per call (3,750 credits) - budget carefully before use.</td></tr><tr><td>Get Account Usage</td><td><code>getAccountUsage</code></td><td>Returns the connected ScrapingBee account's current API credit usage and concurrency limits - total monthly credits, credits used so far, max concurrent requests, and current concurrent requests. Free to call - does not consume any API credits.</td></tr><tr><td>Get Amazon Pricing</td><td><code>getAmazonPricing</code></td><td>Fetches the full list of current offers for an Amazon product by ASIN - every seller, condition, price, and delivery option on the offer-listing page - useful for price comparison and buy-box monitoring.</td></tr><tr><td>Get Amazon Product</td><td><code>getAmazonProduct</code></td><td>Fetches structured details for a single Amazon product page by ASIN - title, price, rating, images, description, variants - without you writing an Amazon-specific scraper.</td></tr><tr><td>Get Walmart Product</td><td><code>getWalmartProduct</code></td><td>Fetches structured details for a single Walmart product page by product ID - title, price, rating, images, description, availability - without you writing a Walmart-specific scraper.</td></tr><tr><td>Get YouTube Metadata</td><td><code>getYoutubeMetadata</code></td><td>Fetches structured metadata for a single YouTube video by video ID - title, description, channel, view/comment counts, category, upload date - without calling the official YouTube Data API.</td></tr></tbody></table>

<details>

<summary>View 7 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get YouTube Subtitles</td><td><code>getYoutubeSubtitles</code></td><td>Fetches the closed-caption/subtitle track for a YouTube video by video ID, including auto-generated captions, with per-line timing.</td></tr><tr><td>Scrape Webpage</td><td><code>scrapeWebpage</code></td><td>Fetches a webpage through ScrapingBee's proxy/headless-browser infrastructure and returns the rendered HTML (or text/markdown/screenshot variants via flags). Supports JavaScript rendering, premium/stealth residential proxies, geolocation, custom cookies, header forwarding, and JS interaction scenarios to avoid bot detection.</td></tr><tr><td>Search Amazon Products</td><td><code>searchAmazonProducts</code></td><td>Searches Amazon for products matching a keyword query and returns structured search-result listings (title, price, rating, ASIN, image) across one or more result pages.</td></tr><tr><td>Search Google</td><td><code>searchGoogle</code></td><td>Runs a Google search and returns structured results - organic results, ads, knowledge graph, local results, news, images, and related queries - without you having to scrape and parse Google's HTML yourself.</td></tr><tr><td>Search Walmart Products</td><td><code>searchWalmartProducts</code></td><td>Searches Walmart.com for products matching a keyword query and returns structured search-result listings with pricing, ratings, and fulfillment/delivery options.</td></tr><tr><td>Search YouTube</td><td><code>searchYoutube</code></td><td>Searches YouTube for videos, channels, playlists, or movies matching a keyword query, with rich filters for quality, duration, upload date, and content type.</td></tr><tr><td>Take Screenshot</td><td><code>takeScreenshot</code></td><td>Renders a webpage and captures a screenshot of it as a base64-encoded image, optionally full-page or scoped to one element via a CSS selector. Uses the same scrape endpoint with screenshot=true and json_response=true so the image comes back as base64 JSON rather than a raw binary body.</td></tr></tbody></table>

</details>

