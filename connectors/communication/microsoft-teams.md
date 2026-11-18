---
description: "Microsoft Teams via Microsoft Graph API v1.0 — manage teams, channels, channel messages, replies, chats, chat messages, and members."
hidden: true
---

# Microsoft Teams

<img src="../../.gitbook/assets/connectors/lg/microsoft-teams.png" alt="Microsoft Teams logo">

Microsoft Teams via Microsoft Graph API v1.0 — manage teams, channels, channel messages, replies, chats, chat messages, and members.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [teams.microsoft.com](https://teams.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `microsoftTeams` |

## Use it

Add Microsoft Teams from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.microsoftTeams.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Team Member | `addTeamMember` | Add a user to a team by their user ID. |
| Create Channel | `createChannel` | Create a new channel in a team. |
| Create Subscription | `createSubscription` | Create a Microsoft Graph change-notification subscription for a Teams resource such as '/teams/{teamId}/channels/{channelId}/messages' or '/chats/{chatId}/messages' (POST /subscriptions). The notification URL must be a public HTTPS endpoint that answers Microsoft's validation handshake by echoing the plaintext validationToken within 10 seconds, otherwise Microsoft rejects the subscription. Requires the change-notification permission of the subscribed resource. |
| Delete Channel | `deleteChannel` | Delete a channel from a team. Cannot delete the General channel. |
| Get Channel | `getChannel` | Get details of a specific channel in a team. |
| Get Channel Message | `getChannelMessage` | Get a specific message from a team channel. |
| Get Chat | `getChat` | Get a specific chat by chat ID. |
| Get Me | `getMe` | Get the profile of the currently signed-in user. |
| Get Team | `getTeam` | Get details of a specific team by team ID. |
| Get User | `getUser` | Get the profile of a single user by object id or userPrincipalName, for resolving the person behind a chat or channel message (GET /users/{userId}). Requires User.ReadBasic.All or User.Read.All. |

<details>

<summary>See 17 more actions</summary>

* **List Channel Messages** `listChannelMessages`: List messages in a team channel.
* **List Channels** `listChannels`: List all channels in a team (GET /teams/{teamId}/channels). Supports $filter and $select, e.g. filter to private channels only. Requires Channel.ReadBasic.All.
* **List Channels Flat** `listChannelsFlat`: List channels in a team with optional OData filtering (GET /teams/{teamId}/channels), for example only private channels. Returns the standard Microsoft Graph collection envelope. Requires Channel.ReadBasic.All.
* **List Chat Members** `listChatMembers`: List the members of a Microsoft Teams chat, returning each member's membership id, display name, Entra ID user id and roles (GET /chats/{chatId}/members). Requires ChatMember.Read or Chat.ReadWrite.
* **List Chat Messages** `listChatMessages`: List messages in a 1:1 or group chat (GET /chats/{chatId}/messages). Supports $top, $orderby (createdDateTime or lastModifiedDateTime, desc by default), $filter on those date fields, and $skiptoken paging. Requires Chat.Read.
* **List Chats** `listChats`: List all chats the current user is a member of.
* **List Joined Teams** `listJoinedTeams`: List all Microsoft Teams the current user is a member of.
* **List Message Replies** `listMessageReplies`: List all replies to a channel message.
* **List Team Members** `listTeamMembers`: List all members of a team.
* **List User Joined Teams** `listUserJoinedTeams`: List the teams that a specified user is a member of (GET /users/{userId}/joinedTeams). Use List Joined Teams for the signed-in user instead. Requires Team.ReadBasic.All and, for another user, User.Read.All.
* **List Users** `listUsers`: List users in the organization so their ids can be used to add members or start chats (GET /users). Supports OData filtering, ordering, search and paging. Requires User.ReadBasic.All or User.Read.All.
* **Remove Team Member** `removeTeamMember`: Remove a member from a team by their membership ID.
* **Reply to Channel Message** `replyToChannelMessage`: Reply to a message in a team channel.
* **Send Channel Message** `sendChannelMessage`: Send a message to a team channel.
* **Send Chat Message** `sendChatMessage`: Send a message to a chat.
* **Update Channel** `updateChannel`: Update the display name and/or description of a channel (PATCH /teams/{teamId}/channels/{channelId}). Only the fields you pass are sent, so omitted fields keep their current value. Returns 204 No Content. Requires Channel.ReadWrite.All.
* **Update Team** `updateTeam`: Update settings of a team such as description or member permissions.

</details>
