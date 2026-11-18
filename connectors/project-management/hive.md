---
description: "Hive is a project management and collaboration platform."
hidden: true
---

# Hive

Hive is a project management and collaboration platform. Manage projects, actions (tasks), subactions, comments, attachments, labels, statuses, custom fields, tags, resource assignments, workflows, and webhooks.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Authentication** | Credentials you enter |
| **Actions** | 71 |
| **Events** | 0 |
| **Slug** | `hive` |

## Use it

Add Hive from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.hive.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Action Attachment | `addActionAttachment` | Adds an attachment to an action from a URL. |
| Add Project Custom Field | `addProjectCustomField` | Adds or reuses a project custom field and attaches it to the project. |
| Apply Template To Action | `applyTemplateToAction` | Applies a workflow/template (process) to an existing action. |
| Bulk Update Actions | `bulkUpdateActions` | Bulk-updates up to 1000 actions in one call. Each item in the actions array must include _id and any allowed update fields. |
| Copy Project | `copyProject` | Copies an existing project into a new one. |
| Create Action | `createAction` | Creates an action (task) in the workspace. Requires a title; optionally assign a project, assignees, description, status, deadline, and more. |
| Create Action Comment | `createActionComment` | Creates a comment on an action. |
| Create Activity Feed Item | `createActivityFeedItem` | Creates an activity feed item (message) in the workspace, attached to an action or project. |
| Create Custom Field | `createCustomField` | Creates a workspace custom field. |
| Create Custom Tag | `createCustomTag` | Creates a custom tag with optional options. |
| Create Label | `createLabel` | Creates a workspace label. |
| Create Project | `createProject` | Creates a project in the workspace. |
| Create Project Status | `createProjectStatus` | Creates a project status in the workspace. |
| Create Resource Assignment | `createResourceAssignment` | Creates a resource assignment. Requires Resourcing to be enabled on the workspace. |
| Create Role Tag | `createRoleTag` | Creates a role tag. |
| Create Webhook | `createWebhook` | Creates a webhook that posts events to a URL when the chosen trigger fires. |
| Delete Action | `deleteAction` | Deletes one action (task) by ID (Hive soft-delete). |
| Delete Custom Tag | `deleteCustomTag` | Deletes one custom tag by ID. |
| Delete Label | `deleteLabel` | Deletes one label by ID. |
| Delete Project | `deleteProject` | Deletes one project by ID. |
| Delete Project Custom Field | `deleteProjectCustomField` | Disables a custom field on a project. |
| Delete Resource Assignment | `deleteResourceAssignment` | Deletes one resource assignment by ID. |
| Delete Role Tag | `deleteRoleTag` | Deletes a role tag. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook owned by the authenticated user. |
| Export Dashboard Widget Data | `exportDashboardWidgetData` | Returns a temporary download URL for a CSV export of dashboard widget data. |
| Get Action | `getAction` | Retrieves one action (task) by ID. |
| Get Action Attachment | `getActionAttachment` | Retrieves one action attachment by ID. |
| Get Agile Sprint | `getAgileSprint` | Retrieves one agile sprint by ID. |
| Get Custom Field | `getCustomField` | Retrieves one workspace custom field by ID. |
| Get Custom Tag | `getCustomTag` | Retrieves one custom tag by ID. |
| Get Dashboard Widget Data | `getDashboardWidgetData` | Returns processed dashboard widget data. Provide user_filter_id, or workspace_id so the server can locate the dashboard user filter. |
| Get Label | `getLabel` | Retrieves one label by ID. |
| Get Project | `getProject` | Retrieves one project by ID. |
| Get Project Status | `getProjectStatus` | Retrieves one project status by ID. |
| Get Project Tag Assignment | `getProjectTagAssignment` | Retrieves one custom tag assignment for a project. |
| Get Resource Assignment | `getResourceAssignment` | Retrieves one resource assignment by ID. |
| Get User Role Tag | `getUserRoleTag` | Gets the role tag assigned to a user. |
| Get User Tag Assignment | `getUserTagAssignment` | Retrieves one custom tag assignment for a user. |
| List Action Attachments | `listActionAttachments` | Returns cursor-paginated file and Hive Drive attachments for an action. |
| List Action Comments | `listActionComments` | Returns cursor-paginated comments for an action. |
| List Action History | `listActionHistory` | Returns cursor-paginated change-history items for an action. |
| List Agile Sprints | `listAgileSprints` | Returns cursor-paginated agile sprints for the workspace. Requires Agile to be enabled on the workspace. |
| List Custom Fields | `listCustomFields` | Returns cursor-paginated workspace custom fields. |
| List Custom Tags | `listCustomTags` | Lists workspace custom tags. Optionally filter by tag type. |
| List Groups | `listGroups` | Returns cursor-paginated groups (teams) for the workspace. |
| List Labels | `listLabels` | Returns cursor-paginated workspace labels. |
| List Project Statuses | `listProjectStatuses` | Returns cursor-paginated project statuses sorted by creation time. |
| List Project Tags | `listProjectTags` | Lists custom tag assignments for a project. |
| List Project Users | `listProjectUsers` | Returns users visible on a project. |
| List Projects | `listProjects` | Returns projects accessible to the authenticated user (legacy-compatible resource handler). |
| List Resource Assignments | `listResourceAssignments` | Returns cursor-paginated resource assignments. Requires Resourcing to be enabled on the workspace. |
| List Role Tags | `listRoleTags` | Lists workspace role tags. |
| List Subactions | `listSubactions` | Returns cursor-paginated subactions for an action. |
| List User Tags | `listUserTags` | Returns custom tag assignments for a user. |
| List Versioned Files | `listVersionedFiles` | Returns cursor-paginated proofing versioned files accessible to the authenticated user. |
| List Workflows | `listWorkflows` | Returns cursor-paginated workflows for the workspace. |
| List Workspace Actions | `listWorkspaceActions` | Returns cursor-paginated actions (tasks) in the workspace accessible to the authenticated user. |
| List Workspace Projects | `listWorkspaceProjects` | Returns cursor-paginated projects in the workspace. Includes archived projects by default; use the archived filter to narrow. |
| List Workspaces | `listWorkspaces` | Returns cursor-paginated workspaces accessible to the authenticated user. |
| Search Actions | `searchActions` | Searches workspace actions by title. Uses limit/skip paging and returns an array. |
| Trigger Workflow | `triggerWorkflow` | Triggers a workflow by ID and creates/runs its action from the workflow template. |
| Update Action | `updateAction` | Updates one action (task) by ID. Only the fields you provide are changed. Use this to complete an action (set status), reassign it (set assignees), reschedule, relabel, or archive it. |
| Update Custom Tag | `updateCustomTag` | Updates a custom tag's name, multi-select setting, or options. |
| Update Label | `updateLabel` | Updates one label by ID. |
| Update Project | `updateProject` | Updates mutable project fields. Only the fields you provide are changed. |
| Update Project Custom Field | `updateProjectCustomField` | Updates a project custom field value or label. |
| Update Project Tag Assignment | `updateProjectTagAssignment` | Updates the selected options for a project custom tag. |
| Update Resource Assignment | `updateResourceAssignment` | Updates one resource assignment by ID. |
| Update Role Tag | `updateRoleTag` | Updates a role tag. |
| Update User Role Tag | `updateUserRoleTag` | Assigns or changes a user's role tag. |
| Update User Tag Assignment | `updateUserTagAssignment` | Updates the selected options for a user custom tag. |
