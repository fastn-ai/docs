---
description: "AbstractAPI IBAN Validation checks international bank account numbers. Validate whether an IBAN is correct."
hidden: true
---

# AbstractAPI IBAN Validation

<img src="../../.gitbook/assets/connectors/lg/abstract-api-iban-validation.png" alt="AbstractAPI IBAN Validation logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | API key |
| **Slug** | `abstractApiIbanValidation` |

## Setup

Your customers enter their API key for AbstractAPI IBAN Validation when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect AbstractAPI IBAN Validation from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AbstractAPI IBAN Validation**.
2. Select **Connect** on the AbstractAPI IBAN Validation card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AbstractAPI IBAN Validation's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Validate IBAN</td><td><code>validateIban</code></td><td>Checks whether an International Bank Account Number (IBAN) is valid. Spaces in the IBAN are accepted.</td></tr></tbody></table>

