---
description: "FIRST is the global forum of incident response teams. Get exploit prediction scores for vulnerabilities and list member teams and news."
hidden: true
---

# FIRST.Org API

<img src="../../.gitbook/assets/connectors/lg/first-org-api.png" alt="FIRST.Org API logo">

| | |
| --- | --- |
| **Category** | [Security](README.md) |
| **Website** | [first.org](https://first.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `firstOrgApi` |

## Setup

FIRST.Org API needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect FIRST.Org API from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **FIRST.Org API**.
2. Select **Connect** on the FIRST.Org API card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. FIRST.Org API needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use FIRST.Org API's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get EPSS Scores</td><td><code>getEpssScores</code></td><td>Get Exploit Prediction Scoring System (EPSS) scores and percentiles for CVEs: by CVE list, date, score or percentile range, recency, or a 30-day time series Docs: https://api.first.org/epss</td></tr><tr><td>List Countries</td><td><code>listCountries</code></td><td>List countries (ISO 3166-1) with their region, keyed by country code Docs: https://api.first.org/v1/get-countries</td></tr><tr><td>List FIRST Member Teams</td><td><code>listTeams</code></td><td>List or search FIRST member incident response teams (CSIRTs/PSIRTs) with their public profile: name, host, country, contacts, constituency Docs: https://api.first.org/v1/get-teams</td></tr><tr><td>List FIRST News</td><td><code>listNews</code></td><td>List FIRST news items (title, summary, link, published date), newest first, with channel, date and text filters Docs: https://api.first.org/v1/get-news</td></tr><tr><td>List Global IRT Teams</td><td><code>listGlobalIrtTeams</code></td><td>List incident response teams in the Global IRT directory format (short/official name, postal address, country code, e-mail, host, phone numbers). Set envelope=true to get the total count in the body Docs: https://api.first.org/global-irt/v1</td></tr><tr><td>List News Channels</td><td><code>listNewsChannels</code></td><td>List FIRST news channels with their HTML and RSS links Docs: https://api.first.org/v1/get-channels</td></tr></tbody></table>

