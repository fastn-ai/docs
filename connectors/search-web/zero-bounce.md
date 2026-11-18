---
description: "ZeroBounce is an email validation and deliverability platform: verify single or batch email addresses in real time, validate large lists in bulk, check inbox…"
---

# ZeroBounce

ZeroBounce is an email validation and deliverability platform: verify single or batch email addresses in real time, validate large lists in bulk, check inbox activity, score catch-all emails with AI, find and search email formats by domain or company, and evaluate list quality before sending campaigns.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [zerobounce.net](https://zerobounce.net) |
| **Authentication** | Credentials you enter |
| **Actions** | 18 |
| **Events** | 0 |
| **Slug** | `zeroBounce` |

## Use it

Add ZeroBounce from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zeroBounce.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Bulk Scoring File | `deleteBulkScoringFile` | Delete a previously submitted bulk A.I. scoring file and its results from ZeroBounce's servers, freeing up the file_id. |
| Delete Bulk Validation File | `deleteBulkValidationFile` | Delete a previously submitted bulk validation file and its results from ZeroBounce's servers, freeing up the file_id. |
| Find Email Format | `findEmailFormat` | Guess the most likely email address format for a person at a company, given a domain or company name and optionally their first, middle, and last name. Consumes 20 credits (or 1 subscription query) only when a format is confidently determined. |
| Get API Usage | `getApiUsage` | Return a breakdown of validation usage (status and sub-status counts) for your account over a date range. Free to call, does not consume credits. |
| Get Bulk Scoring File Status | `getBulkScoringFileStatus` | Check the processing status and completion percentage of a file previously submitted with Send File for Bulk A.I. Scoring. |
| Get Bulk Scoring Result File | `getBulkScoringResultFile` | Download the A.I. scoring results for a file once its status is Complete, as returned by Get Bulk Scoring File Status. |
| Get Bulk Validation File Status | `getBulkValidationFileStatus` | Check the processing status and completion percentage of a file previously submitted with Send File for Bulk Email Validation. |
| Get Bulk Validation Result File | `getBulkValidationResultFile` | Download the validation results for a file once its status is Complete, as returned by Get Bulk Validation File Status. Returns a CSV file, or a JSON error body if the file_id is unknown or not yet complete. |
| Get Credit Balance | `getCreditBalance` | Return the number of validation credits remaining in your ZeroBounce account. Free to call, does not consume credits. |
| Get Email Activity | `getEmailActivity` | Check whether an email address has shown recent inbox activity (opens, clicks, or logins), useful for flagging outdated contacts before a cold outreach campaign. |
| Get List Evaluation Status | `getListEvaluationStatus` | Check the processing status and quality-risk percentages for a list submitted with Submit List for Evaluation. |
| Score Email | `scoreEmail` | Return an A.I.-generated quality score for a single email address, useful for ranking catch-all or unverifiable addresses that standard validation cannot definitively classify. |
| Send Evaluated File for Full Validation | `sendEvaluatedFileForValidation` | Promote a completed list-evaluation job to a full bulk email validation run, consuming 1 credit per email. The file_id must come from a Submit List for Evaluation job whose status is already complete. |
| Send File for Bulk A.I. Scoring | `sendFileForScoring` | Upload a CSV or TXT file of email addresses for asynchronous bulk A.I. quality scoring. Returns a file_id used with Get Bulk Scoring File Status, Get Bulk Scoring Result File, and Delete Bulk Scoring File. |
| Send File for Bulk Email Validation | `sendFileForValidation` | Upload a CSV or TXT file of email addresses for asynchronous bulk validation. Consumes 1 credit per email once processed. Returns a file_id used with Get Bulk Validation File Status, Get Bulk Validation Result File, and Delete Bulk Validation File. |
| Submit List for Evaluation | `submitListForEvaluation` | Upload a CSV or TXT file of at least 100 email addresses to estimate list quality (invalid, catch-all, spam trap, and risky percentages) before committing to a full paid validation. Returns a file_id used with Get List Evaluation Status and Send Evaluated File for Full Validation. |
| Validate Email | `validateEmail` | Validate a single email address in real time and return its deliverability status, sub-status, and enrichment details such as domain age, MX record, and free-email/catch-all flags. Consumes 1 credit per call. |
| Validate Email Batch | `validateEmailBatch` | Validate up to 100 email addresses in a single real-time call, each optionally paired with the IP address it signed up from. Consumes 1 credit per email in the batch. BLOCKED on this account: ZeroBounce's /v2/validatebatch endpoint returns HTTP 200 with an envelope error {\"errors\":[{\"error\":\"Invalid API Key or your account ran out of credits\",\"email_address\":\"all\"}],\"email_batch\":[]} for every call on this free-tier API key, confirmed identical via a raw curl request outside the platform (same key that succeeds on /v2/validate, /v2/getcredits, etc). This is an account/plan entitlement gate on the free tier, not a wiring defect - the api_key correctly resolves into the JSON body (required here since ZeroBounce's Cloudflare WAF 403s a query-param key on this specific POST route). Re-test once the account is upgraded to a plan with batch API access. |
