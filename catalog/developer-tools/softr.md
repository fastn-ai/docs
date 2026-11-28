---
description: "Softr is a no-code app builder. Manage databases, tables, fields, records and app users."
hidden: true
---

# Softr

<img src="../../.gitbook/assets/connectors/lg/softr.png" alt="Softr logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [softr.io](https://softr.io) |
| **Authentication** | API key |
| **Slug** | `softr` |

## Setup

Your customers enter their API key for Softr when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Softr from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Softr**.
2. Select **Connect** on the Softr card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Softr's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Activate App User</td><td><code>activateAppUser</code></td><td>Reactivate a previously deactivated user in a published Softr application so they can sign in again.</td></tr><tr><td>Create App User</td><td><code>createAppUser</code></td><td>Create a user inside a published Softr application. When no password is supplied Softr generates one, and a magic link can be returned for passwordless sign-in.</td></tr><tr><td>Create Database</td><td><code>createDatabase</code></td><td>Create a new database in the specified workspace.</td></tr><tr><td>Create Record</td><td><code>createRecord</code></td><td>Create a new record in the specified table.</td></tr><tr><td>Create Table</td><td><code>createTable</code></td><td>Create a new table in the specified database.</td></tr><tr><td>Create Table Field</td><td><code>createTableField</code></td><td>Add a new field to a table.</td></tr><tr><td>Deactivate App User</td><td><code>deactivateAppUser</code></td><td>Deactivate a user in a published Softr application. Deactivated users cannot sign in and do not count towards the plan user limit, but their record is kept so they can be reactivated later.</td></tr><tr><td>Delete App User</td><td><code>deleteAppUser</code></td><td>Delete a user from a published Softr application, identified by their email address. The user is removed permanently.</td></tr><tr><td>Delete Database</td><td><code>deleteDatabase</code></td><td>Delete a specific database by its ID. It can only be deleted if it is empty, unless the 'force' parameter is used. The record is removed permanently and cannot be recovered.</td></tr><tr><td>Delete Record</td><td><code>deleteRecord</code></td><td>Delete a specific record by its ID. The record is removed permanently and cannot be recovered.</td></tr></tbody></table>

<details>

<summary>View 19 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Table</td><td><code>deleteTable</code></td><td>Delete a specific table by its ID. It can only be deleted if it is empty, unless the 'force' parameter is used. The record is removed permanently and cannot be recovered.</td></tr><tr><td>Delete Table Field</td><td><code>deleteTableField</code></td><td>Delete a specific field from a table. The record is removed permanently and cannot be recovered.</td></tr><tr><td>Generate User Magic Link</td><td><code>generateUserMagicLink</code></td><td>Generate a magic link that signs the given user into a published Softr application without a password.</td></tr><tr><td>Get Database</td><td><code>getDatabase</code></td><td>Retrieve details of a specific database by its ID.</td></tr><tr><td>Get Record</td><td><code>getRecord</code></td><td>Retrieve details of a specific record by its ID.</td></tr><tr><td>Get Table</td><td><code>getTable</code></td><td>Retrieve details of a specific table by its ID.</td></tr><tr><td>Get Table Field</td><td><code>getTableField</code></td><td>Retrieve details of a specific field.</td></tr><tr><td>Invite App User</td><td><code>inviteAppUser</code></td><td>Send an invitation email to an existing user of a published Softr application and move their status to Invited. The application must be published for the invitation to be delivered.</td></tr><tr><td>List Databases</td><td><code>listDatabases</code></td><td>Retrieve a list of all databases accessible to the authenticated user.</td></tr><tr><td>List Records</td><td><code>listRecords</code></td><td>Retrieve a list of all records in the specified table.</td></tr><tr><td>List Table Views</td><td><code>listTableViews</code></td><td>Retrieve a list of views for a specific table.</td></tr><tr><td>List Tables</td><td><code>listTables</code></td><td>Retrieve a list of all tables in the specified database.</td></tr><tr><td>Search Records</td><td><code>searchRecords</code></td><td>Search for records in the specified table based on filter, sort, and pagination criteria.</td></tr><tr><td>Sync App Users</td><td><code>syncAppUsers</code></td><td>Trigger a user sync for a published Softr application. Supply a JSON array of email addresses as a string to sync specific users, for example ["a@example.com","b@example.com"], or the literal [] to sync every user.</td></tr><tr><td>Update Database</td><td><code>updateDatabase</code></td><td>Update the details of an existing database.</td></tr><tr><td>Update Record</td><td><code>updateRecord</code></td><td>Partially update a specific record by its ID. Only the fields provided in the request body will be changed.</td></tr><tr><td>Update Table</td><td><code>updateTable</code></td><td>Update a table's name and/or description. To modify fields, use the field-specific endpoints.</td></tr><tr><td>Update Table Field</td><td><code>updateTableField</code></td><td>Update the properties of a specific field.</td></tr><tr><td>Validate User Token</td><td><code>validateUserToken</code></td><td>Validate a Softr user authentication JWT against the application's own domain. This endpoint is served by the published application rather than the Softr studio API and takes no API key, so external systems can confirm a Softr session before trusting the user identity it carries.</td></tr></tbody></table>

</details>

