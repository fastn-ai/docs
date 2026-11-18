---
description: "Google Chat API v1 connector for managing spaces, members, messages, reactions, attachments, space events, read state, and notification settings in Google Chat."
hidden: true
---

# Google Chat

<img src="../../.gitbook/assets/connectors/lg/google-chat.png" alt="Google Chat logo">

Google Chat API v1 connector for managing spaces, members, messages, reactions, attachments, space events, read state, and notification settings in Google Chat.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [chat.googleapis.com](https://chat.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleChat` |

## Use it

Add Google Chat from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleChat.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Member As Admin | `createMembershipAdmin` | Adds a user from the organization to any Google Chat space using administrator privileges (spaces.members.create with useAdminAccess=true); if the user's auto-accept is off they are invited instead. Admin access cannot add Chat apps or users outside the organization. Google scope: chat.admin.memberships. Requires a Workspace administrator with the Manage Chat and spaces conversations privilege. Remove with Remove Member As Admin. Returns the created Membership. |
| Create Custom Emoji | `createCustomEmoji` | Creates a custom emoji in the authenticated user's Google Workspace organization from a base64-encoded image. Custom emojis are only available to Google Workspace accounts and the administrator must have turned custom emojis on for the organization. |
| Create Membership | `createMembership` | Adds a human user or a Google Group as a member of a Google Chat space, or invites a user to it. Provide either a member (User) or groupMember (Group). |
| Create Message | `createMessage` | Sends a message to a Google Chat space. Supports plain or formatted text, rich interactive cards (cardsV2), threading, accessory widgets, and private messages visible to a single user. |
| Create Reaction | `createReaction` | Adds an emoji reaction to a message in a Google Chat space. Provide either a standard Unicode emoji or a custom emoji reference. |
| Create Section | `createSection` | Creates a custom section in the signed-in user's Google Chat navigation panel to group conversations (users.sections.create, type CUSTOM_SECTION). Only affects the caller's own view. Google scope: chat.users.sections. Remove it with Delete Section. Returns the created section with its name (users/{user}/sections/{section}). |
| Create Space | `createSpace` | Creates a named space or group chat in Google Chat. Set spaceType to SPACE for a named space (displayName required) or GROUP_CHAT for an unnamed group conversation. To create a direct message, use Set Up Space instead. |
| Delete Custom Emoji | `deleteCustomEmoji` | Deletes a custom emoji from the authenticated user's Google Workspace organization. Only the creator of the custom emoji or an organization emoji manager can delete it. |
| Delete Membership | `deleteMembership` | Removes a member from a Google Chat space. The removed member no longer has access to the space's messages. |
| Delete Message | `deleteMessage` | Deletes a message from a Google Chat space. Set force to true to also delete any threaded replies to the message. |

<details>

<summary>See 42 more actions</summary>

* **Delete Reaction** `deleteReaction`: Removes an emoji reaction from a message in a Google Chat space.
* **Delete Section** `deleteSection`: Deletes one of the signed-in user's custom Google Chat sections (users.sections.delete); spaces in it move back to their default section. System sections cannot be deleted. Google scope: chat.users.sections. Returns an empty body on success.
* **Delete Space** `deleteSpace`: Deletes a named Google Chat space and everything in it, including messages, memberships, and attachments.
* **Delete Space As Admin** `deleteSpaceAdmin`: Permanently deletes a Google Chat space owned by the organization, including all its messages and memberships, using administrator privileges (spaces.delete with useAdminAccess=true). Irreversible: only target a throwaway test space. Google scope: chat.admin.delete. Requires a Workspace administrator with the Manage Chat and spaces conversations privilege. Returns an empty body on success.
* **Download Attachment Media** `downloadAttachmentMedia`: Downloads the binary media of a Google Chat attachment using its attachment data resource name, returning the file content.
* **Find Direct Message** `findDirectMessage`: Returns the existing direct message space between the authenticated user and the specified user, if one exists. Returns 404 if no direct message space has been created between them.
* **Get Attachment** `getAttachment`: Returns the metadata of a message attachment in a Google Chat space, including its content type and a resource name for downloading the media.
* **Get Custom Emoji** `getCustomEmoji`: Returns details about a single custom emoji in the authenticated user's Google Workspace organization, including its emoji name and a temporary image URL.
* **Get Membership** `getMembership`: Returns details about a single membership in a Google Chat space, including the member and their role.
* **Get Message** `getMessage`: Returns details about a single message in a Google Chat space, including its text, cards, sender, and thread.
* **Get My Availability** `getUserAvailability`: Gets the signed-in user's Google Chat availability (users.availability.get): current state (ACTIVE, IDLE, AWAY or DO_NOT_DISTURB), Do Not Disturb metadata and custom status. Read-only; only the caller's own availability can be read. Google scope: chat.users.availability.readonly (or chat.users.availability). Returns the Availability resource.
* **Get Space** `getSpace`: Returns details about a single Google Chat space, including its display name, type, history state, and access settings.
* **Get Space As Admin** `getSpaceAdmin`: Gets any Google Chat space in the Workspace organization using administrator privileges (spaces.get with useAdminAccess=true), even if the admin is not a member. Read-only. Google scope: chat.admin.spaces.readonly (or chat.admin.spaces). Requires a Workspace administrator with the Manage Chat and spaces conversations privilege. Returns the Space resource.
* **Get Space Event** `getSpaceEvent`: Returns a single event that happened in a Google Chat space, such as a new message, membership change, or reaction. The event's payload matches its event type.
* **Get Space Notification Setting** `getSpaceNotificationSetting`: Returns the authenticated user's notification settings for a Google Chat space, including the notification level and mute state.
* **Get Space Read State** `getSpaceReadState`: Returns the authenticated user's read state for a Google Chat space, indicating up to which time messages have been read.
* **Get Thread Read State** `getThreadReadState`: Returns the authenticated user's read state for a specific thread within a Google Chat space, indicating up to which time thread replies have been read.
* **List Custom Emojis** `listCustomEmojis`: Lists the custom emojis visible to the authenticated user in their Google Workspace organization. Custom emojis are only available to Google Workspace accounts and the administrator must have turned custom emojis on for the organization.
* **List Memberships** `listMemberships`: Lists the memberships in a Google Chat space, including joined and optionally invited members and Google Groups. Supports filtering and pagination.
* **List Memberships As Admin** `listMembershipsAdmin`: Lists the human and group members of any Google Chat space in the organization using administrator privileges (spaces.members.list with useAdminAccess=true). Read-only. Google scope: chat.admin.memberships.readonly (or chat.admin.memberships). App memberships are not returned with admin access. Requires a Workspace administrator with the Manage Chat and spaces conversations privilege. Returns memberships[] (name, state, role, member) and nextPageToken.
* **List Message Pins** `listMessagePins`: Lists the pinned messages in a Google Chat space (spaces.messagePins.list). Read-only. Google scope: chat.spaces.pins.readonly (chat.spaces.pins, chat.spaces or chat.spaces.readonly also work). User must be a member of the space. Returns messagePins[] (name and message resource name) and nextPageToken.
* **List Messages** `listMessages`: Lists messages in a Google Chat space that the authenticated user can access. Supports filtering by time and thread, ordering, and including deleted messages.
* **List Reactions** `listReactions`: Lists the emoji reactions on a message in a Google Chat space. Supports filtering by emoji or reacting user and pagination.
* **List Section Items** `listSectionItems`: Lists the spaces grouped under one of the signed-in user's Google Chat sections (users.sections.items.list). Use section '-' with filter space = spaces/{space} to find which section holds a space. Read-only. Google scope: chat.users.sections.readonly (or chat.users.sections). Returns sectionItems[] (name, space) and nextPageToken.
* **List Sections** `listSections`: Lists the signed-in user's Google Chat navigation sections (users.sections.list): the system sections (direct messages, spaces, apps) and any custom sections. Read-only. Google scope: chat.users.sections.readonly (or chat.users.sections). Returns sections[] (name, displayName, type, sortOrder) and nextPageToken.
* **List Space Events** `listSpaceEvents`: Lists events that happened in a Google Chat space, such as messages, memberships, and reactions. A filter specifying at least one event type is required.
* **List Spaces** `listSpaces`: Lists the Google Chat spaces the authenticated user is a member of. Supports filtering by space type and pagination.
* **Mark Me As Active** `markAvailabilityActive`: Sets the signed-in user's Google Chat availability to ACTIVE (users.availability.markAsActive) until an optional expiry, after which it reverts to activity-based state (AWAY when idle). Use a short ttl such as 60s to effectively reset the state. Only affects the caller. Google scope: chat.users.availability. Returns the updated Availability.
* **Mark Me As Away** `markAvailabilityAway`: Sets the signed-in user's Google Chat availability to AWAY (users.availability.markAsAway). The state persists regardless of activity until changed, e.g. with Mark Me As Active. Only affects the caller. Google scope: chat.users.availability. Returns the updated Availability.
* **Patch Message** `patchMessage`: Partially updates a message in a Google Chat space (PATCH). Only the fields listed in updateMask are changed; other fields are left untouched.
* **Pin Message** `createMessagePin`: Pins a message in a Google Chat space so members can find it easily (spaces.messagePins.create). Google scope: chat.spaces.pins (or chat.spaces). User must be a member of the space with permission to pin. Undo with Unpin Message. Returns the MessagePin; its ID matches the message ID.
* **Remove Member As Admin** `deleteMembershipAdmin`: Removes a human or group member from any Google Chat space in the organization using administrator privileges (spaces.members.delete with useAdminAccess=true). App memberships cannot be removed with admin access. Google scope: chat.admin.memberships. Requires a Workspace administrator with the Manage Chat and spaces conversations privilege. Returns the deleted Membership.
* **Search Spaces As Admin** `searchSpacesAdmin`: Searches all Google Chat spaces in the Workspace organization using administrator privileges (spaces.search with useAdminAccess=true), including spaces the admin is not a member of. Read-only. Google scope: chat.admin.spaces.readonly (or chat.admin.spaces). The connected user must be a Workspace administrator with the Manage Chat and spaces conversations privilege. The query must include customer = "customers/my_customer" AND space_type = "SPACE". Returns spaces/results, totalSize and nextPageToken.
* **Set Up Space** `setupSpace`: Creates a Google Chat space and adds specified members to it in a single request. Use this to create a direct message or group chat with named members, or a named space with an initial membership list.
* **Unpin Message** `deleteMessagePin`: Removes a message pin from a Google Chat space (spaces.messagePins.delete); the message itself is not deleted. Google scope: chat.spaces.pins (or chat.spaces). Returns an empty body on success.
* **Update Membership** `updateMembership`: Updates a membership in a Google Chat space, typically to change a member's role between ROLE_MEMBER and ROLE_MANAGER.
* **Update Message** `updateMessage`: Updates a message in a Google Chat space using a full update (PUT). Supply the fields listed in updateMask; unlisted updatable fields are cleared.
* **Update Space** `updateSpace`: Updates fields of an existing Google Chat space. The updateMask query parameter lists which fields to change, for example displayName, spaceDetails, or spaceHistoryState.
* **Update Space As Admin** `patchSpaceAdmin`: Updates a Google Chat space's display name or description/guidelines using administrator privileges (spaces.patch with useAdminAccess=true). Only the fields named in updateMask change. With admin access Google supports the masks display_name, space_details and permission_settings.* (not space_type, space_history_state or access_settings). Google scope: chat.admin.spaces. Requires a Workspace administrator with the Manage Chat and spaces conversations privilege. Returns the updated Space.
* **Update Space Notification Setting** `updateSpaceNotificationSetting`: Updates the authenticated user's notification settings for a Google Chat space, such as the notification level or whether the space is muted.
* **Update Space Read State** `updateSpaceReadState`: Updates the authenticated user's read state for a Google Chat space, marking messages as read or unread up to a given time.
* **Upload Attachment** `uploadAttachment`: Uploads a file as an attachment to a Google Chat space. Returns an attachment data reference that can be included when creating a message. Binary uploads must be provided as a file reference.

</details>
