---
description: "Google Dataplex is a data catalog and governance service. List lakes and create, get, list and delete entry groups."
hidden: true
---

# Google Dataplex

<img src="../../.gitbook/assets/connectors/lg/google-dataplex.png" alt="Google Dataplex logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [dataplex.googleapis.com](https://dataplex.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleDataplex` |

## Setup

Your customers sign in to Google Dataplex through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Dataplex from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleDataplex.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Entry Group</td><td><code>createEntryGroup</code></td><td>Creates an empty Dataplex Universal Catalog entry group (a logical container for catalog entries) with the given ID. Returns a long-running operation; poll it with Get Operation, then read the group with Get Entry Group. Safe to demo: an empty entry group holds no data and can be removed with Delete Entry Group. Requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.read-write.</td></tr><tr><td>Delete Entry Group</td><td><code>deleteEntryGroup</code></td><td>Deletes a Dataplex Universal Catalog entry group (use it to clean up the group made by Create Entry Group). The entry group must be empty. Returns a long-running operation; poll it with Get Operation. Requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.read-write.</td></tr><tr><td>Get Entry Group</td><td><code>getEntryGroup</code></td><td>Retrieves one Dataplex Universal Catalog entry group by project, location and entry group ID. Use it to confirm an entry group exists (for example after Create Entry Group's operation completes) and to read its etag. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.readonly (or dataplex.read-write).</td></tr><tr><td>Get Operation</td><td><code>getOperation</code></td><td>Gets the status of a Dataplex long-running operation, such as the one returned by Create Entry Group or Delete Entry Group. Returns done, and either the result in response or the failure in error. Requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.read-write.</td></tr><tr><td>List Entry Groups</td><td><code>listEntryGroups</code></td><td>Lists the Dataplex Universal Catalog entry groups in a Google Cloud project and location (for example 'global' or 'us-central1'). Returns each entry group's resource name, display name, description, labels and timestamps. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.readonly (or dataplex.read-write).</td></tr><tr><td>List Lakes</td><td><code>listLakes</code></td><td>Lists the Dataplex lakes in a Google Cloud project and region, including each lake's display name, state, metastore settings and asset status. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.readonly (or dataplex.read-write).</td></tr></tbody></table>

## Events

Google Dataplex has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
