---
description: "The Nobel Prize data service covers every Nobel Prize and laureate. List and get prizes and laureates."
hidden: true
---

# Nobel Prize API

<img src="../../.gitbook/assets/connectors/lg/nobel-prize-api.png" alt="Nobel Prize API logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [nobelprize.org](https://nobelprize.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `nobelPrizeApi` |

## Setup

Nobel Prize API needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Nobel Prize API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nobelPrizeApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Laureate</td><td><code>getLaureate</code></td><td>Obtain information about an specific Nobel Prize Laureate. Used as unique identifier. Docs: https://www.nobelprize.org/about/developer-zone-2/ (OpenAPI https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1)</td></tr><tr><td>Get Nobel Prize</td><td><code>getNobelPrize</code></td><td>Obtain information about one specific Nobel Prize. Used as unique identifier for links. Docs: https://www.nobelprize.org/about/developer-zone-2/ (OpenAPI https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1)</td></tr><tr><td>List Laureates</td><td><code>listLaureates</code></td><td>Obtain information about Nobel Prize Laureates (persons and organizations) and their Nobel Prize(s), or search for a set of Laureates. Returns full information about the Laureates and Prizes. Docs: https://www.nobelprize.org/about/developer-zone-2/ (OpenAPI https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1)</td></tr><tr><td>List Nobel Prizes</td><td><code>listNobelPrizes</code></td><td>Obtain information about all Nobel Prizes or search for a specific set of Nobel Prizes. Note that not all information about the Laureates are provided in the output, as a request of making this endpoints response lighter. Call the laureates endpoint for full information. Docs: https://www.nobelprize.org/about/developer-zone-2/ (OpenAPI https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1)</td></tr></tbody></table>

## Events

Nobel Prize API has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
