---
description: "Twist by Doist — asynchronous team communication."
hidden: true
---

# Twist

<img src="../../.gitbook/assets/connectors/twist.png" alt="Twist logo" width="64">

Twist by Doist — asynchronous team communication. Manage workspaces, channels, threads, comments, messages, groups, reactions, attachments, notifications, and search via the Twist API v3.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [twist.com](https://twist.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `twist` |

## Use it

Add Twist from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.twist.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Channel Member | `addChannelMember` | Adds a single workspace user to a Twist channel and returns the updated channel. |
| Add Channel Members | `addChannelMembers` | Adds several workspace users to a Twist channel in one call and returns the updated channel. |
| Add Conversation Member | `addConversationMember` | Adds a single workspace user to a Twist conversation and returns the updated conversation. |
| Add Conversation Members | `addConversationMembers` | Adds several workspace users to a Twist conversation in one call and returns the updated conversation. |
| Add Group Member | `addGroupMember` | Adds a single workspace user to a Twist group. |
| Add Group Members | `addGroupMembers` | Adds several workspace users to a Twist group in one call. |
| Add Reaction | `addReaction` | Adds an emoji reaction to a Twist thread, comment or conversation message on behalf of the authenticated user. Supply exactly one of the thread, comment or message identifiers. |
| Add Workspace Member | `addWorkspaceMember` | Invites a person to a Twist workspace by email, optionally setting their name, role and the channels they join. Twist sends the invitation email as part of this call. |
| Add Workspace Member (v3) | `addWorkspaceMemberV3` | Invites a person to a Twist workspace using the older v3 endpoint. Doist has deprecated this route in favour of Add Workspace Member. |
| Archive All Inbox Threads | `archiveAllInboxThreads` | Archives every thread in the authenticated user's Twist inbox for a workspace, optionally only those older than a given time. |

<details>

<summary>See 114 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Channel | `archiveChannel` | Archives a Twist channel so it no longer appears in the active channel list. A channel must be archived before it can be deleted. |
| Archive Conversation | `archiveConversation` | Archives a Twist conversation so it no longer appears in the authenticated user's active message list. |
| Archive Inbox Thread | `archiveInboxThread` | Archives a single thread out of the authenticated user's Twist inbox. The thread itself stays in its channel. |
| Autocomplete Threads | `autocompleteThreads` | Finds Twist threads whose title contains the given text, across every channel the authenticated user can see. Intended for type-ahead thread pickers. |
| Check Google Connection | `checkGoogleConnection` | Reports whether the authenticated Twist account is linked to a Google account, and which Google address it is linked to. |
| Clear Unread Threads | `clearUnreadThreads` | Clears the unread thread indicator across an entire Twist workspace for the authenticated user. |
| Create Channel | `createChannel` | Creates a new channel in a Twist workspace, optionally seeding its members, colour, icon and default notification recipients. |
| Create Comment | `createComment` | Posts a new comment to a Twist thread. Passing a thread action of close or reopen alongside the comment also closes or reopens the thread. |
| Create Group | `createGroup` | Creates a new user group in a Twist workspace so that a set of people can be notified together in threads. |
| Create Thread | `createThread` | Creates a new thread in a Twist channel, optionally notifying specific users or groups and attaching files or action buttons. |
| Create Workspace | `createWorkspace` | Creates a new Twist workspace owned by the authenticated user. |
| Delete Channel | `deleteChannel` | Permanently deletes a Twist channel and all of its threads. The channel must already be archived, and the deletion cannot be undone. |
| Delete Comment | `deleteComment` | Deletes a Twist thread comment. Only the original author or a workspace administrator may delete a comment. |
| Delete Conversation Message | `deleteConversationMessage` | Deletes a message from a Twist conversation. Only the original sender can delete their message. |
| Delete Group | `deleteGroup` | Deletes a Twist user group. The people in the group keep their workspace membership. |
| Delete Thread | `deleteThread` | Permanently deletes a Twist thread and all of its comments. The deletion cannot be undone. |
| Delete Workspace | `deleteWorkspace` | Permanently deletes a Twist workspace and all of its data. Requires the authenticated user's current password for confirmation and cannot be undone. |
| Disable Loop In Email | `disableLoopInEmail` | Disables the loop-in email address of a Twist channel, thread or conversation so mail sent to it is no longer posted. |
| Disable Workspace Invite Link | `disableWorkspaceInviteLink` | Disables the invite link of a Twist workspace so it can no longer be used to join. |
| Disconnect Google Account | `disconnectGoogleAccount` | Unlinks the authenticated Twist account from its Google account, after which Google sign-in can no longer be used for it. |
| Execute Batch Request | `executeBatchRequest` | Runs several Twist API calls in a single HTTP request and returns their consolidated responses in the same order. Unlike the rest of the Twist API this endpoint parses only form-encoded input, so the connector submits it that way. |
| Favorite Channel | `favoriteChannel` | Marks a Twist channel as a favourite for the authenticated user so it is pinned to the top of their sidebar. |
| Get Channel | `getChannel` | Retrieves a single Twist channel by its identifier. |
| Get Comment | `getComment` | Retrieves a single Twist thread comment by its identifier. The comment is returned nested under a comment key. |
| Get Conversation | `getConversation` | Retrieves a single Twist conversation by its identifier, including its participants and last message. |
| Get Conversation Message | `getConversationMessage` | Retrieves a single Twist conversation message by its identifier. |
| Get Default Workspace | `getDefaultWorkspace` | Retrieves the authenticated user's default Twist workspace. |
| Get Group | `getGroup` | Retrieves a single Twist user group by its identifier. |
| Get Inbox | `getInbox` | Retrieves the authenticated user's Twist inbox for a workspace as a list of the most recently active threads. |
| Get Inbox Count | `getInboxCount` | Returns how many threads are currently in the authenticated user's Twist inbox for a workspace. |
| Get Notification Settings | `getNotificationSettings` | Retrieves the authenticated user's desktop, email, push and badge notification settings for a Twist workspace. |
| Get Or Create Conversation | `getOrCreateConversation` | Returns the Twist conversation shared by the given set of users, creating it first if it does not already exist. |
| Get Or Create Loop In Email | `getOrCreateLoopInEmail` | Returns the email address that forwards mail into a Twist channel, thread or conversation, creating the address first if it does not exist. |
| Get Or Create Workspace Invite Link | `getOrCreateWorkspaceInviteLink` | Returns the invite link for a Twist workspace, creating one first if the workspace does not have an active link. |
| Get Reactions | `getReactions` | Retrieves the reactions on a Twist thread, comment or conversation message. Supply exactly one of the thread, comment or message identifiers. The response is a map whose keys are the emoji and whose values are the identifiers of the users who reacted; it is an empty object when there are no reactions. |
| Get Session User | `getSessionUser` | Retrieves the profile of the user associated with the current access token, including id, name, email, timezone, and default workspace. Useful as a lightweight credential verification call. |
| Get Thread | `getThread` | Retrieves a single Twist thread by its identifier, including its content, participants, reactions and unread state. |
| Get Workspace | `getWorkspace` | Retrieves a single Twist workspace by its identifier. |
| Get Workspace Invite Link | `getWorkspaceInviteLink` | Returns the existing invite link for a Twist workspace. The URL is null when no link has been created or the link has been disabled. |
| Get Workspace Member | `getWorkspaceMember` | Retrieves one member of a Twist workspace by their user identifier. |
| Get Workspace Member (v3) | `getWorkspaceMemberV3` | Retrieves one member of a Twist workspace by user identifier using the older v3 endpoint. Doist has deprecated this route in favour of Get Workspace Member. |
| Get Workspace Member By Email | `getWorkspaceMemberByEmail` | Retrieves one member of a Twist workspace by their email address. Twist's v4 endpoint currently answers 404 Resource not found even for members that exist, so use Get Workspace Member By Email (v3) until Doist fixes it. |
| Get Workspace Member By Email (v3) | `getWorkspaceMemberByEmailV3` | Retrieves one member of a Twist workspace by email using the older v3 endpoint. Doist has deprecated this route, but it is currently the only lookup-by-email that works, because the v4 replacement answers 404. |
| Get Workspace Member Info | `getWorkspaceMemberInfo` | Retrieves a member's profile together with their current local time, in the context of a Twist workspace. |
| Get Workspace Member Info (v3) | `getWorkspaceMemberInfoV3` | Retrieves a member's profile and local time using the older v3 endpoint. Doist has deprecated this route in favour of Get Workspace Member Info. |
| Get Workspace Member Local Time | `getWorkspaceMemberLocalTime` | Returns the current local time of a member of a Twist workspace, which is useful before pinging someone outside their working hours. The endpoint responds with a bare JSON string rather than an object. |
| Get Workspace Member Local Time (v3) | `getWorkspaceMemberLocalTimeV3` | Returns a workspace member's current local time using the older v3 endpoint, as a bare JSON string. Doist has deprecated this route in favour of Get Workspace Member Local Time. |
| Join Workspace By Invite Link | `joinWorkspaceByInviteLink` | Adds the authenticated user to a Twist workspace using that workspace's invite link. |
| List Channels | `listChannels` | Lists the channels of a Twist workspace that the authenticated user can see, optionally returning archived channels instead of active ones. |
| List Comments | `listComments` | Lists the comments posted in a Twist thread, with pagination by timestamp or comment index. |
| List Conversation Messages | `listConversationMessages` | Lists the messages in a Twist conversation, with pagination by message index. Full message objects are always returned; unlike the thread and comment list endpoints, this one has no identifiers-only mode. |
| List Conversations | `listConversations` | Lists the Twist conversations the authenticated user takes part in within a workspace, with cursor-style pagination and an option to return archived conversations. |
| List Groups | `listGroups` | Lists the user groups defined in a Twist workspace. |
| List Public Channels | `listPublicChannels` | Lists the public channels of a Twist workspace, including channels the authenticated user has not joined. |
| List Threads | `listThreads` | Lists the threads in a Twist channel, with filtering by attachment, pinned or starred state and cursor-style pagination by identifier or timestamp. |
| List Unread Conversations | `listUnreadConversations` | Lists the Twist conversations in a workspace that have messages the authenticated user has not read. |
| List Unread Threads | `listUnreadThreads` | Lists the threads in a Twist workspace that the authenticated user has not fully read, returning the unread position for each. |
| List Workspace Member IDs | `listWorkspaceMemberIds` | Lists just the user identifiers of the people who belong to a Twist workspace, which is cheaper than fetching full member profiles. |
| List Workspace Members | `listWorkspaceMembers` | Lists the people who belong to a Twist workspace, with the public profile information other members can see. |
| List Workspace Members (v3) | `listWorkspaceMembersV3` | Lists the people who belong to a Twist workspace using the older v3 endpoint. Doist has deprecated this route in favour of List Workspace Members; use that unless you need v3 compatibility. |
| List Workspaces | `listWorkspaces` | Lists every Twist workspace the authenticated user belongs to. |
| Mark All Inbox Threads Read | `markAllInboxThreadsRead` | Marks every thread in the authenticated user's Twist inbox for a workspace as read. |
| Mark All Threads Read | `markAllThreadsRead` | Marks every thread in a Twist channel, or in a whole workspace, as read for the authenticated user. Supply either a channel or a workspace identifier. |
| Mark Comment Position | `markCommentPosition` | Records the last comment the authenticated user has read in a Twist thread, which drives the unread marker shown in the Twist clients. |
| Mark Conversation Read | `markConversationRead` | Marks a Twist conversation as read up to a given message for the authenticated user. Supply either the message index or the message identifier. |
| Mark Conversation Unread | `markConversationUnread` | Marks a Twist conversation as unread from a given message for the authenticated user. Supply either the message index or the message identifier; the index must refer to an existing message. |
| Mark Thread Read | `markThreadRead` | Marks a Twist thread as read up to the given comment index for the authenticated user. |
| Mark Thread Unread | `markThreadUnread` | Marks a Twist thread as unread from the given comment index for the authenticated user. |
| Mark Thread Unread For Others | `markThreadUnreadForOthers` | Marks a Twist thread as unread for the other participants, which is useful for drawing their attention back to a thread that changed. |
| Move Thread To Channel | `moveThreadToChannel` | Moves a Twist thread, together with all of its comments, into a different channel in the same workspace. |
| Mute Conversation | `muteConversation` | Mutes a Twist conversation for a number of minutes so the authenticated user receives no notifications from it. |
| Mute Thread | `muteThread` | Mutes a Twist thread for a number of minutes so new comments on it stop reaching the authenticated user's inbox. |
| Pin Thread | `pinThread` | Pins a Twist thread to the top of its channel for everyone in the workspace. |
| Remove Attachment | `removeAttachment` | Removes a file attachment from a Twist thread, comment or conversation message. Supply exactly one of the thread, comment or message identifiers. |
| Remove Channel Member | `removeChannelMember` | Removes a single user from a Twist channel and returns the updated channel. |
| Remove Channel Members | `removeChannelMembers` | Removes several users from a Twist channel in one call and returns the updated channel. |
| Remove Conversation Member | `removeConversationMember` | Removes a single user from a Twist conversation and returns the updated conversation. Note that this endpoint only accepts POST, although the Twist reference shows it as a GET. |
| Remove Conversation Members | `removeConversationMembers` | Removes several users from a Twist conversation in one call and returns the updated conversation. Note that this endpoint only accepts POST, although the Twist reference shows it as a GET. |
| Remove Group Member | `removeGroupMember` | Removes a single user from a Twist group. |
| Remove Group Members | `removeGroupMembers` | Removes several users from a Twist group in one call. |
| Remove Reaction | `removeReaction` | Removes the authenticated user's emoji reaction from a Twist thread, comment or conversation message. Supply exactly one of the thread, comment or message identifiers. |
| Remove Workspace Member | `removeWorkspaceMember` | Removes a person from a Twist workspace. Their existing threads and comments stay, because the content belongs to the workspace. |
| Remove Workspace Member (v3) | `removeWorkspaceMemberV3` | Removes a person from a Twist workspace using the older v3 endpoint. Doist has deprecated this route in favour of Remove Workspace Member. |
| Resend Workspace Invite | `resendWorkspaceInvite` | Sends a fresh Twist workspace invitation to someone who has not yet accepted their original invite. |
| Resend Workspace Invite (v3) | `resendWorkspaceInviteV3` | Resends a Twist workspace invitation using the older v3 endpoint. Doist has deprecated this route in favour of Resend Workspace Invite. |
| Reset User Presence | `resetUserPresence` | Marks the authenticated user as inactive in a Twist workspace, which is the counterpart to Set User Presence. |
| Search Conversation Messages | `searchConversationMessages` | Searches the messages of a single Twist conversation and returns the identifiers of the messages that match, up to the latest 10000 matches. |
| Search Thread Comments | `searchThreadComments` | Searches the comments of a single Twist thread and returns the identifiers of the comments that match, up to the latest 10000 matches. |
| Search Workspace | `searchWorkspace` | Runs a full-text search across the threads and conversations of a Twist workspace, sorted by last activity, with optional filters on type, author, recipients, channels and dates. |
| Send Conversation Message | `sendConversationMessage` | Sends a new message to an existing Twist conversation, optionally with mentions, attachments and action buttons. |
| Set User Presence | `setUserPresence` | Marks the authenticated user as active in the given Twist workspace, recording the platform the user is active on. |
| Star Thread | `starThread` | Stars a Twist thread for the authenticated user so it can be found quickly later. |
| Subscribe Webhook | `subscribeWebhook` | Registers an outgoing webhook so Twist sends a JSON payload to the given URL whenever the chosen event happens. The subscription can optionally be narrowed to a single workspace, channel, thread or conversation. |
| Unarchive Channel | `unarchiveChannel` | Restores a previously archived Twist channel to the active channel list. |
| Unarchive Conversation | `unarchiveConversation` | Restores an archived Twist conversation to the authenticated user's active message list. |
| Unarchive Inbox Thread | `unarchiveInboxThread` | Returns a previously archived thread to the authenticated user's Twist inbox. |
| Unfavorite Channel | `unfavoriteChannel` | Removes a Twist channel from the authenticated user's favourites. |
| Unmute Conversation | `unmuteConversation` | Unmutes a Twist conversation so the authenticated user receives its notifications again. |
| Unmute Thread | `unmuteThread` | Unmutes a Twist thread so new comments reach the authenticated user's inbox again. |
| Unpin Thread | `unpinThread` | Removes a Twist thread from the pinned threads of its channel. |
| Unstar Thread | `unstarThread` | Removes the authenticated user's star from a Twist thread. |
| Unsubscribe Webhook | `unsubscribeWebhook` | Stops Twist sending outgoing webhook events to the given URL, removing every event subscription registered for it. |
| Update Channel | `updateChannel` | Updates an existing Twist channel. Only the fields supplied are changed; the channel name is always required by the API. |
| Update Comment | `updateComment` | Updates the content, mentions, attachments or action buttons of an existing Twist thread comment. |
| Update Conversation | `updateConversation` | Updates the title of a Twist group conversation, and optionally archives it at the same time. |
| Update Conversation Message | `updateConversationMessage` | Updates a Twist conversation message. Only messages sent by the authenticated user can be edited. |
| Update Group | `updateGroup` | Renames an existing Twist user group. |
| Update Notification Setting | `updateNotificationSetting` | Changes one of the authenticated user's notification settings for a Twist workspace. |
| Update Notification Settings | `updateNotificationSettings` | Changes several of the authenticated user's notification settings for a Twist workspace in one call. The settings must be supplied as a JSON-encoded string, which is what the Twist endpoint expects on the wire. |
| Update Thread | `updateThread` | Updates the title, content, mentions, attachments or action buttons of an existing Twist thread. |
| Update User Profile | `updateUserProfile` | Updates the authenticated Twist user's own profile and availability settings, including their name, timezone, away mode and off days. |
| Update Workspace | `updateWorkspace` | Updates the name of an existing Twist workspace. |
| Update Workspace Member | `updateWorkspaceMember` | Changes the role a person holds in a Twist workspace. Identify the person by either their email address or their user identifier. |
| Update Workspace Member (v3) | `updateWorkspaceMemberV3` | Changes a person's role in a Twist workspace using the older v3 endpoint. Doist has deprecated this route in favour of Update Workspace Member. |

</details>
