---
description: "Visualping watches web pages for changes. Create, update, list and delete monitoring jobs, and read change reports."
hidden: true
---

# Visualping

<img src="../../.gitbook/assets/connectors/lg/visualping.png" alt="Visualping logo">

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [visualping.io](https://visualping.io) |
| **Authentication** | Access token |
| **Slug** | `visualping` |

## Setup

Your customers enter their access token for Visualping when they connect. Nothing else needs setting up.

## Use it

Add Visualping from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.visualping.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Job</td><td><code>createJob</code></td><td>Create a new monitoring job (monitor) for a URL. Pass notification.webhook to register a webhook destination for page-change events.</td></tr><tr><td>Delete Job</td><td><code>deleteJob</code></td><td>Delete a monitoring job. Used by webhook unsubscription to remove the monitor backing a subscription.</td></tr><tr><td>Get Job</td><td><code>getJob</code></td><td>Retrieve a monitoring job by id.</td></tr><tr><td>Get Report Page</td><td><code>getReportPage</code></td><td>Reverse-chronological activity feed across every job in a workspace. All body fields are required — pass null for ones you don't want to filter on.</td></tr><tr><td>List Jobs</td><td><code>listJobs</code></td><td>List monitoring jobs with optional active-state filter and pagination.</td></tr><tr><td>Update Job</td><td><code>updateJob</code></td><td>Update a monitoring job's configuration.</td></tr></tbody></table>

## Events

Visualping has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
