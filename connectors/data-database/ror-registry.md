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

## Use it

Add ROR (Research Organization Registry) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.rorRegistry.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get API Status</td><td><code>getHeartbeat</code></td><td>Check that the ROR API is up; returns the text OK Docs: https://ror.readme.io/v2/docs/rest-api</td></tr><tr><td>Get Organization</td><td><code>getOrganization</code></td><td>Get one organization record by ROR id Docs: https://ror.readme.io/v2/docs/rest-api</td></tr><tr><td>Match Affiliation</td><td><code>matchAffiliation</code></td><td>Match a free-text affiliation string (e.g. from a paper's author list) to ROR organizations, each with a score, matching type and a 'chosen' flag for a confident match Docs: https://ror.readme.io/v2/docs/rest-api</td></tr><tr><td>Search Organizations</td><td><code>searchOrganizations</code></td><td>Search the Research Organization Registry by name, acronym, alias or external id, or with Elasticsearch query syntax, filter by type, status, country or continent, and page through results 20 at a time Docs: https://ror.readme.io/v2/docs/rest-api</td></tr></tbody></table>

## Events

ROR (Research Organization Registry) has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
