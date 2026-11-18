---
description: "Asana is a work management platform."
hidden: true
---

# Asana

<img src="../../.gitbook/assets/connectors/asana.png" alt="Asana logo" width="64">

Asana is a work management platform. Build, manage, and automate tasks, projects, goals, portfolios, teams, and workspaces via the Asana REST API v1.0.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [asana.com](https://asana.com) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Slug** | `asana` |

## Use it

Add Asana from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.asana.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Custom Field Setting to Portfolio | `addCustomFieldSettingForPortfolio` | Add a custom field to a portfolio. Returns the created custom field setting. |
| Add Custom Field Setting to Project | `addCustomFieldSettingForProject` | Add a custom field to a project. Returns the created custom field setting. |
| Add Dependencies | `addDependenciesForTask` | Mark a set of tasks as dependencies of the given task. Returns an empty data object. |
| Add Dependents | `addDependentsForTask` | Mark a set of tasks as dependents of the given task. Returns an empty data object. |
| Add Followers to Goal | `addFollowersForGoal` | Add followers to a goal. Returns the full goal. |
| Add Followers to Project | `addFollowersForProject` | Add followers to a project. Returns the full project. |
| Add Followers to Task | `addFollowersForTask` | Add followers to a task. Returns the full updated task. |
| Add Item to Portfolio | `addItemForPortfolio` | Add a project or portfolio item to a portfolio. Returns an empty data object. |
| Add Members to Portfolio | `addMembersForPortfolio` | Add members to a portfolio. Returns the full portfolio. |
| Add Members to Project | `addMembersForProject` | Add members to a project. Returns the full project. |

<details>

<summary>See 149 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Add Project to Task | `addProjectForTask` | Add the task to a project, optionally at a specific position or section. Returns an empty data object. |
| Add Supporting Relationship to Goal | `addSupportingRelationship` | Add a supporting resource (goal, project, task, or portfolio) to a goal. A goal gid yields a subgoal relationship; others yield supporting_work. Returns the goal relationship. |
| Add Tag to Task | `addTagForTask` | Add a tag to a task. Returns an empty data object. |
| Add Task to Section | `addTaskForSection` | Move a task into a section, optionally positioned relative to another task. Returns an empty data object. |
| Add User to Team | `addUserForTeam` | Add a user to a team. Returns the team membership record. |
| Add User to Workspace | `addUserForWorkspace` | Add a user to a workspace or organization. Returns the user's compact record. |
| Create a Membership | `createMembership` | Create a membership granting a user/team access to a goal, project, or portfolio. Returns the membership. |
| Create a Team | `createTeam` | Create a new team within an organization. Returns the team. |
| Create an Organization Export | `createOrganizationExport` | Start an export of a complete organization. Requires Super Admin. Returns the org export object; poll Get Organization Export for the download_url. |
| Create Comment on a Task | `createStoryForTask` | Add a comment (story) to a task. Provide text OR html_text, not both. Returns the created story. |
| Create Custom Field | `createCustomField` | Create a new custom field in a workspace. Returns the custom field. |
| Create Enum Option | `createEnumOptionForCustomField` | Create a new enum option for an enum/multi_enum custom field. Returns the enum option. |
| Create Goal | `createGoal` | Create a new goal in a workspace. For organizations a team is required. Returns the goal. |
| Create Portfolio | `createPortfolio` | Create a new portfolio in a workspace. Returns the portfolio. |
| Create Project | `createProject` | Create a new project in a workspace. For organizations a team is required. Returns the full project. |
| Create Project Brief | `createProjectBrief` | Create a project brief for a project. Provide html_text OR text. Returns the brief. |
| Create Project in Team | `createProjectForTeam` | Create a new project within a team (team taken from path). Returns the project. |
| Create Project in Workspace | `createProjectForWorkspace` | Create a new project within a workspace (workspace taken from path). Returns the project. |
| Create Section in Project | `createSectionForProject` | Create a new section in a project, optionally positioned relative to another section. Returns the section. |
| Create Status Update | `createStatusUpdate` | Create a status update on a project, portfolio, or goal. Returns the status update. |
| Create Subtask | `createSubtaskForTask` | Create a new subtask under the given parent task. Returns the full subtask record. |
| Create Tag | `createTag` | Create a new tag in a workspace. Returns the tag. |
| Create Tag in Workspace | `createTagForWorkspace` | Create a new tag within a specific workspace (workspace taken from the path). Returns the tag. |
| Create Task | `createTask` | Create a new task in a workspace, project, or as a subtask. A task must resolve a workspace via workspace, projects, or parent. Returns the full task object. |
| Delete a Membership | `deleteMembership` | Delete a membership. Returns an empty data object. |
| Delete a Status Update | `deleteStatusUpdate` | Delete a status update. Returns an empty data object. |
| Delete a Story | `deleteStory` | Delete a comment story. Only comment-type stories you authored can be deleted. Returns an empty data object. |
| Delete a Webhook | `deleteWebhook` | Delete (unregister) a webhook. Returns an empty data object. |
| Delete an Attachment | `deleteAttachment` | Delete an attachment. Returns an empty data object. |
| Delete Custom Field | `deleteCustomField` | Delete a custom field. Returns an empty data object. |
| Delete Goal | `deleteGoal` | Delete a goal. Returns an empty data object. |
| Delete Portfolio | `deletePortfolio` | Delete a portfolio. Returns an empty data object. |
| Delete Project | `deleteProject` | Delete a project. Returns an empty data object. |
| Delete Project Brief | `deleteProjectBrief` | Delete a project brief. Returns an empty data object. |
| Delete Project Template | `deleteProjectTemplate` | Delete a project template. Returns an empty data object. |
| Delete Section | `deleteSection` | Delete a section. The section must be empty, and the last section in a project cannot be deleted. Returns an empty data object. |
| Delete Tag | `deleteTag` | Delete a tag. Returns an empty data object. |
| Delete Task | `deleteTask` | Delete a task. The task is moved to the trash and is recoverable for 30 days. Returns an empty data object. |
| Duplicate Project | `duplicateProject` | Create a copy of a project. Returns a Job object whose new_project references the created project. |
| Duplicate Task | `duplicateTask` | Create a copy of a task. Returns a Job object whose new_task references the created task once the job completes. |
| Establish a Webhook | `createWebhook` | Register a webhook on a resource. Asana performs an X-Hook-Secret handshake against the target before returning the webhook. Returns the webhook. |
| Get a Goal Relationship | `getGoalRelationship` | Get the full record for a single goal relationship. |
| Get a Job by ID | `getJob` | Get the status of an asynchronous job (e.g. task/project duplication or template instantiation). |
| Get a Membership | `getMembership` | Get the full record for a single membership. |
| Get a Status Update | `getStatusUpdate` | Get the full record for a single status update. |
| Get a Story | `getStory` | Get the full record for a single story. |
| Get a Team | `getTeam` | Get the full record for a single team. |
| Get a Team Membership | `getTeamMembership` | Get the full record for a single team membership. |
| Get a Team's Projects | `getProjectsForTeam` | Get the compact project records for all projects in a team. |
| Get a User | `getUser` | Get the full record for a single user. The user_gid accepts 'me', an email, or a gid. |
| Get a User's Favorites | `getFavoritesForUser` | Get the user's favorites of a given resource type in a workspace. Both resource_type and workspace are required. Only returns favorites for the authenticated user. |
| Get a Webhook | `getWebhook` | Get the full record for a single webhook. |
| Get a Workspace | `getWorkspace` | Get the full record for a single workspace. |
| Get a Workspace Membership | `getWorkspaceMembership` | Get the full record for a single workspace membership. |
| Get an Attachment | `getAttachment` | Get the full record for a single attachment, including download/view URLs. |
| Get an Organization Export | `getOrganizationExport` | Get the details and state of an organization export. The download_url is populated once state is finished. |
| Get Attachments from an Object | `getAttachmentsForObject` | Get the compact records for all attachments on an object (task, project, or project_brief). The parent gid is required. |
| Get Current User | `getCurrentUser` | Get the full record for the currently authenticated user. |
| Get Custom Field | `getCustomField` | Get the full record for a single custom field. |
| Get Custom Fields in Workspace | `getCustomFieldsForWorkspace` | Get the compact custom field records in a workspace. |
| Get Dependencies | `getDependenciesForTask` | Get the compact representations of all tasks that the given task depends on. Requires a paid (premium) Asana plan; free workspaces get 402. |
| Get Dependents | `getDependentsForTask` | Get the compact representations of all tasks that depend on the given task. Requires a paid (premium) Asana plan; free workspaces get 402. |
| Get Events on a Resource | `getEvents` | Poll for events on a task or project. Omit sync on the first call (the API returns a 412 with a fresh sync token); pass the returned token on subsequent calls. |
| Get Goal | `getGoal` | Get the full record for a single goal. |
| Get Goal Relationships | `getGoalRelationships` | Get the compact goal relationship records for a supported goal. |
| Get Items in a Portfolio | `getItemsForPortfolio` | Get the compact records for all items (projects/portfolios) in a portfolio. |
| Get Memberships from a Project | `getProjectMembershipsForProject` | Get the compact project membership records for a project, optionally filtered by user. |
| Get Memberships from a Team | `getTeamMembershipsForTeam` | Get the compact team membership records for a team. |
| Get Memberships from a User | `getTeamMembershipsForUser` | Get the compact team membership records for a user in a workspace. The workspace param is required. |
| Get Multiple Goals | `getGoals` | Get the compact goal records, optionally filtered by workspace, team, project, task, or portfolio. Requires a paid (premium) Asana plan; free workspaces get 402. |
| Get Multiple Memberships | `getMemberships` | Get the compact membership records for a parent (goal/project/portfolio), optionally filtered by member. |
| Get Multiple Portfolios | `getPortfolios` | Get the compact portfolio records in a workspace. The workspace param is required. |
| Get Multiple Project Templates | `getProjectTemplates` | Get the compact project template records, optionally filtered by workspace or team. |
| Get Multiple Projects | `getProjects` | Get the compact project records, optionally filtered by workspace, team, or archived status. |
| Get Multiple Tags | `getTags` | Get the compact records for all tags, optionally filtered by workspace. |
| Get Multiple Tasks | `getTasks` | Get a list of tasks. You must filter by project, section, or (assignee + workspace). Returns compact task objects with pagination. |
| Get Multiple Users | `getUsers` | Get the compact user records, optionally filtered by workspace or team. |
| Get Multiple Webhooks | `getWebhooks` | Get the compact webhook records in a workspace. The workspace param is required. Optionally filter by resource. |
| Get Multiple Workspaces | `getWorkspaces` | Get the compact records for all workspaces visible to the authenticated user. |
| Get Parent Goals | `getParentGoalsForGoal` | Get the compact records for all parent goals of the given goal. |
| Get Portfolio | `getPortfolio` | Get the full record for a single portfolio. |
| Get Portfolio Custom Field Settings | `getCustomFieldSettingsForPortfolio` | Get the compact custom field settings for a portfolio. |
| Get Portfolio Memberships | `getPortfolioMembershipsForPortfolio` | Get the compact portfolio membership records for a portfolio. |
| Get Project | `getProject` | Get the complete record for a single project. |
| Get Project Brief | `getProjectBrief` | Get the full record for a single project brief. |
| Get Project Custom Field Settings | `getCustomFieldSettingsForProject` | Get the compact custom field settings for a project. Requires a paid (premium) Asana plan; free workspaces get 402. |
| Get Project Template | `getProjectTemplate` | Get the full record for a single project template. |
| Get Project Templates in Team | `getProjectTemplatesForTeam` | Get the compact project template records for a team. |
| Get Projects a Task Is In | `getProjectsForTask` | Get the compact project records for all projects the given task belongs to. |
| Get Projects in Workspace | `getProjectsForWorkspace` | Get the compact project records for all projects in a workspace. |
| Get Section | `getSection` | Get the complete record for a single section. |
| Get Sections in Project | `getSectionsForProject` | Get the compact records for all sections in the given project. |
| Get Status Updates | `getStatusUpdates` | Get the status updates for a parent object (project, portfolio, or goal). The parent gid is required. |
| Get Stories on a Task | `getStoriesForTask` | Get the compact records for all stories (comments and system updates) on a task. |
| Get Subtasks | `getSubtasksForTask` | Get the compact representation of all subtasks of a task. |
| Get Tag | `getTag` | Get the complete record for a single tag. |
| Get Tags in Workspace | `getTagsForWorkspace` | Get the compact records for all tags in a specific workspace. |
| Get Task | `getTask` | Get the complete record for a single task by its gid. Use opt_fields to expand related objects. |
| Get Task Count of a Project | `getTaskCountsForProject` | Get task counts for a project. You MUST request the count fields via opt_fields (e.g. num_tasks,num_incomplete_tasks,num_completed_tasks,num_milestones) — nothing is returned by default. |
| Get Tasks from a Project | `getTasksForProject` | Get the compact task records for all tasks within the given project. |
| Get Tasks from a Section | `getTasksForSection` | Get the compact task records for all tasks within the given section. |
| Get Tasks from a Tag | `getTasksForTag` | Get the compact task records for all tasks with the given tag. |
| Get Tasks from a User Task List | `getTasksForUserTaskList` | Get the compact list of tasks in a user's My Tasks list, identified by the user task list gid. |
| Get Team Memberships | `getTeamMemberships` | Get the compact team membership records. Filter by team alone, or by user + workspace. |
| Get Teams for a User | `getTeamsForUser` | Get the compact records for all teams a user is a member of within an organization. The organization param is required. |
| Get Teams in a Workspace | `getTeamsForWorkspace` | Get the compact records for all teams in a workspace visible to the authenticated user. |
| Get Users in a Team | `getUsersForTeam` | Get the compact user records for all members of a team. |
| Get Users in a Workspace | `getUsersForWorkspace` | Get the compact user records for all users in a workspace. |
| Get Workspace Memberships for a User | `getWorkspaceMembershipsForUser` | Get the compact workspace membership records for a user. |
| Get Workspace Memberships for a Workspace | `getWorkspaceMembershipsForWorkspace` | Get the compact workspace membership records for a workspace, optionally filtered by user. |
| Instantiate Project from Template | `instantiateProject` | Create a new project from a project template. Returns a Job whose new_project references the created project. |
| Move or Reorder Section | `insertSectionForProject` | Reorder a section within its project, positioning it before or after another section (exactly one of before_section/after_section). Returns an empty data object. |
| Remove Custom Field Setting from Portfolio | `removeCustomFieldSettingForPortfolio` | Remove a custom field from a portfolio. Returns an empty data object. |
| Remove Custom Field Setting from Project | `removeCustomFieldSettingForProject` | Remove a custom field from a project. Returns an empty data object. |
| Remove Dependencies | `removeDependenciesForTask` | Unlink a set of tasks as dependencies of the given task. Returns an empty data object. |
| Remove Dependents | `removeDependentsForTask` | Unlink a set of tasks as dependents of the given task. Returns an empty data object. |
| Remove Followers from Goal | `removeFollowersForGoal` | Remove followers from a goal. Returns the full goal. |
| Remove Followers from Project | `removeFollowersForProject` | Remove followers from a project. Returns the full project. |
| Remove Followers from Task | `removeFollowersForTask` | Remove followers from a task. Returns the full updated task. |
| Remove Item from Portfolio | `removeItemForPortfolio` | Remove an item from a portfolio. Returns an empty data object. |
| Remove Members from Portfolio | `removeMembersForPortfolio` | Remove members from a portfolio. Returns the full portfolio. |
| Remove Members from Project | `removeMembersForProject` | Remove members from a project. Returns the full project. |
| Remove Project from Task | `removeProjectForTask` | Remove the task from a project. Returns an empty data object. |
| Remove Supporting Relationship from Goal | `removeSupportingRelationship` | Remove a supporting resource from a goal. Returns an empty data object. |
| Remove Tag from Task | `removeTagForTask` | Remove a tag from a task. Returns an empty data object. |
| Remove User from Team | `removeUserForTeam` | Remove a user from a team. Returns an empty data object. |
| Remove User from Workspace | `removeUserForWorkspace` | Remove a user from a workspace or organization. Returns an empty data object. |
| Reorder Enum Option | `insertEnumOptionForCustomField` | Reorder an enum option within a custom field, positioned before or after another option. Returns the enum option. |
| Search Tasks in a Workspace | `searchTasksForWorkspace` | Full-text and filtered search for tasks in a workspace. Results are not stably ordered and do not support offset pagination (single page, max 100). Requires a paid (premium) Asana plan; free workspaces get 402. |
| Set Goal Metric | `createGoalMetric` | Create/set the metric on a goal. Returns the full goal with its metric. |
| Set Parent of a Task | `setParentForTask` | Change the parent of a task, making it a subtask of the given parent (or a top-level task when parent is null). Returns the full task. |
| Typeahead Search | `typeaheadForWorkspace` | Typeahead search for objects of a given resource_type in a workspace. Returns compact matching objects. |
| Update a Goal Relationship | `updateGoalRelationship` | Update a goal relationship's contribution weight. Returns the goal relationship. |
| Update a Membership | `updateMembership` | Update a membership's access level. Returns the membership. |
| Update a Story | `updateStory` | Update a comment story (text/html_text/is_pinned). Only comment-type stories you authored can be edited. |
| Update a Team | `updateTeam` | Update an existing team. Only provided fields are changed. |
| Update a Webhook | `updateWebhook` | Update a webhook's filters (the new filter set replaces the existing one). Returns the webhook. |
| Update a Workspace | `updateWorkspace` | Update a workspace (only the name is editable in practice). |
| Update Custom Field | `updateCustomField` | Update an existing custom field. Only provided fields are changed. |
| Update Enum Option | `updateEnumOption` | Update an enum option's name, color, or enabled state. Returns the enum option. |
| Update Goal | `updateGoal` | Update an existing goal, including its status. Only provided fields are changed. |
| Update Goal Metric Current Value | `updateGoalMetric` | Update the current value of a goal's metric. Returns the full goal with the updated metric (400 if no metric exists). |
| Update Portfolio | `updatePortfolio` | Update an existing portfolio. Only provided fields are changed. |
| Update Project | `updateProject` | Update an existing project. Only provided fields are changed. |
| Update Project Brief | `updateProjectBrief` | Update a project brief. Provide html_text OR text. Returns the brief. |
| Update Section | `updateSection` | Update the name of a section. |
| Update Tag | `updateTag` | Update an existing tag's name, color, or notes. |
| Update Task | `updateTask` | Update an existing task. Only provided fields are changed (sparse update). Set nullable fields to clear them. |
| Upload External Attachment | `createAttachmentForObject` | Attach an external file (by URL) to a task, project, or project_brief. Uses multipart/form-data with resource_subtype=external. For binary file uploads, use the Asana file-upload flow directly. Returns the attachment. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Resource Added | `added` | A resource (task, project, story, etc.) was created/added within the watched resource. Asana sends an events[] batch; each event has action='added'. |
| Resource Changed | `changed` | A field on the watched resource (or a child) changed. Each event has action='changed' and a change object describing the field and old/new values. |
| Resource Deleted | `deleted` | A resource was deleted (moved to trash). Each event has action='deleted'. |
| Resource Removed | `removed` | A resource was removed from the watched resource (e.g. a task removed from a project). Each event has action='removed'. |
| Resource Undeleted | `undeleted` | A previously deleted resource was restored from the trash. Each event has action='undeleted'. |
