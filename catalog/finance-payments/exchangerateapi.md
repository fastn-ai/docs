---
description: "ExchangeRate-API provides currency exchange rates. Get latest and historical rates, convert currency pairs and list supported currencies."
hidden: true
---

# ExchangeRate-API

<img src="../../.gitbook/assets/connectors/lg/exchangerateapi.png" alt="ExchangeRate-API logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [exchangerate-api.com](https://exchangerate-api.com) |
| **Authentication** | API key |
| **Slug** | `exchangerateapi` |

## Setup

Your customers enter their API key for ExchangeRate-API when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect ExchangeRate-API from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **ExchangeRate-API**.
2. Select **Connect** on the ExchangeRate-API card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use ExchangeRate-API's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Convert Currency Pair</td><td><code>convertCurrencyPair</code></td><td>Returns the current exchange rate between two specific currencies, given a base currency code and a target currency code.</td></tr><tr><td>Convert Currency Pair With Amount</td><td><code>convertCurrencyPairWithAmount</code></td><td>Converts a specific amount from one currency to another using the current exchange rate, given a base currency code, a target currency code, and the amount to convert.</td></tr><tr><td>Get API Request Quota</td><td><code>getRequestQuota</code></td><td>Returns the account's monthly request quota, the number of requests remaining in the current billing period, and the day of month the quota resets. Note that calling this endpoint itself counts against the quota, and the counter may lag actual usage by 5-60 minutes.</td></tr><tr><td>Get Enriched Exchange Rate Data</td><td><code>getEnrichedRateData</code></td><td>Returns the exchange rate between two currencies together with localization metadata for the target currency (display name, symbol, region, and flag image). Requires a Business or Volume plan; returns a plan-upgrade-required error on lower plans.</td></tr><tr><td>Get Historical Exchange Rates</td><td><code>getHistoricalRates</code></td><td>Returns exchange rates from a base currency to every supported currency for a specific past date. Requires a Pro, Business, or Volume plan; returns a plan-upgrade-required error on lower plans. Full currency coverage is available from 1 January 2021 onward; dates from 1990-2020 return a limited 35-currency subset.</td></tr><tr><td>Get Historical Exchange Rates With Amount</td><td><code>getHistoricalRatesWithAmount</code></td><td>Returns historical converted amounts from a base currency to every supported currency for a specific past date, given an amount in the base currency. Requires a Pro, Business, or Volume plan; returns a plan-upgrade-required error on lower plans.</td></tr><tr><td>Get Latest Exchange Rates</td><td><code>getLatestRates</code></td><td>Returns the latest exchange rates from a given base currency to every currency supported by ExchangeRate-API. Rates refresh once every 24 hours.</td></tr><tr><td>List Supported Currency Codes</td><td><code>listSupportedCodes</code></td><td>Returns every ISO 4217 currency code and full currency name supported by ExchangeRate-API, useful for validating or populating currency-selection inputs.</td></tr></tbody></table>

