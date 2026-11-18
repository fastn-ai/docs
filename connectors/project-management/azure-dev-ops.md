---
description: "Azure DevOps — accounts and profile, projects, Git repositories, branches/refs, repository items (content) and commit changes, via the Azure DevOps REST API…"
---

# Azure DevOps

Azure DevOps — accounts and profile, projects, Git repositories, branches/refs, repository items (content) and commit changes, via the Azure DevOps REST API (dev.azure.com and app.vssps.visualstudio.com).

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [dev.azure.com](https://dev.azure.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 84 |
| **Events** | 0 |
| **Slug** | `azureDevOps` |

## Use it

Add Azure DevOps from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.azureDevOps.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Work Item Comment | `addWorkItemComment` | Adds a comment to the discussion of a work item. |
| Create Pull Request | `createPullRequest` | Creates a pull request from a source branch into a target branch of a Git repository. |
| Create Pull Request Thread | `createPullRequestThread` | Creates a new comment thread on a pull request with an initial comment. |
| Create Repository | `createRepository` | Creates a new, empty Git repository in a team project. |
| Create Service Hook Subscription | `createServiceHookSubscription` | Creates a web hook service hook subscription that posts an Azure DevOps event, such as git.push, to the given URL for a project. |
| Create Work Item | `createWorkItem` | Creates a work item of the given type with a title and description. Additional fields can be set afterwards with Update Work Item. |
| Delete Repository | `deleteRepository` | Deletes a Git repository, moving it to the project recycle bin. This removes the repository from the project and cannot be undone once purged. |
| Delete Service Hook Subscription | `deleteServiceHookSubscription` | Deletes a service hook subscription by its id, stopping further event deliveries. |
| Delete Work Item | `deleteWorkItem` | Deletes a work item, sending it to the project recycle bin. Set Destroy to true to remove it permanently, which cannot be undone. |
| Get Blob | `getBlob` | Retrieves the metadata of a Git blob (file object) by its SHA-1 object id. |
| Get Build | `getBuild` | Retrieves a single build by its numeric build id. |
| Get Build Definition | `getBuildDefinition` | Retrieves a single build definition by its numeric definition id. |
| Get Build Timeline | `getBuildTimeline` | Retrieves the timeline of a build, listing every stage, job and task with its state and result. |
| Get Commit | `getCommit` | Retrieves a single Git commit by its SHA-1 commit id, including author, committer and comment. |
| Get Commit Changes | `getCommitChanges` | Retrieves the file changes introduced by a specific Git commit. |
| Get Item | `getItem` | Retrieves metadata for a file or folder in a Git repository, and optionally its content, at a given path and version. |
| Get My Profile | `getMyProfile` | Retrieves the Azure DevOps profile of the currently authenticated user, including the public alias (id) required to look up the organizations that user belongs to. |
| Get Operation | `getOperation` | Retrieves the status of a long-running asynchronous operation, such as the project creation returned by Create Project. |
| Get Pipeline | `getPipeline` | Retrieves a single pipeline definition by its numeric pipeline id. |
| Get Pipeline Run | `getPipelineRun` | Retrieves a single pipeline run by its run id, including its state, result and resources. |
| Get Project | `getProject` | Retrieves a single team project in an Azure DevOps organization by its id or name, optionally including its capabilities and default team. |
| Get Project Properties | `getProjectProperties` | Retrieves the properties of a team project, such as its process template id and source control type. |
| Get Pull Request | `getPullRequest` | Retrieves a single pull request by its id, including source and target branches, reviewers and merge status. |
| Get Push | `getPush` | Retrieves a single push to a Git repository by its push id, including the ref updates it made. |
| Get Repository | `getRepository` | Retrieves a single Git repository by its id or name within a team project. |
| Get Team | `getTeam` | Retrieves a single team in a team project by its id or name. |
| Get Tree | `getTree` | Retrieves a Git tree object by its SHA-1 object id, listing the entries it contains. |
| Get Work Item | `getWorkItem` | Retrieves a single work item by its numeric id, including its fields, relations and links. |
| Get Work Item Type | `getWorkItemType` | Retrieves the definition of a single work item type in a project, including its fields and states. |
| List Agent Pools | `listAgentPools` | Lists the build and release agent pools configured in the organization. |
| List All Repositories | `listAllRepositories` | Lists every Git repository across all projects in an Azure DevOps organization. |
| List All Teams | `listAllTeams` | Lists every team across all projects in an Azure DevOps organization. |
| List Build Artifacts | `listBuildArtifacts` | Lists the artifacts produced by a build. |
| List Build Changes | `listBuildChanges` | Lists the source changes associated with a build. |
| List Build Definitions | `listBuildDefinitions` | Lists the build definitions in a team project. |
| List Build Logs | `listBuildLogs` | Lists the log files produced by a build. |
| List Builds | `listBuilds` | Lists the builds in a team project, optionally filtered by definition, status, result or branch. |
| List Classification Nodes - Areas | `listAreaPaths` | Lists the area path classification nodes of a team project, used to categorise work items by product area. |
| List Classification Nodes - Iterations | `listIterationPaths` | Lists the iteration path classification nodes of a team project, used to assign work items to sprints. |
| List Commits | `listCommits` | Lists the commits in a Git repository, optionally filtered by branch, author or item path. |
| List Graph Groups | `listGraphGroups` | Lists the groups in an Azure DevOps organization's identity graph. |
| List Graph Users | `listGraphUsers` | Lists the users in an Azure DevOps organization's identity graph. |
| List Items | `listItems` | Lists the files and folders under a path in a Git repository, recursing to the requested level. |
| List Organizations | `listOrganizations` | Lists the Azure DevOps organizations (accounts) that a given user is a member of. Pass the member's profile id, obtainable from Get My Profile. |
| List Pipeline Runs | `listPipelineRuns` | Lists the runs of a pipeline, newest first. |
| List Pipelines | `listPipelines` | Lists the pipelines defined in a team project. |
| List Policy Configurations | `listPolicyConfigurations` | Lists the branch policy configurations defined in a team project. |
| List Policy Types | `listPolicyTypes` | Lists the branch policy types available in a team project, such as minimum reviewers and build validation. |
| List Processes | `listProcesses` | Lists the work item process templates available in the organization, such as Agile, Scrum, Basic and CMMI. |
| List Projects | `listProjects` | Lists all team projects in an Azure DevOps organization that the authenticated user has access to. |
| List Pull Request Commits | `listPullRequestCommits` | Lists the commits included in a pull request. |
| List Pull Request Iterations | `listPullRequestIterations` | Lists the iterations (pushes of new commits) of a pull request. |
| List Pull Request Reviewers | `listPullRequestReviewers` | Lists the reviewers assigned to a pull request together with their vote. |
| List Pull Request Threads | `listPullRequestThreads` | Lists the comment threads on a pull request, including each thread's comments and status. |
| List Pull Request Work Items | `listPullRequestWorkItems` | Lists references to the work items linked to a pull request. |
| List Pull Requests | `listPullRequests` | Lists the pull requests of a Git repository, optionally filtered by status, creator, reviewer or target branch. |
| List Pull Requests By Project | `listPullRequestsByProject` | Lists pull requests across every Git repository in a team project. |
| List Pushes | `listPushes` | Lists the pushes made to a Git repository, newest first. |
| List Queries | `listQueries` | Lists the saved work item queries and query folders in a team project. |
| List Refs | `listRefs` | Lists the refs (branches and tags) of a Git repository. Use the filter input to narrow to a namespace such as 'heads/' for branches or 'tags/' for tags. |
| List Repositories | `listRepositories` | Lists the Git repositories in a team project. |
| List Service Endpoints | `listServiceEndpoints` | Lists the service connections (service endpoints) defined in a team project. |
| List Service Hook Consumers | `listServiceHookConsumers` | Lists the service hook consumers available in the organization, such as Web Hooks, Slack and Azure Storage. |
| List Service Hook Publishers | `listServiceHookPublishers` | Lists the service hook publishers and the event types each one can raise. |
| List Service Hook Subscriptions | `listServiceHookSubscriptions` | Lists the service hook subscriptions configured in an Azure DevOps organization. |
| List Team Members | `listTeamMembers` | Lists the members of a team, including whether each member is a team administrator. |
| List Teams In Project | `listTeams` | Lists all teams defined within a team project. |
| List Variable Groups | `listVariableGroups` | Lists the pipeline variable groups defined in a team project. |
| List Wikis | `listWikis` | Lists the wikis defined in a team project. |
| List Work Item Comments | `listWorkItemComments` | Lists the comments recorded on a work item. |
| List Work Item Fields | `listWorkItemFields` | Lists all work item fields defined in the organization, with their reference names and data types. |
| List Work Item Relation Types | `listWorkItemRelationTypes` | Lists the work item link (relation) types available in the organization, such as Parent, Child and Related. |
| List Work Item Revisions | `listWorkItemRevisions` | Lists every historical revision of a work item. |
| List Work Item Tags | `listWorkItemTags` | Lists the work item tags defined in a team project. |
| List Work Item Types | `listWorkItemTypes` | Lists the work item types available in a team project, such as Bug, Task, User Story and Epic. |
| List Work Item Updates | `listWorkItemUpdates` | Lists the field-level updates applied to a work item over its lifetime. |
| List Work Items | `listWorkItems` | Retrieves a batch of work items by their ids. Pass a comma-separated list of up to 200 work item ids. |
| Query Work Items By WIQL | `queryWorkItemsByWiql` | Runs a Work Item Query Language (WIQL) query and returns the matching work item references. Use List Work Items to fetch the full work items for the returned ids. |
| Queue Build | `queueBuild` | Queues a new build for a build definition on the specified source branch. |
| Run Pipeline | `runPipeline` | Queues a new run of a pipeline on the specified branch and returns the created run. |
| Update Pull Request | `updatePullRequest` | Updates a pull request, for example to change its title or description, or to complete or abandon it by setting the status. |
| Update Refs | `updateRefs` | Creates, updates or deletes a Git ref such as a branch. To create a branch set Old Object ID to forty zeros; to delete one set New Object ID to forty zeros. |
| Update Repository | `updateRepository` | Renames a Git repository or changes its default branch. |
| Update Work Item | `updateWorkItem` | Replaces the value of a single field on a work item, identified by its field reference name such as System.Title or System.State. |
