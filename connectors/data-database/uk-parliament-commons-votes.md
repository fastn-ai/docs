---
description: "The UK Parliament Commons Votes API gives open data on House of Commons divisions (votes): search divisions by title, date and member, get a division with…"
hidden: true
---

# UK Parliament Commons Votes API

<img src="../../.gitbook/assets/connectors/uk-parliament-commons-votes.png" alt="UK Parliament Commons Votes API logo" width="64">

The UK Parliament Commons Votes API gives open data on House of Commons divisions (votes): search divisions by title, date and member, get a division with every MP's Aye/No vote, count results, get an MP's voting record and results grouped by party. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [parliament.uk](https://parliament.uk) |
| **Authentication** | No authentication |
| **Slug** | `ukParliamentCommonsVotes` |

## Use it

Add UK Parliament Commons Votes API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ukParliamentCommonsVotes.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Count Divisions | `countDivisions` | Return total results count. Total count of Divisions meeting the specified criteria. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1) (GET /data/divisions.{format}/searchTotalResults) |
| Get Division | `getDivision` | Return a Division. Single Division which has the specified Id. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1) (GET /data/division/{divisionId}.{format}) |
| Get Divisions Grouped by Party | `getDivisionsGroupedByParty` | Return Divisions results grouped by party. Division results which meet the specified criteria grouped by parties. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1) (GET /data/divisions.{format}/groupedbyparty) |
| Get Member Voting Records | `getMemberVoting` | Return voting records for a Member. List of voting records for a member which meet the specified criteria. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1) (GET /data/divisions.{format}/membervoting) |
| Search Divisions | `searchDivisions` | Return a list of Divisions. List of Divisions which meet the specified criteria. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1) (GET /data/divisions.{format}/search) |
