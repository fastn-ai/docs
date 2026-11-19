---
description: "Coinlayer by APILayer delivers real-time and historical cryptocurrency exchange rate data for 385+ cryptocurrencies, sourced from 25+ exchanges."
hidden: true
---

# Coinlayer

<img src="../../.gitbook/assets/connectors/lg/coinlayer.png" alt="Coinlayer logo">

Coinlayer by APILayer delivers real-time and historical cryptocurrency exchange rate data for 385+ cryptocurrencies, sourced from 25+ exchanges. Endpoints cover the list of supported currencies, live rates, historical rates by date, currency conversion, time-series (time-frame) rates, and change (fluctuation) data.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [coinlayer.com](https://coinlayer.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `coinlayer` |

## Use it

Add Coinlayer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.coinlayer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Convert Currency Amount</td><td><code>convertCurrencyAmount</code></td><td>Converts an amount from one currency to another using the latest rate, or a historical date's rate if specified. Conversion is listed as a paid-plan-only feature on Coinlayer's plan comparison table, in which case the API returns a paid-plan-required error.</td></tr><tr><td>Get Currency Fluctuation Data</td><td><code>getCurrencyFluctuationData</code></td><td>Returns how cryptocurrency exchange rates changed (absolute and percentage change) between two dates for all or selected symbols. Change is listed as a paid-plan-only feature on Coinlayer's plan comparison table, in which case the API returns a paid-plan-required error.</td></tr><tr><td>Get Historical Exchange Rates</td><td><code>getHistoricalExchangeRates</code></td><td>Returns cryptocurrency exchange rates for a specific past date, optionally filtered to specific symbols and quoted against a target fiat currency, with an option to include expanded market data.</td></tr><tr><td>Get Live Exchange Rates</td><td><code>getLiveExchangeRates</code></td><td>Returns the most recent cryptocurrency exchange rates, optionally filtered to specific symbols and quoted against a target fiat currency, with an option to include expanded market data (high, low, volume, market cap, supply).</td></tr><tr><td>Get Supported Currencies List</td><td><code>getSupportedCurrenciesList</code></td><td>Returns metadata for every cryptocurrency Coinlayer supports (symbol, name, max supply, icon URL) along with the list of supported fiat target currencies. Use the returned symbols as values for the symbols and target parameters on the other endpoints.</td></tr><tr><td>Get Time-Frame Exchange Rates</td><td><code>getTimeFrameExchangeRates</code></td><td>Returns daily historical exchange rates for all or selected cryptocurrencies between two dates. Time-Frame is listed as a paid-plan-only feature on Coinlayer's plan comparison table, in which case the API returns a paid-plan-required error.</td></tr></tbody></table>
