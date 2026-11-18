---
description: "Alpaca commission-free stock, options and crypto trading."
---

# Alpaca

Alpaca commission-free stock, options and crypto trading. Trading API is pinned to the PAPER host https://paper-api.alpaca.markets (no real money). Market Data API on https://data.alpaca.markets. Live trading host api.alpaca.markets is deliberately NOT wired.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [alpaca.markets](https://alpaca.markets) |
| **Authentication** | API key, OAuth 2.0 |
| **Actions** | 90 |
| **Events** | 0 |
| **Slug** | `alpaca` |

## Use it

Add Alpaca from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.alpaca.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Asset To Watchlist | `addAssetToWatchlist` | Append one symbol to an existing watchlist by watchlist id. |
| Add Asset To Watchlist By Name | `addAssetToWatchlistByName` | Append one symbol to a watchlist addressed by name. |
| Cancel All Orders | `cancelAllOrders` | Cancel every open order on the PAPER account. Returns 207 Multi-Status listing each order id and its cancel status. |
| Cancel Order By ID | `cancelOrderById` | Cancel a single open order by id on the PAPER account. Returns 204 No Content on success. |
| Cancel Order By ID (legacy v1) | `cancelOrderByIdV1` | DEPRECATED legacy v1 Trading API mirror of Cancel Order By ID, PAPER host only. Returns 204. Prefer cancelOrderById (v2). |
| Close All Positions | `closeAllPositions` | Liquidate every open PAPER position. Set cancel_orders=true to also cancel resting orders. Returns 207 Multi-Status. |
| Close Position | `closePosition` | Liquidate one PAPER position by symbol, optionally a partial qty or percentage. Returns the closing order. |
| Create Order | `createOrder` | Place an order on the PAPER trading account. No real money is involved. Supports market/limit/stop/stop_limit/trailing_stop, qty or notional, and optional client_order_id. |
| Create Order (legacy v1) | `createOrderV1` | DEPRECATED legacy v1 Trading API mirror of Create Order, on the PAPER host only. Prefer createOrder (v2). |
| Create Watchlist | `createWatchlist` | Create a named watchlist with an initial list of symbols. |
| Delete Watchlist By ID | `deleteWatchlistById` | Delete a watchlist by id. Returns 204 No Content. |
| Delete Watchlist By Name | `deleteWatchlistByName` | Delete a watchlist addressed by name. Returns 204 No Content. |
| Do Not Exercise Options Position | `doNotExerciseOptionsPosition` | Submit a do-not-exercise (DNE) instruction for a held option contract on the PAPER account, overriding auto-exercise at expiry. |
| Exercise Options Position | `exerciseOptionsPosition` | Submit an exercise instruction for a held option contract on the PAPER account. Requires an open long option position. |
| Get Account | `getAccount` | Returns the Alpaca paper trading account (cash, buying power, equity, status). |
| Get Account (legacy v1) | `getAccountV1` | DEPRECATED legacy v1 Trading API mirror of Get Account. Undocumented but live on the paper host. Prefer getAccount (v2). |
| Get Account Activities | `getAccountActivities` | Returns account activities (fills, journals, dividends, fees). Filter with activity_types, date range and pagination. |
| Get Account Activities By Type | `getAccountActivitiesByType` | Returns account activities of one specific activity type, e.g. FILL, JNLC, DIV. |
| Get Account Configurations | `getAccountConfigurations` | Returns the current account configuration values (shorting, margin multiplier, trade confirm email, PDT check). |
| Get Account Portfolio History | `getAccountPortfolioHistory` | Timeseries of equity and profit/loss for the paper account over a period. |
| Get All Open Positions | `getAllOpenPositions` | List every open position in the PAPER account. |
| Get All Open Positions (legacy v1) | `getAllOpenPositionsV1` | DEPRECATED legacy v1 Trading API mirror of Get All Open Positions. Prefer getAllOpenPositions (v2). |
| Get Asset By Symbol Or ID | `getAssetBySymbolOrId` | Get a single asset by its ticker symbol or asset UUID. |
| Get Asset By Symbol Or ID (legacy v1) | `getAssetBySymbolOrIdV1` | DEPRECATED legacy v1 Trading API mirror of Get Asset By Symbol Or ID. Prefer getAssetBySymbolOrId (v2). |
| Get Assets | `getAssets` | List tradable assets, filterable by status, asset_class, exchange and attributes. |
| Get Assets (legacy v1) | `getAssetsV1` | DEPRECATED legacy v1 Trading API mirror of Get Assets. Prefer getAssets (v2). |
| Get Calendar | `getCalendar` | US market trading calendar (open/close/session times and settlement dates) for a date range. |
| Get Clock | `getClock` | Current US market clock: whether the market is open and the next open/close timestamps. |
| Get Company Logo | `getCompanyLogo` | Company logo image for a ticker symbol. Requires a market data subscription that includes logos; otherwise the vendor returns 403 "Subscription does not permit querying logos". |
| Get Corporate Action Announcement By ID | `getCorporateActionAnnouncementById` | Get one corporate action announcement by its announcement id. |
| Get Corporate Action Announcements | `getCorporateActionAnnouncements` | List corporate action announcements (dividends, splits, mergers) in a date window. |
| Get Corporate Actions Data | `getCorporateActionsData` | Historical corporate actions (dividends, splits, spin-offs) from the market data API. |
| Get Crypto Bars | `getCryptoBars` | Historical OHLCV bars for crypto pairs on the US venue, e.g. symbols=BTC/USD. |
| Get Crypto Quotes | `getCryptoQuotes` | Historical quotes for crypto pairs on the US venue. |
| Get Crypto Snapshots | `getCryptoSnapshots` | Snapshot (latest trade, quote, minute bar, daily bar) for each requested crypto pair. |
| Get Crypto Trades | `getCryptoTrades` | Historical trade prints for crypto pairs on the US venue. |
| Get Historical Forex Rates | `getHistoricalForexRates` | Historical FX rates for currency pairs. Requires a forex-enabled market data subscription; otherwise the vendor returns 403 "forbidden: insufficient grants". |
| Get Latest Crypto Bars | `getLatestCryptoBars` | Latest minute bar for each requested crypto pair. |
| Get Latest Crypto Orderbooks | `getLatestCryptoOrderbooks` | Latest order book (bids and asks) for each requested crypto pair. |
| Get Latest Crypto Quotes | `getLatestCryptoQuotes` | Latest bid/ask quote for each requested crypto pair. |
| Get Latest Crypto Trades | `getLatestCryptoTrades` | Latest trade print for each requested crypto pair. |
| Get Latest Forex Rates | `getLatestForexRates` | Latest FX rates for currency pairs. Requires a forex-enabled market data subscription; otherwise the vendor returns 403 "forbidden: insufficient grants". |
| Get Latest Option Quotes | `getLatestOptionQuotes` | Latest bid/ask quote for each requested option contract symbol. |
| Get Latest Option Trades | `getLatestOptionTrades` | Latest trade print for each requested option contract symbol. |
| Get Latest Stock Bar Single Symbol | `getLatestStockBarSingle` | Most recent minute bar for one stock symbol (single-symbol route). |
| Get Latest Stock Bars | `getLatestStockBars` | Most recent minute bar for each requested stock symbol. |
| Get Latest Stock Quote Single Symbol | `getLatestStockQuoteSingle` | Latest NBBO quote for one stock symbol (single-symbol route). |
| Get Latest Stock Quotes | `getLatestStockQuotes` | Latest NBBO quote for each requested stock symbol. |
| Get Latest Stock Trade Single Symbol | `getLatestStockTradeSingle` | Latest trade print for one stock symbol (single-symbol route). |
| Get Latest Stock Trades | `getLatestStockTrades` | Latest trade print for each requested stock symbol. |
| Get Most Active Stocks | `getMostActiveStocks` | Screener: most active stocks by trade count or volume. |
| Get News | `getNews` | Market news articles, optionally filtered by symbols and date range. |
| Get Open Position | `getOpenPosition` | Get one open position by symbol or asset id. |
| Get Open Position (legacy v1) | `getOpenPositionV1` | DEPRECATED legacy v1 Trading API mirror of Get Open Position. Prefer getOpenPosition (v2). |
| Get Option Bars | `getOptionBars` | Historical OHLCV bars for one or more option contract symbols. |
| Get Option Chain | `getOptionChain` | Full option chain snapshot for an underlying symbol, filterable by expiration, strike and type. |
| Get Option Condition Codes | `getOptionConditionCodes` | Mapping of option trade or quote condition codes to descriptions. |
| Get Option Contract By Symbol Or ID | `getOptionContractBySymbolOrId` | Get a single option contract by OCC symbol or contract UUID. |
| Get Option Contracts | `getOptionContracts` | List option contracts filtered by underlying symbols, expiration, strike, type and style. |
| Get Option Exchange Codes | `getOptionExchangeCodes` | Mapping of option exchange codes to exchange names. |
| Get Option Snapshots | `getOptionSnapshots` | Snapshots (latest quote, trade and greeks) for specific option contract symbols. |
| Get Option Trades | `getOptionTrades` | Historical trade prints for one or more option contract symbols. |
| Get Order By Client Order ID | `getOrderByClientOrderId` | Retrieve a single order by the client-supplied client_order_id. |
| Get Order By Client Order ID (legacy v1) | `getOrderByClientOrderIdV1` | DEPRECATED legacy v1 Trading API mirror of Get Order By Client Order ID. Prefer getOrderByClientOrderId (v2). |
| Get Order By ID | `getOrderById` | Retrieve a single order by its Alpaca order id. |
| Get Order By ID (legacy v1) | `getOrderByIdV1` | DEPRECATED legacy v1 Trading API mirror of Get Order By ID. Prefer getOrderById (v2). |
| Get Orders | `getOrders` | List paper-account orders filtered by status, symbols, side and time range. |
| Get Orders (legacy v1) | `getOrdersV1` | DEPRECATED legacy v1 Trading API mirror of Get Orders. Prefer getOrders (v2). |
| Get Stock Auctions | `getStockAuctions` | Historical opening and closing auction prints for one or more stock symbols. |
| Get Stock Auctions Single Symbol | `getStockAuctionsSingle` | Historical auction prints for one stock symbol (single-symbol route). |
| Get Stock Bars | `getStockBars` | Historical OHLCV bars for one or more stock symbols over a timeframe. |
| Get Stock Bars Single Symbol | `getStockBarsSingle` | Historical OHLCV bars for one stock symbol (single-symbol route). |
| Get Stock Condition Codes | `getStockConditionCodes` | Mapping of trade or quote condition codes to descriptions for a given tape (A, B or C). Both ticktype and tape are required by the vendor. |
| Get Stock Exchange Codes | `getStockExchangeCodes` | Mapping of stock exchange codes to exchange names. |
| Get Stock Quotes | `getStockQuotes` | Historical NBBO quotes for one or more stock symbols. |
| Get Stock Quotes Single Symbol | `getStockQuotesSingle` | Historical NBBO quotes for one stock symbol (single-symbol route). |
| Get Stock Snapshot Single Symbol | `getStockSnapshotSingle` | Snapshot for one stock symbol (single-symbol route). |
| Get Stock Snapshots | `getStockSnapshots` | Snapshot (latest trade, quote, minute bar, daily bar, previous daily bar) for each requested stock symbol. Response is keyed by symbol. |
| Get Stock Trades | `getStockTrades` | Historical trade prints for one or more stock symbols. |
| Get Stock Trades Single Symbol | `getStockTradesSingle` | Historical trade prints for one stock symbol (single-symbol route). |
| Get Top Crypto Movers | `getTopCryptoMovers` | Screener: top crypto gainers and losers for the current session. |
| Get Top Market Movers | `getTopMarketMovers` | Screener: top stock gainers and losers for the current session. |
| Get Watchlist By ID | `getWatchlistById` | Get one watchlist and its assets by watchlist id. |
| Get Watchlist By Name | `getWatchlistByName` | Get a watchlist by its name instead of its id. |
| Get Watchlists | `getWatchlists` | List all watchlists on the account. |
| Remove Asset From Watchlist | `removeAssetFromWatchlist` | Remove one symbol from a watchlist by watchlist id and symbol. |
| Replace Order | `replaceOrder` | Replace an open order with new qty/limit/stop/trail parameters. PAPER account only. |
| Update Account Configurations | `updateAccountConfigurations` | PATCH the paper account configuration (shorting, fractional trading, suspend trade, trade confirm email, margin multiplier, PDT check). |
| Update Watchlist By ID | `updateWatchlistById` | Replace a watchlist's name and full symbol list by watchlist id. |
| Update Watchlist By Name | `updateWatchlistByName` | Replace a watchlist's name and symbol list, addressing it by its current name. |
