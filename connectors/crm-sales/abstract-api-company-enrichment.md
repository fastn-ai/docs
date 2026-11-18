---
description: "AbstractAPI Company Enrichment returns firmographic data for a company domain, including name, logo, description, headquarters, industry codes, headcount,…"
hidden: true
---

# AbstractAPI Company Enrichment

AbstractAPI Company Enrichment returns firmographic data for a company domain, including name, logo, description, headquarters, industry codes, headcount, revenue, contact details, public listing, technologies, and social profiles.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 1 |
| **Events** | 0 |
| **Slug** | `abstractApiCompanyEnrichment` |

## Use it

Add AbstractAPI Company Enrichment from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiCompanyEnrichment.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Enrich Company | `enrichCompany` | Looks up a company by its website domain and returns its name, logo, description, founding year, headquarters address and coordinates, SIC/NAICS codes, industry, headcount, revenue, phone numbers, emails, public listing, technologies, and social profile URLs. |
