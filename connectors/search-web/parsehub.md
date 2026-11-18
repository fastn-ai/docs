---
description: "ParseHub is a visual web scraping service that turns websites without an API into structured data."
hidden: true
---

# ParseHub

<img src="../../.gitbook/assets/connectors/parsehub.png" alt="ParseHub logo" width="64">

ParseHub is a visual web scraping service that turns websites without an API into structured data. This connector covers the complete ParseHub API v2: listing and retrieving scraping projects, starting cloud runs with optional start URL, template and value overrides, polling run status, downloading extracted run data as JSON or CSV, retrieving the data of a project's most recent ready run, and cancelling or deleting runs.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [parsehub.com](https://parsehub.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `parsehub` |

## Use it

Add ParseHub from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.parsehub.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Run | `cancelRun` | Cancels a ParseHub run that is currently initialized, queued or running, and returns the updated run object with status cancelled. Data already extracted before cancellation may still be downloadable if the run's data_ready field is true. |
| Delete Run | `deleteRun` | Permanently deletes a ParseHub run and the data it extracted, and returns the token of the deleted run. This cannot be undone. |
| Get Last Ready Run Data | `getLastReadyRunData` | Downloads the data extracted by a project's most recent run whose data is ready, without needing to track individual run tokens. Returns JSON by default, or CSV when the format parameter is set to csv. ParseHub serves this response gzip-encoded. |
| Get Project | `getProject` | Retrieves a single ParseHub project by its project token, including its run list of the 20 most recent runs and its most recent and most recent ready run. Use the offset parameter to page further back through the run list. |
| Get Run | `getRun` | Retrieves the run object for a given run token, including its status, whether its data is ready, timings and page count. Poll this to detect when a run has finished. ParseHub rate-limits this endpoint per run to 25 calls during the first five minutes after the run started, and one call every three minutes thereafter; a project webhook configured in the ParseHub client is the recommended alternative. |
| Get Run Data | `getRunData` | Downloads the data extracted by a completed ParseHub run. Returns JSON by default, or CSV when the format parameter is set to csv. ParseHub serves this response gzip-encoded. The run's data_ready field must be true before the data is available. |
| List Projects | `listProjects` | Lists the scraping projects in your ParseHub account, most recently created first, together with the total number of projects. Projects are created in the ParseHub desktop client; the API cannot create them. |
| Run Project | `runProject` | Starts a new cloud run of a ParseHub project and returns the created run object immediately with status initialized, while the run continues in the background. Optionally override the start URL, the starting template and the starting global scope for this run, and request an email notification when the run finishes. Use Get Run to poll for completion, or configure a project webhook in the ParseHub client to be notified instead. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Run Cancelled | `cancelled` | Fires when a run of the project was cancelled, either through the Cancel Run action or in the ParseHub client. Data extracted before cancellation may still be available when data_ready is true. Setup is manual: ParseHub has no webhook registration API. In the ParseHub desktop client, open the project, go to its Settings tab, paste the fastn webhook URL into the Webhook field and save. ParseHub then POSTs to that URL whenever any of the project's runs changes its status or data_ready field. Note that ParseHub sends valid JSON with a Content-Type of application/x-www-form-urlencoded, and retries a failed delivery once per hour up to three times or until it receives an HTTP 200. |
| Run Completed | `complete` | Fires when a run of the project has finished successfully and its extracted data is ready to download with Get Run Data or Get Last Ready Run Data. Setup is manual: ParseHub has no webhook registration API. In the ParseHub desktop client, open the project, go to its Settings tab, paste the fastn webhook URL into the Webhook field and save. ParseHub then POSTs to that URL whenever any of the project's runs changes its status or data_ready field. Note that ParseHub sends valid JSON with a Content-Type of application/x-www-form-urlencoded, and retries a failed delivery once per hour up to three times or until it receives an HTTP 200. |
| Run Failed | `error` | Fires when a run of the project ended in an error. When ParseHub judges that a retry is likely to succeed it restarts the run automatically, and the payload then carries an additional new_run object holding the metadata of the restarted run. Setup is manual: ParseHub has no webhook registration API. In the ParseHub desktop client, open the project, go to its Settings tab, paste the fastn webhook URL into the Webhook field and save. ParseHub then POSTs to that URL whenever any of the project's runs changes its status or data_ready field. Note that ParseHub sends valid JSON with a Content-Type of application/x-www-form-urlencoded, and retries a failed delivery once per hour up to three times or until it receives an HTTP 200. |
| Run Initialized | `initialized` | Fires when a run of the project has been created and is about to be queued. Setup is manual: ParseHub has no webhook registration API. In the ParseHub desktop client, open the project, go to its Settings tab, paste the fastn webhook URL into the Webhook field and save. ParseHub then POSTs to that URL whenever any of the project's runs changes its status or data_ready field. Note that ParseHub sends valid JSON with a Content-Type of application/x-www-form-urlencoded, and retries a failed delivery once per hour up to three times or until it receives an HTTP 200. |
| Run Queued | `queued` | Fires when a run of the project has been queued for execution on the ParseHub cloud. Setup is manual: ParseHub has no webhook registration API. In the ParseHub desktop client, open the project, go to its Settings tab, paste the fastn webhook URL into the Webhook field and save. ParseHub then POSTs to that URL whenever any of the project's runs changes its status or data_ready field. Note that ParseHub sends valid JSON with a Content-Type of application/x-www-form-urlencoded, and retries a failed delivery once per hour up to three times or until it receives an HTTP 200. |
| Run Started | `running` | Fires when a run of the project has begun traversing pages. Setup is manual: ParseHub has no webhook registration API. In the ParseHub desktop client, open the project, go to its Settings tab, paste the fastn webhook URL into the Webhook field and save. ParseHub then POSTs to that URL whenever any of the project's runs changes its status or data_ready field. Note that ParseHub sends valid JSON with a Content-Type of application/x-www-form-urlencoded, and retries a failed delivery once per hour up to three times or until it receives an HTTP 200. |
