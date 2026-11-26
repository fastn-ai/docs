---
description: "Microsoft Teams is team chat and meetings in Microsoft 365. Manage teams, channels, members, chats and messages."
hidden: true
---

# Microsoft Teams

<img src="../../.gitbook/assets/connectors/lg/microsoft-teams.png" alt="Microsoft Teams logo">

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [teams.microsoft.com](https://teams.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `microsoftTeams` |

## Setup

Your customers sign in to Microsoft Teams through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Microsoft Teams from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.microsoftTeams.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Team Member</td><td><code>addTeamMember</code></td><td>Add a user to a team by their user ID.</td></tr><tr><td>Create Channel</td><td><code>createChannel</code></td><td>Create a new channel in a team.</td></tr><tr><td>Create Subscription</td><td><code>createSubscription</code></td><td>Create a Microsoft Graph change-notification subscription for a Teams resource such as '/teams/{teamId}/channels/{channelId}/messages' or '/chats/{chatId}/messages' The notification URL must be a public HTTPS endpoint that answers Microsoft's validation handshake by echoing the plaintext validationToken within 10 seconds, otherwise Microsoft rejects the subscription. Requires the change-notification permission of the subscribed resource.</td></tr><tr><td>Delete Channel</td><td><code>deleteChannel</code></td><td>Delete a channel from a team. Cannot delete the General channel.</td></tr><tr><td>Get Channel</td><td><code>getChannel</code></td><td>Get details of a specific channel in a team.</td></tr><tr><td>Get Channel Message</td><td><code>getChannelMessage</code></td><td>Get a specific message from a team channel.</td></tr><tr><td>Get Chat</td><td><code>getChat</code></td><td>Get a specific chat by chat ID.</td></tr><tr><td>Get Me</td><td><code>getMe</code></td><td>Get the profile of the currently signed-in user.</td></tr><tr><td>Get Team</td><td><code>getTeam</code></td><td>Get details of a specific team by team ID.</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Get the profile of a single user by object id or userPrincipalName, for resolving the person behind a chat or channel message Requires User.ReadBasic.All or User.Read.All.</td></tr></tbody></table>

<details>

<summary>View 17 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Channel Messages</td><td><code>listChannelMessages</code></td><td>List messages in a team channel.</td></tr><tr><td>List Channels</td><td><code>listChannels</code></td><td>List all channels in a team Supports $filter and $select, e.g. filter to private channels only. Requires Channel.ReadBasic.All.</td></tr><tr><td>List Channels Flat</td><td><code>listChannelsFlat</code></td><td>List channels in a team with optional OData filtering, for example only private channels. Returns the standard Microsoft Graph collection envelope. Requires Channel.ReadBasic.All.</td></tr><tr><td>List Chat Members</td><td><code>listChatMembers</code></td><td>List the members of a Microsoft Teams chat, returning each member's membership id, display name, Entra ID user id and roles Requires ChatMember.Read or Chat.ReadWrite.</td></tr><tr><td>List Chat Messages</td><td><code>listChatMessages</code></td><td>List messages in a 1:1 or group chat Supports $top, $orderby (createdDateTime or lastModifiedDateTime, desc by default), $filter on those date fields, and $skiptoken paging. Requires Chat.Read.</td></tr><tr><td>List Chats</td><td><code>listChats</code></td><td>List all chats the current user is a member of.</td></tr><tr><td>List Joined Teams</td><td><code>listJoinedTeams</code></td><td>List all Microsoft Teams the current user is a member of.</td></tr><tr><td>List Message Replies</td><td><code>listMessageReplies</code></td><td>List all replies to a channel message.</td></tr><tr><td>List Team Members</td><td><code>listTeamMembers</code></td><td>List all members of a team.</td></tr><tr><td>List User Joined Teams</td><td><code>listUserJoinedTeams</code></td><td>List the teams that a specified user is a member of Use List Joined Teams for the signed-in user instead. Requires Team.ReadBasic.All and, for another user, User.Read.All.</td></tr><tr><td>List Users</td><td><code>listUsers</code></td><td>List users in the organization so their ids can be used to add members or start chats Supports OData filtering, ordering, search and paging. Requires User.ReadBasic.All or User.Read.All.</td></tr><tr><td>Remove Team Member</td><td><code>removeTeamMember</code></td><td>Remove a member from a team by their membership ID.</td></tr><tr><td>Reply to Channel Message</td><td><code>replyToChannelMessage</code></td><td>Reply to a message in a team channel.</td></tr><tr><td>Send Channel Message</td><td><code>sendChannelMessage</code></td><td>Send a message to a team channel.</td></tr><tr><td>Send Chat Message</td><td><code>sendChatMessage</code></td><td>Send a message to a chat.</td></tr><tr><td>Update Channel</td><td><code>updateChannel</code></td><td>Update the display name and/or description of a channel Only the fields you pass are sent, so omitted fields keep their current value. Requires Channel.ReadWrite.All.</td></tr><tr><td>Update Team</td><td><code>updateTeam</code></td><td>Update settings of a team such as description or member permissions.</td></tr></tbody></table>

</details>

## Events

Microsoft Teams has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
