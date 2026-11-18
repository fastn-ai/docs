---
description: "Google Cloud SQL Admin API v1 (https://sqladmin.googleapis.com/v1)."
hidden: true
---

# Google Cloud SQL Admin

<img src="../../.gitbook/assets/connectors/lg/google-cloud-sql-admin.png" alt="Google Cloud SQL Admin logo">

Google Cloud SQL Admin API v1 (https://sqladmin.googleapis.com/v1). List and inspect Cloud SQL instances, list, create and delete databases on an existing instance, poll long-running operations, list machine tiers and database flags, and list instances through the Cloud SQL read-only remote MCP endpoint. OAuth 2.0 (Google) authorization-code auth with the cloudsql, cloudsql.readonly and sqlservice.admin scopes.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [sqladmin.googleapis.com](https://sqladmin.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleCloudSqlAdmin` |

## Use it

Add Google Cloud SQL Admin from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudSqlAdmin.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Database | `createDatabase` | Creates a new, empty database on an existing Cloud SQL instance. This is a harmless, reversible change: remove the database afterwards with Delete Database. Returns a long-running Operation; poll it with Get Operation. Accepted with the https://www.googleapis.com/auth/cloudsql or https://www.googleapis.com/auth/sqlservice.admin scope. |
| Delete Database | `deleteDatabase` | Deletes a database from a Cloud SQL instance, for example the demo database made with Create Database. The database's data is permanently removed. Returns a long-running Operation; poll it with Get Operation. Accepted with the https://www.googleapis.com/auth/cloudsql or https://www.googleapis.com/auth/sqlservice.admin scope. |
| Get Instance | `getInstance` | Gets one Cloud SQL instance by its instance ID, including database version, region, tier, state, IP addresses and settings. Read-only; accepted with the https://www.googleapis.com/auth/sqlservice.admin or https://www.googleapis.com/auth/cloudsql scope. |
| Get Operation | `getOperation` | Gets the status of a Cloud SQL long-running operation, such as the CREATE_DATABASE or DELETE_DATABASE operation returned by Create Database and Delete Database. Poll until status is DONE and check error. Read-only; accepted with the https://www.googleapis.com/auth/sqlservice.admin or https://www.googleapis.com/auth/cloudsql scope. |
| List Databases | `listDatabases` | Lists the databases on a Cloud SQL instance, with each database's name, charset and collation. Read-only; accepted with the https://www.googleapis.com/auth/sqlservice.admin or https://www.googleapis.com/auth/cloudsql scope. |
| List Flags | `listFlags` | Lists the database flags that can be set on Cloud SQL instances, optionally for one database version such as POSTGRES_16 or MYSQL_8_0, with each flag's type, allowed values and whether a restart is required. Read-only; accepted with the https://www.googleapis.com/auth/sqlservice.admin or https://www.googleapis.com/auth/cloudsql scope. |
| List Instances | `listInstances` | Lists the Cloud SQL instances in a Google Cloud project, with each instance's name, database version, region, tier, state and connection settings. Use a small maxResults. Read-only; accepted with the https://www.googleapis.com/auth/sqlservice.admin or https://www.googleapis.com/auth/cloudsql scope. |
| List Instances (Read-Only MCP) | `listInstancesReadOnly` | Lists the Cloud SQL instances in a project by calling the list_instances tool on Google's Cloud SQL read-only remote MCP endpoint (https://sqladmin.googleapis.com/mcp/readonly, stateless JSON-RPC tools/call). This read-only toolset is the documented use of the https://www.googleapis.com/auth/cloudsql.readonly scope (view Cloud SQL resources and data). Returns a JSON-RPC result whose structuredContent holds items (instance name, databaseVersion, region, tier, state) and nextPageToken. |
| List Tiers | `listTiers` | Lists the Cloud SQL machine tiers (machine types) available to a Google Cloud project, with their RAM, maximum disk size and supported regions. Read-only; accepted with the https://www.googleapis.com/auth/sqlservice.admin or https://www.googleapis.com/auth/cloudsql scope. |
