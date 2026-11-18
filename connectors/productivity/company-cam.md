---
description: "CompanyCam is a photo documentation and project collaboration app for contractors."
hidden: true
---

# CompanyCam

<img src="../../.gitbook/assets/connectors/company-cam.png" alt="CompanyCam logo" width="64">

CompanyCam is a photo documentation and project collaboration app for contractors. This connector covers the CompanyCam Core API v2: projects (create, update, archive, restore, delete, notepad, labels, comments, documents, collaborators, invitations, assigned users and checklists), photos (upload by URI, update, delete, comments, tags and descriptions), videos, tags, users, groups, checklists and checklist templates, the current company and user, and webhook subscriptions for real-time project, photo, comment, document, video, checklist and task events.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [companycam.com](https://companycam.com) |
| **Authentication** | Bearer token |
| **Slug** | `companyCam` |

## Use it

Add CompanyCam from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.companyCam.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Photo Comment | `createPhotoComment` | Post a comment on a photo. Comments appear in the project feed alongside the photo. |
| Add Photo Tags | `createPhotoTags` | Apply one or more tags to a photo. Tags that do not exist yet are created automatically. |
| Add Photo To Project | `createProjectPhoto` | Add a photo to a project by giving CompanyCam a publicly reachable image URL, which it downloads and processes. The photo only appears in list results once its processing_status becomes processed. |
| Add Project Comment | `createProjectComment` | Post a comment on a project. Comments appear in the project feed and notify the crew assigned to it. |
| Add Project Labels | `createProjectLabels` | Add one or more labels to a project. Labels that do not exist yet are created automatically. |
| Archive Project | `archiveProject` | Archive a project so it is hidden from the active project list while keeping all of its photos and documents. Use Restore Project to bring it back. |
| Assign User To Project | `assignUserToProject` | Assign a user to a project so the project appears in their project list. Required for restricted users, who can only see projects they are assigned to. |
| Create Group | `createGroup` | Create a user group (crew) and optionally add members to it. |
| Create Project | `createProject` | Create a project, the container CompanyCam uses to group photos, documents, checklists and comments for one job site. Supply an address or coordinates so the project appears on the map. |
| Create Project Checklist | `createProjectChecklist` | Add a checklist to a project by copying an existing checklist template. Use List Checklist Templates to find the template identifier. |

<details>

<summary>See 52 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Project Invitation | `createInvitation` | Create a collaboration invitation for a project and return its shareable acceptance URL. CompanyCam does not send the invitation itself, so no email or text message is dispatched. |
| Create Tag | `createTag` | Create a tag in the company so it can be applied to photos and projects. |
| Create User | `createUser` | Invite a new user into the company. The new user receives CompanyCam credentials, so only run this for a real teammate you intend to add. |
| Create Webhook | `createWebhook` | Register a webhook so CompanyCam POSTs matching events to your endpoint. Scopes accept an exact event name such as project.created, a family wildcard such as photo.*, or * for every event. Your endpoint must answer with HTTP 200 or the delivery is retried. |
| Delete Group | `deleteGroup` | Delete a user group. Its members remain in the company but are no longer grouped together. |
| Delete Photo | `deletePhoto` | Delete a photo. The photo moves to a deleted state and stops appearing in project galleries. |
| Delete Project | `deleteProject` | Delete a project. The project and everything captured at it move to a deleted state and stop appearing in the default project list. |
| Delete Project Label | `deleteProjectLabel` | Remove a label from a project. The label itself remains available for other projects. |
| Delete Tag | `deleteTag` | Delete a tag from the company. The tag is removed from every photo and project it was applied to. |
| Delete User | `deleteUser` | Remove a user from the company. This revokes the user's access to CompanyCam and cannot be undone through the API. |
| Delete Webhook | `deleteWebhook` | Delete a webhook subscription so CompanyCam stops sending events to its endpoint. |
| List Checklist Templates | `listChecklistTemplates` | List the checklist templates defined in the company. Use a template identifier from here with Create Project Checklist. |
| List Checklists | `listChecklists` | List every checklist in the company across all projects, optionally filtered to completed or outstanding ones. |
| List Groups | `listGroups` | List the user groups in the company. Groups are crews used to organise users and to filter photos and videos. |
| List Photo Comments | `listPhotoComments` | List the comments posted on a photo, newest first. |
| List Photo Tags | `listPhotoTags` | List the tags applied to a photo. |
| List Photos | `listPhotos` | List photos visible to the connected user across all projects, most recently captured first. Filter by project, user, group, tag or capture-date range. Photos only appear here once CompanyCam has finished processing them. |
| List Project Assigned Users | `listProjectAssignedUsers` | List the users currently assigned to a project. Restricted users can only see projects they are assigned to. |
| List Project Checklists | `listProjectChecklists` | List the checklists that have been added to a project, with their sections and tasks. |
| List Project Collaborators | `listProjectCollaborators` | List the external companies collaborating on a project. Collaborators are separate CompanyCam companies that accepted an invitation to the project. |
| List Project Comments | `listProjectComments` | List the comments posted on a project, newest first. |
| List Project Documents | `listProjectDocuments` | List the documents attached to a project, including their download URLs, content types and byte sizes. |
| List Project Invitations | `listProjectInvitations` | List the collaboration invitations that have been created for a project, including their shareable acceptance URLs. |
| List Project Labels | `listProjectLabels` | List the labels applied to a project. Labels categorise projects, for example by job type or crew. |
| List Project Photos | `listProjectPhotos` | List the photos captured at one project, most recently captured first. Filter by user, group, tag or capture-date range. |
| List Project Videos | `listProjectVideos` | List the videos captured at one project, most recently captured first. |
| List Projects | `listProjects` | List projects in the company, most recently updated first. Supports a free-text search, a modified-since cutoff and an active or deleted status filter. |
| List Tags | `listTags` | List every tag defined in the company. Tag identifiers returned here can be used to filter photo and video lists. |
| List Users | `listUsers` | List the users in the company, newest first. Results are paginated. |
| List Videos | `listVideos` | List videos visible to the connected user, most recently captured first. Until a video's status is processed, playback_url returns the raw upload URL rather than the HLS stream. |
| List Webhooks | `listWebhooks` | List the webhook subscriptions registered for the company, with the scopes each one is subscribed to. |
| Remove User From Project | `removeUserFromProject` | Remove a user's assignment from a project. A restricted user loses access to the project entirely. |
| Restore Project | `restoreProject` | Restore a DELETED project, returning its status to active. Verified against the live API: this endpoint does not clear the archived flag, so a project archived with Archive Project stays archived after calling it. |
| Retrieve Company | `getCurrentCompany` | Retrieve the CompanyCam company associated with this connection, including its name, status, address and logo image variants. |
| Retrieve Current User | `getCurrentUser` | Retrieve the CompanyCam user that owns the API token used by this connection, including their name, email address, role and company id. |
| Retrieve Group | `getGroup` | Retrieve a single user group by its unique identifier, including its members. |
| Retrieve Photo | `getPhoto` | Retrieve a single photo by its unique identifier, including every image size variant and its processing status. |
| Retrieve Project | `getProject` | Retrieve a single project by its unique identifier, including its address, coordinates, featured image and primary contact. |
| Retrieve Project Checklist | `getProjectChecklist` | Retrieve a single checklist on a project, including its sections, tasks and sub-tasks. |
| Retrieve Tag | `getTag` | Retrieve a single tag by its unique identifier. |
| Retrieve User | `getUser` | Retrieve a single user in the company by their unique identifier. |
| Retrieve Video | `getVideo` | Retrieve a single video by its unique identifier. Poll this until status is processed before using playback_url or format. |
| Retrieve Webhook | `getWebhook` | Retrieve a single webhook subscription by its unique identifier. |
| Update Group | `updateGroup` | Rename a user group or replace its member list. |
| Update Photo | `updatePhoto` | Mark a photo as internal-only or return it to normal visibility. Internal photos are excluded from customer-facing galleries and reports. |
| Update Photo Description | `updatePhotoDescription` | Create or replace the description shown under a photo. |
| Update Project | `updateProject` | Update a project's name, address, coordinates or geofence. Only the fields you supply are changed. |
| Update Project Notepad | `updateProjectNotepad` | Replace the free-text notepad attached to a project. The notepad is the shared scratch space crews use for job notes. |
| Update Tag | `updateTag` | Rename a tag. The change applies everywhere the tag is used. |
| Update User | `updateUser` | Update the profile details of a user in the company. Only the fields you supply are changed. |
| Update Webhook | `updateWebhook` | Change a webhook's endpoint, subscribed scopes, signing token or enabled state. |
| Upload Project Document | `createProjectDocument` | Attach a document to a project by sending its contents Base64 encoded in the request body. The file must be 30 MB or smaller. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| All Checklist Events | `todo_list.*` | Fires for every checklist (todo list) event. |
| All Checklist Task Events | `task.*` | Fires for every checklist task event. |
| All Comment Events | `comment.*` | Fires for every comment event. |
| All Document Events | `document.*` | Fires for every document event. |
| All Events | `*` | Fires for every event CompanyCam emits. Prefer a narrower scope unless you really want everything. |
| All Photo Events | `photo.*` | Fires for every photo event. |
| All Project Events | `project.*` | Fires for every project event. |
| All Video Events | `video.*` | Fires for every video event. |
| Checklist Completed | `todo_list.completed` | Fires when every task on a checklist has been completed. |
| Checklist Created | `todo_list.created` | Fires when a checklist is created on a project. |

<details>

<summary>See 19 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Checklist Deleted | `todo_list.deleted` | Fires when a checklist is deleted. |
| Checklist Task Completed | `task.completed` | Fires when a checklist task is completed. This does not apply to project tasks. |
| Comment Created | `comment.created` | Fires when a comment is created on a photo or a project. |
| Document Created | `document.created` | Fires when a document is added to a project. |
| Document Updated | `document.updated` | Fires when a project document is updated. |
| Photo Created | `photo.created` | Fires once a photo has been created and processed by CompanyCam. |
| Photo Description Updated | `photo.description_updated` | Fires when a photo's description is created or updated. |
| Photo Tag Added | `photo.tag_added` | Fires when a tag is added to a photo. |
| Photo Updated | `photo.updated` | Fires when a photo is edited, for example annotated. |
| Project Archived | `project.archived` | Fires when a project is archived. |
| Project Contact Created | `project.contact_created` | Fires when a contact is added to a project. |
| Project Contact Updated | `project.contact_updated` | Fires when a project's contact is edited. |
| Project Created | `project.created` | Fires when a project is created. |
| Project Deleted | `project.deleted` | Fires when a project is deleted. |
| Project Label Added | `project.label_added` | Fires when a label is added to a project. |
| Project Merged | `project.merged` | Fires when a project is merged into another project. |
| Project Updated | `project.updated` | Fires when a project is updated. |
| Video Created | `video.created` | Fires when a video is added to a project. |
| Video Updated | `video.updated` | Fires when a video is updated, including when processing finishes and playback_url becomes the HLS stream. |

</details>
