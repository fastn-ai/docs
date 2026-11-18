---
description: "CoinMarketCap is the most-referenced source of cryptocurrency market data, covering real-time and historical prices, market capitalisation, OHLCV candles,…"
hidden: true
---

# CoinMarketCap

<img src="../../.gitbook/assets/connectors/lg/coin-market-cap.png" alt="CoinMarketCap logo">

CoinMarketCap is the most-referenced source of cryptocurrency market data, covering real-time and historical prices, market capitalisation, OHLCV candles, exchange and on-chain DEX data, derivatives, tokenised real-world assets and CMC's proprietary indices. This connector covers the CoinMarketCap Pro API: cryptocurrency listings, quotes, metadata, market pairs, OHLCV, categories, airdrops and trending; exchange listings, quotes, market pairs and assets; global metrics, Fear and Greed and Altcoin Season indices; the CMC 100 and CMC 20 indices; content and community feeds; DEX token, pool, holder, liquidity and K-line data; derivatives and liquidations; real-world assets; CMC AI insights; and the fiat map, price conversion and API key utilities.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [coinmarketcap.com](https://coinmarketcap.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `coinMarketCap` |

## Use it

Add CoinMarketCap from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.coinMarketCap.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Get DEX Token Prices | `batchGetDexTokenPrices` | Returns the current on-chain price of several DEX tokens in one call, given a list of platform and contract address pairs that may span different blockchains. |
| Batch Query DEX Tokens | `batchQueryDexTokens` | Returns full on-chain profiles for several DEX tokens on the same blockchain in one call, given a list of contract addresses. |
| Convert Price | `convertPrice` | Converts an amount of one cryptocurrency or fiat currency into one or more other currencies using the latest market rate, or the rate at a given historical timestamp. |
| Export Postman Collection | `exportPostmanCollection` | Returns a Postman collection document for the CoinMarketCap Pro API, pre-filled with the endpoints available to the connected key's subscription plan. |
| Get Airdrop | `getAirdrop` | Returns a single token airdrop by its unique id, including the project, the cryptocurrency being distributed, the schedule, the prize pool and the winner count. |
| Get API Key Info | `getApiKeyInfo` | Returns the subscription plan and current usage of the connected API key, including the credit limit, credits used and left for the month, the per-minute rate limit and when the plan resets. |
| Get CMC AI Coin Map | `getCmcAiCoinMap` | Returns the cryptocurrencies that CMC AI publishes question-and-answer insights for, mapped to their CoinMarketCap ids. |
| Get Cryptocurrency Category | `getCryptocurrencyCategory` | Returns a single cryptocurrency category with its aggregate market statistics and a paginated list of the coins it contains, each with the latest market quote. |
| Get Cryptocurrency ID Map | `getCryptocurrencyIdMap` | Returns a mapping of all cryptocurrencies to their unique CoinMarketCap ids, along with name, symbol, slug, listing status and the first and last dates historical data is available for. Use these ids rather than symbols to identify assets on the other endpoints. |
| Get Cryptocurrency Metadata | `getCryptocurrencyMetadata` | Returns static metadata for one or more cryptocurrencies, including logo, description, official website and social links, technical documentation, category, tags and contract addresses. |

<details>

<summary>See 80 more actions</summary>

