---
description: "Mailboxlayer validates email addresses. Check one email or a list for syntax, mail server and mailbox existence."
hidden: true
---

# Mailboxlayer

<img src="../../.gitbook/assets/connectors/lg/mailboxlayer.png" alt="Mailboxlayer logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [mailboxlayer.com](https://mailboxlayer.com) |
| **Authentication** | API key |
| **Slug** | `mailboxlayer` |

## Setup

Your customers enter their API key for Mailboxlayer when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Mailboxlayer from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Mailboxlayer**.
2. Select **Connect** on the Mailboxlayer card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Mailboxlayer's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Bulk Validate Emails</td><td><code>bulkValidateEmails</code></td><td>Validates multiple email addresses in a single request, returning the same syntax, MX, SMTP, catch-all, role, disposable/free, and score checks as single validation for each address. Only available on Pro Plus and Enterprise Plus subscription plans.</td></tr><tr><td>Validate Email</td><td><code>validateEmail</code></td><td>Validates a single email address, checking syntax, MX records, SMTP mailbox existence, catch-all configuration, role-based and free/disposable provider status, and returning a numeric deliverability score.</td></tr></tbody></table>

