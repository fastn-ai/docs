---
description: "Fixer is a reliable, lightweight foreign exchange rates and currency conversion API by APILayer."
hidden: true
---

# Fixer

Fixer is a reliable, lightweight foreign exchange rates and currency conversion API by APILayer. It delivers JSON-formatted real-time and historical exchange rate data for 170+ world currencies, aggregated from 15+ trusted financial sources, plus currency conversion, time-series, and fluctuation endpoints.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [fixer.io](https://fixer.io) |
| **Authentication** | Credentials you enter |
| **Actions** | 6 |
| **Events** | 0 |
| **Slug** | `fixer` |

## Use it

Add Fixer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fixer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert Currency Amount | `convertCurrencyAmount` | Converts an amount from one currency to another, optionally using a historical date's rate. Currency conversion is listed as excluded from the Fixer free plan, in which case the API returns a paid-plan-required error. |
| Get Currency Fluctuation Data | `getCurrencyFluctuationData` | Returns how exchange rates fluctuated (change and change percentage) between two dates for all or selected currencies. Fluctuation is listed as excluded from the Fixer free plan, in which case the API returns a paid-plan-required error. |
| Get Historical Exchange Rates | `getHistoricalExchangeRates` | Returns exchange rates for all or selected currencies on a specific past date. Historical rates may not be included on the Fixer free plan, in which case the API returns a paid-plan-required error. |
| Get Latest Exchange Rates | `getLatestExchangeRates` | Returns the most recent exchange rates for all or selected currencies. On the Fixer free plan the base currency is restricted to EUR; requesting any other base returns a paid-plan-required error. |
| Get Supported Currency Symbols | `getSupportedCurrencySymbols` | Returns the full list of currency codes and names that Fixer supports, for use as base or symbols values on the other endpoints. |
| Get Time-Series Exchange Rates | `getTimeSeriesExchangeRates` | Returns daily historical exchange rates for all or selected currencies between two dates. Time-Series is listed as excluded from the Fixer free plan, in which case the API returns a paid-plan-required error. |
