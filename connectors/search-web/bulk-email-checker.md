---
description: "Bulk Email Checker validates email addresses in real time. Verify a single address and get its deliverability status."
hidden: true
---

# Bulk Email Checker

<img src="../../.gitbook/assets/connectors/lg/bulk-email-checker.png" alt="Bulk Email Checker logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [bulkemailchecker.com](https://bulkemailchecker.com) |
| **Authentication** | API key |
| **Slug** | `bulkEmailChecker` |

## Setup

Your customers enter their API key for Bulk Email Checker when they connect. Nothing else needs setting up.

## Use it

Add Bulk Email Checker from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bulkEmailChecker.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Verify Email Address</td><td><code>verifyEmailAddress</code></td><td>Verifies a single email address in real time with the Bulk Email Checker Real-time API and returns a JSON verdict: status (passed, failed or unknown), the underlying event, mailbox and domain parts, a suggested correction for likely typos, complainer / disposable / free-service / gibberish / offensive / role-account flags, remaining credits and hourly quota, and full MX server enrichment. Consumes 1 credit per passed or failed result; unknown results are free.</td></tr><tr><td>Verify Email Address As XML</td><td><code>verifyEmailAddressAsXml</code></td><td>Verifies a single email address with the Bulk Email Checker Real-time API and returns the result as an XML document (the vendor's xml=true mode) rather than JSON. Use this when a downstream system consumes XML, for example a spreadsheet IMPORTXML formula. The payload carries the same fields as the JSON verification: status, event, details, mailbox, domain, the boolean flags, remaining credits and MX enrichment.</td></tr><tr><td>Verify Email Address On Unlimited Endpoint</td><td><code>verifyEmailAddressUnlimited</code></td><td>Verifies a single email address through the Bulk Email Checker Unlimited API endpoint, the high-concurrency path intended for batch list cleaning and high-volume workloads (50+ dedicated threads, no hourly quota) on Unlimited plans. It returns the same JSON verdict shape as the Real-time endpoint. Use the Real-time action for transactional point-of-entry checks and this one for large programmatic runs.</td></tr><tr><td>Verify Email Address On Unlimited Endpoint Via POST</td><td><code>verifyEmailAddressUnlimitedViaPost</code></td><td>Verifies a single email address through the Bulk Email Checker Unlimited API endpoint using an HTTP POST form submission. The API key and the address travel in the form-urlencoded request body, so the key never appears in the request URL - preferred when request URLs are logged. Returns the same JSON verdict as the GET variant; a JSON request body is rejected by the vendor.</td></tr><tr><td>Verify Email Address Via POST</td><td><code>verifyEmailAddressViaPost</code></td><td>Verifies a single email address with the Bulk Email Checker Real-time API using an HTTP POST form submission instead of a GET query string, returning the same JSON verdict as Verify Email Address. The API key and the address travel in the form-urlencoded request body, so the key never appears in the request URL. The vendor accepts only application/x-www-form-urlencoded here; a JSON body is rejected as a missing key.</td></tr></tbody></table>

## Events

Bulk Email Checker has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
