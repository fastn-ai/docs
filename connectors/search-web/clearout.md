---
description: "Clearout email verification, email finder, reverse lookup, name validation and domain MX/WHOIS APIs (api.clearout.io/v2)."
hidden: true
---

# Clearout

<img src="../../.gitbook/assets/connectors/lg/clearout.png" alt="Clearout logo">

Clearout email verification, email finder, reverse lookup, name validation and domain MX/WHOIS APIs (api.clearout.io/v2). API-token authentication.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [clearout.io](https://clearout.io) |
| **Authentication** | API key |
| **Slug** | `clearout` |

## Use it

Add Clearout from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.clearout.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Bulk Finder List | `cancelBulkFinderList` | Cancels an in-progress bulk Email Finder list by list_id. |
| Cancel Bulk Verify List | `cancelBulkVerifyList` | Cancels an in-progress bulk email-verification list by list_id. |
| Download Bulk Finder Result | `downloadBulkFinderResult` | Requests the downloadable result file for a completed bulk Email Finder list. Returns a signed download URL. |
| Download Bulk Verify Result | `downloadBulkVerifyResult` | Requests the downloadable result file for a completed bulk email-verification list. Returns a signed download URL. |
| Find Email Bulk | `findEmailBulk` | Uploads a CSV of name + domain rows for bulk email discovery and returns a list_id to poll with Get Bulk Finder Progress. fileContent is the raw CSV text. |
| Find Email Instant | `findEmailInstant` | Email Finder: discovers a person's business email from their name plus a company domain or company name. Returns the discovered address with a confidence score, or a queue id when it times out and queue is true. |
| Get Account Credits | `getAccountCredits` | Account API: returns remaining credits for every Clearout service (email verifier, email finder, etc). Takes no input. Does not consume credits. |
| Get Available Credits | `getAvailableCredits` | Returns the Clearout account's available email-verification credits, daily limit and low-balance threshold. Takes no input. Does not consume credits. |
| Get Bulk Finder Progress | `getBulkFinderProgress` | Returns progress and result counts for a bulk Email Finder list, by list_id returned from Find Email Bulk. |
| Get Bulk Verify Progress | `getBulkVerifyProgress` | Returns progress and result counts for a bulk email-verification list, by list_id returned from Verify Email Bulk. |

<details>

<summary>See 21 more actions</summary>

* **Get Instant Finder Queue Status** `getInstantFinderQueueStatus`: Retrieves the result of a queued instant Email Finder request using the qid returned when the instant call timed out.
* **Get Plans And Addons** `getPlansAndAddons`: Account API: returns the current subscription plan, pay-as-you-go plans and purchased addons. Takes no input. Does not consume credits.
* **Get Service Limits** `getServiceLimits`: Account API: returns the account's per-service rate and usage limits. Takes no input. Does not consume credits.
* **List Email Finder Lists** `listEmailFinderLists`: Lists bulk Email Finder lists with cursor pagination. Optional filters: date_range and processing status.
* **List Email Verifier Lists** `listEmailVerifierLists`: Lists bulk email-verification lists with cursor pagination. Optional filters: date_range, verified status, source type.
* **Remove Bulk Finder List** `removeBulkFinderList`: Permanently removes a bulk Email Finder list and its results by list_id. Set ignoreResult true when a download is in progress.
* **Remove Bulk Verify List** `removeBulkVerifyList`: Permanently removes a bulk email-verification list and its results by list_id. Set ignoreResult true when a download is in progress.
* **Resolve Domain MX** `resolveDomainMx`: Misc Domain API: resolves and returns the MX records for a domain.
* **Resolve Domain Whois** `resolveDomainWhois`: Misc Domain API: returns WHOIS registration data for a domain (registrar, created/expiry dates, name servers).
* **Reverse Lookup Domain** `reverseLookupDomain`: Reverse Lookup: returns the company profile associated with a domain or company name.
* **Reverse Lookup Email** `reverseLookupEmail`: Reverse Lookup: returns the person and company profile associated with an email address.
* **Reverse Lookup LinkedIn** `reverseLookupLinkedin`: Reverse Lookup: returns the person profile associated with a LinkedIn profile URL.
* **Validate Name** `validateName`: AI name validation: judges whether a supplied full name is a genuine human name, splits first/last, and flags gibberish. gibberishThreshold tunes sensitivity (off, medium, high).
* **Verify Business Account** `verifyBusinessAccount`: Checks whether an email address is a business (non-free) account. Returns a yes/no business flag.
* **Verify Catch All** `verifyCatchAll`: Checks whether an email address belongs to a catch-all (accept-all) domain. Returns a yes/no catch_all flag.
* **Verify Disposable** `verifyDisposable`: Checks whether an email address is a disposable/temporary mailbox. Returns a yes/no disposable flag.
* **Verify Email Bulk** `verifyEmailBulk`: Uploads a CSV/TXT list of email addresses for bulk verification and returns a list_id to poll with Get Bulk Verify Progress. fileContent is the raw text of the file (one email per line, optional header row). Consumes 1 credit per non-test address.
* **Verify Email Instant** `verifyEmailInstant`: Real-time single email address verification. Returns status (valid/invalid/catch_all/unknown), safe_to_send, sub_status, MX and SMTP detail, plus disposable/free/role/gibberish flags. Consumes 1 credit per non-test address.
* **Verify Free Account** `verifyFreeAccount`: Checks whether an email address belongs to a free mail provider (gmail, yahoo, ...). Returns a yes/no free flag.
* **Verify Gibberish Account** `verifyGibberishAccount`: Checks whether the local part of an email address is gibberish / randomly generated. Returns a yes/no gibberish flag.
* **Verify Role Account** `verifyRoleAccount`: Checks whether an email address is a role account (info@, support@, sales@ ...). Returns a yes/no role flag.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Bulk Email Finder Completed | `email_finder.bulk.completed` | Fires when a bulk Email Finder list finishes processing. Payload carries list_id and list_name; call Download Bulk Finder Result with that list_id. payloadSchema is MODELLED from the vendor's documented sample. SIGNATURE: x-co-webhook-signature: t=&lt;unix&gt;,v1=&lt;hex HMAC-SHA256 of "&lt;t&gt;.&lt;raw body&gt;"&gt; with the account Secret Token. REGISTRATION IS UI-ONLY (no webhook API exists). Click-path: https://app.clearout.io/ &gt; Developers &gt; Webhook &gt; Create Webhook &gt; paste the fastn webhook URL into URL &gt; under Event Selection expand 'Email Finder' and tick 'email_finder.bulk.completed' &gt; Save. Generate the account Secret Token on the same page. |
| Bulk Email Verification Completed | `email_verifier.bulk.completed` | Fires when a bulk email-verification list finishes processing. Payload carries list_id and list_name; call Download Bulk Verify Result with that list_id to fetch the results file. payloadSchema is MODELLED from the vendor's documented sample. SIGNATURE: x-co-webhook-signature: t=&lt;unix&gt;,v1=&lt;hex HMAC-SHA256 of "&lt;t&gt;.&lt;raw body&gt;"&gt; with the account Secret Token. REGISTRATION IS UI-ONLY (no webhook API exists). Click-path: https://app.clearout.io/ &gt; Developers &gt; Webhook &gt; Create Webhook &gt; paste the fastn webhook URL into URL &gt; under Event Selection expand 'Email Verifier' and tick 'email_verifier.bulk.completed' &gt; Save. Generate the account Secret Token on the same page. |
| Form Guard Email Validation Completed | `form_guard.email_validation.completed` | Fires when Clearout Form Guard validates an email address on one of your web forms. Payload carries the full verification result plus page_url, widget name and version. payloadSchema is MODELLED from the vendor's documented sample. SIGNATURE: x-co-webhook-signature: t=&lt;unix&gt;,v1=&lt;hex HMAC-SHA256 of "&lt;t&gt;.&lt;raw body&gt;"&gt; with the account Secret Token. REGISTRATION IS UI-ONLY (no webhook API exists). Click-path: https://app.clearout.io/ &gt; Developers &gt; Webhook &gt; Create Webhook &gt; paste the fastn webhook URL into URL &gt; under Event Selection expand 'Form Guard' and tick 'form_guard.email_validation.completed' &gt; Save. Generate the account Secret Token on the same page. This event additionally requires Form Guard to be installed on a live web form. |
| Form Guard Name Validation Completed | `form_guard.name_validation.completed` | Fires when Clearout Form Guard validates a person name on one of your web forms. Payload carries input_name, status, regex_result, profanity, gibberish and normalized_name. payloadSchema is MODELLED from the vendor's documented sample. SIGNATURE: x-co-webhook-signature: t=&lt;unix&gt;,v1=&lt;hex HMAC-SHA256 of "&lt;t&gt;.&lt;raw body&gt;"&gt; with the account Secret Token. REGISTRATION IS UI-ONLY (no webhook API exists). Click-path: https://app.clearout.io/ &gt; Developers &gt; Webhook &gt; Create Webhook &gt; paste the fastn webhook URL into URL &gt; under Event Selection expand 'Form Guard' and tick 'form_guard.name_validation.completed' &gt; Save. Generate the account Secret Token on the same page. This event additionally requires Form Guard to be installed on a live web form. |
| Form Guard Phone Validation Completed | `form_guard.phone_validation.completed` | Fires when Clearout Form Guard validates a phone number on one of your web forms. Payload carries line_type, carrier, location, country fields and the E.164, international and local formats. payloadSchema is MODELLED from the vendor's documented sample. SIGNATURE: x-co-webhook-signature: t=&lt;unix&gt;,v1=&lt;hex HMAC-SHA256 of "&lt;t&gt;.&lt;raw body&gt;"&gt; with the account Secret Token. REGISTRATION IS UI-ONLY (no webhook API exists). Click-path: https://app.clearout.io/ &gt; Developers &gt; Webhook &gt; Create Webhook &gt; paste the fastn webhook URL into URL &gt; under Event Selection expand 'Form Guard' and tick 'form_guard.phone_validation.completed' &gt; Save. Generate the account Secret Token on the same page. This event additionally requires Form Guard to be installed on a live web form. |
| Instant Email Finder Completed | `email_finder.instant.completed` | Fires when an instant Email Finder request completes, including one queued after a timeout. Payload carries the discovered addresses, confidence_score and credits_charged. The vendor's own sample envelope uses event_on rather than event_created_on for this event, so both are declared. payloadSchema is MODELLED from the vendor's documented sample. SIGNATURE: x-co-webhook-signature: t=&lt;unix&gt;,v1=&lt;hex HMAC-SHA256 of "&lt;t&gt;.&lt;raw body&gt;"&gt; with the account Secret Token. REGISTRATION IS UI-ONLY (no webhook API exists). Click-path: https://app.clearout.io/ &gt; Developers &gt; Webhook &gt; Create Webhook &gt; paste the fastn webhook URL into URL &gt; under Event Selection expand 'Email Finder' and tick 'email_finder.instant.completed' &gt; Save. Generate the account Secret Token on the same page. |
| Instant Email Verification Completed | `email_verifier.instant.completed` | Fires after an instant email verification completes, including a request that originally timed out or returned unknown. payloadSchema is MODELLED from the vendor's documented sample (a real delivery could not be captured because registration is UI-only). SIGNATURE: Clearout signs every delivery with header x-co-webhook-signature: t=&lt;unix&gt;,v1=&lt;hex HMAC-SHA256 of "&lt;t&gt;.&lt;raw body&gt;"&gt; using the account-level Secret Token; this config leaves verification unset because the engine requires the secret value up front and it is only obtainable by clicking Generate Token in the UI - set it before production use. REGISTRATION IS UI-ONLY: Clearout exposes no webhook-management API (probed live with a valid token: /v2/webhook, /v2/webhooks, /v2/account/webhooks all return error code 1138 'Endpoint Not found', identical to a garbage route). Click-path: sign in at https://app.clearout.io/ &gt; Developers in the main menu &gt; Webhook &gt; Create Webhook &gt; fill Name, Description and the URL field with the fastn webhook URL (must be public HTTPS) &gt; optionally Add Header for a shared secret &gt; under Event Selection expand 'Email Verifier' and tick 'email_verifier.instant.completed' &gt; Save. Then scroll to Secret Token and click Generate Token, copying it immediately because it is shown only once. Use the paper-plane Test Events button on the webhook row to send a sample payload. |
