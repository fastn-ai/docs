---
description: "Frankfurter is a free exchange rates service using central bank data. Get exchange rates, currency pairs and supported currencies."
hidden: true
---

# Frankfurter

<img src="../../.gitbook/assets/connectors/lg/frankfurter.png" alt="Frankfurter logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [frankfurter.dev](https://frankfurter.dev) |
| **Authentication** | No sign-in needed |
| **Slug** | `frankfurter` |

## Setup

Frankfurter needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Frankfurter from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Frankfurter**.
2. Select **Connect** on the Frankfurter card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Frankfurter needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Frankfurter's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Currency</td><td><code>getCurrency</code></td><td>Returns details and provider coverage of a single currency. Docs: https://frankfurter.dev</td></tr><tr><td>Get Exchange Rate Pair</td><td><code>getRate</code></td><td>Returns the exchange rate of one currency pair, latest or for a given date. Docs: https://frankfurter.dev</td></tr><tr><td>Get Exchange Rates</td><td><code>getRates</code></td><td>Returns exchange rates: the latest rates by default, rates for one date (date), or a time series (from/to, optionally grouped by week or month), for a base currency and selected quote currencies. Docs: https://frankfurter.dev</td></tr><tr><td>Get Provider</td><td><code>getProvider</code></td><td>Returns details of one data provider. Docs: https://frankfurter.dev</td></tr><tr><td>Get Provider Exchange Rate Pair</td><td><code>getProviderRate</code></td><td>Returns one currency pair rate from a specific provider, latest or for a date. Docs: https://frankfurter.dev</td></tr><tr><td>Get Provider Exchange Rates</td><td><code>getProviderRates</code></td><td>Returns exchange rates published by one specific provider (official reference rates), latest, for a date, or as a time series. Docs: https://frankfurter.dev</td></tr><tr><td>Get Rate Coverage</td><td><code>getCoverage</code></td><td>Returns the date ranges for which rates can be queried, per currency and provider. Docs: https://frankfurter.dev</td></tr><tr><td>List Currencies</td><td><code>listCurrencies</code></td><td>Returns the available currencies with their names and provider coverage; scope=all adds legacy currencies. Docs: https://frankfurter.dev</td></tr><tr><td>List Providers</td><td><code>listProviders</code></td><td>Returns the central banks and official sources (providers) behind the rates. Docs: https://frankfurter.dev</td></tr></tbody></table>

