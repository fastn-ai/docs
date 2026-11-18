---
description: "Atlassian Jira Cloud connector — Issues (CRUD, JQL search, transitions, bulk ops, comments, worklogs, attachments, links, remote links, watchers, votes),…"
---

# Jira

Atlassian Jira Cloud connector — Issues (CRUD, JQL search, transitions, bulk ops, comments, worklogs, attachments, links, remote links, watchers, votes), Projects (components, versions, categories, roles, types), Users/Groups/Permissions, Fields & custom field options, Issue types/Statuses/Priorities/Resolutions/Labels, Filters & sharing, Dashboards, Time tracking, dynamic Webhooks, plus the Jira Software Agile API (boards, sprints, epics, backlog). Platform REST v3 + Agile 1.0 via api.atlassian.com (OAuth 2.0 3LO).

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [atlassian.com](https://atlassian.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 647 |
| **Events** | 8 |
| **Slug** | `jira` |

## Use it

Add Jira from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.jira.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Actors to Project Role | `addActorsToProjectRole` | Adds actors (users and/or groups) to a project role. Returns the updated project role. |
| Add Atlassian Team to Plan | `addAtlassianTeamToPlan` | Add an Atlassian team to a plan. Returns 204 on success. |
| Add Attachment | `addAttachment` | Add an attachment to an issue. POST /issue/{issueIdOrKey}/attachments. multipart/form-data with X-Atlassian-Token: no-check; the file is sent as form field 'file' (FileRef). NOTE: fastn multipart support is limited — file upload may require the file content be provided as a FileRef input named 'file'; verify behavior at execution time. |
| Add Comment | `addComment` | Add a comment to an issue. The body field is Atlassian Document Format (ADF). |
| Add Default Actors to Project Role | `addDefaultActorsToProjectRole` | Adds default actors (users and/or groups) to a project role. These actors are assigned to all new projects by default. |
| Add Field to Default Screen | `addFieldToDefaultScreen` | Adds a field to the default tab of the default screen. |
| Add Filter As Favourite | `setFavouriteForFilter` | Adds a filter as a favorite for the user. Returns the updated filter. |
| Add Gadget To Dashboard | `addGadget` | Adds a gadget to a dashboard. Provide either moduleKey or uri (not both). |
| Add Issue Security Level Members | `addIssueSecurityLevelMembers` | Adds members to an issue security level. Requires Administer Jira global permission. |
| Add Issue Security Levels | `addSecurityLevels` | Adds levels and levels' members to the issue security scheme. Requires Administer Jira global permission. |
| Add Issue Types To Context | `addIssueTypesToContext` | Adds issue types to a custom field context, making the context apply to those issue types. PUT /rest/api/3/field/{fieldId}/context/{contextId}/issuetype. Returns 204 on success. |
| Add Issue Types To Issue Type Scheme | `addIssueTypesToIssueTypeScheme` | Adds issue types to an issue type scheme. PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype |
| Add Notifications to Notification Scheme | `addNotificationsToScheme` | Adds notifications to a notification scheme. Requires Administer Jira global permission. |
| Add Screen Tab Field | `addScreenTabField` | Adds a field to a screen tab. |
| Add Share Permission | `addSharePermission` | Add a share permission to a filter. Set type and the corresponding id field (e.g. type=group + groupId, type=project + projectId). |
| Add User To Group | `addUserToGroup` | Add a user to a group. |
| Add Vote | `addVote` | Add the calling user's vote to an issue. POST /issue/{issueIdOrKey}/votes. No request body. |
| Add Watcher | `addWatcher` | Add a user as a watcher of an issue. POST /issue/{issueIdOrKey}/watchers. Body is the accountId string of the user to add as a watcher. |
| Add Worklog | `addWorklog` | Add a worklog to an issue. The comment field is Atlassian Document Format (ADF). timeSpentSeconds and started are required. |
| Analyse Jira Expression | `analyseExpression` | Analyses and validates a list of Jira expressions. Returns a list of analysis results, one for each expression. The analyses include type checking, validation of variables, and semantic analysis. |
| Append Mappings to Issue Type Screen Scheme | `appendMappingsToIssueTypeScreenScheme` | Appends issue type to screen scheme mappings to an issue type screen scheme. |
| Archive Issues (by ID/Key) | `archiveIssues` | Archive issues by issue ID/key. PUT /issue/archive. |
| Archive Issues Async (by JQL) | `archiveIssuesAsync` | Archive issues asynchronously by JQL. POST /issue/archive. Returns a task URL string. |
| Archive Plan | `archivePlan` | Archive a plan by ID. Returns 204 on success. |
| Archive Project | `archiveProject` | Archive a project. POST /rest/api/3/project/{projectIdOrKey}/archive. Returns 204 No Content. |
| Assign Field Configuration Scheme To Project | `assignFieldConfigurationSchemeToProject` | Assigns a field configuration scheme to a project. PUT /rest/api/3/fieldconfigurationscheme/project |
| Assign Issue | `assignIssue` | Assign an issue to a user. PUT /issue/{issueIdOrKey}/assignee. Use accountId of the user (null = default assignee, -1 = automatic). Returns 204. |
| Assign Issue Type Scheme To Project | `assignIssueTypeSchemeToProject` | Assigns an issue type scheme to a project. PUT /rest/api/3/issuetypescheme/project |
| Assign Issue Type Screen Scheme to Project | `assignIssueTypeScreenSchemeToProject` | Assigns an issue type screen scheme to a project. Issue type screen schemes can only be assigned to classic projects. |
| Assign Issue Types To Field Configurations | `assignIssueTypesToFieldConfigurations` | Assigns issue types to field configurations for a field configuration scheme. PUT /rest/api/3/fieldconfigurationscheme/{id}/mapping |
| Assign Permission Scheme | `assignPermissionScheme` | Assigns a permission scheme to a project. Requires Administer Projects or Administer Jira permission. |
| Assign Projects To Custom Field Context | `assignProjectsToCustomFieldContext` | Assigns a custom field context to projects. PUT /rest/api/3/field/{fieldId}/context/{contextId}/project. BLOCKED: Instance has only one classic project (FVT/10001); adding it gives 400 'already associated', and the only other project (KAN) is next-gen (404). Action config is correct. |
| Assign Workflow Scheme to Project | `assignWorkflowSchemeToProject` | Assigns a workflow scheme to a project. This operation is performed by project administrators only. |
| Associate Security Scheme to Project | `associateSecuritySchemeToProject` | Associates an issue security scheme with a project. Allows mapping old security levels to new ones. Requires Administer Jira global permission. |
| Bulk Create Issues | `createIssues` | Bulk create issues. POST /issue/bulk. issueUpdates is an array of {fields,...} objects. |
| Bulk Create Statuses | `createStatuses` | Creates statuses for a global or project scope. POST /rest/api/3/statuses. statuses is an array; scope is an object {type, project}. |
| Bulk Create Workflows | `bulkCreateWorkflows` | Creates workflows using the new bulk workflow creation API. Requires statuses and workflow definitions. |
| Bulk Delete Issue Property | `bulkDeleteIssueProperty` | Deletes a property value from multiple issues. Only entities the user has access to are updated. Returns 303 with task progress URL. |
| Bulk Delete Issues | `submitBulkDelete` | Bulk delete a list of issues. Returns a taskId to poll via getBulkOperationProgress. |
| Bulk Delete Statuses | `deleteStatusesById` | Deletes statuses by ID. DELETE /rest/api/3/statuses. id query param (ampersand-separated list) set explicitly. |
| Bulk Delete Worklogs | `bulkDeleteWorklogs` | Delete a list of worklogs from an issue. |
| Bulk Edit Dashboards | `bulkEditDashboards` | Bulk edit dashboards. Apply an action (changeOwner, changePermission, addPermission, removePermission) to multiple dashboards. |
| Bulk Edit Issues | `submitBulkEdit` | Bulk edit field values on a list of issues. Returns a taskId. |
| Bulk Fetch Issues | `bulkFetchIssues` | Bulk fetch issues by IDs or keys. POST /issue/bulkfetch. |
| Bulk Get Custom Field Configurations | `bulkGetCustomFieldConfigurations` | Returns a paginated list of configurations for multiple Connect custom fields. POST /rest/api/3/app/field/context/configuration/list. BLOCKED (business-400): Jira returns 400 'This API works only with fields provided by Forge apps.' — requires a Forge app that provides the custom fields. Cannot be exercised with standard OAuth 3LO or regular custom fields. |
| Bulk Get Groups | `bulkGetGroups` | Get a list of groups matching the supplied ids/names (paginated). |
| Bulk Get Statuses | `getStatusesById` | Returns a list of statuses by ID. GET /rest/api/3/statuses. |
| Bulk Get Statuses By Name | `getStatusesByName` | Returns a list of statuses by name. GET /rest/api/3/statuses/byNames. |
| Bulk Get Users | `bulkGetUsers` | Get a list of users matching the supplied accountIds (paginated). |
| Bulk Get Workflow Schemes | `bulkGetWorkflowSchemes` | Returns a list of workflow schemes by project IDs or workflow scheme IDs using the new bulk read endpoint. |
| Bulk Get Workflows (New API) | `bulkGetWorkflows` | Returns a list of workflows matching the specified criteria using the new workflows API (POST /workflows). Supports filtering by workflow IDs, names, and project/issue type associations. |
| Bulk Move Issues | `submitBulkMove` | Bulk move issues to a destination project/issue type. Returns a taskId. |
| Bulk Move Worklogs | `bulkMoveWorklogs` | Move a list of worklogs from one issue to another. |
| Bulk Set Issue Properties By Issue | `bulkSetIssuePropertiesByIssue` | Sets or updates entity property values on issues. Up to 10 entity properties can be specified for each issue and up to 100 issues included in the request. This is the per-issue variant. Returns 303 with task progress URL. |
| Bulk Set Issue Property | `bulkSetIssueProperty` | Sets a property value on multiple issues. You can specify up to 10,000 issues. Only entities the user has access to are updated. Returns a 303 (See Other) response with task progress URL. |
| Bulk Set Issues Properties By List | `bulkSetIssuesPropertiesByList` | Sets or updates entity property values on issues. Up to 10 entity properties can be specified for each issue and up to 100 issues included in the request. Returns 303 with task progress URL. |
| Bulk Transition Issue Statuses | `submitBulkTransition` | Bulk transition the status of a list of issues. Returns a taskId. |
| Bulk Unwatch Issues | `submitBulkUnwatch` | Bulk unwatch a list of issues. Returns a taskId. |
| Bulk Update Statuses | `updateStatuses` | Updates statuses by ID. PUT /rest/api/3/statuses. statuses is an array of {id, name, statusCategory, description}. |
| Bulk Update Workflows | `bulkUpdateWorkflows` | Updates workflows using the new bulk workflow update API. |
| Bulk Watch Issues | `submitBulkWatch` | Bulk watch a list of issues. Returns a taskId. |
| Cancel Task | `cancelTask` | Cancel a long-running asynchronous task by task ID. Returns 202 on success. |
| Change Filter Owner | `changeFilterOwner` | Changes the owner of a filter. |
| Check Dev Info Exists By Properties | `checkDevInfoExistsByProperties` | Checks if any development information exists for the specified entity properties in Jira devinfo. |
| Check Issues Against JQL | `matchIssues` | Check which issues match a list of JQL queries. POST /jql/match. |
| Copy Dashboard | `copyDashboard` | Copies a dashboard. Any values provided in the body replace those in the copied dashboard. |
| Count Issues Using JQL | `countIssues` | Get an approximate count of issues matching a JQL query. POST /search/approximate-count. |
| Create Board | `createBoard` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:board-scope:jira-software). Creates a new board. Board name, type and filter ID is required. Requires a Jira Software license. |
| Create Component | `createComponent` | Create a project component. POST /rest/api/3/component. Requires name and project. Returns the created component object. |
| Create Custom Field | `createCustomField` | Creates a custom field. POST /rest/api/3/field. |
| Create Custom Field Context | `createCustomFieldContext` | Creates a custom field context. POST /rest/api/3/field/{fieldId}/context. Optionally scope to specific issue types and projects. |
| Create Custom Field Options (Context) | `createCustomFieldOption` | Creates options for a custom field context. POST /rest/api/3/field/{fieldId}/context/{contextId}/option. options is an array of {value, disabled, optionId}. |
| Create Dashboard | `createDashboard` | Creates a dashboard. |
| Create Draft Workflow Scheme | `createDraftWorkflowScheme` | Creates a draft workflow scheme from an active workflow scheme, by copying the active workflow scheme. |
| Create Field Configuration | `createFieldConfiguration` | Creates a new field configuration. POST /rest/api/3/fieldconfiguration |
| Create Field Configuration Scheme | `createFieldConfigurationScheme` | Creates a field configuration scheme. POST /rest/api/3/fieldconfigurationscheme |
| Create Filter | `createFilter` | Create a filter. The filter is shared according to the default share scope and the user becomes the filter owner. |
| Create Group | `createGroup` | Create a group with the supplied name. |
| Create Issue | `createIssue` | Create an issue or subtask. POST /issue. fields is an object containing required fields like project, summary, issuetype, and the ADF description. description is an Atlassian Document Format (ADF) object rendered bare. |
| Create Issue (Plain Text) | `createIssuePlainText` | Create a Jira issue from flat, plain-text inputs. POST /rest/api/3/issue. The plain-text description is wrapped into an Atlassian Document Format (ADF) paragraph, so callers never build ADF. priority and assignee are objects ({name} / {accountId}); optional fields left unset are omitted from the request. Returns the created issue's id, key and self URL. |
| Create Issue Link Type | `createIssueLinkType` | Create a new issue link type. POST /issueLinkType. Provide name, inward, and outward descriptions. |
| Create Issue Security Scheme | `createIssueSecurityScheme` | Creates a security scheme with security scheme levels and levels' members. Requires Administer Jira global permission. |
| Create Issue Type | `createIssueType` | Creates an issue type and adds it to the default issue type scheme. POST /rest/api/3/issuetype. |
| Create Issue Type Scheme | `createIssueTypeScheme` | Creates an issue type scheme. POST /rest/api/3/issuetypescheme |
| Create Issue Type Screen Scheme | `createIssueTypeScreenScheme` | Creates an issue type screen scheme. |
| Create Notification Scheme | `createNotificationScheme` | Creates a notification scheme with notifications. Requires Administer Jira global permission. |
| Create or Update Remote Issue Link | `createOrUpdateRemoteIssueLink` | Create or update a remote issue link from an issue to an item in a remote system. If a globalId is matched it updates, otherwise creates. POST /issue/{issueIdOrKey}/remotelink. |
| Create Permission Grant | `createPermissionGrant` | Creates a permission grant in a permission scheme. Requires Administer Jira global permission. |
| Create Permission Scheme | `createPermissionScheme` | Creates a new permission scheme. Requires Administer Jira global permission. |
| Create Plan | `createPlan` | Create a new Advanced Roadmaps plan. Returns the ID of the created plan. |
| Create Plan-Only Team | `createPlanOnlyTeam` | Create a new plan-only team in a plan. Plan-only teams exist only within the plan and are not Atlassian teams. |
| Create Priority | `createPriority` | Creates an issue priority. POST /rest/api/3/priority. |
| Create Priority Scheme | `createPriorityScheme` | Create a new priority scheme. Returns the scheme ID and optionally a task if async. |
| Create Project | `createProject` | Create a project. POST /rest/api/3/project. Requires key, name and leadAccountId. Returns the created project's id, key and self URL. |
| Create Project Avatar | `createProjectAvatar` | Loads a custom avatar for a project (POST /avatar2). Returns the new Avatar object with its ID. |
| Create Project Category | `createProjectCategory` | Create a project category. POST /rest/api/3/projectCategory. Requires name. Returns the created category object. |
| Create Project Role | `createProjectRole` | Create a new project role. POST /rest/api/3/role. Requires name. Returns the created role object. |
| Create Related Work | `createRelatedWork` | Create a related work item for a version. POST /rest/api/3/version/{id}/relatedwork. Returns the created related work item. |
| Create Resolution | `createResolution` | Creates an issue resolution. POST /rest/api/3/resolution. |
| Create Screen | `createScreen` | Creates a screen with a default field tab. |
| Create Screen Scheme | `createScreenScheme` | Creates a screen scheme. |
| Create Screen Tab | `createScreenTab` | Creates a tab for a screen. |
| Create Sprint | `createSprint` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:sprint:jira-software). Creates a future sprint. Sprint name and origin board id are required. Start date, end date, and goal are optional. |
| Create UI Modification | `createUiModification` | Create a new UI modification for customizing the Jira UI. Returns the ID and self link of the created modification. |
| Create User | `createUser` | Create a user. The user is added to the default groups specified by products. Returns the created user. |
| Create Version | `createVersion` | Create a project version. POST /rest/api/3/version. Requires name and projectId. Returns the created version object. |
| Create Workflow Scheme | `createWorkflowScheme` | Creates a workflow scheme. |
| Create Workflow Transition Property | `createWorkflowTransitionProperty` | Adds a property to a workflow transition. Workflow must be inactive or the transition must be a global transition. |
| Delete Actors from Project Role | `deleteActorsFromProjectRole` | Deletes actors (users/groups) from a project role. Specify user (account ID) or group/groupId query params. |
| Delete And Replace Version | `deleteAndReplaceVersion` | Delete a version and replace its usages on issues/custom fields. POST /rest/api/3/version/{id}/removeAndSwap. Returns 204 No Content. |
| Delete Attachment | `removeAttachment` | Delete an attachment from an issue. |
| Delete Board | `deleteBoard` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:board-scope:jira-software). Deletes the board. Admin without the view permission can still remove the board. |
| Delete Board Property | `deleteBoardProperty` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:board-scope:jira-software). Removes the property from the board identified by the id. The user removing the property is required to have permissions to modify the board. |
| Delete Build By Key | `deleteBuildByKey` | Deletes a specific build from Jira identified by pipeline ID and build number. |
| Delete Builds By Properties | `deleteBuildsByProperties` | Deletes builds from Jira that match the specified entity properties. |
| Delete Comment | `deleteComment` | Delete a comment from an issue. |
| Delete Comment Property | `deleteCommentProperty` | Deletes a property from a comment. Returns 204 if successful. Returns 404 if the comment or property does not exist. |
| Delete Component | `deleteComponent` | Delete a project component. DELETE /rest/api/3/component/{id}. Optionally reassign issues to another component. Returns 204 No Content. |
| Delete Custom Field | `deleteCustomField` | Deletes a custom field (moves it to trash if not already). DELETE /rest/api/3/field/{id}. |
| Delete Custom Field Context | `deleteCustomFieldContext` | Deletes a custom field context. DELETE /rest/api/3/field/{fieldId}/context/{contextId}. Returns 204 on success. |
| Delete Custom Field Options (Context) | `deleteCustomFieldOption` | Deletes a custom field option. DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}. |
| Delete Dashboard | `deleteDashboard` | Deletes a dashboard by ID. |
| Delete Dashboard Item Property | `deleteDashboardItemProperty` | Deletes a dashboard item property. |
| Delete Default Actors from Project Role | `deleteDefaultActorsFromProjectRole` | Deletes default actors from a project role. Returns the updated project role. |
| Delete Default Workflow | `deleteWorkflowSchemeDefault` | Resets the default workflow for a workflow scheme to the default value (jira). |
| Delete Deployment By Key | `deleteDeploymentByKey` | Deletes a specific deployment from Jira identified by pipeline ID, environment ID, and deployment sequence number. |
| Delete Deployments By Properties | `deleteDeploymentsByProperties` | Deletes deployments from Jira that match the specified entity properties. Used to bulk-delete deployments by property value. |
| Delete Dev Info By Properties | `deleteDevInfoByProperties` | Deletes development information stored in Jira that matches the specified entity properties. |
| Delete Dev Info Entity | `deleteDevInfoEntity` | Deletes a specific development information entity (commit, branch, or pull request) from a repository in Jira devinfo. |
| Delete Dev Info Repository | `deleteDevInfoRepository` | Deletes a repository and all its associated development information from Jira devinfo. |
| Delete DevOps Component By ID | `deleteDevOpsComponentById` | Deletes a specific DevOps component from Jira by its ID. |
| Delete DevOps Components By Properties | `deleteDevOpsComponentsByProperties` | Deletes DevOps components from Jira that match the specified entity properties. |
| Delete Draft Default Workflow | `deleteDraftWorkflowSchemeDefault` | Resets the default workflow for a draft workflow scheme to the default value (jira). |
| Delete Draft Workflow Scheme | `deleteDraftWorkflowScheme` | Deletes a draft workflow scheme. |
| Delete Feature Flag By ID | `deleteFeatureFlagById` | Deletes a specific feature flag from Jira by its ID. |
| Delete Feature Flags By Properties | `deleteFeatureFlagsByProperties` | Deletes feature flags from Jira that match the specified entity properties. |
| Delete Field Configuration | `deleteFieldConfiguration` | Deletes a field configuration. DELETE /rest/api/3/fieldconfiguration/{id} |
| Delete Field Configuration Scheme | `deleteFieldConfigurationScheme` | Deletes a field configuration scheme. DELETE /rest/api/3/fieldconfigurationscheme/{id} |
| Delete Filter | `deleteFilter` | Delete a filter by ID. |
| Delete Inactive Workflow | `deleteInactiveWorkflow` | Delete an inactive workflow. Only workflows with no active associations can be deleted. |
| Delete Incident By ID | `deleteIncidentById` | Deletes a specific incident from Jira Operations by its ID. |
| Delete Issue | `deleteIssue` | Delete an issue. DELETE /issue/{issueIdOrKey}. deleteSubtasks must be true to delete an issue that has subtasks. |
| Delete Issue Link | `deleteIssueLink` | Delete an issue link by its ID. DELETE /issueLink/{linkId}. |
| Delete Issue Link Type | `deleteIssueLinkType` | Delete an issue link type by its ID. DELETE /issueLinkType/{issueLinkTypeId}. |
| Delete Issue Property | `deleteIssueProperty` | Deletes an issue's property. Returns a 204 if successful. Returns a 404 if the issue or property does not exist. |
| Delete Issue Security Scheme | `deleteIssueSecurityScheme` | Deletes an issue security scheme. Requires Administer Jira global permission. |
| Delete Issue Type | `deleteIssueType` | Deletes an issue type and reassigns its issues. DELETE /rest/api/3/issuetype/{id}. alternativeIssueTypeId query param set explicitly. |
| Delete Issue Type Property | `deleteIssueTypeProperty` | Deletes the issue type property. Returns 204 if successful. Returns 404 if the issue type or property does not exist. |
| Delete Issue Type Scheme | `deleteIssueTypeScheme` | Deletes an issue type scheme. DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId} |
| Delete Issue Type Screen Scheme | `deleteIssueTypeScreenScheme` | Deletes an issue type screen scheme. |
| Delete Issue Types for Workflow in Draft Scheme | `deleteDraftWorkflowSchemeWorkflow` | Deletes the workflow-issue type mappings for a specific workflow in the draft workflow scheme. |
| Delete Issue Types for Workflow in Scheme | `deleteWorkflowSchemeWorkflow` | Deletes the workflow-issue type mappings for a specific workflow in a workflow scheme. |
| Delete Notification Scheme | `deleteNotificationScheme` | Deletes a notification scheme. Requires Administer Jira global permission. |
| Delete Operations Data By Properties | `deleteOperationsDataByProperties` | Deletes Operations data (incidents and reviews) from Jira that match the specified entity properties. |
| Delete Operations Workspaces | `deleteOperationsWorkspaces` | Deletes (unlinks) Operations workspace IDs from the Jira site. |
| Delete Permission Scheme | `deletePermissionScheme` | Deletes a permission scheme. Requires Administer Jira global permission. |
| Delete Permission Scheme Grant | `deletePermissionSchemeGrant` | Deletes a permission grant from a permission scheme. Requires Administer Jira global permission. |
| Delete Plan-Only Team | `deletePlanOnlyTeam` | Delete a plan-only team from a plan. Returns 204 on success. |
| Delete Post-Incident Review By ID | `deletePostIncidentReviewById` | Deletes a specific post-incident review from Jira Operations by its ID. |
| Delete Preference | `removePreference` | Delete a preference of the current user by key. |
| Delete Priority | `deletePriority` | Deletes an issue priority (async). DELETE /rest/api/3/priority/{id}. BLOCKED: Jira Cloud automatically adds newly created priorities to the default priority scheme, making them report 409 'Priority is still in use' — the priority must be removed from all priority schemes before deletion. This is a provider account-state constraint. Returns 303 task object on success. |
| Delete Priority Scheme | `deletePriorityScheme` | Delete a priority scheme by ID. Returns 204 on success. |
| Delete Project | `deleteProject` | Delete a project. DELETE /rest/api/3/project/{projectIdOrKey}. Returns 204 No Content. |
| Delete Project Asynchronously | `deleteProjectAsynchronously` | Delete a project asynchronously (long-running task). POST /rest/api/3/project/{projectIdOrKey}/delete. Returns 303 with a task progress location. |
| Delete Project Avatar | `deleteProjectAvatar` | Deletes a custom project avatar. System avatars cannot be deleted. |
| Delete Project Category | `removeProjectCategory` | Delete a project category. DELETE /rest/api/3/projectCategory/{id}. Returns 204 No Content. |
| Delete Project Property | `deleteProjectProperty` | Deletes the property from a project. Returns 204 if successful. Returns 404 if the project or property does not exist. |
| Delete Project Role | `deleteProjectRole` | Delete a project role. DELETE /rest/api/3/role/{id}. Optionally swap to another role. Returns 204 No Content. |
| Delete Related Work | `deleteRelatedWork` | Delete a related work item from a version. DELETE /rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}. Returns 204 No Content. |
| Delete Remote Issue Link By Global ID | `deleteRemoteIssueLinkByGlobalId` | Delete the remote issue link matching the given globalId. DELETE /issue/{issueIdOrKey}/remotelink with globalId query param. |
| Delete Remote Issue Link By ID | `deleteRemoteIssueLinkById` | Delete a remote issue link by its ID. DELETE /issue/{issueIdOrKey}/remotelink/{linkId}. |
| Delete Remote Link By ID | `deleteRemoteLinkById` | Deletes a specific remote link from Jira by its ID. |
| Delete Remote Links By Properties | `deleteRemoteLinksByProperties` | Deletes remote links from Jira that match the specified entity properties. |
| Delete Resolution | `deleteResolution` | Deletes an issue resolution. DELETE /rest/api/3/resolution/{id}. replaceWith query param set explicitly (required). |
| Delete Screen | `deleteScreen` | Deletes a screen. |
| Delete Screen Scheme | `deleteScreenScheme` | Deletes a screen scheme. A screen scheme cannot be deleted if it is used in an issue type screen scheme. |
| Delete Screen Tab | `deleteScreenTab` | Deletes a screen tab. |
| Delete Share Permission | `deleteSharePermission` | Delete a share permission from a filter. |
| Delete Sprint | `deleteSprint` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:sprint:jira-software). Deletes a sprint. Once a sprint is deleted, all issues in the sprint will be moved to the backlog. |
| Delete Sprint Property | `deleteProperty` | Removes the property from the sprint identified by the id. The user removing the property is required to have permissions to modify the sprint. |
| Delete UI Modification | `deleteUiModification` | Delete a UI modification by ID. Returns 204 on success. |
| Delete Universal Avatar | `deleteUniversalAvatar` | Deletes a custom avatar for a project or issue type. System avatars cannot be deleted. |
| Delete User | `removeUser` | Delete a user by accountId. |
| Delete User Property | `deleteUserProperty` | Deletes a property from a user. Returns 204 if successful. Returns 404 if the user or property does not exist. |
| Delete Version | `deleteVersion` | Delete a project version. DELETE /rest/api/3/version/{id}. Optionally move fixVersion/affectedVersion to another version. Returns 204 No Content. |
| Delete Webhooks | `deleteWebhooks` | Delete registered Jira dynamic webhooks by ID. Sends a JSON body { webhookIds: [number] }. |
| Delete Workflow for Issue Type in Draft Scheme | `deleteDraftWorkflowSchemeIssueType` | Deletes the workflow-issue type mapping for the draft workflow scheme. |
| Delete Workflow for Issue Type in Scheme | `deleteWorkflowSchemeIssueType` | Deletes the workflow-issue type mapping for a workflow scheme. |
| Delete Workflow Scheme | `deleteWorkflowScheme` | Deletes a workflow scheme. Note that a workflow scheme cannot be deleted if it is active (that is, being used by at least one project). |
| Delete Workflow Transition Property | `deleteWorkflowTransitionProperty` | Deletes a property from a workflow transition. Workflow must be inactive or the transition must be a global transition. |
| Delete Workflow Transition Rule Configurations | `deleteWorkflowTransitionRuleConfigs` | Deletes workflow transition rules from one or more workflows. Only Atlassian Connect app administrators can use this operation. |
| Delete Worklog | `deleteWorklog` | Delete a worklog from an issue. |
| Delete Worklog Property | `deleteWorklogProperty` | Deletes a worklog's property. Returns 204 if successful. Returns 404 if the issue, worklog, or property does not exist. |
| Duplicate Plan | `duplicatePlan` | Duplicate an existing plan. The new plan name must be provided. |
| Edit Issue | `editIssue` | Edit an issue's fields. PUT /issue/{issueIdOrKey}. fields holds the fields to set/update (description is an ADF object). Returns 204 unless returnIssue=true. |
| Estimate Issue For Board | `estimateIssueForBoard` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:issue:jira-software). Updates the estimation of the issue. The boardId query param is used to determine which field is used for estimation for the board. |
| Eval Jira Expression (Legacy) | `evalJiraExpression` | Legacy endpoint being removed. Evaluates a Jira expression and returns its value. Prefer evaluateExpression which uses the enhanced search API. |
| Evaluate Jira Expression | `evaluateExpression` | Evaluates a Jira expression using the enhanced search API. Returns the value of the expression and optional metadata about the expression complexity. |
| Export Archived Issues | `exportArchivedIssues` | Export archived issues. PUT /issues/archive/export. All body fields are optional filters. |
| Find Components For Projects | `findComponentsForProjects` | Find components across projects, paginated. GET /rest/api/3/component. Returns a paginated page object with values array. |
| Find Groups | `findGroups` | Find groups whose names contain the query string, for use in a group picker. |
| Find User Keys By Query | `findUserKeysByQuery` | Find user keys using a structured JQL-like user search query. |
| Find Users | `findUsers` | Find users matching a query string against displayName and emailAddress. |
| Find Users Assignable To Issues | `findAssignableUsers` | Find users that can be assigned to an issue or project. |
| Find Users Assignable To Projects | `findBulkAssignableUsers` | Find users that can be assigned to issues in one or more projects. |
| Find Users By Query | `findUsersByQuery` | Find users using a structured JQL-like user search query. |
| Find Users For Picker | `findUsersForPicker` | Find users matching a query for use in a user picker. |
| Find Users With Browse Permission | `findUsersWithBrowsePermission` | Find users who can browse a given issue or project. |
| Find Users With Permissions | `findUsersWithAllPermissions` | Find users with all of the supplied permissions for a project or issue. |
| Fully Update Project Role | `fullyUpdateProjectRole` | Fully update a project role's name and description. PUT /role/{id}. Both name and description are replaced. Returns the updated role object {self, name, id, description, actors}. |
| Get Accessible Project Type By Key | `getAccessibleProjectTypeByKey` | Get an accessible project type by its key. GET /project/type/{projectTypeKey}/accessible. Returns the project type {key, formattedKey, descriptionI18nKey, icon, color} if accessible to the current user. |
| Get Accessible Resources | `getAccessibleResources` | List the Jira sites the OAuth token can access. Returns an array of {id,url,name,scopes,avatarUrl}; the id IS the cloudId used by every other action. Call once after connecting. |
| Get Account IDs For Users (Migration) | `bulkGetUsersMigration` | Get account IDs for users based on usernames and/or keys (migration helper). |
| Get Agile Issue | `getAgileIssue` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:issue:jira-software). Returns a single issue, for a given issue ID or issue key, with Agile-specific fields (sprint, closedSprints, flagged, epic). This only includes issues the user has permission to view. |
| Get All Accessible Project Types | `getAllAccessibleProjectTypes` | Get all project types accessible to the current user. GET /project/type/accessible. Returns an array of project types, each {key, formattedKey, descriptionI18nKey, icon, color}. |
| Get All Boards | `getAllBoards` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns all boards. This only includes boards the user has permission to view. Supports filtering by type, name, project, etc. |
| Get All Dashboards | `getAllDashboards` | Returns a list of dashboards owned by or shared with the user. Optionally filter to my or favourite. |
| Get All Issue Types For User | `getIssueAllTypes` | Returns all issue types. GET /rest/api/3/issuetype. |
| Get All Labels | `getAllLabels` | Returns a paginated list of available labels. GET /rest/api/3/label. |
| Get All Permission Schemes | `getAllPermissionSchemes` | Returns all permission schemes. Requires Administer Jira global permission. |
| Get All Permissions | `getAllPermissions` | Get all permissions, including project and global permissions. |
| Get All Project Avatars | `getAllProjectAvatars` | Returns all project avatars (both system and custom) for a project. |
| Get All Project Categories | `getAllProjectCategories` | Get all project categories. GET /rest/api/3/projectCategory. Returns an array of project category objects. |
| Get All Project Roles | `getAllProjectRoles` | Get all project roles available in Jira. GET /rest/api/3/role. Returns an array of role objects. |
| Get All Project Types | `getAllProjectTypes` | Get all project types for the Jira site. GET /project/type. Returns an array of project types, each {key, formattedKey, descriptionI18nKey, icon, color}. |
| Get All Projects | `getAllProjects` | Get all projects visible to the user. GET /rest/api/3/project. Returns an array of project objects. |
| Get All Quick Filters | `getAllQuickFilters` | Returns all quick filters from a board, for the given board ID. |
| Get All Screen Tabs | `getAllScreenTabs` | Returns the list of tabs for a bulk of screens. |
| Get All Sprints | `getAllSprints` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:sprint:jira-software). Returns all sprints from a board, for the given board ID. This only includes sprints that the user has permission to view. |
| Get All Statuses | `getStatuses` | Returns all statuses associated with active workflows. GET /rest/api/3/status. |
| Get All Statuses For Project | `getAllStatuses` | Get all issue types with their statuses for a project. GET /rest/api/3/project/{projectIdOrKey}/statuses. Returns an array of issue-type/status objects. |
| Get All Time Tracking Providers | `getAvailableTimeTrackingImplementations` | Returns all time tracking providers available in the Jira instance. |
| Get All Users | `getAllUsers` | Get a list of all (active and inactive) users via the users/search endpoint. |
| Get All Users Default | `getAllUsersDefault` | Get a list of all (active and inactive) users. |
| Get All Versions | `getAllVersions` | Returns all versions from a board, for the given board ID. This only includes versions that the user has permission to view. |
| Get Alternative Issue Types | `getAlternativeIssueTypes` | Returns alternative issue types for the given issue type. GET /rest/api/3/issuetype/{id}/alternatives. |
| Get Announcement Banner | `getAnnouncementBanner` | Get the current announcement banner configuration for the Jira instance. |
| Get Application License Count | `getApplicationLicenseCount` | Returns the approximate number of user accounts for a single Jira license. Note that information is cached with a 7-day lifecycle and could be stale at the time of call. |
| Get Application Role | `getApplicationRole` | Returns an application role by its key. In Jira, application roles are managed using the Application access configuration page. |
| Get Approximate Issue Count For Backlog | `getApproximateIssueCountForBacklog` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns the approximate number of issues that match the JQL search for the board's backlog. |
| Get Approximate Issue Count For Board | `getApproximateIssueCountForBoard` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns the approximate number of issues that match the JQL search for a board. |
| Get Approximate License Count | `getApproximateLicenseCount` | Returns the approximate number of user accounts across all Jira licenses. Note that information is cached with a 7-day lifecycle and could be stale at the time of call. |
| Get Assigned Permission Scheme | `getAssignedPermissionScheme` | Returns the permission scheme associated with a project. Requires Administer Projects or Administer Jira permission. |
| Get Atlassian Team in Plan | `getAtlassianTeamInPlan` | Get details of a specific Atlassian team in a plan. |
| Get Attachment Content | `getAttachmentContent` | Return the contents of an attachment. By default returns a redirect to the download. |
| Get Attachment Metadata | `getAttachment` | Return the metadata for an attachment. Note this does not return the contents of the attachment. |
| Get Attachment Thumbnail | `getAttachmentThumbnail` | Return the thumbnail of an attachment. |
| Get Available Gadgets | `getAllAvailableDashboardGadgets` | Returns a list of all available gadgets that can be added to a dashboard. |
| Get Available Priorities for Scheme | `getAvailablePrioritiesForScheme` | Get available priorities that can be added to a priority scheme. |
| Get Available Screen Fields | `getAvailableScreenFields` | Returns the fields that can be added to a tab on a screen. |
| Get Avatar Image By ID | `getAvatarImageById` | Returns a project or issue type avatar image by ID. |
| Get Avatar Image By Owner | `getAvatarImageByOwner` | Returns the avatar image for a project or issue type by owner entity ID. |
| Get Avatar Image By Type | `getAvatarImageByType` | Returns the default system avatar image for the specified avatar type. GET /rest/api/3/universal_avatar/view/type/{type}. BLOCKED: Returns binary image (PNG/SVG); fastn platform returns 502 'Body is unusable: Body has already been read' on binary responses. |
| Get Board | `getBoard` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns the board for the given board ID. This board will only be returned if the user has permission to view it. |
| Get Board By Filter ID | `getBoardByFilterId` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns any boards which use the provided filter id. This only includes boards the user has permission to view. |
| Get Board Configuration | `getBoardConfiguration` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns the configuration of a Jira board, including column config, estimation, filter, and ranking settings. |
| Get Board Configuration | `getConfiguration` | Get the board configuration. The response contains the filter, column config, estimation and ranking settings for the board. |
| Get Board Issues For Epic | `getBoardIssuesForEpic` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns all issues that belong to an epic on the board, for the given epic ID and the board ID. |
| Get Board Issues For Epic (Enhanced) | `getBoardIssuesForEpicJSIS` | Returns all issues that belong to an epic on the board using the enhanced JSIS search (token pagination). Software base path /rest/software/1.0. |
| Get Board Issues For Sprint | `getBoardIssuesForSprint` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns all issues in a sprint, for a given sprint ID, that belong to the board. This only includes issues that the user has permission to view. |
| Get Board Issues For Sprint (Enhanced) | `getBoardIssuesForSprintJSIS` | Returns all issues in a sprint that belong to the board using the enhanced JSIS search (token pagination). Software base path /rest/software/1.0. |
| Get Board Projects | `getBoardProjects` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns all projects that are associated with a given board. |
| Get Board Projects Full | `getBoardProjectsFull` | Returns all projects including project category that are associated with a given board. |
| Get Board Property | `getBoardProperty` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns the value of the property with a given key from the board identified by the id. |
| Get Board Property Keys | `getBoardPropertyKeys` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns the keys of all properties for the board identified by the id. |
| Get Board Versions | `getBoardVersions` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns all versions from a date-ordered list of versions associated with a given board. |
| Get Build By Key | `getBuildByKey` | Returns a specific build from Jira identified by pipeline ID and build number. |
| Get Bulk Available Transitions | `getAvailableTransitions` | Get available workflow transitions for a set of issues for bulk transition. |
| Get Bulk Changelogs | `getBulkChangelogs` | Bulk fetch changelogs for multiple issues. POST /changelog/bulkfetch. |
| Get Bulk Editable Fields | `getBulkEditableFields` | Get the fields that can be bulk edited for a set of issues. |
| Get Bulk Operation Progress | `getBulkOperationProgress` | Get the progress of a bulk issue operation by task ID. |
| Get Bulk Permissions | `getBulkPermissions` | Check global and project permissions in bulk for a user. POST /permissions/check. Returns the global permissions and project permissions the user has, given the requested permissions, projects, and issues. |
| Get Changelogs | `getChangeLogs` | Get changelogs for an issue (paginated). GET /issue/{issueIdOrKey}/changelog. |
| Get Changelogs by IDs | `getChangeLogsByIds` | Get changelogs for an issue by changelog IDs. POST /issue/{issueIdOrKey}/changelog/list. |
| Get Columns | `getColumns` | Returns the columns configured for a filter. |
| Get Comment | `getComment` | Return a single comment of an issue. |
| Get Comment Property | `getCommentProperty` | Returns the key and value of a comment's property. Returns 404 if the comment or property does not exist. |
| Get Comment Property Keys | `getCommentPropertyKeys` | Returns the URLs and keys of the properties of a comment. Returns 404 if the comment does not exist. |
| Get Comments By IDs | `getCommentsByIds` | Return comments for a list of comment IDs. |
| Get Component | `getComponent` | Get a project component by ID. GET /rest/api/3/component/{id}. Returns the component object. |
| Get Component Issues Count | `getComponentRelatedIssues` | Get the count of issues assigned to a component. GET /rest/api/3/component/{id}/relatedIssueCounts. Returns the issue count. |
| Get Context Default Values | `getContextDefaultValues` | Returns a paginated list of default values for a custom field context. GET /rest/api/3/field/{fieldId}/context/defaultValue. |
| Get Contexts For Field | `getContextsForFieldDeprecated` | Returns a paginated list of contexts for a custom field. GET /rest/api/3/field/{fieldId}/contexts. |
| Get Create Field Metadata for Issue Type | `getCreateIssueMetaIssueTypeId` | Get field metadata for creating issues of a given type in a project. GET /issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId}. |
| Get Create Issue Metadata | `getCreateIssueMeta` | Get metadata for creating issues. GET /issue/createmeta. Filter with projectIds, projectKeys, issuetypeIds, issuetypeNames, expand. |
| Get Create Metadata Issue Types | `getCreateIssueMetaIssueTypes` | Get issue types available for creating issues in a project. GET /issue/createmeta/{projectIdOrKey}/issuetypes. |
| Get Current User | `getCurrentUser` | Get details of the currently authenticated user (the 'myself' endpoint). |
| Get Custom Field Configuration | `getCustomFieldConfiguration` | Returns a paginated list of configurations for a custom field created by a Connect app. GET /rest/api/3/app/field/{fieldIdOrKey}/context/configuration. BLOCKED (business-400): Jira returns 400 'This API works only with fields provided by Forge apps.' — requires a Forge app that provides the custom fields. Cannot be exercised with standard OAuth 3LO or regular custom fields. |
| Get Custom Field Contexts | `getContextsForField` | Returns a paginated list of contexts for a custom field. GET /rest/api/3/field/{fieldId}/context. Optionally filter by isAnyIssueType, isGlobalContext, or specific contextId values. |
| Get Custom Field Contexts For Projects And Issue Types | `getCustomFieldContextsForProjectsAndIssueTypes` | Returns a paginated list of project and issue type mappings and, for each mapping, the ID of a custom field context that applies to the project and issue type. POST /rest/api/3/field/{fieldId}/context/mapping. |
| Get Custom Field Option | `getCustomFieldOption` | Returns a custom field option. GET /rest/api/3/customFieldOption/{id}. |
| Get Custom Field Options (Context) | `getOptionsForContext` | Returns a paginated list of options for a custom field context. GET /rest/api/3/field/{fieldId}/context/{contextId}/option. |
| Get Dashboard | `getDashboard` | Returns a dashboard by ID. |
| Get Dashboard Item Property | `getDashboardItemProperty` | Returns the value of a dashboard item property. |
| Get Dashboard Item Property Keys | `getDashboardItemPropertyKeys` | Returns the keys of all properties for a dashboard item. |
| Get Default Actors for Project Role | `getDefaultActorsForProjectRole` | Returns the default actors for a project role (actors applied to all new projects). Uses the global role ID. |
| Get Default Share Scope | `getDefaultShareScope` | Returns the default sharing settings for new filters and dashboards for the user. |
| Get Default Workflow | `getWorkflowSchemeDefault` | Returns the default workflow for a workflow scheme. |
| Get Default Workflow Editor | `getDefaultWorkflowEditor` | Returns the user's default workflow editor (new or classic). |
| Get Deployment By Key | `getDeploymentByKey` | Returns a specific deployment from Jira identified by pipeline ID, environment ID, and deployment sequence number. |
| Get Deployment Gating Status | `getDeploymentGatingStatus` | Returns the gating status of a specific deployment in Jira, indicating whether it passed deployment gates. |
| Get Dev Info Repository | `getDevInfoRepository` | Returns the development information for a specific repository stored in Jira devinfo. |
| Get Dev Status For Issue | `getDevStatusForIssue` | Returns the development information (commits, branches, pull requests) for a Jira issue via the dev-status API. |
| Get DevOps Component By ID | `getDevOpsComponentById` | Returns a specific DevOps component from Jira by its ID. |
| Get Draft Default Workflow | `getDraftWorkflowSchemeDefault` | Returns the default workflow for the draft workflow scheme. |
| Get Draft Workflow Scheme | `getDraftWorkflowScheme` | Returns the draft workflow scheme for an active workflow scheme. |
| Get Edit Issue Metadata | `getEditIssueMeta` | Get metadata for editing an issue's fields. GET /issue/{issueIdOrKey}/editmeta. |
| Get Epic | `getEpic` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:epic:jira-software). Returns the epic for a given epic ID. This epic will only be returned if the user has permission to view it. |
| Get Epics | `getEpics` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:epic:jira-software). Returns all epics from the board, for the given board ID. This only includes epics that the user has permission to view. |
| Get Events | `getEvents` | Get all issue events configured in Jira. GET /events. |
| Get Expanded Attachment Contents Metadata (Raw) | `expandAttachmentForMachines` | Return the contents metadata for an expanded archive attachment in machine-readable (raw) form. |
| Get Expanded Attachment Metadata (Human) | `expandAttachmentForHumans` | Return all metadata for the contents of an expanded archive attachment in human-readable form. |
| Get Failed Webhooks | `getFailedWebhooks` | Returns webhooks that have recently failed to be delivered to the registered URL for the app, within the last 72 hours. |
| Get Favourite Filters | `getFavouriteFilters` | Returns the visible favorite filters of the user. |
| Get Feature Flag By ID | `getFeatureFlagById` | Returns a specific feature flag from Jira by its ID. |
| Get Features For Board | `getFeaturesForBoard` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns the features for a board. |
| Get Field Configuration Items | `getFieldConfigurationItems` | Returns a paginated list of all fields for a field configuration. GET /rest/api/3/fieldconfiguration/{id}/fields |
| Get Field Configuration Scheme Mapping | `getFieldConfigurationSchemeMapping` | Returns a paginated list of field configuration issue type items. GET /rest/api/3/fieldconfigurationscheme/mapping |
| Get Field Configuration Scheme Project Associations | `getFieldConfigurationSchemeProjectAssociations` | Returns a paginated list of field configuration schemes and associated projects. GET /rest/api/3/fieldconfigurationscheme/project |
| Get Field Project Associations | `getFieldProjectAssociations` | Returns a paginated list of project associations for a field. GET /rest/api/3/field/{fieldId}/association/project. |
| Get Fields | `getFields` | Returns system and custom issue fields. GET /rest/api/3/field. Returns an array of field objects. |
| Get Fields For Projects | `getProjectFields` | Returns a paginated list of fields for the given projects and work types. GET /rest/api/3/projects/fields. |
| Get Fields Paginated | `getFieldsPaginated` | Returns a paginated list of fields for Classic Jira projects. GET /rest/api/3/field/search. |
| Get Filter | `getFilter` | Returns a filter by ID. |
| Get Gadgets | `getAllGadgets` | Returns a list of gadgets on a dashboard. |
| Get Group | `getGroup` | Get a group, including a paginated list of its members. |
| Get IDs Of Deleted Worklogs | `getIdsOfWorklogsDeletedSince` | Return a list of IDs and delete timestamps for worklogs deleted after a given time. |
| Get IDs Of Updated Worklogs | `getIdsOfWorklogsModifiedSince` | Return a list of IDs and update timestamps for worklogs updated after a given time. |
| Get Incident By ID | `getIncidentById` | Returns a specific incident from Jira Operations by its ID. |
| Get Instance License | `getInstanceLicense` | Returns licensing information about the Jira instance. |
| Get Is Watching Issue Bulk | `getIsWatchingIssueBulk` | Get whether the calling user is watching each of a list of issues. POST /issue/watching. |
| Get Issue | `getIssue` | Get a single issue by ID or key. GET /issue/{issueIdOrKey}. |
| Get Issue Comments | `getComments` | Return all comments for an issue. |
| Get Issue Estimation For Board | `getIssueEstimationForBoard` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:issue:jira-software). Returns the estimation of the issue and a fieldId of the field that is used for it. The boardId param is used to determine which field is used for estimation for the board. |
| Get Issue Limit Report | `getIssueLimitReport` | Get issue limit report (issues approaching/breaching field count limits). GET /issue/limit/report. |
| Get Issue Link | `getIssueLink` | Get a single issue link by its ID. GET /issueLink/{linkId}. |
| Get Issue Link Type | `getIssueLinkType` | Get a single issue link type by its ID. GET /issueLinkType/{issueLinkTypeId}. |
| Get Issue Link Types | `getIssueLinkTypes` | Get the list of all issue link types in the Jira instance. GET /issueLinkType. |
| Get Issue Picker Suggestions | `getIssuePickerResource` | Get issue suggestions for auto-completion. GET /issue/picker. |
| Get Issue Property | `getIssueProperty` | Returns the key and value of an issue's property. Returns a 404 if the issue or property does not exist. |
| Get Issue Property Keys | `getIssuePropertyKeys` | Returns the URLs and keys of an issue's properties. Returns a 404 if the issue does not exist. |
| Get Issue Security Level Members | `getSecurityLevelMembers` | Returns a paginated list of issue security level members. Can filter by member ID, scheme ID, and level ID. |
| Get Issue Security Level Members by Scheme | `getIssueSecurityLevelMembers` | Returns a paginated list of issue security level members for a given issue security scheme. |
| Get Issue Security Levels | `getSecurityLevels` | Returns a paginated list of issue security levels. Can filter by level ID, scheme ID, and whether to return only default levels. |
| Get Issue Security Scheme | `getIssueSecurityScheme` | Returns an issue security scheme along with its security levels. Requires Administer Jira global permission. |
| Get Issue Security Schemes | `getIssueSecuritySchemes` | Returns all issue security schemes. Requires Administer Jira global permission. |
| Get Issue Type | `getIssueType` | Returns an issue type. GET /rest/api/3/issuetype/{id}. |
| Get Issue Type Mappings For Contexts | `getIssueTypeMappingsForContexts` | Returns a paginated list of issue types for the contexts of a custom field. GET /rest/api/3/field/{fieldId}/context/issuetypemapping. |
| Get Issue Type Property | `getIssueTypeProperty` | Returns the key and value of the issue type property. Returns 404 if the issue type or property does not exist. |
| Get Issue Type Property Keys | `getIssueTypePropertyKeys` | Returns all the property keys of the issue type. Returns 404 if the issue type is not found. |
| Get Issue Type Scheme Mapping | `getIssueTypeSchemeMapping` | Returns a paginated list of issue type scheme items. GET /rest/api/3/issuetypescheme/mapping |
| Get Issue Type Scheme Project Associations | `getIssueTypeSchemeProjectAssociations` | Returns a paginated list of issue type schemes and, for each issue type scheme, a list of the projects that use it. GET /rest/api/3/issuetypescheme/project |
| Get Issue Type Screen Scheme Mappings | `getIssueTypeScreenSchemeMappings` | Returns a paginated list of the mappings between issue types and screen schemes for a list of issue type screen schemes. |
| Get Issue Type Screen Schemes for Project | `getIssueTypeScreenSchemesForProject` | Returns a paginated list of issue type screen schemes and, for each issue type screen scheme, a list of the projects that use it. |
| Get Issue Type Usages By Status And Project | `getProjectIssueTypeUsagesForStatus` | Returns issue type usages for a status in a project. GET /rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages. |
| Get Issue Types For Project | `getIssueTypesForProject` | Returns issue types for a project. GET /rest/api/3/issuetype/project. |
| Get Issue Types for Workflow in Draft Scheme | `getDraftWorkflowSchemeWorkflow` | Returns the issue types associated with a workflow in the draft workflow scheme. |
| Get Issue Types for Workflow in Scheme | `getWorkflowSchemeWorkflow` | Returns the issue types associated with a workflow in a workflow scheme. |
| Get Issue Watchers | `getIssueWatchers` | Get the watchers for a Jira issue. GET /issue/{issueIdOrKey}/watchers. |
| Get Issue Worklogs | `getIssueWorklog` | Return the worklogs for an issue. |
| Get Issues For Backlog | `getIssuesForBacklog` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns all issues from the board's backlog, for the given board ID. This only includes issues that the user has permission to view. |
| Get Issues For Backlog (Enhanced) | `getIssuesForBacklogJSIS` | Returns all issues from the board's backlog using the enhanced JSIS search (token pagination). Software base path /rest/software/1.0. |
| Get Issues For Board | `getIssuesForBoard` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns all issues from a board, for the given board ID. This only includes issues that the user has permission to view. |
| Get Issues For Board (Enhanced) | `getIssuesForBoardJSIS` | Returns all issues from a board using the enhanced JSIS search (token pagination). Software base path /rest/software/1.0. |
| Get Issues For Epic | `getIssuesForEpic` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:epic:jira-software). Returns all issues that belong to the epic, for the given epic ID. This only includes issues that the user has permission to view. |
| Get Issues For Epic (Enhanced) | `getIssuesForEpicJSIS` | Returns all issues that belong to the epic using the enhanced JSIS search (token pagination). Software base path /rest/software/1.0. |
| Get Issues For Sprint | `getIssuesForSprint` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:sprint:jira-software). Returns all issues in a sprint, for a given sprint ID. This only includes issues that the user has permission to view. |
| Get Issues For Sprint (Enhanced) | `getIssuesForSprintJSIS` | Returns all issues in a sprint using the enhanced JSIS search (token pagination). Software base path /rest/software/1.0. |
| Get Issues Without Epic | `getIssuesWithoutEpic` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns all issues that do not belong to any epic. This only includes issues that the user has permission to view. |
| Get Issues Without Epic (Enhanced) | `getIssuesWithoutEpicJSIS` | Returns all issues that do not belong to any epic using the enhanced JSIS search (token pagination). Software base path /rest/software/1.0. |
| Get Issues Without Epic For Board | `getIssuesWithoutEpicForBoard` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns all issues that do not belong to any epic on a board, for the given board ID. |
| Get Issues Without Epic For Board (Enhanced) | `getIssuesWithoutEpicForBoardJSIS` | Returns all issues that do not belong to any epic on a board using the enhanced JSIS search (token pagination). Software base path /rest/software/1.0. |
| Get Jira Attachment Settings | `getAttachmentMeta` | Return the attachment settings (whether attachments are enabled and the maximum upload size). |
| Get JQL Autocomplete Data (GET) | `getAutoComplete` | Get reference data for building JQL queries (fields, functions, reserved words). GET /jql/autocompletedata. |
| Get JQL Autocomplete Data (POST) | `getAutoCompletePost` | Get reference data for building JQL queries, filtered by project. POST /jql/autocompletedata. |
| Get JQL Field Autocomplete Suggestions | `getFieldAutoCompleteForQueryString` | Get autocomplete suggestions for a JQL field value. GET /jql/autocompletedata/suggestions. |
| Get Locale | `getLocale` | Get the locale of the current user. |
| Get My Filters | `getMyFilters` | Returns the filters owned by the user. If includeFavourites is true, the user's favorite filters are also returned. |
| Get My Permissions | `getMyPermissions` | Get a list of permissions indicating which permissions the current user has for a project, issue or comment context. |
| Get Notification Scheme | `getNotificationScheme` | Returns a notification scheme, including the list of events and the recipients who will receive notifications for those events. Requires Administer Jira global permission. |
| Get Notification Scheme to Project Mappings | `getNotificationSchemeToProjectMappings` | Returns a paginated mapping of projects and notification schemes. Can filter by notification scheme ID and project ID. |
| Get Notification Schemes | `getNotificationSchemes` | Returns a paginated list of notification schemes. Can filter by scheme ID, project ID, and whether to return only default schemes. |
| Get Operations Workspaces | `getOperationsWorkspaces` | Returns all Operations workspace IDs or a specific Operations workspace linked to the Jira site. |
| Get Permission Scheme | `getPermissionScheme` | Returns a permission scheme. Requires Administer Jira global permission. |
| Get Permission Scheme Grant | `getPermissionSchemeGrant` | Returns a permission grant. Requires Administer Jira global permission. |
| Get Permission Scheme Grants | `getPermissionSchemeGrants` | Returns all permission grants for a permission scheme. Requires Administer Jira global permission. |
| Get Permitted Projects | `getPermittedProjects` | Get the projects where the user has the given project permissions. POST /permissions/project. Returns the list of projects {id, key} for which the user holds all the requested permissions. |
| Get Plan | `getPlan` | Get a single plan by ID. Returns full plan details including issueSources, exclusionRules, permissions and scheduling. |
| Get Plan-Only Team | `getPlanOnlyTeam` | Get details of a specific plan-only team in a plan. |
| Get Post-Incident Review By ID | `getPostIncidentReviewById` | Returns a specific post-incident review from Jira Operations by its ID. |
| Get Preference | `getPreference` | Get the value of a preference of the current user by key. |
| Get Priorities | `getPriorities` | Returns the list of all issue priorities. GET /rest/api/3/priority. |
| Get Priorities by Priority Scheme | `listPrioritiesByScheme` | Get all priorities associated with a given priority scheme. |
| Get Priority | `getPriority` | Returns an issue priority. GET /rest/api/3/priority/{id}. |
| Get Priority Scheme | `getPriorityScheme` | Get a specific priority scheme by scheme ID. |
| Get Priority Scheme Mappings | `getPrioritySchemeMappings` | Get suggested priority mappings for migrating issues between priority schemes. |
| Get Project | `getProject` | Get a project by ID or key. GET /rest/api/3/project/{projectIdOrKey}. Returns the full project object. |
| Get Project Category By ID | `getProjectCategoryById` | Get a project category by ID. GET /rest/api/3/projectCategory/{id}. Returns the category object. |
| Get Project Components | `getProjectComponents` | Get all components in a project. GET /rest/api/3/project/{projectIdOrKey}/components. Returns an array of component objects. |
| Get Project Components Paginated | `getProjectComponentsPaginated` | Get a paginated list of components in a project. GET /rest/api/3/project/{projectIdOrKey}/component. Returns a paginated page object. |
| Get Project Context Mapping | `getProjectContextMapping` | Returns a paginated list of context to project mappings for a custom field. GET /rest/api/3/field/{fieldId}/context/projectmapping. |
| Get Project Features | `getProjectFeatures` | Returns the features enabled for a project, including their state (ENABLED, DISABLED, COMING_SOON). |
| Get Project Issue Type Hierarchy | `getHierarchy` | Get the issue type hierarchy for a project. GET /rest/api/3/project/{projectId}/hierarchy. Returns the hierarchy levels. |
| Get Project Notification Scheme | `getNotificationSchemeForProject` | Get the notification scheme associated with a project. GET /rest/api/3/project/{projectKeyOrId}/notificationscheme. Returns the notification scheme object. |
| Get Project Property | `getProjectProperty` | Returns the value of a project property. Returns 404 if the project or property does not exist. |
| Get Project Property Keys | `getProjectPropertyKeys` | Returns all project property keys for the project. Returns 404 if the project is not found. |
| Get Project Role By ID | `getProjectRoleById` | Get a project role by ID (definition only, no actors). GET /rest/api/3/role/{id}. Returns the role object. |
| Get Project Role Details | `getProjectRoleDetails` | Get all project roles and their details for a project. GET /rest/api/3/project/{projectIdOrKey}/roledetails. Returns an array of role detail objects. |
| Get Project Role For Project | `getProjectRole` | Get details of a specific project role for a project. GET /rest/api/3/project/{projectIdOrKey}/role/{id}. Returns the role with its actors. |
| Get Project Role for Project | `getProjectRoleForProject` | Returns a project role's details and actors (users and groups) assigned to the role. Use this to see who is in a role on a specific project. |
| Get Project Roles For Project | `getProjectRoles` | Get the project roles available for a project, as a map of role name to role URL. GET /rest/api/3/project/{projectIdOrKey}/role. |
| Get Project Type By Key | `getProjectTypeByKey` | Get a project type by its key. GET /project/type/{projectTypeKey}. Returns the project type {key, formattedKey, descriptionI18nKey, icon, color}. |
| Get Project Usages By Status | `getProjectUsagesForStatus` | Returns projects that use a status. GET /rest/api/3/statuses/{statusId}/projectUsages. |
| Get Project Versions | `getProjectVersions` | Get all versions in a project. GET /rest/api/3/project/{projectIdOrKey}/versions. Returns an array of version objects. |
| Get Project Versions Paginated | `getProjectVersionsPaginated` | Get a paginated list of versions in a project. GET /rest/api/3/project/{projectIdOrKey}/version. Returns a paginated page object. |
| Get Projects | `getProjects` | Returns all projects associated with a board (Jira Software agile endpoint). BLOCKED: requires Jira Software scopes (read:board-scope:jira-software) not available in the current OAuth token. |
| Get Projects by Priority Scheme | `listProjectsByPriorityScheme` | Get all projects associated with a given priority scheme. |
| Get Projects for Issue Type Screen Scheme | `getProjectsForIssueTypeScreenScheme` | Returns a paginated list of projects associated with an issue type screen scheme. |
| Get Projects Full | `getProjectsFull` | Returns all projects statically associated with a board with full project details (Jira Software agile endpoint). BLOCKED: requires Jira Software scopes (read:board-scope:jira-software) not available in the current OAuth token. |
| Get Projects Using Issue Security Schemes | `getProjectsUsingSecuritySchemes` | Returns a paginated mapping of issue security schemes to projects. Can filter by scheme ID and project ID. |
| Get Quick Filter | `getQuickFilter` | Returns the quick filter for a given quick filter ID. The board that the quick filter belongs to can be determined from the response. |
| Get Recent Projects | `getRecent` | Get the user's most recently accessed projects. GET /rest/api/3/project/recent. Returns an array of project objects. |
| Get Related Work | `getRelatedWork` | Get related work items for a version. GET /rest/api/3/version/{id}/relatedwork. Returns an array of related work items. |
| Get Remote Issue Link By ID | `getRemoteIssueLinkById` | Get a single remote issue link by its ID. GET /issue/{issueIdOrKey}/remotelink/{linkId}. |
| Get Remote Issue Links | `getRemoteIssueLinks` | Get the remote issue links for a Jira issue. Optionally filter by globalId. GET /issue/{issueIdOrKey}/remotelink. Response is an array of remote link objects. |
| Get Remote Link By ID | `getRemoteLinkById` | Returns a specific remote link from Jira by its ID. |
| Get Reports For Board | `getReportsForBoard` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:board-scope:jira-software). Returns a list of all the reports available on the specified board. |
| Get Required Status Mappings for Workflow Scheme Update | `getRequiredStatusMappingsForWorkflowSchemeUpdate` | Returns the required status mappings for the passed new workflow scheme for a project when using the new workflow scheme update API. |
| Get Resolution | `getResolution` | Returns an issue resolution value. GET /rest/api/3/resolution/{id}. |
| Get Resolutions | `getResolutions` | Returns a list of all issue resolution values. GET /rest/api/3/resolution. |
| Get Selected Time Tracking Provider | `getSelectedTimeTrackingImplementation` | Returns the time tracking provider that is currently selected for the Jira instance. Returns an empty body (204) if time tracking is disabled. |
| Get Server Info | `getServerInfo` | Returns information about the Jira instance (version, build, deployment type, server time, timezone). |
| Get Share Permission | `getSharePermission` | Returns a single share permission for a filter. |
| Get Share Permissions | `getSharePermissions` | Returns the share permissions for a filter. |
| Get Sprint | `getSprint` | BLOCKED: OAuth token lacks Jira Software agile scopes (read:sprint:jira-software). Returns the sprint for a given sprint ID. The sprint will only be returned if the user can view the board that the sprint was created on. |
| Get Sprint Property | `getProperty` | Returns the value of the property with a given key from the sprint identified by the id. |
| Get Sprint Property Keys | `getPropertiesKeys` | Returns the keys of all properties for the sprint identified by the id. |
| Get Status | `getStatus` | Returns a status by ID or name. GET /rest/api/3/status/{idOrName}. |
| Get Status Category | `getStatusCategory` | Get a single status category by ID or key. |
| Get Status Transitions | `getStatusTransitions` | Returns a list of all status transitions and their sub-tasks. GET /rest/api/3/statustransitions. BLOCKED: Returns 401 'scope does not match' — endpoint requires additional OAuth scope not available in current connection. |
| Get Task | `getTask` | Get the status and progress of a long-running asynchronous task by task ID. |
| Get Time Tracking Settings | `getSharedTimeTrackingConfiguration` | Returns the time tracking settings (default unit, time format, working days/hours). |
| Get Transitions | `getTransitions` | Get the transitions available on an issue from its current status. GET /issue/{issueIdOrKey}/transitions. |
| Get Trashed Fields Paginated | `getTrashedFieldsPaginated` | Returns a paginated list of fields in the trash. GET /rest/api/3/field/search/trashed. |
| Get Universal Avatars | `getUniversalAvatars` | Returns the system and custom avatars for a project or issue type. Supply 'type' as 'project' or 'issuetype', and 'entityId' as the project/issue-type ID. |
| Get User | `getUser` | Get a user by accountId. Returns the user's details including accountId, displayName, email, groups and avatars. |
| Get User Default Columns | `getUserDefaultColumns` | Get the default issue table columns for the user. |
| Get User Email | `getUserEmail` | Get the email of a user by accountId (subject to privacy settings). BLOCKED: Requires 'read:email-address:jira' Beta OAuth scope restricted to Atlassian-approved Connect apps and Forge apps using asApp() — not available via standard OAuth 2.0 tokens. Returns 401 'Unauthorized; scope does not match'. |
| Get User Email Bulk | `getUserEmailBulk` | Get the emails for a list of users by accountId (subject to privacy settings). BLOCKED: Requires 'read:email-address:jira' Beta OAuth scope restricted to Atlassian-approved Connect apps and Forge apps using asApp() — not available via standard OAuth 2.0 tokens. Returns 401 'Unauthorized; scope does not match'. |
| Get User Groups | `getUserGroups` | Get the groups a user belongs to by accountId. |
| Get User Property | `getUserProperty` | Returns the value of a user property. Returns 404 if the user or property does not exist. |
| Get User Property Keys | `getUserPropertyKeys` | Returns the keys of all properties for a user. Note: This operation does not access the user's profile properties. Returns 404 if the user is not found. |
| Get Users From Group | `getUsersFromGroup` | Get a paginated list of the users that are members of a group. |
| Get Version | `getVersion` | Get a project version by ID. GET /rest/api/3/version/{id}. Returns the version object. |
| Get Version Related Issues Count | `getVersionRelatedIssues` | Get counts of issues related to a version. GET /rest/api/3/version/{id}/relatedIssueCounts. Returns affected/fixed counts. |
| Get Version Unresolved Issues Count | `getVersionUnresolvedIssues` | Get counts of unresolved issues for a version. GET /rest/api/3/version/{id}/unresolvedIssueCount. Returns issue counts. |
| Get Votes | `getVotes` | Get the votes on a Jira issue. GET /issue/{issueIdOrKey}/votes. |
| Get Workflow Capabilities | `getWorkflowCapabilities` | Returns the list of workflow capabilities. You MUST supply either workflowId, or BOTH projectId and issueTypeId - otherwise Jira returns 400 "You must provide either a workflow ID, or both project and issue type IDs." |
| Get Workflow for Issue Type in Draft Scheme | `getDraftWorkflowSchemeIssueType` | Returns the workflow associated with an issue type in the draft workflow scheme. BLOCKED: Returns 404 'The workflow scheme does not have a draft.' — requires a draft workflow scheme to exist, which only occurs during active workflow updates. |
| Get Workflow for Issue Type in Scheme | `getWorkflowSchemeIssueType` | Returns the workflow associated with an issue type in a workflow scheme. |
| Get Workflow Project Issue Type Usages | `getWorkflowProjectIssueTypeUsages` | Returns a list of issue types in a project that are using a given workflow. |
| Get Workflow Project Usages | `getWorkflowProjectUsages` | Returns a list of projects that are using a given workflow. |
| Get Workflow Scheme | `getWorkflowScheme` | Returns a workflow scheme by its ID. |
| Get Workflow Scheme Project Associations | `getWorkflowSchemeProjectAssociations` | Returns a list of the workflow schemes associated with a list of projects. Each returned workflow scheme includes a list of the requested projects associated with it. |
| Get Workflow Scheme Project Usages | `getWorkflowSchemeProjectUsages` | Returns the projects that are using a given workflow scheme. |
| Get Workflow Scheme Usages for Workflow | `getWorkflowSchemeUsagesForWorkflow` | Returns a list of workflow schemes that are using a given workflow. |
| Get Workflow Transition Properties | `getWorkflowTransitionProperties` | Returns the properties associated with a workflow transition. Workflow and transition must be specified. |
| Get Workflow Transition Rule Configurations | `getWorkflowTransitionRuleConfigs` | Returns a paginated list of workflows with transition rules. The workflows can be filtered to return only those containing workflow transition rules of a specific type. |
| Get Workflow Usages By Status | `getWorkflowUsagesForStatus` | Returns workflows that use a status. GET /rest/api/3/statuses/{statusId}/workflowUsages. |
| Get Worklog | `getWorklog` | Return a worklog of an issue. |
| Get Worklog Property | `getWorklogProperty` | Returns the key and value of a worklog's property. Returns 404 if the issue, worklog, or property does not exist. |
| Get Worklog Property Keys | `getWorklogPropertyKeys` | Returns the URLs and keys of the properties of a worklog. Returns 404 if the issue or worklog does not exist. |
| Get Worklogs For IDs | `getWorklogsForIds` | Return worklog details for a list of worklog IDs. Response is a JSON array of worklog objects. |
| Link Issues | `linkIssues` | Create a link between two issues. POST /issueLink. Provide type, inwardIssue, outwardIssue, and optionally a comment. |
| List Application Roles | `listApplicationRoles` | Returns all application roles. In Jira, application roles are managed using the Application access configuration page. |
| List Classification Levels | `listClassificationLevels` | Get all data classification levels available for the Jira instance. |
| List Field Configuration Schemes | `listFieldConfigurationSchemes` | Returns a paginated list of field configuration schemes. GET /rest/api/3/fieldconfigurationscheme |
| List Field Configurations | `listFieldConfigurations` | Returns a paginated list of all field configurations. GET /rest/api/3/fieldconfiguration |
| List Issue Type Schemes | `listIssueTypeSchemes` | Returns a paginated list of issue type schemes. GET /rest/api/3/issuetypescheme |
| List Issue Type Screen Schemes | `listIssueTypeScreenSchemes` | Returns a paginated list of issue type screen schemes. Only issue type screen schemes used in classic projects are returned. |
| List Plan Teams | `listPlanTeams` | Get all teams in a plan (paginated). Returns both Atlassian teams and plan-only teams. |
| List Plans | `listPlans` | Get all plans (Advanced Roadmaps) paginated. Returns plans with cursor-based pagination. |
| List Priority Schemes | `listPrioritySchemes` | Get all priority schemes with pagination. Supports filtering by priority ID, scheme ID, scheme name, and ordering. |
| List Registered Webhooks | `listRegisteredWebhooks` | List the Jira dynamic webhooks currently registered for the calling OAuth app (paginated). |
| List Screen Schemes | `listScreenSchemes` | Returns a paginated list of screen schemes. Only screen schemes used in classic projects are returned. |
| List Screen Tab Fields | `listScreenTabFields` | Returns all fields for a screen tab. |
| List Screen Tabs | `listScreenTabs` | Returns the list of tabs for a screen. |
| List Screens | `listScreens` | Returns a paginated list of all screens or those specified by one or more screen IDs. |
| List Status Categories | `listStatusCategories` | Get all status categories. Status categories are the high-level groupings of statuses (e.g., To Do, In Progress, Done). |
| List UI Modifications | `listUiModifications` | Get all UI modifications for the Jira instance. UI modifications allow customizing the Jira UI. |
| List Workflow History Entries | `listWorkflowHistory` | Returns a list of history entries for a specific workflow identified by its ID. |
| List Workflow Schemes | `listWorkflowSchemes` | Returns a paginated list of all workflow schemes, not including draft workflow schemes. |
| Load Issue Type Avatar | `createIssueTypeAvatar` | Load an avatar for the issue type. POST /rest/api/3/issuetype/{id}/avatar2. BLOCKED: fastn platform cannot stream raw binary image uploads — the bodyType:binary bodyTemplate path corrupts image bytes before they reach Jira (400 image could not be read). Classified business-400: platform binary upload limitation. |
| Load Universal Avatar | `loadUniversalAvatar` | Loads a custom avatar for a project or issue type from a supplied image. The image must be supplied as a multipart/form-data or binary body. Returns the cropped avatar. |
| Merge Versions | `mergeVersions` | Merge a version into another version. PUT /rest/api/3/version/{id}/mergeto/{moveIssuesTo}. The source version is deleted and its issues moved. Returns 204 No Content. |
| Migrate JQL Queries (user IDs to account IDs) | `migrateQueries` | Convert user identifiers to account IDs in JQL queries. POST /jql/pdcleaner. |
| Move Custom Field To Trash | `trashCustomField` | Moves a custom field to trash. POST /rest/api/3/field/{id}/trash. |
| Move Issue Types In Issue Type Scheme | `moveIssueTypesInIssueTypeScheme` | Changes the order of issue types in an issue type scheme. PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move |
| Move Issues To Backlog | `moveIssuesToBacklog` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:sprint:jira-software). Move issues to the backlog. Removes issues from all sprints if they are assigned. Max 50 issues per call. |
| Move Issues To Backlog For Board | `moveIssuesToBacklogForBoard` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:board-scope:jira-software). Move issues to the backlog of a particular board (if they are already on that board). Optionally rank and place the issues. Max 50 issues per call. |
| Move Issues To Board | `moveIssuesToBoard` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:board-scope:jira-software). Move issues from the backlog to the board (if they are not already in the backlog of that board). Optionally rank and place the issues. Max 50 issues per call. |
| Move Issues To Epic | `moveIssuesToEpic` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:epic:jira-software). Moves issues to an epic, for a given epic id. Issues can be only in a single epic at the same time. Max 50 issues per call. |
| Move Issues To Sprint And Rank | `moveIssuesToSprintAndRank` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:sprint:jira-software). Moves issues to a sprint, for a given sprint ID. Issues can only be moved to open or active sprints. Max 50 issues per call. Optionally rank. |
| Move Priorities | `movePriorities` | Changes the order of issue priorities. PUT /rest/api/3/priority/move. |
| Move Resolutions | `moveResolutions` | Changes the order of issue resolutions. PUT /rest/api/3/resolution/move. |
| Move Screen Tab | `moveScreenTab` | Moves a screen tab. |
| Move Screen Tab Field | `moveScreenTabField` | Moves a screen tab field. If after and position are provided in the request, position is ignored. |
| Move Version | `moveVersion` | Move (reorder) a version within a project. POST /rest/api/3/version/{id}/move. Provide either after or position. Returns the moved version object. |
| Parse JQL Queries | `parseJqlQueries` | Parse and validate JQL queries into structured form. POST /jql/parse. validation query param is required. |
| Partial Update Project Role | `partialUpdateProjectRole` | Partially update a project role's name and/or description. POST /rest/api/3/role/{id}. Returns the updated role object. |
| Partially Update Epic | `partiallyUpdateEpic` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:epic:jira-software). Performs a partial update of the epic. A partial update means that fields not present in the request body are not updated. |
| Partially Update Sprint | `partiallyUpdateSprint` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:sprint:jira-software). Performs a partial update of a sprint. A partial update means that fields not present in the request body are not updated. Sprint state can be set to active only if board has at most one active sprint already. |
| Preview Workflow | `previewWorkflow` | Returns a preview of a workflow, showing its layout and structure based on project and issue type filters. |
| Publish Draft Workflow Scheme | `publishDraftWorkflowScheme` | Publishes a draft workflow scheme. After publishing the active workflow scheme is updated with the status mappings from the draft. Optionally validates the draft before publishing. |
| Rank Epics | `rankEpics` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:epic:jira-software). Moves (ranks) an epic before or after a given epic. If rankCustomFieldId is not defined, the default rank field will be used. |
| Rank Issues | `rankIssues` | Moves (ranks) issues before or after a given issue. At most 50 issues may be ranked at once. This operation may fail for some issues if the user lacks permission. |
| Read Workflow Version from History | `readWorkflowHistory` | Returns a specific version of a workflow from its history using the workflow ID and version number. |
| Refresh Webhooks | `refreshWebhooks` | Extend the life of the supplied Jira dynamic webhooks by 30 days. Sends a JSON body { webhookIds: [number] }. |
| Register Webhooks | `registerWebhooks` | Register Jira dynamic webhooks (OAuth-app-only). POSTs an array of webhook definitions (events + jqlFilter) and a callback URL; returns webhookRegistrationResult with createdWebhookId per entry. |
| Remove Atlassian Team from Plan | `removeAtlassianTeamFromPlan` | Remove an Atlassian team from a plan. Returns 204 on success. |
| Remove Custom Field Context From Projects | `removeCustomFieldContextFromProjects` | Removes a custom field context from projects. POST /rest/api/3/field/{fieldId}/context/{contextId}/project/remove. BLOCKED: Removing all projects from a context would make it global, but a global context already exists per Jira's 'one global context' rule. Action config is correct. |
| Remove Filter As Favourite | `deleteFavouriteForFilter` | Removes a filter as a favorite for the user. Returns the updated filter. |
| Remove Gadget From Dashboard | `removeGadget` | Removes a gadget from a dashboard. The remaining gadgets are moved up to fill the gap. |
| Remove Group | `removeGroup` | Delete a group. Optionally transfer comment/worklog restrictions to a swap group. |
| Remove Issue Security Level | `removeIssueSecurityLevel` | Deletes an issue security level. Issues using this level are migrated to another level if specified. Requires Administer Jira global permission. |
| Remove Issue Type From Issue Type Scheme | `removeIssueTypeFromIssueTypeScheme` | Removes an issue type from an issue type scheme. DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId} |
| Remove Issue Types From Context | `removeIssueTypesFromContext` | Removes issue types from a custom field context. POST /rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove. Returns 204 on success. |
| Remove Issue Types From Field Configuration Scheme | `removeIssueTypesFromFieldConfigurationScheme` | Removes issue types from the field configuration scheme's issue type mappings. POST /rest/api/3/fieldconfigurationscheme/{id}/mapping/delete |
| Remove Issues From Epic | `removeIssuesFromEpic` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:epic:jira-software). Removes issues from epics. The user needs Edit Issue permission. Max 50 issues per call. |
| Remove Mappings from Issue Type Screen Scheme | `removeMappingsFromIssueTypeScreenScheme` | Removes issue type to screen scheme mappings from an issue type screen scheme. |
| Remove Member from Issue Security Level | `removeMemberFromSecurityLevel` | Removes a member from an issue security level. Requires Administer Jira global permission. |
| Remove Notification from Notification Scheme | `removeNotificationFromScheme` | Removes a notification from a notification scheme. Requires Administer Jira global permission. |
| Remove Screen Tab Field | `removeScreenTabField` | Removes a field from a screen tab. |
| Remove User From Group | `removeUserFromGroup` | Remove a user from a group. |
| Remove Vote | `removeVote` | Remove the calling user's vote from an issue. DELETE /issue/{issueIdOrKey}/votes. |
| Remove Watcher | `removeWatcher` | Remove a user as a watcher of an issue. DELETE /issue/{issueIdOrKey}/watchers with accountId query param. |
| Reorder Custom Field Options (Context) | `reorderCustomFieldOptions` | Changes the order of custom field options or cascading options in a context. PUT /rest/api/3/field/{fieldId}/context/{contextId}/option/move. |
| Replace Custom Field Options | `replaceCustomFieldOption` | Replaces a custom field option in issues and deletes it. DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue. Query params replaceWith and jql set explicitly. |
| Reset Columns | `resetColumns` | Reset the columns of a filter to the default columns. |
| Reset User Default Columns | `resetUserColumns` | Reset the default issue table columns for the user to the system default. |
| Restore Custom Field From Trash | `restoreCustomField` | Restores a custom field from trash. POST /rest/api/3/field/{id}/restore. |
| Restore Project | `restoreProject` | Restore a deleted or archived project. POST /rest/api/3/project/{projectIdOrKey}/restore. Returns the restored project object. |
| Sanitize JQL Queries | `sanitiseJqlQueries` | Sanitize JQL queries (remove info the account cannot view). POST /jql/sanitize. |
| Search For Dashboards | `getDashboardsPaginated` | Returns a paginated list of dashboards. Search by name, account, group, project, or status. |
| Search For Filters | `getFiltersPaginated` | Returns a paginated list of filters. Use this to search for filters by name, account, group, project, or ID. |
| Search Issue Security Schemes | `searchSecuritySchemes` | Returns a paginated list of issue security schemes. Supports filtering by scheme ID and project ID. |
| Search Issues by JQL (GET) | `searchAndReconsileIssuesUsingJql` | Search for issues using JQL enhanced search (GET /search/jql). Token-paginated via nextPageToken. This is the NEW search endpoint (legacy /search was removed). |
| Search Issues by JQL (POST) | `searchAndReconsileIssuesUsingJqlPost` | Search for issues using JQL enhanced search (POST /search/jql). Token-paginated. This is the NEW search endpoint (legacy /search was removed). |
| Search Priorities | `searchPriorities` | Returns a paginated list of priorities. GET /rest/api/3/priority/search. |
| Search Projects | `searchProjects` | Get projects paginated, with filtering/ordering. GET /rest/api/3/project/search. Returns a paginated page object with values array. |
| Search Resolutions | `searchResolutions` | Returns a paginated list of resolutions. GET /rest/api/3/resolution/search. |
| Search Statuses Paginated | `searchStatuses` | Returns a paginated list of statuses that match a search. GET /rest/api/3/statuses/search. |
| Search Workflows (Classic) | `searchWorkflows` | Get a paginated list of classic workflows using the GET /workflow/search endpoint. Supports filtering by name, activity status, and ordering. |
| Search Workflows (New API) | `searchWorkflowsNew` | Search for workflows using the new workflows API. Returns a paginated list of workflows with expanded information. |
| Select Time Tracking Provider | `selectTimeTrackingImplementation` | Selects a time tracking provider for the Jira instance. |
| Send Notification for Issue | `notify` | Send an email notification for an issue. POST /issue/{issueIdOrKey}/notify. Returns 204. |
| Set Actors for Project Role | `setActorsForProjectRole` | Sets actors (users and groups) for a project role, replacing any existing actors. Returns the updated project role. |
| Set Board Property | `setBoardProperty` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:board-scope:jira-software). Sets the value of the specified board's property. The value is an arbitrary JSON object passed in the body. |
| Set Columns | `setColumns` | Set the columns for a filter. The columns are an array of field IDs. |
| Set Comment Property | `setCommentProperty` | Creates or updates the value of a property for a comment. A new property is created or the value of an existing property is updated. |
| Set Context Default Values | `setContextDefaultValues` | Sets default values for a custom field context. PUT /rest/api/3/field/{fieldId}/context/defaultValue. Returns 204 on success. |
| Set Custom Field Value | `setCustomFieldValue` | Sets the value of a custom field on one or more issues. PUT /rest/api/3/app/field/{fieldIdOrKey}/value. BLOCKED: This API works only with fields provided by Forge apps — not usable with standard Jira custom fields." |
| Set Dashboard Item Property | `setDashboardItemProperty` | Sets the value of a dashboard item property. The value is an arbitrary JSON object. |
| Set Default Issue Security Levels | `setDefaultSecurityLevels` | Sets default issue security levels for schemes. Each entry maps a scheme ID to its default security level ID. |
| Set Default Priority | `setDefaultPriority` | Sets default issue priority. PUT /rest/api/3/priority/default. |
| Set Default Resolution | `setDefaultResolution` | Sets default issue resolution. PUT /rest/api/3/resolution/default. |
| Set Default Share Scope | `setDefaultShareScope` | Sets the default sharing settings for new filters and dashboards for the user. |
| Set Issue Property | `setIssueProperty` | Sets the value of an issue's property. Use this resource to store custom data against an issue. A new property is created or the value of an existing property is overwritten. |
| Set Issue Type Property | `setIssueTypeProperty` | Creates or updates the value of the issue type property. A new property is created or the value of an existing property is updated. |
| Set Issue Types for Workflow in Draft Scheme | `setDraftWorkflowSchemeWorkflow` | Sets the issue types for a workflow in the draft workflow scheme. |
| Set Issue Types for Workflow in Scheme | `setWorkflowSchemeWorkflow` | Sets the issue types for a workflow in a workflow scheme. The workflow can also be set as the default workflow for the workflow scheme. |
| Set Locale | `setLocale` | Set the locale of the current user (deprecated by Atlassian but still supported). |
| Set Preference | `setPreference` | Set the value of a preference of the current user by key. The value is sent as the raw request body. |
| Set Project Avatar | `setProjectAvatar` | Sets the project avatar. Use the avatar ID from getAllProjectAvatars or createProjectAvatar. |
| Set Project Property | `setProjectProperty` | Sets the value of the project property. A new property is created or the value of an existing property is updated. |
| Set Sprint Property | `setProperty` | Sets the value of the specified sprint's property. The value is an arbitrary JSON object passed in the body. |
| Set Time Tracking Settings | `setSharedTimeTrackingConfiguration` | Sets the time tracking settings (default unit, time format, working days/hours). |
| Set User Default Columns | `setUserColumns` | Set the default issue table columns for the user. The columns are passed as form-encoded 'columns' values; pass column ids via the columns array. |
| Set User Property | `setUserProperty` | Sets the value of a user's property. A new property is created or the value of an existing property is updated. Use this to store custom data against a Jira user. |
| Set Workflow for Issue Type in Draft Scheme | `setDraftWorkflowSchemeIssueType` | Sets the workflow for an issue type in the draft workflow scheme. |
| Set Workflow for Issue Type in Scheme | `setWorkflowSchemeIssueType` | Sets the workflow for an issue type in a workflow scheme. |
| Set Worklog Property | `setWorklogProperty` | Sets the value of a worklog's property. A new property is created or the value of an existing property is updated. |
| Store Development Information | `storeDevelopmentInformation` | Stores development information (repositories, commits, branches, PRs) linked to Jira issues via the devinfo API. |
| Submit Builds | `submitBuilds` | Submits build data for one or more Jira issues. Builds are linked to issues and shown in the Jira issue view. |
| Submit Deployments | `submitDeployments` | Submits deployment data for one or more Jira issues. Deployments are linked to issues and shown in the Jira issue view. |
| Submit DevOps Components | `submitDevOpsComponents` | Submits DevOps component data to Jira to associate CI/CD components with Jira projects. |
| Submit Feature Flags | `submitFeatureFlags` | Submits feature flag data for one or more Jira issues. Feature flags are linked to issues and shown in the Jira issue view. |
| Submit Operations Data | `submitOperationsData` | Submits Operations data (incidents and post-incident reviews) to Jira for display in DevOps views. |
| Submit Operations Workspaces | `submitOperationsWorkspaces` | Submits (links) Operations workspace IDs to the Jira site. |
| Submit Remote Links | `submitRemoteLinks` | Submits remote link data to associate external resources with Jira issues. |
| Swap Sprint | `swapSprint` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:sprint:jira-software). Swaps the position of a sprint with another sprint. |
| Switch Workflow Scheme for Project | `switchWorkflowSchemeForProject` | Switches the workflow scheme for a project. Allows migrating statuses between workflow schemes. |
| Toggle Features | `toggleFeatures` | Enables or disables a board feature. |
| Toggle Project Feature | `toggleProjectFeature` | Sets the state (ENABLED or DISABLED) of a project feature identified by featureKey. Returns all project features. |
| Transition Issue | `transitionIssue` | Perform a transition on an issue (e.g. move to Done). POST /issue/{issueIdOrKey}/transitions. transition is {"id":"&lt;transitionId&gt;"} from getTransitions. Returns 204. |
| Trash Plan | `trashPlan` | Move a plan to trash by ID. Returns 204 on success. |
| Unarchive Issues (by ID/Key) | `unarchiveIssues` | Unarchive issues by issue keys/ID. PUT /issue/unarchive. |
| Update Announcement Banner | `updateAnnouncementBanner` | Update the announcement banner configuration. Returns 204 on success. |
| Update Atlassian Team in Plan | `updateAtlassianTeamInPlan` | Update an Atlassian team's settings in a plan using JSON Patch operations. |
| Update Comment | `updateComment` | Update a comment on an issue. The body field is Atlassian Document Format (ADF). |
| Update Component | `updateComponent` | Update a project component. PUT /rest/api/3/component/{id}. Returns the updated component object. |
| Update Custom Field | `updateCustomField` | Updates a custom field. PUT /rest/api/3/field/{fieldId}. |
| Update Custom Field Configuration | `updateCustomFieldConfiguration` | Updates the configuration of a custom field created by a Connect or Forge app. PUT /rest/api/3/app/field/{fieldIdOrKey}/context/configuration. BLOCKED: This API works only with fields provided by Forge apps — not usable with standard Jira custom fields. |
| Update Custom Field Context | `updateCustomFieldContext` | Updates a custom field context. PUT /rest/api/3/field/{fieldId}/context/{contextId}. Returns 204 on success. |
| Update Custom Field Options (Context) | `updateCustomFieldOption` | Updates options for a custom field context. PUT /rest/api/3/field/{fieldId}/context/{contextId}/option. |
| Update Dashboard | `updateDashboard` | Updates a dashboard, replacing all the dashboard details with the supplied values. The user must be the owner. |
| Update Default Screen Scheme for Issue Type Screen Scheme | `updateDefaultScreenSchemeForIssueTypeScreenScheme` | Updates the default screen scheme of an issue type screen scheme. The default screen scheme is used for all unmapped issue types. |
| Update Default Workflow | `updateWorkflowSchemeDefault` | Sets the default workflow for a workflow scheme. Optionally updates the default workflow for the scheme's draft. |
| Update Draft Default Workflow | `updateDraftWorkflowSchemeDefault` | Sets the default workflow for a draft workflow scheme. |
| Update Draft Workflow Scheme | `updateDraftWorkflowScheme` | Updates a draft workflow scheme. If a draft workflow scheme does not exist for the active workflow scheme, then a draft is created. |
| Update Field Configuration | `updateFieldConfiguration` | Updates a field configuration. PUT /rest/api/3/fieldconfiguration/{id} |
| Update Field Configuration Items | `updateFieldConfigurationItems` | Updates fields in a field configuration. PUT /rest/api/3/fieldconfiguration/{id}/fields |
| Update Field Configuration Scheme | `updateFieldConfigurationScheme` | Updates a field configuration scheme. PUT /rest/api/3/fieldconfigurationscheme/{id} |
| Update Filter | `updateFilter` | Update an existing filter by ID. Only the owner or an admin can update a filter. |
| Update Gadget On Dashboard | `updateGadget` | Changes the title, position, and color of a gadget on a dashboard. |
| Update Issue (Plain Text) | `updateIssuePlainText` | Partially update a Jira issue from flat inputs: PUT /rest/api/2/issue/{issueIdOrKey}?returnIssue=true (v2 accepts a plain-text description, so no ADF is needed). Only the fields provided are sent; others are unchanged. priority and assignee are objects ({name} / {accountId}). Status changes need a workflow transition and are not done here. Returns the updated issue. |
| Update Issue Link Type | `updateIssueLinkType` | Update an issue link type by its ID. PUT /issueLinkType/{issueLinkTypeId}. |
| Update Issue Security Level | `updateIssueSecurityLevel` | Updates the name and description of an issue security level. Requires Administer Jira global permission. |
| Update Issue Security Scheme | `updateIssueSecurityScheme` | Updates the issue security scheme. Requires Administer Jira global permission. |
| Update Issue Type | `updateIssueType` | Updates an issue type. PUT /rest/api/3/issuetype/{id}. |
| Update Issue Type Scheme | `updateIssueTypeScheme` | Updates an issue type scheme. PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId} |
| Update Issue Type Screen Scheme | `updateIssueTypeScreenScheme` | Updates an issue type screen scheme. |
| Update Multiple Custom Field Values | `updateMultipleCustomFieldValues` | Updates the value of one or more custom fields added by Connect or Forge apps on one or more issues. POST /rest/api/3/app/field/value. Returns 204 on success. |
| Update Notification Scheme | `updateNotificationScheme` | Updates a notification scheme. Requires Administer Jira global permission. |
| Update Permission Scheme | `updatePermissionScheme` | Updates a permission scheme. Requires Administer Jira global permission. |
| Update Plan | `updatePlan` | Update an existing plan using JSON Patch format. Accepts an array of patch operations to update plan fields. |
| Update Plan-Only Team | `updatePlanOnlyTeam` | Update a plan-only team's settings in a plan using JSON Patch operations. |
| Update Priority | `updatePriority` | Updates an issue priority. PUT /rest/api/3/priority/{id}. |
| Update Priority Scheme | `updatePriorityScheme` | Update an existing priority scheme. Returns 202 with a task for async processing. |
| Update Project | `updateProject` | Update a project. PUT /rest/api/3/project/{projectIdOrKey}. Only the fields provided are changed. Returns the updated project object. |
| Update Project Category | `updateProjectCategory` | Update a project category. PUT /rest/api/3/projectCategory/{id}. Returns the updated category object. |
| Update Related Work | `updateRelatedWork` | Update a related work item for a version. PUT /rest/api/3/version/{id}/relatedwork. Pass relatedWorkId in the body. Returns the updated related work item. |
| Update Remote Issue Link | `updateRemoteIssueLink` | Update a remote issue link by its ID. PUT /issue/{issueIdOrKey}/remotelink/{linkId}. |
| Update Resolution | `updateResolution` | Updates an issue resolution. PUT /rest/api/3/resolution/{id}. |
| Update Screen | `updateScreen` | Updates a screen. |
| Update Screen Scheme | `updateScreenScheme` | Updates a screen scheme. Only screen schemes used in classic projects can be updated. |
| Update Screen Tab | `updateScreenTab` | Updates the name of a screen tab. |
| Update Sprint | `updateSprint` | BLOCKED: OAuth token lacks Jira Software agile scopes (write:sprint:jira-software). Performs a full update of a sprint. A full update means that the result will be exactly the same as the request body. Any fields not present in the request will be set to null. |
| Update UI Modification | `updateUiModification` | Update an existing UI modification. Returns 204 on success. |
| Update Version | `updateVersion` | Update a project version. PUT /rest/api/3/version/{id}. Returns the updated version object. |
| Update Workflow Scheme | `updateWorkflowScheme` | Updates a workflow scheme, including the name, default workflow, issue type to project mappings, and more. If the workflow scheme is active (that is, being used by at least one project), then a draft workflow scheme is created or updated instead. |
| Update Workflow Scheme (New API) | `updateWorkflowSchemeNew` | Updates a workflow scheme using the new API. Allows updating the scheme's name, description, default workflow, and issue type mappings. |
| Update Workflow Transition Property | `updateWorkflowTransitionProperty` | Updates a workflow transition by changing the property value. Workflow must be inactive or the transition must be a global transition. |
| Update Workflow Transition Rule Configurations | `updateWorkflowTransitionRuleConfigs` | Updates configuration of workflow transition rules. Only Atlassian Connect app administrators can use this operation. |
| Update Worklog | `updateWorklog` | Update a worklog on an issue. The comment field is Atlassian Document Format (ADF). |
| Validate Create Workflows | `validateCreateWorkflows` | Validates a workflow creation request without executing it. Returns validation errors if any. |
| Validate Update Workflows | `validateUpdateWorkflows` | Validates a workflow update request without executing it. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Comment Created | `comment_created` | Triggered when a comment is added to an issue. |
| Comment Deleted | `comment_deleted` | Triggered when an issue comment is deleted. |
| Comment Updated | `comment_updated` | Triggered when an issue comment is updated. |
| Issue Created | `jira:issue_created` | Triggered when an issue is created. |
| Issue Deleted | `jira:issue_deleted` | Triggered when an issue is deleted. |
| Issue Property Deleted | `issue_property_deleted` | Triggered when an issue entity property is deleted. |
| Issue Property Set | `issue_property_set` | Triggered when an issue entity property is set. |
| Issue Updated | `jira:issue_updated` | Triggered when an issue is updated. |
