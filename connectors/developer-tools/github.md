---
description: "GitHub REST API v3 connector — repositories, contents, branches/commits/git-data, issues & comments & labels & milestones, pull requests & reviews, releases,…"
hidden: true
---

# GitHub

<img src="../../.gitbook/assets/connectors/lg/github.png" alt="GitHub logo">

GitHub REST API v3 connector — repositories, contents, branches/commits/git-data, issues & comments & labels & milestones, pull requests & reviews, releases, users & orgs & teams, Actions (workflows/runs), search, and repository webhooks. OAuth 2.0.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [github.com](https://github.com) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Slug** | `github` |

## Use it

Add GitHub from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.github.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Enterprise OIDC Repo Property | `addEnterpriseOidcRepoProperty` | Adds a repository custom property to the OIDC subject claim customization for an enterprise. |
| Add Enterprise Runner Labels | `addEnterpriseRunnerLabels` | Adds custom labels to a self-hosted runner configured in an enterprise. |
| Add Enterprise Team Member | `addEnterpriseTeamMembership` | Adds (or updates) a single user's membership in an enterprise team via PUT. Returns the membership. |
| Add Enterprise Team Members (Bulk) | `addEnterpriseTeamMemberships` | Bulk-adds members to an enterprise team by username. |
| Add Enterprise Team Organization | `addEnterpriseTeamOrganization` | Connects a single organization to an enterprise team via PUT. Returns the connected organization. |
| Add Enterprise Team Organizations (Bulk) | `addEnterpriseTeamOrganizations` | Bulk-connects organizations to an enterprise team by organization slug. |
| Add Labels to Issue | `addLabels` | Add labels to an issue. The labels are appended to any existing labels. Returns the full array of labels on the issue. |
| Add Organization Access To Enterprise Runner Group | `addEnterpriseRunnerGroupOrg` | Adds an organization to the list of organizations that have access to a self-hosted runner group in an enterprise. Returns 204 No Content. |
| Add Repositories To Enterprise Org App Installation | `addEnterpriseOrgAppInstallationRepositories` | Add repositories to an app installation's selected-repository set in an org. Pass a pre-stringified JSON body of the form {"repositories":["repo-a","repo-b"]}. |
| Add Runner To Enterprise Runner Group | `addEnterpriseRunnerGroupRunner` | Adds a self-hosted runner to a runner group for an enterprise. Returns 204 No Content. |

<details>

<summary>See 243 more actions</summary>

* **Add Teams To Enterprise Copilot Subscription** `addEnterpriseCopilotTeams`: Adds enterprise teams to the Copilot subscription for an enterprise.
* **Add Users To Enterprise Copilot Subscription** `addEnterpriseCopilotUsers`: Adds users to the Copilot subscription for an enterprise.
* **Assign Enterprise Role To Team** `assignEnterpriseRoleToTeam`: Assign a specific enterprise role to a team. Returns 204 No Content.
* **Assign Enterprise Role To User** `assignEnterpriseRoleToUser`: Assign a specific enterprise role to a user. Returns 204 No Content.
* **Attach Enterprise Code Security Configuration** `attachEnterpriseCodeSecurityConfiguration`: Attaches an enterprise code security configuration to repositories. Returns 202 Accepted.
* **Create Branch** `createBranch`: Creates a new branch in a repository, pointing at the given commit SHA (GitHub git refs API, POST /repos/{owner}/{repo}/git/refs with ref refs/heads/&lt;branch&gt;). To branch from an existing branch, first call Get Branch on it and pass its commit.sha. Returns the new reference (ref, node_id, url, object.sha). Fails with 422 "Reference already exists" if the branch name is taken.
* **Create Enterprise Audit Log Stream** `createEnterpriseAuditLogStream`: Create an audit log streaming endpoint for an enterprise. Pass a pre-stringified JSON body with: enabled (boolean), stream_type (e.g. Azure Blob Storage, Splunk, Amazon S3, Google Cloud Storage, Datadog), vendor_specific (provider-specific config object).
* **Create Enterprise Budget** `createEnterpriseBudget`: Creates a budget for an enterprise.
* **Create Enterprise Code Security Configuration** `createEnterpriseCodeSecurityConfiguration`: Creates a code security configuration in an enterprise.
* **Create Enterprise Hosted Runner** `createEnterpriseHostedRunner`: Creates a GitHub-hosted runner for an enterprise.
* **Create Enterprise Network Configuration** `createEnterpriseNetworkConfiguration`: Creates a hosted compute network configuration for an enterprise.
* **Create Enterprise Org App Installation** `createEnterpriseOrgAppInstallation`: Install a GitHub App (owned by the enterprise) into an organization. Pass a pre-stringified JSON body with: client_id (required), repository_selection (all|selected, optional), repositories (optional array of repo names when selected).
* **Create Enterprise Ruleset** `createEnterpriseRuleset`: Create a repository ruleset that applies across an enterprise. Pass a pre-stringified JSON body with: name (required), enforcement (active|evaluate|disabled, required), target (optional), conditions (optional object), rules (optional array), bypass_actors (optional array).
* **Create Enterprise Runner Registration Token** `createEnterpriseRunnerRegistrationToken`: Returns a token to register a self-hosted runner with an enterprise.
* **Create Enterprise Runner Remove Token** `createEnterpriseRunnerRemoveToken`: Returns a token to remove a self-hosted runner from an enterprise.
* **Create Enterprise Self-Hosted Runner Group** `createEnterpriseRunnerGroup`: Creates a new self-hosted runner group for an enterprise. Returns the created runner group object.
* **Create Enterprise Team** `createEnterpriseTeam`: Creates a new enterprise team. Optionally maps the team to an IdP group (group_id) and controls organization sync. Returns the created team.
* **Create Issue** `createIssue`: Create a new issue in a repository. Requires a title. Returns the created issue object (201).
* **Create Issue Comment** `createIssueComment`: Create a comment on an issue. Requires the comment body. Returns the created comment object (201).
* **Create Label** `createLabel`: Create a label in a repository. Requires a name. Returns the created label object (201).
* **Create Milestone** `createMilestone`: Create a milestone in a repository. Requires a title. Returns the created milestone object (201).
* **Create or Update File Contents** `createOrUpdateFile`: Create a new file or replace an existing file in a repository. Content must be Base64-encoded. To update an existing file you must supply its current blob sha. PUT /repos/{owner}/{repo}/contents/{path}.
* **Create Organization Repository** `createOrgRepo`: Creates a new repository in the specified organization. BLOCKED (provider account-state): authenticated user belongs to no organization (listUserOrgs returned []), so an org repo cannot be created anywhere. Executing against public org 'github' returns 403 'You need admin access to the organization before adding a repository to it.' configHealthy:true (auth resolved, URL routed). Wiring is correct (POST /orgs/{org}/repos, field-by-field bodyTemplate). Returns the full repository object (201) on success when admin access exists.
* **Create Pull Request** `createPull`: Create a new pull request. Provide title (or issue), head and base branches, optional body, draft and maintainer_can_modify flags. Returns the created pull request object (201).
* **Create Pull Request Review** `createReview`: Create a review on a pull request. Optionally specify commit_id, body, event (APPROVE/REQUEST_CHANGES/COMMENT, omit for PENDING) and inline comments. Returns the created review object.
* **Create Release** `createRelease`: Create a release for a repository. Users with push access can create a release. Requires tag_name. Returns the created release object (201).
* **Create Repo Webhook** `createRepoWebhook`: Create a repository webhook. Used by the webhook subscription code to register a webhook that delivers issue events to a fastn callback URL. Returns the created hook object (201).
* **Create Repository For Authenticated User** `createUserRepo`: Creates a new repository for the authenticated user. Returns the full repository object (201).
* **Create SCIM Group (Enterprise)** `createScimGroup`: Provisions a new SCIM group in an enterprise. Returns the created SCIM group resource.
* **Create SCIM User (Enterprise)** `createScimUser`: Provisions a new SCIM user in an enterprise. Returns the created SCIM user resource.
* **Delete Enterprise Audit Log Stream** `deleteEnterpriseAuditLogStream`: Delete an audit log streaming endpoint by id. Returns 204 No Content.
* **Delete Enterprise Budget** `deleteEnterpriseBudget`: Deletes a budget configured for an enterprise. Returns 204 No Content.
* **Delete Enterprise Code Security Configuration** `deleteEnterpriseCodeSecurityConfiguration`: Deletes a code security configuration from an enterprise. Returns 204 No Content.
* **Delete Enterprise Custom Property** `deleteEnterpriseCustomProperty`: Delete a custom property definition from an enterprise by name. Returns 204 No Content.
* **Delete Enterprise Hosted Runner** `deleteEnterpriseHostedRunner`: Deletes a GitHub-hosted runner for an enterprise.
* **Delete Enterprise Hosted Runner Custom Image** `deleteEnterpriseHostedRunnerCustomImage`: Deletes a custom image and all its versions for GitHub-hosted runners in an enterprise.
* **Delete Enterprise Hosted Runner Custom Image Version** `deleteEnterpriseHostedRunnerCustomImageVersion`: Deletes a specific version of a custom image for GitHub-hosted runners in an enterprise.
* **Delete Enterprise Network Configuration** `deleteEnterpriseNetworkConfiguration`: Deletes a hosted compute network configuration from an enterprise. Returns 204 No Content.
* **Delete Enterprise OIDC Repo Property** `deleteEnterpriseOidcRepoProperty`: Removes a repository custom property from the OIDC subject claim customization for an enterprise.
* **Delete Enterprise Org App Installation** `deleteEnterpriseOrgAppInstallation`: Uninstall a GitHub App from an organization managed by the enterprise. Returns 204 No Content.
* **Delete Enterprise Ruleset** `deleteEnterpriseRuleset`: Delete an enterprise repository ruleset by id. Returns 204 No Content.
* **Delete Enterprise Runner** `deleteEnterpriseRunner`: Forces the removal of a self-hosted runner from an enterprise.
* **Delete Enterprise Self-Hosted Runner Group** `deleteEnterpriseRunnerGroup`: Deletes a self-hosted runner group for an enterprise. Returns 204 No Content.
* **Delete Enterprise Team** `deleteEnterpriseTeam`: Deletes an enterprise team by its team slug. Returns 204 No Content.
* **Delete File** `deleteFile`: Delete a file in a repository. Requires the blob sha of the file being deleted. DELETE /repos/{owner}/{repo}/contents/{path}.
* **Delete Release** `deleteRelease`: Delete a release identified by release_id. Users with push access can delete a release. Returns 204 No Content.
* **Delete Repo Webhook** `deleteRepoWebhook`: Delete a repository webhook by its id. Used by the webhook unsubscription code. Returns 204 No Content.
* **Delete Repository** `deleteRepo`: Deletes a repository. Requires admin access. Returns 204 No Content on success. BLOCKED (provider auth-scope gating): the OAuth token lacks the 'delete_repo' scope. Executed against two repos the authenticated user (sarmadnawaz) demonstrably OWNS — fastn-verify-uog-1780668 and fastn-verify-gh — both return 403 'Must have admin rights to Repository.' configHealthy:true (auth resolved, URL routed correctly via url=host + path=/repos/{owner}/{repo}; no doubled-URL defect). Since ownership is confirmed, the 403 is not an admin-rights gap but the missing delete_repo OAuth scope; re-grant that scope to obtain 204. Leftover scratch repos remain (could not be cleaned up due to this scope gap).
* **Delete SCIM Group (Enterprise)** `deleteScimGroup`: Deprovisions (deletes) a SCIM group in an enterprise. Returns 204 No Content.
* **Delete SCIM User (Enterprise)** `deleteScimUser`: Deprovisions (deletes) a SCIM user in an enterprise. Returns 204 No Content.
* **Disable Enterprise Access Restrictions** `disableEnterpriseAccessRestrictions`: Disable IP allow list / access restrictions for an enterprise. Returns 204 No Content.
* **Disable Selected Organization For Enterprise Actions** `disableEnterprisePermissionsOrg`: Removes an organization from the list of selected organizations that are enabled for GitHub Actions in an enterprise. Returns 204 No Content.
* **Dispatch Workflow** `dispatchWorkflow`: Manually trigger a GitHub Actions workflow run (workflow_dispatch event). The workflow must define an on.workflow_dispatch trigger. Returns 204 No Content on success.
* **Enable Enterprise Access Restrictions** `enableEnterpriseAccessRestrictions`: Enable IP allow list / access restrictions for an enterprise. Returns 204 No Content.
* **Enable Selected Organization For Enterprise Actions** `enableEnterprisePermissionsOrg`: Adds an organization to the list of selected organizations that are enabled for GitHub Actions in an enterprise. Returns 204 No Content.
* **Generate Enterprise Runner JIT Config** `generateEnterpriseRunnerJitConfig`: Generate a just-in-time configuration for a new enterprise self-hosted runner.
* **Get Allowed Actions For Enterprise** `getEnterpriseAllowedActions`: Gets the selected actions and reusable workflows that are allowed in an enterprise. Only applicable when allowed_actions is set to selected.
* **Get Authenticated User** `getAuthenticatedUser`: Get the profile of the user associated with the access token. Returns extended fields like plan, total_private_repos, and collaborators for the authenticated account.
* **Get Branch** `getBranch`: Gets a single branch for the given repository. Returns the branch object with commit and protection details.
* **Get Commit** `getCommit`: Gets a single commit by SHA, branch name, or tag. Returns the commit object with stats and files.
* **Get Default Enterprise Code Security Configurations** `getEnterpriseCodeSecurityDefaultConfigurations`: Lists the default code security configurations for an enterprise.
* **Get Enterprise Actions Permissions** `getEnterpriseActionsPermissions`: Gets the GitHub Actions permissions policy for organizations and allowed actions in an enterprise. Returns enabled_organizations and allowed_actions.
* **Get Enterprise Advanced Security Billing** `getEnterpriseAdvancedSecurityBilling`: Get GitHub Advanced Security active committer usage and billing for an enterprise. Optional query: advanced_security_product (e.g. code_security, secret_protection).
* **Get Enterprise AI Credit Usage** `getEnterpriseAiCreditUsage`: Gets the AI credit usage report for an enterprise.
* **Get Enterprise Announcement** `getEnterpriseAnnouncement`: Get the global announcement banner configured for an enterprise.
* **Get Enterprise Artifact And Log Retention Settings** `getEnterpriseArtifactRetention`: Gets the artifact and log retention period settings for an enterprise.
* **Get Enterprise Audit Log** `getEnterpriseAuditLog`: List audit log events for an enterprise. Optional query filters: phrase (search), include (web/git/all), after, before (cursor), order (asc/desc), page, per_page.
* **Get Enterprise Audit Log Stream** `getEnterpriseAuditLogStream`: Get a single audit log streaming endpoint configuration by its id.
* **Get Enterprise Audit Log Stream Key** `getEnterpriseAuditLogStreamKey`: Get the public encryption key used to set up an enterprise audit log streaming endpoint.
* **Get Enterprise Billing Usage Report** `getEnterpriseBillingUsage`: Gets a report of the metered usage for an enterprise.
* **Get Enterprise Billing Usage Summary** `getEnterpriseBillingUsageSummary`: Gets a summary of the metered usage for an enterprise.
* **Get Enterprise Budget** `getEnterpriseBudget`: Gets a specific budget configured for an enterprise.
* **Get Enterprise Cache Retention Limit** `getEnterpriseCacheRetentionLimit`: Gets the GitHub Actions cache retention limit policy for an enterprise.
* **Get Enterprise Cache Storage Limit** `getEnterpriseCacheStorageLimit`: Gets the GitHub Actions cache storage limit policy for an enterprise.
* **Get Enterprise Cache Usage** `getEnterpriseCacheUsage`: Gets the total GitHub Actions cache usage for an enterprise.
* **Get Enterprise Code Security And Analysis** `getEnterpriseCodeSecurityAnalysis`: Get the enterprise-wide code security and analysis settings (Advanced Security, secret scanning, push protection, Dependabot, etc.).
* **Get Enterprise Code Security Configuration** `getEnterpriseCodeSecurityConfiguration`: Gets a code security configuration available in an enterprise.
* **Get Enterprise Consumed Licenses** `getEnterpriseConsumedLicenses`: List GitHub Enterprise license seats consumed across the enterprise. Optional query: page, per_page.
* **Get Enterprise Copilot Metrics Report (1 Day)** `getEnterpriseCopilotMetricsReport1Day`: Gets the daily Copilot metrics report for an enterprise for a given day.
* **Get Enterprise Copilot User Teams Metrics Report (1 Day)** `getEnterpriseCopilotUserTeamsMetricsReport1Day`: Gets the daily Copilot metrics report broken down by user teams for an enterprise.
* **Get Enterprise Copilot Users Metrics Report (1 Day)** `getEnterpriseCopilotUsersMetricsReport1Day`: Gets the daily Copilot metrics report broken down by user for an enterprise.
* **Get Enterprise Custom Properties Schema** `getEnterpriseCustomPropertiesSchema`: List all custom property definitions configured for an enterprise.
* **Get Enterprise Custom Property** `getEnterpriseCustomProperty`: Get a single custom property definition for an enterprise by name.
* **Get Enterprise Default Workflow Permissions** `getEnterpriseWorkflowPermissions`: Gets the default workflow permissions granted to the GITHUB_TOKEN when running workflows in an enterprise, and whether GitHub Actions can approve pull requests.
* **Get Enterprise Fork PR Contributor Approval Policy** `getEnterpriseForkPrContributorApproval`: Gets the fork pull request contributor approval policy for an enterprise.
* **Get Enterprise Fork PR Workflows In Private Repos** `getEnterpriseForkPrPrivateRepos`: Gets whether workflows triggered by pull requests from forks are allowed to run on private repositories in an enterprise, and related token/secret settings.
* **Get Enterprise Hosted Runner** `getEnterpriseHostedRunner`: Gets a GitHub-hosted runner configured in an enterprise.
* **Get Enterprise Hosted Runner Custom Image** `getEnterpriseHostedRunnerCustomImage`: Gets a specific custom image available for GitHub-hosted runners in an enterprise.
* **Get Enterprise Hosted Runner Custom Image Version** `getEnterpriseHostedRunnerCustomImageVersion`: Gets a specific version of a custom image available to GitHub-hosted runners in an enterprise.
* **Get Enterprise Hosted Runner Limits** `getEnterpriseHostedRunnerLimits`: Gets the GitHub-hosted runner limits for an enterprise.
* **Get Enterprise License Sync Status** `getEnterpriseLicenseSyncStatus`: Get the license sync status between GitHub Enterprise Cloud and connected GitHub Enterprise Server instances.
* **Get Enterprise Member Copilot Details** `getEnterpriseMemberCopilotDetails`: Gets the Copilot seat assignment details for a member of an enterprise.
* **Get Enterprise Network Configuration** `getEnterpriseNetworkConfiguration`: Gets a hosted compute network configuration for an enterprise.
* **Get Enterprise Network Settings** `getEnterpriseNetworkSettings`: Gets a hosted compute network settings resource for an enterprise.
* **Get Enterprise OIDC Repo Properties** `getEnterpriseOidcRepoProperties`: Gets the customization template for OIDC subject claim repository properties for an enterprise.
* **Get Enterprise Premium Request Usage** `getEnterprisePremiumRequestUsage`: Gets the premium request usage report for an enterprise.
* **Get Enterprise Role** `getEnterpriseRole`: Get a single enterprise role by id, including its permissions.
* **Get Enterprise Ruleset** `getEnterpriseRuleset`: Get a single enterprise repository ruleset by id.
* **Get Enterprise Ruleset Version** `getEnterpriseRulesetVersion`: Get a specific historical version of an enterprise repository ruleset.
* **Get Enterprise Runner** `getEnterpriseRunner`: Gets a specific self-hosted runner configured in an enterprise.
* **Get Enterprise Self-Hosted Runner Group** `getEnterpriseRunnerGroup`: Gets a single self-hosted runner group for an enterprise by ID.
* **Get Enterprise Self-Hosted Runners Settings** `getEnterpriseSelfHostedRunnersSettings`: Gets the settings for whether self-hosted runners are disabled for all organizations in an enterprise.
* **Get Enterprise Team** `getEnterpriseTeam`: Fetches a single enterprise team by its team slug.
* **Get Enterprise Team Membership** `getEnterpriseTeamMembership`: Gets the membership of a single user in an enterprise team.
* **Get Enterprise Team Organization** `getEnterpriseTeamOrganization`: Gets the connection of a single organization to an enterprise team.
* **Get Issue** `getIssue`: Get a single issue by its number in a repository. Returns the full issue object.
* **Get Latest Enterprise Copilot Metrics Report (28 Day)** `getEnterpriseCopilotMetricsReport28DayLatest`: Gets the latest 28-day Copilot metrics report for an enterprise.
* **Get Latest Enterprise Copilot Users Metrics Report (28 Day)** `getEnterpriseCopilotUsersMetricsReport28DayLatest`: Gets the latest 28-day Copilot metrics report broken down by user for an enterprise.
* **Get Latest Release** `getLatestRelease`: Get the latest published full release for the repository. The latest release is the most recent non-prerelease, non-draft release, sorted by created_at. Returns a release object.
* **Get Organization** `getOrg`: Get detailed information about a single organization by its login. Some fields require the authenticated user to be an organization owner.
* **Get Pull Request** `getPull`: Get a single pull request by number. Returns the full pull request object including merge status, mergeable state and statistics.
* **Get Release** `getRelease`: Get a single release by its unique release_id. Returns a release object.
* **Get Repo Webhook** `getRepoWebhook`: Get a single repository webhook by its id. Returns the hook object.
* **Get Repository** `getRepo`: Gets a single repository by owner and repo name. Returns the full repository object.
* **Get Repository Content** `getContent`: Get the contents of a file or directory in a repository. Returns file content (Base64-encoded), a directory listing (array), a symlink, or a submodule depending on the path. GET /repos/{owner}/{repo}/contents/{path}.
* **Get Repository README** `getReadme`: Get the preferred README for a repository. Returns the README file content (Base64-encoded). GET /repos/{owner}/{repo}/readme.
* **Get SCIM Group (Enterprise)** `getScimGroup`: Fetches a single provisioned SCIM group in an enterprise by its SCIM group id.
* **Get SCIM User (Enterprise)** `getScimUser`: Fetches a single provisioned SCIM user in an enterprise by its SCIM user id.
* **Get User** `getUser`: Get publicly available information about a GitHub user by username.
* **Get Workflow Run** `getWorkflowRun`: Get a specific GitHub Actions workflow run by its run_id. Returns the full workflow run object.
* **List Branches** `listBranches`: Lists branches for the given repository. Returns an array of branch objects.
* **List Collaborators** `listCollaborators`: Lists collaborators for the given repository. Returns an array of collaborator objects with permissions.
* **List Commits** `listCommits`: Lists commits for the given repository. Returns an array of commit objects.
* **List Deployment Statuses** `listDeploymentStatuses`: List statuses for a deployment (GET /repos/{owner}/{repo}/deployments/{deployment_id}/statuses). Returns the deployment's statuses, most recent first, with pagination. Requires repo or repo_deployment scope.
* **List Deployments** `listDeployments`: List deployments for a repository (GET /repos/{owner}/{repo}/deployments). Returns deployments, most recent first. Supports filtering by sha, ref, task, and environment, with pagination.
* **List Enterprise Audit Log Streams** `listEnterpriseAuditLogStreams`: List the configured audit log streaming endpoints for an enterprise.
* **List Enterprise Budget User States** `listEnterpriseBudgetUserStates`: Lists the per-user states for a specific enterprise budget.
* **List Enterprise Budgets** `listEnterpriseBudgets`: Lists the budgets configured for an enterprise.
* **List Enterprise Code Scanning Alerts** `listEnterpriseCodeScanningAlerts`: Lists code scanning alerts for the default branch for all eligible repositories in an enterprise.
* **List Enterprise Code Security Configurations** `listEnterpriseCodeSecurityConfigurations`: Lists all code security configurations available in an enterprise.
* **List Enterprise Copilot Seats** `listEnterpriseCopilotSeats`: Lists all Copilot seat assignments for an enterprise.
* **List Enterprise Dependabot Alerts** `listEnterpriseDependabotAlerts`: Lists Dependabot alerts for repositories that are part of an enterprise.
* **List Enterprise Hosted Runner Custom Image Versions** `listEnterpriseHostedRunnerCustomImageVersions`: Gets the list of versions for a custom image available to GitHub-hosted runners in an enterprise.
* **List Enterprise Hosted Runner Custom Images** `listEnterpriseHostedRunnerCustomImages`: Gets the list of custom images available for GitHub-hosted runners in an enterprise.
* **List Enterprise Hosted Runner GitHub-Owned Images** `listEnterpriseHostedRunnerGithubOwnedImages`: Gets the list of GitHub-owned images available for GitHub-hosted runners in an enterprise.
* **List Enterprise Hosted Runner Machine Sizes** `listEnterpriseHostedRunnerMachineSizes`: Gets the list of machine specs available for GitHub-hosted runners in an enterprise.
* **List Enterprise Hosted Runner Partner Images** `listEnterpriseHostedRunnerPartnerImages`: Gets the list of partner images available for GitHub-hosted runners in an enterprise.
* **List Enterprise Hosted Runner Platforms** `listEnterpriseHostedRunnerPlatforms`: Gets the list of platforms available for GitHub-hosted runners in an enterprise.
* **List Enterprise Hosted Runners** `listEnterpriseHostedRunners`: Lists all GitHub-hosted runners configured in an enterprise.
* **List Enterprise Installable Org Accessible Repositories** `listEnterpriseInstallableOrgRepositories`: List repositories in an organization that a GitHub App can be granted access to during installation. Optional query: page, per_page.
* **List Enterprise Installable Organizations** `listEnterpriseInstallableOrganizations`: List organizations in an enterprise where a GitHub App owned by the enterprise can be installed. Optional query: page, per_page.
* **List Enterprise Network Configurations** `listEnterpriseNetworkConfigurations`: Lists all hosted compute network configurations for an enterprise.
* **List Enterprise Org App Installation Repositories** `listEnterpriseOrgAppInstallationRepositories`: List repositories an app installation in an org can access. Optional query: page, per_page.
* **List Enterprise Org App Installations** `listEnterpriseOrgAppInstallations`: List GitHub App installations in an organization managed by the enterprise. Optional query: page, per_page.
* **List Enterprise Push Rule Bypass Requests** `listEnterprisePushRuleBypassRequests`: Lists push rule bypass requests within an enterprise.
* **List Enterprise Roles** `listEnterpriseRoles`: List all custom and built-in enterprise roles for an enterprise.
* **List Enterprise Ruleset History** `listEnterpriseRulesetHistory`: List the version history of an enterprise repository ruleset. Optional query: page, per_page.
* **List Enterprise Runner Downloads** `listEnterpriseRunnerDownloads`: List binaries for the runner application that you can download and run on an enterprise.
* **List Enterprise Runner Labels** `listEnterpriseRunnerLabels`: Lists all labels for a self-hosted runner configured in an enterprise.
* **List Enterprise Runners** `listEnterpriseRunners`: List all self-hosted runners configured for an enterprise.
* **List Enterprise Secret Scanning Alerts** `listEnterpriseSecretScanningAlerts`: Lists secret scanning alerts for eligible repositories in an enterprise.
* **List Enterprise Secret Scanning Bypass Requests** `listEnterpriseSecretScanningBypassRequests`: Lists secret scanning push protection bypass requests within an enterprise.
* **List Enterprise Self-Hosted Runner Groups** `listEnterpriseRunnerGroups`: Lists all self-hosted runner groups for an enterprise. Supports filtering to groups visible to a specific organization and pagination.
* **List Enterprise Team Memberships** `listEnterpriseTeamMemberships`: Lists the members of an enterprise team. Supports pagination (per_page, page).
* **List Enterprise Team Organizations** `listEnterpriseTeamOrganizations`: Lists the organizations connected to an enterprise team. Supports pagination (per_page, page).
* **List Enterprise Teams** `listEnterpriseTeams`: Lists all enterprise teams for an enterprise. Supports pagination (per_page, page).
* **List Issue Comments** `listIssueComments`: List comments on an issue. Returns a top-level JSON array of comment objects.
* **List Issue Timeline** `listIssueTimeline`: List timeline events for an issue (GET /repos/{owner}/{repo}/issues/{issue_number}/timeline). Returns the chronological event stream for an issue (labeled, assigned, commented, cross-referenced, closed, etc.), with pagination.
* **List Issues** `listIssues`: List issues in a repository. Returns a top-level JSON array of issue objects. Supports filtering by milestone, state, assignee, creator, mentioned, labels; sorting and pagination.
* **List Labels** `listLabels`: List all labels for a repository. Returns a top-level JSON array of label objects.
* **List Milestones** `listMilestones`: List milestones for a repository. Returns a top-level JSON array of milestone objects.
* **List Organization Access To Enterprise Runner Group** `listEnterpriseRunnerGroupOrgs`: Lists the organizations with access to a self-hosted runner group in an enterprise.
* **List Organization Members** `listOrgMembers`: List all users who are members of an organization. Supports filtering by 2FA status and role, plus pagination. Response is a top-level JSON array.
* **List Organization Repositories** `listOrgRepos`: Lists repositories for the specified organization. Returns an array of minimal repository objects.
* **List Organization Teams** `listOrgTeams`: List all teams in an organization. BLOCKED (provider account-state): authenticated user belongs to no organization (listUserOrgs returned []); executing against public org 'github' returns 403 'Must have admin rights to Repository'. Requires org admin/membership which is not constructible for this account. Wiring is correct (GET /orgs/{org}/teams, auth header present). Response is a top-level JSON array.
* **List Pull Request Files** `listPullFiles`: List the files changed in a pull request. Returns a JSON array of file objects with status, additions, deletions and patch. Up to 3000 files, paginated.
* **List Pull Request Reviews** `listReviews`: List reviews for a pull request in chronological order. Returns a JSON array of review objects.
* **List Pull Requests** `listPulls`: List pull requests in a repository. Returns a JSON array of pull request objects. Supports filtering by state, head, base, sorting and pagination.
* **List Releases** `listReleases`: List releases for a repository. Returns a top-level JSON array of release objects, sorted by created_at descending. Supports pagination via page/per_page.
* **List Repo Webhooks** `listRepoWebhooks`: List repository webhooks. Returns a top-level JSON array of hook objects.
* **List Repositories For Enterprise Code Security Configuration** `listEnterpriseCodeSecurityConfigurationRepositories`: Lists the repositories associated with an enterprise code security configuration.
* **List Runners In Enterprise Runner Group** `listEnterpriseRunnerGroupRunners`: Lists the self-hosted runners that are in a runner group for an enterprise.
* **List SCIM Groups (Enterprise)** `listScimGroups`: Lists provisioned SCIM groups for an enterprise. Supports pagination (startIndex, count) and SCIM filter. Returns a SCIM ListResponse.
* **List SCIM Users (Enterprise)** `listScimUsers`: Lists provisioned SCIM users for an enterprise. Supports pagination (startIndex, count) and SCIM filter. Returns a SCIM ListResponse.
* **List Selected Organizations Enabled For Enterprise Actions** `listEnterprisePermissionsOrgs`: Lists the organizations that are selected to be enabled for GitHub Actions in an enterprise. Only applicable when enabled_organizations is set to selected.
* **List Tags** `listTags`: Lists tags for the given repository. Returns an array of tag objects.
* **List Teams Assigned To Enterprise Role** `listEnterpriseRoleTeams`: List all teams assigned a given enterprise role.
* **List User Organizations** `listUserOrgs`: List organizations for the authenticated user. Returns both public and private memberships. Supports pagination via page and per_page. Response is a top-level JSON array.
* **List User Repositories** `listUserRepos`: Lists repositories that the authenticated user has explicit permission to access. Returns an array of repository objects.
* **List Users Assigned To Enterprise Role** `listEnterpriseRoleUsers`: List all users assigned a given enterprise role.
* **List Workflow Runs** `listWorkflowRuns`: List all GitHub Actions workflow runs for a repository, optionally filtered by actor, branch, event, status, etc. Returns total_count and an array of workflow_runs.
* **List Workflows** `listWorkflows`: List all GitHub Actions workflows in a repository. Returns a total_count and an array of workflow objects.
* **Merge Pull Request** `mergePull`: Merge a pull request. Optionally set commit_title, commit_message, required head sha, and merge_method (merge/squash/rebase). Returns sha, merged and message.
* **Ping Repo Webhook** `pingRepoWebhook`: Trigger a ping event to be sent to the webhook. Returns 204 No Content.
* **Promote Enterprise Custom Property** `promoteEnterpriseCustomProperty`: Promote an organization-level custom property to the enterprise so it applies across all organizations. Returns 204 No Content.
* **Remove All Enterprise Roles From Team** `removeAllEnterpriseRolesFromTeam`: Remove all enterprise role assignments from a team. Returns 204 No Content.
* **Remove All Enterprise Roles From User** `removeAllEnterpriseRolesFromUser`: Remove all enterprise role assignments from a user. Returns 204 No Content.
* **Remove All Enterprise Runner Labels** `removeEnterpriseRunnerAllLabels`: Remove all custom labels from a self-hosted runner configured in an enterprise.
* **Remove Enterprise Announcement** `removeEnterpriseAnnouncement`: Remove the global announcement banner from an enterprise. Returns 204 No Content.
* **Remove Enterprise Role From Team** `removeEnterpriseRoleFromTeam`: Remove a specific enterprise role from a team. Returns 204 No Content.
* **Remove Enterprise Role From User** `removeEnterpriseRoleFromUser`: Remove a specific enterprise role from a user. Returns 204 No Content.
* **Remove Enterprise Runner Label** `removeEnterpriseRunnerLabel`: Remove a custom label from a self-hosted runner configured in an enterprise.
* **Remove Enterprise Team Member** `removeEnterpriseTeamMembership`: Removes a single user's membership from an enterprise team via DELETE. Returns 204 No Content.
* **Remove Enterprise Team Members (Bulk)** `removeEnterpriseTeamMemberships`: Bulk-removes members from an enterprise team by username.
* **Remove Enterprise Team Organization** `removeEnterpriseTeamOrganization`: Disconnects a single organization from an enterprise team via DELETE. Returns 204 No Content.
* **Remove Enterprise Team Organizations (Bulk)** `removeEnterpriseTeamOrganizations`: Bulk-disconnects organizations from an enterprise team by organization slug.
* **Remove Organization Access From Enterprise Runner Group** `removeEnterpriseRunnerGroupOrg`: Removes an organization from the list of organizations that have access to a self-hosted runner group in an enterprise. Returns 204 No Content.
* **Remove Repositories From Enterprise Org App Installation** `removeEnterpriseOrgAppInstallationRepositories`: Remove repositories from an app installation's selected-repository set in an org. Pass a pre-stringified JSON body of the form {"repositories":["repo-a","repo-b"]}.
* **Remove Runner From Enterprise Runner Group** `removeEnterpriseRunnerGroupRunner`: Removes a self-hosted runner from a runner group for an enterprise. The runner is not removed from the enterprise. Returns 204 No Content.
* **Remove Teams From Enterprise Copilot Subscription** `removeEnterpriseCopilotTeams`: Removes enterprise teams from the Copilot subscription for an enterprise.
* **Remove Users From Enterprise Copilot Subscription** `removeEnterpriseCopilotUsers`: Removes users from the Copilot subscription for an enterprise.
* **Replace SCIM Group (Enterprise)** `replaceScimGroup`: Replaces an existing SCIM group (full update via PUT) in an enterprise. Returns the updated group resource.
* **Replace SCIM User (Enterprise)** `replaceScimUser`: Replaces an existing SCIM user (full update via PUT) in an enterprise. Returns the updated user resource.
* **Search Code** `searchCode`: Search for file contents and file paths on GitHub. GET /search/code. Note: code search has a stricter rate limit (10 req/min) and only searches the default branch of indexed repositories.
* **Search Issues And Pull Requests** `searchIssues`: Search for issues and pull requests on GitHub using keywords and qualifiers. GET /search/issues.
* **Search Repositories** `searchRepos`: Search for repositories on GitHub using keywords and qualifiers. GET /search/repositories. Returns up to 1000 results, 100 per page.
* **Search Users** `searchUsers`: Search for users on GitHub using keywords and qualifiers. GET /search/users.
* **Set Allowed Actions For Enterprise** `setEnterpriseAllowedActions`: Sets the selected actions and reusable workflows that are allowed in an enterprise. Only applicable when allowed_actions is set to selected. Returns 204 No Content.
* **Set Default Enterprise Code Security Configuration** `setEnterpriseCodeSecurityDefaultConfiguration`: Sets a code security configuration as a default for an enterprise to be applied to new repositories.
* **Set Enterprise Actions Permissions** `setEnterpriseActionsPermissions`: Sets the GitHub Actions permissions policy for organizations and allowed actions in an enterprise. Returns 204 No Content.
* **Set Enterprise Announcement** `setEnterpriseAnnouncement`: Set or update the global announcement banner for an enterprise. Pass a pre-stringified JSON body with fields: announcement (required), expires_at (optional ISO8601), user_dismissible (optional boolean).
* **Set Enterprise Artifact And Log Retention Settings** `setEnterpriseArtifactRetention`: Sets the artifact and log retention period (in days) for an enterprise. Returns 204 No Content.
* **Set Enterprise Cache Retention Limit** `setEnterpriseCacheRetentionLimit`: Sets the GitHub Actions cache retention limit policy for an enterprise.
* **Set Enterprise Cache Storage Limit** `setEnterpriseCacheStorageLimit`: Sets the GitHub Actions cache storage limit policy for an enterprise.
* **Set Enterprise Code Security And Analysis** `setEnterpriseCodeSecurityAnalysis`: Update enterprise-wide code security and analysis settings. Pass a pre-stringified JSON body with any of: advanced_security_enabled_for_new_repositories, dependabot_alerts_enabled_for_new_repositories, secret_scanning_enabled_for_new_repositories, secret_scanning_push_protection_enabled_for_new_repositories, secret_scanning_push_protection_custom_link.
* **Set Enterprise Default Workflow Permissions** `setEnterpriseWorkflowPermissions`: Sets the default workflow permissions granted to the GITHUB_TOKEN and whether GitHub Actions can approve pull requests, for an enterprise. Returns 204 No Content.
* **Set Enterprise Fork PR Contributor Approval Policy** `setEnterpriseForkPrContributorApproval`: Sets the fork pull request contributor approval policy for an enterprise. Returns 204 No Content.
* **Set Enterprise Fork PR Workflows In Private Repos** `setEnterpriseForkPrPrivateRepos`: Sets whether workflows triggered by pull requests from forks are allowed to run on private repositories in an enterprise, and related token/secret settings. Returns 204 No Content.
* **Set Enterprise OIDC Issuer** `setEnterpriseOidcIssuer`: Sets the GitHub OIDC custom issuer policy for an enterprise.
* **Set Enterprise Org App Installation Repository Selection** `setEnterpriseOrgAppInstallationRepositorySelection`: Change an app installation's repository selection mode in an org. Pass a pre-stringified JSON body, e.g. {"repository_selection":"all"} or {"repository_selection":"selected"}.
* **Set Enterprise Runner Labels** `setEnterpriseRunnerLabels`: Remove all previous custom labels and set the new custom labels for a specific self-hosted runner in an enterprise.
* **Set Enterprise Security Product Enablement** `setEnterpriseSecurityProductEnablement`: Enable or disable a GitHub Advanced Security product for all organizations in an enterprise. security_product is one of advanced_security, dependabot_alerts, secret_scanning, secret_scanning_push_protection. enablement is enable_all or disable_all.
* **Set Enterprise Self-Hosted Runners Settings** `setEnterpriseSelfHostedRunnersSettings`: Sets whether self-hosted runners are disabled for all organizations in an enterprise. Returns 204 No Content.
* **Set Organization Access For Enterprise Runner Group** `setEnterpriseRunnerGroupOrgs`: Replaces the list of organizations that have access to a self-hosted runner group in an enterprise. Returns 204 No Content.
* **Set Runners In Enterprise Runner Group** `setEnterpriseRunnerGroupRunners`: Replaces the list of self-hosted runners that are part of a runner group in an enterprise. Returns 204 No Content.
* **Set Selected Organizations Enabled For Enterprise Actions** `setEnterprisePermissionsOrgs`: Replaces the list of selected organizations that are enabled for GitHub Actions in an enterprise. Only applicable when enabled_organizations is set to selected. Returns 204 No Content.
* **Update Enterprise Audit Log Stream** `updateEnterpriseAuditLogStream`: Update an existing audit log streaming endpoint. Pass a pre-stringified JSON body with enabled, stream_type, and vendor_specific.
* **Update Enterprise Budget** `updateEnterpriseBudget`: Updates a budget configured for an enterprise.
* **Update Enterprise Code Security Configuration** `updateEnterpriseCodeSecurityConfiguration`: Updates a code security configuration in an enterprise.
* **Update Enterprise Custom Properties Schema** `updateEnterpriseCustomPropertiesSchema`: Create or update custom property definitions for an enterprise (bulk). Pass a pre-stringified JSON body of the form {"properties":[{"property_name":"environment","value_type":"single_select","required":true,"default_value":"production","allowed_values":["production","staging"]}]}.
* **Update Enterprise Hosted Runner** `updateEnterpriseHostedRunner`: Updates a GitHub-hosted runner for an enterprise.
* **Update Enterprise Network Configuration** `updateEnterpriseNetworkConfiguration`: Updates a hosted compute network configuration for an enterprise.
* **Update Enterprise Ruleset** `updateEnterpriseRuleset`: Update an enterprise repository ruleset. Pass a pre-stringified JSON body with any of name, enforcement, target, conditions, rules, bypass_actors.
* **Update Enterprise Self-Hosted Runner Group** `updateEnterpriseRunnerGroup`: Updates the name, visibility, or workflow restrictions of a self-hosted runner group for an enterprise. Returns the updated runner group object.
* **Update Enterprise Team** `updateEnterpriseTeam`: Updates an existing enterprise team (PATCH). Only fields provided are changed. Returns the updated team.
* **Update Issue** `updateIssue`: Update an issue (title, body, state, assignees, labels, milestone, etc.) by issue number. Returns the updated issue object.
* **Update Pull Request** `updatePull`: Update an existing pull request: change title, body, state (open/closed), base branch, or maintainer_can_modify. Returns the updated pull request object.
* **Update Release** `updateRelease`: Update a release identified by release_id. Users with push access can edit a release. All body fields are optional. Returns the updated release object (200).
* **Update Repo Webhook** `updateRepoWebhook`: Update a repository webhook by its id (events, active state, config). The config block is replaced on every update, so send url, content_type and secret together (an omitted secret is removed and content_type falls back to form). Events are optional; if omitted the current events are kept. Returns the updated hook object.
* **Update Repository** `updateRepo`: Updates a repository's settings (partial update: only the fields you pass are sent and changed). Requires admin access. Set archived=false to unarchive. Returns the full updated repository object.
* **Update SCIM Group (Enterprise)** `updateScimGroup`: Partially updates a SCIM group (PATCH with SCIM Operations) in an enterprise. Returns the updated group resource.
* **Update SCIM User (Enterprise)** `updateScimUser`: Partially updates a SCIM user (PATCH with SCIM Operations) in an enterprise. Commonly used to activate/deactivate a user. Returns the updated user resource.
* **Upsert Enterprise Custom Property** `upsertEnterpriseCustomProperty`: Create or update a single custom property definition for an enterprise. Pass a pre-stringified JSON body, e.g. {"value_type":"single_select","required":true,"default_value":"production","description":"Deployment env","allowed_values":["production","staging"]}.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Branch or Tag Created | `create` | A Git branch or tag was created. GitHub sends event type 'create'. This event has no 'action' field. |
| Branch or Tag Deleted | `delete` | A Git branch or tag was deleted. GitHub sends event type 'delete'. This event has no 'action' field. |
| Branch Protection Rule Created | `branch_protection_rule.created` | A branch protection rule was created. GitHub sends event type 'branch_protection_rule'. |
| Branch Protection Rule Deleted | `branch_protection_rule.deleted` | A branch protection rule was deleted. |
| Branch Protection Rule Edited | `branch_protection_rule.edited` | A branch protection rule was edited. |
| Check Run | `check_run` | Activity on a check run. GitHub sends event type 'check_run'; payload 'action' is one of created, completed, rerequested, requested_action. |
| Check Suite | `check_suite` | Activity on a check suite. GitHub sends event type 'check_suite'; payload 'action' is one of completed, requested, rerequested. |
| Commit Comment Created | `commit_comment.created` | A commit comment was created. GitHub sends event type 'commit_comment'; payload 'action' is 'created'. |
| Deployment Created | `deployment.created` | A deployment was created. GitHub sends event type 'deployment'; payload 'action' is 'created'. |
| Deployment Status Created | `deployment_status.created` | A deployment status was created. GitHub sends event type 'deployment_status'; payload 'action' is 'created'. |

<details>

<summary>See 91 more events</summary>

* **Discussion Answered** `discussion.answered`: A comment on a discussion was marked as the answer.
* **Discussion Comment Created** `discussion_comment.created`: A comment on a discussion was created. GitHub sends event type 'discussion_comment'.
* **Discussion Created** `discussion.created`: A discussion was created. GitHub sends event type 'discussion'.
* **Discussion Edited** `discussion.edited`: A discussion was edited.
* **GitHub Pages Build** `page_build`: A GitHub Pages site was built. GitHub sends event type 'page_build'. This event has no 'action' field.
* **Issue Assigned** `issues.assigned`: A user was assigned to an issue.
* **Issue Closed** `issues.closed`: An issue was closed.
* **Issue Comment Created** `issue_comment.created`: A comment on an issue was created. GitHub sends event type 'issue_comment' in the X-GitHub-Event header.
* **Issue Comment Deleted** `issue_comment.deleted`: A comment on an issue was deleted.
* **Issue Comment Edited** `issue_comment.edited`: A comment on an issue was edited.
* **Issue Deleted** `issues.deleted`: An issue was deleted.
* **Issue Demilestoned** `issues.demilestoned`: An issue was removed from a milestone.
* **Issue Edited** `issues.edited`: The title or body of an issue was edited.
* **Issue Labeled** `issues.labeled`: A label was added to an issue.
* **Issue Locked** `issues.locked`: Conversation on an issue was locked.
* **Issue Milestoned** `issues.milestoned`: An issue was added to a milestone.
* **Issue Opened** `issues.opened`: An issue was opened. GitHub sends event type 'issues' in the X-GitHub-Event header and the specific sub-event in the payload 'action' field.
* **Issue Pinned** `issues.pinned`: An issue was pinned to a repository.
* **Issue Reopened** `issues.reopened`: A closed issue was reopened.
* **Issue Transferred** `issues.transferred`: An issue was transferred to another repository.
* **Issue Unassigned** `issues.unassigned`: A user was unassigned from an issue.
* **Issue Unlabeled** `issues.unlabeled`: A label was removed from an issue.
* **Issue Unlocked** `issues.unlocked`: Conversation on an issue was unlocked.
* **Issue Unpinned** `issues.unpinned`: An issue was unpinned from a repository.
* **Label Created** `label.created`: A label was created. GitHub sends event type 'label' in the X-GitHub-Event header.
* **Label Deleted** `label.deleted`: A label was deleted.
* **Label Edited** `label.edited`: A label was edited.
* **Member Added** `member.added`: A user accepted an invitation to a repository. GitHub sends event type 'member'.
* **Member Edited** `member.edited`: The permissions of a collaborator on a repository were changed.
* **Member Removed** `member.removed`: A collaborator was removed from a repository.
* **Milestone Closed** `milestone.closed`: A milestone was closed.
* **Milestone Created** `milestone.created`: A milestone was created. GitHub sends event type 'milestone' in the X-GitHub-Event header.
* **Milestone Deleted** `milestone.deleted`: A milestone was deleted.
* **Milestone Edited** `milestone.edited`: A milestone was edited.
* **Milestone Opened** `milestone.opened`: A milestone was opened.
* **Pull Request Assigned** `pull_request.assigned`: A user was assigned to a pull request. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Auto Merge Disabled** `pull_request.auto_merge_disabled`: Auto merge was disabled for a pull request. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Auto Merge Enabled** `pull_request.auto_merge_enabled`: Auto merge was enabled for a pull request. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Closed** `pull_request.closed`: A pull request was closed. If merged is true it was merged, otherwise it was closed without merging. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Converted To Draft** `pull_request.converted_to_draft`: A pull request was converted to a draft. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Demilestoned** `pull_request.demilestoned`: A pull request was removed from a milestone. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Dequeued** `pull_request.dequeued`: A pull request was removed from the merge queue. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Edited** `pull_request.edited`: The title or body of a pull request was edited, or the base branch was changed. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Enqueued** `pull_request.enqueued`: A pull request was added to the merge queue. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Labeled** `pull_request.labeled`: A label was added to a pull request. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Locked** `pull_request.locked`: Conversation on a pull request was locked. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Milestoned** `pull_request.milestoned`: A pull request was added to a milestone. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Opened** `pull_request.opened`: A pull request was opened. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Ready For Review** `pull_request.ready_for_review`: A draft pull request was marked ready for review. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Reopened** `pull_request.reopened`: A closed pull request was reopened. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Review Comment Created** `pull_request_review_comment.created`: A comment on a pull request diff was created. GitHub sends event type 'pull_request_review_comment'.
* **Pull Request Review Comment Deleted** `pull_request_review_comment.deleted`: A comment on a pull request diff was deleted. GitHub sends event type 'pull_request_review_comment'.
* **Pull Request Review Comment Edited** `pull_request_review_comment.edited`: A comment on a pull request diff was edited. GitHub sends event type 'pull_request_review_comment'.
* **Pull Request Review Dismissed** `pull_request_review.dismissed`: A review on a pull request was dismissed. GitHub sends event type 'pull_request_review'.
* **Pull Request Review Edited** `pull_request_review.edited`: The body of a review on a pull request was edited. GitHub sends event type 'pull_request_review'.
* **Pull Request Review Request Removed** `pull_request.review_request_removed`: A request for review by a person or team was removed from a pull request. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Review Requested** `pull_request.review_requested`: Review by a person or team was requested for a pull request. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Review Submitted** `pull_request_review.submitted`: A review on a pull request was submitted. GitHub sends event type 'pull_request_review' in the X-GitHub-Event header.
* **Pull Request Review Thread Resolved** `pull_request_review_thread.resolved`: A pull request review comment thread was resolved. GitHub sends event type 'pull_request_review_thread'.
* **Pull Request Review Thread Unresolved** `pull_request_review_thread.unresolved`: A pull request review comment thread was marked as unresolved. GitHub sends event type 'pull_request_review_thread'.
* **Pull Request Stacked** `pull_request.stacked`: A pull request was stacked on another pull request. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Synchronize** `pull_request.synchronize`: A pull request's head branch was updated (new commits pushed, or the base branch changed). GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Unassigned** `pull_request.unassigned`: A user was unassigned from a pull request. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Unlabeled** `pull_request.unlabeled`: A label was removed from a pull request. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Pull Request Unlocked** `pull_request.unlocked`: Conversation on a pull request was unlocked. GitHub sends event type 'pull_request' in the X-GitHub-Event header.
* **Push** `push`: One or more commits were pushed to a repository branch or tag. GitHub sends event type 'push' in the X-GitHub-Event header. This event has no 'action' field.
* **Release Created** `release.created`: A draft was saved, or a release/pre-release was published without previously being saved as a draft.
* **Release Deleted** `release.deleted`: A release, pre-release, or draft release was deleted.
* **Release Edited** `release.edited`: The details of a release, pre-release, or draft release were edited.
* **Release Prereleased** `release.prereleased`: A pre-release was created.
* **Release Published** `release.published`: A release, pre-release, or draft of a release was published. GitHub sends event type 'release'.
* **Release Released** `release.released`: A release was published, or a pre-release was changed to a release.
* **Release Unpublished** `release.unpublished`: A release or pre-release was unpublished.
* **Repository Archived** `repository.archived`: A repository was archived.
* **Repository Created** `repository.created`: A repository was created. GitHub sends event type 'repository'.
* **Repository Edited** `repository.edited`: The topics, default branch, description, or homepage of a repository was edited.
* **Repository Forked** `fork`: A user forked the repository. GitHub sends event type 'fork'. This event has no 'action' field.
* **Repository Made Public** `public`: A private repository was made public. GitHub sends event type 'public'. This event has no 'action' field.
* **Repository Privatized** `repository.privatized`: The visibility of a repository was changed to private.
* **Repository Publicized** `repository.publicized`: The visibility of a repository was changed to public.
* **Repository Renamed** `repository.renamed`: A repository was renamed.
* **Repository Unarchived** `repository.unarchived`: A repository was unarchived.
* **Star Created** `star.created`: A star was added to the repository. GitHub sends event type 'star'; payload 'action' is 'created'.
* **Star Deleted** `star.deleted`: A star was removed from the repository. GitHub sends event type 'star'; payload 'action' is 'deleted'.
* **Status** `status`: The status of a Git commit changed. GitHub sends event type 'status'. This event has no 'action' field.
* **Watch Started** `watch.started`: A user starred (watched) the repository. GitHub sends event type 'watch'; payload 'action' is 'started'.
* **Wiki Page Updated** `gollum`: A wiki page was created or updated. GitHub sends event type 'gollum'. This event has no 'action' field.
* **Workflow Job** `workflow_job`: Activity on a workflow job in a run. GitHub sends event type 'workflow_job'; payload 'action' is one of queued, in_progress, completed.
* **Workflow Run Completed** `workflow_run.completed`: A workflow run finished.
* **Workflow Run In Progress** `workflow_run.in_progress`: A workflow run is in progress.
* **Workflow Run Requested** `workflow_run.requested`: A workflow run was requested. GitHub sends event type 'workflow_run'.

</details>
