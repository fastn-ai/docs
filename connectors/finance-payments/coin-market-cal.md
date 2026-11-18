---
description: "CoinMarketCal is the leading crypto events calendar, tracking upcoming and historical announcements - listings, hard forks, token unlocks, airdrops, AMAs and…"
hidden: true
---

# CoinMarketCal

<img src="../../.gitbook/assets/connectors/lg/coin-market-cal.png" alt="CoinMarketCal logo">

CoinMarketCal is the leading crypto events calendar, tracking upcoming and historical announcements - listings, hard forks, token unlocks, airdrops, AMAs and more - for thousands of cryptocurrencies. This connector covers the full CoinMarketCal v2 REST API: the event feed with coin, category, date-range, impact and sort filters, single event lookup, the supported coin directory, single coin lookup, the event category list and the API usage and quota endpoint.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [coinmarketcal.com](https://coinmarketcal.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `coinMarketCal` |

## Use it

Add CoinMarketCal from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.coinMarketCal.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get API Usage | `getApiUsage` | Returns the current billing period's API usage for the connected key: the plan tier, requests made, monthly quota, requests remaining and when the quota resets. |
| Get Coin | `getCoin` | Returns a single cryptocurrency from the CoinMarketCal directory by its slug, including ticker symbol, market-cap rank, icon and upcoming event counts. |
| Get Event | `getEvent` | Returns a single CoinMarketCal event by its numeric id, including its title, dates, related coins, source links and impact fields. |
| List Coins | `listCoins` | Returns the directory of cryptocurrencies CoinMarketCal tracks, with slug, ticker symbol, market-cap rank, icon and upcoming event counts. Supports a text search and cursor pagination, and is the source of the coin slugs accepted by the List Events coins filter. |
| List Event Categories | `listEventCategories` | Returns the event categories CoinMarketCal classifies events into, such as exchange listings, hard forks and token unlocks. The returned ids are the values accepted by the categories filter on List Events. This endpoint requires a Standard plan or above; Free-plan keys receive HTTP 403. |
| List Events | `listEvents` | Returns the CoinMarketCal event feed - upcoming and past crypto events such as listings, hard forks, token unlocks, airdrops and community calls. Results can be narrowed by coin, category, date range and minimum impact, sorted, and paged through with the cursor returned in meta. The categories filter requires a Standard plan or above and impactMin requires an Elite plan or above. |
