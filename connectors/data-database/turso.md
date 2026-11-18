---
description: "Turso is a managed SQLite-compatible edge database platform built on libSQL."
hidden: true
---

# Turso

Turso is a managed SQLite-compatible edge database platform built on libSQL. This connector wraps the Turso Platform API to manage databases, database tokens, instances, groups, locations, organizations, members, invites, API tokens and audit logs.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [turso.tech](https://turso.tech) |
| **Authentication** | Credentials you enter |
| **Actions** | 49 |
| **Events** | 0 |
| **Slug** | `turso` |

## Use it

Add Turso from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.turso.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Location to Group | `addLocationToGroup` | Adds a location to the specified group. Calls POST /v1/organizations/{organizationSlug}/groups/{groupName}/locations/{location} on the Turso API. |
| Add Member | `addMember` | Add an existing Turso user to an organization. Calls POST /v1/organizations/{organizationSlug}/members on the Turso API. |
| Create API Token | `createApiToken` | Creates a new Platform API token for the authenticated user and returns the token value. The token value is shown only once, so store it immediately. Calls POST /v1/auth/api-tokens/{tokenName} on the Turso API. |
| Create Database | `createDatabase` | Creates a new database in a group for the organization or user. Calls POST /v1/organizations/{organizationSlug}/databases on the Turso API. |
| Create Group | `createGroup` | Creates a new group for the organization or user. Calls POST /v1/organizations/{organizationSlug}/groups on the Turso API. |
| Create Group Auth Token | `createGroupAuthToken` | Generates an authorization token for the specified group. Calls POST /v1/organizations/{organizationSlug}/groups/{groupName}/auth/tokens on the Turso API. |
| Current Subscription | `currentSubscription` | Returns the current subscription details for the organization. Calls GET /v1/organizations/{organizationSlug}/subscription on the Turso API. |
| Delete Database | `deleteDatabase` | Delete a database belonging to the organization or user. Calls DELETE /v1/organizations/{organizationSlug}/databases/{databaseName} on the Turso API. |
| Delete Group | `deleteGroup` | Delete a group belonging to the organization or user. Calls DELETE /v1/organizations/{organizationSlug}/groups/{groupName} on the Turso API. |
| Delete Invite | `deleteInvite` | Delete a pending invite for the organization by email. Calls DELETE /v2/organizations/{organizationSlug}/invites/{email} on the Turso API. |
| Generate Database Auth Token | `generateDatabaseAuthToken` | Generates an authorization token for the specified database. Calls POST /v1/organizations/{organizationSlug}/databases/{databaseName}/auth/tokens on the Turso API. |
| Get Current User | `getCurrentUser` | Returns information about the currently authenticated user. Calls GET /v1/user on the Turso API. |
| Invalidate All Database Auth Tokens | `invalidateAllDatabaseAuthTokens` | Invalidates all authorization tokens for the specified database. Calls POST /v1/organizations/{organizationSlug}/databases/{databaseName}/auth/rotate on the Turso API. |
| Invalidate All Group Auth Tokens | `invalidateAllGroupAuthTokens` | Invalidates all authorization tokens for the specified group. Calls POST /v1/organizations/{organizationSlug}/groups/{groupName}/auth/rotate on the Turso API. |
| Invite Organization Member | `inviteOrganizationMember` | Invite a user to an organization. If the user isn't already registered with Turso, they will receive a signup link. If an existing pending invite exists for the same email, it will be replaced. Calls POST /v2/organizations/{organizationSlug}/invites on the Turso API. |
| List API Tokens | `listApiTokens` | Returns a list of API tokens belonging to a user. Calls GET /v1/auth/api-tokens on the Turso API. |
| List Audit Logs | `listAuditLogs` | Return the audit logs for the given organization, ordered by the `created_at` field in descending order. Calls GET /v1/organizations/{organizationSlug}/audit-logs on the Turso API. |
| List Database Instances | `listDatabaseInstances` | Returns a list of instances of a database. Instances are the individual primary or replica databases in each region defined by the group. Calls GET /v1/organizations/{organizationSlug}/databases/{databaseName}/instances on the Turso API. |
| List Databases | `listDatabases` | Returns a list of databases belonging to the organization or user. Calls GET /v1/organizations/{organizationSlug}/databases on the Turso API. |
| List Groups | `listGroups` | Returns a list of groups belonging to the organization or user. Calls GET /v1/organizations/{organizationSlug}/groups on the Turso API. |
| List Invites | `listInvites` | Returns a list of pending invites for the organization. Calls GET /v2/organizations/{organizationSlug}/invites on the Turso API. |
| List Invoices | `listInvoices` | Returns a list of invoices for the organization. Calls GET /v1/organizations/{organizationSlug}/invoices on the Turso API. |
| List Locations | `listLocations` | Returns a list of locations where you can create or replicate databases. Calls GET /v1/locations on the Turso API. |
| List Members | `listMembers` | Returns a list of members part of the organization. Calls GET /v1/organizations/{organizationSlug}/members on the Turso API. |
| List Organization API Tokens | `listOrganizationApiTokens` | Returns the API tokens scoped to this organization (both organization-scoped and group-scoped). Unrestricted tokens are not returned here — manage those via [`GET /v1/auth/api-tokens`](/api-reference/tokens/list). Authorization is symmetric with the revoke endpoint: - **Admins and owners** see every token scoped to the organization, with the minting user attached in the `owner` field. - **Members and viewers** see only tokens they minted themselves. This mirrors the personal-access-token model used in GitHub organization settings: admins get the full attribution list; everyone else sees their own access. Calls GET /v1/organizations/{organizationSlug}/api-tokens on the Turso API. |
| List Organizations | `listOrganizations` | Returns a list of organizations the authenticated user owns or is a member of. Calls GET /v1/organizations on the Turso API. |
| List Plans | `listPlans` | Returns a list of available plans and their quotas. Calls GET /v1/organizations/{organizationSlug}/plans on the Turso API. |
| Organization Usage | `organizationUsage` | Fetch current billing cycle usage for an organization. Calls GET /v1/organizations/{organizationSlug}/usage on the Turso API. |
| Remove Location from Group | `removeLocationFromGroup` | Removes a location from the specified group. Calls DELETE /v1/organizations/{organizationSlug}/groups/{groupName}/locations/{location} on the Turso API. |
| Remove Member | `removeMember` | Remove a user from the organization by username. Calls DELETE /v1/organizations/{organizationSlug}/members/{username} on the Turso API. |
| Retrieve Database | `retrieveDatabase` | Returns a database belonging to the organization or user. Calls GET /v1/organizations/{organizationSlug}/databases/{databaseName} on the Turso API. |
| Retrieve Database Configuration | `retrieveDatabaseConfiguration` | Retrieve an individual database configuration belonging to the organization or user. Calls GET /v1/organizations/{organizationSlug}/databases/{databaseName}/configuration on the Turso API. |
| Retrieve Database Instance | `retrieveDatabaseInstance` | Return the individual database instance by name. Calls GET /v1/organizations/{organizationSlug}/databases/{databaseName}/instances/{instanceName} on the Turso API. |
| Retrieve Database Stats | `retrieveDatabaseStats` | Fetch the top queries of a database, including the count of rows read and written. Calls GET /v1/organizations/{organizationSlug}/databases/{databaseName}/stats on the Turso API. |
| Retrieve Database Usage | `retrieveDatabaseUsage` | Fetch activity usage for a database in a given time period. Calls GET /v1/organizations/{organizationSlug}/databases/{databaseName}/usage on the Turso API. |
| Retrieve Group | `retrieveGroup` | Returns a group belonging to the organization or user. Calls GET /v1/organizations/{organizationSlug}/groups/{groupName} on the Turso API. |
| Retrieve Group Configuration | `retrieveGroupConfiguration` | Retrieve an individual group configuration belonging to the organization or user. Calls GET /v1/organizations/{organizationSlug}/groups/{groupName}/configuration on the Turso API. |
| Retrieve Member | `retrieveMember` | Retrieve details of a specific member in the organization. Calls GET /v1/organizations/{organizationSlug}/members/{username} on the Turso API. |
| Retrieve Organization | `retrieveOrganization` | Retrieve details of a specific organization. Calls GET /v1/organizations/{organizationSlug} on the Turso API. |
| Revoke API Token | `revokeApiToken` | Revokes the provided API token belonging to a user. Calls DELETE /v1/auth/api-tokens/{tokenName} on the Turso API. |
| Revoke Organization API Token | `revokeOrganizationApiToken` | Revokes a token scoped to this organization. The path takes a token **ID**, not a name, because names are unique per user but not across users — an admin revoking a member's token can't disambiguate by name alone. Authorization is symmetric with the list endpoint: - **Admins and owners** can revoke any token scoped to the organization (org-scoped or group-scoped, regardless of who minted it). - **Members and viewers** can revoke only tokens they minted themselves. A token scoped to a different organization returns `404`, not `403`, so the endpoint does not leak the existence of cross-org token IDs. Unrestricted tokens are also unreachable here and must be revoked via [`DELETE /v1/auth/api-tokens/{tokenName}`](/api-reference/tokens/revoke). Calls DELETE /v1/organizations/{organizationSlug}/api-tokens/{tokenId} on the Turso API. |
| Transfer Group | `transferGroup` | Transfer a group to another organization that you own or a member of. Calls POST /v1/organizations/{organizationSlug}/groups/{groupName}/transfer on the Turso API. |
| Unarchive Group | `unarchiveGroup` | Unarchive a group that has been archived due to inactivity. Calls POST /v1/organizations/{organizationSlug}/groups/{groupName}/unarchive on the Turso API. |
| Update Database Configuration | `updateDatabaseConfiguration` | Update a database configuration belonging to the organization or user. Calls PATCH /v1/organizations/{organizationSlug}/databases/{databaseName}/configuration on the Turso API. |
| Update Databases in Group | `updateDatabasesInGroup` | Updates all databases in the group to the latest libSQL version. Calls POST /v1/organizations/{organizationSlug}/groups/{groupName}/update on the Turso API. |
| Update Group Configuration | `updateGroupConfiguration` | Update a group configuration belonging to the organization or user. Calls PATCH /v1/organizations/{organizationSlug}/groups/{groupName}/configuration on the Turso API. |
| Update Member Role | `updateMemberRole` | Update the role of an organization member. Only organization admins or owners can perform this action. Calls PATCH /v1/organizations/{organizationSlug}/members/{username} on the Turso API. |
| Update Organization | `updateOrganization` | Update an organization you own or are a member of. Calls PATCH /v1/organizations/{organizationSlug} on the Turso API. |
| Validate API Token | `validateApiToken` | Validates an API token belonging to a user. Calls GET /v1/auth/validate on the Turso API. |
