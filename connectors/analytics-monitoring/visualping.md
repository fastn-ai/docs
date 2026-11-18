---
description: "Visualping website-change monitoring — create and manage monitoring jobs that fire a webhook when a page changes."
---

# Visualping

Visualping website-change monitoring — create and manage monitoring jobs that fire a webhook when a page changes. Used to ingest page-change pain signals.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [visualping.io](https://visualping.io) |
| **Authentication** | Bearer token |
| **Actions** | 6 |
| **Events** | 0 |
| **Slug** | `visualping` |

## Use it

Add Visualping from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.visualping.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Job | `createJob` | Create a new monitoring job (monitor) for a URL. Pass notification.webhook to register a webhook destination for page-change events. |
| Delete Job | `deleteJob` | Delete a monitoring job. Used by webhook unsubscription to remove the monitor backing a subscription. |
| Get Job | `getJob` | Retrieve a monitoring job by id. |
| Get Report Page | `getReportPage` | Reverse-chronological activity feed across every job in a workspace. All body fields are required — pass null for ones you don't want to filter on. |
| List Jobs | `listJobs` | List monitoring jobs with optional active-state filter and pagination. |
| Update Job | `updateJob` | Update a monitoring job's configuration. |
