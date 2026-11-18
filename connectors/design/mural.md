---
description: "Mural visual collaboration API."
hidden: true
---

# Mural

<img src="../../.gitbook/assets/connectors/lg/mural.png" alt="Mural logo">

Mural visual collaboration API. Manage murals and their content (sticky notes, textboxes, titles, shapes, images, files, comments, areas, arrows and tables), rooms and folders, workspaces, templates, tags, voting sessions, timers, private mode, visitor settings, exports and member permissions.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [mural.co](https://mural.co) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `mural` |

## Use it

Add Mural from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mural.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Area | `createArea` | Create an area widget on a mural. Authorization scope: murals:write |
| Create Arrow | `createArrow` | Create an arrow widget on a mural. Authorization scope: murals:write |
| Create Asset | `createAsset` | Create an asset URL to upload a file or image to a mural. Authorization scope: murals:write |
| Create Comment | `createComment` | Create a comment widget on a mural. Authorization scope: murals:write |
| Create Custom Template | `createCustomTemplate` | Creates a custom template based on a mural to use in a workspace. Authorization scope: templates:write |
| Create File | `createFile` | Create a file widget on a mural. Authorization scope: murals:write |
| Create Image | `createImage` | Create an image widget in a mural. Authorization scope: murals:write |
| Create Mural | `createMural` | Create a mural in a room owned by the authenticated user. Authorization scope: murals:write |
| Create Mural From Template | `createMuralFromTemplate` | Create a mural in a room based on a template. Authorization scope: murals:write |
| Create Mural Tag | `createMuralTag` | Create a tag in a mural. Tag text is limited to 25 characters. Authorization scope: murals:write |
| Create Room | `createRoom` | Create a room in a workspace that the authenticated user has write access to. Authorization scope: rooms:write |
| Create Room Folder | `createRoomFolder` | Creates a new folder in a room that the authenticated user has write access to. Authorization scope: rooms:write |
| Create Shape Widgets | `createShapeWidget` | Create one or more shape widgets on a mural. Limit 1000. Authorization scope: murals:write |
| Create Sticky Notes | `createStickyNote` | Create one or more sticky note widgets on a mural. Limit 1000. Authorization scope: murals:write |
| Create Table | `createTable` | Create a table widget on a mural. Authorization scope: murals:write |
| Create Textboxes | `createTextbox` | Create one or more text box widgets on a mural. Limit 1000. Authorization scope: murals:write |
| Create Titles | `createTitle` | Create one or more title widgets on a mural. Limit 1000. Authorization scope: murals:write |
| Delete Mural | `deleteMuralById` | Deletes a mural that the authenticated user owns. Authorization scope: murals:write |
| Delete Mural Tag | `deleteTagById` | Delete a tag from a mural. Authorization scope: murals:write |
| Delete Mural Voting Session | `deleteMuralVotingSessionById` | Deletes a single voting session in a mural. Authorization scope: murals:write |
| Delete Room | `deleteRoomById` | Deletes a room that the authenticated user owns. Authorization scope: rooms:write |
| Delete Room Folder | `deleteFolderById` | Delete a folder (and all its sub-folders and murals) from a room. Authorization scope: rooms:write |
| Delete Template | `deleteTemplateById` | Deletes a template that the authenticated user owns. Authorization scope: templates:write |
| Delete Widget | `deleteWidgetById` | Delete a widget and its content from a Mural. Authorization scope: murals:write |
| Duplicate Mural | `duplicateMural` | Duplicate an existing mural. Authorization scope: murals:write |
| End Mural Voting Session | `endMuralVotingSession` | Ends a voting session for the specified mural. Required authorization scope: murals:write |
| Export Mural | `exportMural` | Allows an authenticated user of a mural to export mural to a pdf file. Authorization scope: murals:read |
| Get Current User | `getCurrentMember` | Returns information for the currently authenticated user. Authorization scope: identity:read |
| Get Default Templates | `getDefaultTemplates` | Returns all default templates. Authorization scope: templates:read |
| Get Mural | `getMuralById` | Returns info for a mural that the authenticated user has read access to. Authorization scope: murals:read |
| Get Mural Access Info | `muralAccessInfo` | Get the permission information for a particular mural. Authorization scope: none |
| Get Mural Export URL | `exportURLMural` | Returns a download URL for the exported file. The URL expires at the time shown in the expireOn property in the response. After the URL expires, request a new download URL for the export. Authorization scope: murals:read |
| Get Mural File Widgets | `getMuralFileWidgets` | Returns all files for a mural. Authorization scope: murals:read |
| Get Mural Tag | `getTagById` | Get a tag on a mural Authorization scope: murals:read |
| Get Mural Tags | `getMuralTags` | Returns the tags in a mural. Authorization scope: murals:read |
| Get Mural Timer | `getMuralTimer` | Retrieves the timer details for a specified mural. Required authorization scope: murals:read |
| Get Mural Users | `getMuralUsers` | Returns all users of a mural. Users include members and guests. Authorization scope: users:read |
| Get Mural Voting Session | `getMuralVotingSessionById` | Returns a single voting session in a mural. Authorization scope: murals:read |
| Get Mural Voting Session Results | `getMuralVotingSessionResults` | Returns the results of a voting session in a mural. Authorization scope: murals:read |
| Get Mural Voting Sessions | `getMuralVotingSessions` | Returns the voting sessions in a mural. Authorization scope: murals:read |
| Get Mural Widgets | `getMuralWidgets` | Returns all of the widgets for a mural. Does not currently include drawings. Authorization scope: murals:read |
| Get Private Mode | `getPrivateMode` | Retrieves the current private mode session for the specified mural. Required authorization scope: murals:read |
| Get Recent Templates | `getRecentTemplates` | Returns the recent templates used by a user for a workspace the authenticated user has access to. By default, default and custom templates are returned. By specifying parameter withoutDefault=true, the list of returned templates will not include default templates. Authorization scope: templates:read |
| Get Room | `getRoomInfoById` | Returns information about a room that the authenticated user has read access to. Authorization scope: rooms:read |
| Get Room Folders | `getRoomFolders` | Returns all folders for a room that the authenticated user has access to. Authorization scope: rooms:read |
| Get Room Members | `getRoomMembers` | Returns all members (including partial) and guests for a room the authenticated user has read access to. Authorization scope: users:read |
| Get Room Murals | `getRoomMurals` | Returns all murals for a room that the authenticated user has read access to. Authorization scope: murals:read |
| Get Templates By Workspace | `getTemplatesByWorkspace` | Returns default templates and custom templates for a workspace the authenticated user has access to. Authorization scope: templates:read |
| Get Widget | `getMuralWidget` | Returns information about a widget specified by its id. Authorization scope: murals:read |
| Get Workspace | `getWorkspace` | Returns information for a workspace that the authenticated user has read access to. Authorization scope: workspaces:read |
| Get Workspace Murals | `getWorkspaceMurals` | Returns all murals that the authenticated user owns or is a member of for a workspace. Authorization scope: murals:read |
| Get Workspace Open Rooms | `getWorkspaceOpenRooms` | Returns all the discoverable open rooms in a workspace. Authorization scope: rooms:read |
| Get Workspace Recent Murals | `getWorkspaceRecentMurals` | Returns the authenticated user's recently opened active murals in a workspace. Authorization scope: murals:read |
| Get Workspace Rooms | `getWorkspaceRooms` | Returns all rooms in a workspace that the authenticated user has read access to. The user must have access to both the workspace and the rooms. Authorization scope: rooms:read |
| Get Workspaces | `getWorkspaces` | Returns all workspaces the authenticated user is a member of, whether the workspace or user is active or inactive. Authorization scope: workspaces:read |
| Invite Users To Mural | `inviteUsersToMural` | Allows an authenticated user of a mural to invite members and/or guests. You can invite users by specifying either their email address or their username. In both cases the user is notified by email. However, when inviting by username, the user is immediately added to the mural. Authorization scope: murals:write |
| Invite Users To Room | `inviteUsersToRoom` | Allows an authenticated user of a room to invite members and/or guests. You can invite users by specifying either their email address or their username. In both cases the user is notified by email. However, when inviting by username, the user is immediately added to the room. Authorization scope: rooms:write |
| Invite Users To Workspace | `inviteUsersToWorkspace` | Allows an authenticated admin of a workspace to invite members and/or guests. Specify a user's email address to send them an invitation by email. Authorization scope: workspaces:write |
| Remove Mural Users | `removeMuralUsers` | Removes members and/or guests from a specified mural that the authenticated user has write access to. Authorization scope: murals:write |
| Remove Room Users | `removeRoomUsers` | Removes members and/or guests from a specified room that the authenticated user has write access to. Authorization scope: rooms:write |
| Reset Visitor Link | `resetVisitorLink` | Resets the mural visitor URL so the previous visitor URL will no longer work. Authorization scope: murals:write |
| Search Murals | `searchMurals` | Returns all murals that the authenticated user owns or is a member of for a specific workspace. Authorization scope: murals:read |
| Search Rooms | `searchRooms` | Returns all rooms that the authenticated user owns or is a member of from a specific workspace. Authorization scope: rooms:read |
| Search Templates | `searchTemplates` | Returns all custom templates the authenticated user owns or has access to. Authorization scope: templates:read |
| Send Request Access To Mural | `sendRequestAccessToMural` | Sends a request-access notification to the mural owner. Authorization scope: murals:read |
| Start Mural Timer | `startMuralTimer` | Initiates the timer for the specified mural. Required authorization scope: murals:write |
| Start Mural Voting Session | `startMuralVotingSession` | Initiates a voting session for the specified mural. Required authorization scope: murals:write |
| Start Private Mode | `startPrivateMode` | Initiates a private mode session for the specified mural. Required authorization scope: murals:write |
| Stop Mural Timer | `stopMuralTimer` | Stops the timer for the specified mural. Authorization scope: murals:write |
| Stop Private Mode | `stopPrivateMode` | End a private mode session for the specified mural. Authorization scope: murals:write |
| Update Area | `updateArea` | Update an area widget on a mural. Authorization scope: murals:write |
| Update Arrow | `updateArrow` | Update an arrow widget on a mural. Authorization scope: murals:write |
| Update Comment | `updateComment` | Update a comment widget on a mural. Authorization scope: murals:write |
| Update File | `updateFile` | Update a file widget on a mural. Authorization scope: murals:write |
| Update Image | `updateImage` | Update an image widget in a mural. Authorization scope: murals:write |
| Update Mural | `updateMuralById` | Update a mural the authenticated user owns or is a member of. Authorization scope: murals:write |
| Update Mural Member Permissions | `updateMuralMemberPermissions` | Update mural member permissions, by an authenticated owner of the mural. Authorization scope: murals:write |
| Update Mural Tag | `updateTagById` | Update a tag on a mural. Tag text is limited to 25 characters. Authorization scope: murals:write |
| Update Mural Timer | `updateMuralTimer` | Pauses/resumes the mural timer and/or adds extra time to the running timer. Required authorization scope: murals:write |
| Update Mural Visitor Settings | `updateMuralVisitorSettings` | Update visitor settings of a mural, by an authenticated owner of the mural. Authorization scope: murals:write |
| Update Room | `updateRoomById` | Updates a room owned by the authenticated user. Authorization scope: rooms:write |
| Update Room Member Permissions | `updateRoomMemberPermissions` | Updates the permissions of one or more members of the specified room. Authorization scope: rooms:write |
| Update Shape Widget | `updateShapeWidget` | Update a shape widget on a mural. Authorization scope: murals:write |
| Update Sticky Note | `updateStickyNote` | Update a sticky note widget on a mural. Authorization scope: murals:write |
| Update Textbox | `updateTextbox` | Update a textbox widget on a mural. Authorization scope: murals:write |
| Update Title | `updateTitle` | Update a title widget on a mural. Authorization scope: murals:write |
| Vote For Widget In Voting Session | `voteWidgetMuralVotingSession` | Submit a vote for a widget in the active voting session of a mural. Required authorization scope: murals:write |
