---
description: "Val Town is a social platform for writing and hosting serverless TypeScript and JavaScript."
hidden: true
---

# Val Town

<img src="../../.gitbook/assets/connectors/lg/val-town.png" alt="Val Town logo">

Val Town is a social platform for writing and hosting serverless TypeScript and JavaScript. This connector covers vals, val branches and files, environment variables and environment variable groups, users and organizations, blob storage, the hosted SQLite database, transactional email and OpenTelemetry traces and logs through the Val Town REST API.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [val.town](https://val.town) |
| **Authentication** | Credentials you enter |
| **Slug** | `valTown` |

## Use it

Add Val Town from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.valTown.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Attach Environment Variable Group to Val | `attachEnvironmentVariableGroupToVal` | Attach an existing environment variable group to a val so its variables are available at runtime. |
| Create Environment Variable Group | `createEnvironmentVariableGroup` | Create a new account-level environment variable group. |
| Create Group Environment Variable | `createGroupEnvironmentVariable` | Create a new environment variable inside an environment variable group. |
| Create Val | `createVal` | Create a new val, optionally seeding it with files or forking an existing val. |
| Create Val Branch | `createValBranch` | Create a new branch on a val, branching from an existing branch. |
| Create Val Environment Variable | `createValEnvironmentVariable` | Create a new environment variable on a val. |
| Create Val File | `createValFile` | Create a new file or directory inside a val at the given path. |
| Delete Blob | `deleteBlob` | Permanently delete a blob by key. |
| Delete Blob (v1) | `deleteBlobV1` | Permanently delete a blob by key using the v1 endpoint. |
| Delete Environment Variable Group | `deleteEnvironmentVariableGroup` | Delete an account-level environment variable group and all of its variables. |

<details>

<summary>See 42 more actions</summary>

* **Delete Group Environment Variable** `deleteGroupEnvironmentVariable`: Delete an environment variable from an environment variable group by key.
* **Delete Val** `deleteVal`: Permanently delete a val and all of its files and branches.
* **Delete Val Branch** `deleteValBranch`: Delete a branch from a val.
* **Delete Val Environment Variable** `deleteValEnvironmentVariable`: Delete an environment variable from a val.
* **Delete Val File** `deleteValFile`: Delete a file or directory from a val at the given path.
* **Detach Environment Variable Group from Val** `detachEnvironmentVariableGroupFromVal`: Detach an environment variable group from a val.
* **Execute SQLite Batch** `executeSqliteBatch`: Run several SQL statements against the account's hosted SQLite database in one batch, optionally inside a transaction.
* **Execute SQLite Statement** `executeSqliteStatement`: Run a single SQL statement against the account's hosted SQLite database and return the rows and columns.
* **Get Authenticated User** `getAuthenticatedUser`: Retrieve the profile of the user that owns the API token, including username, tier and email.
* **Get Blob** `getBlob`: Download the contents of a single blob by key.
* **Get Blob (v1)** `getBlobV1`: Download the contents of a single blob by key using the v1 endpoint.
* **Get File by ID** `getFileById`: Retrieve the metadata of a val file by its file ID.
* **Get Google Docs Connection Token** `getGoogleDocsConnectionToken`: Exchange the caller's Val Town Google Docs connection for a short-lived Google access token.
* **Get Slack Connection Token** `getSlackConnectionToken`: Exchange the caller's Val Town Slack connection for a short-lived Slack access token.
* **Get User** `getUser`: Retrieve a Val Town user's public profile by their user ID.
* **Get User by Username** `getUserByUsername`: Look up a Val Town user by their username and return their public profile.
* **Get Val** `getVal`: Retrieve a single val by its ID, including its privacy, author and links.
* **Get Val Branch** `getValBranch`: Retrieve a single branch of a val, including its current version.
* **Get Val by Username and Name** `getValByUsernameAndName`: Look up a val by its owner's username and the val's name.
* **Get Val File Content** `getValFileContent`: Download the raw contents of a file inside a val at a given path, branch and version.
* **Get Val Viewer Context** `getValViewerContext`: Retrieve the viewer context for the val runtime, identifying the user the request is running as.
* **List Blobs** `listBlobs`: List the blobs stored in the account's blob storage, optionally filtered by key prefix.
* **List Blobs (v1)** `listBlobsV1`: List the blobs stored in the account's blob storage using the v1 endpoint, optionally filtered by key prefix.
* **List Environment Variable Groups** `listEnvironmentVariableGroups`: List the account-level environment variable groups.
* **List Group Environment Variables** `listGroupEnvironmentVariables`: List the environment variables that belong to an environment variable group.
* **List My Vals** `listMyVals`: List the vals owned by the authenticated user, with pagination.
* **List Organization Memberships** `listOrganizationMemberships`: List the members of a Val Town organization.
* **List Organizations** `listOrganizations`: List the Val Town organizations the authenticated user belongs to.
* **List Telemetry Logs** `listTelemetryLogs`: List OpenTelemetry log records emitted by the account's vals within a time range.
* **List Telemetry Traces** `listTelemetryTraces`: List OpenTelemetry traces recorded for the account's vals within a time range.
* **List Val Branches** `listValBranches`: List the branches of a val with pagination.
* **List Val Environment Variable Groups** `listValEnvironmentVariableGroups`: List the environment variable groups attached to a val.
* **List Val Environment Variables** `listValEnvironmentVariables`: List the environment variables defined directly on a val.
* **List Val Files** `listValFiles`: List the files and directories inside a val at a given path, branch and version.
* **Rename Environment Variable Group** `renameEnvironmentVariableGroup`: Rename an account-level environment variable group.
* **Search Vals** `searchVals`: Search public vals across Val Town by keyword, with pagination.
* **Send Email** `sendEmail`: Send an email from the account's Val Town address. Val Town only permits sending to the email address that owns the account.
* **Store Blob** `storeBlob`: Store or overwrite a blob under the given key. The request body is the raw blob content.
* **Store Blob (v1)** `storeBlobV1`: Store or overwrite a blob under the given key using the v1 endpoint. The request body is the raw blob content.
* **Update Val Environment Variable** `updateValEnvironmentVariable`: Update the value of an existing environment variable on a val.
* **Update Val File** `updateValFile`: Update the contents, name, type or parent directory of a file inside a val.
* **Upsert Group Environment Variable** `upsertGroupEnvironmentVariable`: Create or replace an environment variable inside an environment variable group by key.

</details>
