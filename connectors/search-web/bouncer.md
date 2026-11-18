---
description: "Bouncer email verification API."
hidden: true
---

# Bouncer

<img src="../../.gitbook/assets/connectors/lg/bouncer.png" alt="Bouncer logo">

Bouncer email verification API. Verify the deliverability of a single email address in real time, run large batch verification jobs synchronously or asynchronously, check a domain's MX and catch-all behaviour, screen lists for toxic addresses, and check your remaining verification credits.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [usebouncer.com](https://usebouncer.com) |
| **Authentication** | API key, Basic auth |
| **Slug** | `bouncer` |

## Use it

Add Bouncer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bouncer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Available Credits | `getCredits` | Retrieves the number of email verification credits remaining on the Bouncer account. Rate limited to 10 requests per minute. This call does not consume a credit. |
| Check Batch Status | `getBatchStatus` | Returns the processing status of a batch verification request, including how many addresses it holds and how many credits it consumed once complete. Poll this every 10 to 30 seconds until the status is 'completed', then download the results. Set With Stats to also receive progress counts broken down by deliverability. |
| Check Toxicity List Job Status | `getToxicityList` | Returns the state of a toxicity screening job. Poll until the status is 'completed', then download the results; a status of 'error' means processing failed. |
| Create Batch Verification Request | `createBatch` | Submits a list of email addresses for offline batch verification and returns the batchId used to poll status and download results. A single batch accepts up to 100,000 addresses; 1,000 to 10,000 is the recommended size. Optionally supply a callback URL that Bouncer POSTs to when the batch completes. Limited to 60 new batches per minute. Credits are charged per address verified. |
| Create Batch Verification Request (Legacy v1) | `createBatchV1` | Legacy v1 batch creation endpoint, still live on api.usebouncer.com but not listed in Bouncer's current documentation. It queues a list of addresses like Create Batch Verification Request but returns a different shape: requestId plus a progress object instead of batchId and quantity. The v1 subtree has no /finish or /download route, and its GET returns results rather than status. Use Create Batch Verification Request for new work. |
| Create Batch Verification Request From Text List | `createBatchFromText` | Creates a batch verification request from a plain-text or CSV list of addresses, one per line, instead of a JSON array. This is the same endpoint as Create Batch Verification Request driven with a text/plain body, and is convenient when you already hold a CSV export. Set Skip Header to true when the first line is a column header. |
| Create Toxicity List Job | `createToxicityList` | Submits a list of email addresses to be screened against Bouncer's toxic-address database (spam traps, complainers, known bad actors) and returns the job id used to poll status and download results. Limited to 10 lists per minute. Credits are charged per address screened. |
| Delete Batch Request | `deleteBatch` | Permanently deletes a batch verification request and every email address and result stored with it. Download the results first if you still need them, because this cannot be undone. Credits already spent are not refunded. |
| Delete Batch Request (Legacy v1) | `deleteBatchV1` | Legacy v1 batch delete endpoint, still live on api.usebouncer.com but not listed in Bouncer's current documentation. It permanently deletes the batch and its stored addresses and results. Use Delete Batch Request for new work. |
| Delete Toxicity List Job | `deleteToxicityList` | Permanently deletes a toxicity screening job and the addresses and results stored with it. Download the results first if you still need them, because this cannot be undone. |

<details>

<summary>See 8 more actions</summary>

* **Download Batch Results** `getBatchResults`: Downloads the verification results of a completed batch as JSON, one record per address with its deliverability status, reason, domain and mailbox attributes and quality score. Use the Download filter to return only addresses with a given status. Available once Check Batch Status reports 'completed'.
* **Download Batch Results (Legacy v1)** `getBatchStatusV1`: Legacy v1 batch endpoint, still live on api.usebouncer.com but not listed in Bouncer's current documentation. Unlike its v1.1 counterpart this route returns the verification results array directly rather than a status record, and answers 405 'batch is not completed' while the batch is still running. Use Check Batch Status and Download Batch Results for new work.
* **Download Toxicity List Results** `getToxicityListResults`: Downloads the results of a completed toxicity screening job: one record per address with its toxicity level, where 0 means no toxic signal and higher values mean stronger evidence the address is a spam trap or complainer. Returns 400 'processing is not completed yet' if the job is still running.
* **Finish Batch Early** `finishBatch`: Stops a batch that is still processing: Bouncer wraps up the addresses already in flight and refunds the credits reserved for addresses it has not verified yet. The batch then moves to 'completed' and its partial results can be downloaded.
* **Verify Domain** `verifyDomain`: Checks a single domain and returns whether it has valid MX records, whether it is a catch-all (accept-all) domain, whether it is disposable or a free mail provider, and which mailbox provider sits behind it. Consumes one credit per call. Rate limited to 1000 requests per minute.
* **Verify Email** `verifyEmail`: Verifies a single email address in real time, checking syntax, domain, MX records and SMTP deliverability, and returns a deliverability status, reason, domain and mailbox attributes, provider and quality score. Consumes one credit per call. Use the sandbox addresses (deliverable@sandbox.usebouncer.com and friends) to test for free.
* **Verify Email (Legacy v1)** `verifyEmailV1`: Legacy v1 real-time verification endpoint, still live on api.usebouncer.com but not listed in Bouncer's current documentation. It returns the same verification record as Verify Email. Use Verify Email instead for new work; this action exists so integrations pinned to the v1 path keep working. Consumes one credit per call.
* **Verify Emails In Batch (Synchronous)** `verifyBatchSync`: Adds a list of email addresses to Bouncer's verification queue and returns the results that are already known. The first call for a fresh list normally returns an empty array; re-post the same list after a delay of 5 seconds to 10 minutes and the completed records come back. Results are cached for 24 hours, after which the addresses are verified and charged again. Up to 10,000 addresses per request, 100 requests per minute. Credits are charged per address.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Batch Verification Completed | `batch.completed` | Fires when a Bouncer batch verification request finishes processing. Bouncer has no webhook registration API and no webhook settings page: the callback URL is supplied per job. To receive this event, copy this trigger's webhook URL and pass it as the Callback URL input on the Create Batch Verification Request action (Bouncer sends POST &lt;YOUR-URL&gt; once the batch completes, as described at https://docs.usebouncer.com/api-reference/batch/batch-create under 'Batch Integration Flow With Callbacks'). Then call Download Batch Results with the batchId to fetch the verified records. Every batch you want notifications for must carry the callback URL; there is nothing to enable in the Bouncer app. |
