---
description: "Connect ROR (Research Organization Registry) to your product with fastn."
hidden: true
---

# ROR (Research Organization Registry)

<img src="../../.gitbook/assets/connectors/lg/ror-registry.png" alt="ROR (Research Organization Registry) logo">

ROR (Research Organization Registry) is the open global registry of persistent identifiers for 120,000+ research organizations - universities, funders, hospitals, labs and companies. Search and filter organizations, match free-text affiliation strings, and get full records with names, types, locations, external ids (GRID, ISNI, Wikidata, FundRef) and relationships. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [ror.org](https://ror.org) |
| **Authentication** | No authentication |
| **Slug** | `rorRegistry` |

## Use it

Add ROR (Research Organization Registry) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.rorRegistry.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get API Status</td><td><code>getHeartbeat</code></td><td>Check that the ROR API is up; returns the text OK (GET /v2/heartbeat). Docs: https://ror.readme.io/v2/docs/rest-api</td></tr><tr><td>Get Organization</td><td><code>getOrganization</code></td><td>Get one organization record by ROR id (GET /v2/organizations/{id}). Docs: https://ror.readme.io/v2/docs/rest-api</td></tr><tr><td>Match Affiliation</td><td><code>matchAffiliation</code></td><td>Match a free-text affiliation string (e.g. from a paper's author list) to ROR organizations, each with a score, matching type and a 'chosen' flag for a confident match (GET /v2/organizations?affiliation=). Docs: https://ror.readme.io/v2/docs/rest-api</td></tr><tr><td>Search Organizations</td><td><code>searchOrganizations</code></td><td>Search the Research Organization Registry by name, acronym, alias or external id, or with Elasticsearch query syntax, filter by type, status, country or continent, and page through results 20 at a time (GET /v2/organizations). Docs: https://ror.readme.io/v2/docs/rest-api</td></tr></tbody></table>
