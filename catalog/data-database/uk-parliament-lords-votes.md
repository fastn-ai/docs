---
description: "The UK Parliament Lords Votes service covers House of Lords votes. Search and count divisions, get results by party and read member voting records."
hidden: true
---

# UK Parliament Lords Votes API

<img src="../../.gitbook/assets/connectors/lg/uk-parliament-lords-votes.png" alt="UK Parliament Lords Votes API logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [parliament.uk](https://parliament.uk) |
| **Authentication** | No sign-in needed |
| **Slug** | `ukParliamentLordsVotes` |

## Setup

UK Parliament Lords Votes API needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add UK Parliament Lords Votes API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ukParliamentLordsVotes.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Count Divisions</td><td><code>countDivisions</code></td><td>Return total results count. Get total count of Divisions meeting the specified query, useful for paging lists etc. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>Get Division</td><td><code>getDivision</code></td><td>Return a Division. Get a single Division which has the Id specified. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>Get Divisions Grouped by Party</td><td><code>getDivisionsGroupedByParty</code></td><td>Return Divisions results grouped by party. Get a list of Divisions which contain grouped by party. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>Get Member Voting Records</td><td><code>getMemberVoting</code></td><td>Return voting records for a Member. Get a list of voting records for a Member. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>Search Divisions</td><td><code>searchDivisions</code></td><td>Return a list of Divisions. Get a list of Divisions which meet the specified criteria. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr></tbody></table>

## Events

UK Parliament Lords Votes API has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
