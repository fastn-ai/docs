---
description: "Marketstack by APILayer delivers real-time, intraday, and historical stock market data (EOD, intraday bars, splits, dividends) across 70+ global exchanges,…"
hidden: true
---

# Marketstack

<img src="../../.gitbook/assets/connectors/lg/marketstack.png" alt="Marketstack logo">

Marketstack by APILayer delivers real-time, intraday, and historical stock market data (EOD, intraday bars, splits, dividends) across 70+ global exchanges, plus SEC company-fundamentals data (submissions, company facts, XBRL frames), ETF holdings, government bond yields, commodity prices, market indices, and analyst ratings, via its V2 REST API. Built against V2 because V1 is documented as deprecated for use after June 30, 2025 (though it still responded live during testing).

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [marketstack.com](https://marketstack.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `marketstack` |

## Use it

Add Marketstack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.marketstack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Accounts Payable Concept | `getAccountsPayableConcept` | Returns all disclosed accounts-payable XBRL facts for a single company (CIK), across every unit of measure the company reported in. |
| Get Accounts Payable XBRL Frames | `getAccountsPayableFrames` | Returns one aggregated accounts-payable (US-GAAP) fact per reporting entity, for the calendrical reporting period (frame) requested, in a given unit of measure. |
| Get Commodity Price History | `getCommodityPriceHistory` | Returns historical prices for a specific commodity over a date range, at daily, weekly, monthly, quarterly, or yearly frequency. |
| Get Commodity Prices | `getCommodityPrices` | Returns the current price for a specific commodity, from over 70 world commodities across energy, metals, industrial, agricultural, and livestock categories. Rate-limited to 1 request per minute. |
| Get Company Analyst Ratings | `getCompanyAnalystRatings` | Returns real-time buy/sell/hold analyst ratings and price targets for a stock ticker, plus 15+ years of historical ratings. Rate-limited to 1 request per minute. |
| Get Company Facts | `getCompanyFacts` | Returns all XBRL company-concepts data disclosed by a company, keyed by taxonomy and concept tag, for a specific SEC CIK code. |
| Get Company Name by CIK Code | `getCompanyNameByCik` | Returns the registered company name and details for a specific SEC Central Index Key (CIK) code. |
| Get End-of-Day Data | `getEndOfDayData` | Returns end-of-day data for one or multiple stock tickers. |
| Get End-of-Day Data for a Date | `getEndOfDayDataByDate` | Returns end-of-day data for a specific date for one or multiple stock tickers. |
| Get ETF Holdings | `getEtfHoldings` | Returns the holdings disclosed in SEC filings for a specific ETF, identified by its ticker. |

<details>

<summary>See 36 more actions</summary>

* **Get Exchange End-of-Day Data** `getExchangeEod`: Returns end-of-day data for symbols on a specific exchange, identified by its MIC.
* **Get Exchange End-of-Day Data for a Date** `getExchangeEodByDate`: Returns end-of-day data for a specific date for symbols on a specific exchange.
* **Get Exchange Intraday Data** `getExchangeIntraday`: Returns intraday data for symbols on a specific exchange.
* **Get Exchange Intraday Data for a Date** `getExchangeIntradayByDate`: Returns intraday data for a specific date for symbols on a specific exchange.
* **Get Exchange Latest End-of-Day Data** `getExchangeEodLatest`: Returns the most recent end-of-day data available for symbols on a specific exchange.
* **Get Exchange Latest Intraday Data** `getExchangeIntradayLatest`: Returns the most recent intraday data available for symbols on a specific exchange.
* **Get Government Bond Information** `getBondInfo`: Returns real-time 10-year government bond yield data for a specific country.
* **Get Intraday Data** `getIntradayData`: Returns intraday data with intervals as short as one minute for one or multiple stock tickers.
* **Get Intraday Data for a Date** `getIntradayDataByDate`: Returns intraday data for a specific date for one or multiple stock tickers.
* **Get Latest End-of-Day Data** `getLatestEndOfDayData`: Returns the most recent end-of-day data point for one or multiple stock tickers.
* **Get Latest Intraday Data** `getLatestIntradayData`: Returns the most recent intraday bar for one or multiple stock tickers.
* **Get Market Index Information** `getMarketIndexInfo`: Returns real-time and historical information for a specific stock market index/benchmark.
* **Get Real-Time Stock Price** `getRealTimeStockPrice`: Returns the live market price for a stock ticker across major global exchanges (NYSE, NASDAQ, LON, WSE, EPA, SHE, NSE, and more).
* **Get SEC Submissions** `getSecSubmissions`: Returns SEC filing submission details for a company, looked up by CIK code, CIK company name, or accession number. Optionally filtered by filing or report date range.
* **Get Stock Dividends** `getStockDividends`: Returns the dividend history for one or multiple stock symbols. Covers symbols listed on NASDAQ, PINK, SHG, NYSE, NYSE ARCA, OTCQB, and BATS.
* **Get Stock Exchange by MIC** `getExchangeByMic`: Returns detailed information for a single stock exchange identified by its Market Identifier Code (MIC).
* **Get Stock Splits** `getStockSplits`: Returns the stock split factor history for one or multiple stock symbols. Covers symbols listed on NASDAQ, PINK, SHG, NYSE, NYSE ARCA, OTCQB, and BATS.
* **Get Ticker by Symbol** `getTickerBySymbol`: Returns metadata for a single stock ticker symbol, including identifiers (CIK, ISIN, CUSIP, LEI), sector, industry, and its stock exchange.
* **Get Ticker End-of-Day Data** `getTickerEod`: Returns end-of-day data for a specific stock ticker.
* **Get Ticker End-of-Day Data for a Date** `getTickerEodByDate`: Returns end-of-day data for a specific date for a specific stock ticker.
* **Get Ticker Information** `getTickerInfo`: Returns extended company information for a ticker, including sector, industry, IPO date, fiscal year, and key executives.
* **Get Ticker Intraday Data** `getTickerIntraday`: Returns real-time and intraday data for a specific stock ticker.
* **Get Ticker Intraday Data for a Date** `getTickerIntradayByDate`: Returns intraday data for a specific date for a specific stock ticker.
* **Get Ticker Latest End-of-Day Data** `getTickerEodLatest`: Returns the most recent end-of-day data point for a specific stock ticker.
* **Get Ticker Latest Intraday Data** `getTickerIntradayLatest`: Returns the most recent intraday data point for a specific stock ticker.
* **Get Ticker Stock Dividends** `getTickerDividends`: Returns the dividend history for a specific stock ticker.
* **Get Ticker Stock Splits** `getTickerSplits`: Returns the stock split history for a specific stock ticker.
* **List Bonds by Country** `listBonds`: Returns the full list of countries for which Marketstack supports government bond data.
* **List ETFs** `listEtfs`: Returns the full list of exchange-traded fund (ETF) tickers supported by Marketstack.
* **List Market Indices** `listMarketIndices`: Returns the full list of stock market indices/benchmarks supported by Marketstack, e.g. the S&amp;P 500 and Dow Jones Industrial Average.
* **List Stock Exchanges** `listExchanges`: Returns a paginated list of the 2700+ stock exchanges Marketstack has general information for. Not every exchange listed here is supported by the ticker/EOD/intraday endpoints.
* **List Supported Currencies** `listCurrencies`: Returns a paginated list of currencies supported by the Marketstack API.
* **List Supported Timezones** `listTimezones`: Returns a paginated list of timezones supported by the Marketstack API.
* **List Tickers** `listTickers`: Returns the full paginated list of stock ticker symbols supported by Marketstack.
* **List Tickers for an Exchange** `listExchangeTickers`: Returns all tickers listed on a specific stock exchange, identified by its MIC.
* **Search CIK Code by Company Name** `searchCikByCompanyName`: Searches for SEC Central Index Key (CIK) codes by company name or a partial match of the name.

</details>
