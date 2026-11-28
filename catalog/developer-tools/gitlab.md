---
description: "GitLab is a platform for code hosting and CI/CD. Manage projects, issues, merge requests, branches, commits, files and pipelines."
hidden: true
---

# GitLab

<img src="../../.gitbook/assets/connectors/lg/gitlab.png" alt="GitLab logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [gitlab.com](https://gitlab.com) |
| **Authentication** | OAuth 2.0, Personal access token |
| **Slug** | `gitlab` |

## Setup

Your customers sign in to GitLab through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect GitLab from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **GitLab**.
2. Select **Connect** on the GitLab card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. GitLab offers more than one sign-in method. Choose one in **Auth Method**, then:

   * For a key or credential method, fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

     <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

   * For OAuth 2.0, keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to GitLab and approve access in the window that opens.

     <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use GitLab's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Branch</td><td><code>createBranch</code></td><td>Create a branch from a ref</td></tr><tr><td>Create Commit</td><td><code>createCommit</code></td><td>Create a commit with multiple file actions</td></tr><tr><td>Create Issue</td><td><code>createIssue</code></td><td>Create an issue in a project</td></tr><tr><td>Create Issue Note</td><td><code>createIssueNote</code></td><td>Add a note (comment) to an issue</td></tr><tr><td>Create Label</td><td><code>createLabel</code></td><td>Create a project label</td></tr><tr><td>Create Merge Request</td><td><code>createMergeRequest</code></td><td>Create a merge request</td></tr><tr><td>Create Pipeline</td><td><code>createPipeline</code></td><td>Trigger a new pipeline on a ref</td></tr><tr><td>Create Project</td><td><code>createProject</code></td><td>Create a project</td></tr><tr><td>Create Project Hook</td><td><code>createProjectHook</code></td><td>Create a project webhook Used by the webhook config subscription code; per-event flags toggle delivery.</td></tr><tr><td>Create Repository File</td><td><code>createRepositoryFile</code></td><td>Create a new file in the repository</td></tr></tbody></table>

<details>

<summary>View 25 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Branch</td><td><code>deleteBranch</code></td><td>Delete a branch</td></tr><tr><td>Delete Project</td><td><code>deleteProject</code></td><td>Delete a project</td></tr><tr><td>Delete Project Hook</td><td><code>deleteProjectHook</code></td><td>Delete a project webhook</td></tr><tr><td>Delete Repository File</td><td><code>deleteRepositoryFile</code></td><td>Delete a file</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Get the authenticated user</td></tr><tr><td>Get Issue</td><td><code>getIssue</code></td><td>Get a project issue by IID</td></tr><tr><td>Get Merge Request</td><td><code>getMergeRequest</code></td><td>Get a merge request by IID</td></tr><tr><td>Get Project</td><td><code>getProject</code></td><td>Get a project by ID or URL-encoded path</td></tr><tr><td>Get Repository File</td><td><code>getRepositoryFile</code></td><td>Get a file's metadata and base64 content</td></tr><tr><td>List Branches</td><td><code>listBranches</code></td><td>List repository branches</td></tr><tr><td>List Commits</td><td><code>listCommits</code></td><td>List repository commits</td></tr><tr><td>List Groups</td><td><code>listGroups</code></td><td>List groups visible to the user</td></tr><tr><td>List Issue Notes</td><td><code>listIssueNotes</code></td><td>List notes (comments) on an issue</td></tr><tr><td>List Issues</td><td><code>listIssues</code></td><td>List issues in a project</td></tr><tr><td>List Labels</td><td><code>listLabels</code></td><td>List project labels</td></tr><tr><td>List Merge Requests</td><td><code>listMergeRequests</code></td><td>List merge requests in a project</td></tr><tr><td>List Pipelines</td><td><code>listPipelines</code></td><td>List pipelines for a project</td></tr><tr><td>List Project Hooks</td><td><code>listProjectHooks</code></td><td>List project webhooks</td></tr><tr><td>List Projects</td><td><code>listProjects</code></td><td>List projects visible to the user</td></tr><tr><td>List Repository Tree</td><td><code>listRepositoryTree</code></td><td>List files and directories in a project repository tree. Returns blobs (files) and trees (directories) for a given ref and path. Supports recursive listing.</td></tr><tr><td>List Users</td><td><code>listUsers</code></td><td>List users</td></tr><tr><td>Merge Merge Request</td><td><code>mergeMergeRequest</code></td><td>Accept and merge a merge request</td></tr><tr><td>Update Issue</td><td><code>updateIssue</code></td><td>Update or close an issue Use state_event close/reopen.</td></tr><tr><td>Update Project</td><td><code>updateProject</code></td><td>Update a project</td></tr><tr><td>Update Repository File</td><td><code>updateRepositoryFile</code></td><td>Update an existing file</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Deployment</td><td><code>deployment</code></td><td>A deployment status changed.</td></tr><tr><td>Issue</td><td><code>issue</code></td><td>Issue created, updated, closed, or reopened.</td></tr><tr><td>Job</td><td><code>job</code></td><td>A CI job status changed.</td></tr><tr><td>Merge Request</td><td><code>merge_request</code></td><td>MR created, updated, merged, or closed.</td></tr><tr><td>Note (Comment)</td><td><code>note</code></td><td>A comment was added to a commit, issue, MR, or snippet.</td></tr><tr><td>Pipeline</td><td><code>pipeline</code></td><td>Pipeline status changed.</td></tr><tr><td>Push</td><td><code>push</code></td><td>Code pushed to the repository.</td></tr><tr><td>Release</td><td><code>release</code></td><td>A release was created or updated.</td></tr><tr><td>Tag Push</td><td><code>tag_push</code></td><td>A tag was pushed.</td></tr><tr><td>Wiki Page</td><td><code>wiki_page</code></td><td>A wiki page was created, updated, or deleted.</td></tr></tbody></table>
