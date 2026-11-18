---
description: "Docker Hub API v2 connector — manage repositories, tags, image immutability rules, repository webhooks, personal access tokens, organizations, teams (groups),…"
---

# Docker Hub

Docker Hub API v2 connector — manage repositories, tags, image immutability rules, repository webhooks, personal access tokens, organizations, teams (groups), members, invites, and audit logs on hub.docker.com. Authenticates with a short-lived session JWT obtained from the Login action (username + password or PAT).

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [hub.docker.com](https://hub.docker.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 54 |
| **Events** | 0 |
| **Slug** | `dockerHub` |

## Use it

Add Docker Hub from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dockerHub.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Group Member | `addGroupMember` | Add a user to a group (team) within an organization by username. |
| Assign Group To Repository | `assignRepositoryGroup` | Grant an organization group (team) a permission level (read, write, or admin) on a repository. |
| Bulk Create Invites | `bulkCreateInvites` | Invite one or more people to an organization (optionally to a specific team and role) by email or Docker ID. Set dry_run to true to validate the invite without sending it. |
| Cancel Invite | `cancelInvite` | Cancel a pending organization invitation by its ID. |
| Check Repository | `checkRepository` | Retrieve a repository via the namespaces path and confirm it exists. Returns the repository object with HTTP 200, or 404 if it does not exist. (The Docker Hub HEAD existence-check variant is not representable through this connector tooling, so this GET variant is used.) |
| Create Access Token | `createAuthToken` | Exchange an account identifier and secret (username + password/PAT, or organization name + organization access token) for a bearer access token usable against the Docker Hub API. |
| Create Access Token (PAT) | `createAccessToken` | Create a new personal access token with a friendly label and a set of scopes. The plaintext token is returned once, on creation only. Requires a password-authenticated session. |
| Create Organization Access Token | `createOrgAccessToken` | Create an organization access token scoped to specific repositories or the whole organization. Returns the token value once, on creation. |
| Create Organization Group | `createOrgGroup` | Create a new group (team) in an organization with a name and optional description. |
| Create Repository | `createRepository` | Create a new image repository in a namespace (a user or organization). The repository name must be 2-255 lowercase characters and may contain periods, underscores, or hyphens. |
| Create Repository Webhook | `createRepositoryWebhook` | Create a webhook pipeline on a repository. The pipeline fires the configured webhook URLs when a new image is pushed. Returns the created pipeline including its slug (used to delete it). |
| Delete Access Token (PAT) | `deleteAccessToken` | Permanently delete a personal access token by its UUID. Returns HTTP 202 on success. |
| Delete Organization Access Token | `deleteOrgAccessToken` | Delete an organization access token by its ID. |
| Delete Organization Group | `deleteOrgGroup` | Delete a group (team) from an organization by name. |
| Delete Repository | `deleteRepository` | Permanently delete a repository and all of its tags from a namespace. Returns HTTP 202 on success. This is irreversible. |
| Delete Repository Tag | `deleteRepositoryTag` | Delete a specific tag from a repository. Returns HTTP 204 on success, or 404 if the tag does not exist. |
| Delete Repository Webhook | `deleteRepositoryWebhook` | Delete a webhook pipeline from a repository by its slug. Returns HTTP 204 on success. |
| Export Organization Members | `exportOrgMembers` | Export the full member list of an organization. Requires organization owner permissions. |
| Get Access Token (PAT) | `getAccessToken` | Retrieve a single personal access token by its UUID. The token value itself is not returned (only shown once at creation). |
| Get Current User | `getCurrentUser` | Retrieve the profile of the currently authenticated Docker Hub user. |
| Get Organization Access Token | `getOrgAccessToken` | Retrieve a single organization access token by its ID. |
| Get Organization Group | `getOrgGroup` | Retrieve details of a single group (team) in an organization by name. |
| Get Organization Settings | `getOrgSettings` | Retrieve an organization's settings, including its restricted-images policy. Requires organization owner permissions. |
| Get Repository | `getRepository` | Retrieve details of a single repository in a namespace, including privacy, description, pull/star counts, permissions, and immutable-tag settings. |
| Get Repository Tag | `getRepositoryTag` | Retrieve a single tag of a repository, including its per-architecture images (digest, os, architecture, size) and push/pull timestamps. |
| Get User | `getUser` | Retrieve the public profile of a Docker Hub user by username. |
| List Access Tokens | `listAccessTokens` | List the authenticated user's personal access tokens, with pagination. Requires a session authenticated with a password (personal-access-token sessions cannot manage tokens). |
| List Audit Log Actions | `listAuditActions` | List the distinct audit log action types available for an organization account, for use as filters. Requires a Team or Business subscription. |
| List Audit Log Events | `listAuditLogs` | List audit log events for an organization account, optionally filtered by action, resource name, actor, and time range. Audit logs require a Team or Business subscription. |
| List Group Members | `listGroupMembers` | List the members (users) of a group (team) within an organization, with optional search and pagination. |
| List Namespace Repositories | `listNamespaceRepositories` | List repositories in a namespace using the namespaces API path, with pagination. |
| List Organization Access Tokens | `listOrgAccessTokens` | List an organization's access tokens (organization-scoped API tokens), with pagination. |
| List Organization Groups | `listOrgGroups` | List the groups (teams) of an organization, optionally filtered by a member username or a search term. |
| List Organization Invites | `listOrgInvites` | List the pending invitations for an organization. |
| List Organization Members | `listOrgMembers` | List the members of an organization, with optional search and pagination. |
| List Repositories | `listRepositories` | List all repositories owned by a namespace (a user or organization), with pagination. |
| List Repository Tags | `listRepositoryTags` | List the tags of a repository, with pagination. Each tag includes its images (per-architecture digests and sizes) and status. |
| List Repository Webhooks | `listRepositoryWebhooks` | List the webhook pipelines configured on a repository. Each pipeline fires its webhooks when a new image is pushed to the repository. |
| List User Organizations | `listUserOrgs` | List the organizations the authenticated user belongs to, with pagination. |
| Login | `login` | Authenticate with a Docker Hub username and password (or Personal Access Token) and receive a short-lived session JWT. Use the returned token as the Session Token (JWT) credential for this connector; it typically expires in about an hour, so re-run this action and re-save the connection when it expires. If the account has 2FA enabled, a login_2fa_token is returned instead — complete authentication via the Second Factor Login action. |
| Remove Group Member | `removeGroupMember` | Remove a user from a group (team) within an organization by username. |
| Remove Organization Member | `removeOrgMember` | Remove a member from an organization by username. Requires organization owner permissions. |
| Replace Organization Group | `updateOrgGroup` | Replace a group's details (name and description) in an organization. The name is required. |
| Resend Invite | `resendInvite` | Resend a pending organization invitation email by its ID. |
| Second Factor Login | `twoFactorLogin` | Complete two-factor authentication after the Login action returned a login_2fa_token. Submit the intermediate token together with the current time-based one-time passcode to receive the session JWT. |
| Set Repository Privacy | `setRepositoryPrivacy` | Change a repository's visibility to private or public. |
| Update Access Token (PAT) | `updateAccessToken` | Update a personal access token's label and/or active state (activate or deactivate it). Only the fields you provide are changed. |
| Update Organization Access Token | `updateOrgAccessToken` | Update an organization access token's label, description, active state, or resource scopes. Only the fields you provide are changed. |
| Update Organization Group | `patchOrgGroup` | Partially update a group's details (name and/or description) in an organization. Only the fields you provide are changed. |
| Update Organization Member Role | `updateOrgMember` | Change the role of a member within an organization (owner, editor, or member). Requires organization owner permissions. |
| Update Organization Settings | `updateOrgSettings` | Update an organization's restricted-images policy, controlling whether members may pull unrestricted images and whether official and verified-publisher images are allowed. Requires organization owner permissions. |
| Update Repository | `updateRepository` | Update a repository's short description and/or full description. Only the fields you provide are changed. |
| Update Repository Immutable Tags | `updateRepositoryImmutableTags` | Enable or disable immutable-tag protection on a repository and set the tag name patterns (regular expressions) that are protected from being overwritten or deleted. |
| Verify Repository Immutable Tags | `verifyRepositoryImmutableTags` | Preview which existing tags in a repository would match a proposed set of immutable-tag rules, without applying them. |
