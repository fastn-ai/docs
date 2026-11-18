---
description: "Veriphone phone number validation and carrier lookup API."
hidden: true
---

# Veriphone

<img src="../../.gitbook/assets/connectors/lg/veriphone.png" alt="Veriphone logo">

Veriphone phone number validation and carrier lookup API. Validate phone numbers, detect line types (mobile, fixed line, VoIP, toll free), identify the original and currently serving carrier via portability registries, format numbers to E.164/international/local, generate example numbers, check credit balance and payment history, and run bulk CSV verification jobs for 240+ countries.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [veriphone.io](https://veriphone.io) |
| **Authentication** | API key |
| **Slug** | `veriphone` |

## Use it

Add Veriphone from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.veriphone.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Subscription | `cancelSubscription` | Cancels the account's paid Veriphone subscription, returning it to the free plan. This route is served only to the Veriphone web dashboard: it authenticates with a Firebase session, not an API key, and answers a valid API key with 401 "This endpoint requires Firebase authentication". Billing-affecting and not reversible through the API. |
| Delete Account | `deleteAccount` | Permanently deletes the entire Veriphone account, including its API key, credits and bulk files. DESTRUCTIVE AND IRREVERSIBLE - it removes the identity this connector authenticates as, and there is no API route to undo it. The route is served only to the Veriphone web dashboard: it authenticates with a Firebase session, not an API key, and answers a valid API key with 401 "This endpoint requires Firebase authentication". |
| Delete Account (v2) | `deleteAccountV2` | Legacy v2 route that permanently deletes the entire Veriphone account. DESTRUCTIVE AND IRREVERSIBLE - it removes the identity this connector authenticates as, and there is no API route to undo it. Served only to the Veriphone web dashboard: it authenticates with a Firebase session, not an API key, and answers a valid API key with 401 "This endpoint requires Firebase authentication". |
| Delete Bulk Upload | `deleteBulkUpload` | Permanently deletes a bulk upload and its verification results. Returns 404 File not found for an unknown id and 403 when the file belongs to another account. This cannot be undone. |
| Delete Bulk Upload (v2) | `deleteBulkUploadV2` | Legacy v2 endpoint that permanently deletes a bulk upload and its verification results. Returns 404 File not found for an unknown id and 403 when the file belongs to another account. This cannot be undone. |
| Download Bulk Results CSV | `downloadBulkResults` | Downloads the verified results CSV for a bulk upload, or the original uploaded file when verification has not run yet. The results file keeps every original column and appends phone_valid, e164, local_number, type, country, region and carrier; files verified in current mode append ported, current_carrier, current_line_type and current_lookup as well. |
| Download Bulk Results CSV (v2) | `downloadBulkResultsV2` | Legacy v2 endpoint that downloads the verified results CSV for a bulk upload, or the original uploaded file when verification has not run yet. The response carries the file base64-encoded in the data field. |
| Get Account Profile | `getAccountProfile` | Returns the Veriphone account profile. This route is served only to the Veriphone web dashboard: it authenticates with a Firebase session, not an API key, and answers a valid API key with 401 "This endpoint requires Firebase authentication". It is included for completeness and will start working for any credential Veriphone later admits to this realm. |
| Get Account Profile (v2) | `getAccountProfileV2` | Legacy v2 account-profile route, served only to the Veriphone web dashboard. It authenticates with a Firebase session, not an API key, and answers a valid API key with 401 "This endpoint requires Firebase authentication". |
| Get Bulk Job Status | `getBulkJobStatus` | Polls the processing status of a bulk verification job and returns just the upload id and its status. Live values are new, ready, verifying, complete and deleted (the docs write complete as "completed"). Returns an empty status when the id does not exist or is not owned by your account. |
| Get Bulk Job Status (v2) | `getBulkJobStatusV2` | Legacy v2 endpoint that polls the processing status of a bulk verification job. Live status values are new, ready, verifying, complete and deleted. Returns an empty status when the id does not exist or is not owned by your account. |
| Get Bulk Upload Details | `getBulkUpload` | Returns the full detail record for a single bulk upload, with the same fields as one entry of List Bulk Uploads. Returns an empty object when the id does not exist or is not owned by your account. |
| Get Bulk Upload Details (v2) | `getBulkUploadV2` | Legacy v2 endpoint returning the full detail record for a single bulk upload. Returns an empty object when the id does not exist or is not owned by your account. |
| Get Credit Balance | `getCreditBalance` | Returns the Veriphone account's credit balance and usage for the current billing period, split by lookup mode (static and current). Use it before running verifications to check remaining quota. |
| Get Credit Balance (v2) | `getCreditBalanceV2` | Legacy v2 credit and usage endpoint. Returns the account email, verifications used this period, active flag, pay-as-you-go balance, monthly limit, plan name and reset day. The v3 equivalent adds a per-mode usage breakdown. |
| Get Example Phone Number | `getExamplePhoneNumber` | Returns a synthetic example phone number for a given country and line type, formatted in international, local and E.164 form. Useful for seeding test data, placeholder values and input-mask examples without touching a real subscriber number. Does not consume verification credits. |
| Get Example Phone Number (v2) | `getExamplePhoneNumberV2` | Legacy v2 example-number endpoint. Returns a synthetic example phone number for a country and line type in international, local and E.164 form. Consumes no verification credits. |
| List Bulk Uploads | `listBulkUploads` | Returns every non-deleted bulk upload on the account, newest first, with its processing status, row counts, valid/invalid tallies, billable rows and sample records. |
| List Bulk Uploads (v2) | `listBulkUploadsV2` | Legacy v2 endpoint returning every non-deleted bulk upload on the account, newest first, with processing status, row counts and valid/invalid tallies. |
| List Current Lookup Coverage | `listCurrentCoverage` | Returns the list of countries where Current lookups (mode=current, portability-registry resolution of the serving carrier) are available, with the date the coverage list was last updated. This endpoint is public and consumes no credits. |
| List Payments And Subscription | `listPayments` | Returns the Veriphone account's payment history and active subscription details, including product and plan name, amount, currency, receipt URL, subscription status and next bill date. The subscription object is empty when no active subscription exists. |
| List Payments And Subscription (v2) | `listPaymentsV2` | Legacy v2 billing endpoint. Returns the account's payment history and active subscription details. The subscription object is empty when no active subscription exists. |
| Start Bulk Verification Job | `startBulkVerification` | Starts the background job that verifies every phone number in a previously uploaded CSV. The account must hold enough credits to cover every row at the chosen mode's full rate before the job will start, otherwise a 402 is returned quoting credits_required, credits_available and credits_missing. Poll Get Bulk Job Status until it completes, then download the results. |
| Start Bulk Verification Job (v2) | `startBulkVerificationV2` | Legacy v2 endpoint that starts the background verification job for an uploaded CSV. The account must hold enough credits to cover every row before the job will start, otherwise a 402 is returned. Poll Get Bulk Job Status (v2) until it completes. |
| Upload Bulk CSV File | `uploadBulkFile` | Uploads a CSV file of phone numbers for bulk verification and returns the upload id used by every other bulk operation. Supply the CSV text, the zero-based index of the phone-number column and the zero-based index of the first data row. Maximum 100 MB and 1 million rows. Uploading does not consume credits; starting the verification does. |
| Upload Bulk CSV File (v2) | `uploadBulkFileV2` | Legacy v2 bulk upload endpoint. Uploads a CSV of phone numbers and returns the upload id used by the other v2 bulk operations. Maximum 100 MB and 1 million rows. Uploading does not consume credits. |
| Verify Phone Number | `verifyPhoneNumber` | Validates a phone number and returns its validity, line type, carrier, region, country and formatted representations (E.164, international, local). Set mode to current to also resolve the carrier currently serving the number from national portability registries. Each successful verification deducts credits: 1 for static mode, 10 for current mode. |
| Verify Phone Number (v2) | `verifyPhoneNumberV2` | Legacy v2 phone validation endpoint, kept for integrations already built against v2. Validates a number and returns validity, line type, carrier, region and formatted forms. Unlike v3 it has no lookup modes and reports an invalid number with status "error" rather than "success". Each successful call deducts 1 credit; inputs with fewer than 4 or more than 20 digits return status "syntax-error" and are not charged. New integrations should use Verify Phone Number. |
