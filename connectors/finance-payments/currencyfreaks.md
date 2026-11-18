---
description: "CurrencyFreaks provides real-time and historical foreign exchange rates and currency conversion for over 1,000 world currencies and metals, plus IP-based…"
hidden: true
---

# CurrencyFreaks

<img src="../../.gitbook/assets/connectors/currencyfreaks.png" alt="CurrencyFreaks logo" width="64">

CurrencyFreaks provides real-time and historical foreign exchange rates and currency conversion for over 1,000 world currencies and metals, plus IP-based local currency lookup. Sister brand to ipgeolocation.io and WhoisFreaks.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [currencyfreaks.com](https://currencyfreaks.com) |
| **Authentication** | API key |
| **Slug** | `currencyfreaks` |

## Use it

Add CurrencyFreaks from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.currencyfreaks.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert Currency | `convertCurrency` | Converts an amount from one currency to another using the latest exchange rates. This endpoint is available on paid plans only. |
| Convert Currency Historical | `convertCurrencyHistorical` | Converts an amount from one currency to another using the exchange rate on a specific past date. This endpoint is available on paid plans only. |
| Get Currency By IP Address | `getCurrencyByIp` | Looks up the local currency for an IP address's geographic location and converts a given amount from a source currency into that local currency. Uses the caller's IP if none is supplied. This endpoint requires a Growth plan or higher. |
| Get Currency Fluctuation | `getCurrencyFluctuation` | Returns how currencies fluctuate day-to-day over a date range, relative to a base currency. This endpoint requires a Professional plan or higher. |
| Get Historical Data Limits | `getHistoricalDataLimits` | Returns the availability period (earliest and latest dates) for historical exchange rate data, broken down by currency. No API key is required for this endpoint. |
| Get Historical Exchange Rates | `getHistoricalExchangeRates` | Returns exchange rates for a specific past date, relative to a base currency. Historical data is available for most currencies back to 1984-11-28. This endpoint is available on paid plans only. |
| Get Latest Exchange Rates | `getLatestExchangeRates` | Returns the latest exchange rates for all or a filtered set of currencies, relative to a base currency (USD by default). Available on all plans. |
| Get Time Series Rates | `getTimeSeriesRates` | Returns daily historical exchange rates between two dates, relative to a base currency. This endpoint requires a Professional plan or higher. |
| List Currency Symbols | `listCurrencySymbols` | Returns the currency codes and full names of all currencies available in CurrencyFreaks. No API key is required for this endpoint. |
| List Supported Currencies | `listSupportedCurrencies` | Returns the complete list of currencies supported by CurrencyFreaks, including each currency's code, full name, country, and icon. No API key is required for this endpoint. |
