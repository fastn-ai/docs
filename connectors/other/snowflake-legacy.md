---
description: "Legacy Snowflake connector providing SQL-driven access to the Snowflake Data Cloud: databases, schemas, tables, views, columns, warehouses, users, roles,…"
hidden: true
---

# Snowflake (Legacy)

Legacy Snowflake connector providing SQL-driven access to the Snowflake Data Cloud: databases, schemas, tables, views, columns, warehouses, users, roles, grants, stages, file formats, sequences, pipes, streams, tasks, functions and procedures, plus arbitrary SQL execution. Every action runs a SQL statement through the Snowflake SQL API (POST https://{account}.snowflakecomputing.com/api/v2/statements), which is the stateless equivalent of the session endpoint the legacy Python driver connector used, and keeps the legacy credential shape of account, user and token. Authentication is Programmatic Access Token only; for key-pair JWT or OAuth, and for the Snowflake resource REST APIs, use the standard Snowflake connector instead.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [snowflake.com](https://snowflake.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 130 |
| **Events** | 0 |
| **Slug** | `snowflakeLegacy` |

## Use it

Add Snowflake (Legacy) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.snowflakeLegacy.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Abort All Queries On Warehouse | `abortQueriesOnWarehouse` | Cancels every query and statement currently running on a virtual warehouse, by running ALTER WAREHOUSE with ABORT ALL QUERIES. |
| Add Table Column | `addTableColumn` | Adds a column to an existing table by running ALTER TABLE with ADD COLUMN and the data type you supply. |
| Cancel Statement | `cancelStatement` | Cancels a statement that is still running, by calling POST /api/v2/statements/{statementHandle}/cancel. Returns an error if the statement has already finished. |
| Clone Table | `cloneTable` | Creates a zero-copy clone of a table by running CREATE TABLE with CLONE. The clone shares storage with the source until either copy is modified. |
| Copy Into Table From Stage | `copyIntoTableFromStage` | Loads staged data files into a table by running COPY INTO from a named stage with a named file format. Returns one row per file loaded, with row counts and any errors. |
| Count Rows | `countRows` | Returns the number of rows in a table by running SELECT COUNT. |
| Create Database | `createDatabase` | Creates a new database in the account by running CREATE DATABASE IF NOT EXISTS. The name is treated as an unquoted Snowflake identifier and is folded to upper case. |
| Create File Format | `createFileFormat` | Creates a named file format in a schema by running CREATE FILE FORMAT IF NOT EXISTS, describing how staged data files are parsed. |
| Create Role | `createRole` | Creates an account role by running CREATE ROLE IF NOT EXISTS. Requires a role with the CREATE ROLE privilege, such as USERADMIN or ACCOUNTADMIN. |
| Create Schema | `createSchema` | Creates a new schema inside a database by running CREATE SCHEMA IF NOT EXISTS. |
| Create Sequence | `createSequence` | Creates a sequence in a schema by running CREATE SEQUENCE IF NOT EXISTS, for generating unique increasing numbers. |
| Create Stage | `createStage` | Creates a named internal stage in a schema by running CREATE STAGE IF NOT EXISTS. Use it as a staging area for loading and unloading files. |
| Create Stream | `createStream` | Creates a change-data-capture stream on a table by running CREATE STREAM IF NOT EXISTS with ON TABLE. The stream records row-level changes made to the table. |
| Create Table | `createTable` | Creates a table by running CREATE TABLE IF NOT EXISTS with the column definitions you supply, for example ID NUMBER, NAME VARCHAR(100), CREATED_AT TIMESTAMP_NTZ. |
| Create Task | `createTask` | Creates a scheduled task in a schema by running CREATE TASK IF NOT EXISTS with a warehouse, a schedule and a SQL body. New tasks are created suspended and must be resumed before they run. |
| Create View | `createView` | Creates or replaces a view over a query by running CREATE OR REPLACE VIEW. |
| Create Warehouse | `createWarehouse` | Creates a virtual warehouse by running CREATE WAREHOUSE IF NOT EXISTS. The warehouse is created suspended with auto-resume enabled, so it only consumes credits once a query runs on it. |
| Delete Rows | `deleteRows` | Deletes the rows of a table that match a condition, by running DELETE FROM with WHERE. The condition is required so a delete can never silently empty a whole table. |
| Describe Database | `describeDatabase` | Describes a database by running DESCRIBE DATABASE, returning the schemas it contains. |
| Describe File Format | `describeFileFormat` | Returns the property values of a named file format by running DESCRIBE FILE FORMAT. |
| Describe Pipe | `describePipe` | Returns the COPY statement, notification channel and other properties of a Snowpipe pipe by running DESCRIBE PIPE. |
| Describe Query Result | `describeResult` | Returns the column metadata of a previously executed query by running DESCRIBE RESULT against its query id. The query must have been run within the last 24 hours. |
| Describe Schema | `describeSchema` | Describes a schema by running DESCRIBE SCHEMA, returning the objects it contains. |
| Describe Sequence | `describeSequence` | Returns the current value and interval of a sequence by running DESCRIBE SEQUENCE. |
| Describe Stage | `describeStage` | Returns the file format, copy and location properties of a named stage by running DESCRIBE STAGE. |
| Describe Stream | `describeStream` | Returns the properties of a change-data-capture stream by running DESCRIBE STREAM. |
| Describe Task | `describeTask` | Returns the schedule, state, warehouse and SQL definition of a task by running DESCRIBE TASK. |
| Describe User | `describeUser` | Returns the properties and parameter values of a Snowflake user by running DESCRIBE USER. Requires a role with the MANAGE USERS privilege. |
| Describe View | `describeView` | Returns the column definitions of a view by running DESCRIBE VIEW. |
| Describe Warehouse | `describeWarehouse` | Returns the property values of a virtual warehouse by running DESCRIBE WAREHOUSE. |
| Drop Database | `dropDatabase` | Drops a database by running DROP DATABASE IF EXISTS. The database moves to Time Travel and can be recovered with Undrop Database within its retention period. |
| Drop File Format | `dropFileFormat` | Drops a named file format by running DROP FILE FORMAT IF EXISTS. |
| Drop Role | `dropRole` | Drops an account role by running DROP ROLE IF EXISTS. Privileges granted to the role are removed with it. |
| Drop Schema | `dropSchema` | Drops a schema by running DROP SCHEMA IF EXISTS. The schema moves to Time Travel and can be recovered with Undrop Schema within its retention period. |
| Drop Sequence | `dropSequence` | Drops a sequence by running DROP SEQUENCE IF EXISTS. |
| Drop Stage | `dropStage` | Drops a named stage by running DROP STAGE IF EXISTS. Files held in an internal stage are deleted with it. |
| Drop Stream | `dropStream` | Drops a change-data-capture stream by running DROP STREAM IF EXISTS. |
| Drop Table | `dropTable` | Drops a table by running DROP TABLE IF EXISTS. The table moves to Time Travel and can be recovered with Undrop Table within its retention period. |
| Drop Table Column | `dropTableColumn` | Removes a column from a table by running ALTER TABLE with DROP COLUMN. The column and its data are deleted. |
| Drop Task | `dropTask` | Drops a task by running DROP TASK IF EXISTS. |
| Drop View | `dropView` | Drops a view by running DROP VIEW IF EXISTS. |
| Drop Warehouse | `dropWarehouse` | Drops a virtual warehouse by running DROP WAREHOUSE IF EXISTS. Queries running on it are cancelled. |
| Execute Query | `executeQuery` | Runs any single SQL statement through the Snowflake SQL API and returns its result set with column metadata. Set Warehouse for statements that need compute, such as SELECT. Keep result sets small; large scans consume warehouse credits. |
| Execute Task | `executeTask` | Runs a task once immediately, outside its schedule, by running EXECUTE TASK. |
| Get Current Session Context | `getCurrentContext` | Returns the account, region, user, role, warehouse, database, schema and Snowflake version the connection resolves to. Use this to confirm a connection is healthy. |
| Get Information Schema Columns | `getInformationSchemaColumns` | Returns column metadata for the tables of one schema from INFORMATION_SCHEMA.COLUMNS, including ordinal position, data type, nullability and default. |
| Get Login History | `getLoginHistory` | Returns recent login attempts against the account by querying the LOGIN_HISTORY information schema table function, including the client used and whether each attempt succeeded. |
| Get Query History | `getQueryHistory` | Returns recent queries run in the account by querying the QUERY_HISTORY information schema table function, including each query's text, status, duration and bytes scanned. |
| Get Query History By User | `getQueryHistoryByUser` | Returns the recent queries run by one user, by querying the QUERY_HISTORY_BY_USER information schema table function. |
| Get Statement Status | `getStatementStatus` | Checks the status of a statement submitted earlier and returns its result once it has finished, by calling GET /api/v2/statements/{statementHandle}. Use this for statements that returned asynchronously with HTTP 202. |
| Get Table Schema | `getTableSchema` | Returns the column definitions of a table by running DESCRIBE TABLE: column name, type, nullability, default, primary and unique key flags, and comment. |
| Get Table Storage Metrics | `getTableStorageMetrics` | Returns storage consumption per table in a database by querying the TABLE_STORAGE_METRICS information schema view: active bytes, Time Travel bytes and Fail-safe bytes. |
| Get Task History | `getTaskHistory` | Returns the recent run history of a task by querying the TASK_HISTORY information schema table function, including each run's state, return value and error. |
| Get Warehouse Load History | `getWarehouseLoadHistory` | Returns the query load on a virtual warehouse over recent hours, by querying the WAREHOUSE_LOAD_HISTORY information schema table function. |
| Get Warehouse Metering History | `getWarehouseMeteringHistory` | Returns the credits consumed per virtual warehouse over recent days, by querying the WAREHOUSE_METERING_HISTORY information schema table function. |
| Grant Database Privilege To Role | `grantPrivilegeOnDatabase` | Grants a database-level privilege to a role by running GRANT ON DATABASE TO ROLE. |
| Grant Role To Role | `grantRoleToRole` | Builds a role hierarchy by granting one account role to another, using GRANT ROLE TO ROLE. |
| Grant Role To User | `grantRoleToUser` | Grants an account role to a user by running GRANT ROLE TO USER. |
| Grant Schema Privilege To Role | `grantPrivilegeOnSchema` | Grants a schema-level privilege to a role by running GRANT ON SCHEMA TO ROLE. |
| Grant Table Privilege To Role | `grantPrivilegeOnTable` | Grants a table-level privilege to a role by running GRANT ON TABLE TO ROLE. |
| Insert Row | `insertRow` | Inserts one row into a table by running INSERT INTO with the column list and values you supply. String values must be single-quoted inside the Values field. |
| List Account Parameters | `listParameters` | Lists the account-level parameters and their current and default values by running SHOW PARAMETERS IN ACCOUNT. |
| List Alerts | `listAlerts` | Lists the alerts defined in a schema by running SHOW ALERTS IN SCHEMA, including each alert's condition, action and schedule. |
| List All Objects In Account | `listObjectsInAccount` | Lists every table and view across the account that the connected role can see, by running SHOW OBJECTS IN ACCOUNT. |
| List All Schemas In Account | `listSchemasInAccount` | Lists every schema across every database the connected role can see, by running SHOW SCHEMAS IN ACCOUNT. |
| List Connections | `listConnections` | Lists the replication connections defined in the account by running SHOW CONNECTIONS. |
| List Database Roles | `listDatabaseRoles` | Lists the database roles defined in a database by running SHOW DATABASE ROLES IN DATABASE. |
| List Databases | `listDatabases` | Lists every database in the Snowflake account that the connected user's role can see, by running SHOW DATABASES. Returns one row per database with its name, owner, comment, retention time and kind. |
| List Dynamic Tables | `listDynamicTables` | Lists the dynamic tables in a schema by running SHOW DYNAMIC TABLES IN SCHEMA, including their target lag and refresh mode. |
| List External Tables | `listExternalTables` | Lists the external tables in a schema by running SHOW EXTERNAL TABLES IN SCHEMA. |
| List File Formats | `listFileFormats` | Lists the named file formats in a schema by running SHOW FILE FORMATS IN SCHEMA. |
| List Foreign Keys | `listImportedKeys` | Lists the foreign key constraints that reference tables in a schema by running SHOW IMPORTED KEYS IN SCHEMA. |
| List Future Grants In Schema | `listFutureGrantsInSchema` | Lists the future grants defined on a schema by running SHOW FUTURE GRANTS IN SCHEMA. Future grants apply automatically to objects created later in the schema. |
| List Grantees Of Role | `listGrantsOfRole` | Lists the users and roles a role has been granted to, by running SHOW GRANTS OF ROLE. |
| List Grants On Database | `listGrantsOnDatabase` | Lists the privileges granted on a database by running SHOW GRANTS ON DATABASE. |
| List Grants On Schema | `listGrantsOnSchema` | Lists the privileges granted on a schema by running SHOW GRANTS ON SCHEMA. |
| List Grants On Table | `listGrantsOnTable` | Lists the privileges granted on a table by running SHOW GRANTS ON TABLE. |
| List Grants On Warehouse | `listGrantsOnWarehouse` | Lists the privileges granted on a virtual warehouse by running SHOW GRANTS ON WAREHOUSE. |
| List Iceberg Tables | `listIcebergTables` | Lists the Apache Iceberg tables in a schema by running SHOW ICEBERG TABLES IN SCHEMA. |
| List Integrations | `listIntegrations` | Lists all account integrations (API, notification, security, storage and catalog integrations) by running SHOW INTEGRATIONS. |
| List Locks | `listLocks` | Lists the transaction locks currently held in the account by running SHOW LOCKS IN ACCOUNT. |
| List Materialized Views | `listMaterializedViews` | Lists the materialized views in a schema by running SHOW MATERIALIZED VIEWS IN SCHEMA. Materialized views require Snowflake Enterprise Edition or higher. |
| List Native Applications | `listApplications` | Lists the Snowflake Native Apps installed in the account by running SHOW APPLICATIONS. |
| List Network Policies | `listNetworkPolicies` | Lists the network policies defined in the account by running SHOW NETWORK POLICIES. |
| List Objects In Schema | `listObjects` | Lists every table and view in a schema in one call by running SHOW OBJECTS IN SCHEMA. |
| List Open Transactions | `listTransactions` | Lists the transactions currently open in the account by running SHOW TRANSACTIONS. |
| List Pipes | `listPipes` | Lists the Snowpipe pipes in a schema by running SHOW PIPES IN SCHEMA, including each pipe's COPY definition and notification channel. |
| List Primary Keys | `listPrimaryKeys` | Lists the primary key constraints defined on the tables in a schema by running SHOW PRIMARY KEYS IN SCHEMA. |
| List Procedures | `listProcedures` | Lists the stored procedures in a schema by running SHOW PROCEDURES IN SCHEMA, including each procedure's argument signature. |
| List Regions | `listRegions` | Lists the Snowflake regions available to the account by running SHOW REGIONS. |
| List Replication Databases | `listReplicationDatabases` | Lists the primary and secondary databases available for replication across the organization by running SHOW REPLICATION DATABASES. |
| List Resource Monitors | `listResourceMonitors` | Lists the resource monitors defined in the account by running SHOW RESOURCE MONITORS, including their credit quota and current usage. |
| List Role Permissions | `listRolePermissions` | Lists every privilege granted to a role by running SHOW GRANTS TO ROLE, including the object each privilege applies to. |
| List Roles | `listRoles` | Lists every account role by running SHOW ROLES, including how many users and roles each one is granted to. |
| List Schemas | `listSchemas` | Lists the schemas in a database by running SHOW SCHEMAS IN DATABASE. Returns each schema's name, owner, comment and retention time. |
| List Secrets | `listSecrets` | Lists the secret objects defined in a schema by running SHOW SECRETS IN SCHEMA. Secret values are never returned, only the metadata. |
| List Sequences | `listSequences` | Lists the sequences in a schema by running SHOW SEQUENCES IN SCHEMA, including each sequence's next value and interval. |
| List Session Variables | `listVariables` | Lists the session variables set in the current session by running SHOW VARIABLES. The Snowflake SQL API uses a fresh session per statement, so this normally returns an empty result. |
| List Shares | `listShares` | Lists the inbound and outbound shares available to the account by running SHOW SHARES. |
| List Stage Files | `listStageFiles` | Lists the files held in a named stage by running LIST, returning each file's path, size, MD5 and last modified time. |
| List Stages | `listStages` | Lists the named internal and external stages in a schema by running SHOW STAGES IN SCHEMA. |
| List Streams | `listStreams` | Lists the change-data-capture streams in a schema by running SHOW STREAMS IN SCHEMA, including the source object each stream tracks. |
| List Table Columns | `listColumns` | Lists the columns of one table by running SHOW COLUMNS IN TABLE, returning each column's name, data type, nullability and default. |
| List Tables | `listTables` | Lists the tables in a schema by running SHOW TABLES IN SCHEMA. Returns each table's name, kind, row count, byte size and owner. |
| List Tags | `listTags` | Lists the object tags defined in a schema by running SHOW TAGS IN SCHEMA. |
| List Tasks | `listTasks` | Lists the tasks in a schema by running SHOW TASKS IN SCHEMA, including each task's schedule, state and SQL definition. |
| List User Functions | `listFunctions` | Lists the user-defined functions in a schema by running SHOW USER FUNCTIONS IN SCHEMA, including each function's argument signature and language. |
| List User Permissions | `listUserPermissions` | Lists every role granted to a Snowflake user by running SHOW GRANTS TO USER. This is the legacy connector's user-permission report. |
| List Users | `listUsers` | Lists every user in the Snowflake account by running SHOW USERS. Requires a role with the MANAGE USERS privilege, such as USERADMIN or ACCOUNTADMIN. |
| List Views | `listViews` | Lists the views defined in a schema by running SHOW VIEWS IN SCHEMA, including each view's text and owner. |
| List Warehouses | `listWarehouses` | Lists every virtual warehouse in the account visible to the connected user's role, by running SHOW WAREHOUSES. Returns each warehouse's name, state, size, cluster counts and auto-suspend settings. |
| Merge Into Table | `mergeIntoTable` | Runs a MERGE statement that upserts rows from a source query into a target table, using the join condition and the matched and not-matched clauses you supply. The target is aliased T and the source S. |
| Rename Table | `renameTable` | Renames a table within its schema by running ALTER TABLE with RENAME TO. |
| Resize Warehouse | `alterWarehouseSize` | Changes the compute size of a virtual warehouse by running ALTER WAREHOUSE with SET WAREHOUSE_SIZE. |
| Resume Task | `resumeTask` | Resumes a suspended task so it runs on its schedule, by running ALTER TASK with RESUME. |
| Resume Warehouse | `resumeWarehouse` | Resumes a suspended virtual warehouse so it can run queries, by running ALTER WAREHOUSE with RESUME IF SUSPENDED. A running warehouse consumes credits. |
| Revoke Database Privilege From Role | `revokePrivilegeOnDatabase` | Revokes a database-level privilege from a role by running REVOKE ON DATABASE FROM ROLE. |
| Revoke Role From Role | `revokeRoleFromRole` | Removes one account role from another by running REVOKE ROLE FROM ROLE. |
| Revoke Role From User | `revokeRoleFromUser` | Revokes an account role from a user by running REVOKE ROLE FROM USER. |
| Revoke Table Privilege From Role | `revokePrivilegeOnTable` | Revokes a table-level privilege from a role by running REVOKE ON TABLE FROM ROLE. |
| Select Rows | `selectRows` | Reads rows from a table by running SELECT with a row limit. Use Execute Query for projections, filters or joins. Keep the limit small; large scans consume warehouse credits. |
| Set Database Comment | `alterDatabaseComment` | Sets or replaces the comment on a database by running ALTER DATABASE with SET COMMENT. |
| Set Table Comment | `setTableComment` | Sets or replaces the comment on a table by running COMMENT ON TABLE. |
| Suspend Task | `suspendTask` | Suspends a task so it stops running on its schedule, by running ALTER TASK with SUSPEND. |
| Suspend Warehouse | `suspendWarehouse` | Suspends a running virtual warehouse so it stops consuming credits, by running ALTER WAREHOUSE with SUSPEND. Snowflake rejects this if the warehouse is already suspended. |
| Truncate Table | `truncateTable` | Removes every row from a table while keeping the table and its structure, by running TRUNCATE TABLE. The rows remain recoverable through Time Travel. |
| Undrop Database | `undropDatabase` | Restores the most recent dropped version of a database by running UNDROP DATABASE, provided it is still within the Time Travel retention period. |
| Undrop Schema | `undropSchema` | Restores the most recent dropped version of a schema by running UNDROP SCHEMA, provided it is still within the Time Travel retention period. |
| Undrop Table | `undropTable` | Restores the most recent dropped version of a table by running UNDROP TABLE, provided it is still within the Time Travel retention period. |
| Update Rows | `updateRows` | Updates the rows of a table that match a condition, by running UPDATE with SET and WHERE. The condition is required so an update can never silently rewrite a whole table. |
