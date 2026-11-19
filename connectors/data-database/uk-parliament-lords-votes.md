---
description: "The UK Parliament Lords Votes API gives open data on House of Lords divisions (votes): search divisions by title, date and member, get a division with every…"
hidden: true
---

# UK Parliament Lords Votes API

<img src="../../.gitbook/assets/connectors/lg/uk-parliament-lords-votes.png" alt="UK Parliament Lords Votes API logo">

The UK Parliament Lords Votes API gives open data on House of Lords divisions (votes): search divisions by title, date and member, get a division with every Lord's vote, count results, get a member's voting record and results grouped by party. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [parliament.uk](https://parliament.uk) |
| **Authentication** | No authentication |
| **Slug** | `ukParliamentLordsVotes` |

## Use it

Add UK Parliament Lords Votes API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ukParliamentLordsVotes.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Count Divisions</td><td><code>countDivisions</code></td><td>Return total results count. Get total count of Divisions meeting the specified query, useful for paging lists etc. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /data/Divisions/searchTotalResults)</td></tr><tr><td>Get Division</td><td><code>getDivision</code></td><td>Return a Division. Get a single Division which has the Id specified. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /data/Divisions/{divisionId})</td></tr><tr><td>Get Divisions Grouped by Party</td><td><code>getDivisionsGroupedByParty</code></td><td>Return Divisions results grouped by party. Get a list of Divisions which contain grouped by party. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /data/Divisions/groupedbyparty)</td></tr><tr><td>Get Member Voting Records</td><td><code>getMemberVoting</code></td><td>Return voting records for a Member. Get a list of voting records for a Member. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /data/Divisions/membervoting)</td></tr><tr><td>Search Divisions</td><td><code>searchDivisions</code></td><td>Return a list of Divisions. Get a list of Divisions which meet the specified criteria. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /data/Divisions/search)</td></tr></tbody></table>
