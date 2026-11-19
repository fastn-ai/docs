---
description: "Connect UK Parliament Register of Interests API to your product with fastn."
hidden: true
---

# UK Parliament Register of Interests API

<img src="../../.gitbook/assets/connectors/lg/uk-parliament-interests.png" alt="UK Parliament Register of Interests API logo">

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

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Interest Category</td><td><code>getCategory</code></td><td>Return details of an interest category by ID. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/v1/Categories/{id})</td></tr><tr><td>Get Register</td><td><code>getRegister</code></td><td>Return a published version of a register of interests by ID. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/v1/Registers/{id})</td></tr><tr><td>Get Registered Interest</td><td><code>getInterest</code></td><td>Return the latest version of an interest which has been published. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/v1/Interests/{id})</td></tr><tr><td>List Interest Categories</td><td><code>listCategories</code></td><td>Return a list of categories interests should be registered under, sorted by category number. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/v1/Categories)</td></tr><tr><td>List Registers</td><td><code>listRegisters</code></td><td>Return a list of published versions of registers of interests. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/v1/Registers)</td></tr><tr><td>Search Registered Interests</td><td><code>searchInterests</code></td><td>Return a list of interests that have been published on a register. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/v1/Interests)</td></tr></tbody></table>
