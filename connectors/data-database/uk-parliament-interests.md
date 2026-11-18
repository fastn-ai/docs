---
description: "The UK Parliament Register of Members' Financial Interests API gives open data on MPs' declared interests: list interest categories and published registers,…"
hidden: true
---

# UK Parliament Register of Interests API

<img src="../../.gitbook/assets/connectors/uk-parliament-interests.png" alt="UK Parliament Register of Interests API logo" width="64">

The UK Parliament Register of Members' Financial Interests API gives open data on MPs' declared interests: list interest categories and published registers, search interests by member, category, register and published/registered/updated dates, and get one interest with its payments and details. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [parliament.uk](https://parliament.uk) |
| **Authentication** | No authentication |
| **Slug** | `ukParliamentInterests` |

## Use it

Add UK Parliament Register of Interests API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ukParliamentInterests.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Interest Category | `getCategory` | Return details of an interest category by ID. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/v1/Categories/{id}) |
| Get Register | `getRegister` | Return a published version of a register of interests by ID. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/v1/Registers/{id}) |
| Get Registered Interest | `getInterest` | Return the latest version of an interest which has been published. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/v1/Interests/{id}) |
| List Interest Categories | `listCategories` | Return a list of categories interests should be registered under, sorted by category number. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/v1/Categories) |
| List Registers | `listRegisters` | Return a list of published versions of registers of interests. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/v1/Registers) |
| Search Registered Interests | `searchInterests` | Return a list of interests that have been published on a register. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/v1/Interests) |
