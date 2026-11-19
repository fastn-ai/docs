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

## Use it

Add CoinMarketCal from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.coinMarketCal.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get API Usage</td><td><code>getApiUsage</code></td><td>Returns the current billing period's API usage for the connected key: the plan tier, requests made, monthly quota, requests remaining and when the quota resets.</td></tr><tr><td>Get Coin</td><td><code>getCoin</code></td><td>Returns a single cryptocurrency from the CoinMarketCal directory by its slug, including ticker symbol, market-cap rank, icon and upcoming event counts.</td></tr><tr><td>Get Event</td><td><code>getEvent</code></td><td>Returns a single CoinMarketCal event by its numeric id, including its title, dates, related coins, source links and impact fields.</td></tr><tr><td>List Coins</td><td><code>listCoins</code></td><td>Returns the directory of cryptocurrencies CoinMarketCal tracks, with slug, ticker symbol, market-cap rank, icon and upcoming event counts. Supports a text search and cursor pagination, and is the source of the coin slugs accepted by the List Events coins filter.</td></tr><tr><td>List Event Categories</td><td><code>listEventCategories</code></td><td>Returns the event categories CoinMarketCal classifies events into, such as exchange listings, hard forks and token unlocks. The returned ids are the values accepted by the categories filter on List Events. This endpoint requires a Standard plan or above; Free-plan keys receive HTTP 403.</td></tr><tr><td>List Events</td><td><code>listEvents</code></td><td>Returns the CoinMarketCal event feed - upcoming and past crypto events such as listings, hard forks, token unlocks, airdrops and community calls. Results can be narrowed by coin, category, date range and minimum impact, sorted, and paged through with the cursor returned in meta. The categories filter requires a Standard plan or above and impactMin requires an Elite plan or above.</td></tr></tbody></table>

## Events

CoinMarketCal has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
