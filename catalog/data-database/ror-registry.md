---
description: "ROR is the open registry of research organization identifiers. Search organizations, get one by ID and match affiliation text."
hidden: true
---

# ROR (Research Organization Registry)

<img src="../../.gitbook/assets/connectors/lg/ror-registry.png" alt="ROR (Research Organization Registry) logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [ror.org](https://ror.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `rorRegistry` |

## Setup

ROR (Research Organization Registry) needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect ROR (Research Organization Registry) from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **ROR (Research Organization Registry)**.
2. Select **Connect** on the ROR (Research Organization Registry) card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. ROR (Research Organization Registry) needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use ROR (Research Organization Registry)'s actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get API Status</td><td><code>getHeartbeat</code></td><td>Check that the ROR API is up; returns the text OK Docs: https://ror.readme.io/v2/docs/rest-api</td></tr><tr><td>Get Organization</td><td><code>getOrganization</code></td><td>Get one organization record by ROR id Docs: https://ror.readme.io/v2/docs/rest-api</td></tr><tr><td>Match Affiliation</td><td><code>matchAffiliation</code></td><td>Match a free-text affiliation string (e.g. from a paper's author list) to ROR organizations, each with a score, matching type and a 'chosen' flag for a confident match Docs: https://ror.readme.io/v2/docs/rest-api</td></tr><tr><td>Search Organizations</td><td><code>searchOrganizations</code></td><td>Search the Research Organization Registry by name, acronym, alias or external id, or with Elasticsearch query syntax, filter by type, status, country or continent, and page through results 20 at a time Docs: https://ror.readme.io/v2/docs/rest-api</td></tr></tbody></table>

