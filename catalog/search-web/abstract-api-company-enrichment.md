---
description: "AbstractAPI Company Enrichment looks up company details from a domain. Get a company's name, logo, description, headquarters and industry."
hidden: true
---

# AbstractAPI Company Enrichment

<img src="../../.gitbook/assets/connectors/lg/abstract-api-company-enrichment.png" alt="AbstractAPI Company Enrichment logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | API key |
| **Slug** | `abstractApiCompanyEnrichment` |

## Setup

Your customers enter their API key for AbstractAPI Company Enrichment when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect AbstractAPI Company Enrichment from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AbstractAPI Company Enrichment**.
2. Select **Connect** on the AbstractAPI Company Enrichment card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AbstractAPI Company Enrichment's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Enrich Company</td><td><code>enrichCompany</code></td><td>Looks up a company by its website domain and returns its name, logo, description, founding year, headquarters address and coordinates, SIC/NAICS codes, industry, headcount, revenue, phone numbers, emails, public listing, technologies, and social profile URLs.</td></tr></tbody></table>

