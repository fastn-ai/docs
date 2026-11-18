---
description: "CoinGecko is the world's largest independent cryptocurrency data aggregator."
hidden: true
---

# CoinGecko

CoinGecko is the world's largest independent cryptocurrency data aggregator. This connector covers the complete CoinGecko API v3: simple prices, search and ID maps, coins and market data, coin charts and OHLC, categories, tokenized real world assets (RWA), exchanges, derivatives, public treasury holdings, NFT collections, trending searches, news and insights, global market data, BTC exchange rates, plus the Onchain (GeckoTerminal) DEX endpoints for networks, DEXs, pools, tokens, OHLCV charts, trades, wallets, holders and categories. Endpoints marked as paid-plan only in the CoinGecko docs require a Pro API key.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [coingecko.com](https://coingecko.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 100 |
| **Events** | 0 |
| **Slug** | `coingecko` |

## Use it

Add CoinGecko from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.coingecko.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check API Server Status | `pingServer` | Checks that the CoinGecko API server is reachable and returns its status message. |
| Filter Onchain Pools | `poolsMegafilter` | Searches DEX liquidity pools across all networks with rich filters (networks, DEXs, FDV, reserve, volume, age, transaction counts, price change, taxes, holders, safety checks) and sorting. Available on CoinGecko paid (Pro) API plans only. |
| Get API Usage | `apiUsage` | Returns the account's API usage: plan, rate limit per minute, monthly call credits, calls made and calls remaining. Available on CoinGecko paid (Pro) API plans only. |
| Get BTC Exchange Rates | `exchangeRates` | Returns the BTC exchange rate against every supported fiat currency, cryptocurrency and commodity, keyed by currency code with name, unit, value and type. |
| Get Circulating Supply Chart | `coinsIdCirculatingSupplyChart` | Returns a coin's historical circulating supply as timestamped pairs for the last N days. Available on CoinGecko Enterprise plan only. |
| Get Circulating Supply Chart By Range | `coinsIdCirculatingSupplyChartRange` | Returns a coin's historical circulating supply as timestamped pairs between two dates. Available on CoinGecko Enterprise plan only. |
| Get Coin | `coinsId` | Returns all metadata (image, websites, socials, description, contract addresses, categories) and market data (price, market cap, all-time high, supply, exchange tickers) for a coin by its coin ID. |
| Get Coin By Token Address | `coinsContractAddress` | Returns all metadata and market data of a coin identified by its asset platform and token contract address. |
| Get Coin History By Date | `coinsIdHistory` | Returns a coin's historical snapshot (price, market cap and 24h volume in every currency, plus image and public interest stats) at a given date. |
| Get Coin Market Chart | `coinsIdMarketChart` | Returns historical chart data for a coin (price, market cap and 24h volume as timestamped pairs) for the last N days in a target currency, with automatic or explicit granularity. |
| Get Coin Market Chart By Range | `coinsIdMarketChartRange` | Returns historical chart data for a coin (price, market cap and 24h volume as timestamped pairs) between two dates in a target currency. |
| Get Coin OHLC Chart | `coinsIdOhlc` | Returns the OHLC (open, high, low, close) candles of a coin for the last N days in a target currency. |
| Get Coin OHLC Chart By Range | `coinsIdOhlcRange` | Returns the OHLC (open, high, low, close) candles of a coin between two dates in a target currency at daily or hourly interval. Available on CoinGecko paid (Pro) API plans only. |
| Get Coin Prices | `simplePrice` | Returns the current price of one or more coins, looked up by coin ID, symbol or name, in one or more target currencies, optionally with market cap, 24h volume, 24h change and last-updated timestamp. |
| Get Coin Supply Breakdown | `coinsIdSupplyBreakdown` | Returns a coin's supply breakdown: total, circulating, outstanding and non-circulating supply plus the list of non-circulating wallets. Available on CoinGecko paid (Pro) API plans only. |
| Get Derivatives Exchange | `derivativesExchangesId` | Returns a derivatives exchange's data (name, open interest, 24h volume, pair counts, country, description) and optionally its tickers, by exchange ID. |
| Get Exchange | `exchangesId` | Returns an exchange's profile (name, year established, country, links, trust score, 24h BTC volume) and its top 100 tickers, by exchange ID. |
| Get Exchange Volume Chart | `exchangesIdVolumeChart` | Returns an exchange's historical trading volume in BTC as timestamped pairs for the last N days, for a spot or derivatives exchange ID. |
| Get Exchange Volume Chart By Range | `exchangesIdVolumeChartRange` | Returns an exchange's historical trading volume in BTC as timestamped pairs between two UNIX timestamps. Available on CoinGecko paid (Pro) API plans only. |
| Get Global DeFi Market Data | `globalDefi` | Returns global decentralized finance market data for the top 100 DeFi coins: DeFi market cap, ETH market cap, DeFi-to-ETH ratio, 24h trading volume, DeFi dominance and top DeFi coin. |
| Get Global Market Cap Chart | `globalMarketCapChart` | Returns historical total crypto market cap and volume as timestamped pairs for the last N days in a target currency. Available on CoinGecko paid (Pro) API plans only. |
| Get Global Market Data | `cryptoGlobal` | Returns global cryptocurrency market data: number of active coins, ICO counts, markets, total market cap and volume by currency, market cap dominance and 24h changes. |
| Get NFT Collection | `nftsId` | Returns an NFT collection's data by collection ID: name, images, description, floor price, market cap, 24h volume, unique holders, sales, links and percentage changes. |
| Get NFT Collection By Contract Address | `nftsContractAddress` | Returns an NFT collection's data (floor price, market cap, 24h volume, holders, sales, links) by its asset platform and contract address. |
| Get NFT Collection Market Chart | `nftsIdMarketChart` | Returns an NFT collection's historical floor price, 24h volume and market cap in USD and native currency as timestamped pairs for the last N days. Available on CoinGecko paid (Pro) API plans only. |
| Get NFT Collection Market Chart By Contract Address | `nftsContractAddressMarketChart` | Returns an NFT collection's historical floor price, 24h volume and market cap as timestamped pairs for the last N days, by asset platform and contract address. Available on CoinGecko paid (Pro) API plans only. |
| Get Onchain Pool | `poolAddress` | Returns a DEX liquidity pool on a network by pool address: token prices, FDV, market cap, price changes, transaction counts, volume and reserves, optionally with base token, quote token and DEX details. |
| Get Onchain Pool Token Info | `poolTokenInfoContractAddress` | Returns metadata (name, symbol, images, CoinGecko coin ID, websites, socials, description, GeckoTerminal score) for the base and quote tokens of a DEX pool, by network and pool address. |
| Get Onchain Pools By Addresses | `poolsAddresses` | Returns several DEX liquidity pools on one network by comma-separated pool addresses (up to 30 per call), with prices, volume, transactions and reserves. |
| Get Onchain Token | `tokenDataContractAddress` | Returns onchain data for a token by network and contract address: name, symbol, decimals, CoinGecko coin ID, supply, USD price, FDV, market cap, reserves and 24h volume, optionally with its top pools. |
| Get Onchain Token Info | `tokenInfoContractAddress` | Returns token metadata by network and contract address: name, symbol, images, CoinGecko coin ID, websites, socials, description, categories, GeckoTerminal score and holder information. |
| Get Onchain Token Prices | `onchainSimplePrice` | Returns the USD price of one or more tokens on a network by contract address, optionally with market cap, 24h volume, 24h price change and total reserve. |
| Get Onchain Token Prices Across Networks | `onchainSimplePriceMulti` | Returns the USD price of up to 50 tokens across different networks given network:address pairs, optionally with market cap, volume, price change and reserve. Available on CoinGecko Enterprise plan only. |
| Get Onchain Tokens Across Networks | `tokensDataContractAddressesMulti` | Returns onchain data for up to 50 tokens across different networks, given network:address pairs, optionally with their top pools. Available on CoinGecko Enterprise plan only. |
| Get Onchain Tokens By Addresses | `tokensDataContractAddresses` | Returns onchain data for several tokens on one network by comma-separated contract addresses (up to 30 per call), optionally with their top pools. |
| Get Pool OHLCV Chart | `poolOhlcvContractAddress` | Returns OHLCV candles (open, high, low, close, volume) for a DEX pool by network, pool address and timeframe, in USD or quote token, up to 1000 candles per call. |
| Get RWA | `rwasId` | Returns the metadata of a tokenized real world asset by RWA ID, optionally including its tokens, tokenized market data and 7-day sparkline. |
| Get RWA Issuer | `rwasIssuersId` | Returns an RWA issuer's market data (market cap, 24h change, 24h volume) and the tokens it issues, by issuer ID. |
| Get RWA Market Chart | `rwasIdMarketChart` | Returns historical tokenized price, market cap and volume of a tokenized real world asset as timestamped pairs for the last N days. Available on CoinGecko paid (Pro) API plans only. |
| Get Token Holders Chart | `tokenHoldersChartTokenAddress` | Returns the historical number of holders of a token as timestamped pairs for the last 7 days, 30 days or all time. Available on CoinGecko paid (Pro) API plans only. |
| Get Token List By Asset Platform | `tokenLists` | Returns the full token list of a blockchain network in the Ethereum token list standard format (name, logo, timestamp, tokens with chain ID, address, symbol, decimals and version). |
| Get Token Market Chart By Address | `contractAddressMarketChart` | Returns historical chart data (price, market cap and 24h volume as timestamped pairs) for a token identified by asset platform and contract address, for the last N days. |
| Get Token Market Chart By Address And Range | `contractAddressMarketChartRange` | Returns historical chart data (price, market cap and 24h volume as timestamped pairs) for a token identified by asset platform and contract address, between two dates. |
| Get Token OHLCV Chart | `tokenOhlcvTokenAddress` | Returns OHLCV candles for a token across its pools by network, token address and timeframe, up to 1000 candles per call. Available on CoinGecko paid (Pro) API plans only. |
| Get Token Prices By Address | `simpleTokenPrice` | Returns the current price of one or more tokens on an asset platform, looked up by token contract address, in one or more target currencies, optionally with market cap, 24h volume, 24h change and last-updated timestamp. |
| Get Total Supply Chart | `coinsIdTotalSupplyChart` | Returns a coin's historical total supply as timestamped pairs for the last N days. Available on CoinGecko Enterprise plan only. |
| Get Total Supply Chart By Range | `coinsIdTotalSupplyChartRange` | Returns a coin's historical total supply as timestamped pairs between two dates. Available on CoinGecko Enterprise plan only. |
| Get Treasury Holdings By Entity | `publicTreasuryEntity` | Returns a public company's or government's crypto treasury: profile, total treasury value, unrealized P&L, mNAV and per-coin holdings, optionally with holding changes over selected timeframes. |
| Get Treasury Holdings Chart | `publicTreasuryEntityChart` | Returns the historical holdings of a coin by a public company or government as timestamped amount and USD value pairs for the last N days. |
| Get Trending Searches | `trendingSearch` | Returns the coins, NFT collections and categories most searched on CoinGecko in the last 24 hours, with market data for each. |
| Get Wallet Token Balances | `walletTokenBalances` | Returns the token holdings of a wallet address across the requested networks with amounts and USD values, filterable and paginated. Available on CoinGecko paid (Pro) API plans only. |
| List Asset Platforms | `assetPlatformsList` | Returns every asset platform (blockchain network) supported by CoinGecko with its ID, chain identifier, name, native coin ID and image. Use the IDs in token address lookups. |
| List Coin Categories | `coinsCategoriesList` | Returns every coin category supported by CoinGecko with its category ID and name. |
| List Coin Categories With Market Data | `coinsCategories` | Returns every coin category with its aggregate market cap, 24h market cap change, 24h volume, description and top 3 coins, sortable by market cap, name or 24h change. |
| List Coin Insights | `insights` | Returns the latest coin insights published on CoinGecko, filterable by coin and date range, paginated. Available on CoinGecko Enterprise plan only. |
| List Coin Tickers | `coinsIdTickers` | Returns the trading tickers of a coin across centralized and decentralized exchanges, with last price, volume, spread, trust score and optional order-book depth, paginated 100 per page. |
| List Coins | `coinsList` | Returns every coin supported by CoinGecko with its coin ID, symbol and name, optionally including asset platform contract addresses. Use the returned IDs in other coin actions. |
| List Coins With Market Data | `coinsMarkets` | Returns coins with price, market cap, volume, supply, all-time high and low and price change data in a target currency, filterable by coin IDs, names, symbols or category, sortable and paginated. |
| List Crypto News | `news` | Returns the latest crypto news articles and guides on CoinGecko, filterable by coin, language and type, paginated. Available on CoinGecko paid (Pro) API plans only. |
| List Derivatives Exchanges | `derivativesExchangesList` | Returns every derivatives exchange supported by CoinGecko with its ID and name. |
| List Derivatives Exchanges With Data | `derivativesExchanges` | Returns derivatives exchanges with open interest in BTC, 24h volume in BTC, number of perpetual and futures pairs, country and year established, sortable and paginated. |
| List Derivatives Tickers | `derivativesTickers` | Returns all perpetual and futures tickers from derivatives exchanges with price, 24h change, contract type, index, basis, spread, funding rate, open interest and volume. |
| List DEXs By Network | `dexesList` | Returns every decentralized exchange supported by GeckoTerminal on a network with its DEX ID and name, paginated. |
| List Exchange Tickers | `exchangesIdTickers` | Returns an exchange's tickers with last price, volume, spread and trust score, filterable by coin IDs, sortable and paginated 100 per page. |
| List Exchanges | `exchangesList` | Returns every exchange supported by CoinGecko with its exchange ID and name. |
| List Exchanges With Data | `exchanges` | Returns exchanges with active trading volume on CoinGecko, including name, country, year established, trust score and 24h volume in BTC, paginated. |
| List New Onchain Pools | `latestPoolsList` | Returns the most recently created DEX liquidity pools across all networks on GeckoTerminal, paginated 20 per page. |
| List New Onchain Pools By Network | `latestPoolsNetwork` | Returns the most recently created DEX liquidity pools on one network, paginated 20 per page. |
| List NFT Collection Tickers | `nftsIdTickers` | Returns the latest floor price and 24h volume of an NFT collection on each NFT marketplace. Available on CoinGecko paid (Pro) API plans only. |
| List NFT Collections | `nftsList` | Returns every NFT collection supported by CoinGecko with its ID, contract address, name, asset platform ID and symbol, sortable and paginated. |
| List NFT Collections With Market Data | `nftsMarkets` | Returns NFT collections with floor price, market cap, 24h volume, holders and sales data, filterable by asset platform, sortable and paginated. Available on CoinGecko paid (Pro) API plans only. |
| List Onchain Categories | `categoriesList` | Returns the token categories tracked on GeckoTerminal with aggregate volume, transaction counts, FDV and reserve data, sortable and paginated. Available on CoinGecko paid (Pro) API plans only. |
| List Onchain Networks | `networksList` | Returns every blockchain network supported by GeckoTerminal with its network ID, name and CoinGecko asset platform ID, paginated. |
| List Onchain Pools By Category | `poolsCategory` | Returns the DEX liquidity pools belonging to a GeckoTerminal category, sortable and paginated. Available on CoinGecko paid (Pro) API plans only. |
| List Pool Trades | `poolTradesContractAddress` | Returns recent trades of a DEX pool by network and pool address (up to 300 per page, cursor paginated), with transaction hash, block, trader, amounts, prices and trade kind. |
| List Pool Trades By Range | `poolTradesContractAddressRange` | Returns trades of a DEX pool between two dates, cursor paginated. Available on CoinGecko paid (Pro) API plans only. |
| List Public Treasury Entities | `entitiesList` | Returns the public companies and governments tracked by CoinGecko's crypto treasury data, with entity ID, ticker symbol, name and country. |
| List Recently Added Coins | `coinsListNew` | Returns the latest 200 coins recently listed on CoinGecko with ID, symbol, name and activation timestamp. Available on CoinGecko paid (Pro) API plans only. |
| List Recently Updated Onchain Tokens | `tokensInfoRecentUpdated` | Returns the 100 tokens whose metadata was most recently updated on GeckoTerminal, across all networks or one network. |
| List RWA Issuers | `rwasIssuersList` | Returns every tokenized real world asset issuer supported by CoinGecko with its issuer ID and name. |
| List RWA Tickers | `rwasIdTickers` | Returns the tickers of a tokenized real world asset's tokens across centralized and decentralized exchanges, filterable by issuer or exchange. Available on CoinGecko paid (Pro) API plans only. |
| List RWAs | `rwasList` | Returns every tokenized real world asset (RWA) supported by CoinGecko with its ID, symbol, name and asset type (stock, commodity or ETF). |
| List RWAs With Market Data | `rwasMarkets` | Returns tokenized real world assets with tokenized price, market cap and volume data, filterable by asset type, IDs, names, symbols or issuer, sortable and paginated. |
| List Supported Currencies | `simpleSupportedCurrencies` | Returns every target currency code supported by CoinGecko price endpoints (fiat currencies, major coins and commodities). |
| List Token Trades | `tokenTradesContractAddress` | Returns recent trades of a token across all its pools by network and token address, cursor paginated. Available on CoinGecko paid (Pro) API plans only. |
| List Token Trades By Range | `tokenTradesContractAddressRange` | Returns trades of a token across all its pools between two dates, cursor paginated. Available on CoinGecko paid (Pro) API plans only. |
| List Top Gainers And Losers | `coinsTopGainersLosers` | Returns the top 30 coins with the largest price gain and the largest price loss over a chosen time duration. Available on CoinGecko paid (Pro) API plans only. |
| List Top Onchain Pools By DEX | `topPoolsDex` | Returns the top liquidity pools of one decentralized exchange on a network, sorted by 24h transaction count or volume, paginated 20 per page. |
| List Top Onchain Pools By Network | `topPoolsNetwork` | Returns the top DEX liquidity pools on one network, sorted by 24h transaction count or volume, paginated 20 per page. |
| List Top Onchain Pools By Token | `topPoolsContractAddress` | Returns the top DEX liquidity pools that include a token, by network and token contract address, sortable by liquidity-weighted volume, transaction count or volume. |
| List Top Token Holders | `topTokenHoldersTokenAddress` | Returns the top holders of a token by network and contract address, with balances, share of supply and optional PnL details. Available on CoinGecko paid (Pro) API plans only. |
| List Top Token Traders | `topTokenTradersTokenAddress` | Returns the top traders of a token by network and contract address, with realized and unrealized PnL, buy and sell totals and balance. Available on CoinGecko paid (Pro) API plans only. |
| List Treasury Holdings By Coin | `companiesPublicTreasury` | Returns public companies' or governments' holdings of a coin (total holdings, USD value, market cap dominance and the per-entity breakdown), paginated and sortable. |
| List Treasury Transactions | `publicTreasuryTransactionHistory` | Returns a public company's or government's crypto buy and sell transaction history with date, source document, net holding change, USD value and running balance, filterable by coin, sortable and paginated. |
| List Trending Onchain Pools | `trendingPoolsList` | Returns the trending DEX liquidity pools across all networks on GeckoTerminal, ranked over a chosen duration, paginated 20 per page. |
| List Trending Onchain Pools By Network | `trendingPoolsNetwork` | Returns the trending DEX liquidity pools on one network, ranked over a chosen duration, paginated 20 per page. |
| List Trending Search Pools | `trendingSearchPools` | Returns the DEX pools most searched on GeckoTerminal across all networks, up to 10, with trending rank and market data. Available on CoinGecko paid (Pro) API plans only. |
| List Wallet Token Transfers | `walletTokenTransfers` | Returns the token transfers of a wallet address on a network, filterable by token, date range and direction, cursor paginated. Available on CoinGecko paid (Pro) API plans only. |
| Search | `searchData` | Searches coins, exchanges, categories and NFT collections listed on CoinGecko by a free-text query and returns matching entries with their IDs. |
| Search Onchain Pools | `searchPools` | Searches DEX liquidity pools across all networks or one network by pool address, token name, token symbol or token contract address. |
