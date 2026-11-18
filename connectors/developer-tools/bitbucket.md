---
description: "Bitbucket Cloud (Atlassian) REST API v2.0 connector."
hidden: true
---

# Bitbucket

<img src="../../.gitbook/assets/connectors/bitbucket.png" alt="Bitbucket logo" width="64">

Bitbucket Cloud (Atlassian) REST API v2.0 connector. Manage workspaces, repositories, pull requests, issues, commits, refs/branches/tags, source, pipelines, snippets, projects, deploy keys, branch restrictions, downloads, and webhooks. Base URL https://api.bitbucket.org/2.0.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [bitbucket.org](https://bitbucket.org) |
| **Authentication** | Basic auth, OAuth 2.0 |
| **Slug** | `bitbucket` |

## Use it

Add Bitbucket from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bitbucket.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Default Reviewer | `addDefaultReviewer` | Add a user as a default reviewer on a repository. Requires repository:admin scope. target_username is the user's account UUID or selected user identifier. |
| Add Project Default Reviewer | `addProjectDefaultReviewer` | Add a user as a default reviewer for every pull request on every repository in a project. |
| Add User GPG Key | `createUserGpgKey` | Add a GPG public key to a user account so Bitbucket can show commits signed with it as verified. |
| Approve Commit | `approveCommit` | Approve a commit as the authenticated user. |
| Approve Pull Request | `approvePullRequest` | Approve a pull request as the authenticated user. POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve |
| Compare Two Commits (Diff Stat) | `compareCommitsDiffstat` | Return the diff stat (files changed, lines added/removed) between two commits, branches, or tags. |
| Compare Two Commits (Diff) | `compareCommitsDiff` | Return the raw diff between two commits, branches, or tags. Use spec formatted as "target..source" (e.g. main..feature-branch). |
| Create Branch | `createBranch` | Create a new branch pointing at a target commit/branch. POST /2.0/repositories/{workspace}/{repo_slug}/refs/branches |
| Create Branch Restriction | `createBranchRestriction` | Create a branch restriction. POST /2.0/repositories/{workspace}/{repo_slug}/branch-restrictions |
| Create Commit Comment | `createCommitComment` | Add a comment to a commit. POST /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/comments |

<details>

