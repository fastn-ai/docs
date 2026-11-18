---
description: "The CISA Known Exploited Vulnerabilities (KEV) catalog is the US Cybersecurity and Infrastructure Security Agency's authoritative, free list of…"
hidden: true
---

# CISA Known Exploited Vulnerabilities

<img src="../../.gitbook/assets/connectors/cisa-kev.png" alt="CISA Known Exploited Vulnerabilities logo" width="64">

The CISA Known Exploited Vulnerabilities (KEV) catalog is the US Cybersecurity and Infrastructure Security Agency's authoritative, free list of vulnerabilities exploited in the wild, with required actions and remediation due dates. Get the full catalog as JSON or CSV and its JSON schema. No API key needed.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [cisa.gov](https://cisa.gov) |
| **Authentication** | No authentication |
| **Slug** | `cisaKev` |

## Use it

Add CISA Known Exploited Vulnerabilities from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cisaKev.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get KEV Catalog (CSV) | `getKevCatalogCsv` | Get the full CISA Known Exploited Vulnerabilities catalog as CSV text (GET /sites/default/files/csv/known_exploited_vulnerabilities.csv, about 1 MB). Docs: https://www.cisa.gov/known-exploited-vulnerabilities-catalog |
| Get KEV Catalog (JSON) | `getKevCatalog` | Get the full CISA Known Exploited Vulnerabilities catalog as JSON: title, catalog version, release date, count and every vulnerability with CVE id, vendor, product, date added, required action, due date and ransomware use (GET /sites/default/files/feeds/known_exploited_vulnerabilities.json, about 1.8 MB). Docs: https://www.cisa.gov/known-exploited-vulnerabilities-catalog |
| Get KEV JSON Schema | `getKevSchema` | Get the JSON Schema that describes the KEV catalog JSON feed (GET /sites/default/files/feeds/known_exploited_vulnerabilities_schema.json). Docs: https://www.cisa.gov/known-exploited-vulnerabilities-catalog |
