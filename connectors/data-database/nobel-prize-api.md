---
description: "The official Nobel Prize API (Nobel Prize Outreach, v2.1) gives open data on every Nobel Prize and laureate since 1901: list and filter prizes by year and…"
hidden: true
---

# Nobel Prize API

The official Nobel Prize API (Nobel Prize Outreach, v2.1) gives open data on every Nobel Prize and laureate since 1901: list and filter prizes by year and category, get one prize, search laureates by name, gender, birth/death place and date, affiliation and motivation, and get full laureate records, as JSON or CSV. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [nobelprize.org](https://nobelprize.org) |
| **Authentication** | No authentication |
| **Actions** | 4 |
| **Events** | 0 |
| **Slug** | `nobelPrizeApi` |

## Use it

Add Nobel Prize API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nobelPrizeApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Laureate | `getLaureate` | Obtain information about an specific Nobel Prize Laureate. Used as unique identifier. Docs: https://www.nobelprize.org/about/developer-zone-2/ (OpenAPI https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1) (GET /laureate/{laureateID}) |
| Get Nobel Prize | `getNobelPrize` | Obtain information about one specific Nobel Prize. Used as unique identifier for links. Docs: https://www.nobelprize.org/about/developer-zone-2/ (OpenAPI https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1) (GET /nobelPrize/{category}/{year}) |
| List Laureates | `listLaureates` | Obtain information about Nobel Prize Laureates (persons and organizations) and their Nobel Prize(s), or search for a set of Laureates. Returns full information about the Laureates and Prizes. Docs: https://www.nobelprize.org/about/developer-zone-2/ (OpenAPI https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1) (GET /laureates) |
| List Nobel Prizes | `listNobelPrizes` | Obtain information about all Nobel Prizes or search for a specific set of Nobel Prizes. Note that not all information about the Laureates are provided in the output, as a request of making this endpoints response lighter. Call the laureates endpoint for full information. Docs: https://www.nobelprize.org/about/developer-zone-2/ (OpenAPI https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1) (GET /nobelPrizes) |
