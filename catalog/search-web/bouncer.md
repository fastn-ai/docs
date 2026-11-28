---
description: "Bouncer is an email verification service. Verify single emails or run batch verification jobs, download results, and check lists for toxic addresses."
hidden: true
---

# Bouncer

<img src="../../.gitbook/assets/connectors/lg/bouncer.png" alt="Bouncer logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [usebouncer.com](https://usebouncer.com) |
| **Authentication** | API key, Username and password |
| **Slug** | `bouncer` |

## Setup

Your customers enter their API key or username and password for Bouncer when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Bouncer from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Bouncer**.
2. Select **Connect** on the Bouncer card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Bouncer's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check Available Credits</td><td><code>getCredits</code></td><td>Retrieves the number of email verification credits remaining on the Bouncer account. Rate limited to 10 requests per minute. This call does not consume a credit.</td></tr><tr><td>Check Batch Status</td><td><code>getBatchStatus</code></td><td>Returns the processing status of a batch verification request, including how many addresses it holds and how many credits it consumed once complete. Poll this every 10 to 30 seconds until the status is 'completed', then download the results. Set With Stats to also receive progress counts broken down by deliverability.</td></tr><tr><td>Check Toxicity List Job Status</td><td><code>getToxicityList</code></td><td>Returns the state of a toxicity screening job. Poll until the status is 'completed', then download the results; a status of 'error' means processing failed.</td></tr><tr><td>Create Batch Verification Request</td><td><code>createBatch</code></td><td>Submits a list of email addresses for offline batch verification and returns the batchId used to poll status and download results. A single batch accepts up to 100,000 addresses; 1,000 to 10,000 is the recommended size. Optionally supply a callback URL that Bouncer POSTs to when the batch completes. Limited to 60 new batches per minute. Credits are charged per address verified.</td></tr><tr><td>Create Batch Verification Request (Legacy v1)</td><td><code>createBatchV1</code></td><td>Legacy v1 batch creation endpoint, still live on api.usebouncer.com but not listed in Bouncer's current documentation. It queues a list of addresses like Create Batch Verification Request but returns a different shape: requestId plus a progress object instead of batchId and quantity. The v1 subtree has no /finish or /download route, and its GET returns results rather than status. Use Create Batch Verification Request for new work.</td></tr><tr><td>Create Batch Verification Request From Text List</td><td><code>createBatchFromText</code></td><td>Creates a batch verification request from a plain-text or CSV list of addresses, one per line, instead of a JSON array. This is the same endpoint as Create Batch Verification Request driven with a text/plain body, and is convenient when you already hold a CSV export. Set Skip Header to true when the first line is a column header.</td></tr><tr><td>Create Toxicity List Job</td><td><code>createToxicityList</code></td><td>Submits a list of email addresses to be screened against Bouncer's toxic-address database (spam traps, complainers, known bad actors) and returns the job id used to poll status and download results. Limited to 10 lists per minute. Credits are charged per address screened.</td></tr><tr><td>Delete Batch Request</td><td><code>deleteBatch</code></td><td>Permanently deletes a batch verification request and every email address and result stored with it. Download the results first if you still need them, because this cannot be undone. Credits already spent are not refunded.</td></tr><tr><td>Delete Batch Request (Legacy v1)</td><td><code>deleteBatchV1</code></td><td>Legacy v1 batch delete endpoint, still live on api.usebouncer.com but not listed in Bouncer's current documentation. It permanently deletes the batch and its stored addresses and results. Use Delete Batch Request for new work.</td></tr><tr><td>Delete Toxicity List Job</td><td><code>deleteToxicityList</code></td><td>Permanently deletes a toxicity screening job and the addresses and results stored with it. Download the results first if you still need them, because this cannot be undone.</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Download Batch Results</td><td><code>getBatchResults</code></td><td>Downloads the verification results of a completed batch as JSON, one record per address with its deliverability status, reason, domain and mailbox attributes and quality score. Use the Download filter to return only addresses with a given status. Available once Check Batch Status reports 'completed'.</td></tr><tr><td>Download Batch Results (Legacy v1)</td><td><code>getBatchStatusV1</code></td><td>Legacy v1 batch endpoint, still live on api.usebouncer.com but not listed in Bouncer's current documentation. Use Check Batch Status and Download Batch Results for new work.</td></tr><tr><td>Download Toxicity List Results</td><td><code>getToxicityListResults</code></td><td>Downloads the results of a completed toxicity screening job: one record per address with its toxicity level, where 0 means no toxic signal and higher values mean stronger evidence the address is a spam trap or complainer.</td></tr><tr><td>Finish Batch Early</td><td><code>finishBatch</code></td><td>Stops a batch that is still processing: Bouncer wraps up the addresses already in flight and refunds the credits reserved for addresses it has not verified yet. The batch then moves to 'completed' and its partial results can be downloaded.</td></tr><tr><td>Verify Domain</td><td><code>verifyDomain</code></td><td>Checks a single domain and returns whether it has valid MX records, whether it is a catch-all (accept-all) domain, whether it is disposable or a free mail provider, and which mailbox provider sits behind it. Consumes one credit per call. Rate limited to 1000 requests per minute.</td></tr><tr><td>Verify Email</td><td><code>verifyEmail</code></td><td>Verifies a single email address in real time, checking syntax, domain, MX records and SMTP deliverability, and returns a deliverability status, reason, domain and mailbox attributes, provider and quality score. Consumes one credit per call. Use the sandbox addresses (deliverable@sandbox.usebouncer.com and friends) to test for free.</td></tr><tr><td>Verify Email (Legacy v1)</td><td><code>verifyEmailV1</code></td><td>Legacy v1 real-time verification endpoint, still live on api.usebouncer.com but not listed in Bouncer's current documentation. It returns the same verification record as Verify Email. Use Verify Email instead for new work; this action exists so integrations pinned to the v1 path keep working. Consumes one credit per call.</td></tr><tr><td>Verify Emails In Batch (Synchronous)</td><td><code>verifyBatchSync</code></td><td>Adds a list of email addresses to Bouncer's verification queue and returns the results that are already known. The first call for a fresh list normally returns an empty array; re-post the same list after a delay of 5 seconds to 10 minutes and the completed records come back. Results are cached for 24 hours, after which the addresses are verified and charged again. Up to 10,000 addresses per request, 100 requests per minute. Credits are charged per address.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Batch Verification Completed</td><td><code>batch.completed</code></td><td>Fires when a Bouncer batch verification request finishes processing. Bouncer has no webhook registration API and no webhook settings page: the callback URL is supplied per job. To receive this event, copy this trigger's webhook URL and pass it as the Callback URL input on the Create Batch Verification Request action (Bouncer sends POST &lt;YOUR-URL&gt; once the batch completes, as described at https://docs.usebouncer.com/api-reference/batch/batch-create under 'Batch Integration Flow With Callbacks'). Then call Download Batch Results with the batchId to fetch the verified records. Every batch you want notifications for must carry the callback URL; there is nothing to enable in the Bouncer app.</td></tr></tbody></table>
