---
description: "ScrapingBee is a web scraping API that handles headless browser rendering, JavaScript execution, and rotating proxies (including premium/stealth residential…"
hidden: true
---

# ScrapingBee

<img src="../../.gitbook/assets/connectors/scrapingbee.png" alt="ScrapingBee logo" width="64">

ScrapingBee is a web scraping API that handles headless browser rendering, JavaScript execution, and rotating proxies (including premium/stealth residential proxies) so you can scrape any webpage without getting blocked. It also offers specialized APIs for Google Search, Fast Search, Amazon, Walmart, YouTube, ChatGPT, Gemini, and AI-powered employee search.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [scrapingbee.com](https://scrapingbee.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `scrapingbee` |

## Use it

Add ScrapingBee from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.scrapingbee.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Ask ChatGPT | `askChatgpt` | Sends a prompt to ChatGPT (optionally with live web search enabled) and returns its response, without you needing an OpenAI account or API key. |
| Ask Gemini | `askGemini` | Sends a prompt to Google Gemini and returns its response, without you needing a Google AI API key. |
| Extract Structured Data | `extractStructuredData` | Scrapes a webpage and extracts structured data from it using CSS-selector extraction rules (extract_rules) and/or AI-powered extraction (ai_query/ai_extract_rules), returning clean JSON instead of raw HTML. Uses the same underlying scrape endpoint as Scrape Webpage but is a distinct use case since the response shape is structured JSON, not a page body. |
| Fast Search | `fastSearch` | Runs a lightweight, sub-second search and returns results - a faster, cheaper alternative to Search Google for use cases that don't need the full richness of a Google SERP scrape. |
| Find Employees (Agentic Search) | `findEmployeesAgenticSearch` | Runs an AI agent that searches the web for people/employees matching a natural-language description (role, seniority, company, location, etc.) and returns matching candidate profiles. Very high cost per call (3,750 credits) - budget carefully before use. |
| Get Account Usage | `getAccountUsage` | Returns the connected ScrapingBee account's current API credit usage and concurrency limits - total monthly credits, credits used so far, max concurrent requests, and current concurrent requests. Free to call - does not consume any API credits. |
| Get Amazon Pricing | `getAmazonPricing` | Fetches the full list of current offers for an Amazon product by ASIN - every seller, condition, price, and delivery option on the offer-listing page - useful for price comparison and buy-box monitoring. |
| Get Amazon Product | `getAmazonProduct` | Fetches structured details for a single Amazon product page by ASIN - title, price, rating, images, description, variants - without you writing an Amazon-specific scraper. |
| Get Walmart Product | `getWalmartProduct` | Fetches structured details for a single Walmart product page by product ID - title, price, rating, images, description, availability - without you writing a Walmart-specific scraper. |
| Get YouTube Metadata | `getYoutubeMetadata` | Fetches structured metadata for a single YouTube video by video ID - title, description, channel, view/comment counts, category, upload date - without calling the official YouTube Data API. |

<details>

<summary>See 7 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get YouTube Subtitles | `getYoutubeSubtitles` | Fetches the closed-caption/subtitle track for a YouTube video by video ID, including auto-generated captions, with per-line timing. |
| Scrape Webpage | `scrapeWebpage` | Fetches a webpage through ScrapingBee's proxy/headless-browser infrastructure and returns the rendered HTML (or text/markdown/screenshot variants via flags). Supports JavaScript rendering, premium/stealth residential proxies, geolocation, custom cookies, header forwarding, and JS interaction scenarios to avoid bot detection. |
| Search Amazon Products | `searchAmazonProducts` | Searches Amazon for products matching a keyword query and returns structured search-result listings (title, price, rating, ASIN, image) across one or more result pages. |
| Search Google | `searchGoogle` | Runs a Google search and returns structured results - organic results, ads, knowledge graph, local results, news, images, and related queries - without you having to scrape and parse Google's HTML yourself. |
| Search Walmart Products | `searchWalmartProducts` | Searches Walmart.com for products matching a keyword query and returns structured search-result listings with pricing, ratings, and fulfillment/delivery options. |
| Search YouTube | `searchYoutube` | Searches YouTube for videos, channels, playlists, or movies matching a keyword query, with rich filters for quality, duration, upload date, and content type. |
| Take Screenshot | `takeScreenshot` | Renders a webpage and captures a screenshot of it as a base64-encoded image, optionally full-page or scoped to one element via a CSS selector. Uses the same scrape endpoint with screenshot=true and json_response=true so the image comes back as base64 JSON rather than a raw binary body. |

</details>