<summary>See 177 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Deploy Key | `createDeployKey` | Add a deploy key to a repository. POST /2.0/repositories/{workspace}/{repo_slug}/deploy-keys |
| Create Deployment Environment Variable | `createDeploymentVariable` | Create a variable on a deployment environment. Requires pipeline:variable scope. |
| Create Pipeline Schedule | `createPipelineSchedule` | Create a pipeline schedule for a repository. Requires pipeline:write scope. |
| Create Project | `createProject` | Create a new project in a workspace. POST /2.0/workspaces/{workspace}/projects |
| Create Pull Request | `createPullRequest` | Create a pull request. POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests |
| Create Pull Request Comment | `createPullRequestComment` | Add a comment to a pull request. POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments |
| Create Pull Request Task | `createPullRequestTask` | Create a to-do task on a pull request, optionally attached to a specific comment. |
| Create Repository | `createRepository` | Create a new repository in a workspace. POST /2.0/repositories/{workspace}/{repo_slug} |
| Create Repository Environment | `createRepositoryEnvironment` | Create a deployment environment for a repository. Requires repository:admin scope. |
| Create Repository Pipeline Variable | `createRepoPipelineVariable` | Create a repository-level pipeline variable. Requires pipeline:variable scope. |
| Create Repository Runner | `createRepositoryRunner` | Create/register a pipeline runner against a repository. Requires runner:write scope. |
| Create Snippet | `createSnippet` | Create a snippet under a workspace. POST /2.0/snippets/{workspace}. Files are sent as multipart form data; pass title and is_private. |
| Create Source File Commit | `createSrcFileCommit` | Create a commit by uploading a file to the repository source. Uses application/x-www-form-urlencoded with message, branch, and a file path key whose value is the file content. Required to seed a default branch and commit pipeline configs. |
| Create Tag | `createTag` | Create a new tag pointing at a target commit. POST /2.0/repositories/{workspace}/{repo_slug}/refs/tags |
| Create User SSH Key | `createUserSshKey` | Add an SSH key to a user account. Requires account:write scope. |
| Create Webhook | `createWebhook` | Create a webhook subscription on a repository. POST /2.0/repositories/{workspace}/{repo_slug}/hooks. Used by webhook subscription code. |
| Create Workspace Pipeline Variable | `createWorkspacePipelineVariable` | Create a workspace-level pipeline variable. Requires pipeline:variable scope. |
| Create Workspace Runner | `createWorkspaceRunner` | Create/register a pipeline runner against a workspace. Requires runner:write scope. |
| Create Workspace Webhook | `createWorkspaceWebhook` | Create a workspace-level webhook subscription. POST /2.0/workspaces/{workspace}/hooks |
| Decline Pull Request | `declinePullRequest` | Decline (reject) a pull request. POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/decline |
| Delete Branch | `deleteBranch` | Delete a branch. DELETE /2.0/repositories/{workspace}/{repo_slug}/refs/branches/{name}. Returns 204. |
| Delete Branch Restriction | `deleteBranchRestriction` | Delete a branch restriction by ID. Requires repository:admin scope. Returns 204. |
| Delete Commit Comment | `deleteCommitComment` | Delete a comment on a commit. |
| Delete Deploy Key | `deleteDeployKey` | Delete a repository deploy key by ID. Requires repository:admin scope. Returns 204. |
| Delete Deployment Environment Variable | `deleteDeploymentVariable` | Delete a deployment environment variable by UUID. Requires pipeline:variable scope. Returns 204. |
| Delete Download Artifact | `deleteDownloadArtifact` | Delete a download artifact from a repository's Downloads section. |
| Delete Pipeline Schedule | `deletePipelineSchedule` | Delete a pipeline schedule by UUID. Requires pipeline:write scope. Returns 204. |
| Delete Project | `deleteProject` | Delete a project. DELETE /2.0/workspaces/{workspace}/projects/{project_key}. Returns 204 No Content. |
| Delete Pull Request Comment | `deletePullRequestComment` | Delete a pull request comment. |
| Delete Pull Request Task | `deletePullRequestTask` | Delete a to-do task from a pull request. |
| Delete Repository | `deleteRepository` | Delete a repository. DELETE /2.0/repositories/{workspace}/{repo_slug}. Returns 204. |
| Delete Repository Environment | `deleteRepositoryEnvironment` | Delete a deployment environment by UUID. Requires repository:admin scope. Returns 204. |
| Delete Repository Group Permission Config | `deleteRepoGroupPermissionConfig` | Remove a group's explicit access grant from a repository. |
| Delete Repository Pipeline Variable | `deleteRepoPipelineVariable` | Delete a repository-level pipeline variable by UUID. Requires pipeline:variable scope. Returns 204. |
| Delete Repository Runner | `deleteRepositoryRunner` | Delete a repository pipeline runner by UUID. Requires runner:write scope. Returns 204. |
| Delete Repository User Permission | `deleteRepositoryUserPermission` | Remove a user's explicit permission from a repository. Requires repository:admin scope. Returns 204. |
| Delete Snippet | `deleteSnippet` | Delete a snippet. DELETE /2.0/snippets/{workspace}/{encoded_id}. Returns 204. |
| Delete User GPG Key | `deleteUserGpgKey` | Remove a GPG key from a user account. |
| Delete User SSH Key | `deleteUserSshKey` | Delete an SSH key from a user account by UUID. Requires account:write scope. Returns 204. |
| Delete Webhook | `deleteWebhook` | Delete a webhook subscription. DELETE /2.0/repositories/{workspace}/{repo_slug}/hooks/{uid}. Returns 204. Used by webhook unsubscription code. |
| Delete Workspace Pipeline Variable | `deleteWorkspacePipelineVariable` | Delete a workspace-level pipeline variable by UUID. Requires pipeline:variable scope. Returns 204. |
| Delete Workspace Runner | `deleteWorkspaceRunner` | Delete a workspace pipeline runner by UUID. Requires runner:write scope. Returns 204. |
| Delete Workspace Webhook | `deleteWorkspaceWebhook` | Delete a workspace-level webhook subscription. DELETE /2.0/workspaces/{workspace}/hooks/{uid}. Returns 204. |
| Fork Repository | `forkRepository` | Create a fork of a repository. Optionally target a workspace and new name. |
| Get Branch | `getBranch` | Get a single branch by name. GET /2.0/repositories/{workspace}/{repo_slug}/refs/branches/{name} |
| Get Branch Restriction | `getBranchRestriction` | Get a single branch restriction by ID. Requires repository:admin scope. |
| Get Branching Model | `getBranchingModel` | Get the branching model configured for a repository. GET /2.0/repositories/{workspace}/{repo_slug}/branching-model |
| Get Branching Model Settings | `getBranchingModelSettings` | Get the branching model configuration (development/production branch overrides, branch type prefixes) for a repository. |
| Get Commit | `getCommit` | Get a single commit by hash. GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit} |
| Get Commit Comment | `getCommitComment` | Get a single comment on a commit by id. |
| Get Current User | `getCurrentUser` | Get the currently authenticated user account. GET /2.0/user |
| Get Deploy Key | `getDeployKey` | Get a single repository deploy key by ID. Requires repository:admin scope. |
| Get Deployment | `getDeployment` | Get a single deployment by deployment UUID. |
| Get Download Artifact Link | `getDownloadArtifact` | Get the download link and metadata for a single download artifact on a repository. |
| Get Effective Branching Model | `getEffectiveBranchingModel` | Get the branching model actually applied to a repository, after merging repository and project-level overrides. |
| Get Merge Base | `getMergeBase` | Return the common ancestor commit between two commits, branches, or tags. |
| Get Pipeline | `getPipeline` | Get a pipeline run by UUID. GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid} |
| Get Pipeline Schedule | `getPipelineSchedule` | Get a pipeline schedule by UUID. Requires pipeline scope. |
| Get Pipeline Step | `getPipelineStep` | Get a single pipeline step by step UUID. |
| Get Pipeline Step Log | `getPipelineStepLog` | Get the log output of a pipeline step. GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/log. Returns raw log text. |
| Get Project | `getProject` | Get a project in a workspace by project key. GET /2.0/workspaces/{workspace}/projects/{project_key} |
| Get Project Branching Model | `getProjectBranchingModel` | Get the branching model configured at the project level, inherited by repositories that do not override it. |
| Get Project Branching Model Settings | `getProjectBranchingModelSettings` | Get the branching model configuration override stored on a project. |
| Get Project Default Reviewer | `getProjectDefaultReviewer` | Get a single default reviewer configured on a project. |
| Get Pull Request | `getPullRequest` | Get a single pull request. GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id} |
| Get Pull Request Comment | `getPullRequestComment` | Get a single pull request comment by comment id. |
| Get Pull Request Conflicts | `getPullRequestConflicts` | Return the list of file conflicts that would occur if this pull request were merged right now. |
| Get Pull Request Diff | `getPullRequestDiff` | Get the raw unified diff of a pull request. GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff. Returns text/plain. |
| Get Pull Request Diff Stat | `getPullRequestDiffstat` | Return the diff stat (files changed, lines added/removed per file) for a pull request, without the raw diff content. |
| Get Pull Request Merge Task Status | `getPullRequestMergeTaskStatus` | Poll the status of an asynchronous pull request merge task (merges can be queued when they involve large history rewrites). |
| Get Pull Request Patch | `getPullRequestPatch` | Return the pull request's changes as a raw git-format patch file that can be applied with git apply. |
| Get Pull Request Task | `getPullRequestTask` | Get a single to-do task on a pull request by id. |
| Get Raw File Content | `getRawFileContent` | Get the raw content of a single file at a ref. GET /2.0/repositories/{workspace}/{repo_slug}/src/{commit}/{path}. Returns the raw file body. |
| Get Repository | `getRepository` | Get a single repository. GET /2.0/repositories/{workspace}/{repo_slug} |
| Get Repository Environment | `getRepositoryEnvironment` | Get a single deployment environment by UUID. Requires repository scope. |
| Get Repository Group Permission Config | `getRepoGroupPermissionConfig` | Get the explicit access level granted to a specific group on a repository. |
| Get Repository Pipeline Variable | `getRepoPipelineVariable` | Get a single repository-level pipeline variable by UUID. Requires pipeline:variable scope. |
| Get Repository Runner | `getRepositoryRunner` | Get a single repository pipeline runner by UUID. Requires runner scope. |
| Get Repository Settings Inheritance | `getRepositoryOverrideSettings` | Get whether a repository inherits branch restrictions and merge checks from its project, or overrides them. |
| Get Snippet | `getSnippet` | Get a snippet by workspace and encoded ID. GET /2.0/snippets/{workspace}/{encoded_id} |
| Get Snippet Commit | `getSnippetCommit` | Get a specific snippet commit/revision. |
| Get Source Listing | `getSourceListing` | Browse the source tree (file/directory listing) at a ref and path. GET /2.0/repositories/{workspace}/{repo_slug}/src/{commit}/{path} |
| Get Tag | `getTag` | Get a single tag by name. |
| Get User | `getUser` | Get a user account by account ID or UUID. GET /2.0/users/{selected_user} |
| Get User Email | `getUserEmail` | Get details of a specific email address of the authenticated user. Requires email scope. |
| Get User GPG Key | `getUserGpgKey` | Get a single GPG key on a user account by fingerprint. |
| Get User Permission On Workspace | `getUserWorkspacePermission` | Get the authenticated user's permission level on a specific workspace. |
| Get User SSH Key | `getUserSshKey` | Get a single SSH key for a user by UUID. Requires account scope. |
| Get Webhook | `getWebhook` | Get a single webhook subscription. GET /2.0/repositories/{workspace}/{repo_slug}/hooks/{uid} |
| Get Workspace | `getWorkspace` | Get a single workspace by slug or UUID. GET /2.0/workspaces/{workspace} |
| Get Workspace GPG Public Key | `getWorkspaceGpgPublicKey` | Get the GPG public key(s) Bitbucket uses to sign commits made through this workspace's merge/web-edit actions. |
| Get Workspace Member | `getWorkspaceMember` | Get a single workspace member by user account UUID. Requires account scope / workspace membership. |
| Get Workspace Runner | `getWorkspaceRunner` | Get a single workspace pipeline runner by UUID. Requires runner scope. |
| Get Workspace Webhook | `getWorkspaceWebhook` | Get a single workspace-level webhook by uid. |
| List All Repositories | `listAllRepositories` | List repositories in a workspace. GET /2.0/repositories/{workspace}. Replaces deprecated unscoped GET /2.0/repositories (HTTP 410, CHANGE-2770). |
| List Branch Restrictions | `listBranchRestrictions` | List branch restrictions (permissions) for a repository. GET /2.0/repositories/{workspace}/{repo_slug}/branch-restrictions |
| List Branches | `listBranches` | List branches in a repository. GET /2.0/repositories/{workspace}/{repo_slug}/refs/branches |
| List Commit Comments | `listCommitComments` | List comments on a commit. GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/comments |
| List Commit Statuses | `listCommitStatuses` | List build statuses for a commit. GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses |
| List Commits | `listCommits` | List commits in a repository, optionally from a branch/tag/revision. GET /2.0/repositories/{workspace}/{repo_slug}/commits |
| List Current User Permissions Workspaces | `listUserPermissionsWorkspaces` | List the workspaces the authenticated user is a member of, with their permission level. GET /2.0/user/workspaces. Replaces deprecated GET /2.0/user/permissions/workspaces (HTTP 410, CHANGE-2770). |
| List Default Reviewers | `listDefaultReviewers` | List default reviewers configured on a repository. Requires repository:admin scope. |
| List Deploy Keys | `listDeployKeys` | List deploy keys (SSH) for a repository. GET /2.0/repositories/{workspace}/{repo_slug}/deploy-keys |
| List Deployment Environment Variables | `listDeploymentVariables` | List variables for a deployment environment. Requires pipeline:variable scope. |
| List Downloads | `listDownloads` | List download artifacts for a repository. GET /2.0/repositories/{workspace}/{repo_slug}/downloads |
| List Effective Default Reviewers | `listEffectiveDefaultReviewers` | List the effective default reviewers for a repository, combining reviewers set on the repository and on its project. |
| List Pipeline Schedules | `listPipelineSchedules` | List pipeline schedules for a repository. Requires pipeline scope. |
| List Pipeline Steps | `listPipelineSteps` | List the steps of a pipeline run. GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps |
| List Pipelines | `listPipelines` | List pipeline runs for a repository. GET /2.0/repositories/{workspace}/{repo_slug}/pipelines |
| List Project Default Reviewers | `listProjectDefaultReviewers` | List the default reviewers configured for a project; they are added to every pull request on every repository in the project. |
| List Pull Request Activity | `listPullRequestActivity` | List the activity log for a pull request (approvals, updates, comments). GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/activity |
| List Pull Request Comments | `listPullRequestComments` | List comments on a pull request. GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments |
| List Pull Request Commits | `listPullRequestCommits` | List commits on a pull request. GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/commits |
| List Pull Request Statuses | `listPullRequestStatuses` | List commit statuses (build statuses) associated with a pull request. |
| List Pull Request Tasks | `listPullRequestTasks` | List the to-do tasks attached to a pull request. |
| List Pull Requests | `listPullRequests` | List pull requests in a repository. GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests |
| List Pull Requests Containing Commit | `listPullRequestsForCommit` | List the pull requests that contain a given commit. |
| List Refs | `listRefs` | List all refs (branches and tags) in a repository. GET /2.0/repositories/{workspace}/{repo_slug}/refs |
| List Repositories In Workspace | `listRepositories` | List repositories in a workspace. GET /2.0/repositories/{workspace} |
| List Repository Deployments | `listRepositoryDeployments` | List deployments for a repository. Requires repository scope. |
| List Repository Environments | `listRepositoryEnvironments` | List deployment environments for a repository. Requires repository scope. |
| List Repository Forks | `listRepositoryForks` | List forks of a repository. GET /2.0/repositories/{workspace}/{repo_slug}/forks |
| List Repository Group Permissions | `listRepositoryGroupPermissions` | List explicit group permissions on a repository. Requires repository:admin scope. |
| List Repository Group Permissions Config | `listRepoGroupPermissionsConfig` | List the explicit group access grants configured on a repository. |
| List Repository Permissions For Workspace Repo | `listWorkspaceSingleRepoPermissions` | List the users and their permission level for a single repository within a workspace. |
| List Repository Pipeline Variables | `listRepoPipelineVariables` | List repository-level pipeline variables. Requires pipeline:variable scope. |
| List Repository Runners | `listRepositoryRunners` | List pipeline runners configured against a repository. Requires runner scope. |
| List Repository User Permissions | `listRepositoryUserPermissions` | List explicit user permissions on a repository. Requires repository:admin scope. |
| List Repository Watchers | `listRepositoryWatchers` | List users watching a repository. GET /2.0/repositories/{workspace}/{repo_slug}/watchers |
| List Snippet Comments | `listSnippetComments` | List comments on a snippet. |
| List Snippets | `listSnippets` | List snippets in a workspace. GET /2.0/snippets/{workspace}. Replaces deprecated unscoped GET /2.0/snippets (HTTP 410, CHANGE-2770). |
| List Subscribable Webhook Events | `listSubscribableWebhookEvents` | List the specific webhook event types available for a given subject type (repository, workspace, project, etc). |
| List Tags | `listTags` | List tags in a repository. GET /2.0/repositories/{workspace}/{repo_slug}/refs/tags |
| List User Emails | `listUserEmails` | List email addresses for the authenticated user. Requires email scope. |
| List User GPG Keys | `listUserGpgKeys` | List the GPG keys registered on a user account, used to verify signed commits. |
| List User SSH Keys | `listUserSshKeys` | List SSH keys for a user. Requires account scope. selected_user is the account UUID or username. |
| List Webhook Resource Types | `listWebhookResourceTypes` | List the resource types (repository, workspace, etc.) that support webhook subscriptions. |
| List Webhooks | `listWebhooks` | List webhook subscriptions on a repository. GET /2.0/repositories/{workspace}/{repo_slug}/hooks |
| List Workspace Members | `listWorkspaceMembers` | List all members of a workspace. GET /2.0/workspaces/{workspace}/members |
| List Workspace Permissions | `listWorkspacePermissions` | List the workspace memberships (users and their permission) for a workspace. Requires account scope / workspace membership. |
| List Workspace Pipeline Variables | `listWorkspacePipelineVariables` | List workspace-level pipeline variables. Requires pipeline:variable scope. |
| List Workspace Projects | `listWorkspaceProjects` | List projects in a workspace. GET /2.0/workspaces/{workspace}/projects |
| List Workspace Pull Requests For User | `listWorkspacePullRequestsForUser` | List the pull requests across every repository in a workspace that a given user authored, reviewed, or is a default reviewer on. |
| List Workspace Repository Permissions | `listWorkspaceRepositoryPermissions` | List the repository permissions for all users across a workspace. Requires account scope / workspace membership. |
| List Workspace Runners | `listWorkspaceRunners` | List pipeline runners configured against a workspace. Requires runner scope. |
| List Workspace Webhooks | `listWorkspaceWebhooks` | List workspace-level webhook subscriptions. GET /2.0/workspaces/{workspace}/hooks |
| List workspaces | `listWorkspaces` | List workspaces the authenticated user is a member of. Replaces deprecated GET /2.0/workspaces (HTTP 410). |
| Merge Pull Request | `mergePullRequest` | Merge a pull request. POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge |
| Remove Default Reviewer | `removeDefaultReviewer` | Remove a default reviewer from a repository. Requires repository:admin scope. Returns 204. |
| Remove Project Default Reviewer | `removeProjectDefaultReviewer` | Remove a user from a project's default reviewers. |
| Remove Pull Request Change Request | `removePullRequestChangeRequest` | Remove the authenticated user's "changes requested" status from a pull request. |
| Reopen Pull Request Comment Thread | `reopenPullRequestComment` | Reopen a previously resolved pull request comment thread. |
| Request Changes On Pull Request | `requestChangesPullRequest` | Mark a pull request as needing changes (request-changes). POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/request-changes |
| Resolve Pull Request Comment Thread | `resolvePullRequestComment` | Mark a pull request comment thread as resolved. |
| Search Code In Workspace | `searchCodeInWorkspace` | Full-text search source code across every repository in a workspace. |
| Set Build Status | `setBuildStatus` | Create a build status on a commit. POST /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build |
| Set Repository Settings Inheritance | `setRepositoryOverrideSettings` | Set whether a repository overrides its project's branch restrictions and branching model, instead of inheriting them. |
| Stop Pipeline | `stopPipeline` | Stop a running pipeline. POST /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/stopPipeline. Returns 204. |
| Trigger Pipeline | `triggerPipeline` | Trigger (run) a pipeline for a branch/commit/custom selector. POST /2.0/repositories/{workspace}/{repo_slug}/pipelines |
| Unapprove Commit | `unapproveCommit` | Remove the authenticated user's approval from a commit. |
| Unapprove Pull Request | `unapprovePullRequest` | Remove the authenticated user's approval. DELETE /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve. Returns 204. |
| Update Branch Restriction | `updateBranchRestriction` | Update a branch restriction by ID. Requires repository:admin scope. |
| Update Branching Model Settings | `updateBranchingModelSettings` | Update the branching model configuration for a repository. |
| Update Commit Comment | `updateCommitComment` | Update the text of a comment on a commit. |
| Update Pipeline Schedule | `updatePipelineSchedule` | Update a pipeline schedule by UUID. Requires pipeline:write scope. |
| Update Project | `updateProject` | Update an existing project. PUT /2.0/workspaces/{workspace}/projects/{project_key} |
| Update Pull Request | `updatePullRequest` | Update an open pull request (title, description, destination, reviewers). PUT /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id} |
| Update Pull Request Comment | `updatePullRequestComment` | Update the content of a pull request comment. |
| Update Pull Request Task | `updatePullRequestTask` | Update a pull request task's text or resolve/reopen it. |
| Update Repository | `updateRepository` | Update repository settings. PUT /2.0/repositories/{workspace}/{repo_slug} |
| Update Repository Group Permission Config | `updateRepoGroupPermissionConfig` | Grant or change a group's explicit access level on a repository. |
| Update Repository Pipeline Variable | `updateRepoPipelineVariable` | Update a repository-level pipeline variable by UUID. Requires pipeline:variable scope. |
| Update Repository User Permission | `updateRepositoryUserPermission` | Grant or update a user's explicit permission on a repository. Requires repository:admin scope. permission is one of read, write, admin. |
| Update Snippet | `updateSnippet` | Update a snippet (title and/or files) via multipart form. |
| Update Webhook | `updateWebhook` | Update a webhook subscription. PUT /2.0/repositories/{workspace}/{repo_slug}/hooks/{uid} |
| Update Workspace Pipeline Variable | `updateWorkspacePipelineVariable` | Update a workspace-level pipeline variable by UUID. Requires pipeline:variable scope. |
| Update Workspace Webhook | `updateWorkspaceWebhook` | Update a workspace-level webhook. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Build Status Created | `repo:commit_status_created` | A build status (commit status) is created on a commit. |
| Build Status Updated | `repo:commit_status_updated` | An existing build status (commit status) is updated. |
| Issue Comment Created | `issue:comment_created` | A comment is added to an issue. |
| Issue Created | `issue:created` | An issue is created in the repository issue tracker. |
| Issue Updated | `issue:updated` | An issue is updated (state, assignee, or content changes). |
| Pull Request Approval Removed | `pullrequest:unapproved` | A user removes their approval from a pull request. |
| Pull Request Approved | `pullrequest:approved` | A user approves a pull request. |
| Pull Request Comment Created | `pullrequest:comment_created` | A comment is added to a pull request. |
| Pull Request Created | `pullrequest:created` | A pull request is created. |
| Pull Request Declined | `pullrequest:rejected` | A pull request is declined. |

<details>

<summary>See 4 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Pull Request Merged | `pullrequest:fulfilled` | A pull request is merged. |
| Pull Request Updated | `pullrequest:updated` | A pull request's title, description, or destination changes, or commits are pushed to the source branch. |
| Repository Fork | `repo:fork` | A user forks a repository. |
| Repository Push | `repo:push` | A user pushes one or more commits to a repository. Event type carried in the X-Event-Key request header. |

</details>
