---
description: "CurrencyFreaks provides foreign exchange rates for world currencies. Get latest and historical rates, convert amounts and look up currency by IP."
hidden: true
---

# CurrencyFreaks

<img src="../../.gitbook/assets/connectors/lg/currencyfreaks.png" alt="CurrencyFreaks logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [currencyfreaks.com](https://currencyfreaks.com) |
| **Authentication** | API key |
| **Slug** | `currencyfreaks` |

## Setup

Your customers enter their API key for CurrencyFreaks when they connect. Nothing else needs setting up.

## Use it

Add CurrencyFreaks from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.currencyfreaks.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Convert Currency</td><td><code>convertCurrency</code></td><td>Converts an amount from one currency to another using the latest exchange rates. This endpoint is available on paid plans only.</td></tr><tr><td>Convert Currency Historical</td><td><code>convertCurrencyHistorical</code></td><td>Converts an amount from one currency to another using the exchange rate on a specific past date. This endpoint is available on paid plans only.</td></tr><tr><td>Get Currency By IP Address</td><td><code>getCurrencyByIp</code></td><td>Looks up the local currency for an IP address's geographic location and converts a given amount from a source currency into that local currency. Uses the caller's IP if none is supplied. This endpoint requires a Growth plan or higher.</td></tr><tr><td>Get Currency Fluctuation</td><td><code>getCurrencyFluctuation</code></td><td>Returns how currencies fluctuate day-to-day over a date range, relative to a base currency. This endpoint requires a Professional plan or higher.</td></tr><tr><td>Get Historical Data Limits</td><td><code>getHistoricalDataLimits</code></td><td>Returns the availability period (earliest and latest dates) for historical exchange rate data, broken down by currency. No API key is required for this endpoint.</td></tr><tr><td>Get Historical Exchange Rates</td><td><code>getHistoricalExchangeRates</code></td><td>Returns exchange rates for a specific past date, relative to a base currency. Historical data is available for most currencies back to 1984-11-28. This endpoint is available on paid plans only.</td></tr><tr><td>Get Latest Exchange Rates</td><td><code>getLatestExchangeRates</code></td><td>Returns the latest exchange rates for all or a filtered set of currencies, relative to a base currency (USD by default). Available on all plans.</td></tr><tr><td>Get Time Series Rates</td><td><code>getTimeSeriesRates</code></td><td>Returns daily historical exchange rates between two dates, relative to a base currency. This endpoint requires a Professional plan or higher.</td></tr><tr><td>List Currency Symbols</td><td><code>listCurrencySymbols</code></td><td>Returns the currency codes and full names of all currencies available in CurrencyFreaks. No API key is required for this endpoint.</td></tr><tr><td>List Supported Currencies</td><td><code>listSupportedCurrencies</code></td><td>Returns the complete list of currencies supported by CurrencyFreaks, including each currency's code, full name, country, and icon. No API key is required for this endpoint.</td></tr></tbody></table>

## Events

CurrencyFreaks has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
