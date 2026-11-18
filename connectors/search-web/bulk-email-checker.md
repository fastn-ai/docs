---
description: "Bulk Email Checker is an email verification service that validates email addresses in real time, returning deliverability status, SMTP handshake result,…"
hidden: true
---

# Bulk Email Checker

Bulk Email Checker is an email verification service that validates email addresses in real time, returning deliverability status, SMTP handshake result, disposable/role/free-mailbox flags, typo suggestions and MX server enrichment. This connector wraps the vendor's entire public HTTP surface: the Real-time Email Verification API and its Unlimited API alias, in both JSON and XML response formats, over GET and POST.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [bulkemailchecker.com](https://bulkemailchecker.com) |
| **Authentication** | API key |
| **Actions** | 5 |
| **Events** | 0 |
| **Slug** | `bulkEmailChecker` |

## Use it

Add Bulk Email Checker from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bulkEmailChecker.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Verify Email Address | `verifyEmailAddress` | Verifies a single email address in real time with the Bulk Email Checker Real-time API and returns a JSON verdict: status (passed, failed or unknown), the underlying event, mailbox and domain parts, a suggested correction for likely typos, complainer / disposable / free-service / gibberish / offensive / role-account flags, remaining credits and hourly quota, and full MX server enrichment. Consumes 1 credit per passed or failed result; unknown results are free. |
| Verify Email Address As XML | `verifyEmailAddressAsXml` | Verifies a single email address with the Bulk Email Checker Real-time API and returns the result as an XML document (the vendor's xml=true mode) rather than JSON. Use this when a downstream system consumes XML, for example a spreadsheet IMPORTXML formula. The payload carries the same fields as the JSON verification: status, event, details, mailbox, domain, the boolean flags, remaining credits and MX enrichment. |
| Verify Email Address On Unlimited Endpoint | `verifyEmailAddressUnlimited` | Verifies a single email address through the Bulk Email Checker Unlimited API endpoint, the high-concurrency path intended for batch list cleaning and high-volume workloads (50+ dedicated threads, no hourly quota) on Unlimited plans. It returns the same JSON verdict shape as the Real-time endpoint. Use the Real-time action for transactional point-of-entry checks and this one for large programmatic runs. |
| Verify Email Address On Unlimited Endpoint Via POST | `verifyEmailAddressUnlimitedViaPost` | Verifies a single email address through the Bulk Email Checker Unlimited API endpoint using an HTTP POST form submission. The API key and the address travel in the form-urlencoded request body, so the key never appears in the request URL - preferred when request URLs are logged. Returns the same JSON verdict as the GET variant; a JSON request body is rejected by the vendor. |
| Verify Email Address Via POST | `verifyEmailAddressViaPost` | Verifies a single email address with the Bulk Email Checker Real-time API using an HTTP POST form submission instead of a GET query string, returning the same JSON verdict as Verify Email Address. The API key and the address travel in the form-urlencoded request body, so the key never appears in the request URL. The vendor accepts only application/x-www-form-urlencoded here; a JSON body is rejected as a missing key. |
