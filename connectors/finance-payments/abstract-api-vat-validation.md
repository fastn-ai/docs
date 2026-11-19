---
description: "AbstractAPI VAT Validation and Rates validates EU VAT numbers and returns the registered company, calculates VAT-compliant prices for a country and goods…"
hidden: true
---

# AbstractAPI VAT Validation

<img src="../../.gitbook/assets/connectors/lg/abstract-api-vat-validation.png" alt="AbstractAPI VAT Validation logo">

AbstractAPI VAT Validation and Rates validates EU VAT numbers and returns the registered company, calculates VAT-compliant prices for a country and goods category, and lists a country's current standard and reduced VAT rates.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `abstractApiVatValidation` |

## Use it

Add AbstractAPI VAT Validation from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiVatValidation.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Calculate VAT</td><td><code>calculateVat</code></td><td>Calculates a VAT-compliant price for an amount in a given country, optionally applying a reduced-rate goods category or splitting VAT out of an amount that already includes it.</td></tr><tr><td>List VAT Categories</td><td><code>listVatCategories</code></td><td>Lists the current VAT rates for a country, including the standard rate and every reduced-rate goods category with its description.</td></tr><tr><td>Validate VAT Number</td><td><code>validateVatNumber</code></td><td>Checks whether a VAT number is valid and, if it is, returns the registered company name and address and the country it belongs to.</td></tr></tbody></table>
