---
description: "ThoughtSpot analytics platform — REST API v2."
hidden: true
---

# ThoughtSpot

<img src="../../.gitbook/assets/connectors/thoughtspot.png" alt="ThoughtSpot logo" width="64">

ThoughtSpot analytics platform — REST API v2. Search and AI-driven analytics over Liveboards, Answers, Metadata (worksheets, tables, models), Users, Groups, Roles, Tags, Data Objects, Connections, Orgs, Security/Sharing, Version Control (Git/TML), Reports, and Webhooks. Authenticates with a username/password login exchanged for a bearer access token against a per-tenant cluster URL (Cloud multi-tenant or self-hosted).

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [thoughtspot.com](https://thoughtspot.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `thoughtspot` |

## Use it

Add ThoughtSpot from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.thoughtspot.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate User | `activateUser` | Reactivates one or more previously deactivated ThoughtSpot user accounts. |
| Assign Tag | `assignTag` | Assigns one or more tags to a ThoughtSpot metadata object. |
| Create Group | `createGroup` | Creates a new ThoughtSpot user group used to organize users and assign shared privileges. |
| Create Role | `createRole` | Creates a new ThoughtSpot role that can be assigned to users and groups to grant a named set of privileges. |
| Create Tag | `createTag` | Creates a new ThoughtSpot tag that can be assigned to metadata objects for organization and filtering. |
| Create User | `createUser` | Creates a new ThoughtSpot user account with the given credentials, contact details, and group memberships. |
| Create Webhook | `createWebhook` | Creates a webhook destination endpoint that ThoughtSpot can deliver event payloads to. Requires an 'events' array of WebhookEventType enum values; ThoughtSpot's public docs and API error messages do not enumerate the valid values for this beta enum, so real values must be supplied by the caller (see connector notes). |
| Deactivate User | `deactivateUser` | Deactivates one or more ThoughtSpot user accounts, blocking sign-in without deleting the account. |
| Delete Group | `deleteGroup` | Permanently deletes a ThoughtSpot user group. |
| Delete Metadata Object | `deleteMetadataObject` | Permanently deletes one or more ThoughtSpot metadata objects (Liveboards, Answers, Worksheets, Models, or Connections) identified by GUID and type. |

<details>

<summary>See 34 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Role | `deleteRole` | Permanently deletes a ThoughtSpot role. |
| Delete Tag | `deleteTag` | Permanently deletes a ThoughtSpot tag. |
| Delete User | `deleteUser` | Permanently deletes a ThoughtSpot user account. |
| Delete Webhook | `deleteWebhook` | Permanently deletes one or more ThoughtSpot webhook destinations. Always returns HTTP 200 even on failure - assert failed_count is 0 and check failed_webhooks for per-item errors. |
| Export Metadata TML | `exportMetadataTml` | Exports the TML (ThoughtSpot Modeling Language) representation of one or more metadata objects, such as a Liveboard, Answer, or Worksheet. |
| Fetch Object Permissions | `fetchObjectPermissions` | Retrieves the sharing permissions currently granted on a ThoughtSpot metadata object. |
| Get Answer Data | `getAnswerData` | Retrieves the result data for a saved ThoughtSpot Answer. |
| Get Answer SQL | `getAnswerSql` | Retrieves the generated SQL query behind a saved ThoughtSpot Answer. |
| Get Connection Status | `getConnectionStatus` | Retrieves the live connectivity status of a ThoughtSpot external data connection. |
| Get Full Access Token | `getFullAccessToken` | Authenticates with a ThoughtSpot username and password and returns a bearer access token used to authorize every other action in this connector. |
| Get Liveboard Data | `getLiveboardData` | Retrieves the underlying data for the visualizations on a ThoughtSpot Liveboard. |
| Get Liveboard SQL | `getLiveboardSql` | Retrieves the generated SQL queries behind the visualizations on a ThoughtSpot Liveboard. |
| Get Session User | `getSessionUser` | Retrieves the profile and privileges of the ThoughtSpot user identified by the current bearer access token. |
| Revoke Token | `revokeToken` | Revokes a previously issued ThoughtSpot bearer access token, immediately invalidating it for further use. |
| Search Connections | `searchConnections` | Searches the external data connections configured in ThoughtSpot (e.g. Snowflake, BigQuery) and returns their configuration. |
| Search Data | `searchData` | Runs a natural-language-style search query against a ThoughtSpot data source (worksheet, model, or table) and returns the resulting rows. |
| Search Git Commits | `searchGitCommits` | Retrieves the commit history recorded against the Git repository linked to this ThoughtSpot org. |
| Search Git Config | `searchGitConfig` | Retrieves the Git repository configuration(s) linked to this ThoughtSpot org for version control of TML objects. |
| Search Groups | `searchGroups` | Searches ThoughtSpot user groups matching the given filters and returns their details. |
| Search Metadata | `searchMetadata` | Searches ThoughtSpot metadata objects (Liveboards, Answers, Worksheets, Tables, Models, Connections, and more) matching the given filters and returns their details. |
| Search Orgs | `searchOrgs` | Searches the ThoughtSpot orgs (tenants) configured on this cluster and returns their details. |
| Search Roles | `searchRoles` | Searches ThoughtSpot roles matching the given filters and returns their details. |
| Search Tags | `searchTags` | Searches ThoughtSpot tags matching the given filters and returns their details. |
| Search Users | `searchUsers` | Searches ThoughtSpot users matching the given filters and returns their profiles. |
| Search Webhooks | `searchWebhooks` | Retrieves the webhook destinations configured on this ThoughtSpot cluster. |
| Share Metadata Object | `shareMetadataObject` | Shares one or more ThoughtSpot metadata objects with specific users or groups, granting a chosen permission level. |
| Unassign Tag | `unassignTag` | Removes one or more tags from a ThoughtSpot metadata object. |
| Update Group | `updateGroup` | Updates the display name, description, or privileges of an existing ThoughtSpot user group. |
| Update Org | `updateOrg` | Updates the name, description, or status of an existing ThoughtSpot org (tenant). |
| Update Role | `updateRole` | Updates the display name or description of an existing ThoughtSpot role. |
| Update Tag | `updateTag` | Updates the name or color of an existing ThoughtSpot tag. |
| Update User | `updateUser` | Updates the profile, contact details, or group memberships of an existing ThoughtSpot user. |
| Update Webhook | `updateWebhook` | Updates the name, destination URL, or enabled state of an existing ThoughtSpot webhook. Untested against a live webhook because Create Webhook could not be certified (undocumented 'events' enum); the request/URL wiring mirrors the other webhook actions. |
| Validate Token | `validateToken` | Validates whether a ThoughtSpot bearer access token is currently active and returns the identity it is valid for. |

</details>
