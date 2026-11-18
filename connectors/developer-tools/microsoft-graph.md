---
description: "Microsoft Graph API v1.0 — manage users, groups, mail, calendar events, and SharePoint sites across the Microsoft 365 ecosystem."
hidden: true
---

# Microsoft Graph

<img src="../../.gitbook/assets/connectors/lg/microsoft-graph.png" alt="Microsoft Graph logo">

Microsoft Graph API v1.0 — manage users, groups, mail, calendar events, and SharePoint sites across the Microsoft 365 ecosystem.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [microsoft.com](https://microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `microsoftGraph` |

## Use it

Add Microsoft Graph from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.microsoftGraph.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Event | `acceptEvent` | Accept a meeting invitation (POST /me/events/{eventId}/accept). Returns 202. |
| Add Group Member | `addGroupMember` | Add a user to a group. |
| Add Message Attachment | `addMessageAttachment` | Add a file attachment to a draft message (POST /me/messages/{messageId}/attachments) using base64 contentBytes. |
| Cancel Event | `cancelEvent` | Cancel an event as the organizer, sending a cancellation to attendees (POST /me/events/{eventId}/cancel). Returns 202. |
| Copy Message | `copyMessage` | Copy a message to another mail folder (POST /me/messages/{messageId}/copy). Returns the new message copy. |
| Create App Registration | `createAppRegistration` | Register a new application in Microsoft Entra ID (POST /applications). Creates the application object that a service principal can then be created from. Requires Application.ReadWrite.All and is a tenant-level change, so run it only against a tenant you administer. |
| Create App Role Assignment | `createAppRoleAssignments` | Assign an app role of a resource application to a user, group or service principal (POST /servicePrincipals/{principalId}/appRoleAssignments). This is how application permissions are granted to an app and how users are assigned to an enterprise application. Requires AppRoleAssignment.ReadWrite.All and grants privileges in the tenant. |
| Create Calendar | `createCalendar` | Create a new calendar in the default calendar group (POST /me/calendars). |
| Create Contact | `createContact` | Create an Outlook contact (POST /me/contacts). Requires Contacts.ReadWrite. Returns 201. |
| Create Drive Folder | `createDriveFolder` | Create a folder in OneDrive root (POST /me/drive/root/children). Requires Files.ReadWrite. Returns 201. |

<details>

<summary>See 106 more actions</summary>

* **Create Event** `createEvent`: Create a new calendar event.
* **Create Forward Draft** `createForward`: Create a draft forward of a message to recipients (POST /me/messages/{messageId}/createForward). Returns a draft message; does not send.
* **Create Group** `createGroup`: Create a new Microsoft 365 or security group.
* **Create Mail Folder** `createMailFolder`: Create a new mail folder under the mailbox root (POST /me/mailFolders).
* **Create Message (Draft)** `createMessage`: Create a draft email message in the signed-in user's mailbox (POST /me/messages). Returns the created draft message resource.
* **Create Message Rule** `createMessageRule`: Create an inbox rule that moves messages from a sender to a target folder (POST /me/mailFolders/inbox/messageRules).
* **Create OAuth2 Permission Grant** `createOauth2PermissionGrants`: Grant delegated permissions (OAuth2 scopes) from a resource API to a client service principal (POST /oauth2PermissionGrants). Consent can be granted for all users in the tenant or for a single user. Requires DelegatedPermissionGrant.ReadWrite.All and permanently changes what an application may do on behalf of users, so treat it as a privileged tenant change.
* **Create Reply Draft** `createReply`: Create a draft reply to a message (POST /me/messages/{messageId}/createReply). Returns a draft message; does not send.
* **Create Reply-All Draft** `createReplyAll`: Create a draft reply-all to a message (POST /me/messages/{messageId}/createReplyAll). Returns a draft message; does not send.
* **Create Service Principal** `createServicePrincipal`: Create a service principal (enterprise application instance) in the tenant for an existing application registration (POST /servicePrincipals). The application must already be registered; pass its application (client) id. Requires Application.ReadWrite.All and changes tenant-level identity configuration.
* **Create Subscription** `createSubscription`: Create a Microsoft Graph change-notification subscription (webhook) for a resource such as me/messages or me/events (POST /subscriptions). notificationUrl must respond to Graph's validation token within 10s.
* **Create User** `createUser`: Create a new user in the organization.
* **Decline Event** `declineEvent`: Decline a meeting invitation (POST /me/events/{eventId}/decline). Returns 202.
* **Delete Calendar** `deleteCalendar`: Delete a calendar (DELETE /me/calendars/{calendarId}). Returns 204.
* **Delete Contact** `deleteContact`: Delete an Outlook contact (DELETE /me/contacts/{contactId}). Requires Contacts.ReadWrite. Returns 204.
* **Delete Drive Item** `deleteDriveItem`: Delete a OneDrive item (DELETE /me/drive/items/{itemId}). Soft delete to recycle bin. Requires Files.ReadWrite. Returns 204.
* **Delete Event** `deleteEvent`: Delete a calendar event.
* **Delete Group** `deleteGroup`: Delete a group.
* **Delete Mail Folder** `deleteMailFolder`: Delete a mail folder (DELETE /me/mailFolders/{mailFolderId}). Returns 204.
* **Delete Message** `deleteMessage`: Delete an email message.
* **Delete Message Attachment** `deleteMessageAttachment`: Delete an attachment from a message (DELETE /me/messages/{messageId}/attachments/{attachmentId}). Returns 204.
* **Delete Subscription** `deleteSubscription`: Delete (unsubscribe) a change-notification subscription (DELETE /subscriptions/{subscriptionId}). Returns 204.
* **Delete User** `deleteUser`: Delete a user from the organization.
* **Find Meeting Times** `findMeetingTimes`: Suggest meeting times for the signed-in user and one attendee based on availability and a meeting duration (POST /me/findMeetingTimes). Returns candidate time slots with a confidence score. Requires Calendars.Read.Shared.
* **Forward Event** `forwardEvent`: Forward a meeting to additional recipients (POST /me/events/{eventId}/forward). Returns 202.
* **Forward Message** `forwardMessage`: Forward a message to recipients and send immediately (POST /me/messages/{messageId}/forward). Returns 202 Accepted with no body.
* **Get Calendar** `getCalendar`: Get a calendar by id, or use 'calendar' for the default (GET /me/calendars/{calendarId}).
* **Get Chat** `getChat`: Get a Teams chat by id (GET /chats/{chatId}).
* **Get Contact** `getContact`: Get a single Outlook contact by id (GET /me/contacts/{contactId}). Requires Contacts.Read.
* **Get Drive** `getDrive`: Get the signed-in user's default OneDrive (GET /me/drive). Requires Files.Read.
* **Get Drive Item** `getDriveItem`: Get a OneDrive item (file or folder) by id (GET /me/drive/items/{itemId}). Requires Files.Read.
* **Get Drive Item By Path** `getDriveItemByPath`: Get a OneDrive item by path (GET /me/drive/root:/{path}). Requires Files.Read.
* **Get Event** `getEvent`: Get a specific calendar event by ID.
* **Get Group** `getGroup`: Get details of a specific group by group ID.
* **Get Mail Folder** `getMailFolder`: Get a mail folder by id or well-known name (GET /me/mailFolders/{mailFolderId}).
* **Get Mailbox Settings** `getMailboxSettings`: Get the signed-in user's mailbox settings — time zone, language, automatic replies, working hours (GET /me/mailboxSettings).
* **Get Me** `getMe`: Get the profile of the currently signed-in user (GET /me). Supports $select to choose properties and $expand to include related entities such as the user's manager. Requires User.Read.
* **Get Message** `getMessage`: Get a specific email message by ID.
* **Get Message Attachment** `getMessageAttachment`: Get a single attachment of a message (GET /me/messages/{messageId}/attachments/{attachmentId}).
* **Get My Drive** `getMyDrive`: Get the signed-in user's OneDrive (GET /me/drive). Returns drive id, driveType, owner, quota.
* **Get My Manager** `getMyManager`: Get the signed-in user's manager (GET /me/manager). Requires User.Read.All.
* **Get My Photo** `getMyPhoto`: Get the signed-in user's profile photo binary (GET /me/photo/$value). Returns image bytes; 404 if no photo set.
* **Get My Photo Metadata** `getMyPhotoMetadata`: Get profile photo metadata (GET /me/photo): id, height, width, contentType.
* **Get Root Site** `getRootSite`: Get the tenant root SharePoint site (GET /sites/root). Requires Sites.Read.All.
* **Get Schedule** `getSchedule`: Get free/busy availability for a mailbox over a time window (POST /me/calendar/getSchedule). Returns an availability view string plus the mailbox's working hours. Requires Calendars.Read.Shared.
* **Get Service Principal By App ID** `getServicePrincipalByAppId`: Get the service principal (enterprise application) for an application client id, including the OAuth2 delegated permissions and app roles it publishes (GET /servicePrincipals(appId='{appId}')). Use it to inspect which permissions an app exposes before granting them. Requires Application.Read.All.
* **Get Site** `getSite`: Get a SharePoint site by site ID.
* **Get Site Root** `getSiteRoot`: Get the tenant root SharePoint site (GET /sites/root). Returns site id, displayName, webUrl.
* **Get Subscription** `getSubscription`: Get a single change-notification subscription by id (GET /subscriptions/{subscriptionId}).
* **Get Team** `getTeam`: Get a team's full settings (GET /teams/{teamId}). Requires Team.ReadBasic.All.
* **Get Team Channel** `getTeamChannel`: Get a single channel in a Team (GET /teams/{teamId}/channels/{channelId}).
* **Get User** `getUser`: Get a specific user by object id or userPrincipalName (GET /users/{userId}). Supports $select to choose properties and $expand to include related entities such as the user's manager. Requires User.Read.All.
* **List Calendar Groups** `listCalendarGroups`: List the user's calendar groups (GET /me/calendarGroups).
* **List Calendar View** `listCalendarView`: List occurrences/events in the calendar within a time window, expanding recurring series (GET /me/calendarView?startDateTime=&endDateTime=).
* **List Calendars** `listCalendars`: List all calendars for the signed-in user.
* **List Channel Messages** `listChannelMessages`: List messages in a team channel (GET /teams/{teamId}/channels/{channelId}/messages). Requires ChannelMessage.Read.All.
* **List Channels** `listChannels`: List channels in a team (GET /teams/{teamId}/channels). Requires Channel.ReadBasic.All.
* **List Chat Messages** `listChatMessages`: List messages in a Teams chat (GET /chats/{chatId}/messages). Requires Chat.Read.
* **List Chats** `listChats`: List the signed-in user's Teams chats (GET /me/chats). Requires Chat.ReadBasic.
* **List Child Folders** `listChildFolders`: List child folders of a mail folder (GET /me/mailFolders/{mailFolderId}/childFolders).
* **List Contacts** `listContacts`: List the signed-in user's Outlook contacts (GET /me/contacts). Requires Contacts.Read.
* **List Drive Root Children** `listDriveRootChildren`: List items in the root of the user's OneDrive (GET /me/drive/root/children). Requires Files.Read.
* **List Drives** `listDrives`: List all drives available to the signed-in user (GET /me/drives). Requires Files.Read.
* **List Event Instances** `listEventInstances`: List occurrences of a recurring event series within a time window (GET /me/events/{eventId}/instances?startDateTime=&endDateTime=).
* **List Events** `listEvents`: List calendar events for the signed-in user.
* **List Folder Children** `listFolderChildren`: List children of a specific drive item / folder by id (GET /me/drive/items/{itemId}/children).
* **List Folder Messages** `listFolderMessages`: List messages within a specific mail folder (GET /me/mailFolders/{mailFolderId}/messages).
* **List Group Members** `listGroupMembers`: List members of a group.
* **List Groups** `listGroups`: List all groups in the organization.
* **List Joined Teams** `listJoinedTeams`: List teams the signed-in user is a member of (GET /me/joinedTeams). Requires Team.ReadBasic.All.
* **List Mail Folders** `listMailFolders`: List all mail folders in the signed-in user's mailbox.
* **List Message Attachments** `listMessageAttachments`: List attachments of a message (GET /me/messages/{messageId}/attachments).
* **List Message Rules** `listMessageRules`: List inbox message rules (GET /me/mailFolders/inbox/messageRules).
* **List Messages** `listMessages`: List email messages in the signed-in user's mailbox.
* **List My Chats** `listMyChats`: List the signed-in user's Teams chats (GET /me/chats). Use $top to page.
* **List My Direct Reports** `listMyDirectReports`: List the signed-in user's direct reports (GET /me/directReports). Requires User.Read.All.
* **List Organizations** `listOrganizations`: List the organization (tenant) resource for the signed-in user's Microsoft Entra ID tenant, including tenant id, display name, verified domains and assigned service plans. The collection always contains exactly one organization, so this also answers "which tenant am I connected to". Requires Organization.Read.All or User.Read.
* **List Site Drives** `listSiteDrives`: List document libraries (drives) in a SharePoint site (GET /sites/{siteId}/drives). Requires Sites.Read.All.
* **List Site List Items** `listSiteListItems`: List items in a SharePoint list (GET /sites/{siteId}/lists/{listId}/items?expand=fields). Requires Sites.Read.All.
* **List Site Lists** `listSiteLists`: List all lists in a SharePoint site.
* **List Sites** `listSites`: Search and list SharePoint sites.
* **List Subscriptions** `listSubscriptions`: List active Microsoft Graph change-notification subscriptions for the app/user (GET /subscriptions).
* **List Team Members** `listTeamMembers`: List members of a team (GET /teams/{teamId}/members). Requires TeamMember.Read.All.
* **List User Direct Reports** `listUserDirectReports`: List the users and contacts who report directly to the specified user (GET /users/{userId}/directReports). Accepts a user object id or userPrincipalName. Requires User.Read.All.
* **List Users** `listUsers`: List users in the organization (GET /users). Supports OData $select, $filter, $orderby, $search, $count and paging; the request always sends ConsistencyLevel: eventual so advanced queries such as $count and $search work. Requires User.Read.All.
* **Move Message** `moveMessage`: Move a message to another mail folder (POST /me/messages/{messageId}/move). Returns the moved message with a new id.
* **Reauthorize Subscription** `reauthorizeSubscription`: Reauthorize a change-notification subscription after a reauthorizationRequired lifecycle event (POST /subscriptions/{subscriptionId}/reauthorize). Returns 204.
* **Remove Group Member** `removeGroupMember`: Remove a user from a group.
* **Renew Subscription** `renewSubscription`: Renew (extend the expiration of) a change-notification subscription (PATCH /subscriptions/{subscriptionId}).
* **Reply To Message** `replyMessage`: Reply to the sender of a message and send immediately (POST /me/messages/{messageId}/reply). Returns 202 Accepted with no body.
* **Reply-All To Message** `replyAllMessage`: Reply to all recipients of a message and send immediately (POST /me/messages/{messageId}/replyAll). Returns 202 Accepted with no body.
* **Search Drive Items** `searchDriveItems`: Search the user's OneDrive for items matching a query (GET /me/drive/root/search(q='{query}')).
* **Search Sites** `searchSites`: Search SharePoint sites by keyword (GET /sites?search={query}). Requires Sites.Read.All.
* **Send Channel Message** `sendChannelMessage`: Post a message to a team channel (POST /teams/{teamId}/channels/{channelId}/messages). Requires ChannelMessage.Send. Returns 201.
* **Send Chat Message** `sendChatMessage`: Send a message to an existing Teams chat (POST /chats/{chatId}/messages). Requires ChatMessage.Send. Returns 201.
* **Send Draft Message** `sendDraftMessage`: Send an existing draft message (POST /me/messages/{messageId}/send). Returns 202 Accepted with no body.
* **Send Mail** `sendMail`: Send an email from the signed-in user's mailbox.
* **Tentatively Accept Event** `tentativelyAcceptEvent`: Tentatively accept a meeting invitation (POST /me/events/{eventId}/tentativelyAccept). Returns 202.
* **Update Calendar** `updateCalendar`: Update a calendar's name or color (PATCH /me/calendars/{calendarId}).
* **Update Contact** `updateContact`: Update an Outlook contact (PATCH /me/contacts/{contactId}). Requires Contacts.ReadWrite.
* **Update Event** `updateEvent`: Update an existing calendar event.
* **Update Mail Folder** `updateMailFolder`: Rename a mail folder (PATCH /me/mailFolders/{mailFolderId}).
* **Update Mailbox Settings** `updateMailboxSettings`: Update mailbox settings such as time zone or automatic replies (PATCH /me/mailboxSettings).
* **Update Message** `updateMessage`: Update writable properties of a message, e.g. mark read/unread, change subject, importance, categories, or isDraft body (PATCH /me/messages/{messageId}).
* **Update User** `updateUser`: Update properties of a user.
* **Upload Drive File** `uploadDriveFile`: Upload (create/replace) a small file (&lt;=250MB) by path (PUT /me/drive/root:/{path}:/content). Body is raw file content. Requires Files.ReadWrite. Returns 200/201.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Calendar Event Created | `event.created` | A new calendar event was created (resource me/events, changeType created). |
| Calendar Event Deleted | `event.deleted` | A calendar event was deleted (resource me/events, changeType deleted). |
| Calendar Event Updated | `event.updated` | A calendar event was updated (resource me/events, changeType updated). |
| Message Created | `message.created` | A new message arrived in the user's mailbox (resource me/messages, changeType created). |
| Message Deleted | `message.deleted` | A message was deleted (resource me/messages, changeType deleted). |
| Message Updated | `message.updated` | A message was updated, e.g. read/flag change (resource me/messages, changeType updated). |
