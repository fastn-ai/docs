---
description: "DeBounce email validation and list-hygiene API."
hidden: true
---

# DeBounce

<img src="../../.gitbook/assets/connectors/lg/de-bounce.png" alt="DeBounce logo">

Validates single email addresses in real time, runs bulk list validation, checks disposable domains, enriches addresses with name and avatar data, reports credit balance and daily API usage, and looks up company logos by domain.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [debounce.io](https://debounce.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `deBounce` |

## Use it

Add DeBounce from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.deBounce.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check Disposable Email Domain</td><td><code>checkDisposableEmailDomain</code></td><td>Checks an email address against DeBounce's real-time list of disposable and temporary email domains and returns whether the domain is disposable. This endpoint is free, requires no API key and does not consume a validation credit.</td></tr><tr><td>Download Bulk Validation Results</td><td><code>downloadBulkValidationResults</code></td><td>Downloads the results CSV for a completed bulk validation list from the DeBounce results CDN. Run Get Bulk Validation Status first and take the file name from the end of its download_link, for example 1033918-6ab2dfc0b6a2d.csv. The CSV has one row per address with EMAIL, RESULT, REASON, STATUS CODE, ROLE, FREE and DOMAIN columns. This call is free and needs no API key; DeBounce purges results ten days after validation.</td></tr><tr><td>Get Account Balance</td><td><code>getAccountBalance</code></td><td>Returns the number of validation credits remaining on the DeBounce account. This call is free and does not consume a credit. Use it before running validations to confirm the account has enough balance.</td></tr><tr><td>Get API Usage History</td><td><code>getApiUsageHistory</code></td><td>Returns the number of validations performed within a date range, so credit consumption can be tracked over time. Dates use the YY-MM-DD format; the start date must be 20-08-14 or later and the end date cannot be in the future. This call is free. Note that DeBounce echoes the account's own API key back in the response, so do not forward this action's raw output to untrusted consumers.</td></tr><tr><td>Get Bulk Validation Status</td><td><code>getBulkValidationStatus</code></td><td>Checks the progress of a list previously submitted through Upload Bulk Email List and returns its status, completion percentage and, once finished, the CSV download link for the results. Only lists uploaded through the bulk API have an API-accessible status; lists uploaded in the DeBounce dashboard do not. This call is free.</td></tr><tr><td>Get Company Logo</td><td><code>getCompanyLogo</code></td><td>Retrieves a company's logo as a PNG image by domain name, falling back to a generated monogram when no logo is available. This endpoint is free, requires no API key and does not consume a validation credit. The image is returned as a binary file reference.</td></tr><tr><td>Upload Bulk Email List</td><td><code>uploadBulkEmailList</code></td><td>Submits a hosted email list for bulk validation and returns the list ID used to poll progress. The file must be a public HTTPS direct-file URL ending in .csv or .txt on your own server, under 20MB, with at most 200,000 addresses one per line; file-sharing links such as Google Drive or Dropbox are rejected. Validation starts automatically and only one bulk job runs at a time per account. Each address in the list consumes one credit.</td></tr><tr><td>Validate Email Address</td><td><code>validateEmailAddress</code></td><td>Validates a single email address in real time and returns its deliverability result, including syntax, domain, MX, role-account, free-provider, disposable and accept-all checks plus a numeric send score. Consumes one validation credit per call. Setting photo to true adds an avatar lookup for 1 extra credit; setting append to true runs full data enrichment for 20 extra credits.</td></tr></tbody></table>
