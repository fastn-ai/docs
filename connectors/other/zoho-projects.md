---
description: "Zoho Projects is Zoho's cloud project management suite."
hidden: true
---

# Zoho Projects

Zoho Projects is Zoho's cloud project management suite. This connector provides access to Zoho Projects' REST API: portals, projects, dashboard/status updates, milestones, tasklists, tasks (with comments/subtasks), timesheets/time logs, bugs, tags, events/calendar, forums, users, client contacts, documents/folders, search, entity properties, and teams (user groups).

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [zoho.com](https://zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 101 |
| **Events** | 0 |
| **Slug** | `zohoProjects` |

## Use it

Add Zoho Projects from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoProjects.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Bug Time Log | `addBugTimeLog` | Adds a time log entry to a bug. |
| Add Event | `addEvent` | Adds a calendar event to a project. |
| Add Folder | `addFolder` | Adds a document folder to a project. |
| Add Forum | `addForum` | Adds a forum post to a project. |
| Add Forum Category | `addForumCategory` | Adds a forum category to a project. |
| Add Forum Comment | `addForumComment` | Adds a comment to a forum post. |
| Add General Time Log | `addGeneralTimeLog` | Adds a general (non-task, non-bug) time log entry to a project. |
| Add Project Status | `addProjectStatus` | Adds a new status update for a project. |
| Add Task Comment | `addTaskComment` | Adds a comment to a task. |
| Add Task Time Log | `addTaskTimeLog` | Adds a time log entry to a task. |
| Add User to Team | `addUserToTeam` | Adds a single user to a team. |
| Associate Contacts | `associateContacts` | Associates existing client contacts to a project. |
| Associate Multiple Teams to Project | `associateMultipleTeams` | Associates more than one team to a project. |
| Associate Project to Team | `associateProjectToTeam` | Associates a project to a team. |
| Associate Tag | `associateTag` | Associates a tag with an entity (project=2, milestone=3, tasklist=4, task=5, bug=6, forum=7, status=8) in a project. |
| Convert Contact to Client User | `convertContactToClientUser` | Converts a client contact into a full client user. |
| Create Bug | `createBug` | Creates a bug (issue) in a project. |
| Create Contacts | `createContacts` | Creates one or more client contacts in a portal. |
| Create Milestone | `createMilestone` | Creates a milestone in a project. |
| Create Project | `createProject` | Creates a new project in the given portal. |
| Create Tags | `createTags` | Creates one or more tags in a portal. |
| Create Task | `createTask` | Creates a task in a project. |
| Create Tasklist | `createTasklist` | Creates a tasklist in a project. |
| Create Team | `createTeam` | Creates a new team (usergroup) in the portal. |
| Delete Bug | `deleteBug` | Deletes a bug. |
| Delete Bug Time Log | `deleteBugTimeLog` | Deletes a time log entry from a bug. |
| Delete Contact | `deleteContact` | Deletes a client contact from a portal. |
| Delete Document | `deleteDocument` | Deletes a document. |
| Delete Event | `deleteEvent` | Deletes a calendar event. |
| Delete Folder | `deleteFolder` | Deletes a document folder. |
| Delete Forum | `deleteForum` | Deletes a forum post. |
| Delete General Time Log | `deleteGeneralTimeLog` | Deletes a general time log entry. |
| Delete Milestone | `deleteMilestone` | Deletes a milestone. |
| Delete Project | `deleteProject` | Deletes a project. |
| Delete Tag | `deleteTag` | Deletes a tag from a portal. |
| Delete Task | `deleteTask` | Deletes a task. |
| Delete Task Comment | `deleteTaskComment` | Deletes a task comment. |
| Delete Task Time Log | `deleteTaskTimeLog` | Deletes a time log entry from a task. |
| Delete Tasklist | `deleteTasklist` | Deletes a tasklist. |
| Delete Team | `deleteTeam` | Deletes a team from a project. |
| Dissociate Contact | `dissociateContact` | Dissociates a client contact from a project. |
| Dissociate Tag | `dissociateTag` | Dissociates a tag from an entity in a project. |
| Get Bug | `getBug` | Gets the details of a bug. |
| Get Document Version Details | `getDocumentVersion` | Gets the version details of a document. |
| Get Milestone | `getMilestone` | Gets the details of a milestone. |
| Get Project | `getProject` | Gets the details of a specific project. |
| Get Task | `getTask` | Gets all the details of a task. |
| List Bug Custom Fields | `listBugCustomFields` | Gets all the custom fields configured for bugs in a project. |
| List Bug Default Fields | `listBugDefaultFields` | Gets all the default fields (severity, module, reproducible, etc.) configured for bugs in a project. |
| List Bugs | `listBugs` | Gets all the bugs (issues) in a project. |
| List Contacts | `listContacts` | Fetches all client contacts from a portal. |
| List Documents | `listDocuments` | Gets all the documents in a project. |
| List Events | `listEvents` | Gets all the calendar events in a project. |
| List Folders | `listFolders` | Gets all the document folders in a project. |
| List Forum Categories | `listForumCategories` | Gets all the forum categories in a project. |
| List Forum Comments | `listForumComments` | Gets all the comments on a forum post. |
| List Forums | `listForums` | Gets all the forum posts in a project. |
| List Milestones | `listMilestones` | Gets all the milestones in a project. |
| List Portal Teams | `listPortalTeams` | Gets team (usergroup) details from the portal. |
| List Portals | `listPortals` | Gets all the portals accessible to the logged-in user. A portal is the top-level Zoho Projects workspace/organization; every other resource (projects, tasks, etc.) is scoped under a portalId returned here. |
| List Project Activities | `listProjectActivities` | Lists the recent activities (activity feed) of a project. |
| List Project Contacts | `listProjectContacts` | Fetches all client contacts associated with a project. |
| List Project Statuses | `listProjectStatuses` | Gets the status updates posted for a project. |
| List Project Teams | `listProjectTeams` | Gets team (usergroup) details from a project. |
| List Projects | `listProjects` | Gets all the projects in the portal for the logged-in user. |
| List Subtasks | `listSubtasks` | Gets all the subtasks of a task. |
| List Tags | `listTags` | Fetches all tags present in a portal. |
| List Task Comments | `listTaskComments` | Gets all the comments on a task. |
| List Tasklist Tasks | `listTasklistTasks` | Gets all the tasks in a given tasklist. |
| List Tasklists | `listTasklists` | Gets all the tasklists in a project. |
| List Tasks | `listTasks` | Gets all the tasks in a project. |
| List Time Logs | `listTimeLogs` | Gets all the time logs in a project. |
| List Users | `listUsers` | Gets all the users in a project. |
| Remove Entity Properties | `removeEntityProperties` | Deletes key-value data stored against an entity. |
| Remove Team from Project | `removeTeamFromProject` | Removes a team from a project. |
| Remove User from Team | `removeUserFromTeam` | Removes a user from a team. |
| Resend Team Verification Code | `resendTeamVerificationCode` | Resends the verification code for a team's email alias. |
| Retrieve Entity Properties | `retrieveEntityProperties` | Retrieves key-value data stored against a project/task/bug entity. |
| Search Across Portal | `searchPortal` | Searches across all modules (projects, milestones, tasks, tasklists, forums, forumcomments, taskcomments, bugs, users, documents, events, all) in the portal. |
| Search Across Project | `searchProject` | Searches within a specific project. |
| Search Tag Results | `searchTagResults` | Fetches the tag results (entities tagged) across the portal. |
| Select Team Lead | `selectTeamLead` | Updates the team lead. |
| Store Entity Properties | `storeEntityProperties` | Stores key-value data against a project/task/bug entity. |
| Update Bug | `updateBug` | Updates a bug. |
| Update Bug Time Log | `updateBugTimeLog` | Updates a time log entry on a bug. |
| Update Contact | `updateContact` | Updates a client contact in a portal. |
| Update Entity Properties | `updateEntityProperties` | Updates key-value data stored against an entity. |
| Update Event | `updateEvent` | Updates a calendar event. |
| Update Folder | `updateFolder` | Renames a document folder. |
| Update Forum | `updateForum` | Updates a forum post. |
| Update General Time Log | `updateGeneralTimeLog` | Updates a general time log entry. |
| Update Milestone | `updateMilestone` | Updates a milestone. |
| Update Milestone Status | `updateMilestoneStatus` | Marks a milestone as completed or not completed. |
| Update Project | `updateProject` | Updates a project's name, description, or status (active/archived). |
| Update Tag | `updateTag` | Updates a tag's name or color. |
| Update Task | `updateTask` | Updates a task. |
| Update Task Time Log | `updateTaskTimeLog` | Updates a time log entry on a task. |
| Update Tasklist | `updateTasklist` | Updates a tasklist. |
| Verify Team Email Alias | `verifyTeamEmailAlias` | Verifies the team's email alias using a verification code. |
| View Team Details | `viewTeamDetails` | Fetches details of a particular team. |
| View Team Summary | `viewTeamSummary` | Views the overall summary of a team. |
