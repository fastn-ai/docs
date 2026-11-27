---
description: "Amplitude is a product analytics platform. Send events, identify users, run event segmentation, export data and read cohorts and user activity."
hidden: true
---

# Amplitude

<img src="../../.gitbook/assets/connectors/lg/amplitude.png" alt="Amplitude logo">

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [amplitude.com](https://amplitude.com) |
| **Authentication** | Username and password |
| **Slug** | `amplitude` |

## Setup

Your customers enter their username and password for Amplitude when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Amplitude from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Amplitude**.
2. Select **Connect** on the Amplitude card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Amplitude's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Upload Events</td><td><code>batchUploadEvents</code></td><td>Send a large batch of events (POST api2.amplitude.com/batch).</td></tr><tr><td>Create Event Type</td><td><code>createEventType</code></td><td>Create an event type in the Taxonomy (POST amplitude.com/api/2/taxonomy/event, form-urlencoded).</td></tr><tr><td>Event Segmentation</td><td><code>eventSegmentation</code></td><td>Get event counts/segmentation over time (GET amplitude.com/api/2/events/segmentation).</td></tr><tr><td>Export Data</td><td><code>exportData</code></td><td>Export raw event data for a time range as a zip archive (GET amplitude.com/api/2/export). Returns binary.</td></tr><tr><td>Get Average Session Length</td><td><code>getAverageSessionLength</code></td><td>Get average session length over time (GET amplitude.com/api/2/sessions/average).</td></tr><tr><td>Get Cohort Members</td><td><code>getCohortMembers</code></td><td>Download a completed cohort export (GET amplitude.com/api/5/cohorts/request/{requestId}/file). Returns CSV.</td></tr><tr><td>Get Cohort Status</td><td><code>getCohortStatus</code></td><td>Check the status of a cohort export request (GET amplitude.com/api/5/cohorts/request-status/{requestId}).</td></tr><tr><td>Get User Activity</td><td><code>getUserActivity</code></td><td>Get a user's event stream (GET amplitude.com/api/2/useractivity).</td></tr><tr><td>Get User Counts</td><td><code>getUserCounts</code></td><td>Get active or new user counts (GET amplitude.com/api/2/users).</td></tr><tr><td>Identify User</td><td><code>identifyUser</code></td><td>Set user properties via the Identify API (POST api2.amplitude.com/identify, form-urlencoded).</td></tr></tbody></table>

<details>

<summary>View 5 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Cohorts</td><td><code>listCohorts</code></td><td>List all behavioral cohorts (GET amplitude.com/api/3/cohorts).</td></tr><tr><td>List Event Types</td><td><code>listEventTypes</code></td><td>List event types from the Taxonomy API (GET amplitude.com/api/2/taxonomy/event).</td></tr><tr><td>Request Cohort</td><td><code>requestCohort</code></td><td>Request a cohort membership export; returns a request_id to poll (GET amplitude.com/api/5/cohorts/request/{cohortId}).</td></tr><tr><td>Search Users</td><td><code>searchUsers</code></td><td>Find Amplitude IDs matching a user (GET amplitude.com/api/2/usersearch).</td></tr><tr><td>Upload Events</td><td><code>uploadEvents</code></td><td>Send events via the HTTP V2 API (POST api2.amplitude.com/2/httpapi).</td></tr></tbody></table>

</details>

