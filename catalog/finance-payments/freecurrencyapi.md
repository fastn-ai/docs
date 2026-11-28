---
description: "FreeCurrencyAPI provides foreign exchange rates. Get latest and historical rates and list supported currencies."
hidden: true
---

# FreeCurrencyAPI

<img src="../../.gitbook/assets/connectors/lg/freecurrencyapi.png" alt="FreeCurrencyAPI logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [freecurrencyapi.com](https://freecurrencyapi.com) |
| **Authentication** | API key |
| **Slug** | `freecurrencyapi` |

## Setup

Your customers enter their API key for FreeCurrencyAPI when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect FreeCurrencyAPI from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **FreeCurrencyAPI**.
2. Select **Connect** on the FreeCurrencyAPI card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use FreeCurrencyAPI's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Account Status</td><td><code>getAccountStatus</code></td><td>Returns the account ID and current monthly quota usage for the connected API key. Calling this action does not count against the quota.</td></tr><tr><td>Get Historical Exchange Rates</td><td><code>getHistoricalRates</code></td><td>Returns foreign-exchange rates for a single past date. Requesting a date range is a paid currencyapi.com feature and is not available on this free-tier API.</td></tr><tr><td>Get Latest Exchange Rates</td><td><code>getLatestRates</code></td><td>Returns the latest foreign-exchange rates for a base currency, optionally limited to a specific list of currency codes.</td></tr><tr><td>List Supported Currencies</td><td><code>listCurrencies</code></td><td>Returns metadata (symbol, name, decimal digits, and type) for the currencies supported by the API, optionally filtered to a specific list of currency codes.</td></tr></tbody></table>

