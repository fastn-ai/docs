---
description: "Amplitude Analytics — HTTP V2 ingest (api2.amplitude.com: /2/httpapi, /batch, /identify) plus Dashboard REST, Behavioral Cohorts, and Taxonomy APIs…"
hidden: true
---

# Amplitude

<img src="../../.gitbook/assets/connectors/lg/amplitude.png" alt="Amplitude logo">

Amplitude Analytics — HTTP V2 ingest (api2.amplitude.com: /2/httpapi, /batch, /identify) plus Dashboard REST, Behavioral Cohorts, and Taxonomy APIs (amplitude.com/api). Event upload, identify, segmentation, active/new users, session length, user search/activity, export, cohorts, and event taxonomy. Auth: HTTP Basic with API Key as username and Secret Key as password (US region). No inbound webhooks.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [amplitude.com](https://amplitude.com) |
| **Authentication** | Basic auth |
| **Slug** | `amplitude` |

## Use it

Add Amplitude from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.amplitude.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Upload Events</td><td><code>batchUploadEvents</code></td><td>Send a large batch of events (POST api2.amplitude.com/batch).</td></tr><tr><td>Create Event Type</td><td><code>createEventType</code></td><td>Create an event type in the Taxonomy (POST amplitude.com/api/2/taxonomy/event, form-urlencoded).</td></tr><tr><td>Event Segmentation</td><td><code>eventSegmentation</code></td><td>Get event counts/segmentation over time (GET amplitude.com/api/2/events/segmentation).</td></tr><tr><td>Export Data</td><td><code>exportData</code></td><td>Export raw event data for a time range as a zip archive (GET amplitude.com/api/2/export). Returns binary.</td></tr><tr><td>Get Average Session Length</td><td><code>getAverageSessionLength</code></td><td>Get average session length over time (GET amplitude.com/api/2/sessions/average).</td></tr><tr><td>Get Cohort Members</td><td><code>getCohortMembers</code></td><td>Download a completed cohort export (GET amplitude.com/api/5/cohorts/request/{requestId}/file). Returns CSV.</td></tr><tr><td>Get Cohort Status</td><td><code>getCohortStatus</code></td><td>Check the status of a cohort export request (GET amplitude.com/api/5/cohorts/request-status/{requestId}).</td></tr><tr><td>Get User Activity</td><td><code>getUserActivity</code></td><td>Get a user's event stream (GET amplitude.com/api/2/useractivity).</td></tr><tr><td>Get User Counts</td><td><code>getUserCounts</code></td><td>Get active or new user counts (GET amplitude.com/api/2/users).</td></tr><tr><td>Identify User</td><td><code>identifyUser</code></td><td>Set user properties via the Identify API (POST api2.amplitude.com/identify, form-urlencoded).</td></tr></tbody></table>

<details>

<summary>View 5 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Cohorts</td><td><code>listCohorts</code></td><td>List all behavioral cohorts (GET amplitude.com/api/3/cohorts).</td></tr><tr><td>List Event Types</td><td><code>listEventTypes</code></td><td>List event types from the Taxonomy API (GET amplitude.com/api/2/taxonomy/event).</td></tr><tr><td>Request Cohort</td><td><code>requestCohort</code></td><td>Request a cohort membership export; returns a request_id to poll (GET amplitude.com/api/5/cohorts/request/{cohortId}).</td></tr><tr><td>Search Users</td><td><code>searchUsers</code></td><td>Find Amplitude IDs matching a user (GET amplitude.com/api/2/usersearch).</td></tr><tr><td>Upload Events</td><td><code>uploadEvents</code></td><td>Send events via the HTTP V2 API (POST api2.amplitude.com/2/httpapi).</td></tr></tbody></table>

</details>
