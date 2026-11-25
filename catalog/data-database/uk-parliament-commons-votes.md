---
description: "The UK Parliament Commons Votes service covers House of Commons votes. Search and count divisions, get results by party and read member voting records."
hidden: true
---

# UK Parliament Commons Votes API

<img src="../../.gitbook/assets/connectors/lg/uk-parliament-commons-votes.png" alt="UK Parliament Commons Votes API logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [parliament.uk](https://parliament.uk) |
| **Authentication** | No sign-in needed |
| **Slug** | `ukParliamentCommonsVotes` |

## Setup

UK Parliament Commons Votes API needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add UK Parliament Commons Votes API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ukParliamentCommonsVotes.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Count Divisions</td><td><code>countDivisions</code></td><td>Return total results count. Total count of Divisions meeting the specified criteria. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1)</td></tr><tr><td>Get Division</td><td><code>getDivision</code></td><td>Return a Division. Single Division which has the specified Id. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1)</td></tr><tr><td>Get Divisions Grouped by Party</td><td><code>getDivisionsGroupedByParty</code></td><td>Return Divisions results grouped by party. Division results which meet the specified criteria grouped by parties. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1)</td></tr><tr><td>Get Member Voting Records</td><td><code>getMemberVoting</code></td><td>Return voting records for a Member. List of voting records for a member which meet the specified criteria. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1)</td></tr><tr><td>Search Divisions</td><td><code>searchDivisions</code></td><td>Return a list of Divisions. List of Divisions which meet the specified criteria. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1)</td></tr></tbody></table>

## Events

UK Parliament Commons Votes API has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
