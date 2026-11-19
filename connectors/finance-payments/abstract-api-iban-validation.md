---
description: "AbstractAPI IBAN Validation checks whether an International Bank Account Number (IBAN) is valid."
hidden: true
---

# AbstractAPI IBAN Validation

<img src="../../.gitbook/assets/connectors/lg/abstract-api-iban-validation.png" alt="AbstractAPI IBAN Validation logo">

AbstractAPI IBAN Validation checks whether an International Bank Account Number (IBAN) is valid.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `abstractApiIbanValidation` |

## Use it

Add AbstractAPI IBAN Validation from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiIbanValidation.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Validate IBAN</td><td><code>validateIban</code></td><td>Checks whether an International Bank Account Number (IBAN) is valid. Spaces in the IBAN are accepted.</td></tr></tbody></table>
