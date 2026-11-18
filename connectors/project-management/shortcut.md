---
description: "Shortcut (formerly Clubhouse) project management."
hidden: true
---

# Shortcut

<img src="../../.gitbook/assets/connectors/lg/shortcut.png" alt="Shortcut logo">

Shortcut (formerly Clubhouse) project management. Manage stories, epics, iterations, objectives, milestones, projects, workflows, members, teams, groups, labels, docs, files, and story links via the Shortcut REST API v3.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Authentication** | Credentials you enter |
| **Slug** | `shortcut` |

## Use it

Add Shortcut from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.shortcut.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Category | `createCategory` | Create Category allows you to create a new Category in Shortcut. |
| Create Doc | `createDoc` | Creates a new Doc. Supports markdown or HTML input via content_format parameter. |
| Create Entity Template | `createEntityTemplate` | Create a new entity template for the Workspace. |
| Create Epic | `createEpic` | Create Epic allows you to create a new Epic in Shortcut. |
| Create Epic Comment | `createEpicComment` | This endpoint allows you to create a threaded Comment on an Epic. |
| Create Epic Comment Reply | `createEpicCommentComment` | This endpoint allows you to create a nested Comment reply to an existing Epic Comment. |
| Create Epic Health | `createEpicHealth` | Create a new health status for the specified Epic. |
| Create Group | `createGroup` | Create Group |
| Create Iteration | `createIteration` | Create Iteration |
| Create Label | `createLabel` | Create Label allows you to create a new Label in Shortcut. |

<details>

<summary>See 133 more actions</summary>

