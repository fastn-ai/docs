---
description: "Snowflake Data Cloud connector using the Snowflake SQL REST API (/api/v2/statements) and the resource-management REST APIs (databases, schemas, tables,…"
hidden: true
---

# Snowflake

<img src="../../.gitbook/assets/connectors/lg/snowflake.png" alt="Snowflake logo">

Snowflake Data Cloud connector using the Snowflake SQL REST API (/api/v2/statements) and the resource-management REST APIs (databases, schemas, tables, warehouses, users, roles, pipes, tasks). Base URL is per-account: https://{account}.snowflakecomputing.com/api/v2. Auth is key-pair JWT or OAuth bearer token supplied by the user (Phase 2 will supply a generated JWT).

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [snowflake.com](https://snowflake.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `snowflake` |

## Use it

Add Snowflake from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.snowflake.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Abort All Queries on Warehouse | `abortAllQueriesOnWarehouse` | Abort all running and queued queries on a warehouse. |
| Cancel Statement | `cancelStatement` | Cancel the execution of a running SQL statement by its handle. |
| Create Database | `createDatabase` | Create a new database. Use createMode query param (errorIfExists / orReplace / ifNotExists). |
| Create or Alter Database | `createOrAlterDatabase` | Create a database or alter it to match the specified definition (PUT idempotent). |
| Create or Alter Schema | `createOrAlterSchema` | Create or alter a schema to match the definition (PUT idempotent). |
| Create or Alter Table | `createOrAlterTable` | Create or alter a table to match the definition (PUT idempotent). |
| Create or Alter Task | `createOrAlterTask` | Create or alter a task to match the definition (PUT idempotent). |
| Create or Alter User | `createOrAlterUser` | Create or alter a user to match the definition (PUT idempotent). |
| Create or Alter Warehouse | `createOrAlterWarehouse` | Create or alter a warehouse to match the definition (PUT idempotent). |
| Create Pipe | `createPipe` | Create a pipe with a COPY INTO statement for continuous data loading. |

<details>

<summary>See 55 more actions</summary>

* **Create Role** `createRole`: Create an account-level role.
* **Create Schema** `createSchema`: Create a schema in a database. createMode query param controls existing-object behavior.
* **Create Table** `createTable`: Create a table with columns in a schema. columns is an array of {name,datatype,...} objects.
* **Create Task** `createTask`: Create a task with a SQL definition. Provide warehouse (or use serverless), optional schedule.
* **Create User** `createUser`: Create a user. Only name is required.
* **Create Warehouse** `createWarehouse`: Create a warehouse. Only name is required; size/type and other settings default per the account.
* **Delete Database** `deleteDatabase`: Drop a database by name. Set ifExists=true to avoid error if it does not exist.
* **Delete Pipe** `deletePipe`: Drop a pipe. ifExists avoids error when absent.
* **Delete Role** `deleteRole`: Drop an account-level role. ifExists avoids error when absent.
* **Delete Schema** `deleteSchema`: Drop a schema. ifExists avoids error when absent.
* **Delete Table** `deleteTable`: Drop a table. ifExists avoids error when absent.
* **Delete Task** `deleteTask`: Drop a task. ifExists avoids error when absent.
* **Delete User** `deleteUser`: Drop a user. ifExists avoids error when absent.
* **Delete Warehouse** `deleteWarehouse`: Drop a warehouse. ifExists avoids error when absent.
* **Disable Warehouse** `disableWarehouse`: Disable a warehouse so it cannot be resumed/used.
* **Enable Warehouse** `enableWarehouse`: Enable a disabled warehouse.
* **Execute Task** `executeTask`: Manually trigger a single run of a task (and optionally its graph).
* **Get Database** `getDatabase`: Fetch a single database by name.
* **Get Pipe** `getPipe`: Fetch a single pipe by name.
* **Get Schema** `getSchema`: Fetch a single schema by name within a database.
* **Get Statement Status** `getStatementStatus`: Check the status of (and retrieve results/partition for) a previously submitted SQL statement by its handle.
* **Get Table** `getTable`: Fetch a single table by name.
* **Get Task** `getTask`: Fetch a single task by name.
* **Get Task Complete Graphs** `getTaskCompleteGraphs`: Get completed task-graph runs for a task within the retention window.
* **Get Task Current Graphs** `getTaskCurrentGraphs`: Get currently scheduled/running task-graph runs for a task.
* **Get Task Dependents** `getTaskDependents`: Fetch the child (dependent) tasks of a task in its DAG.
* **Get User** `getUser`: Fetch a single user by name.
* **Get Warehouse** `getWarehouse`: Fetch a single warehouse by name.
* **Grant Future Privileges to Role** `grantFuturePrivilegesToRole`: Grant future privileges to a role on objects of a type within a container.
* **Grant Privileges to Role** `grantPrivilegesToRole`: Grant privileges (or roles) to a role on a securable.
* **Grant Role to User** `grantRoleToUser`: Grant a role to a user.
* **List Databases** `listDatabases`: List databases in the account. Supports like/startsWith/showLimit/fromName filters.
* **List Future Grants** `listFutureGrants`: List future grants associated with a role.
* **List Grants Of Role** `listGrantsOfRole`: List the users and roles that this role has been granted to.
* **List Grants On Role** `listGrantsOnRole`: List grants on this role object (privileges held on the role securable).
* **List Pipes** `listPipes`: List pipes in a schema.
* **List Role Grants** `listRoleGrants`: List privileges/roles granted to a role.
* **List Roles** `listRoles`: List account-level roles.
* **List Schemas** `listSchemas`: List schemas in a database.
* **List Tables** `listTables`: List tables in a schema.
* **List Tasks** `listTasks`: List tasks in a schema.
* **List User Grants** `listUserGrants`: List roles granted to a user.
* **List Users** `listUsers`: List users in the account.
* **List Warehouses** `listWarehouses`: List warehouses in the account.
* **Refresh Pipe** `refreshPipe`: Refresh a pipe to copy a set of staged data files to the target table.
* **Rename Warehouse** `renameWarehouse`: Rename a warehouse.
* **Resume Task** `resumeTask`: Resume a suspended task so it runs on its schedule.
* **Resume Warehouse** `resumeWarehouse`: Resume (start) a suspended warehouse.
* **Revoke Future Grants from Role** `revokeFutureGrants`: Revoke future privileges from a role.
* **Revoke Grants from Role** `revokeRoleGrants`: Revoke privileges (or roles) from a role.
* **Revoke Grants from User** `revokeUserGrants`: Revoke a role grant from a user.
* **Submit SQL Statement** `submitStatement`: Submit one or more SQL statements (query, DML, DDL) for execution via the Snowflake SQL API. Returns a ResultSet with status, metadata, and rows. Set async=true to run asynchronously and poll with getStatementStatus.
* **Suspend Task** `suspendTask`: Suspend a task so it stops running on its schedule.
* **Suspend Warehouse** `suspendWarehouse`: Suspend (stop) a running warehouse.
* **Use Warehouse** `useWarehouse`: Set the warehouse as the current warehouse for the session.

</details>
