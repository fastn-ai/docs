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

## Use it

Add AbstractAPI VAT Validation from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiVatValidation.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Calculate VAT</td><td><code>calculateVat</code></td><td>Calculates a VAT-compliant price for an amount in a given country, optionally applying a reduced-rate goods category or splitting VAT out of an amount that already includes it.</td></tr><tr><td>List VAT Categories</td><td><code>listVatCategories</code></td><td>Lists the current VAT rates for a country, including the standard rate and every reduced-rate goods category with its description.</td></tr><tr><td>Validate VAT Number</td><td><code>validateVatNumber</code></td><td>Checks whether a VAT number is valid and, if it is, returns the registered company name and address and the country it belongs to.</td></tr></tbody></table>

## Events

AbstractAPI VAT Validation has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
