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

## Connect in Fastn

Your customers connect UK Parliament Commons Votes API from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **UK Parliament Commons Votes API**.
2. Select **Connect** on the UK Parliament Commons Votes API card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. UK Parliament Commons Votes API needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use UK Parliament Commons Votes API's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Count Divisions</td><td><code>countDivisions</code></td><td>Return total results count. Total count of Divisions meeting the specified criteria. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1)</td></tr><tr><td>Get Division</td><td><code>getDivision</code></td><td>Return a Division. Single Division which has the specified Id. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1)</td></tr><tr><td>Get Divisions Grouped by Party</td><td><code>getDivisionsGroupedByParty</code></td><td>Return Divisions results grouped by party. Division results which meet the specified criteria grouped by parties. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1)</td></tr><tr><td>Get Member Voting Records</td><td><code>getMemberVoting</code></td><td>Return voting records for a Member. List of voting records for a member which meet the specified criteria. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1)</td></tr><tr><td>Search Divisions</td><td><code>searchDivisions</code></td><td>Return a list of Divisions. List of Divisions which meet the specified criteria. Docs: https://commonsvotes-api.parliament.uk/swagger/ui/index (Swagger /swagger/docs/v1)</td></tr></tbody></table>

