---
description: "Mailboxlayer is a real-time email validation and verification API by APILayer."
hidden: true
---

# Mailboxlayer

<img src="../../.gitbook/assets/connectors/mailboxlayer.png" alt="Mailboxlayer logo" width="64">

Mailboxlayer is a real-time email validation and verification API by APILayer. It checks email syntax, typos, MX records, SMTP mailbox existence, catch-all configuration, role-based and disposable/free provider status, and returns a numeric deliverability score.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [mailboxlayer.com](https://mailboxlayer.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `mailboxlayer` |

## Use it

Add Mailboxlayer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mailboxlayer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Validate Emails | `bulkValidateEmails` | Validates multiple email addresses in a single request, returning the same syntax, MX, SMTP, catch-all, role, disposable/free, and score checks as single validation for each address. Only available on Pro Plus and Enterprise Plus subscription plans. |
| Validate Email | `validateEmail` | Validates a single email address, checking syntax, MX records, SMTP mailbox existence, catch-all configuration, role-based and free/disposable provider status, and returning a numeric deliverability score. |