* **Create Linked File** `createLinkedFile`: Create Linked File allows you to create a new Linked File in Shortcut.
* **Create Milestone** `createMilestone`: (Deprecated: Use 'Create Objective') Create Milestone allows you to create a new Milestone in Shortcut.
* **Create Multiple Stories** `createMultipleStories`: Create Multiple Stories allows you to create multiple stories in a single request using the same syntax as [Create Story](https://developer.shortcut.com/api/rest/v3#create-story).
* **Create Objective** `createObjective`: Create Objective allows you to create a new Objective in Shortcut.
* **Create Objective Health** `createObjectiveHealth`: Create a new health status for the specified Objective.
* **Create Project** `createProject`: Create Project is used to create a new Shortcut Project.
* **Create Story** `createStory`: Create Story is used to add a new story to your Shortcut Workspace. This endpoint requires that either workflow_state_id or project_id be provided, but will reject the request if both or neither are specified. The workflow_state_id has been marked as required and is the recommended field to specify because we are in the process of sunsetting Projects in Shortcut.
* **Create Story Comment** `createStoryComment`: Create Comment allows you to create a Comment on any Story.
* **Create Story From Template** `createStoryFromTemplate`: Create Story From Template is used to add a new story derived from a template to your Shortcut Workspace.
* **Create Story Link** `createStoryLink`: Story Links (called Story Relationships in the UI) allow you create semantic relationships between two stories. The parameters read like an active voice grammatical sentence: subject -&gt; verb -&gt; object. The subject story acts on the object Story; the object story is the direct object of the sentence. The subject story "blocks", "duplicates", or "relates to" the object story. Examples: - "story 5 blocks story 6” -- story 6 is now "blocked" until story 5 is moved to a Done workflow state.
* **Create Story Reaction** `createStoryReaction`: Create a reaction to a story comment.
* **Create Task** `createTask`: Create Task is used to create a new task in a Story.
* **Create Webhook Integration** `createGenericIntegration`: Create Generic Integration
* **Delete Category** `deleteCategory`: Delete Category can be used to delete any Category.
* **Delete Custom Field** `deleteCustomField`: Delete Custom Field
* **Delete Doc** `deleteDoc`: Permanently deletes a Doc and its associated data. Requires admin access to the doc. When a document is deleted, connected clients will be notified via SSE events.
* **Delete Entity Template** `deleteEntityTemplate`: Delete Entity Template
* **Delete Epic** `deleteEpic`: Delete Epic can be used to delete the Epic. The only required parameter is Epic ID.
* **Delete Epic Comment** `deleteEpicComment`: This endpoint allows you to delete a Comment from an Epic.
* **Delete File** `deleteFile`: Delete File deletes a previously uploaded file.
* **Delete Iteration** `deleteIteration`: Delete Iteration
* **Delete Label** `deleteLabel`: Delete Label can be used to delete any Label.
* **Delete Linked File** `deleteLinkedFile`: Delete Linked File can be used to delete any previously attached Linked-File.
* **Delete Milestone** `deleteMilestone`: (Deprecated: Use 'Delete Objective') Delete Milestone can be used to delete any Milestone.
* **Delete Multiple Stories** `deleteMultipleStories`: Delete Multiple Stories allows you to delete multiple archived stories at once.
* **Delete Objective** `deleteObjective`: Delete Objective can be used to delete any Objective.
* **Delete Project** `deleteProject`: Delete Project can be used to delete a Project. Projects can only be deleted if all associated Stories are moved or deleted. In the case that the Project cannot be deleted, you will receive a 422 response.
* **Delete Story** `deleteStory`: Delete Story can be used to delete any Story.
* **Delete Story Comment** `deleteStoryComment`: Delete a Comment from any story.
* **Delete Story Link** `deleteStoryLink`: Removes the relationship between the stories for the given Story Link.
* **Delete Story Reaction** `deleteStoryReaction`: Delete a reaction from any story comment.
* **Delete Task** `deleteTask`: Delete Task can be used to delete any previously created Task on a Story.
* **Delete Webhook Integration** `deleteGenericIntegration`: Delete Generic Integration
* **Disable Iterations** `disableIterations`: Disables Iterations for the current workspace
* **Disable Story Templates** `disableStoryTemplates`: Disables the Story Template feature for the Workspace.
* **Enable Iterations** `enableIterations`: Enables Iterations for the current workspace
* **Enable Story Templates** `enableStoryTemplates`: Enables the Story Template feature for the Workspace.
* **Get Category** `getCategory`: Get Category returns information about the selected Category.
* **Get Current Member** `getCurrentMemberInfo`: Returns information about the authenticated member.
* **Get Custom Field** `getCustomField`: Get Custom Field
* **Get Doc** `getDoc`: Get a Doc by its public ID with content. Use content_format=html query parameter to include HTML content.
* **Get Entity Template** `getEntityTemplate`: Get Entity Template returns information about a given entity template.
* **Get Epic** `getEpic`: Get Epic returns information about the selected Epic.
* **Get Epic Comment** `getEpicComment`: This endpoint returns information about the selected Epic Comment.
* **Get Epic Health** `getEpicHealth`: Get the current health for the specified Epic.
* **Get Epic Workflow** `getEpicWorkflow`: Returns the Epic Workflow for the Workspace.
* **Get File** `getFile`: Get File returns information about the selected UploadedFile.
* **Get Group** `getGroup`: Returns the details of one Group (team) in the Shortcut workspace, looked up by its public ID.
* **Get Iteration** `getIteration`: Get Iteration
* **Get Key Result** `getKeyResult`: Get Key Result returns information about a chosen Key Result.
* **Get Label** `getLabel`: Get Label returns information about the selected Label.
* **Get Linked File** `getLinkedFile`: Get File returns information about the selected Linked File.
* **Get Member** `getMember`: Returns information about a Member.
* **Get Milestone** `getMilestone`: (Deprecated: Use 'Get Objective') Get Milestone returns information about a chosen Milestone.
* **Get Objective** `getObjective`: Get Objective returns information about a chosen Objective.
* **Get Objective Health** `getObjectiveHealth`: Get the current health for the specified Objective.
* **Get Project** `getProject`: Get Project returns information about the selected Project.
* **Get Repository** `getRepository`: Get Repository returns information about the selected Repository.
* **Get Story** `getStory`: Get Story returns information about a chosen Story.
* **Get Story Comment** `getStoryComment`: Get Comment is used to get Comment information.
* **Get Story History** `storyHistory`: Story History
* **Get Story Link** `getStoryLink`: Returns the stories and their relationship for the given Story Link.
* **Get Task** `getTask`: Returns information about a chosen Task.
* **Get Webhook Integration** `getGenericIntegration`: Get Generic Integration
* **Get Workflow** `getWorkflow`: Get Workflow returns information about a chosen Workflow.
* **Link Document to Epic** `linkDocumentToEpic`: Create a relationship between a Document and an Epic.
* **List Categories** `listCategories`: List Categories returns a list of all Categories and their attributes.
* **List Category Milestones** `listCategoryMilestones`: List Category Milestones returns a list of all Milestones with the Category.
* **List Category Objectives** `listCategoryObjectives`: Returns a list of all Objectives with the Category.
* **List Custom Fields** `listCustomFields`: List Custom Fields
* **List Docs** `listDocs`: List Docs returns a list of Doc that the current user can read.
* **List Document Epics** `listDocumentEpics`: Get a list of all Epics related to this Document.
* **List Entity Templates** `listEntityTemplates`: List all the entity templates for the Workspace.
* **List Epic Comments** `listEpicComments`: Get a list of all Comments on an Epic.
* **List Epic Documents** `listEpicDocuments`: Get a list of all Documents related to this Epic.
* **List Epic Healths** `listEpicHealths`: List the history of health statuses for the specified Epic, most recent first.
* **List Epic Stories** `listEpicStories`: Get a list of all Stories in an Epic.
* **List Epics** `listEpics`: List Epics returns a list of all Epics and their attributes.
* **List Epics Paginated** `listEpicsPaginated`: List Epics with pagination returns a paginated list of Epics and their attributes.
* **List Files** `listFiles`: List Files returns a list of all UploadedFiles in the workspace.
* **List Group Stories** `listGroupStories`: List the Stories assigned to the Group. (By default, limited to 1,000).
* **List Groups** `listGroups`: A group in our API maps to a "Team" within the Shortcut Product. A Team is a collection of Users that can be associated to Stories, Epics, and Iterations within Shortcut.
* **List Iteration Stories** `listIterationStories`: Get a list of all Stories in an Iteration.
* **List Iterations** `listIterations`: List Iterations
* **List Label Epics** `listLabelEpics`: List all of the Epics with the Label.
* **List Label Stories** `listLabelStories`: List all of the Stories with the Label.
* **List Labels** `listLabels`: List Labels returns a list of all Labels and their attributes.
* **List Linked Files** `listLinkedFiles`: List Linked Files returns a list of all Linked-Files and their attributes.
* **List Members** `listMembers`: Returns information about members of the Workspace.
* **List Milestone Epics** `listMilestoneEpics`: (Deprecated: Use 'List Objective Epics') List all of the Epics within the Milestone.
* **List Milestones** `listMilestones`: (Deprecated: Use 'List Objectives') List Milestones returns a list of all Milestones and their attributes.
* **List Objective Epics** `listObjectiveEpics`: List all of the Epics within the Objective.
* **List Objective Healths** `listObjectiveHealths`: List the history of health statuses for the specified Objective, most recent first.
* **List Objectives** `listObjectives`: List Objectives returns a list of all Objectives and their attributes.
* **List Project Stories** `listStories`: List Stories returns a list of all Stories in a selected Project and their attributes.
* **List Projects** `listProjects`: List Projects returns a list of all Projects and their attributes.
* **List Repositories** `listRepositories`: List Repositories returns a list of all Repositories and their attributes.
* **List Stories By External Link** `getExternalLinkStories`: Get Stories which have a given External Link associated with them.
* **List Story Comments** `listStoryComment`: Lists Comments associated with a Story
* **List Story Sub-Tasks** `listStorySubTasks`: List Story Sub tasks returns a list of all Sub-task Stories for a given parent Story.
* **List Workflows** `listWorkflows`: Returns a list of all Workflows in the Workspace.
* **Query Stories** `queryStories`: Search Stories lets you search Stories based on desired parameters.
* **Search** `search`: Search lets you search Epics and Stories based on desired parameters. Since ordering of the results can change over time (due to search ranking decay, new Epics and Stories being created), the `next` value from the previous response can be used as the path and query string for the next page to ensure stable ordering.
* **Search Documents** `searchDocuments`: Search Documents lets you search Documents based on desired parameters. Supports structured filters: title, archived, created_by_me, followed_by_me.
* **Search Epics** `searchEpics`: Search Epics lets you search Epics based on desired parameters. Since ordering of stories can change over time (due to search ranking decay, new Epics being created), the `next` value from the previous response can be used as the path and query string for the next page to ensure stable ordering.
* **Search Iterations** `searchIterations`: Search Iterations lets you search Iterations based on desired parameters. Since ordering of results can change over time (due to search ranking decay, new Iterations being created), the `next` value from the previous response can be used as the path and query string for the next page to ensure stable ordering.
* **Search Milestones** `searchMilestones`: Search Milestones lets you search Milestones based on desired parameters. Since ordering of results can change over time (due to search ranking decay, new Milestones being created), the `next` value from the previous response can be used as the path and query string for the next page to ensure stable ordering.
* **Search Objectives** `searchObjectives`: Search Objectives lets you search Objectives based on desired parameters. Since ordering of results can change over time (due to search ranking decay, new Objectives being created), the `next` value from the previous response can be used as the path and query string for the next page to ensure stable ordering.
* **Search Stories** `searchStories`: Search Stories lets you search Stories based on desired parameters. Since ordering of stories can change over time (due to search ranking decay, new stories being created), the `next` value from the previous response can be used as the path and query string for the next page to ensure stable ordering.
* **Unlink Document from Epic** `unlinkDocumentFromEpic`: Remove a relationship between a Document and an Epic.
* **Unlink Story Comment From Slack** `unlinkCommentThreadFromSlack`: Unlinks a Comment from its linked Slack thread (Comment replies and Slack replies will no longer be synced)
* **Update Category** `updateCategory`: Update Category allows you to replace a Category name with another name. If you try to name a Category something that already exists, you will receive a 422 response.
* **Update Custom Field** `updateCustomField`: Update Custom Field can be used to update the definition of a Custom Field. The order of items in the 'values' collection is interpreted to be their ascending sort order.To delete an existing enum value, simply omit it from the 'values' collection. New enum values may be created inline by including an object in the 'values' collection having a 'value' entry with no 'id' (eg. {'value': 'myNewValue', 'color_key': 'green'}).
* **Update Doc** `updateDoc`: Updates an existing Doc's title and/or content. Supports markdown or HTML input via content_format parameter. When a document is updated: (1) For Tiptap-migrated docs, SSE events notify connected Tiptap clients to refresh. (2) For non-migrated docs, CKEditor cache is flushed and SSE events notify connected CKEditor users.
* **Update Entity Template** `updateEntityTemplate`: Update an entity template's name or its contents.
* **Update Epic** `updateEpic`: Update Epic can be used to update numerous fields in the Epic. The only required parameter is Epic ID, which can be found in the Shortcut UI.
* **Update Epic Comment** `updateEpicComment`: This endpoint allows you to update a threaded Comment on an Epic.
* **Update File** `updateFile`: Update File updates the properties of an UploadedFile (but not its content).
* **Update Group** `updateGroup`: Update Group
* **Update Health** `updateHealth`: Update an existing health status by its ID.
* **Update Iteration** `updateIteration`: Update Iteration
* **Update Key Result** `updateKeyResult`: Update Key Result allows updating a Key Result's name or initial, observed, or target values.
* **Update Label** `updateLabel`: Update Label allows you to replace a Label name with another name. If you try to name a Label something that already exists, you will receive a 422 response.
* **Update Linked File** `updateLinkedFile`: Updated Linked File allows you to update properties of a previously attached Linked-File.
* **Update Milestone** `updateMilestone`: (Deprecated: Use 'Update Objective') Update Milestone can be used to update Milestone properties.
* **Update Multiple Stories** `updateMultipleStories`: Update Multiple Stories allows you to make changes to numerous stories at once.
* **Update Objective** `updateObjective`: Update Objective can be used to update Objective properties.
* **Update Project** `updateProject`: Update Project can be used to change properties of a Project.
* **Update Story** `updateStory`: Update Story can be used to update Story properties.
* **Update Story Comment** `updateStoryComment`: Update Comment replaces the text of the existing Comment.
* **Update Story Link** `updateStoryLink`: Updates the stories and/or the relationship for the given Story Link.
* **Update Task** `updateTask`: Update Task can be used to update Task properties.
* **Upload Files** `uploadFiles`: Upload Files uploads one or many files and optionally associates them with a story. Use the multipart/form-data content-type to upload. Each `file` key should contain a separate file. Each UploadedFile's name comes from the Content-Disposition header "filename" directive for that field.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Epic Created | `epic.create` | Fired when a Epic is created in the Shortcut workspace. |
| Epic Deleted | `epic.delete` | Fired when a Epic is deleted in the Shortcut workspace. |
| Epic Updated | `epic.update` | Fired when a Epic is updated in the Shortcut workspace. |
| Iteration Created | `iteration.create` | Fired when a Iteration is created in the Shortcut workspace. |
| Iteration Deleted | `iteration.delete` | Fired when a Iteration is deleted in the Shortcut workspace. |
| Iteration Updated | `iteration.update` | Fired when a Iteration is updated in the Shortcut workspace. |
| Label Created | `label.create` | Fired when a Label is created in the Shortcut workspace. |
| Label Deleted | `label.delete` | Fired when a Label is deleted in the Shortcut workspace. |
| Label Updated | `label.update` | Fired when a Label is updated in the Shortcut workspace. |
| Objective Created | `milestone.create` | Fired when a Objective is created in the Shortcut workspace. |

<details>

<summary>See 19 more events</summary>

* **Objective Deleted** `milestone.delete`: Fired when a Objective is deleted in the Shortcut workspace.
* **Objective Updated** `milestone.update`: Fired when a Objective is updated in the Shortcut workspace.
* **Project Created** `project.create`: Fired when a Project is created in the Shortcut workspace.
* **Project Deleted** `project.delete`: Fired when a Project is deleted in the Shortcut workspace.
* **Project Updated** `project.update`: Fired when a Project is updated in the Shortcut workspace.
* **Story Comment Created** `story-comment.create`: Fired when a Story Comment is created in the Shortcut workspace.
* **Story Comment Deleted** `story-comment.delete`: Fired when a Story Comment is deleted in the Shortcut workspace.
* **Story Comment Updated** `story-comment.update`: Fired when a Story Comment is updated in the Shortcut workspace.
* **Story Created** `story.create`: Fired when a Story is created in the Shortcut workspace.
* **Story Deleted** `story.delete`: Fired when a Story is deleted in the Shortcut workspace.
* **Story Link Created** `story-link.create`: Fired when a Story Link is created in the Shortcut workspace.
* **Story Link Deleted** `story-link.delete`: Fired when a Story Link is deleted in the Shortcut workspace.
* **Story Updated** `story.update`: Fired when a Story is updated in the Shortcut workspace.
* **Task Created** `story-task.create`: Fired when a Task is created in the Shortcut workspace.
* **Task Deleted** `story-task.delete`: Fired when a Task is deleted in the Shortcut workspace.
* **Task Updated** `story-task.update`: Fired when a Task is updated in the Shortcut workspace.
* **Team Created** `group.create`: Fired when a Team is created in the Shortcut workspace.
* **Team Deleted** `group.delete`: Fired when a Team is deleted in the Shortcut workspace.
* **Team Updated** `group.update`: Fired when a Team is updated in the Shortcut workspace.

</details>
