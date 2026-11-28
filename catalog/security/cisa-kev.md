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

## Connect in Fastn

Your customers connect CISA Known Exploited Vulnerabilities from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **CISA Known Exploited Vulnerabilities**.
2. Select **Connect** on the CISA Known Exploited Vulnerabilities card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. CISA Known Exploited Vulnerabilities needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use CISA Known Exploited Vulnerabilities's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get KEV Catalog (CSV)</td><td><code>getKevCatalogCsv</code></td><td>Get the full CISA Known Exploited Vulnerabilities catalog as CSV text, about 1 MB). Docs: https://www.cisa.gov/known-exploited-vulnerabilities-catalog</td></tr><tr><td>Get KEV Catalog (JSON)</td><td><code>getKevCatalog</code></td><td>Get the full CISA Known Exploited Vulnerabilities catalog as JSON: title, catalog version, release date, count and every vulnerability with CVE id, vendor, product, date added, required action, due date and ransomware use, about 1.8 MB). Docs: https://www.cisa.gov/known-exploited-vulnerabilities-catalog</td></tr><tr><td>Get KEV JSON Schema</td><td><code>getKevSchema</code></td><td>Get the JSON Schema that describes the KEV catalog JSON feed Docs: https://www.cisa.gov/known-exploited-vulnerabilities-catalog</td></tr></tbody></table>

