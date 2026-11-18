---
description: "GitLab REST API v4 (default base https://gitlab.com, configurable for self-managed)."
hidden: true
---

# GitLab

GitLab REST API v4 (default base https://gitlab.com, configurable for self-managed). Manage projects, issues, merge requests, branches, commits, repository files, tags, pipelines, jobs, labels, milestones, notes/comments, users, groups, and project webhooks (hooks). Auth: Bearer personal/project access token; set baseUrl for self-managed instances.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [gitlab.com](https://gitlab.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Actions** | 35 |
| **Events** | 10 |
| **Slug** | `gitlab` |

## Use it

Add GitLab from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.gitlab.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Branch | `createBranch` | Create a branch from a ref (POST /projects/{id}/repository/branches). |
| Create Commit | `createCommit` | Create a commit with multiple file actions (POST /projects/{id}/repository/commits). |
| Create Issue | `createIssue` | Create an issue in a project (POST /projects/{id}/issues). |
| Create Issue Note | `createIssueNote` | Add a note (comment) to an issue (POST /projects/{id}/issues/{iid}/notes). |
| Create Label | `createLabel` | Create a project label (POST /projects/{id}/labels). |
| Create Merge Request | `createMergeRequest` | Create a merge request (POST /projects/{id}/merge_requests). |
| Create Pipeline | `createPipeline` | Trigger a new pipeline on a ref (POST /projects/{id}/pipeline). |
| Create Project | `createProject` | Create a project (POST /projects). |
| Create Project Hook | `createProjectHook` | Create a project webhook (POST /projects/{id}/hooks). Used by the webhook config subscription code; per-event flags toggle delivery. |
| Create Repository File | `createRepositoryFile` | Create a new file in the repository (POST /projects/{id}/repository/files/{file_path}). |
| Delete Branch | `deleteBranch` | Delete a branch (DELETE /projects/{id}/repository/branches/{branch}). Returns 204. |
| Delete Project | `deleteProject` | Delete a project (DELETE /projects/{id}). Returns 202. |
| Delete Project Hook | `deleteProjectHook` | Delete a project webhook (DELETE /projects/{id}/hooks/{hook_id}). Returns 204. |
| Delete Repository File | `deleteRepositoryFile` | Delete a file (DELETE /projects/{id}/repository/files/{file_path}). Returns 204. |
| Get Current User | `getCurrentUser` | Get the authenticated user (GET /user). |
| Get Issue | `getIssue` | Get a project issue by IID (GET /projects/{id}/issues/{iid}). |
| Get Merge Request | `getMergeRequest` | Get a merge request by IID (GET /projects/{id}/merge_requests/{iid}). |
| Get Project | `getProject` | Get a project by ID or URL-encoded path (GET /projects/{id}). |
| Get Repository File | `getRepositoryFile` | Get a file's metadata and base64 content (GET /projects/{id}/repository/files/{file_path}). |
| List Branches | `listBranches` | List repository branches (GET /projects/{id}/repository/branches). |
| List Commits | `listCommits` | List repository commits (GET /projects/{id}/repository/commits). |
| List Groups | `listGroups` | List groups visible to the user (GET /groups). |
| List Issue Notes | `listIssueNotes` | List notes (comments) on an issue (GET /projects/{id}/issues/{iid}/notes). |
| List Issues | `listIssues` | List issues in a project (GET /projects/{id}/issues). |
| List Labels | `listLabels` | List project labels (GET /projects/{id}/labels). |
| List Merge Requests | `listMergeRequests` | List merge requests in a project (GET /projects/{id}/merge_requests). |
| List Pipelines | `listPipelines` | List pipelines for a project (GET /projects/{id}/pipelines). |
| List Project Hooks | `listProjectHooks` | List project webhooks (GET /projects/{id}/hooks). |
| List Projects | `listProjects` | List projects visible to the user (GET /projects). |
| List Repository Tree | `listRepositoryTree` | List files and directories in a project repository tree. Returns blobs (files) and trees (directories) for a given ref and path. Supports recursive listing. |
| List Users | `listUsers` | List users (GET /users). |
| Merge Merge Request | `mergeMergeRequest` | Accept and merge a merge request (PUT /projects/{id}/merge_requests/{iid}/merge). |
| Update Issue | `updateIssue` | Update or close an issue (PUT /projects/{id}/issues/{iid}). Use state_event close/reopen. |
| Update Project | `updateProject` | Update a project (PUT /projects/{id}). |
| Update Repository File | `updateRepositoryFile` | Update an existing file (PUT /projects/{id}/repository/files/{file_path}). |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Deployment | `deployment` | A deployment status changed. |
| Issue | `issue` | Issue created, updated, closed, or reopened. |
| Job | `job` | A CI job status changed. |
| Merge Request | `merge_request` | MR created, updated, merged, or closed. |
| Note (Comment) | `note` | A comment was added to a commit, issue, MR, or snippet. |
| Pipeline | `pipeline` | Pipeline status changed. |
| Push | `push` | Code pushed to the repository. |
| Release | `release` | A release was created or updated. |
| Tag Push | `tag_push` | A tag was pushed. |
| Wiki Page | `wiki_page` | A wiki page was created, updated, or deleted. |
