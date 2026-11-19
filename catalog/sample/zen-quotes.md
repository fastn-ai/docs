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

## Use it

Add ZenQuotes from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zenQuotes.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Quote of the Day</td><td><code>getQuoteOfTheDay</code></td><td>Returns the single quote ZenQuotes features as today's daily inspiration. The same quote is returned all day and refreshes at midnight server time (00:00 CST). No authentication or parameters required.</td></tr><tr><td>Get Random Inspirational Image</td><td><code>getRandomImage</code></td><td>Returns a randomly generated inspirational image (JPEG) featuring a quote, rendered server-side by ZenQuotes. No authentication or parameters required.</td></tr><tr><td>Get Random Quote</td><td><code>getRandomQuote</code></td><td>Returns a single random inspirational quote from the ZenQuotes free public database. No authentication, parameters, or attribution key required; rate-limited to 5 requests per 30 seconds per IP on the free tier.</td></tr><tr><td>Get Random Quotes Batch</td><td><code>getRandomQuotesBatch</code></td><td>Returns a batch of up to 50 random quotes from the ZenQuotes free public database in one call, intended to be cached client-side rather than re-fetched per quote. No authentication or parameters required.</td></tr></tbody></table>

## Events

ZenQuotes has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
