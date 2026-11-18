---
description: "The FIRST.Org API is the free public API of the Forum of Incident Response and Security Teams."
hidden: true
---

# FIRST.Org API

<img src="../../.gitbook/assets/connectors/lg/first-org-api.png" alt="FIRST.Org API logo">

The FIRST.Org API is the free public API of the Forum of Incident Response and Security Teams. Get EPSS exploit-prediction scores for CVEs (current, historic and 30-day series), search FIRST member CSIRT/PSIRT teams and the Global IRT directory, and read FIRST news, news channels and the country list. No API key needed (1000 requests per minute).

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [first.org](https://first.org) |
| **Authentication** | No authentication |
| **Slug** | `firstOrgApi` |

## Use it

Add FIRST.Org API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.firstOrgApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get EPSS Scores | `getEpssScores` | Get Exploit Prediction Scoring System (EPSS) scores and percentiles for CVEs: by CVE list, date, score or percentile range, recency, or a 30-day time series (GET /data/v1/epss). Docs: https://api.first.org/epss |
| List Countries | `listCountries` | List countries (ISO 3166-1) with their region, keyed by country code (GET /data/v1/countries). Docs: https://api.first.org/v1/get-countries |
| List FIRST Member Teams | `listTeams` | List or search FIRST member incident response teams (CSIRTs/PSIRTs) with their public profile: name, host, country, contacts, constituency (GET /data/v1/teams). Docs: https://api.first.org/v1/get-teams |
| List FIRST News | `listNews` | List FIRST news items (title, summary, link, published date), newest first, with channel, date and text filters (GET /data/v1/news). Docs: https://api.first.org/v1/get-news |
| List Global IRT Teams | `listGlobalIrtTeams` | List incident response teams in the Global IRT directory format (short/official name, postal address, country code, e-mail, host, phone numbers). Set envelope=true to get the total count in the body (GET /global-irt/v1/teams). Docs: https://api.first.org/global-irt/v1 |
| List News Channels | `listNewsChannels` | List FIRST news channels with their HTML and RSS links (GET /data/v1/channels). Docs: https://api.first.org/v1/get-channels |
