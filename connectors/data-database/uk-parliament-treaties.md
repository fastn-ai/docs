---
description: "The UK Parliament Treaties API gives open data on treaties laid before Parliament under the CRaG Act: search treaties by text, lead government department,…"
---

# UK Parliament Treaties API

The UK Parliament Treaties API gives open data on treaties laid before Parliament under the CRaG Act: search treaties by text, lead government department, series and parliamentary process, get a treaty and its business items (laying, debates, committee reports), and list government organisations and treaty series. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [parliament.uk](https://parliament.uk) |
| **Authentication** | No authentication |
| **Actions** | 6 |
| **Events** | 0 |
| **Slug** | `ukParliamentTreaties` |

## Use it

Add UK Parliament Treaties API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ukParliamentTreaties.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Business Item | `getBusinessItem` | Returns business item by ID. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/BusinessItem/{id}) |
| Get Treaty | `getTreaty` | Returns a treaty by ID. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Treaty/{id}) |
| List Government Organisations | `listGovernmentOrganisations` | Returns all government organisations. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/GovernmentOrganisation) |
| List Series Memberships | `listSeriesMemberships` | Returns all series memberships. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/SeriesMembership) |
| List Treaty Business Items | `listTreatyBusinessItems` | Returns business items belonging to the treaty with ID. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Treaty/{id}/BusinessItems) |
| Search Treaties | `searchTreaties` | Returns a list of treaties. Docs: https://treaties-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Treaty) |