* **Get Cryptocurrency Price Performance Stats** `getCryptocurrencyPricePerformanceStats`: Returns price performance statistics for one or more cryptocurrencies over the requested time periods, including the open, high, low and close prices, percent change and return on investment for each window.
* **Get DEX Platform Detail** `getDexPlatformDetail`: Returns detail for a single blockchain platform supported by the DEX endpoints, including its native currency, explorer and aggregate on-chain activity.
* **Get DEX Token Detail** `getDexTokenDetail`: Returns the full on-chain profile of a DEX token by blockchain platform and contract address, including price, liquidity, market cap, holder count and pool information.
* **Get DEX Token Price** `getDexTokenPrice`: Returns the current on-chain price of a single DEX token, identified by blockchain platform and contract address.
* **Get DEX Token Security Detail** `getDexTokenSecurityDetail`: Returns the contract security analysis for a DEX token, covering honeypot and rug-pull indicators, mintability, ownership, trading taxes and liquidity lock status.
* **Get Exchange ID Map** `getExchangeIdMap`: Returns a mapping of all cryptocurrency exchanges to their unique CoinMarketCap ids, with name, slug, listing status and the date range of available historical data. Use these ids to identify exchanges on the other exchange endpoints.
* **Get Exchange Metadata** `getExchangeMetadata`: Returns static metadata for one or more exchanges, including logo, description, launch date, fee structure, supported fiat currencies and official website and social links.
* **Get Fiat ID Map** `getFiatIdMap`: Returns the fiat currencies and precious metals CoinMarketCap supports as conversion targets, with their unique ids, ISO codes, names and currency signs.
* **Get Historical Altcoin Season Index** `getHistoricalAltcoinSeasonIndex`: Returns historical readings of the CMC Altcoin Season Index, showing how altcoin outperformance against Bitcoin has moved over time.
* **Get Historical CMC 100 Index** `getHistoricalCmc100Index`: Returns historical values of the CoinMarketCap 100 Index over a time range, each point carrying the index value and the constituents in force at that time.
* **Get Historical CMC 20 Index** `getHistoricalCmc20Index`: Returns historical values of the CoinMarketCap 20 Index over a time range, each point carrying the index value and the constituents in force at that time.
* **Get Historical Cryptocurrency OHLCV** `getHistoricalCryptocurrencyOhlcv`: Returns historical open, high, low, close and volume candles for one or more cryptocurrencies over a time range, at daily or hourly granularity.
* **Get Historical Cryptocurrency Quotes** `getHistoricalCryptocurrencyQuotes`: Returns an interval of historical market quotes for one or more cryptocurrencies over a time range, with a selectable sampling interval.
* **Get Historical Exchange Quotes** `getHistoricalExchangeQuotes`: Returns an interval of historical aggregate market data for one or more exchanges over a time range, at a selectable sampling interval.
* **Get Historical Fear And Greed Index** `getHistoricalFearAndGreedIndex`: Returns historical daily readings of the CMC Crypto Fear and Greed Index, each with its value and sentiment classification.
* **Get Historical Global Metrics** `getHistoricalGlobalMetrics`: Returns an interval of historical aggregate market metrics, including total market cap, total volume and Bitcoin dominance, over a time range at a selectable sampling interval.
* **Get K-Line Candles** `getKLineCandles`: Returns candlestick (K-line) data for a DEX token or liquidity pool at the requested interval, in USD, native or quote units, for price or market cap.
* **Get K-Line Points** `getKLinePoints`: Returns a lightweight point series for a DEX token or liquidity pool at the requested interval, suitable for sparkline charts of price or market cap.
* **Get Latest Altcoin Season Index** `getLatestAltcoinSeasonIndex`: Returns the current CMC Altcoin Season Index, which measures how many of the top altcoins have outperformed Bitcoin over the last 90 days.
* **Get Latest Blockchain Statistics** `getLatestBlockchainStatistics`: Returns the latest on-chain statistics for the supported proof-of-work blockchains, including block height, block time, hashrate, difficulty, reward and mempool size.
* **Get Latest CMC 100 Index** `getLatestCmc100Index`: Returns the latest value of the CoinMarketCap 100 Index, its 24 hour change and the current index constituents with their weights.
* **Get Latest CMC 20 Index** `getLatestCmc20Index`: Returns the latest value of the CoinMarketCap 20 Index, its 24 hour change and the current index constituents with their weights.
* **Get Latest CMC AI Coin Insights** `getLatestCmcAiCoinInsights`: Returns the latest CMC AI question-and-answer insights for specific cryptocurrencies, as shown on their CoinMarketCap coin detail pages.
* **Get Latest CMC AI Market Feed** `getLatestCmcAiMarketFeed`: Returns the latest CMC AI market question-and-answer items shown on the CoinMarketCap homepage, each pairing a market question with an AI-generated answer and its sources.
* **Get Latest Cryptocurrency OHLCV** `getLatestCryptocurrencyOhlcv`: Returns the open, high, low, close and volume values for the current UTC day so far, for one or more cryptocurrencies.
* **Get Latest Cryptocurrency Quotes** `getLatestCryptocurrencyQuotes`: Returns the latest market quote for one or more cryptocurrencies identified by CoinMarketCap id, slug or symbol, including price, volume, supply, market cap and percent changes in any supported conversion currency.
* **Get Latest DEX Pair Quotes** `getLatestDexPairQuotes`: Returns the latest market quote for one or more decentralised exchange spot pairs, identified by pool contract address and network.
* **Get Latest Exchange Quotes** `getLatestExchangeQuotes`: Returns the latest aggregate market data for one or more exchanges identified by CoinMarketCap id or slug, including 24 hour volume and the number of active market pairs.
* **Get Latest FCAS Quotes** `getLatestFcasQuotes`: Returns the latest Flipside Crypto FCAS fundamental health score for specific cryptocurrencies, identified by CoinMarketCap id, slug or symbol. CoinMarketCap marks this partner endpoint as deprecated.
* **Get Latest Fear And Greed Index** `getLatestFearAndGreedIndex`: Returns the current CMC Crypto Fear and Greed Index value and its sentiment classification, from Extreme Fear through to Extreme Greed.
* **Get Latest Global Metrics** `getLatestGlobalMetrics`: Returns the latest aggregate market metrics for the whole cryptocurrency market, including total market cap, total 24 hour volume, Bitcoin and Ethereum dominance, DeFi and stablecoin volumes and the number of active cryptocurrencies, exchanges and market pairs.
* **Get Latest Real World Asset Quotes** `getLatestRealWorldAssetQuotes`: Returns the latest market quote for one or more tokenised real-world assets, including price, market cap, 24 hour volume and percent changes.
* **Get Latest Total Liquidations** `getLatestTotalLiquidations`: Returns market-wide derivatives liquidation totals over the recent rolling windows, split by long and short positions.
* **Get Real World Asset ID Map** `getRealWorldAssetIdMap`: Returns a mapping of the tokenised real-world assets CoinMarketCap tracks - equities, commodities, currencies, government securities, ETFs and real estate - to their unique ids, symbols and slugs.
* **Get Real World Asset Issuer** `getRealWorldAssetIssuer`: Returns a single real-world asset issuer by id, together with the paginated list of tokens it has issued.
* **Get Real World Asset Metadata** `getRealWorldAssetMetadata`: Returns static metadata for one or more tokenised real-world assets, including the underlying instrument, issuer, website, logo and description.
* **Get Simple Price** `getSimplePrice`: Returns a lightweight price lookup for one or more cryptocurrencies, optionally including market cap, 24 hour volume, 24 hour change and the last updated timestamp in each quote.
* **Get Token Holder Count** `getTokenHolderCount`: Returns the current number of wallets holding a DEX token on a given blockchain.
* **Get Token Holder Detail** `getTokenHolderDetail`: Returns the detailed position of a single wallet in a DEX token, including its balance, cost basis, realised and unrealised profit and trading history for that token.
* **Get Token Holder Tag Counts** `getTokenHolderTagCounts`: Returns how many of a DEX token's holders fall into each behavioural cohort - smart money, whales, KOLs, bots, snipers and the developer.
* **List Airdrops** `listAirdrops`: Returns the token airdrops CoinMarketCap tracks, filterable by status and by the cryptocurrency they belong to, with start and end dates, total prize and winner count.
* **List Community Post Comments** `listCommunityPostComments`: Returns the comments left on a CoinMarketCap Community post, with the commenting account and engagement counts.
* **List Community Trending Tokens** `listCommunityTrendingTokens`: Returns the tokens being discussed most in the CoinMarketCap Community over the last 24 hours, ranked by mention volume.
* **List Community Trending Topics** `listCommunityTrendingTopics`: Returns the topics trending in the CoinMarketCap Community over the last 24 hours, ranked by discussion volume.
* **List Cryptocurrency Categories** `listCryptocurrencyCategories`: Returns the cryptocurrency categories CoinMarketCap maintains, such as DeFi, gaming or layer one, each with the number of tokens, average price change and aggregate market cap and volume. Can be filtered to the categories a given asset belongs to.
* **List Cryptocurrency Market Pairs** `listCryptocurrencyMarketPairs`: Returns the active market pairs a cryptocurrency trades on across every exchange CoinMarketCap tracks, with price, volume and liquidity per pair.
* **List Derivative Market Pairs By Cryptocurrency** `listDerivativeMarketPairsByCryptocurrency`: Returns the perpetual and futures contracts available for a given cryptocurrency across all derivatives exchanges, with index price, funding rate, open interest and 24 hour volume.
* **List Derivative Market Pairs By Exchange** `listDerivativeMarketPairsByExchange`: Returns the perpetual and futures market pairs listed on a derivatives exchange, with index price, funding rate, open interest and 24 hour volume for each contract.
* **List Derivatives Exchanges** `listDerivativesExchanges`: Returns the derivatives exchanges CoinMarketCap tracks, with their open interest, 24 hour derivatives volume and number of perpetual and futures market pairs.
* **List DEX Liquidity Changes** `listDexLiquidityChanges`: Returns the recent liquidity add and remove events for a DEX token, filterable by maker address, time range and USD volume, with cursor pagination.
* **List DEX Platforms** `listDexPlatforms`: Returns the blockchain platforms the DEX endpoints support, with the platform id, name and block explorer URL. These ids and names are the values accepted by the other DEX actions.
* **List DEX Token Pools** `listDexTokenPools`: Returns the liquidity pools a DEX token trades in, with the decentralised exchange, paired asset, liquidity and 24 hour volume for each pool.
* **List DEX Token Transactions** `listDexTokenTransactions`: Returns the recent swap transactions for a DEX token, filterable by trade direction, maker address, time range and volume, with cursor pagination.
* **List Exchange Assets** `listExchangeAssets`: Returns the proof-of-reserves wallet holdings CoinMarketCap tracks for an exchange, with the balance, blockchain platform and current USD value of each asset.
* **List Exchange Market Pairs** `listExchangeMarketPairs`: Returns the active market pairs listed on a given exchange, each with the traded assets, category, fee type and the latest price and volume.
* **List Historical Cryptocurrency Listings** `listHistoricalCryptocurrencyListings`: Returns a ranked, paginated snapshot of cryptocurrencies and their market data as it stood on a given historical date.
* **List Latest Community Posts** `listLatestCommunityPosts`: Returns the most recent posts from the CoinMarketCap Community feed for a given cryptocurrency, with engagement counts and the posting account.
* **List Latest Content** `listLatestContent`: Returns the latest crypto news, Alexandria articles and community content CoinMarketCap aggregates, optionally filtered to specific cryptocurrencies and content types.
* **List Latest Cryptocurrency Listings** `listLatestCryptocurrencyListings`: Returns a ranked, paginated list of all active cryptocurrencies with the latest market data, and supports price, market cap, volume, circulating supply and percent-change thresholds as filters.
* **List Latest DEX Spot Pairs** `listLatestDexSpotPairs`: Returns a ranked list of decentralised exchange spot trading pairs with their latest market data, filterable by network, exchange, base and quote asset and by liquidity, volume, transaction count and percent change thresholds. The live API requires either dex_id or dex_slug (for example 'raydium' or 'uniswap-v3') on every call.
* **List Latest Exchange Listings** `listLatestExchangeListings`: Returns a ranked list of all active cryptocurrency exchanges with their latest aggregate market data, including 24 hour volume, number of market pairs and traffic score.
* **List Latest FCAS Listings** `listLatestFcasListings`: Returns the latest Flipside Crypto FCAS fundamental health scores for all supported cryptocurrencies, covering user activity, developer behaviour and market maturity. CoinMarketCap marks this partner endpoint as deprecated.
* **List Latest Liquidations By Cryptocurrency** `listLatestLiquidationsByCryptocurrency`: Returns recent derivatives liquidation totals broken down by cryptocurrency, split by long and short positions across the rolling time windows.
* **List Latest Liquidations By Exchange** `listLatestLiquidationsByExchange`: Returns recent derivatives liquidation totals broken down by exchange, split by long and short positions across the rolling time windows.
* **List Meme Tokens** `listMemeTokens`: Returns meme-coin launchpad tokens grouped into newly created, about to graduate and graduated cohorts, with an optional filter applied to each cohort.
* **List Most Visited Cryptocurrencies** `listMostVisitedCryptocurrencies`: Returns the cryptocurrencies with the most page views on CoinMarketCap over the selected time window, with their latest market data.
* **List New Cryptocurrency Listings** `listNewCryptocurrencyListings`: Returns the cryptocurrencies most recently added to CoinMarketCap, ordered by listing date, with their latest market data.
* **List New DEX Tokens** `listNewDexTokens`: Returns the DEX tokens most recently deployed on the selected blockchains, ranked by the chosen sort field, with cursor pagination.
* **List Real World Asset Issuers** `listRealWorldAssetIssuers`: Returns the issuers that tokenise real-world assets, with the number of assets each has issued and their aggregate market cap.
* **List Real World Asset Market Pairs** `listRealWorldAssetMarketPairs`: Returns the market pairs a tokenised real-world asset trades on, with the exchange, the paired asset and the latest price and volume.
* **List Real World Assets** `listRealWorldAssets`: Returns a ranked, paginated list of tokenised real-world assets with their latest market data, filterable by category, issuer and market cap or volume thresholds.
* **List Token Holder Trend** `listTokenHolderTrend`: Returns a daily time series of how many wallets hold a DEX token, for charting holder growth over a period.
* **List Token Holders** `listTokenHolders`: Returns the wallets holding a DEX token, optionally narrowed to a behavioural cohort such as smart money, whales, KOLs, bots, snipers or the developer.
* **List Top Community Posts** `listTopCommunityPosts`: Returns the top-ranked posts from the CoinMarketCap Community feed for a given cryptocurrency, ordered by engagement.
* **List Top DEX Gainers And Losers** `listTopDexGainersAndLosers`: Returns the DEX tokens with the largest price gains and losses across the selected blockchains over a time interval, with cursor pagination.
* **List Trending Cryptocurrencies** `listTrendingCryptocurrencies`: Returns the cryptocurrencies trending on CoinMarketCap over the selected time window, ranked by trending score, with their latest market data.
* **List Trending DEX Tokens** `listTrendingDexTokens`: Returns the DEX tokens trending across the selected blockchains over a time interval, ranked by the chosen sort field, with cursor pagination.
* **List Trending Gainers And Losers** `listTrendingGainersAndLosers`: Returns the biggest cryptocurrency gainers and losers over the selected time window, ranked by percent change, with their latest market data.
* **Query DEX Token Liquidity** `queryDexTokenLiquidity`: Returns a time series of a DEX token's pooled liquidity at the requested interval, for charting how liquidity has moved.
* **Search DEX Tokens** `searchDexTokens`: Searches DEX tokens by name, symbol or contract address across supported blockchains and returns the matching tokens with their platform and market data.

</details>
