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

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Upload Events | `batchUploadEvents` | Send a large batch of events (POST api2.amplitude.com/batch). |
| Create Event Type | `createEventType` | Create an event type in the Taxonomy (POST amplitude.com/api/2/taxonomy/event, form-urlencoded). |
| Event Segmentation | `eventSegmentation` | Get event counts/segmentation over time (GET amplitude.com/api/2/events/segmentation). |
| Export Data | `exportData` | Export raw event data for a time range as a zip archive (GET amplitude.com/api/2/export). Returns binary. |
| Get Average Session Length | `getAverageSessionLength` | Get average session length over time (GET amplitude.com/api/2/sessions/average). |
| Get Cohort Members | `getCohortMembers` | Download a completed cohort export (GET amplitude.com/api/5/cohorts/request/{requestId}/file). Returns CSV. |
| Get Cohort Status | `getCohortStatus` | Check the status of a cohort export request (GET amplitude.com/api/5/cohorts/request-status/{requestId}). |
| Get User Activity | `getUserActivity` | Get a user's event stream (GET amplitude.com/api/2/useractivity). |
| Get User Counts | `getUserCounts` | Get active or new user counts (GET amplitude.com/api/2/users). |
| Identify User | `identifyUser` | Set user properties via the Identify API (POST api2.amplitude.com/identify, form-urlencoded). |
| List Cohorts | `listCohorts` | List all behavioral cohorts (GET amplitude.com/api/3/cohorts). |
| List Event Types | `listEventTypes` | List event types from the Taxonomy API (GET amplitude.com/api/2/taxonomy/event). |
| Request Cohort | `requestCohort` | Request a cohort membership export; returns a request_id to poll (GET amplitude.com/api/5/cohorts/request/{cohortId}). |
| Search Users | `searchUsers` | Find Amplitude IDs matching a user (GET amplitude.com/api/2/usersearch). |
| Upload Events | `uploadEvents` | Send events via the HTTP V2 API (POST api2.amplitude.com/2/httpapi). |
