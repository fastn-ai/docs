---
description: "The UK Parliament Treaties API gives open data on treaties laid before Parliament under the CRaG Act: search treaties by text, lead government department,…"
hidden: true
---

# UK Parliament Treaties API

<img src="../../.gitbook/assets/connectors/lg/uk-parliament-treaties.png" alt="UK Parliament Treaties API logo">

The UK Parliament Treaties API gives open data on treaties laid before Parliament under the CRaG Act: search treaties by text, lead government department, series and parliamentary process, get a treaty and its business items (laying, debates, committee reports), and list government organisations and treaty series. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [parliament.uk](https://parliament.uk) |
| **Authentication** | No authentication |
| **Slug** | `ukParliamentTreaties` |

## Use it

Add UK Parliament Treaties API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ukParliamentTreaties.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Business Item</td><td><code>getBusinessItem</code></td><td>Returns business item by ID. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/BusinessItem/{id})</td></tr><tr><td>Get Treaty</td><td><code>getTreaty</code></td><td>Returns a treaty by ID. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Treaty/{id})</td></tr><tr><td>List Government Organisations</td><td><code>listGovernmentOrganisations</code></td><td>Returns all government organisations. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/GovernmentOrganisation)</td></tr><tr><td>List Series Memberships</td><td><code>listSeriesMemberships</code></td><td>Returns all series memberships. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/SeriesMembership)</td></tr><tr><td>List Treaty Business Items</td><td><code>listTreatyBusinessItems</code></td><td>Returns business items belonging to the treaty with ID. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Treaty/{id}/BusinessItems)</td></tr><tr><td>Search Treaties</td><td><code>searchTreaties</code></td><td>Returns a list of treaties. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Treaty)</td></tr></tbody></table>
