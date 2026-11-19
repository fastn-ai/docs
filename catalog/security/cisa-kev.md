---
description: "The CISA Known Exploited Vulnerabilities catalog lists flaws attacked in the wild. Download the full catalog as JSON or CSV."
hidden: true
---

# CISA Known Exploited Vulnerabilities

<img src="../../.gitbook/assets/connectors/lg/cisa-kev.png" alt="CISA Known Exploited Vulnerabilities logo">

| | |
| --- | --- |
| **Category** | [Security](README.md) |
| **Website** | [cisa.gov](https://cisa.gov) |
| **Authentication** | No sign-in needed |
| **Slug** | `cisaKev` |

## Setup

CISA Known Exploited Vulnerabilities needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add CISA Known Exploited Vulnerabilities from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cisaKev.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get KEV Catalog (CSV)</td><td><code>getKevCatalogCsv</code></td><td>Get the full CISA Known Exploited Vulnerabilities catalog as CSV text, about 1 MB). Docs: https://www.cisa.gov/known-exploited-vulnerabilities-catalog</td></tr><tr><td>Get KEV Catalog (JSON)</td><td><code>getKevCatalog</code></td><td>Get the full CISA Known Exploited Vulnerabilities catalog as JSON: title, catalog version, release date, count and every vulnerability with CVE id, vendor, product, date added, required action, due date and ransomware use, about 1.8 MB). Docs: https://www.cisa.gov/known-exploited-vulnerabilities-catalog</td></tr><tr><td>Get KEV JSON Schema</td><td><code>getKevSchema</code></td><td>Get the JSON Schema that describes the KEV catalog JSON feed Docs: https://www.cisa.gov/known-exploited-vulnerabilities-catalog</td></tr></tbody></table>

## Events

CISA Known Exploited Vulnerabilities has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
