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

## Use it

Add Neo4j AuraDB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.neo4jAuraDB.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Commit Transaction</td><td><code>commitTransaction</code></td><td>commits an explicit transaction, optionally running a last statement first. Docs: https://neo4j.com/docs/query-api/current/transactions/</td></tr><tr><td>Open Transaction</td><td><code>openTransaction</code></td><td>opens an explicit transaction, optionally running a first statement. Returns transaction.id and expires; on Aura the response header neo4j-cluster-affinity must be replayed on later calls. Status is 202 even on errors - check errors. Docs: https://neo4j.com/docs/query-api/current/transactions/</td></tr><tr><td>Rollback Transaction</td><td><code>rollbackTransaction</code></td><td>rolls back an explicit transaction. Docs: https://neo4j.com/docs/query-api/current/transactions/</td></tr><tr><td>Run Cypher Query</td><td><code>runCypherQuery</code></td><td>Executes a single Cypher statement against the database in an implicit (auto-commit) transaction. The database is automatically rolled back if any part of the query fails. Use this for standalone reads and writes; use the transaction actions instead when multiple statements must succeed or fail together. Docs: https://neo4j.com/docs/query-api/current/query/</td></tr><tr><td>Run Query In Transaction</td><td><code>runTransactionQuery</code></td><td>runs a statement inside an open explicit transaction (an empty statement keeps it alive). Docs: https://neo4j.com/docs/query-api/current/transactions/</td></tr></tbody></table>

## Events

Neo4j AuraDB has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
