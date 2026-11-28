---
description: "AbstractAPI VAT Validation checks EU VAT numbers. Validate VAT numbers, calculate VAT and list VAT categories."
hidden: true
---

# AbstractAPI VAT Validation

<img src="../../.gitbook/assets/connectors/lg/abstract-api-vat-validation.png" alt="AbstractAPI VAT Validation logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | API key |
| **Slug** | `abstractApiVatValidation` |

## Setup

Your customers enter their API key for AbstractAPI VAT Validation when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect AbstractAPI VAT Validation from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AbstractAPI VAT Validation**.
2. Select **Connect** on the AbstractAPI VAT Validation card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AbstractAPI VAT Validation's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Calculate VAT</td><td><code>calculateVat</code></td><td>Calculates a VAT-compliant price for an amount in a given country, optionally applying a reduced-rate goods category or splitting VAT out of an amount that already includes it.</td></tr><tr><td>List VAT Categories</td><td><code>listVatCategories</code></td><td>Lists the current VAT rates for a country, including the standard rate and every reduced-rate goods category with its description.</td></tr><tr><td>Validate VAT Number</td><td><code>validateVatNumber</code></td><td>Checks whether a VAT number is valid and, if it is, returns the registered company name and address and the country it belongs to.</td></tr></tbody></table>

