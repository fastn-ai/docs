---
description: "Frankfurter is a free, keyless, open-source exchange rates API with daily mid-market rates for 200+ currencies from central banks and official sources,…"
hidden: true
---

# Frankfurter

<img src="../../.gitbook/assets/connectors/frankfurter.png" alt="Frankfurter logo" width="64">

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

| Action | Slug | What it does |
| --- | --- | --- |
| Get Currency | `getCurrency` | Returns details and provider coverage of a single currency. Docs: https://frankfurter.dev |
| Get Exchange Rate Pair | `getRate` | Returns the exchange rate of one currency pair, latest or for a given date. Docs: https://frankfurter.dev |
| Get Exchange Rates | `getRates` | Returns exchange rates: the latest rates by default, rates for one date (date), or a time series (from/to, optionally grouped by week or month), for a base currency and selected quote currencies. Docs: https://frankfurter.dev |
| Get Provider | `getProvider` | Returns details of one data provider. Docs: https://frankfurter.dev |
| Get Provider Exchange Rate Pair | `getProviderRate` | Returns one currency pair rate from a specific provider, latest or for a date. Docs: https://frankfurter.dev |
| Get Provider Exchange Rates | `getProviderRates` | Returns exchange rates published by one specific provider (official reference rates), latest, for a date, or as a time series. Docs: https://frankfurter.dev |
| Get Rate Coverage | `getCoverage` | Returns the date ranges for which rates can be queried, per currency and provider. Docs: https://frankfurter.dev |
| List Currencies | `listCurrencies` | Returns the available currencies with their names and provider coverage; scope=all adds legacy currencies. Docs: https://frankfurter.dev |
| List Providers | `listProviders` | Returns the central banks and official sources (providers) behind the rates. Docs: https://frankfurter.dev |
