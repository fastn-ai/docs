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

## Connect in Fastn

Your customers connect UK Parliament Lords Votes API from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **UK Parliament Lords Votes API**.
2. Select **Connect** on the UK Parliament Lords Votes API card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. UK Parliament Lords Votes API needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use UK Parliament Lords Votes API's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Count Divisions</td><td><code>countDivisions</code></td><td>Return total results count. Get total count of Divisions meeting the specified query, useful for paging lists etc. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>Get Division</td><td><code>getDivision</code></td><td>Return a Division. Get a single Division which has the Id specified. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>Get Divisions Grouped by Party</td><td><code>getDivisionsGroupedByParty</code></td><td>Return Divisions results grouped by party. Get a list of Divisions which contain grouped by party. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>Get Member Voting Records</td><td><code>getMemberVoting</code></td><td>Return voting records for a Member. Get a list of voting records for a Member. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>Search Divisions</td><td><code>searchDivisions</code></td><td>Return a list of Divisions. Get a list of Divisions which meet the specified criteria. Docs: https://lordsvotes-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr></tbody></table>

