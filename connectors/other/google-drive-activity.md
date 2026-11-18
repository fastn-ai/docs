---
description: "Query the activity record of files and folders in Google Drive using the Google Drive Activity API v2."
hidden: true
---

# Google Drive Activity

Query the activity record of files and folders in Google Drive using the Google Drive Activity API v2. Returns consolidated activity events such as creates, edits, moves, renames, comments, permission changes and deletions for a Drive item or an entire folder hierarchy.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [driveactivity.googleapis.com](https://driveactivity.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 1 |
| **Events** | 0 |
| **Slug** | `googleDriveActivity` |

## Use it

Add Google Drive Activity from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleDriveActivity.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Query Drive Activity | `queryDriveActivity` | Queries the Google Drive activity record and returns a page of activities. Supply either itemName to scope the query to a single Drive item or ancestorName to scope it to a folder and all of its descendants; exactly one of the two must be provided. Results can be narrowed with a filter expression on time and action type, consolidated with a consolidation strategy, and paged with pageSize and pageToken. |
