---
description: "Currencylayer is a reliable, lightweight foreign exchange rates and currency data API by APILayer."
---

# Currencylayer

Currencylayer is a reliable, lightweight foreign exchange rates and currency data API by APILayer. It delivers JSON-formatted real-time and End-of-Day historical exchange rate data for 168 world currencies and precious metals, plus single-currency conversion, time-frame, and currency-change endpoints.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [currencylayer.com](https://currencylayer.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 6 |
| **Events** | 0 |
| **Slug** | `currencylayer` |

## Use it

Add Currencylayer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.currencylayer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert Currency Amount | `convertCurrencyAmount` | Converts an amount from one currency to another using the latest exchange rate, or a historical rate if a date is supplied. Currencylayer documents Currency Conversion as a paid-plan feature on some subscription tiers; it returned a genuine 2xx response with a real converted amount when tested against the connected account. |
| Get Currency Change Data | `getCurrencyChangeData` | Returns the margin and percentage change of one or more currencies relative to a source currency over a time-frame. If no start_date/end_date is supplied, the change is calculated from yesterday's End-of-Day data to the latest available rates. Currencylayer documents Currency-Change Queries as an Enterprise-only feature; it returned a genuine 2xx response with real change data when tested against the connected account. |
| Get Historical Exchange Rates | `getHistoricalExchangeRates` | Returns accurate End-of-Day exchange rate data for a specific past date, for all or a selected set of currencies. Historical Rates go back up to 16 years and are included on the Free plan; note that some currencies (e.g. Bitcoin) have no data before their introduction date. |
| Get Live Exchange Rates | `getLiveExchangeRates` | Returns the most recent exchange rate data for all, or a selected set, of the 168 world currencies Currencylayer supports, quoted against a source currency (USD by default). Live Rates are included on the Free plan. |
| Get Supported Currencies | `getSupportedCurrencies` | Returns the full list of the 168 currency codes and full currency names that Currencylayer supports, for use as source or currencies values on the other endpoints. |
| Get Timeframe Exchange Rates | `getTimeframeExchangeRates` | Returns daily historical exchange rates for every day within a date range of up to 365 days, for all or a selected set of currencies. Currencylayer documents Time-Frame Queries as a Professional/Enterprise-only feature; it returned a genuine 2xx response with real per-day rate data when tested against the connected account. |
