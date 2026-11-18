---
description: "AbstractAPI Exchange Rates returns the latest exchange rates for 80+ fiat and crypto currencies, converts an arbitrary amount between two currencies, and…"
hidden: true
---

# AbstractAPI Exchange Rates

<img src="../../.gitbook/assets/connectors/lg/abstract-api-exchange-rates.png" alt="AbstractAPI Exchange Rates logo">

AbstractAPI Exchange Rates returns the latest exchange rates for 80+ fiat and crypto currencies, converts an arbitrary amount between two currencies, and looks up historical rates for a given date.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `abstractApiExchangeRates` |

## Use it

Add AbstractAPI Exchange Rates from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiExchangeRates.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert Currency | `convertCurrency` | Converts an amount from a base currency into a single target currency at the latest rate, or at the rate of a given historical date, and returns the converted amount and the rate used. |
| Get Historical Exchange Rates | `getHistoricalExchangeRates` | Returns the exchange rates from a base currency to one or more target currencies on a specific past date. AbstractAPI documents this endpoint as a closed beta, so it may not be enabled on every account. |
| Get Live Exchange Rates | `getLiveExchangeRates` | Returns the most recent exchange rates from a base currency to one or more target currencies. If no target is given, rates for every supported currency are returned. |
