---
description: "SEC EDGAR holds US company filings. Read company submissions and financial facts, and list company and mutual fund tickers."
hidden: true
---

# SEC EDGAR

<img src="../../.gitbook/assets/connectors/lg/sec-edgar.png" alt="SEC EDGAR logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [sec.gov](https://sec.gov) |
| **Authentication** | No sign-in needed |
| **Slug** | `secEdgar` |

## Setup

SEC EDGAR needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add SEC EDGAR from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.secEdgar.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Company Concept</td><td><code>getCompanyConcept</code></td><td>Get every reported value of one XBRL concept (tag) for one company, grouped by unit of measure, with filing and period details (GET data.sec.gov/api/xbrl/companyconcept/CIK##########/{taxonomy}/{tag}.json). Unknown tags return 404. Docs: https://www.sec.gov/search-filings/edgar-application-programming-interfaces</td></tr><tr><td>Get Company Submissions</td><td><code>getCompanySubmissions</code></td><td>Get a filer's profile (name, tickers, exchanges, SIC, addresses, fiscal year end) and its most recent filings (at least one year or 1,000 filings) as column arrays: accession numbers, form types, filing and report dates, primary documents (GET data.sec.gov/submissions/CIK##########.json). Older filings are listed in filings.files - fetch them with Get Submissions History File. Docs: https://www.sec.gov/search-filings/edgar-application-programming-interfaces</td></tr><tr><td>Get Submissions History File</td><td><code>getSubmissionsHistoryFile</code></td><td>Get an older batch of a filer's filings listed in filings.files of Get Company Submissions (GET data.sec.gov/submissions/{name}). Docs: https://www.sec.gov/search-filings/edgar-application-programming-interfaces</td></tr><tr><td>Get XBRL Frame</td><td><code>getXbrlFrame</code></td><td>Get one fact per company for a concept, unit and calendar period across all filers - the latest value that best fits the period (GET data.sec.gov/api/xbrl/frames/{taxonomy}/{tag}/{unit}/{period}.json). Responses can be several hundred KB. Docs: https://www.sec.gov/search-filings/edgar-application-programming-interfaces</td></tr><tr><td>List Company Tickers</td><td><code>listCompanyTickers</code></td><td>List every company ticker with its CIK and company name (GET www.sec.gov/files/company_tickers.json, about 800 KB). Object keyed by row number. Docs: https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data</td></tr><tr><td>List Company Tickers with Exchange</td><td><code>listCompanyTickersWithExchange</code></td><td>List every company ticker with CIK, name and exchange (GET www.sec.gov/files/company_tickers_exchange.json) as a fields + data table. Docs: https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data</td></tr><tr><td>List Mutual Fund Tickers</td><td><code>listMutualFundTickers</code></td><td>List mutual fund tickers with CIK, series id and class id (GET www.sec.gov/files/company_tickers_mf.json, about 1.2 MB) as a fields + data table. Docs: https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data</td></tr></tbody></table>

## Events

SEC EDGAR has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
