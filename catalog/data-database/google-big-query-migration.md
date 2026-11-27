---
description: "Google BigQuery Migration moves data warehouse workloads into BigQuery. Create, list, get and delete migration workflows and read translations."
hidden: true
---

# Google BigQuery Migration

<img src="../../.gitbook/assets/connectors/lg/google-big-query-migration.png" alt="Google BigQuery Migration logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [bigquerymigration.googleapis.com](https://bigquerymigration.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleBigQueryMigration` |

## Setup

Your customers sign in to Google BigQuery Migration through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google BigQuery Migration from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google BigQuery Migration**.
2. Select **Connect** on the Google BigQuery Migration card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google BigQuery Migration and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google BigQuery Migration's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Migration Workflow</td><td><code>createMigrationWorkflow</code></td><td>Creates a BigQuery migration workflow in a project and location. Pass only a displayName to create an empty workflow (safe for demos; remove it afterwards with Delete Migration Workflow), or add tasks, a map of task key to task such as {"translate": {"type": "Translation_Teradata2BQ", "translationConfigDetails": {"gcsSourcePath": "gs://bucket/in", "gcsTargetPath": "gs://bucket/out", "sourceDialect": {"teradataDialect": {"mode": "SQL"}}, "targetDialect": {"bigqueryDialect": {}}}}}. Returns the created workflow with its server-generated name. Requires the Google OAuth scope https://www.googleapis.com/auth/bigquerymigration.</td></tr><tr><td>Delete Migration Workflow</td><td><code>deleteMigrationWorkflow</code></td><td>Deletes a BigQuery migration workflow (use it to clean up the workflow made by Create Migration Workflow). Returns an empty object on success. Requires the Google OAuth scope https://www.googleapis.com/auth/bigquerymigration.</td></tr><tr><td>Get Migration Workflow</td><td><code>getMigrationWorkflow</code></td><td>Retrieves one BigQuery migration workflow by project, location and workflow ID, including its tasks, state and timestamps. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/bigquerymigration.readonly (or bigquerymigration).</td></tr><tr><td>Get Translation (MCP)</td><td><code>getTranslationMcp</code></td><td>Reads the state and result of a SQL translation started by Translate Query (MCP), by calling the read-only get_translation tool on Google's BigQuery Migration remote MCP endpoint (https://bigquerymigration.googleapis.com/mcp). Returns translationState (RUNNING, SUCCEEDED, FAILED), the translated BigQuery SQL and translation logs. Read-only; demonstrates the https://www.googleapis.com/auth/bigquerymigration.readonly scope (bigquerymigration also works).</td></tr><tr><td>List Migration Workflows</td><td><code>listMigrationWorkflows</code></td><td>Lists the BigQuery migration workflows (SQL translation and assessment jobs) in a Google Cloud project and migration location ('us' or 'eu'), with each workflow's display name, tasks, state and timestamps. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/bigquerymigration.readonly (or bigquerymigration).</td></tr><tr><td>Translate Query (MCP)</td><td><code>translateQueryMcp</code></td><td>Translates a single SQL query (e.g. Teradata, Redshift, Snowflake, Postgresql, MySQL) into BigQuery SQL by calling the translate_query tool on Google's BigQuery Migration remote MCP endpoint (https://bigquerymigration.googleapis.com/mcp, JSON-RPC tools/call). Creates a translation workflow and returns its ID plus, when finished, the translated query and logs; poll with Get Translation (MCP). This MCP toolset is the documented use of the https://www.googleapis.com/auth/bigquerymigration scope. Needs projectNumber (numeric) and location (us or eu).</td></tr></tbody></table>

