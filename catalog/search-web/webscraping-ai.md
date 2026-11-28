---
description: "WebScraping.AI scrapes web pages. Get page HTML and text, extract fields, ask questions about a page and search the web."
hidden: true
---

# WebScraping.AI

<img src="../../.gitbook/assets/connectors/lg/webscraping-ai.png" alt="WebScraping.AI logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [webscraping.ai](https://webscraping.ai) |
| **Authentication** | API key |
| **Slug** | `webscrapingAi` |

## Setup

Your customers enter their API key for WebScraping.AI when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect WebScraping.AI from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **WebScraping.AI**.
2. Select **Connect** on the WebScraping.AI card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use WebScraping.AI's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Ask Question About Page</td><td><code>askQuestionAboutPage</code></td><td>Fetches a web page through WebScraping.AI's proxies and headless browser, then uses an LLM to answer a question or follow instructions about the page content and returns the answer as text. Consumes API credits.</td></tr><tr><td>Extract Page Fields</td><td><code>extractPageFields</code></td><td>Fetches a web page through WebScraping.AI's proxies and headless browser, then uses an LLM to extract the structured fields you describe (for example a product title, price and description) and returns them as a JSON object. Consumes API credits.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Returns the account's remaining API call and credit quotas, the time the monthly quota resets and the remaining concurrency. Does not consume credits.</td></tr><tr><td>Get Multiple Selected HTML</td><td><code>getMultipleSelectedHtml</code></td><td>Fetches a web page and returns the HTML of every element matching the given CSS selectors, rendered through WebScraping.AI's proxies and headless browser. The response is a JSON array of arrays of matched element HTML. Consumes API credits.</td></tr><tr><td>Get Page HTML</td><td><code>getPageHtml</code></td><td>Fetches a web page through WebScraping.AI's proxies and, by default, a headless Chromium browser, and returns the rendered page HTML. Optionally runs custom JavaScript on the page and returns its result instead. Consumes API credits (more for residential or stealth proxies).</td></tr><tr><td>Get Page Text</td><td><code>getPageText</code></td><td>Fetches a web page through WebScraping.AI's proxies and headless browser and returns its title, description and body content converted to Markdown, optionally with the links found in the body. Consumes API credits.</td></tr><tr><td>Get Selected HTML</td><td><code>getSelectedHtml</code></td><td>Fetches a web page and returns the HTML of the first element matching a CSS selector (or the whole page when no selector is given), rendered through WebScraping.AI's proxies and headless browser. Consumes API credits.</td></tr><tr><td>Search Web</td><td><code>searchWeb</code></td><td>Runs a search query on a search engine (currently Google) and returns the parsed organic results with pagination, handling proxy routing and result parsing. Consumes API credits.</td></tr></tbody></table>

