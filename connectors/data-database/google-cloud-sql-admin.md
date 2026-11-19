---
description: "Google Cloud SQL is a managed relational database service. List and inspect instances, create and delete databases and check operations."
hidden: true
---

# Google Cloud SQL Admin

<img src="../../.gitbook/assets/connectors/lg/google-cloud-sql-admin.png" alt="Google Cloud SQL Admin logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [sqladmin.googleapis.com](https://sqladmin.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleCloudSqlAdmin` |

## Setup

Your customers sign in to Google Cloud SQL Admin through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Cloud SQL Admin from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudSqlAdmin.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Database</td><td><code>createDatabase</code></td><td>Creates a new, empty database on an existing Cloud SQL instance. This is a harmless, reversible change: remove the database afterwards with Delete Database. Returns a long-running Operation; poll it with Get Operation. Accepted with the https://www.googleapis.com/auth/cloudsql or https://www.googleapis.com/auth/sqlservice.admin scope.</td></tr><tr><td>Delete Database</td><td><code>deleteDatabase</code></td><td>Deletes a database from a Cloud SQL instance, for example the demo database made with Create Database. The database's data is permanently removed. Returns a long-running Operation; poll it with Get Operation. Accepted with the https://www.googleapis.com/auth/cloudsql or https://www.googleapis.com/auth/sqlservice.admin scope.</td></tr><tr><td>Get Instance</td><td><code>getInstance</code></td><td>Gets one Cloud SQL instance by its instance ID, including database version, region, tier, state, IP addresses and settings. Read-only; accepted with the https://www.googleapis.com/auth/sqlservice.admin or https://www.googleapis.com/auth/cloudsql scope.</td></tr><tr><td>Get Operation</td><td><code>getOperation</code></td><td>Gets the status of a Cloud SQL long-running operation, such as the CREATE_DATABASE or DELETE_DATABASE operation returned by Create Database and Delete Database. Poll until status is DONE and check error. Read-only; accepted with the https://www.googleapis.com/auth/sqlservice.admin or https://www.googleapis.com/auth/cloudsql scope.</td></tr><tr><td>List Databases</td><td><code>listDatabases</code></td><td>Lists the databases on a Cloud SQL instance, with each database's name, charset and collation. Read-only; accepted with the https://www.googleapis.com/auth/sqlservice.admin or https://www.googleapis.com/auth/cloudsql scope.</td></tr><tr><td>List Flags</td><td><code>listFlags</code></td><td>Lists the database flags that can be set on Cloud SQL instances, optionally for one database version such as POSTGRES_16 or MYSQL_8_0, with each flag's type, allowed values and whether a restart is required. Read-only; accepted with the https://www.googleapis.com/auth/sqlservice.admin or https://www.googleapis.com/auth/cloudsql scope.</td></tr><tr><td>List Instances</td><td><code>listInstances</code></td><td>Lists the Cloud SQL instances in a Google Cloud project, with each instance's name, database version, region, tier, state and connection settings. Use a small maxResults. Read-only; accepted with the https://www.googleapis.com/auth/sqlservice.admin or https://www.googleapis.com/auth/cloudsql scope.</td></tr><tr><td>List Instances (Read-Only MCP)</td><td><code>listInstancesReadOnly</code></td><td>Lists the Cloud SQL instances in a project by calling the list_instances tool on Google's Cloud SQL read-only remote MCP endpoint (https://sqladmin.googleapis.com/mcp/readonly, stateless JSON-RPC tools/call). This read-only toolset is the documented use of the https://www.googleapis.com/auth/cloudsql.readonly scope (view Cloud SQL resources and data). Returns a JSON-RPC result whose structuredContent holds items (instance name, databaseVersion, region, tier, state) and nextPageToken.</td></tr><tr><td>List Tiers</td><td><code>listTiers</code></td><td>Lists the Cloud SQL machine tiers (machine types) available to a Google Cloud project, with their RAM, maximum disk size and supported regions. Read-only; accepted with the https://www.googleapis.com/auth/sqlservice.admin or https://www.googleapis.com/auth/cloudsql scope.</td></tr></tbody></table>

## Events

Google Cloud SQL Admin has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
