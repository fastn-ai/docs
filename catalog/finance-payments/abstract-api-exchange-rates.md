---
description: "AbstractAPI Exchange Rates provides currency exchange rates. Get live and historical rates and convert amounts between currencies."
hidden: true
---

# AbstractAPI Exchange Rates

<img src="../../.gitbook/assets/connectors/lg/abstract-api-exchange-rates.png" alt="AbstractAPI Exchange Rates logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | API key |
| **Slug** | `abstractApiExchangeRates` |

## Setup

Your customers enter their API key for AbstractAPI Exchange Rates when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect AbstractAPI Exchange Rates from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AbstractAPI Exchange Rates**.
2. Select **Connect** on the AbstractAPI Exchange Rates card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AbstractAPI Exchange Rates's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Convert Currency</td><td><code>convertCurrency</code></td><td>Converts an amount from a base currency into a single target currency at the latest rate, or at the rate of a given historical date, and returns the converted amount and the rate used.</td></tr><tr><td>Get Historical Exchange Rates</td><td><code>getHistoricalExchangeRates</code></td><td>Returns the exchange rates from a base currency to one or more target currencies on a specific past date. AbstractAPI documents this endpoint as a closed beta, so it may not be enabled on every account.</td></tr><tr><td>Get Live Exchange Rates</td><td><code>getLiveExchangeRates</code></td><td>Returns the most recent exchange rates from a base currency to one or more target currencies. If no target is given, rates for every supported currency are returned.</td></tr></tbody></table>

