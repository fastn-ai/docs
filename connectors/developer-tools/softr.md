---
description: "Softr no-code app builder API."
---

# Softr

Softr no-code app builder API. Covers the Softr Database API for databases, tables, table views, table fields and records including search, and the Softr application user API for creating, deleting, activating, deactivating, inviting and syncing users of a published application, generating magic links and validating user authentication tokens. Authenticates with a Softr workspace personal access token sent in the Softr-Api-Key header; user endpoints additionally target a published application through the Softr-Domain header.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [softr.io](https://softr.io) |
| **Authentication** | Credentials you enter |
| **Actions** | 29 |
| **Events** | 0 |
| **Slug** | `softr` |

## Use it

Add Softr from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.softr.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate App User | `activateAppUser` | Reactivate a previously deactivated user in a published Softr application so they can sign in again. |
| Create App User | `createAppUser` | Create a user inside a published Softr application. When no password is supplied Softr generates one, and a magic link can be returned for passwordless sign-in. |
| Create Database | `createDatabase` | Create a new database in the specified workspace. |
| Create Record | `createRecord` | Create a new record in the specified table. |
| Create Table | `createTable` | Create a new table in the specified database. |
| Create Table Field | `createTableField` | Add a new field to a table. |
| Deactivate App User | `deactivateAppUser` | Deactivate a user in a published Softr application. Deactivated users cannot sign in and do not count towards the plan user limit, but their record is kept so they can be reactivated later. |
| Delete App User | `deleteAppUser` | Delete a user from a published Softr application, identified by their email address. The user is removed permanently. |
| Delete Database | `deleteDatabase` | Delete a specific database by its ID. It can only be deleted if it is empty, unless the 'force' parameter is used. The record is removed permanently and cannot be recovered. |
| Delete Record | `deleteRecord` | Delete a specific record by its ID. The record is removed permanently and cannot be recovered. |
| Delete Table | `deleteTable` | Delete a specific table by its ID. It can only be deleted if it is empty, unless the 'force' parameter is used. The record is removed permanently and cannot be recovered. |
| Delete Table Field | `deleteTableField` | Delete a specific field from a table. The record is removed permanently and cannot be recovered. |
| Generate User Magic Link | `generateUserMagicLink` | Generate a magic link that signs the given user into a published Softr application without a password. |
| Get Database | `getDatabase` | Retrieve details of a specific database by its ID. |
| Get Record | `getRecord` | Retrieve details of a specific record by its ID. |
| Get Table | `getTable` | Retrieve details of a specific table by its ID. |
| Get Table Field | `getTableField` | Retrieve details of a specific field. |
| Invite App User | `inviteAppUser` | Send an invitation email to an existing user of a published Softr application and move their status to Invited. The application must be published for the invitation to be delivered. |
| List Databases | `listDatabases` | Retrieve a list of all databases accessible to the authenticated user. |
| List Records | `listRecords` | Retrieve a list of all records in the specified table. |
| List Table Views | `listTableViews` | Retrieve a list of views for a specific table. |
| List Tables | `listTables` | Retrieve a list of all tables in the specified database. |
| Search Records | `searchRecords` | Search for records in the specified table based on filter, sort, and pagination criteria. |
| Sync App Users | `syncAppUsers` | Trigger a user sync for a published Softr application. Supply a JSON array of email addresses as a string to sync specific users, for example ["a@example.com","b@example.com"], or the literal [] to sync every user. |
| Update Database | `updateDatabase` | Update the details of an existing database. |
| Update Record | `updateRecord` | Partially update a specific record by its ID. Only the fields provided in the request body will be changed. |
| Update Table | `updateTable` | Update a table's name and/or description. To modify fields, use the field-specific endpoints. |
| Update Table Field | `updateTableField` | Update the properties of a specific field. |
| Validate User Token | `validateUserToken` | Validate a Softr user authentication JWT against the application's own domain. This endpoint is served by the published application rather than the Softr studio API and takes no API key, so external systems can confirm a Softr session before trusting the user identity it carries. |
