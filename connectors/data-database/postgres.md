---
description: "Generic PostgreSQL database connector with full introspection coverage."
hidden: true
---

# PostgreSQL

<img src="../../.gitbook/assets/connectors/lg/postgres.png" alt="PostgreSQL logo">

Generic PostgreSQL database connector with full introspection coverage. Run any SQL or use the typed introspection actions.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Authentication** | Credentials you enter |
| **Slug** | `postgres` |

## Use it

Add PostgreSQL from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.postgres.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Analyze Table | `analyzeTable` | Run ANALYZE on a table to refresh planner statistics. Schema and table are injected as identifiers. |
| Count Rows | `countRows` | Count the number of rows in a table. Schema and table names are injected as identifiers (not parametrizable in SQL). |
| Current Database | `currentDatabase` | Return the name of the currently connected database and current user. |
| Current User | `currentUser` | Return the current session user and current user (effective role). |
| Delete Rows | `deleteRows` | Delete rows from a table matching a WHERE clause. Schema/table/whereClause are injected as SQL text; values bind from params via ? placeholders. WHERE clause is required to avoid accidental full-table deletes. |
| Describe Table | `describeTable` | Return a full description of one table: columns (with type, nullability, default), primary key, foreign keys, and indexes, as a single JSON object. |
| Explain Query | `explainQuery` | Return the query plan for a SQL statement using EXPLAIN (does not execute it). Provide the statement in input.sql. |
| Get Database Size | `getDatabaseSize` | Get the on-disk size of a database (defaults to the current database). |
| Get Server Version | `getServerVersion` | Return the PostgreSQL server version string. |
| Get Table Size | `getTableSize` | Get total size (table + indexes + toast) of a table in bytes and human-readable form. |

<details>

<summary>See 29 more actions</summary>

* **Insert Rows** `insertRows`: Insert one or more rows into a table and return them (RETURNING *). Schema/table/columns/valuesClause are injected as SQL text; every value binds from params via ? placeholders, in order. Example: columns "id, name", valuesClause "(?, ?), (?, ?)", params [1,"a",2,"b"]. For bytea columns write hex: valuesClause "(?, decode(?, 'hex'))" and read it back with encode(col, 'hex') via the query action.
* **List Active Connections** `listActiveConnections`: List active backends/connections to the current database (pg_stat_activity).
* **List Columns** `listColumns`: List columns for a table with type, nullability and default.
* **List Constraints** `listConstraints`: List constraints (PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK) on a table.
* **List Databases** `listDatabases`: List all databases on the server (excluding templates).
* **List Extensions** `listExtensions`: List installed extensions in the current database.
* **List Foreign Keys** `listForeignKeys`: List foreign-key relationships for a table including referenced table and column.
* **List Functions** `listFunctions`: List functions in a schema (excludes aggregate and window; defaults to public).
* **List Indexes** `listIndexes`: List indexes defined on a table including their definitions.
* **List Locks** `listLocks`: List current locks held/awaited in the database (pg_locks joined to pg_stat_activity).
* **List Materialized Views** `listMaterializedViews`: List materialized views in a schema (defaults to public).
* **List Primary Keys** `listPrimaryKeys`: List primary key columns for a table.
* **List Procedures** `listProcedures`: List stored procedures in a schema (prokind = 'p'; defaults to public).
* **List Roles** `listRoles`: List database roles with their key attributes.
* **List Schemas** `listSchemas`: List all non-system schemas in the database.
* **List Sequences** `listSequences`: List sequences in a schema (defaults to public).
* **List Settings** `listSettings`: List server configuration parameters (pg_settings). Optionally filter by name prefix.
* **List Table Comments** `listTableComments`: List comments on tables and columns in a schema (defaults to public).
* **List Tables** `listTables`: List base tables in a schema (defaults to public).
* **List Tablespaces** `listTablespaces`: List tablespaces in the cluster.
* **List Triggers** `listTriggers`: List triggers in a schema (defaults to public).
* **List Types** `listTypes`: List user-defined enum and composite types in a schema (defaults to public).
* **List Views** `listViews`: List views in a schema (defaults to public).
* **Query** `query`: Execute any SQL statement (SELECT/INSERT/UPDATE/DELETE/DDL). SQL comes from input.sql; use ? placeholders bound positionally to input.params.
* **Select Rows** `selectRows`: Select rows from a table with an optional WHERE clause, row limit, ordering and paging. Schema/table/whereClause/orderBy/offset are injected as SQL text; use ? placeholders in whereClause bound from params (e.g. "id = ?"). To page a table pass orderBy "ORDER BY id" and offset "OFFSET 100" (include the keyword). Leave both out for the old behaviour.
* **Session Info** `sessionInfo`: Return session info: current user, database, schema, server version and backend pid.
* **Table Exists** `tableExists`: Check whether a table exists in the given schema. Returns a single row with an exists boolean.
* **Upsert Rows** `upsertRows`: Insert rows, or update them when the conflict columns already exist (INSERT ... ON CONFLICT DO UPDATE, RETURNING *). Schema/table/columns/valuesClause/conflictColumns/updateClause are injected as SQL text; values bind from params via ? placeholders. Example: columns "id, name", valuesClause "(?, ?)", conflictColumns "id", updateClause "name = EXCLUDED.name", params [1,"a"]. For bytea columns write hex with decode(?, 'hex').
* **Vacuum Table** `vacuumTable`: Run VACUUM on a table to reclaim storage. Schema and table are injected as identifiers. Cannot run inside a transaction block.

</details>
