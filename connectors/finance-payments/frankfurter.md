---
description: "Frankfurter is a free, keyless, open-source exchange rates API with daily mid-market rates for 200+ currencies from central banks and official sources,…"
hidden: true
---

# Frankfurter

<img src="../../.gitbook/assets/connectors/lg/frankfurter.png" alt="Frankfurter logo">

Frankfurter is a free, keyless, open-source exchange rates API with daily mid-market rates for 200+ currencies from central banks and official sources, history back to 1948, single currency pairs, time series and per-provider rates (API v2).

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [frankfurter.dev](https://frankfurter.dev) |
| **Authentication** | No authentication |
| **Slug** | `frankfurter` |

## Use it

Add Frankfurter from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.frankfurter.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Currency</td><td><code>getCurrency</code></td><td>Returns details and provider coverage of a single currency. Docs: https://frankfurter.dev</td></tr><tr><td>Get Exchange Rate Pair</td><td><code>getRate</code></td><td>Returns the exchange rate of one currency pair, latest or for a given date. Docs: https://frankfurter.dev</td></tr><tr><td>Get Exchange Rates</td><td><code>getRates</code></td><td>Returns exchange rates: the latest rates by default, rates for one date (date), or a time series (from/to, optionally grouped by week or month), for a base currency and selected quote currencies. Docs: https://frankfurter.dev</td></tr><tr><td>Get Provider</td><td><code>getProvider</code></td><td>Returns details of one data provider. Docs: https://frankfurter.dev</td></tr><tr><td>Get Provider Exchange Rate Pair</td><td><code>getProviderRate</code></td><td>Returns one currency pair rate from a specific provider, latest or for a date. Docs: https://frankfurter.dev</td></tr><tr><td>Get Provider Exchange Rates</td><td><code>getProviderRates</code></td><td>Returns exchange rates published by one specific provider (official reference rates), latest, for a date, or as a time series. Docs: https://frankfurter.dev</td></tr><tr><td>Get Rate Coverage</td><td><code>getCoverage</code></td><td>Returns the date ranges for which rates can be queried, per currency and provider. Docs: https://frankfurter.dev</td></tr><tr><td>List Currencies</td><td><code>listCurrencies</code></td><td>Returns the available currencies with their names and provider coverage; scope=all adds legacy currencies. Docs: https://frankfurter.dev</td></tr><tr><td>List Providers</td><td><code>listProviders</code></td><td>Returns the central banks and official sources (providers) behind the rates. Docs: https://frankfurter.dev</td></tr></tbody></table>
