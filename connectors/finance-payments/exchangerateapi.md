---
description: "Currency exchange rate and conversion API (v6) from exchangerate-api.com."
hidden: true
---

# ExchangeRate-API

<img src="../../.gitbook/assets/connectors/exchangerateapi.png" alt="ExchangeRate-API logo" width="64">

Currency exchange rate and conversion API (v6) from exchangerate-api.com. Provides latest exchange rates for a base currency, currency-pair conversion (with optional amount), historical exchange rates by date, enriched currency metadata, the list of supported currency codes, and account request-quota status.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [exchangerate-api.com](https://exchangerate-api.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `exchangerateapi` |

## Use it

Add ExchangeRate-API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.exchangerateapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert Currency Pair | `convertCurrencyPair` | Returns the current exchange rate between two specific currencies, given a base currency code and a target currency code. |
| Convert Currency Pair With Amount | `convertCurrencyPairWithAmount` | Converts a specific amount from one currency to another using the current exchange rate, given a base currency code, a target currency code, and the amount to convert. |
| Get API Request Quota | `getRequestQuota` | Returns the account's monthly request quota, the number of requests remaining in the current billing period, and the day of month the quota resets. Note that calling this endpoint itself counts against the quota, and the counter may lag actual usage by 5-60 minutes. |
| Get Enriched Exchange Rate Data | `getEnrichedRateData` | Returns the exchange rate between two currencies together with localization metadata for the target currency (display name, symbol, region, and flag image). Requires a Business or Volume plan; returns a plan-upgrade-required error on lower plans. |
| Get Historical Exchange Rates | `getHistoricalRates` | Returns exchange rates from a base currency to every supported currency for a specific past date. Requires a Pro, Business, or Volume plan; returns a plan-upgrade-required error on lower plans. Full currency coverage is available from 1 January 2021 onward; dates from 1990-2020 return a limited 35-currency subset. |
| Get Historical Exchange Rates With Amount | `getHistoricalRatesWithAmount` | Returns historical converted amounts from a base currency to every supported currency for a specific past date, given an amount in the base currency. Requires a Pro, Business, or Volume plan; returns a plan-upgrade-required error on lower plans. |
| Get Latest Exchange Rates | `getLatestRates` | Returns the latest exchange rates from a given base currency to every currency supported by ExchangeRate-API. Rates refresh once every 24 hours. |
| List Supported Currency Codes | `listSupportedCodes` | Returns every ISO 4217 currency code and full currency name supported by ExchangeRate-API, useful for validating or populating currency-selection inputs. |
