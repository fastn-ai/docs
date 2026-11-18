---
description: "AbstractAPI VAT Validation and Rates validates EU VAT numbers and returns the registered company, calculates VAT-compliant prices for a country and goods…"
---

# AbstractAPI VAT Validation

AbstractAPI VAT Validation and Rates validates EU VAT numbers and returns the registered company, calculates VAT-compliant prices for a country and goods category, and lists a country's current standard and reduced VAT rates.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 3 |
| **Events** | 0 |
| **Slug** | `abstractApiVatValidation` |

## Use it

Add AbstractAPI VAT Validation from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiVatValidation.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Calculate VAT | `calculateVat` | Calculates a VAT-compliant price for an amount in a given country, optionally applying a reduced-rate goods category or splitting VAT out of an amount that already includes it. |
| List VAT Categories | `listVatCategories` | Lists the current VAT rates for a country, including the standard rate and every reduced-rate goods category with its description. |
| Validate VAT Number | `validateVatNumber` | Checks whether a VAT number is valid and, if it is, returns the registered company name and address and the country it belongs to. |
