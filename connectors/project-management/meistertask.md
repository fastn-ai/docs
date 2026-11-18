---
description: "MeisterTask is a task and project management tool."
hidden: true
---

# MeisterTask

MeisterTask is a task and project management tool. Manage projects, sections, tasks, subtasks, checklists, comments, labels, attachments, custom fields, time tracking, and team members via the MeisterTask REST API.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [meistertask.com](https://meistertask.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 95 |
| **Events** | 0 |
| **Slug** | `meistertask` |

## Use it

Add MeisterTask from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.meistertask.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Checklist To Project | `addChecklistToProject` | Create a checklist on a project. |
| Add Checklist To Task | `addChecklistToTask` | Create a checklist on a task. |
| Add Label To Task | `addLabelToTask` | Attach an existing project label to a task. |
| Add Project Membership | `addProjectMembership` | Add a team or group membership to a project. Business plan only. |
| Add Project Right | `addProjectRight` | Grant a person access to a project by email, with an optional role. |
| Add Task Relationship | `addTaskRelationship` | Create a relationship from one task to another. |
| Add Task Subscription | `addTaskSubscription` | Add a person as a follower of a task. Only project members can follow; the current assignee cannot. |
| Create Attachment | `createAttachment` | Upload a file attachment to a task. The file is sent as multipart form-data. |
| Create Checklist Item | `createChecklistItem` | Add an item to a checklist. |
| Create Comment | `createComment` | Add a comment to a task. |
| Create Custom Field | `createCustomField` | Set a custom field value on a task. Business plan only. |
| Create Custom Field Type | `createCustomFieldType` | Create a custom field type in a project. Business plan only. |
| Create Dropdown Item | `createDropdownItem` | Create a dropdown item for a custom field type. Business plan only. |
| Create Label | `createLabel` | Create a new label (tag) in a project. |
| Create Project | `createProject` | Create a new project. A share_mode is required (1 or 2). |
| Create Project Image | `createProjectImage` | Upload a new project icon image. The file is sent as multipart form-data. |
| Create Section | `createSection` | Create a new section within a project. |
| Create Subtask | `createSubtask` | Create a subtask under an existing task and link it to the parent atomically. |
| Create Task | `createTask` | Create a new task within a section. |
| Create Timeline Item | `createTimelineItem` | Create a timeline item (schedule) for a task. Business plan only. |
| Create Work Interval | `createWorkInterval` | Start or record a time-tracking work interval on a task. Omit finished_at to start an ongoing interval. |
| Delete Attachment | `deleteAttachment` | Delete an attachment from its task. |
| Delete Checklist | `deleteChecklist` | Delete a checklist. |
| Delete Checklist Item | `deleteChecklistItem` | Delete a checklist item. |
| Delete Comment | `deleteComment` | Delete a comment from its task. |
| Delete Custom Field | `deleteCustomField` | Delete a custom field value from a task. Business plan only. |
| Delete Custom Field Type | `deleteCustomFieldType` | Delete a custom field type. Business plan only. |
| Delete Dropdown Item | `deleteDropdownItem` | Delete a dropdown item. Business plan only. |
| Delete Label | `deleteLabel` | Delete a label from its project. |
| Delete Project Image | `deleteProjectImage` | Remove a project's icon image. |
| Delete Work Interval | `deleteWorkInterval` | Delete a work interval. |
| Disable Project Setting | `disableProjectSetting` | Disable a previously enabled project setting. |
| Duplicate Project | `duplicateProject` | Duplicate an existing project, optionally including its tasks, checklists, labels, attachments, and rights. |
| Enable Project Setting | `enableProjectSetting` | Enable a feature for a project, such as time tracking or task relationships. |
| Get Attachment | `getAttachment` | Retrieve a single attachment by its ID. |
| Get Checklist | `getChecklist` | Retrieve a single checklist by its ID. |
| Get Checklist Item | `getChecklistItem` | Retrieve a single checklist item by its ID. |
| Get Comment | `getComment` | Retrieve a single comment by its ID. |
| Get Current Person | `getCurrentPerson` | Retrieve the profile of the currently authenticated MeisterTask user, including id, name, and email. |
| Get Custom Field | `getCustomField` | Retrieve a single custom field value by its ID. Business plan only. |
| Get Custom Field Type | `getCustomFieldType` | Retrieve a single custom field type by its ID. Business plan only. |
| Get Dropdown Item | `getDropdownItem` | Retrieve a single dropdown item by its ID. Business plan only. |
| Get Group | `getGroup` | Retrieve a single group by its ID. Business plan only. |
| Get Label | `getLabel` | Retrieve a single label by its ID. |
| Get Person | `getPerson` | Retrieve a single person by their ID. |
| Get Project | `getProject` | Retrieve a single project by its ID. |
| Get Project Image | `getProjectImage` | Retrieve the icon image of a project. |
| Get Project Members | `getProjectMembers` | List the members of a project, optionally including full person records. |
| Get Section | `getSection` | Retrieve a single section by its ID. |
| Get Task | `getTask` | Retrieve a single task by its ID. |
| Get Task Label | `getTaskLabel` | Retrieve a single task label by its ID. |
| Get Task Timeline Item | `getTaskTimelineItem` | Retrieve the timeline item of a task. Business plan only. |
| List Checklist Items | `listChecklistItems` | List all items of a checklist. |
| List Custom Field Types | `listCustomFieldTypes` | List all custom field types defined in a project. Business plan only. |
| List Dropdown Items | `listDropdownItems` | List all dropdown items of a custom field type. Business plan only. |
| List Groups | `listGroups` | List all groups in the team. Business plan only. |
| List Persons | `listPersons` | List all persons the authenticated user can access. |
| List Project Checklists | `listProjectChecklists` | List all checklists defined in a project. |
| List Project Labels | `listProjectLabels` | List all labels (tags) defined in a project. |
| List Project Persons | `listProjectPersons` | List all persons who have access to a project. |
| List Project Settings | `listProjectSettings` | List the settings enabled for a project. |
| List Project Tasks | `listProjectTasks` | List all tasks within a project. |
| List Project Work Intervals | `listProjectWorkIntervals` | List all time-tracking work intervals in a project. |
| List Projects | `listProjects` | List all projects the authenticated user can access, optionally filtered by status. |
| List Section Tasks | `listSectionTasks` | List all tasks within a section. |
| List Sections | `listSections` | List all sections the authenticated user can access. |
| List Subtasks | `listSubtasks` | List all subtasks of a task. |
| List Task Attachments | `listTaskAttachments` | List all attachments on a task. |
| List Task Checklist Items | `listTaskChecklistItems` | List all checklist items across all checklists of a task. |
| List Task Checklists | `listTaskChecklists` | List all checklists on a task. |
| List Task Comments | `listTaskComments` | List all comments on a task. |
| List Task Custom Fields | `listCustomFields` | List all custom field values on a task. Business plan only. |
| List Task Labels | `listTaskLabels` | List all label attachments (task labels) of a task. |
| List Task Relationships | `listTaskRelationships` | List all relationships of a task. |
| List Task Subscriptions | `listTaskSubscriptions` | List all followers (subscriptions) of a task. |
| List Task Tags | `listTaskTags` | List all labels (tags) attached to a task. |
| List Task Work Intervals | `listTaskWorkIntervals` | List all time-tracking work intervals on a task. |
| List Tasks | `listTasks` | List all tasks the authenticated user can access, with optional filters. |
| Remove Label From Task | `removeLabelFromTask` | Detach a label from a task. |
| Remove Project Membership | `removeProjectMembership` | Remove a team or group membership from a project. Business plan only. |
| Remove Project Right | `removeProjectRight` | Revoke a person's access to a project. |
| Remove Task Relationship | `removeTaskRelationship` | Remove a relationship from a task. |
| Remove Task Subscription | `removeTaskSubscription` | Remove a follower from a task. |
| Update Checklist | `updateChecklist` | Update a checklist's name or sequence. |
| Update Checklist Item | `updateChecklistItem` | Update a checklist item's name, sequence, or status (e.g. mark it complete). |
| Update Custom Field | `updateCustomField` | Update a custom field value. Business plan only. |
| Update Custom Field Type | `updateCustomFieldType` | Update a custom field type's name or description. Business plan only. |
| Update Dropdown Item | `updateDropdownItem` | Update a dropdown item's name or sequence. Business plan only. |
| Update Label | `updateLabel` | Update a label's name or color. |
| Update Project | `updateProject` | Update a project's name, description, status, or sharing mode. |
| Update Project Membership | `updateProjectMembership` | Update the role of a project membership. Business plan only. |
| Update Project Right | `updateProjectRight` | Update a project right's role or watching flag. |
| Update Section | `updateSection` | Update a section's name or status. |
| Update Task | `updateTask` | Update a task, including moving it to another section, reassigning, or changing its status. |
| Update Work Interval | `updateWorkInterval` | Update the start or end time of a work interval. |
