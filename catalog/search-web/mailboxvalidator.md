---
description: "MailboxValidator validates email addresses. Check an address, and detect disposable and free email providers."
hidden: true
---

# MailboxValidator

<img src="../../.gitbook/assets/connectors/lg/mailboxvalidator.png" alt="MailboxValidator logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [mailboxvalidator.com](https://mailboxvalidator.com) |
| **Authentication** | API key |
| **Slug** | `mailboxvalidator` |

## Setup

Your customers enter their API key for MailboxValidator when they connect. Nothing else needs setting up.

## Use it

Add MailboxValidator from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mailboxvalidator.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check Disposable Email Address</td><td><code>checkDisposableEmailAddress</code></td><td>Checks whether one email address comes from a disposable (temporary, throw-away) email provider Use it to block fake sign-ups, trial abuse and promotion abuse at the point of registration. Consumes one credit from the same shared balance as the other endpoints. A syntactically invalid address</td></tr><tr><td>Check Disposable Email Address (Legacy V1)</td><td><code>checkDisposableEmailAddressLegacyV1</code></td><td>Legacy v1 disposable-email lookup Undocumented on the MailboxValidator documentation site but live. Prefer Check Disposable Email Address (v2) for new work; use this only to match an existing v1 integration. Differences from v2: is_disposable arrives as the STRING "True"/"False", and errors are returned with HTTP 200 carrying non-empty error_code and error_message fields instead of an HTTP 4xx, so callers must inspect error_code rather than the status code. Consumes one credit from the same shared balance.</td></tr><tr><td>Check Free Email Provider</td><td><code>checkFreeEmailProvider</code></td><td>Checks whether one email address belongs to a free email service provider such as Gmail, Hotmail, Yahoo or AOL Use it to require a corporate address at sign-up or to segment a list. Much cheaper in response size than full validation but it still consumes one credit from the same shared balance. Unlike Validate Email Address, a syntactically invalid address here</td></tr><tr><td>Check Free Email Provider (Legacy V1)</td><td><code>checkFreeEmailProviderLegacyV1</code></td><td>Legacy v1 free-email-provider lookup Undocumented on the MailboxValidator documentation site but live. Prefer Check Free Email Provider (v2) for new work; use this only to match an existing v1 integration. Differences from v2: is_free arrives as the STRING "True"/"False", and errors are returned with HTTP 200 carrying non-empty error_code and error_message fields instead of an HTTP 4xx, so callers must inspect error_code rather than the status code. Consumes one credit from the same shared balance.</td></tr><tr><td>Validate Email Address</td><td><code>validateEmailAddress</code></td><td>Runs the full MailboxValidator v2 single email validation on one address and returns every check: syntax, MX record, SMTP server reachability, mailbox verification, server-down, greylisting, disposable, suppression list, role-based, high-risk, catch-all, DMARC enforcement, strict SPF, website existence, plus the mailboxvalidator_score reputation score and an overall status. BILLING TRAP: this endpoint consumes one credit even when the address is syntactically invalid - it answers HTTP 200 with is_syntax=false rather than an error, so a bad address costs the same as a good one. There is no free syntax pre-check and no credit-balance endpoint; credits_available in the response is the only way to read the remaining balance, and reading it costs a credit. Yahoo addresses are not supported by the vendor.</td></tr><tr><td>Validate Email Address (Legacy V1)</td><td><code>validateEmailAddressLegacyV1</code></td><td>Legacy v1 single email validation This endpoint is not listed on the MailboxValidator documentation site but is still live and is the only path described by the host's own machine-readable spec at https://api.mailboxvalidator.com/openapi.json. Prefer Validate Email Address (v2) for new work; use this only to match an existing v1 integration byte for byte. Three differences from v2: booleans arrive as the STRINGS "True"/"False" and unavailable checks as "-" rather than JSON booleans and null; v1 omits base_email_address, is_dmarc_enforced, is_strict_spf and website_exist; and errors are returned with HTTP 200 carrying non-empty error_code and error_message fields instead of an HTTP 4xx, so callers must inspect error_code rather than the status code. Consumes one credit from the same shared balance, including for a syntactically invalid address.</td></tr></tbody></table>

## Events

MailboxValidator has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
