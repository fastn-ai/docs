---
description: "CoinMarketCal is a calendar of cryptocurrency events. List and look up events, coins and event categories."
hidden: true
---

# CoinMarketCal

<img src="../../.gitbook/assets/connectors/lg/coin-market-cal.png" alt="CoinMarketCal logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [coinmarketcal.com](https://coinmarketcal.com) |
| **Authentication** | API key |
| **Slug** | `coinMarketCal` |

## Setup

Your customers enter their API key for CoinMarketCal when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect CoinMarketCal from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **CoinMarketCal**.
2. Select **Connect** on the CoinMarketCal card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use CoinMarketCal's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get API Usage</td><td><code>getApiUsage</code></td><td>Returns the current billing period's API usage for the connected key: the plan tier, requests made, monthly quota, requests remaining and when the quota resets.</td></tr><tr><td>Get Coin</td><td><code>getCoin</code></td><td>Returns a single cryptocurrency from the CoinMarketCal directory by its slug, including ticker symbol, market-cap rank, icon and upcoming event counts.</td></tr><tr><td>Get Event</td><td><code>getEvent</code></td><td>Returns a single CoinMarketCal event by its numeric id, including its title, dates, related coins, source links and impact fields.</td></tr><tr><td>List Coins</td><td><code>listCoins</code></td><td>Returns the directory of cryptocurrencies CoinMarketCal tracks, with slug, ticker symbol, market-cap rank, icon and upcoming event counts. Supports a text search and cursor pagination, and is the source of the coin slugs accepted by the List Events coins filter.</td></tr><tr><td>List Event Categories</td><td><code>listEventCategories</code></td><td>Returns the event categories CoinMarketCal classifies events into, such as exchange listings, hard forks and token unlocks. The returned ids are the values accepted by the categories filter on List Events. This endpoint requires a Standard plan or above; Free-plan keys receive HTTP 403.</td></tr><tr><td>List Events</td><td><code>listEvents</code></td><td>Returns the CoinMarketCal event feed - upcoming and past crypto events such as listings, hard forks, token unlocks, airdrops and community calls. Results can be narrowed by coin, category, date range and minimum impact, sorted, and paged through with the cursor returned in meta. The categories filter requires a Standard plan or above and impactMin requires an Elite plan or above.</td></tr></tbody></table>

