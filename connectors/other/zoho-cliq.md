---
description: "Zoho Cliq is Zoho's team chat/messaging platform."
hidden: true
---

# Zoho Cliq

Zoho Cliq is Zoho's team chat/messaging platform. This connector provides access to Cliq's REST API v2: channels, chats (1:1/group), messages, threads, reactions, users, user status, teams, departments, designations, bots, scheduled messages, and organization/profile data.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [zoho.com](https://zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 64 |
| **Events** | 0 |
| **Slug** | `zohoCliq` |

## Use it

Add Zoho Cliq from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoCliq.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Bot to Channel | `addBotToChannel` | Associate a bot with a channel. |
| Add Channel Members | `addChannelMembers` | Add members to a channel. |
| Add Reaction | `addReaction` | Add an emoji reaction to a message. |
| Add Status | `addStatus` | Create a new saved custom status message for the authenticated user. |
| Add Team Members | `addTeamMembers` | Add members to a team. |
| Add Thread Followers | `addThreadFollowers` | Add followers to a thread. |
| Add Users | `addUsers` | Invite/add new users to the Zoho Cliq organization. |
| Archive Channel | `archiveChannel` | Archive a channel. |
| Create Channel | `createChannel` | Create a new channel in Zoho Cliq. |
| Create Team | `createTeam` | Create a new team within the organization. |
| Create Thread Message | `createThreadMessage` | Start a new thread by posting a message in a channel with a thread_message_id. |
| Delete Channel | `deleteChannel` | Delete a channel. |
| Delete Ephemeral Status | `deleteEphemeralStatus` | Remove the current transient status before it expires. |
| Delete Message | `deleteMessage` | Delete a message from a chat. |
| Delete Reaction | `deleteReaction` | Remove your emoji reaction from a message. |
| Delete Status | `deleteStatus` | Delete a saved custom status. |
| Delete Sticky Message | `deleteStickyMessage` | Remove the sticky (pinned) message of a chat. |
| Delete Team | `deleteTeam` | Delete a team. |
| Delete Team Member | `deleteTeamMember` | Remove a specific member from a team. |
| Edit Message | `editMessage` | Edit the text of an existing message. |
| Follow Thread | `followThread` | Follow a thread as the authenticated user. |
| Get Bot Subscribers | `getBotSubscribers` | Get the list of users subscribed to a bot. |
| Get Channel | `getChannel` | Retrieve details of a specific channel. |
| Get Channel Members | `getChannelMembers` | Get the list of members in a channel. |
| Get Channel Threads | `getChannelThreads` | Get threads within a channel. |
| Get Chat Members | `getChatMembers` | Get the members of a chat. |
| Get Current Status | `getCurrentStatus` | Get the current chat status (available, busy, away, etc.) of the authenticated user. |
| Get File | `getFile` | Get metadata/content for a file shared in Zoho Cliq by its file ID. |
| Get Message | `getMessage` | Retrieve a specific message from a chat. |
| Get Messages | `getMessages` | Retrieve messages of a chat within a time range. |
| Get Reactions | `getReactions` | Get the reactions on a message. |
| Get Sticky Message | `getStickyMessage` | Get the sticky (pinned) message of a chat. |
| Get Team | `getTeam` | Retrieve details of a specific team. |
| Get Team Members | `getTeamMembers` | Get the list of members in a team. |
| Get Thread Followers | `getThreadFollowers` | Get the followers of a thread. |
| Get Thread Non-Followers | `getThreadNonFollowers` | Get the users who are not following a thread. |
| Get User | `getUser` | Retrieve details of a specific user. |
| Get User Teams | `getUserTeams` | Fetch the list of teams a user belongs to. |
| Join Channel | `joinChannel` | Join a channel as the authenticated user. |
| Leave Channel | `leaveChannel` | Leave a channel as the authenticated user. |
| Leave Chat | `leaveChat` | Leave a group chat. |
| List Channels | `listChannels` | List channels in the Zoho Cliq organization. |
| List Chats | `listChats` | List chats (1:1, group chats, channels) for the authenticated user. |
| List Statuses | `listStatuses` | List all saved custom status messages for the authenticated user. |
| List Teams | `listTeams` | List teams in the organization. |
| List User Field Layouts | `listUserFieldLayouts` | List the user profile field layout definitions. |
| List Users | `listUsers` | List all users in the Zoho Cliq organization. |
| Mute Chat | `muteChat` | Mute a chat. |
| Post Message to Bot | `postMessageToBot` | Post a text message to a bot. |
| Post Message to Channel | `postMessageToChannel` | Post a text message into a channel by channel ID. |
| Post Message to Chat | `postMessageToChat` | Post a text message into a chat (1:1, group, or channel) by chat ID. |
| Post Message to User | `postMessageToUser` | Post a direct message to a user (buddy) by email or ZUID. |
| Remove Channel Members | `removeChannelMembers` | Remove members from a channel. |
| Remove Thread Followers | `removeThreadFollowers` | Remove followers from a thread. |
| Set Ephemeral Status | `setEphemeralStatus` | Set a temporary (transient) chat status that auto-expires. |
| Set Sticky Message | `setStickyMessage` | Pin a message as the sticky message of a chat. |
| Trigger Bot Call | `triggerBotCall` | Trigger a bot to place a call and dictate a message to one or more users. |
| Unarchive Channel | `unarchiveChannel` | Unarchive a previously archived channel. |
| Unfollow Thread | `unfollowThread` | Unfollow a thread as the authenticated user. |
| Unmute Chat | `unmuteChat` | Unmute a chat. |
| Update Channel | `updateChannel` | Update a channel's name, description or configuration. |
| Update Current Status | `updateCurrentStatus` | Set the authenticated user's current status to a previously saved status by ID. |
| Update Team | `updateTeam` | Update a team's name or description. |
| Update User | `updateUser` | Update details of an existing user. |
