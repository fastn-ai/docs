---
description: "Google BigQuery Migration API (bigquerymigration.googleapis.com v2)."
hidden: true
---

# Google BigQuery Migration

<img src="../../.gitbook/assets/connectors/lg/google-big-query-migration.png" alt="Google BigQuery Migration logo">

Google BigQuery Migration API (bigquerymigration.googleapis.com v2). List, get, create and delete BigQuery migration workflows (SQL translation and assessment workflows used to move a data warehouse to BigQuery). Authorizes with Google OAuth 2.0 using the BigQuery Migration scopes bigquerymigration.readonly (list/get workflows) and bigquerymigration (create/delete workflows).

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [bigquerymigration.googleapis.com](https://bigquerymigration.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleBigQueryMigration` |

## Use it

Add Google BigQuery Migration from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleBigQueryMigration.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Migration Workflow | `createMigrationWorkflow` | Creates a BigQuery migration workflow in a project and location. Pass only a displayName to create an empty workflow (safe for demos; remove it afterwards with Delete Migration Workflow), or add tasks, a map of task key to task such as {"translate": {"type": "Translation_Teradata2BQ", "translationConfigDetails": {"gcsSourcePath": "gs://bucket/in", "gcsTargetPath": "gs://bucket/out", "sourceDialect": {"teradataDialect": {"mode": "SQL"}}, "targetDialect": {"bigqueryDialect": {}}}}}. Returns the created workflow with its server-generated name. Requires the Google OAuth scope https://www.googleapis.com/auth/bigquerymigration. |
| Delete Migration Workflow | `deleteMigrationWorkflow` | Deletes a BigQuery migration workflow (use it to clean up the workflow made by Create Migration Workflow). Returns an empty object on success. Requires the Google OAuth scope https://www.googleapis.com/auth/bigquerymigration. |
| Get Migration Workflow | `getMigrationWorkflow` | Retrieves one BigQuery migration workflow by project, location and workflow ID, including its tasks, state and timestamps. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/bigquerymigration.readonly (or bigquerymigration). |
| Get Translation (MCP) | `getTranslationMcp` | Reads the state and result of a SQL translation started by Translate Query (MCP), by calling the read-only get_translation tool on Google's BigQuery Migration remote MCP endpoint (https://bigquerymigration.googleapis.com/mcp). Returns translationState (RUNNING, SUCCEEDED, FAILED), the translated BigQuery SQL and translation logs. Read-only; demonstrates the https://www.googleapis.com/auth/bigquerymigration.readonly scope (bigquerymigration also works). |
| List Migration Workflows | `listMigrationWorkflows` | Lists the BigQuery migration workflows (SQL translation and assessment jobs) in a Google Cloud project and migration location ('us' or 'eu'), with each workflow's display name, tasks, state and timestamps. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/bigquerymigration.readonly (or bigquerymigration). |
| Translate Query (MCP) | `translateQueryMcp` | Translates a single SQL query (e.g. Teradata, Redshift, Snowflake, Postgresql, MySQL) into BigQuery SQL by calling the translate_query tool on Google's BigQuery Migration remote MCP endpoint (https://bigquerymigration.googleapis.com/mcp, JSON-RPC tools/call). Creates a translation workflow and returns its ID plus, when finished, the translated query and logs; poll with Get Translation (MCP). This MCP toolset is the documented use of the https://www.googleapis.com/auth/bigquerymigration scope. Needs projectNumber (numeric) and location (us or eu). |
