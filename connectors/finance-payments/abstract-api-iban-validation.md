---
description: "AbstractAPI IBAN Validation checks whether an International Bank Account Number (IBAN) is valid."
hidden: true
---

# AbstractAPI IBAN Validation

AbstractAPI IBAN Validation checks whether an International Bank Account Number (IBAN) is valid.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 1 |
| **Events** | 0 |
| **Slug** | `abstractApiIbanValidation` |

## Use it

Add AbstractAPI IBAN Validation from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiIbanValidation.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Validate IBAN | `validateIban` | Checks whether an International Bank Account Number (IBAN) is valid. Spaces in the IBAN are accepted. |
