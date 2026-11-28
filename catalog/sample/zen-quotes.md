---
description: "ZenQuotes is a free quotes service. Get the quote of the day, random quotes and inspirational images."
hidden: true
---

# ZenQuotes

<img src="../../.gitbook/assets/connectors/lg/zen-quotes.png" alt="ZenQuotes logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [zenquotes.io](https://zenquotes.io) |
| **Authentication** | No sign-in needed |
| **Slug** | `zenQuotes` |

## Setup

ZenQuotes needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect ZenQuotes from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **ZenQuotes**.
2. Select **Connect** on the ZenQuotes card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. ZenQuotes needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use ZenQuotes's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Quote of the Day</td><td><code>getQuoteOfTheDay</code></td><td>Returns the single quote ZenQuotes features as today's daily inspiration. The same quote is returned all day and refreshes at midnight server time (00:00 CST). No authentication or parameters required.</td></tr><tr><td>Get Random Inspirational Image</td><td><code>getRandomImage</code></td><td>Returns a randomly generated inspirational image (JPEG) featuring a quote, rendered server-side by ZenQuotes. No authentication or parameters required.</td></tr><tr><td>Get Random Quote</td><td><code>getRandomQuote</code></td><td>Returns a single random inspirational quote from the ZenQuotes free public database. No authentication, parameters, or attribution key required; rate-limited to 5 requests per 30 seconds per IP on the free tier.</td></tr><tr><td>Get Random Quotes Batch</td><td><code>getRandomQuotesBatch</code></td><td>Returns a batch of up to 50 random quotes from the ZenQuotes free public database in one call, intended to be cached client-side rather than re-fetched per quote. No authentication or parameters required.</td></tr></tbody></table>

