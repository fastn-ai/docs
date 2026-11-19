---
description: "Free current and historical foreign-exchange rates from freecurrencyapi.com (the free tier of currencyapi.com)."
hidden: true
---

# FreeCurrencyAPI

<img src="../../.gitbook/assets/connectors/lg/freecurrencyapi.png" alt="FreeCurrencyAPI logo">

Free current and historical foreign-exchange rates from freecurrencyapi.com (the free tier of currencyapi.com). Covers the latest exchange rates, single-date historical rates, supported currency metadata, and account quota status. Authenticates with an API key sent as the 'apikey' request header. Base https://api.freecurrencyapi.com.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [freecurrencyapi.com](https://freecurrencyapi.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `freecurrencyapi` |

## Use it

Add FreeCurrencyAPI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.freecurrencyapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Account Status</td><td><code>getAccountStatus</code></td><td>Returns the account ID and current monthly quota usage for the connected API key. Calling this action does not count against the quota.</td></tr><tr><td>Get Historical Exchange Rates</td><td><code>getHistoricalRates</code></td><td>Returns foreign-exchange rates for a single past date. Requesting a date range is a paid currencyapi.com feature and is not available on this free-tier API.</td></tr><tr><td>Get Latest Exchange Rates</td><td><code>getLatestRates</code></td><td>Returns the latest foreign-exchange rates for a base currency, optionally limited to a specific list of currency codes.</td></tr><tr><td>List Supported Currencies</td><td><code>listCurrencies</code></td><td>Returns metadata (symbol, name, decimal digits, and type) for the currencies supported by the API, optionally filtered to a specific list of currency codes.</td></tr></tbody></table>
