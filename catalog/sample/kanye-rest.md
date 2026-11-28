---
description: "Kanye Rest is a free collection of Kanye West quotes. Get a random quote or list all quotes."
hidden: true
---

# Kanye Rest

<img src="../../.gitbook/assets/connectors/lg/kanye-rest.png" alt="Kanye Rest logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [kanye.rest](https://kanye.rest) |
| **Authentication** | No sign-in needed |
| **Slug** | `kanyeRest` |

## Setup

Kanye Rest needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Kanye Rest from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Kanye Rest**.
2. Select **Connect** on the Kanye Rest card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Kanye Rest needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Kanye Rest's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Random Quote</td><td><code>getRandomQuote</code></td><td>Get one random Kanye West quote as JSON Docs: https://github.com/ajzbc/kanye.rest#usage</td></tr><tr><td>Get Random Quote as Text</td><td><code>getRandomQuoteText</code></td><td>Get one random Kanye West quote as plain text Docs: https://github.com/ajzbc/kanye.rest#usage</td></tr><tr><td>List All Quotes</td><td><code>listQuotes</code></td><td>Get every quote in the collection as a list of strings The vendor notes this response format may change. Docs: https://github.com/ajzbc/kanye.rest#usage</td></tr></tbody></table>

