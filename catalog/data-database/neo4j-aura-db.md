---
description: "Neo4j AuraDB is a managed graph database. Run Cypher queries and open, commit or roll back transactions."
hidden: true
---

# Neo4j AuraDB

<img src="../../.gitbook/assets/connectors/lg/neo4j-aura-db.png" alt="Neo4j AuraDB logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [neo4j.com](https://neo4j.com) |
| **Authentication** | Username and password |
| **Slug** | `neo4jAuraDB` |

## Setup

Your customers enter their username and password for Neo4j AuraDB when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Neo4j AuraDB from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Neo4j AuraDB**.
2. Select **Connect** on the Neo4j AuraDB card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Neo4j AuraDB's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Commit Transaction</td><td><code>commitTransaction</code></td><td>commits an explicit transaction, optionally running a last statement first. Docs: https://neo4j.com/docs/query-api/current/transactions/</td></tr><tr><td>Open Transaction</td><td><code>openTransaction</code></td><td>opens an explicit transaction, optionally running a first statement. Returns transaction.id and expires; on Aura the response header neo4j-cluster-affinity must be replayed on later calls. Status is 202 even on errors - check errors. Docs: https://neo4j.com/docs/query-api/current/transactions/</td></tr><tr><td>Rollback Transaction</td><td><code>rollbackTransaction</code></td><td>rolls back an explicit transaction. Docs: https://neo4j.com/docs/query-api/current/transactions/</td></tr><tr><td>Run Cypher Query</td><td><code>runCypherQuery</code></td><td>Executes a single Cypher statement against the database in an implicit (auto-commit) transaction. The database is automatically rolled back if any part of the query fails. Use this for standalone reads and writes; use the transaction actions instead when multiple statements must succeed or fail together. Docs: https://neo4j.com/docs/query-api/current/query/</td></tr><tr><td>Run Query In Transaction</td><td><code>runTransactionQuery</code></td><td>runs a statement inside an open explicit transaction (an empty statement keeps it alive). Docs: https://neo4j.com/docs/query-api/current/transactions/</td></tr></tbody></table>

