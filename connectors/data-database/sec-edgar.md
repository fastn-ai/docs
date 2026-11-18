---
description: "SEC EDGAR APIs from the U.S."
hidden: true
---

# SEC EDGAR

<img src="../../.gitbook/assets/connectors/sec-edgar.png" alt="SEC EDGAR logo" width="64">

SEC EDGAR APIs from the U.S. Securities and Exchange Commission give free access to company filings and XBRL financial data. Get a company's profile and filing history, every reported value of a financial concept, cross-company XBRL frames for a period, and the official ticker-to-CIK lists. No API key needed (requests carry a declared User-Agent, max 10 per second).

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [sec.gov](https://sec.gov) |
| **Authentication** | No authentication |
| **Slug** | `secEdgar` |

## Use it

Add SEC EDGAR from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.secEdgar.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Company Concept | `getCompanyConcept` | Get every reported value of one XBRL concept (tag) for one company, grouped by unit of measure, with filing and period details (GET data.sec.gov/api/xbrl/companyconcept/CIK##########/{taxonomy}/{tag}.json). Unknown tags return 404. Docs: https://www.sec.gov/search-filings/edgar-application-programming-interfaces |
| Get Company Submissions | `getCompanySubmissions` | Get a filer's profile (name, tickers, exchanges, SIC, addresses, fiscal year end) and its most recent filings (at least one year or 1,000 filings) as column arrays: accession numbers, form types, filing and report dates, primary documents (GET data.sec.gov/submissions/CIK##########.json). Older filings are listed in filings.files - fetch them with Get Submissions History File. Docs: https://www.sec.gov/search-filings/edgar-application-programming-interfaces |
| Get Submissions History File | `getSubmissionsHistoryFile` | Get an older batch of a filer's filings listed in filings.files of Get Company Submissions (GET data.sec.gov/submissions/{name}). Docs: https://www.sec.gov/search-filings/edgar-application-programming-interfaces |
| Get XBRL Frame | `getXbrlFrame` | Get one fact per company for a concept, unit and calendar period across all filers - the latest value that best fits the period (GET data.sec.gov/api/xbrl/frames/{taxonomy}/{tag}/{unit}/{period}.json). Responses can be several hundred KB. Docs: https://www.sec.gov/search-filings/edgar-application-programming-interfaces |
| List Company Tickers | `listCompanyTickers` | List every company ticker with its CIK and company name (GET www.sec.gov/files/company_tickers.json, about 800 KB). Object keyed by row number. Docs: https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data |
| List Company Tickers with Exchange | `listCompanyTickersWithExchange` | List every company ticker with CIK, name and exchange (GET www.sec.gov/files/company_tickers_exchange.json) as a fields + data table. Docs: https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data |
| List Mutual Fund Tickers | `listMutualFundTickers` | List mutual fund tickers with CIK, series id and class id (GET www.sec.gov/files/company_tickers_mf.json, about 1.2 MB) as a fields + data table. Docs: https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data |
