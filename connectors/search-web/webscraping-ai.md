---
description: "WebScraping.AI is a web scraping API with rotating datacenter, residential and stealth proxies and headless Chromium rendering."
hidden: true
---

# WebScraping.AI

<img src="../../.gitbook/assets/connectors/webscraping-ai.png" alt="WebScraping.AI logo" width="64">

WebScraping.AI is a web scraping API with rotating datacenter, residential and stealth proxies and headless Chromium rendering. This connector covers the full WebScraping.AI API: page HTML, page text as Markdown, HTML of selected page areas by CSS selector, LLM answers to questions about a page, LLM extraction of structured fields, Google search results and account quota.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [webscraping.ai](https://webscraping.ai) |
| **Authentication** | Credentials you enter |
| **Slug** | `webscrapingAi` |

## Use it

Add WebScraping.AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.webscrapingAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Ask Question About Page | `askQuestionAboutPage` | Fetches a web page through WebScraping.AI's proxies and headless browser, then uses an LLM to answer a question or follow instructions about the page content and returns the answer as text. Consumes API credits. |
| Extract Page Fields | `extractPageFields` | Fetches a web page through WebScraping.AI's proxies and headless browser, then uses an LLM to extract the structured fields you describe (for example a product title, price and description) and returns them as a JSON object. Consumes API credits. |
| Get Account | `getAccount` | Returns the account's remaining API call and credit quotas, the time the monthly quota resets and the remaining concurrency. Does not consume credits. |
| Get Multiple Selected HTML | `getMultipleSelectedHtml` | Fetches a web page and returns the HTML of every element matching the given CSS selectors, rendered through WebScraping.AI's proxies and headless browser. The response is a JSON array of arrays of matched element HTML. Consumes API credits. |
| Get Page HTML | `getPageHtml` | Fetches a web page through WebScraping.AI's proxies and, by default, a headless Chromium browser, and returns the rendered page HTML. Optionally runs custom JavaScript on the page and returns its result instead. Consumes API credits (more for residential or stealth proxies). |
| Get Page Text | `getPageText` | Fetches a web page through WebScraping.AI's proxies and headless browser and returns its title, description and body content converted to Markdown, optionally with the links found in the body. Consumes API credits. |
| Get Selected HTML | `getSelectedHtml` | Fetches a web page and returns the HTML of the first element matching a CSS selector (or the whole page when no selector is given), rendered through WebScraping.AI's proxies and headless browser. Consumes API credits. |
| Search Web | `searchWeb` | Runs a search query on a search engine (currently Google) and returns the parsed organic results with pagination, handling proxy routing and result parsing. Consumes API credits. |
