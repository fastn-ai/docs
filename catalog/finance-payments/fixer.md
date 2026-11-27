---
description: "Fixer provides foreign exchange rates. Get latest, historical and time-series rates and convert amounts between currencies."
hidden: true
---

# Fixer

<img src="../../.gitbook/assets/connectors/lg/fixer.png" alt="Fixer logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [fixer.io](https://fixer.io) |
| **Authentication** | API key |
| **Slug** | `fixer` |

## Setup

Your customers enter their API key for Fixer when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Fixer from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Fixer**.
2. Select **Connect** on the Fixer card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Fixer's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Convert Currency Amount</td><td><code>convertCurrencyAmount</code></td><td>Converts an amount from one currency to another, optionally using a historical date's rate. Currency conversion is listed as excluded from the Fixer free plan, in which case the API returns a paid-plan-required error.</td></tr><tr><td>Get Currency Fluctuation Data</td><td><code>getCurrencyFluctuationData</code></td><td>Returns how exchange rates fluctuated (change and change percentage) between two dates for all or selected currencies. Fluctuation is listed as excluded from the Fixer free plan, in which case the API returns a paid-plan-required error.</td></tr><tr><td>Get Historical Exchange Rates</td><td><code>getHistoricalExchangeRates</code></td><td>Returns exchange rates for all or selected currencies on a specific past date. Historical rates may not be included on the Fixer free plan, in which case the API returns a paid-plan-required error.</td></tr><tr><td>Get Latest Exchange Rates</td><td><code>getLatestExchangeRates</code></td><td>Returns the most recent exchange rates for all or selected currencies. On the Fixer free plan the base currency is restricted to EUR; requesting any other base returns a paid-plan-required error.</td></tr><tr><td>Get Supported Currency Symbols</td><td><code>getSupportedCurrencySymbols</code></td><td>Returns the full list of currency codes and names that Fixer supports, for use as base or symbols values on the other endpoints.</td></tr><tr><td>Get Time-Series Exchange Rates</td><td><code>getTimeSeriesExchangeRates</code></td><td>Returns daily historical exchange rates for all or selected currencies between two dates. Time-Series is listed as excluded from the Fixer free plan, in which case the API returns a paid-plan-required error.</td></tr></tbody></table>

