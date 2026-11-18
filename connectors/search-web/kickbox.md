---
description: "Kickbox email verification API."
hidden: true
---

# Kickbox

Kickbox email verification API. Single and batch email address verification, account credit balance, and the free open disposable-domain check.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [kickbox.com](https://kickbox.com) |
| **Authentication** | Bearer token |
| **Actions** | 8 |
| **Events** | 2 |
| **Slug** | `kickbox` |

## Use it

Add Kickbox from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.kickbox.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Disposable Email Domain | `checkDisposableEmail` | Free open endpoint (open.kickbox.com, no authentication, no credits) that reports whether an email address is hosted on a known disposable/throwaway domain. GET https://open.kickbox.com/v1/disposable/{email}. Returns {disposable: true\|false}. |
| Get Balance | `getBalance` | Returns the number of verification credits remaining on the Kickbox account. GET /v2/balance. No inputs. |
| Get Batch Verification Status | `getBatchVerificationStatus` | Returns the status of a batch verification job. GET /v2/verify-batch/{jobId}. Status is one of starting, processing, completed or failed. When processing it carries a progress breakdown; when completed it carries stats and a download_url valid for one hour (re-call this action for a freshly signed URL). |
| Get Email Threat Score | `getEmailThreatScore` | Returns ONLY the Email Threat Score for an address, without running a standard verification. GET /v2/verify with threat_only=true. Mutually exclusive with include_threat. Consumes credits. |
| Start Batch Verification | `startBatchVerification` | Submits a list of email addresses for asynchronous batch verification. PUT /v2/verify-batch with a text/csv body of one email address per line (max 1 million addresses / 250MB). Returns the job id used by Get Batch Verification Status. Set callbackUrl to receive a POST when the job completes (pass an empty string for no callback); set filename to name the downloadable result file. |
| Start Batch Verification With Threat Score | `startBatchVerificationWithThreatScore` | Same as Start Batch Verification but with include_threat=true, so the result file also carries threat_score and threat_level columns for every address. PUT /v2/verify-batch?include_threat=true with a text/csv body of one email per line. Returns the job id. |
| Verify Email | `verifyEmail` | Verifies a single email address in real time. GET /v2/verify. Returns result (deliverable\|undeliverable\|risky\|unknown), reason, role, free, disposable, accept_all, did_you_mean, sendex, user, domain. Consumes one verification credit. |
| Verify Email With Threat Score | `verifyEmailWithThreatScore` | Runs a full single-address verification AND returns the Email Threat Score. GET /v2/verify with include_threat=true. Returns the standard verification fields plus threat_score and threat_level. Consumes credits. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Batch Verification Completed | `completed` | Fires when a Kickbox batch verification job finishes successfully. SETUP (Kickbox has no webhook registration API - the callback URL is set per job): copy this trigger's fastn webhook URL, then pass it as the `callbackUrl` input of the `Start Batch Verification` (or `Start Batch Verification With Threat Score`) action for every job you want notified. Kickbox sends the completion payload as a POST to that URL and requires a 2xx response. There is nothing to register in the Kickbox dashboard and nothing to unsubscribe - stop passing the URL and deliveries stop. Note: `download_url` in the payload is valid for one hour; after that call `Get Batch Verification Status` for a freshly signed URL. payloadSchema is MODELLED from the vendor documentation - a real delivery could not be captured because the test account has 0 verification credits, so submitted jobs never leave the queued state. |
| Batch Verification Failed | `failed` | Fires when a Kickbox batch verification job ends in failure; `error` carries the vendor's description. SETUP is identical to Batch Verification Completed: Kickbox has no webhook registration API, so copy this trigger's fastn webhook URL and pass it as the `callbackUrl` input of `Start Batch Verification` for each job. Nothing is registered in the Kickbox dashboard and there is nothing to unsubscribe. payloadSchema is MODELLED from the vendor documentation - a real delivery could not be captured because the test account has 0 verification credits. |
