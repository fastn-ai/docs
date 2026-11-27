---
description: "The UK Parliament Treaties service covers treaties laid before Parliament. Search treaties and read their business items and series."
hidden: true
---

# UK Parliament Treaties API

<img src="../../.gitbook/assets/connectors/lg/uk-parliament-treaties.png" alt="UK Parliament Treaties API logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [parliament.uk](https://parliament.uk) |
| **Authentication** | No sign-in needed |
| **Slug** | `ukParliamentTreaties` |

## Setup

UK Parliament Treaties API needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect UK Parliament Treaties API from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **UK Parliament Treaties API**.
2. Select **Connect** on the UK Parliament Treaties API card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. UK Parliament Treaties API needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use UK Parliament Treaties API's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Business Item</td><td><code>getBusinessItem</code></td><td>Returns business item by ID. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>Get Treaty</td><td><code>getTreaty</code></td><td>Returns a treaty by ID. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>List Government Organisations</td><td><code>listGovernmentOrganisations</code></td><td>Returns all government organisations. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>List Series Memberships</td><td><code>listSeriesMemberships</code></td><td>Returns all series memberships. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>List Treaty Business Items</td><td><code>listTreatyBusinessItems</code></td><td>Returns business items belonging to the treaty with ID. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>Search Treaties</td><td><code>searchTreaties</code></td><td>Returns a list of treaties. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr></tbody></table>

