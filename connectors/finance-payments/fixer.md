---
description: "Fixer is a reliable, lightweight foreign exchange rates and currency conversion API by APILayer."
hidden: true
---

# Fixer

<img src="../../.gitbook/assets/connectors/lg/fixer.png" alt="Fixer logo">

Fixer is a reliable, lightweight foreign exchange rates and currency conversion API by APILayer. It delivers JSON-formatted real-time and historical exchange rate data for 170+ world currencies, aggregated from 15+ trusted financial sources, plus currency conversion, time-series, and fluctuation endpoints.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [fixer.io](https://fixer.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `fixer` |

## Use it

Add Fixer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fixer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Convert Currency Amount</td><td><code>convertCurrencyAmount</code></td><td>Converts an amount from one currency to another, optionally using a historical date's rate. Currency conversion is listed as excluded from the Fixer free plan, in which case the API returns a paid-plan-required error.</td></tr><tr><td>Get Currency Fluctuation Data</td><td><code>getCurrencyFluctuationData</code></td><td>Returns how exchange rates fluctuated (change and change percentage) between two dates for all or selected currencies. Fluctuation is listed as excluded from the Fixer free plan, in which case the API returns a paid-plan-required error.</td></tr><tr><td>Get Historical Exchange Rates</td><td><code>getHistoricalExchangeRates</code></td><td>Returns exchange rates for all or selected currencies on a specific past date. Historical rates may not be included on the Fixer free plan, in which case the API returns a paid-plan-required error.</td></tr><tr><td>Get Latest Exchange Rates</td><td><code>getLatestExchangeRates</code></td><td>Returns the most recent exchange rates for all or selected currencies. On the Fixer free plan the base currency is restricted to EUR; requesting any other base returns a paid-plan-required error.</td></tr><tr><td>Get Supported Currency Symbols</td><td><code>getSupportedCurrencySymbols</code></td><td>Returns the full list of currency codes and names that Fixer supports, for use as base or symbols values on the other endpoints.</td></tr><tr><td>Get Time-Series Exchange Rates</td><td><code>getTimeSeriesExchangeRates</code></td><td>Returns daily historical exchange rates for all or selected currencies between two dates. Time-Series is listed as excluded from the Fixer free plan, in which case the API returns a paid-plan-required error.</td></tr></tbody></table>
