---
description: "Google Cloud Spanner is a distributed relational database. List instances and databases, create and drop databases and run SQL in sessions."
hidden: true
---

# Google Cloud Spanner

<img src="../../.gitbook/assets/connectors/lg/google-cloud-spanner.png" alt="Google Cloud Spanner logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [spanner.googleapis.com](https://spanner.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleCloudSpanner` |

## Setup

Your customers sign in to Google Cloud Spanner through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Cloud Spanner from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Cloud Spanner**.
2. Select **Connect** on the Google Cloud Spanner card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Cloud Spanner and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Cloud Spanner's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Database</td><td><code>createDatabase</code></td><td>Creates a new GoogleSQL-dialect database on an existing Spanner instance by running CREATE DATABASE `&lt;databaseId&gt;`, optionally with extra DDL statements (for example a CREATE TABLE). Harmless and reversible: remove it afterwards with Drop Database. Returns a long-running Operation whose name is &lt;database&gt;/operations/&lt;id&gt;; the database is usually READY within seconds. Requires the https://www.googleapis.com/auth/spanner.admin scope.</td></tr><tr><td>Create Session</td><td><code>createSession</code></td><td>Creates a Spanner session on a database. A session is needed to run SQL with Execute SQL; delete it afterwards with Delete Session (idle sessions are also removed automatically after about an hour). Returns the session, whose name ends in /sessions/&lt;sessionId&gt;. Requires the https://www.googleapis.com/auth/spanner.data scope.</td></tr><tr><td>Delete Session</td><td><code>deleteSession</code></td><td>Ends a Spanner session created with Create Session and releases its server resources. Returns an empty object on success. Requires the https://www.googleapis.com/auth/spanner.data scope.</td></tr><tr><td>Drop Database</td><td><code>dropDatabase</code></td><td>Drops (deletes) a Spanner database, for example the demo database made with Create Database. All of its data is permanently removed; completed backups are kept until they expire. Returns an empty object on success. Requires the https://www.googleapis.com/auth/spanner.admin scope.</td></tr><tr><td>Execute SQL</td><td><code>executeSql</code></td><td>Executes one SQL statement in a Spanner session and returns all results in a single reply (up to 10 MiB). Without a transaction selector the query runs in a temporary strong read-only transaction, so a SELECT such as SELECT 1 or SELECT * FROM INFORMATION_SCHEMA.TABLES LIMIT 5 is read-only and safe. Supports named parameters (@name) via params and paramTypes. Returns the result set metadata and rows. Requires the https://www.googleapis.com/auth/spanner.data scope.</td></tr><tr><td>List Databases</td><td><code>listDatabases</code></td><td>Lists the databases on a Spanner instance, with each database's name, state, dialect and create time. Use a small pageSize. Read-only; requires the https://www.googleapis.com/auth/spanner.admin scope.</td></tr><tr><td>List Instance Configs</td><td><code>listInstanceConfigs</code></td><td>Lists the Spanner instance configurations (regional and multi-region placements such as regional-us-central1 or nam6) available to a Google Cloud project. Use a small pageSize. Read-only; requires the https://www.googleapis.com/auth/spanner.admin scope.</td></tr><tr><td>List Instances</td><td><code>listInstances</code></td><td>Lists the Spanner instances in a Google Cloud project, with each instance's configuration, display name, compute capacity and state. Use a small pageSize and an optional filter such as name:demo. Read-only; requires the https://www.googleapis.com/auth/spanner.admin scope.</td></tr></tbody></table>

