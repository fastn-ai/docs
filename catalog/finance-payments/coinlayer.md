---
description: "Coinlayer provides cryptocurrency exchange rates. Get live and historical rates, convert amounts and track rate changes."
hidden: true
---

# Coinlayer

<img src="../../.gitbook/assets/connectors/lg/coinlayer.png" alt="Coinlayer logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [coinlayer.com](https://coinlayer.com) |
| **Authentication** | API key |
| **Slug** | `coinlayer` |

## Setup

Your customers enter their API key for Coinlayer when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Coinlayer from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Coinlayer**.
2. Select **Connect** on the Coinlayer card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Coinlayer's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Convert Currency Amount</td><td><code>convertCurrencyAmount</code></td><td>Converts an amount from one currency to another using the latest rate, or a historical date's rate if specified. Conversion is listed as a paid-plan-only feature on Coinlayer's plan comparison table, in which case the API returns a paid-plan-required error.</td></tr><tr><td>Get Currency Fluctuation Data</td><td><code>getCurrencyFluctuationData</code></td><td>Returns how cryptocurrency exchange rates changed (absolute and percentage change) between two dates for all or selected symbols. Change is listed as a paid-plan-only feature on Coinlayer's plan comparison table, in which case the API returns a paid-plan-required error.</td></tr><tr><td>Get Historical Exchange Rates</td><td><code>getHistoricalExchangeRates</code></td><td>Returns cryptocurrency exchange rates for a specific past date, optionally filtered to specific symbols and quoted against a target fiat currency, with an option to include expanded market data.</td></tr><tr><td>Get Live Exchange Rates</td><td><code>getLiveExchangeRates</code></td><td>Returns the most recent cryptocurrency exchange rates, optionally filtered to specific symbols and quoted against a target fiat currency, with an option to include expanded market data (high, low, volume, market cap, supply).</td></tr><tr><td>Get Supported Currencies List</td><td><code>getSupportedCurrenciesList</code></td><td>Returns metadata for every cryptocurrency Coinlayer supports (symbol, name, max supply, icon URL) along with the list of supported fiat target currencies. Use the returned symbols as values for the symbols and target parameters on the other endpoints.</td></tr><tr><td>Get Time-Frame Exchange Rates</td><td><code>getTimeFrameExchangeRates</code></td><td>Returns daily historical exchange rates for all or selected cryptocurrencies between two dates. Time-Frame is listed as a paid-plan-only feature on Coinlayer's plan comparison table, in which case the API returns a paid-plan-required error.</td></tr></tbody></table>

