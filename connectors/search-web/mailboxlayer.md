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

## Use it

Add Mailboxlayer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mailboxlayer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Bulk Validate Emails</td><td><code>bulkValidateEmails</code></td><td>Validates multiple email addresses in a single request, returning the same syntax, MX, SMTP, catch-all, role, disposable/free, and score checks as single validation for each address. Only available on Pro Plus and Enterprise Plus subscription plans.</td></tr><tr><td>Validate Email</td><td><code>validateEmail</code></td><td>Validates a single email address, checking syntax, MX records, SMTP mailbox existence, catch-all configuration, role-based and free/disposable provider status, and returning a numeric deliverability score.</td></tr></tbody></table>

## Events

Mailboxlayer has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
