---
description: "Connect CISA Known Exploited Vulnerabilities to your product with fastn."
hidden: true
---

# CISA Known Exploited Vulnerabilities

<img src="../../.gitbook/assets/connectors/lg/cisa-kev.png" alt="CISA Known Exploited Vulnerabilities logo">

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

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get KEV Catalog (CSV)</td><td><code>getKevCatalogCsv</code></td><td>Get the full CISA Known Exploited Vulnerabilities catalog as CSV text (GET /sites/default/files/csv/known_exploited_vulnerabilities.csv, about 1 MB). Docs: https://www.cisa.gov/known-exploited-vulnerabilities-catalog</td></tr><tr><td>Get KEV Catalog (JSON)</td><td><code>getKevCatalog</code></td><td>Get the full CISA Known Exploited Vulnerabilities catalog as JSON: title, catalog version, release date, count and every vulnerability with CVE id, vendor, product, date added, required action, due date and ransomware use (GET /sites/default/files/feeds/known_exploited_vulnerabilities.json, about 1.8 MB). Docs: https://www.cisa.gov/known-exploited-vulnerabilities-catalog</td></tr><tr><td>Get KEV JSON Schema</td><td><code>getKevSchema</code></td><td>Get the JSON Schema that describes the KEV catalog JSON feed (GET /sites/default/files/feeds/known_exploited_vulnerabilities_schema.json). Docs: https://www.cisa.gov/known-exploited-vulnerabilities-catalog</td></tr></tbody></table>
