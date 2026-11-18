---
description: "HashiCorp HCP Terraform (Terraform Cloud) API v2."
hidden: true
---

# Terraform Cloud

HashiCorp HCP Terraform (Terraform Cloud) API v2. Manage organizations, workspaces, projects, runs, plans, applies, configuration versions, state versions, variables, variable sets, teams, policies, registry modules, SSH keys, notifications, run triggers, agent pools, VCS OAuth clients, and memberships. Uses the JSON:API format.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [app.terraform.io](https://app.terraform.io) |
| **Authentication** | Credentials you enter |
| **Actions** | 276 |
| **Events** | 11 |
| **Slug** | `terraformCloud` |

## Use it

Add Terraform Cloud from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.terraformCloud.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Policies To Policy Set | `addPoliciesToPolicySet` | Add one or more policys to a policy set. |
| Add Policy Set Workspace Exclusions | `addPolicySetWorkspaceExclusions` | Exclude one or more workspaces to a policy set. |
| Add Tag To Workspaces | `addTagToWorkspaces` | Apply an existing organization tag to one or more workspaces. |
| Add Team Members By Organization Membership | `addTeamMembersByMembership` | Add one or more users to a team, identified by organization membership ID. Users added by username must already be organization members. |
| Add Team Members By Username | `addTeamMembersByUser` | Add one or more users to a team, identified by username. Users added by username must already be organization members. |
| Add Workspace Remote State Consumers | `addWorkspaceRemoteStateConsumers` | Allow additional workspaces to read this workspace's remote state. |
| Add Workspace Tags | `addWorkspaceTags` | Add one or more tags to a workspace. Tags are created in the organization if they do not exist. |
| Apply Run | `applyRun` | Confirm and apply a run that is waiting for confirmation. This provisions real infrastructure and may incur cost. |
| Apply Variable Set To Projects | `applyVariableSetToProjects` | Apply a variable set to one or more projects. |
| Apply Variable Set To Workspaces | `applyVariableSetToWorkspaces` | Apply a variable set to one or more workspaces. |
| Archive Configuration Version | `archiveConfigurationVersion` | Archive a configuration version, deleting its uploaded tarball. Only API-created configuration versions can be archived. |
| Assign Workspace SSH Key | `assignWorkspaceSshKey` | Assign an SSH key to a workspace so Terraform can clone private module repositories. Pass a null id to unassign. |
| Attach Policy Set To Projects | `addProjectsToPolicySet` | Attach one or more projects to a policy set. |
| Attach Policy Set To Workspaces | `addWorkspacesToPolicySet` | Attach one or more workspaces to a policy set. |
| Attach Run Task To Workspace | `createWorkspaceRunTask` | Attach an existing organization run task to a workspace. Run tasks are a paid feature. |
| Attach VCS Connection To Projects | `addOAuthClientProjects` | Attach a VCS connection to one or more projects. The connection must not be organization scoped. |
| Cancel Run | `cancelRun` | Interrupt a run that is currently planning or applying. |
| Change Account Password | `changeAccountPassword` | Change the password of the user account the API token belongs to. Requires the current password. |
| Create Additional Team Token | `createTeamTokenMultiple` | Generate an additional, independently describable team authentication token without invalidating existing tokens. |
| Create Agent Pool | `createAgentPool` | Create an agent pool in an organization. Agents are a paid feature. |
| Create Agent Token | `createAgentToken` | Generate an authentication token for an agent pool so agents can register with it. Agents are a paid feature. |
| Create Audit Trail Token | `createAuditTrailToken` | Generate an audit trail token for an organization. Audit trails are a paid feature. |
| Create Configuration Version | `createConfigurationVersion` | Create a configuration version in a workspace. The response contains a one-time upload URL for the configuration tarball, which must be uploaded separately before the configuration version can be used. |
| Create GPG Key | `createGpgKey` | Add a GPG public key to a private registry namespace so provider versions can be signature-verified. |
| Create Organization | `createOrganization` | Create a new organization. The name must be unique across HCP Terraform and the email is the primary admin contact. |
| Create Organization Token | `createOrganizationToken` | Generate a new organization API token. This regenerates and invalidates the organization's existing token. |
| Create Plan Export | `createPlanExport` | Export a plan in Sentinel mock format so policies can be tested against it locally. |
| Create Policy | `createPolicy` | Create a policy in an organization. The policy code must be uploaded separately. Policy enforcement is a paid feature. |
| Create Policy Set | `createPolicySet` | Create a policy set in an organization. Policy enforcement is a paid feature. |
| Create Policy Set Parameter | `createPolicySetParameter` | Add a parameter to a policy set. |
| Create Policy Set Version | `createPolicySetVersion` | Create a new version of a policy set so its policy files can be uploaded. Only valid for versioned, non-VCS-backed policy sets. The response contains a one-time upload URL. |
| Create Project | `createProject` | Create a new project in an organization. Projects group workspaces and share settings across them. |
| Create Project Notification Configuration | `createProjectNotificationConfiguration` | Create a notification configuration that sends project events to a webhook, Slack, Microsoft Teams or email. |
| Create Registry Module | `createRegistryModule` | Create a module in an organization's private registry without connecting it to a VCS repository. Module versions are then uploaded through the API. |
| Create Registry Module From VCS | `createRegistryModuleFromVcs` | Publish a module to an organization's private registry from a VCS repository. Versions are then published automatically from repository tags. |
| Create Registry Module Version | `createRegistryModuleVersion` | Create a new version of a private registry module. The response contains a one-time URL for uploading the module tarball. |
| Create Registry Provider | `createRegistryProvider` | Create a provider in an organization's private registry, or add a public provider to the organization's registry. |
| Create Registry Provider Platform | `createRegistryProviderPlatform` | Create a platform for a private registry provider version. The response contains a one-time URL for uploading the provider binary. |
| Create Registry Provider Version | `createRegistryProviderVersion` | Create a version of a private registry provider. The response contains one-time URLs for uploading the SHA sums file and its signature. |
| Create Reserved Tag Key | `createReservedTagKey` | Reserve a tag key in an organization so its value can be governed centrally. |
| Create Run | `createRun` | Create a run in a workspace. A run performs a plan and, depending on the workspace settings, an apply. Set plan-only to true to create a speculative run that can never be applied. |
| Create Run Comment | `createRunComment` | Post a comment on a run. |
| Create Run Task | `createRunTask` | Create a run task in an organization. Run tasks are a paid feature. |
| Create Run Trigger | `createRunTrigger` | Create a run trigger so a successful apply in the source workspace queues a run in this workspace. |
| Create SSH Key | `createSshKey` | Add an SSH private key to an organization so workspaces can clone private module repositories. |
| Create State Version | `createStateVersion` | Create a state version in a workspace. The workspace must be locked by the same token. Supply the base64-encoded state directly, or omit it and use the returned upload URL. |
| Create Team | `createTeam` | Create a team in an organization. Creating teams beyond the default owners team is a paid feature. |
| Create Team Notification Configuration | `createTeamNotificationConfiguration` | Create a notification configuration that sends team events to a webhook, Slack, Microsoft Teams or email. |
| Create Team Token | `createTeamToken` | Generate a new team authentication token. This regenerates and invalidates the team's existing legacy token. |
| Create User Token | `createUserToken` | Generate a new API token for a user. A token can only create tokens for its own user. |
| Create Variable Set | `createVariableSet` | Create a variable set in an organization and optionally assign it to workspaces or projects. |
| Create Variable Set Variable | `createVariableSetVariable` | Add a variable to a variable set. |
| Create VCS Connection | `createOAuthClient` | Create a VCS connection (OAuth client) so workspaces and policy sets can be backed by a VCS repository. |
| Create Workspace | `createWorkspace` | Create a new workspace in an organization. All listed fields are sent; description may be an empty string and auto-apply defaults to false. |
| Create Workspace Notification Configuration | `createWorkspaceNotificationConfiguration` | Create a notification configuration that sends workspace events to a webhook, Slack, Microsoft Teams or email. |
| Create Workspace Variable | `createWorkspaceVariable` | Create a Terraform input variable or environment variable on a workspace. |
| Delete Agent | `deleteAgent` | Deregister an agent. The agent must be in the errored or exited state. Agents are a paid feature. |
| Delete Agent Pool | `deleteAgentPool` | Delete an agent pool. Agents are a paid feature. |
| Delete Audit Trail Token | `deleteAuditTrailToken` | Delete the audit trail token of an organization. Audit trails are a paid feature. |
| Delete Authentication Token | `deleteAuthenticationToken` | Delete an authentication token by its ID. Works for user, team and organization tokens. |
| Delete GPG Key | `deleteGpgKey` | Delete a GPG key from a private registry namespace. |
| Delete Notification Configuration | `deleteNotificationConfiguration` | Delete a notification configuration. |
| Delete Organization | `deleteOrganization` | Permanently delete an organization by name. This removes all workspaces, runs, and state. |
| Delete Organization Data Retention Policy | `deleteDataRetentionPolicy` | Remove the data retention policy from an organization so it inherits the site-wide default. |
| Delete Organization Tags | `deleteOrganizationTags` | Delete one or more tags from an organization, removing them from every workspace. |
| Delete Organization Token | `deleteOrganizationToken` | Delete the API token of an organization. |
| Delete Plan Export | `deletePlanExport` | Delete an exported plan before it expires. |
| Delete Policy | `deletePolicy` | Delete a policy from an organization. |
| Delete Policy Set | `deletePolicySet` | Delete a policy set and stop enforcing its policies. |
| Delete Policy Set Parameter | `deletePolicySetParameter` | Delete a parameter from a policy set. |
| Delete Project | `deleteProject` | Delete a project. The project must not contain any workspaces. |
| Delete Registry Provider | `deleteRegistryProvider` | Delete a provider and all of its versions from an organization's private registry. |
| Delete Registry Provider Platform | `deleteRegistryProviderPlatform` | Delete a platform from a private registry provider version. |
| Delete Registry Provider Version | `deleteRegistryProviderVersion` | Delete a version of a private registry provider and all of its platforms. |
| Delete Reserved Tag Key | `deleteReservedTagKey` | Delete a reserved tag key from an organization. |
| Delete Run Task | `deleteRunTask` | Delete a run task and remove it from every workspace it is attached to. |
| Delete Run Trigger | `deleteRunTrigger` | Delete a run trigger. |
| Delete SSH Key | `deleteSshKey` | Delete an SSH key from an organization. |
| Delete Team | `deleteTeam` | Delete a team and revoke its access to every workspace and project. |
| Delete Team Token | `deleteTeamToken` | Delete the legacy authentication token of a team. |
| Delete Variable Set | `deleteVariableSet` | Delete a variable set and remove it from every workspace and project it is applied to. |
| Delete Variable Set Variable | `deleteVariableSetVariable` | Remove a variable from a variable set. |
| Delete VCS Connection | `deleteOAuthClient` | Delete a VCS connection (OAuth client) and destroy its OAuth tokens. |
| Delete VCS OAuth Token | `deleteOAuthToken` | Delete a VCS OAuth token. |
| Delete Workspace | `deleteWorkspace` | Delete a workspace by organization and workspace name. This is irreversible. |
| Delete Workspace Data Retention Policy | `deleteWorkspaceDataRetentionPolicy` | Remove the data retention policy from a workspace so it inherits the organization policy. |
| Delete Workspace Variable | `deleteWorkspaceVariable` | Delete a variable from a workspace. |
| Detach Policy Set From Projects | `removeProjectsFromPolicySet` | Detach one or more projects from a policy set. |
| Detach Policy Set From Workspaces | `removeWorkspacesFromPolicySet` | Detach one or more workspaces from a policy set. |
| Detach Run Task From Workspace | `deleteWorkspaceRunTask` | Detach a run task from a workspace. |
| Detach VCS Connection From Projects | `removeOAuthClientProjects` | Detach a VCS connection from one or more projects. The connection must not be organization scoped. |
| Discard Run | `discardRun` | Discard a run that is waiting for confirmation, skipping the apply. |
| Download Configuration Version | `downloadConfigurationVersion` | Download the configuration tarball of a configuration version as a gzipped archive. |
| Download Plan Export | `downloadPlanExport` | Download the exported plan data as a gzipped tarball. Only available once the export has finished. |
| Download Run Configuration Version | `downloadRunConfigurationVersion` | Download the configuration tarball used by a run as a gzipped archive. |
| Force Cancel Run | `forceCancelRun` | Forcefully cancel a run that did not respond to a normal cancel. Only available after a cancel was attempted. |
| Force Execute Run | `forceExecuteRun` | Force a pending run to execute immediately by cancelling any prior runs blocking the workspace. |
| Force Unlock Workspace | `forceUnlockWorkspace` | Force-unlock a workspace that was locked by another user, run or token. Requires admin access to the workspace. |
| Get Account Details | `getAccountDetails` | Retrieve the account details of the user or team associated with the API token. |
| Get Agent | `getAgent` | Show a single agent. Agents are a paid feature. |
| Get Agent Pool | `getAgentPool` | Show a single agent pool. Agents are a paid feature. |
| Get Apply | `getApply` | Show the details of an apply, including resource change counts and a URL for reading the apply log. |
| Get Apply Errored State | `getApplyErroredState` | Download the state file that an apply failed to persist, so it can be recovered manually. |
| Get Assessment Result | `getAssessmentResult` | Show the result of a health assessment (drift detection) run against a workspace. Health assessments are a paid feature. |
| Get Assessment Result JSON Output | `getAssessmentResultJsonOutput` | Download the JSON plan produced by a health assessment. Health assessments are a paid feature. |
| Get Assessment Result JSON Schema | `getAssessmentResultJsonSchema` | Download the provider schemas used by a health assessment. Health assessments are a paid feature. |
| Get Assessment Result Log Output | `getAssessmentResultLogOutput` | Download the raw log output of a health assessment. Health assessments are a paid feature. |
| Get Authentication Token | `getAuthenticationToken` | Show the details of an authentication token by its ID. |
| Get Comment | `getComment` | Show a single run comment. |
| Get Configuration Version | `getConfigurationVersion` | Show the details of a single configuration version. |
| Get Configuration Version Ingress Attributes | `getConfigurationVersionIngressAttributes` | Show the VCS commit information associated with a configuration version created from a VCS-backed workspace. |
| Get Cost Estimate | `getCostEstimate` | Show the cost estimate produced for a run. Cost estimation is a paid feature. |
| Get Current State Version | `getCurrentStateVersion` | Show the state version that is currently active for a workspace. |
| Get GitHub App Installation | `getGithubAppInstallation` | Show a single GitHub App installation. |
| Get GPG Key | `getGpgKey` | Show a single GPG key used to sign private registry provider versions. |
| Get IP Ranges | `getIpRanges` | Get the list of HCP Terraform egress IP ranges used for API, notifications, sentinel and VCS traffic. |
| Get Notification Configuration | `getNotificationConfiguration` | Show a single notification configuration, including its recent delivery responses. |
| Get Organization | `getOrganization` | Show details for a single organization by its name. |
| Get Organization Data Retention Policy | `getDataRetentionPolicy` | Show the data retention policy of an organization. Data retention policies are a paid feature. |
| Get Organization Entitlement Set | `getEntitlementSet` | Show the entitlement set for an organization, describing which features and limits are available under its plan. |
| Get Organization Membership | `getOrganizationMembership` | Show a single organization membership. |
| Get Organization Subscription | `getOrganizationSubscription` | Show the current subscription and plan details for an organization. |
| Get Plan | `getPlan` | Show the details of a plan, including resource change counts and a URL for reading the plan log. |
| Get Plan Export | `getPlanExport` | Show the status of a plan export. |
| Get Plan JSON Output | `getPlanJsonOutput` | Download the JSON execution plan for a plan, in the format produced by terraform show -json. |
| Get Policy | `getPolicy` | Show a single policy. Policy enforcement is a paid feature. |
| Get Policy Check | `getPolicyCheck` | Show a single Sentinel policy check. Policy enforcement is a paid feature. |
| Get Policy Set | `getPolicySet` | Show a single policy set. Policy enforcement is a paid feature. |
| Get Policy Set Outcome | `getPolicySetOutcome` | Show a single policy set outcome. Policy enforcement is a paid feature. |
| Get Policy Set Version | `getPolicySetVersion` | Show a policy set version, including its upload URL while it is pending. |
| Get Project | `getProject` | Show the details and settings of a single project. |
| Get Registry Module | `getRegistryModule` | Show a single module in an organization's private registry. |
| Get Registry Provider | `getRegistryProvider` | Show a single provider in an organization's private registry. |
| Get Registry Provider Platform | `getRegistryProviderPlatform` | Show a single platform of a private registry provider version. |
| Get Registry Provider Version | `getRegistryProviderVersion` | Show a single version of a provider in an organization's private registry. |
| Get Run | `getRun` | Show the details and current status of a single run. |
| Get Run Plan JSON Output | `getRunPlanJsonOutput` | Download the JSON execution plan for the plan belonging to a run. |
| Get Run Sanitized Plan JSON Output | `getRunPlanSanitizedOutput` | Download the sanitized JSON execution plan for the plan belonging to a run. |
| Get Run Task | `getRunTask` | Show a single run task. Run tasks are a paid feature. |
| Get Run Task Result | `getTaskResult` | Show the result reported by a single run task invocation. Run tasks are a paid feature. |
| Get Run Task Stage | `getTaskStage` | Show a single run task stage and its results. Run tasks are a paid feature. |
| Get Run Trigger | `getRunTrigger` | Show a single run trigger. |
| Get Sanitized Plan JSON Output | `getPlanSanitizedOutput` | Download the JSON execution plan for a plan with sensitive values redacted. |
| Get SSH Key | `getSshKey` | Show a single SSH key. The private key value is never returned. |
| Get State Version | `getStateVersion` | Show the details of a single state version, including download URLs for the raw and JSON state. |
| Get State Version Output | `getStateVersionOutput` | Show a single state version output. |
| Get Team | `getTeam` | Show the details and organization access of a single team. |
| Get Team Access To Project | `getProjectTeamAccess` | Show a single team/project access relationship. |
| Get Team Access To Workspace | `getTeamAccess` | Show a single team/workspace access relationship. |
| Get Team Token | `getTeamToken` | Show the legacy authentication token of a team. |
| Get User | `getUser` | Show the public profile of a user. |
| Get Variable Set | `getVariableSet` | Show the details of a single variable set. |
| Get VCS Connection | `getOAuthClient` | Show a single VCS connection (OAuth client). |
| Get VCS OAuth Token | `getOAuthToken` | Show a single VCS OAuth token. |
| Get Workspace | `getWorkspace` | Show a single workspace by organization name and workspace name. |
| Get Workspace By ID | `getWorkspaceById` | Show a single workspace by its workspace ID (ws-xxxx). |
| Get Workspace Data Retention Policy | `getWorkspaceDataRetentionPolicy` | Show the data retention policy of a workspace. Data retention policies are a paid feature. |
| Get Workspace Run Task | `getWorkspaceRunTask` | Show a single run task attachment on a workspace. Run tasks are a paid feature. |
| Grant Team Access To Project | `createProjectTeamAccess` | Grant a team access to a project. Managing team access is a paid feature. |
| Grant Team Access To Workspace | `createTeamAccess` | Grant a team access to a workspace. Managing team access is a paid feature. |
| Invite User To Organization | `createOrganizationMembership` | Invite a user to join an organization by email address, optionally adding them to teams. |
| List Agent Pools | `listAgentPools` | List the agent pools of an organization. Agents are a paid feature. |
| List Agent Tokens | `listAgentTokens` | List the authentication tokens of an agent pool. Agents are a paid feature. |
| List Agents | `listAgents` | List the agents registered in an agent pool. Agents are a paid feature. |
| List Audit Trail Events | `listAuditTrail` | List the audit trail events of an organization. Requires an audit trail token. Audit trails are a paid feature. |
| List Configuration Versions | `listConfigurationVersions` | List the configuration versions uploaded to a workspace, most recent first. |
| List Current State Version Outputs | `listCurrentStateVersionOutputs` | List the Terraform outputs of a workspace's current state version. |
| List Feature Sets | `listFeatureSets` | List all feature sets available on HCP Terraform. |
| List GitHub App Installations | `listGithubAppInstallations` | List the GitHub App installations available to the user the API token belongs to. |
| List GPG Keys | `listGpgKeys` | List the GPG keys used to sign private registry provider versions. |
| List My Organization Memberships | `listMyOrganizationMemberships` | List the organization memberships of the user the API token belongs to. |
| List Organization Feature Sets | `listOrganizationFeatureSets` | List the feature sets available to an organization, including the currently active one. |
| List Organization Memberships | `listOrganizationMemberships` | List the members of an organization, including users who have been invited but have not yet accepted. |
| List Organization Module Producers | `listOrganizationModuleProducers` | List the organizations that may share private registry modules with the given organization. |
| List Organization Runs | `listOrganizationRuns` | List the runs across all workspaces in an organization, most recent first. |
| List Organization Tags | `listOrganizationTags` | List the workspace tags defined across an organization. |
| List Organization Variable Sets | `listOrganizationVariableSets` | List the variable sets that belong to an organization. |
| List Organizations | `listOrganizations` | List the organizations the current API token has access to. |
| List Policies | `listPolicies` | List the policies of an organization. Policy enforcement is a paid feature. |
| List Policy Checks | `listPolicyChecks` | List the Sentinel policy checks performed for a run. Policy enforcement is a paid feature. |
| List Policy Evaluations | `listPolicyEvaluations` | List the policy evaluations of a run task stage. Policy enforcement is a paid feature. |
| List Policy Set Outcomes | `listPolicySetOutcomes` | List the policy set outcomes of a policy evaluation. Policy enforcement is a paid feature. |
| List Policy Set Parameters | `listPolicySetParameters` | List the parameters of a policy set. Parameters are passed to Sentinel policies at evaluation time. |
| List Policy Sets | `listPolicySets` | List the policy sets of an organization. Policy enforcement is a paid feature. |
| List Project Effective Tag Bindings | `listProjectEffectiveTagBindings` | List the effective tags of a project, including inherited tags. For projects this matches the tag bindings list. |
| List Project Notification Configurations | `listProjectNotificationConfigurations` | List the notification configurations of a project. |
| List Project Tag Bindings | `listProjectTagBindings` | List the tags bound to a project. Workspaces in the project inherit these tags. |
| List Project Variable Sets | `listProjectVariableSets` | List the variable sets applied to a project. |
| List Projects | `listProjects` | List all projects in an organization. Supports filtering by name and pagination. |
| List Registry Modules | `listRegistryModules` | List the modules in an organization's private registry. |
| List Registry Provider Platforms | `listRegistryProviderPlatforms` | List the platforms of a private registry provider version. |
| List Registry Provider Versions | `listRegistryProviderVersions` | List the versions of a provider in an organization's private registry. |
| List Registry Providers | `listRegistryProviders` | List the providers in an organization's private registry. |
| List Reserved Tag Keys | `listReservedTagKeys` | List the reserved tag keys of an organization. |
| List Run Comments | `listRunComments` | List the comments posted on a run. |
| List Run Task Stages | `listTaskStages` | List the task stages of a run. Run tasks are a paid feature. |
| List Run Tasks | `listRunTasks` | List the run tasks of an organization. Run tasks are a paid feature. |
| List Run Triggers | `listRunTriggers` | List the run triggers of a workspace. The type filter selects inbound or outbound triggers. |
| List SSH Keys | `listSshKeys` | List the SSH keys of an organization. Private key values are never returned. |
| List State Version Outputs | `listStateVersionOutputs` | List the Terraform outputs recorded in a state version. |
| List State Versions | `listStateVersions` | List the state versions of a workspace. The workspace and organization filters are both required. |
| List Team Access To Project | `listProjectTeamAccess` | List the teams that have access to a project and the level of access each has. |
| List Team Access To Workspace | `listTeamAccess` | List the teams that have access to a workspace and the level of access each has. |
| List Team Notification Configurations | `listTeamNotificationConfigurations` | List the notification configurations of a team. |
| List Team Tokens | `listTeamTokens` | List the authentication tokens of the teams in an organization. |
| List Teams | `listTeams` | List the teams in an organization. Managing multiple teams is a paid feature. |
| List User Tokens | `listUserTokens` | List the authentication tokens of a user. A token can only list its own user's tokens. |
| List Variable Set Variables | `listVariableSetVariables` | List the variables that belong to a variable set. |
| List VCS Connections | `listOAuthClients` | List the VCS connections (OAuth clients) of an organization. |
| List VCS Events | `listVcsEvents` | List the VCS events recorded for an organization. Only available for GitHub App connections. |
| List VCS OAuth Tokens | `listOAuthTokens` | List the OAuth tokens of a VCS connection. |
| List Workspace Notification Configurations | `listWorkspaceNotificationConfigurations` | List the notification configurations of a workspace. |
| List Workspace Remote State Consumers | `listWorkspaceRemoteStateConsumers` | List the workspaces that are allowed to read this workspace's remote state. |
| List Workspace Resources | `listWorkspaceResources` | List the infrastructure resources currently managed by a workspace, as recorded in its state. |
| List Workspace Run Tasks | `listWorkspaceRunTasks` | List the run tasks attached to a workspace. Run tasks are a paid feature. |
| List Workspace Runs | `listWorkspaceRuns` | List the runs in a workspace, most recent first. |
| List Workspace Tags | `listWorkspaceTags` | List the tags applied to a workspace. |
| List Workspace Variable Sets | `listWorkspaceVariableSets` | List the variable sets applied to a workspace. |
| List Workspace Variables | `listWorkspaceVariables` | List all Terraform and environment variables defined on a workspace. |
| List Workspaces | `listWorkspaces` | List the workspaces in an organization, optionally filtered by name, tags, or project. |
| Lock Workspace | `lockWorkspace` | Lock a workspace so no new runs can be queued against it. |
| Move Workspaces Into Project | `moveWorkspacesToProject` | Move one or more workspaces into a destination project. |
| Override Policy Check | `overridePolicyCheck` | Override a soft-mandatory policy check that failed, allowing the run to proceed. Policy enforcement is a paid feature. |
| Override Run Task Stage | `overrideTaskStage` | Override a failed advisory or mandatory run task stage so the run can proceed. Run tasks are a paid feature. |
| Permanently Delete Configuration Version | `permanentlyDeleteConfigurationVersion` | Permanently delete the backing data of a soft-deleted configuration version. Requires a data retention policy. |
| Permanently Delete State Version | `permanentlyDeleteStateVersion` | Permanently delete the backing data of a soft-deleted state version. Requires a data retention policy. |
| Remove Policies From Policy Set | `removePoliciesFromPolicySet` | Remove one or more policys from a policy set. |
| Remove Policy Set Workspace Exclusions | `removePolicySetWorkspaceExclusions` | Stop excluding one or more workspaces from a policy set. |
| Remove Team Members By Organization Membership | `removeTeamMembersByMembership` | Remove one or more users from a team, identified by organization membership ID. Users added by username must already be organization members. |
| Remove Team Members By Username | `removeTeamMembersByUser` | Remove one or more users from a team, identified by username. Users added by username must already be organization members. |
| Remove User From Organization | `deleteOrganizationMembership` | Remove a user from an organization, or revoke a pending invitation. |
| Remove Variable Set From Projects | `removeVariableSetFromProjects` | Remove a variable set from one or more projects. |
| Remove Variable Set From Workspaces | `removeVariableSetFromWorkspaces` | Remove a variable set from one or more workspaces. |
| Remove Workspace Remote State Consumers | `deleteWorkspaceRemoteStateConsumers` | Revoke remote state access for one or more consuming workspaces. |
| Remove Workspace Tags | `removeWorkspaceTags` | Remove one or more tags from a workspace. |
| Replace Workspace Remote State Consumers | `updateWorkspaceRemoteStateConsumers` | Replace the complete set of workspaces allowed to read this workspace's remote state. |
| Restore Configuration Version | `restoreConfigurationVersion` | Restore the soft-deleted backing data of a configuration version. Requires a data retention policy. |
| Restore State Version | `restoreStateVersion` | Restore the soft-deleted backing data of a state version. Requires a data retention policy. |
| Revoke Team Access To Project | `deleteProjectTeamAccess` | Revoke a team's access to a project. |
| Revoke Team Access To Workspace | `deleteTeamAccess` | Revoke a team's access to a workspace. |
| Rollback State Version | `rollbackStateVersion` | Roll a workspace back to a previous state version by creating a new state version from it. The workspace must be locked by the same token. |
| Safe Delete Workspace | `safeDeleteWorkspace` | Delete a workspace only if it is not managing any infrastructure. Fails if the workspace still has resources under management. |
| Safe Delete Workspace By Name | `safeDeleteWorkspaceByName` | Delete a workspace by organization and name only if it is not managing any infrastructure. |
| Set Organization Data Retention Policy | `setDataRetentionPolicy` | Create or update the data retention policy of an organization. Data retention policies are a paid feature. |
| Set Workspace Data Retention Policy | `setWorkspaceDataRetentionPolicy` | Create or update the data retention policy of a workspace. Data retention policies are a paid feature. |
| Soft Delete Configuration Version | `softDeleteConfigurationVersion` | Mark the backing data of a configuration version for garbage collection. Requires a data retention policy. |
| Soft Delete State Version | `softDeleteStateVersion` | Mark the backing data of a state version for garbage collection. Requires a data retention policy. |
| Unlock Workspace | `unlockWorkspace` | Unlock a workspace that was locked by the current user or token. |
| Update Account | `updateAccount` | Update the username and email address of the user account the API token belongs to. |
| Update Agent Pool | `updateAgentPool` | Update the name or scope of an agent pool. Agents are a paid feature. |
| Update GPG Key | `updateGpgKey` | Move a GPG key to a different registry namespace. |
| Update Notification Configuration | `updateNotificationConfiguration` | Update the name, triggers, destination or enabled state of a notification configuration. |
| Update Organization | `updateOrganization` | Update settings for an existing organization. All listed fields are sent, so provide the current values for fields you do not intend to change. |
| Update Policy | `updatePolicy` | Update the description, query or enforcement level of a policy. The name cannot be changed. |
| Update Policy Set | `updatePolicySet` | Update the attributes or VCS configuration of a policy set. |
| Update Policy Set Parameter | `updatePolicySetParameter` | Update a parameter of a policy set. |
| Update Project | `updateProject` | Update the name, description or default settings of an existing project. |
| Update Project Tag Bindings | `updateProjectTagBindings` | Add or update the tags bound to a project. Send the complete set of tag bindings to apply. |
| Update Registry Module | `updateRegistryModule` | Update the VCS configuration or no-code settings of a private registry module. |
| Update Registry Module Version | `updateRegistryModuleVersion` | Deprecate or reinstate a version of a private registry module. |
| Update Reserved Tag Key | `updateReservedTagKey` | Update a reserved tag key. |
| Update Run Task | `updateRunTask` | Update the endpoint, description or enabled state of a run task. |
| Update SSH Key | `updateSshKey` | Update the name or private key value of an SSH key. |
| Update Team | `updateTeam` | Update the name, visibility or organization access of a team. |
| Update Team Access To Project | `updateProjectTeamAccess` | Update the access level a team has on a project. |
| Update Team Access To Workspace | `updateTeamAccess` | Update the access level a team has on a workspace. |
| Update Variable Set | `updateVariableSet` | Update the attributes or assignments of an existing variable set. |
| Update Variable Set Variable | `updateVariableSetVariable` | Update a variable that belongs to a variable set. |
| Update VCS Connection | `updateOAuthClient` | Update the credentials or scope of a VCS connection (OAuth client). |
| Update VCS OAuth Token | `updateOAuthToken` | Set the SSH key of a VCS OAuth token, used to clone private submodules. |
| Update Workspace | `updateWorkspace` | Update a workspace by its ID. All listed fields are sent, so supply the current values for any you do not intend to change. |
| Update Workspace Run Task | `updateWorkspaceRunTask` | Update the enforcement level or stages of a run task attached to a workspace. |
| Update Workspace Tag Bindings | `updateWorkspaceTagBindings` | Add or update the key/value tag bindings on a workspace. |
| Update Workspace Variable | `updateWorkspaceVariable` | Update an existing variable on a workspace. Only the attributes you supply are changed. |
| Upload Policy Code | `uploadPolicy` | Upload the policy code for a policy. Send the raw Sentinel or Rego source as the request body. |
| Verify Notification Configuration | `verifyNotificationConfiguration` | Send a verification request to a notification configuration's destination and record the response. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Assessment Check Failure | `assessment:check_failure` | A health assessment check failed. |
| Assessment Drifted | `assessment:drifted` | A health assessment detected drift. |
| Assessment Failed | `assessment:failed` | A health assessment failed to complete. |
| Run Applying | `run:applying` | A run entered the applying phase. |
| Run Completed | `run:completed` | A run completed successfully. |
| Run Created | `run:created` | A run was created. |
| Run Errored | `run:errored` | A run errored. |
| Run Needs Attention | `run:needs_attention` | A run needs manual attention (e.g. a plan awaiting confirmation). |
| Run Planning | `run:planning` | A run entered the planning phase. |
| Workspace Auto Destroy Reminder | `workspace:auto_destroy_reminder` | A reminder that scheduled auto-destroy is approaching for the workspace. |
| Workspace Auto Destroy Run Results | `workspace:auto_destroy_run_results` | The results of a scheduled auto-destroy run for the workspace. |
