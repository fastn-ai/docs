---
description: "Azure Cosmos DB is a managed database service on Microsoft Azure. Manage database accounts, SQL databases and containers, and read keys."
hidden: true
---

# Azure Cosmos DB

<img src="../../.gitbook/assets/connectors/lg/azure-cosmos-db.png" alt="Azure Cosmos DB logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [cosmos.azure.com](https://cosmos.azure.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `azureCosmosDb` |

## Setup

Your customers sign in to Azure Cosmos DB through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Azure Cosmos DB from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Azure Cosmos DB**.
2. Select **Connect** on the Azure Cosmos DB card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Azure Cosmos DB and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Azure Cosmos DB's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create or Update SQL Database</td><td><code>createOrUpdateSqlDatabase</code></td><td>Creates a SQL (NoSQL) API database in a Cosmos DB account, or updates its throughput. Supply Options with either a manual throughput or autoscale settings; a serverless account accepts neither.</td></tr><tr><td>Delete SQL Database</td><td><code>deleteSqlDatabase</code></td><td>Deletes a SQL (NoSQL) API database and every container and document inside it. This cannot be undone unless the account has continuous backup.</td></tr><tr><td>Get Database Account</td><td><code>getDatabaseAccount</code></td><td>Gets a single Azure Cosmos DB database account, including its endpoints, read and write locations, consistency policy, capabilities and backup policy.</td></tr><tr><td>Get Database Account Read-Only Keys</td><td><code>getDatabaseAccountReadOnlyKeys</code></td><td>Gets the primary and secondary read-only master keys of a Cosmos DB account. Unlike List Database Account Keys this only needs read permission on the account.</td></tr><tr><td>Get Location</td><td><code>getLocation</code></td><td>Gets the Cosmos DB capabilities of one Azure region for this subscription, including its backup storage redundancies and availability zone support.</td></tr><tr><td>Get SQL Container</td><td><code>getSqlContainer</code></td><td>Gets a single container in a SQL (NoSQL) API database, including its partition key, indexing policy, unique key policy and time-to-live settings.</td></tr><tr><td>Get SQL Database</td><td><code>getSqlDatabase</code></td><td>Gets a single SQL (NoSQL) API database in a Cosmos DB account.</td></tr><tr><td>List Cosmos DB Operations</td><td><code>listCosmosDbOperations</code></td><td>Lists all Azure Resource Manager operations exposed by the Microsoft.DocumentDB provider, with their display names. Useful for discovering the RBAC actions Cosmos DB defines.</td></tr><tr><td>List Database Account Connection Strings</td><td><code>listDatabaseAccountConnectionStrings</code></td><td>Lists the connection strings of a Cosmos DB account, one per key and API surface. The strings embed master keys, so treat the response as a secret.</td></tr><tr><td>List Database Account Keys</td><td><code>listDatabaseAccountKeys</code></td><td>Lists the primary and secondary read-write and read-only master keys of a Cosmos DB account. These keys grant full data-plane access, so treat the response as a secret.</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Database Account Metric Definitions</td><td><code>listDatabaseAccountMetricDefinitions</code></td><td>Lists the metric definitions available for a Cosmos DB account, including each metric's unit, primary aggregation type and available time grains.</td></tr><tr><td>List Database Account Read-Only Keys</td><td><code>listDatabaseAccountReadOnlyKeys</code></td><td>Lists the primary and secondary read-only master keys of a Cosmos DB account through the POST form of the operation.</td></tr><tr><td>List Database Account Usages</td><td><code>listDatabaseAccountUsages</code></td><td>Lists the current usage quotas of a Cosmos DB account, such as document count and storage consumed, against their limits.</td></tr><tr><td>List Database Accounts</td><td><code>listDatabaseAccounts</code></td><td>Lists every Azure Cosmos DB database account in a subscription, with its API kind, locations, consistency policy and endpoints.</td></tr><tr><td>List Database Accounts by Resource Group</td><td><code>listDatabaseAccountsByResourceGroup</code></td><td>Lists the Azure Cosmos DB database accounts in a single resource group.</td></tr><tr><td>List Locations</td><td><code>listLocations</code></td><td>Lists the Azure regions where Cosmos DB is available to this subscription, with each region's supported backup storage redundancies and availability zone support.</td></tr><tr><td>List SQL Containers</td><td><code>listSqlContainers</code></td><td>Lists the containers in a SQL (NoSQL) API database, with each container's partition key, indexing policy and time-to-live settings.</td></tr><tr><td>List SQL Databases</td><td><code>listSqlDatabases</code></td><td>Lists the SQL (NoSQL) API databases in a Cosmos DB account.</td></tr></tbody></table>

</details>

