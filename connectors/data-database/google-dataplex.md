---
description: "Google Cloud Dataplex Universal Catalog (dataplex.googleapis.com v1)."
hidden: true
---

# Google Dataplex

Google Cloud Dataplex Universal Catalog (dataplex.googleapis.com v1). List Dataplex lakes, list/get/create/delete Universal Catalog entry groups and poll the long-running operations they return. Authorizes with Google OAuth 2.0 using the Dataplex scopes dataplex.readonly (read lakes and entry groups) and dataplex.read-write (create/delete entry groups, read operations).

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [dataplex.googleapis.com](https://dataplex.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 6 |
| **Events** | 0 |
| **Slug** | `googleDataplex` |

## Use it

Add Google Dataplex from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleDataplex.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Entry Group | `createEntryGroup` | Creates an empty Dataplex Universal Catalog entry group (a logical container for catalog entries) with the given ID. Returns a long-running operation; poll it with Get Operation, then read the group with Get Entry Group. Safe to demo: an empty entry group holds no data and can be removed with Delete Entry Group. Requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.read-write. |
| Delete Entry Group | `deleteEntryGroup` | Deletes a Dataplex Universal Catalog entry group (use it to clean up the group made by Create Entry Group). The entry group must be empty. Returns a long-running operation; poll it with Get Operation. Requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.read-write. |
| Get Entry Group | `getEntryGroup` | Retrieves one Dataplex Universal Catalog entry group by project, location and entry group ID. Use it to confirm an entry group exists (for example after Create Entry Group's operation completes) and to read its etag. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.readonly (or dataplex.read-write). |
| Get Operation | `getOperation` | Gets the status of a Dataplex long-running operation, such as the one returned by Create Entry Group or Delete Entry Group. Returns done, and either the result in response or the failure in error. Requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.read-write. |
| List Entry Groups | `listEntryGroups` | Lists the Dataplex Universal Catalog entry groups in a Google Cloud project and location (for example 'global' or 'us-central1'). Returns each entry group's resource name, display name, description, labels and timestamps. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.readonly (or dataplex.read-write). |
| List Lakes | `listLakes` | Lists the Dataplex lakes in a Google Cloud project and region, including each lake's display name, state, metastore settings and asset status. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.readonly (or dataplex.read-write). |
