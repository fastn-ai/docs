---
description: "Google Cloud Spanner API v1 (https://spanner.googleapis.com/v1)."
---

# Google Cloud Spanner

Google Cloud Spanner API v1 (https://spanner.googleapis.com/v1). List instance configurations, instances and databases, create and drop databases on an existing instance, and run SQL queries through sessions (create session, execute SQL, delete session). OAuth 2.0 (Google) authorization-code auth with the spanner.admin and spanner.data scopes.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [spanner.googleapis.com](https://spanner.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 8 |
| **Events** | 0 |
| **Slug** | `googleCloudSpanner` |

## Use it

Add Google Cloud Spanner from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudSpanner.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Database | `createDatabase` | Creates a new GoogleSQL-dialect database on an existing Spanner instance by running CREATE DATABASE `&lt;databaseId&gt;`, optionally with extra DDL statements (for example a CREATE TABLE). Harmless and reversible: remove it afterwards with Drop Database. Returns a long-running Operation whose name is &lt;database&gt;/operations/&lt;id&gt;; the database is usually READY within seconds. Requires the https://www.googleapis.com/auth/spanner.admin scope. |
| Create Session | `createSession` | Creates a Spanner session on a database. A session is needed to run SQL with Execute SQL; delete it afterwards with Delete Session (idle sessions are also removed automatically after about an hour). Returns the session, whose name ends in /sessions/&lt;sessionId&gt;. Requires the https://www.googleapis.com/auth/spanner.data scope. |
| Delete Session | `deleteSession` | Ends a Spanner session created with Create Session and releases its server resources. Returns an empty object on success. Requires the https://www.googleapis.com/auth/spanner.data scope. |
| Drop Database | `dropDatabase` | Drops (deletes) a Spanner database, for example the demo database made with Create Database. All of its data is permanently removed; completed backups are kept until they expire. Returns an empty object on success. Requires the https://www.googleapis.com/auth/spanner.admin scope. |
| Execute SQL | `executeSql` | Executes one SQL statement in a Spanner session and returns all results in a single reply (up to 10 MiB). Without a transaction selector the query runs in a temporary strong read-only transaction, so a SELECT such as SELECT 1 or SELECT * FROM INFORMATION_SCHEMA.TABLES LIMIT 5 is read-only and safe. Supports named parameters (@name) via params and paramTypes. Returns the result set metadata and rows. Requires the https://www.googleapis.com/auth/spanner.data scope. |
| List Databases | `listDatabases` | Lists the databases on a Spanner instance, with each database's name, state, dialect and create time. Use a small pageSize. Read-only; requires the https://www.googleapis.com/auth/spanner.admin scope. |
| List Instance Configs | `listInstanceConfigs` | Lists the Spanner instance configurations (regional and multi-region placements such as regional-us-central1 or nam6) available to a Google Cloud project. Use a small pageSize. Read-only; requires the https://www.googleapis.com/auth/spanner.admin scope. |
| List Instances | `listInstances` | Lists the Spanner instances in a Google Cloud project, with each instance's configuration, display name, compute capacity and state. Use a small pageSize and an optional filter such as name:demo. Read-only; requires the https://www.googleapis.com/auth/spanner.admin scope. |
