---
description: "StockData.org provides stock market data and financial news. Get real-time quotes, intraday and end-of-day prices, and news articles."
hidden: true
---

# StockData.org

<img src="../../.gitbook/assets/connectors/lg/stockdata.png" alt="StockData.org logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [stockdata.org](https://stockdata.org) |
| **Authentication** | API token |
| **Slug** | `stockdata` |

## Setup

Your customers enter their API token for StockData.org when they connect. Nothing else needs setting up.

## Use it

Add StockData.org from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.stockdata.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get End-of-Day Historical Data</td><td><code>getEodData</code></td><td>Returns daily, weekly, monthly, quarterly, or yearly end-of-day OHLCV price history for one or more stock, crypto, or forex symbols.</td></tr><tr><td>Get Intraday Data (Adjusted)</td><td><code>getIntradayAdjusted</code></td><td>Returns intraday OHLCV price history adjusted for stock splits, for one stock symbol, at minute or hour granularity, going back up to 7+ years.</td></tr><tr><td>Get Intraday Data (Unadjusted)</td><td><code>getIntradayUnadjusted</code></td><td>Returns raw, unadjusted intraday OHLCV price history for one stock symbol, at minute or hour granularity, going back up to 7+ years.</td></tr><tr><td>Get News Article By UUID</td><td><code>getNewsByUuid</code></td><td>Returns a single news article, with full identified-entity and sentiment analysis, by its unique UUID.</td></tr><tr><td>Get News Entity Stats (Aggregation)</td><td><code>getNewsStatsAggregation</code></td><td>Returns a single aggregated snapshot of news document counts and average sentiment, grouped by symbol, exchange, industry, or country, over the filtered time range.</td></tr><tr><td>Get News Entity Stats (Time Series)</td><td><code>getNewsStatsIntraday</code></td><td>Returns a time series of news document counts and average sentiment, grouped by symbol, exchange, industry, or country, at a configurable interval.</td></tr><tr><td>Get Real-Time Stock Quote</td><td><code>getStockQuote</code></td><td>Returns the current real-time (or latest available) price quote for one or more stock symbols, including open, high, low, close, volume, day range, 52-week range, and market cap.</td></tr><tr><td>Get Similar News Articles</td><td><code>getSimilarNews</code></td><td>Returns news articles similar to a given article, identified by its UUID, using the same entity, sentiment, source, language, and date filters as the news search endpoint.</td></tr><tr><td>Get Trending News Entities</td><td><code>getTrendingEntities</code></td><td>Returns the entities (symbols, exchanges, industries, or countries) currently trending in the news, ranked by relevance and document volume.</td></tr><tr><td>List Entity Types</td><td><code>listEntityTypes</code></td><td>Returns the list of entity types supported by the entity search and news filters (e.g. equity, index, etf).</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Industries</td><td><code>listIndustries</code></td><td>Returns the list of industry classifications supported by the entity search and news filters.</td></tr><tr><td>List News Sources</td><td><code>listNewsSources</code></td><td>Returns the list of news source domains and IDs available for filtering news search results, optionally grouped by distinct domain and filtered by language.</td></tr><tr><td>List Stock Dividends</td><td><code>listStockDividends</code></td><td>Returns the historical dividend payout events (ex-dividend date, amount per share) for one or more stock symbols.</td></tr><tr><td>List Stock Splits</td><td><code>listStockSplits</code></td><td>Returns the historical stock split events (date, ratio) for one or more stock symbols.</td></tr><tr><td>Search Finance And Market News</td><td><code>searchNews</code></td><td>Searches finance and market news articles with entity, sentiment, source, language, and date filters, returning identified entities, sentiment scores, and highlights for each article.</td></tr><tr><td>Search Stock Entities</td><td><code>searchEntities</code></td><td>Searches the entity directory (stocks, indices, and other tracked entities) by name, symbol, exchange, type, industry, or country and returns matching entity metadata.</td></tr></tbody></table>

</details>

## Events

StockData.org has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
