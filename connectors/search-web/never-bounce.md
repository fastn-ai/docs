---
description: "NeverBounce is a real-time email verification and bulk list-cleaning service."
hidden: true
---

# NeverBounce

<img src="../../.gitbook/assets/connectors/lg/never-bounce.png" alt="NeverBounce logo">

NeverBounce is a real-time email verification and bulk list-cleaning service. This connector covers the full NeverBounce v4 API: account information and credit balance, single email verification, bulk verification jobs (create, parse, start, search, status, results, download and delete) and Point-of-Entry widget token confirmation.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [neverbounce.com](https://neverbounce.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `neverBounce` |

## Use it

Add NeverBounce from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.neverBounce.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Confirm Point Of Entry Token | `confirmPoeToken` | Confirms a verification performed by the NeverBounce Point-of-Entry widget on your own form. Pass back the email, transaction id, confirmation token and result the widget produced so NeverBounce can confirm the token is genuine and the result was not tampered with. |
| Create Job | `createJob` | Creates a bulk verification job from a supplied list of records or from a file at a remote URL and returns the new job id. Creating a job does not consume credits; credits are only charged when the job is started with Start Job or by setting Auto Start. |
| Delete Job | `deleteJob` | Permanently removes a bulk verification job and its results from the NeverBounce account. Credits already spent on the job are not refunded and the results can no longer be downloaded. |
| Download Job Results | `downloadJobResults` | Downloads the results of a completed bulk verification job as a CSV file, with optional segmentation to include or exclude each result code and optional appended columns such as host, domain, role account and email status. This endpoint does not consume credits. |
| Get Account Info | `getAccountInfo` | Retrieves the NeverBounce account's subscription type, the number of bulk jobs in each state and the remaining paid and free verification credits. Use it to check the credit balance before running verifications. This endpoint does not consume credits. |
| Get Job Results | `getJobResults` | Retrieves the per-record verification results of a bulk job as paginated JSON, returning each original record alongside its result code, flags and parsed address components. This endpoint does not consume credits. |
| Get Job Status | `getJobStatus` | Retrieves the current state of a bulk verification job, including its progress percentage, per-result-code totals, estimated bounce rate and any failure reason. This endpoint does not consume credits. |
| Parse Job | `parseJob` | Starts the indexing phase for a bulk verification job that was created without Auto Parse, and optionally begins verification as soon as indexing completes. Parsing does not consume credits. |
| Search Jobs | `searchJobs` | Lists the bulk verification jobs in the account, newest first, with optional filters on job id, filename and job status. Returns paging metadata alongside each job's record counts and progress. This endpoint does not consume credits. |
| Start Job | `startJob` | Begins verification of an indexed bulk job. A full run deducts one credit per billable record; setting Run Sample instead performs a free analysis that estimates the list's bounce rate without charging credits. |

<details>

<summary>See 1 more action</summary>

* **Verify Email** `verifyEmail`: Verifies a single email address in real time and returns its deliverability result (valid, invalid, disposable, catchall or unknown) together with any quality flags and a suggested spelling correction. Each verification consumes one NeverBounce credit.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Job Deleted | `job_deleted` | A bulk job has been deleted and is no longer available for verification or download. To receive this event, pass this trigger's URL as the Callback URL input on the Create Job action (or in the Callback URL field of the list upload screen at app.neverbounce.com). Payload captured from a live NeverBounce delivery. |
| Job Failed | `job_failed` | A bulk job could not be run; the reason is in the Failure Reason field of Get Job Status. To receive this event, pass this trigger's URL as the Callback URL input on the Create Job action (or in the Callback URL field of the list upload screen at app.neverbounce.com). Payload modelled from NeverBounce's documented sample; it matches the shape of the deliveries captured live for the other job events. |
| Job Parsing Finished | `job_parsing_finished` | NeverBounce has finished indexing a bulk verification job; it is now ready to be started, or will start on its own if the job was created with Auto Start. To receive this event, pass this trigger's URL as the Callback URL input on the Create Job action (or in the Callback URL field of the list upload screen at app.neverbounce.com). Payload captured from a live NeverBounce delivery. |
| Job Parsing Started | `job_parsing_started` | NeverBounce has begun indexing a bulk verification job. To receive this event, pass this trigger's URL as the Callback URL input on the Create Job action (or paste it into the Callback URL field when uploading a list at app.neverbounce.com &gt; Upload List &gt; Advanced Options). NeverBounce has no webhook-registration API, so the URL is registered per job at job-creation time. Payload captured from a live NeverBounce delivery. |
| Job Review Completed | `job_review_completed` | A bulk job has been released from NeverBounce's manual review queue. To receive this event, pass this trigger's URL as the Callback URL input on the Create Job action (or in the Callback URL field of the list upload screen at app.neverbounce.com). Payload modelled from NeverBounce's documented sample; it matches the shape of the deliveries captured live for the other job events. |
| Job Run Finished | `job_run_finished` | A bulk job has finished verifying and its results can be fetched with Get Job Results or Download Job Results. To receive this event, pass this trigger's URL as the Callback URL input on the Create Job action (or in the Callback URL field of the list upload screen at app.neverbounce.com). Payload captured from a live NeverBounce delivery. |
| Job Run Started | `job_run_started` | NeverBounce has begun verifying the records in a bulk job. To receive this event, pass this trigger's URL as the Callback URL input on the Create Job action (or in the Callback URL field of the list upload screen at app.neverbounce.com). Payload captured from a live NeverBounce delivery. |
| Job Sample Finished | `job_sample_finished` | The free sample analysis has finished and the estimated bounce rate is available from Get Job Status. To receive this event, pass this trigger's URL as the Callback URL input on the Create Job action (or in the Callback URL field of the list upload screen at app.neverbounce.com). Payload captured from a live NeverBounce delivery. |
| Job Sample Started | `job_sample_started` | NeverBounce has begun the free sample analysis of a bulk job. To receive this event, pass this trigger's URL as the Callback URL input on the Create Job action (or in the Callback URL field of the list upload screen at app.neverbounce.com). Payload captured from a live NeverBounce delivery. |
| Job Stats Updated | `job_stats_updated` | A running job has updated its record counts, which are available from Get Job Status. NeverBounce sends this event frequently while a job runs. To receive this event, pass this trigger's URL as the Callback URL input on the Create Job action (or in the Callback URL field of the list upload screen at app.neverbounce.com). Payload modelled from NeverBounce's documented sample; it matches the shape of the deliveries captured live for the other job events. |
