---
description: "Azure Cosmos DB management over the Microsoft.DocumentDB Azure Resource Manager API at https://management.azure.com."
hidden: true
---

# Azure Cosmos DB

<img src="../../.gitbook/assets/connectors/azure-cosmos-db.jpg" alt="Azure Cosmos DB logo" width="64">

Azure Cosmos DB management over the Microsoft.DocumentDB Azure Resource Manager API at https://management.azure.com. Create and manage database accounts, keys and connection strings, failover and region settings, and the full resource surface for the NoSQL (SQL), MongoDB, Cassandra, Gremlin and Table APIs - databases, containers, collections, keyspaces, tables, graphs, stored procedures, user defined functions, triggers, throughput settings, data-plane role definitions and role assignments, restorable accounts and point-in-time restore resources, private endpoint connections, services and notebook workspaces. Connect with Microsoft Entra ID OAuth 2.0; the signed-in user needs Azure RBAC rights on the target subscription or resource group. Every request carries an api-version query parameter, exposed on each action with the current stable default.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [cosmos.azure.com](https://cosmos.azure.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `azureCosmosDb` |

## Use it

Add Azure Cosmos DB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.azureCosmosDb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create or Update SQL Database | `createOrUpdateSqlDatabase` | Creates a SQL (NoSQL) API database in a Cosmos DB account, or updates its throughput. Supply Options with either a manual throughput or autoscale settings; a serverless account accepts neither. |
| Delete SQL Database | `deleteSqlDatabase` | Deletes a SQL (NoSQL) API database and every container and document inside it. This cannot be undone unless the account has continuous backup. |
| Get Database Account | `getDatabaseAccount` | Gets a single Azure Cosmos DB database account, including its endpoints, read and write locations, consistency policy, capabilities and backup policy. |
| Get Database Account Read-Only Keys | `getDatabaseAccountReadOnlyKeys` | Gets the primary and secondary read-only master keys of a Cosmos DB account. Unlike List Database Account Keys this only needs read permission on the account. |
| Get Location | `getLocation` | Gets the Cosmos DB capabilities of one Azure region for this subscription, including its backup storage redundancies and availability zone support. |
| Get SQL Container | `getSqlContainer` | Gets a single container in a SQL (NoSQL) API database, including its partition key, indexing policy, unique key policy and time-to-live settings. |
| Get SQL Database | `getSqlDatabase` | Gets a single SQL (NoSQL) API database in a Cosmos DB account. |
| List Cosmos DB Operations | `listCosmosDbOperations` | Lists all Azure Resource Manager operations exposed by the Microsoft.DocumentDB provider, with their display names. Useful for discovering the RBAC actions Cosmos DB defines. |
| List Database Account Connection Strings | `listDatabaseAccountConnectionStrings` | Lists the connection strings of a Cosmos DB account, one per key and API surface. The strings embed master keys, so treat the response as a secret. |
| List Database Account Keys | `listDatabaseAccountKeys` | Lists the primary and secondary read-write and read-only master keys of a Cosmos DB account. These keys grant full data-plane access, so treat the response as a secret. |

<details>

<summary>See 8 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Database Account Metric Definitions | `listDatabaseAccountMetricDefinitions` | Lists the metric definitions available for a Cosmos DB account, including each metric's unit, primary aggregation type and available time grains. |
| List Database Account Read-Only Keys | `listDatabaseAccountReadOnlyKeys` | Lists the primary and secondary read-only master keys of a Cosmos DB account through the POST form of the operation. |
| List Database Account Usages | `listDatabaseAccountUsages` | Lists the current usage quotas of a Cosmos DB account, such as document count and storage consumed, against their limits. |
| List Database Accounts | `listDatabaseAccounts` | Lists every Azure Cosmos DB database account in a subscription, with its API kind, locations, consistency policy and endpoints. |
| List Database Accounts by Resource Group | `listDatabaseAccountsByResourceGroup` | Lists the Azure Cosmos DB database accounts in a single resource group. |
| List Locations | `listLocations` | Lists the Azure regions where Cosmos DB is available to this subscription, with each region's supported backup storage redundancies and availability zone support. |
| List SQL Containers | `listSqlContainers` | Lists the containers in a SQL (NoSQL) API database, with each container's partition key, indexing policy and time-to-live settings. |
| List SQL Databases | `listSqlDatabases` | Lists the SQL (NoSQL) API databases in a Cosmos DB account. |

</details>
