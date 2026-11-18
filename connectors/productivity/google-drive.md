---
description: "Google Drive API v3 — list, upload, download, copy, move, and manage files and folders."
hidden: true
---

# Google Drive

Google Drive API v3 — list, upload, download, copy, move, and manage files and folders. Supports shared drives, permissions, comments, and revisions.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [drive.google.com](https://drive.google.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 66 |
| **Events** | 7 |
| **Slug** | `googleDrive` |

## Use it

Add Google Drive from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleDrive.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Approve Approval | `approveApproval` | Approves an approval. POST to files/{fileId}/approvals/{approvalId}:approve. Updates the requesting user's ReviewerResponse. Returns the drive#approval. |
| Cancel Approval | `cancelApproval` | Cancels an approval. POST to files/{fileId}/approvals/{approvalId}:cancel. Updates the approval Status to CANCELLED. Returns the drive#approval. |
| Comment Approval | `commentApproval` | Comments on an approval. POST to files/{fileId}/approvals/{approvalId}:comment. Sends a notification to initiator and reviewers. Returns the drive#approval. |
| Copy File | `copyFile` | Create a copy of an existing file. Optionally give the copy a new name, place it in specific parent folders, and set a description. |
| Create Comment | `createComment` | Add a new comment to a file. |
| Create Drive | `createDrive` | Creates a shared drive. requestId is a REQUIRED query param (a random UUID uniquely identifying this user's request for idempotency). Body is a Drive resource; name is required. |
| Create File | `createFile` | Create a new file or folder metadata entry (no content upload). Set mimeType to application/vnd.google-apps.folder to create a folder. Provide parents to place it in specific folders (use 'root' for My Drive root). Use uploadFile to include content. |
| Create Folder | `createFolder` | Create a new folder in Google Drive. |
| Create Public Permission | `createPermission` | Create a public ("anyone") or domain-wide sharing permission on a file or folder. For sharing with a specific user or group by email, use Share With User instead. |
| Create Reply | `createReply` | Add a reply to a comment on a file. |
| Decline Approval | `declineApproval` | Declines an approval. POST to files/{fileId}/approvals/{approvalId}:decline. Updates the requesting user's ReviewerResponse. Returns the drive#approval. |
| Delete Comment | `deleteComment` | Delete a comment from a file. |
| Delete Drive | `deleteDrive` | Permanently deletes a shared drive for which the user is an organizer. The shared drive cannot contain any untrashed items unless allowItemDeletion is true. driveId is a required path param. |
| Delete File | `deleteFile` | Permanently delete a file by its ID. This cannot be undone. Use trashFile to move to trash instead. |
| Delete Permission | `deletePermission` | Remove a permission from a file or folder (revoke access). |
| Delete Reply | `deleteReply` | Deletes a reply to a comment. Returns an empty body (204) on success. |
| Delete Revision | `deleteRevision` | Permanently deletes a file version (revision). Only works for files with binary content (e.g. images or videos); not for Google Docs/Sheets or the last remaining revision. Returns an empty body (204) on success. |
| Download File | `downloadFile` | Starts a long-running download operation for the content of a file. Returns an Operation resource that can be polled via getOperation. Optionally specify mimeType (for Google editor files) or revisionId (for blobs). |
| Empty Trash | `emptyTrash` | Permanently deletes all of the user's trashed files. Optionally limited to a specific shared drive via driveId. Returns no content (204). |
| Export File | `exportFile` | Exports a Google Workspace document (Docs, Sheets, Slides) to the requested MIME type and returns the exported byte content. mimeType is REQUIRED. Only works for Google-native editor files, not binary blobs. |
| Generate CSE Token | `generateCseToken` | Generates a Client-Side Encryption (CSE) token (signed JWT) used to create or update CSE files. EXPECTED BLOCKED: requires Client-Side Encryption to be configured for the Workspace domain; returns an error on accounts without CSE/KACLS set up. |
| Generate File ID | `generateFileId` | Generate one or more unique file IDs that can be used in subsequent create requests. |
| Get About | `getAbout` | Get information about the current user and their Google Drive storage quota. |
| Get Access Proposal | `getAccessProposal` | Retrieves an access proposal by ID. Returns an AccessProposal resource. See Manage pending access proposals. |
| Get App | `getApp` | Gets a specific installed app by its ID. |
| Get Approval | `getApproval` | Gets an approval by ID. Returns a drive#approval resource. See Manage approvals. |
| Get Comment | `getComment` | Get a specific comment on a file by comment ID. |
| Get Drive | `getDrive` | Get metadata for a specific shared drive by its ID. |
| Get File | `getFile` | Get metadata for a specific file or folder by its ID. |
| Get Operation | `getOperation` | Gets the latest state of a long-running operation (e.g. the operation returned by downloadFile). Poll this to retrieve the result when done becomes true. |
| Get Permission | `getPermission` | Get a specific permission for a file or folder by permission ID. |
| Get Reply | `getReply` | Gets a reply to a comment by ID. Returns the reply's content, author, action (resolve/reopen), and timestamps. |
| Get Revision | `getRevision` | Get metadata for a specific revision of a file. |
| Get Start Page Token | `getStartPageToken` | Get the starting page token for listing future changes. Use this token with listChanges to receive incremental updates. |
| Hide Drive | `hideDrive` | Hides a shared drive from the default view. driveId is a required path param. No request body. |
| List Access Proposals | `listAccessProposals` | Lists the access proposals on a file. Only approvers can list. Returns ListAccessProposalsResponse. See Manage pending access proposals. |
| List Approvals | `listApprovals` | Lists the approvals on a file. Returns a drive#approvalList with items array. See Manage approvals. |
| List Apps | `listApps` | Lists the user's installed apps, optionally filtered by file extensions or MIME types. |
| List Changes | `listChanges` | List changes to files and shared drives since a page token. Use getStartPageToken to get the initial token. |
| List Comments | `listComments` | List all comments on a file. |
| List Drives | `listDrives` | List all shared drives accessible to the user. |
| List File Labels | `listFileLabels` | Lists the labels applied to a file. Returns a paginated LabelList. |
| List Files | `listFiles` | List files and folders in Google Drive. Filter using the q parameter (e.g. 'mimeType=application/vnd.google-apps.folder' or 'parents in ID'). |
| List Permissions | `listPermissions` | List all permissions for a file or folder. |
| List Replies | `listReplies` | List all replies to a comment on a file. |
| List Revisions | `listRevisions` | List all revisions of a file. |
| Modify File Labels | `modifyFileLabels` | Modifies the set of labels applied to a file. Provide labelModifications (an array of per-label modification objects). Returns the list of labels that were added or updated. |
| Move File | `moveFile` | Move a file to a different folder by updating its parents. |
| Reassign Approval | `reassignApproval` | Reassigns the reviewers on an approval. POST to files/{fileId}/approvals/{approvalId}:reassign. Adds or replaces reviewers. Returns the drive#approval. |
| Resolve Access Proposal | `resolveAccessProposal` | Approves or denies an access proposal. POST to files/{fileId}/accessproposals/{proposalId}:resolve. Returns an empty body on success. |
| Restore File | `restoreFile` | Restore a file from the trash. |
| Share With User | `shareWithUser` | Share a file or folder with a specific user or group by email address. Set Send Notification Email to false to grant access without emailing the recipient. Google defaults this to true. |
| Start Approval | `startApproval` | Starts an approval on a file. POST to files/{fileId}/approvals:start. Returns the created drive#approval. |
| Stop Channel | `stopChannel` | Stop watching resources through a notification channel. POST channels/stop with the channel id and the resourceId returned when the channel was created (both required). Returns an empty 204 body on success. |
| Trash File | `trashFile` | Move a file to the trash. The file can be restored later. |
| Unhide Drive | `unhideDrive` | Restores a shared drive to the default view. driveId is a required path param. No request body. |
| Update Comment | `updateComment` | Update the text content of an existing comment. |
| Update Drive | `updateDrive` | Updates the metadata for a shared drive. driveId is a required path param. Body is a Drive resource (name, colorRgb, themeId, hidden, restrictions, backgroundImageFile). |
| Update File | `updateFile` | Update a file or folder's metadata such as name, description, starred and trashed state. Does not change file content (use updateFileContent for that). |
| Update File Content | `updateFileContent` | Replace the byte content of an existing Drive file (keeps the same file ID). Uploads new bytes via the Drive media upload endpoint. Use this to overwrite a file's content; use updateFile to rename metadata only. Returns the file's id, name, mimeType, size, and md5Checksum. |
| Update Permission | `updatePermission` | Update the role of an existing permission (e.g. change reader to writer). |
| Update Reply | `updateReply` | Updates a reply to a comment with patch semantics. Set 'content' (the plain text content) and/or 'action' (resolve or reopen the parent comment). |
| Update Revision | `updateRevision` | Update a revision's keepForever flag to prevent automatic deletion. |
| Upload File With Content | `uploadFile` | Create a new Drive file AND write its real byte content in a single multipart upload. Sets name, mimeType, parent folder, and the file body together. Use this instead of createFile whenever the file should contain content. Returns the created file's id, name, mimeType, size, and md5Checksum. |
| Watch Changes | `watchChanges` | Subscribe to a drive-wide changes notification channel. POST changes/watch with a required pageToken (obtain via getStartPageToken) and a Channel body (id, type='web_hook', address). Google delivers X-Goog-Resource-State notifications to the address. Returns the Channel including resourceId, which together with the channel id is required to stop the channel. |
| Watch File | `watchFile` | Subscribe to a notification channel for changes to a single file. POST files/{fileId}/watch with a Channel body (id, type='web_hook', address). Google delivers X-Goog-Resource-State notifications to the address. Returns the Channel including resourceId, which together with the channel id is required to stop the channel. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Change Notification | `change` | A drive-wide change occurred on a changes/watch channel (X-Goog-Resource-State: change). Call listChanges with the stored pageToken to retrieve the actual changes. |
| Channel Sync | `sync` | Sent once immediately after a watch channel is created to confirm the subscription. X-Goog-Resource-State: sync. |
| Resource Added | `add` | A file or resource was added (X-Goog-Resource-State: add). Carried by file-level watch channels. |
| Resource Removed | `remove` | A file or resource was removed/access lost (X-Goog-Resource-State: remove). |
| Resource Trashed | `trash` | A file was moved to the trash (X-Goog-Resource-State: trash). |
| Resource Untrashed | `untrash` | A file was restored from the trash (X-Goog-Resource-State: untrash). |
| Resource Updated | `update` | A watched resource was updated (X-Goog-Resource-State: update). The X-Goog-Changed header lists what changed (content, properties, parents, children, permissions). |
