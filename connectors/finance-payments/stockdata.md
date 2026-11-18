---
description: "Real-time and historical stock market data, financial news, and market sentiment analytics from StockData.org."
hidden: true
---

# StockData.org

Real-time and historical stock market data, financial news, and market sentiment analytics from StockData.org. Covers live and end-of-day quotes, intraday OHLCV history, corporate actions (splits and dividends), crypto and forex EOD data, finance news search with entity and sentiment filters, market news statistics, and stock/entity metadata lookup.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [stockdata.org](https://stockdata.org) |
| **Authentication** | Credentials you enter |
| **Actions** | 16 |
| **Events** | 0 |
| **Slug** | `stockdata` |

## Use it

Add StockData.org from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.stockdata.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get End-of-Day Historical Data | `getEodData` | Returns daily, weekly, monthly, quarterly, or yearly end-of-day OHLCV price history for one or more stock, crypto, or forex symbols. |
| Get Intraday Data (Adjusted) | `getIntradayAdjusted` | Returns intraday OHLCV price history adjusted for stock splits, for one stock symbol, at minute or hour granularity, going back up to 7+ years. |
| Get Intraday Data (Unadjusted) | `getIntradayUnadjusted` | Returns raw, unadjusted intraday OHLCV price history for one stock symbol, at minute or hour granularity, going back up to 7+ years. |
| Get News Article By UUID | `getNewsByUuid` | Returns a single news article, with full identified-entity and sentiment analysis, by its unique UUID. |
| Get News Entity Stats (Aggregation) | `getNewsStatsAggregation` | Returns a single aggregated snapshot of news document counts and average sentiment, grouped by symbol, exchange, industry, or country, over the filtered time range. |
| Get News Entity Stats (Time Series) | `getNewsStatsIntraday` | Returns a time series of news document counts and average sentiment, grouped by symbol, exchange, industry, or country, at a configurable interval. |
| Get Real-Time Stock Quote | `getStockQuote` | Returns the current real-time (or latest available) price quote for one or more stock symbols, including open, high, low, close, volume, day range, 52-week range, and market cap. |
| Get Similar News Articles | `getSimilarNews` | Returns news articles similar to a given article, identified by its UUID, using the same entity, sentiment, source, language, and date filters as the news search endpoint. |
| Get Trending News Entities | `getTrendingEntities` | Returns the entities (symbols, exchanges, industries, or countries) currently trending in the news, ranked by relevance and document volume. |
| List Entity Types | `listEntityTypes` | Returns the list of entity types supported by the entity search and news filters (e.g. equity, index, etf). |
| List Industries | `listIndustries` | Returns the list of industry classifications supported by the entity search and news filters. |
| List News Sources | `listNewsSources` | Returns the list of news source domains and IDs available for filtering news search results, optionally grouped by distinct domain and filtered by language. |
| List Stock Dividends | `listStockDividends` | Returns the historical dividend payout events (ex-dividend date, amount per share) for one or more stock symbols. |
| List Stock Splits | `listStockSplits` | Returns the historical stock split events (date, ratio) for one or more stock symbols. |
| Search Finance And Market News | `searchNews` | Searches finance and market news articles with entity, sentiment, source, language, and date filters, returning identified entities, sentiment scores, and highlights for each article. |
| Search Stock Entities | `searchEntities` | Searches the entity directory (stocks, indices, and other tracked entities) by name, symbol, exchange, type, industry, or country and returns matching entity metadata. |
