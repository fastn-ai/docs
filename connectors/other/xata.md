---
description: "Xata is a serverless PostgreSQL platform with instant copy-on-write database branches, scale to zero, backups and zero-downtime schema changes."
hidden: true
---

# Xata

<img src="../../.gitbook/assets/connectors/xata.png" alt="Xata logo" width="64">

Xata is a serverless PostgreSQL platform with instant copy-on-write database branches, scale to zero, backups and zero-downtime schema changes. This connector covers the complete Xata control-plane API (api.xata.tech): organizations, members, roles and invitations, organization and user API keys, SSO domains and identity providers, billing customer, invoices and checkout sessions, regions, instance types, images and extensions, resource limits, projects, branches with credentials, metrics, logs, PostgreSQL configuration and backup restores, GitHub App installations and repository mappings, plus the MCP endpoint and the branch SQL gateway.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [xata.io](https://xata.io) |
| **Authentication** | Bearer token |
| **Slug** | `xata` |

## Use it

Add Xata from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.xata.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Claim SSO Domain | `claimSsoDomain` | Claims an email domain for SSO and returns the DNS TXT record that proves control of it. Nothing changes for sign-in until the domain is verified. Wildcards and public email providers are rejected. |
| Create Billing Checkout Session | `createBillingCheckoutSession` | Creates a Stripe checkout session used to activate card billing for an organization and returns its URL. |
| Create Billing Payment Method Session | `createBillingPaymentMethodSession` | Creates a Stripe setup-mode checkout session used to add or update an organization's payment method and returns its URL. |
| Create Branch | `createBranch` | Creates a new database branch in a project, either inheriting its parent's configuration (mode inherit) or with a custom configuration (mode custom: region, instance type, image, storage, replicas, PostgreSQL parameters and preload libraries). Optionally sets scale-to-zero and backup settings. |
| Create GitHub App Installation | `createGithubAppInstallation` | Registers a GitHub App installation id with an organization so repositories can be mapped to Xata branches. |
| Create GitHub Repository Mapping | `createGithubRepositoryMapping` | Maps a GitHub repository to a Xata branch so the GitHub App can create preview branches for pull requests. |
| Create Organization | `createOrganization` | Creates a new organization with the authenticated user as its single owner. Requires a personal (user) API key; organization API keys cannot create organizations. |
| Create Organization API Key | `createOrganizationApiKey` | Creates a new API key for an organization, optionally limited to specific scopes, projects or branches and with an expiry date. The key token is returned only in this response. |
| Create Organization Invitation | `createOrganizationInvitation` | Sends an invitation email asking a user to join the organization. This delivers mail to a real person; use with care. |
| Create Project | `createProject` | Creates a new project in an organization. Projects are containers for database branches. Optionally set the scale-to-zero defaults for base and child branches and IP filtering. |

<details>

<summary>See 59 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create SSO Provider | `createSsoProvider` | Registers an identity provider (Google, Microsoft or generic OIDC) for a verified SSO domain. OIDC and Microsoft need an issuer URL; the client secret is write-only. |
| Create User API Key | `createUserApiKey` | Creates a personal API key for the authenticated user, optionally limited to scopes, projects or branches and with an expiry. The token is returned only once. Only available when connected with a personal (user) API key. |
| Delete Branch | `deleteBranch` | Permanently deletes a branch and all of its data. This cannot be undone. |
| Delete GitHub Repository Mapping | `deleteGithubRepositoryMapping` | Removes the GitHub repository mapping from a branch. |
| Delete Organization | `deleteOrganization` | Permanently deletes an organization. Xata documents this endpoint as not implemented yet; use Request Organization Deletion instead. This action cannot be undone. |
| Delete Organization API Keys | `deleteOrganizationApiKeys` | Deletes one or more organization API keys by id in a single request. |
| Delete Organization Invitation | `deleteOrganizationInvitation` | Permanently deletes an organization invitation by id. |
| Delete Project | `deleteProject` | Permanently deletes a project and all of its branches and databases. This cannot be undone. |
| Delete SSO Domain | `deleteSsoDomain` | Drops a pending domain claim or releases a verified SSO domain. Refused with 409 while an identity provider is still bound to the domain. Idempotent. |
| Delete SSO Provider | `deleteSsoProvider` | Removes an identity provider so members on its domain fall back to their previous sign-in methods. The domain stays verified. Idempotent. |
| Delete User API Keys | `deleteUserApiKeys` | Deletes up to 50 of the authenticated user's personal API keys by id in a single request. Only available when connected with a personal (user) API key. |
| Execute SQL Query | `executeSqlQuery` | Executes a single SQL query with positional parameters against a PostgreSQL branch through the Xata serverless gateway at https://{branchId}.{region}.xata.tech/sql. The gateway authenticates with the branch's PostgreSQL connection string (from Get Branch Credentials) sent in the Connection-String header; the control-plane API key is not accepted there. |
| Get Backup | `getBackup` | Returns a project backup by id with its branch and restore window. |
| Get Billing Customer | `getBillingCustomer` | Returns the billing customer details of an organization: billing email, collection method, payment method status and credit balances. |
| Get Branch | `getBranch` | Returns a branch's details: status and lifecycle of its database cluster, instances, region, scale-to-zero, backup and cluster configuration. |
| Get Branch Credentials | `getBranchCredentials` | Returns the PostgreSQL credentials of a branch (username, password, host, port, database name and a full connection string), optionally for a specific database username. |
| Get Branch Logs | `getBranchLogs` | Returns PostgreSQL log entries of a branch's instances over a time window, with optional filters on instance, level, process or message body and cursor pagination. |
| Get Branch Metrics | `getBranchMetrics` | Returns time-series data for one or more metrics of a branch (for example CPU, memory, storage or connections) over a time window, aggregated as avg, max or min per instance. |
| Get Branch PostgreSQL Configuration | `getBranchPostgresConfig` | Returns the PostgreSQL configuration parameters of a branch with their type, description, acceptable range, default and current value, and whether a restart is needed to change them. |
| Get GitHub Repository Mapping | `getGithubRepositoryMapping` | Returns the GitHub repository mapped to a branch for the Xata GitHub App preview-branch workflow. |
| Get Organization | `getOrganization` | Returns an organization's details by id, including its name, enabled/disabled status, billing status and usage tier. |
| Get Organization Invitation | `getOrganizationInvitation` | Returns the details of a single organization invitation by id. |
| Get Organization Limits | `getOrganizationLimits` | Returns the effective organization-level resource limits: maximum projects and branches, branch creation rate limits, instance counts and sizes, and storage per branch. |
| Get Organization Membership Limits | `getOrganizationMembershipLimits` | Returns the maximum number of members and pending invitations allowed in an organization. |
| Get Organization SSO Configuration | `getOrganizationSso` | Returns the organization's SSO configuration: the registered identity providers and the email domains claimed for them (verified and pending). Client secrets are never returned. |
| Get Project | `getProject` | Returns a project's details by id, including its configuration. |
| Get Project Limits | `getProjectLimits` | Returns the effective resource limits for a project, merging organization-level limits with project-specific overrides. |
| Get Upcoming Billing Invoice | `getUpcomingBillingInvoice` | Returns the upcoming invoice for an organization's active subscription, with amount due, subtotal, total, target date and hosted invoice URL. |
| List Backups | `listBackups` | Lists the backups of a project with the branch each belongs to and the earliest and latest points in time available for restore. |
| List Billing Invoices | `listBillingInvoices` | Lists an organization's billing invoices with their number, amount due, status and PDF link, using cursor pagination. |
| List Branches | `listBranches` | Lists the branches of a project with their region, parent branch, public access and backup support. |
| List Extensions | `listExtensions` | Lists the PostgreSQL extensions, plugins and modules available for a given image in an organization, optionally for a specific region. |
| List GitHub App Installations | `listGithubAppInstallations` | Lists the Xata GitHub App installations associated with an organization. |
| List Images | `listImages` | Lists the PostgreSQL images (versions) available to an organization, optionally for a specific region. |
| List Instance Types | `listInstanceTypes` | Lists the instance types available to an organization in a region, with vCPUs, memory and hourly and storage pricing. |
| List Organization API Keys | `listOrganizationApiKeys` | Lists the API keys of an organization with their preview, scopes, project and branch restrictions, expiry and last-used time. Key tokens are never returned here. |
| List Organization Invitations | `listOrganizationInvitations` | Lists an organization's invitations with optional filtering by status, email, first or last name, free-text search and offset pagination. |
| List Organization Members | `listOrganizationMembers` | Lists the members of an organization with their user id, name, email and role. |
| List Organization Roles | `listOrganizationRoles` | Lists the predefined roles (admin, editor, viewer) that can be assigned to members of an organization. Returns 404 for organizations where roles are not enabled. |
| List Organizations | `listOrganizations` | Returns every organization the authenticated user or API key belongs to, with each organization's id, name and billing status. |
| List Projects | `listProjects` | Lists the projects in an organization that the caller can access, with their scale-to-zero and IP filtering configuration. |
| List Regions | `listRegions` | Lists the regions where new branches can be deployed for an organization, with their cloud provider, public access and backup support. |
| List User API Keys | `listUserApiKeys` | Lists the personal API keys of the authenticated user. Only available when connected with a personal (user) API key, not an organization key. |
| Remove Organization Member | `removeOrganizationMember` | Removes a member from an organization by user id. An organization always keeps at least one admin. |
| Request Organization Deletion | `requestOrganizationDeletion` | Flags an organization for deletion. Rejected while the organization still has active projects. The subscription is cancelled immediately and deletion completes asynchronously after a grace period. This cannot be undone. |
| Resend Organization Invitation | `resendOrganizationInvitation` | Resends a pending invitation email with a fresh expiration time. This delivers mail to a real person; use with care. |
| Restore Branch From Backup | `restoreBranchFromBackup` | Creates a new branch from a backup of an existing source branch, optionally with its own scale-to-zero, backup and cluster configuration. |
| Rotate Branch Credentials | `rotateBranchCredentials` | Rotates the password of a branch database user. Clients using the old credentials stop working; fetch the new ones with Get Branch Credentials. |
| Send MCP Request | `sendMcpRequest` | Sends a single JSON-RPC 2.0 message to Xata's stateless MCP server (Streamable HTTP transport), for example initialize, tools/list or tools/call, and returns the JSON-RPC response. |
| Set Organization Member Role | `setOrganizationMemberRole` | Replaces the role of an organization member. An organization always retains at least one admin. |
| Set SSO Provider Enforcement | `setSsoProviderEnforcement` | Enables or disables enforcement for an identity provider. When enabled, every member on the provider's domain must sign in through it. Refused with 409 until the domain is verified. |
| Update Billing Customer | `updateBillingCustomer` | Updates an organization's billing customer details, such as the billing email address. |
| Update Branch | `updateBranch` | Updates a branch: rename or describe it, change replicas, storage, instance type or image, set backup and scale-to-zero settings, hibernate or wake it, or change PostgreSQL parameters and preload libraries. Only the fields sent are changed. |
| Update GitHub App Installation | `updateGithubAppInstallation` | Updates an existing GitHub App installation record with a new GitHub installation id. |
| Update GitHub Repository Mapping | `updateGithubRepositoryMapping` | Changes the GitHub repository mapped to a branch. |
| Update Organization | `updateOrganization` | Updates an organization's details, such as its name. |
| Update Project | `updateProject` | Updates a project's name or configuration (scale-to-zero defaults, IP filtering). Only the fields sent are changed. |
| Update SSO Provider | `updateSsoProvider` | Replaces an identity provider's credentials (and re-discovers OIDC endpoints from the issuer). The domain and enforcement setting are carried over unchanged. |
| Verify SSO Domain | `verifySsoDomain` | Looks up the DNS challenge TXT record for a claimed SSO domain. A missing or stale record is reported as verified false on a 200 so the check can be retried while DNS propagates. |

</details>
