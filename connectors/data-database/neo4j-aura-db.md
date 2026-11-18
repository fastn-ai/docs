---
description: "Execute Cypher queries and manage read/write transactions against a Neo4j AuraDB graph database instance through Neo4j's official HTTP Query API (the REST…"
hidden: true
---

# Neo4j AuraDB

Execute Cypher queries and manage read/write transactions against a Neo4j AuraDB graph database instance through Neo4j's official HTTP Query API (the REST successor to the legacy Cypher transactional endpoint).

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [neo4j.com](https://neo4j.com) |
| **Authentication** | Basic auth |
| **Actions** | 5 |
| **Events** | 0 |
| **Slug** | `neo4jAuraDB` |

## Use it

Add Neo4j AuraDB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.neo4jAuraDB.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Commit Transaction | `commitTransaction` | POST /db/{db}/query/v2/tx/{txId}/commit - commits an explicit transaction, optionally running a last statement first. Docs: https://neo4j.com/docs/query-api/current/transactions/ |
| Open Transaction | `openTransaction` | POST /db/{db}/query/v2/tx - opens an explicit transaction, optionally running a first statement. Returns transaction.id and expires; on Aura the response header neo4j-cluster-affinity must be replayed on later calls. Status is 202 even on errors - check errors. Docs: https://neo4j.com/docs/query-api/current/transactions/ |
| Rollback Transaction | `rollbackTransaction` | DELETE /db/{db}/query/v2/tx/{txId} - rolls back an explicit transaction. Docs: https://neo4j.com/docs/query-api/current/transactions/ |
| Run Cypher Query | `runCypherQuery` | Executes a single Cypher statement against the database in an implicit (auto-commit) transaction. The database is automatically rolled back if any part of the query fails. Use this for standalone reads and writes; use the transaction actions instead when multiple statements must succeed or fail together. Docs: https://neo4j.com/docs/query-api/current/query/ |
| Run Query In Transaction | `runTransactionQuery` | POST /db/{db}/query/v2/tx/{txId} - runs a statement inside an open explicit transaction (an empty statement keeps it alive). Docs: https://neo4j.com/docs/query-api/current/transactions/ |
