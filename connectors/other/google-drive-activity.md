---
description: "Query the activity record of files and folders in Google Drive using the Google Drive Activity API v2."
hidden: true
---

# Google Drive Activity

<img src="../../.gitbook/assets/connectors/lg/google-drive-activity.png" alt="Google Drive Activity logo">

Returns consolidated activity events such as creates, edits, moves, renames, comments, permission changes and deletions for a Drive item or an entire folder hierarchy.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [driveactivity.googleapis.com](https://driveactivity.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleDriveActivity` |

## Use it

Add Google Drive Activity from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleDriveActivity.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Query Drive Activity</td><td><code>queryDriveActivity</code></td><td>Queries the Google Drive activity record and returns a page of activities. Supply either itemName to scope the query to a single Drive item or ancestorName to scope it to a folder and all of its descendants; exactly one of the two must be provided. Results can be narrowed with a filter expression on time and action type, consolidated with a consolidation strategy, and paged with pageSize and pageToken.</td></tr></tbody></table>
