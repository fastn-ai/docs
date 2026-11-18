---
description: "Connect to Slack to send messages, manage channels, interact with users, and automate workflows directly in your Slack workspace."
hidden: true
---

# Slack

Connect to Slack to send messages, manage channels, interact with users, and automate workflows directly in your Slack workspace.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [slack.com](https://slack.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 177 |
| **Events** | 59 |
| **Slug** | `slack` |

## Use it

Add Slack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.slack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Admin Conversation Restrict Access Group | `createAdminConversationsRestrictAccessAddGroup` | Add an allowlist of IDP groups for accessing a channel |
| Add Admin Emoji | `createAdminEmojiAdd` | Add an emoji. |
| Add Admin Emoji Alias | `createAdminEmojiAddAlia` | Add an emoji alias. |
| Add Admin Usergroup Channels | `createAdminUsergroupsAddChannel` | Add one or more default channels to an IDP group. |
| Add Admin Usergroup Teams | `createAdminUsergroupsAddTeam` | Associate one or more default workspaces with an organization-wide IDP group. |
| Add Call | `createCallsAdd` | Registers a new Call. ⛔ VERIFIED-BLOCKED 2026-06-05: missing_scope needed=calls:write — Slack app's configured bot scopes omit calls:*; re-grantable if app config adds calls:write + reinstall. |
| Add Call Participants | `createCallsParticipantsAdd` | Registers new participants added to a Call. ⛔ VERIFIED-BLOCKED 2026-06-05: missing_scope needed=calls:write (same as above). |
| Add Reaction | `createReactionsAdd` | Adds a reaction to an item. |
| Add Reminder | `createRemindersAdd` | Creates a reminder. ⛔ VERIFIED-BLOCKED 2026-06-05: not_allowed_token_type — reminders.* require a user token even though reminders:read/write appear in bot grant. |
| Add Remote File | `createFilesRemoteAdd` | Adds a file from a remote service. VERIFY 2026-06-05: BLOCKED — ok:false error="missing_scope" needed="remote_files:write" (not granted to the bot token). configHealthy:true, auth+routing OK. |
| Add Star | `createStarsAdd` | Adds a star to an item. ⛔ VERIFIED-BLOCKED 2026-06-05: missing_scope needed=stars:write — user-token-only scope, not grantable to bot. |
| Approve Admin App | `createAdminAppsApprove` | Approve an app for installation on a workspace. |
| Approve Admin Invite Request | `createAdminInviteRequestsApprove` | Approve a workspace invite request. |
| Archive Admin Conversation | `createAdminConversationsArchive` | Archive a public or private channel. |
| Archive Conversation | `createConversationsArchive` | Archives a conversation. |
| Assign Admin User | `createAdminUsersAssign` | Add an Enterprise user to a workspace. |
| Close Conversation | `createConversationsClose` | Closes a direct message or multi-person direct message. |
| Complete Reminder | `createRemindersComplete` | Marks a reminder as complete. ⛔ VERIFIED-BLOCKED 2026-06-05: not_allowed_token_type — user-token-only. |
| Complete Upload External | `completeUploadExternal` | Step 3 of Slack's file upload flow (files.completeUploadExternal). Finalizes files whose bytes were uploaded to the upload_url from Get Upload URL External, and optionally shares them to a channel or as a thread reply with an introductory comment. Without channel_id or channels the file stays private. Replaces the deprecated files.upload method. Requires the files:write scope. |
| Complete Workflow Step | `listWorkflowsStepCompleted` | [DEPRECATED] Retired by Slack. workflows.stepCompleted ceased functioning on 2024-09-26 with the Steps from Apps retirement (https://api.slack.com/legacy/workflows/steps/migration); Slack now answers ok:false / unknown_method. There is no direct replacement; use custom functions on the Slack automation platform. |
| Connect RTM | `listRtmConnect` | Starts a Real Time Messaging session. |
| Convert Admin Conversation To Private | `createAdminConversationsConvertToPrivate` | Convert a public channel to a private channel. |
| Create Admin Conversation | `createAdminConversationsCreate` | Create a public or private channel-based conversation. |
| Create Admin Team | `createAdminTeamsCreate` | Create an Enterprise team. |
| Create Conversation | `createConversationsCreate` | Initiates a public or private channel-based conversation |
| Create User Group | `createUsergroupsCreate` | Create a User Group. BLOCKED (live 2026-06-05): HTTP 200 ok:false error="permission_denied" (warning missing_charset) — usergroups write requires a paid plan / admin privileges this workspace lacks. configHealthy:true (auth + routing OK). Sent {name, handle}. |
| Delete Admin Conversation | `createAdminConversationsDelete` | Delete a public or private channel. |
| Delete File | `createFilesDelete` | Deletes a file. VERIFY 2026-06-05: business-400 — ok:false error="file_not_found" with a placeholder id. configHealthy:true, auth+routing OK. No real file id is constructible (files.list empty; files.upload deprecated). |
| Delete File Comment | `createFilesCommentsDelete` | Deletes an existing comment on a file. VERIFY 2026-06-05: business-400 — ok:false error="file_not_found" with placeholder ids. configHealthy:true, auth+routing OK. No real file/comment id constructible (files.list empty; files.upload deprecated). Note: file comments are a legacy Slack feature. |
| Delete Message | `createChatDelete` | Deletes a message. |
| Delete Reminder | `createRemindersDelete` | Deletes a reminder. ⛔ VERIFIED-BLOCKED 2026-06-05: not_allowed_token_type — user-token-only. |
| Delete Scheduled Message | `createChatDeleteScheduledMessage` | Deletes a pending scheduled message from the queue. |
| Delete User Photo | `createUsersDeletePhoto` | Delete a user's profile photo. BLOCKED (live 2026-06-05): HTTP 200 ok:false error="not_allowed_token_type" — user-token-only (users.profile:write); bot token. configHealthy:true. |
| Deny Admin Invite Request | `createAdminInviteRequestsDeny` | Deny a workspace invite request. |
| Disable User Group | `createUsergroupsDisable` | Disable a User Group. BLOCKED (live 2026-06-05): HTTP 200 ok:false error="permission_denied" — usergroups write requires paid plan/admin. configHealthy:true. Sent {usergroup}. |
| Disconnect Admin Shared Conversation | `createAdminConversationsDisconnectShared` | Disconnect a connected channel from one or more workspaces. |
| Enable User Group | `createUsergroupsEnable` | Enable a User Group. BLOCKED (live 2026-06-05): HTTP 200 ok:false error="permission_denied" — usergroups write requires paid plan/admin. configHealthy:true. Sent {usergroup}. |
| End Call | `createCallsEnd` | Ends a Call. ⛔ VERIFIED-BLOCKED 2026-06-05: missing_scope needed=calls:write (same). |
| End Do Not Disturb | `createDndEndDnd` | End the current user's Do Not Disturb session. BLOCKED (live 2026-06-05): dnd setters are user-token-only; bot token lacks dnd:write. Provider account-state block. ⛔ VERIFIED-BLOCKED 2026-06-05: not_allowed_token_type — dnd.endDnd requires a user token (dnd:write user scope); connection has bot token. |
| End Snooze | `createDndEndSnooze` | End the current user's snooze mode. BLOCKED (live 2026-06-05): dnd setters are user-token-only; bot token lacks dnd:write. Provider account-state block. ⛔ VERIFIED-BLOCKED 2026-06-05: not_allowed_token_type — user-token-only (dnd:write). |
| Exchange Migration IDs | `listMigrationExchange` | Exchange a global user ID for a local team-specific user ID (Enterprise Grid). BLOCKED (live 2026-06-05): HTTP 200 ok:false error="not_enterprise_team" — workspace is not Enterprise Grid (auth.test is_enterprise_install:false). configHealthy:true. Sent {users}. |
| Exchange OAuth V2 Access Token | `listOauthV2Access` | Exchanges a temporary OAuth authorization code (or a refresh token when token rotation is enabled) for a Slack access token using the app's client ID and secret. Credentials are sent in a form-encoded POST body, not the query string. |
| Fail Workflow Step | `listWorkflowsStepFailed` | [DEPRECATED] Retired by Slack. workflows.stepFailed ceased functioning on 2024-09-26 with the Steps from Apps retirement (https://api.slack.com/legacy/workflows/steps/migration); Slack now answers ok:false / unknown_method. There is no direct replacement; use custom functions on the Slack automation platform. |
| Get Admin Conversation Preferences | `listAdminConversationsGetConversationPrefs` | Get conversation preferences for a public or private channel. |
| Get Admin Conversation Teams | `listAdminConversationsGetTeams` | Get all the workspaces a given public or private channel is connected to within this Enterprise org. |
| Get Admin Team Settings | `listAdminTeamsSettingsInfo` | Fetch information about settings in a workspace |
| Get App Permissions Info | `listAppsPermissionsInfo` | [DEPRECATED] Retired by Slack. apps.permissions.info belonged to legacy workspace apps, which retired on 2021-08-24 (https://api.slack.com/legacy/workspace-apps, https://api.slack.com/permissions-api). Slack now answers ok:false / unknown_method. No replacement exists; use a modern Slack app with granular bot scopes. |
| Get Bot Info | `listBotsInfo` | Gets information about a bot user. |
| Get Call Info | `listCallsInfo` | Returns information about a Call. ⛔ VERIFIED-BLOCKED 2026-06-05: missing_scope needed=calls:read (same root cause). |
| Get Conversation Info | `listConversationsInfo` | Retrieve information about a conversation. |
| Get DND Info | `listDndInfo` | Get a user's Do Not Disturb status. BLOCKED (live 2026-06-05): HTTP 200 ok:false error="missing_scope", needed="dnd:read" not in bot token scopes. configHealthy:true. |
| Get File Info | `listFilesInfo` | Gets information about a file. VERIFY 2026-06-05: business-400 — ok:false error="file_not_found" with a placeholder id. configHealthy:true, auth+routing OK. No real file id is constructible: bot has files:read but files.list returns zero visible files and the only create path (files.upload) is method_deprecated. |
| Get Message Permalink | `listChatGetPermalink` | Retrieve a permalink URL for a specific extant message |
| Get OAuth Access Token | `listOauthAccess` | Exchanges a temporary OAuth verifier code for an access token. |
| Get OAuth Token | `listOauthToken` | [DEPRECATED] Retired by Slack. oauth.token was the legacy workspace-app token exchange and retired with workspace apps on 2021-08-24 (https://api.slack.com/legacy/workspace-apps). Slack now answers ok:false / unknown_method. Use the modern OAuth v2 exchange (oauth.v2.access) instead. |
| Get Reactions | `listReactionsGet` | Gets reactions for an item. |
| Get Reminder Info | `listRemindersInfo` | Gets information about a reminder. ⛔ VERIFIED-BLOCKED 2026-06-05: not_allowed_token_type — user-token-only. |
| Get Remote File Info | `listFilesRemoteInfo` | Retrieves info about a remote file. VERIFY 2026-06-05: BLOCKED — ok:false error="missing_scope" needed="remote_files:read" (not granted to the bot token). configHealthy:true. |
| Get Team Billable Info | `listTeamBillableInfo` | Get billable info for a team. BLOCKED (live 2026-06-05): HTTP 200 ok:false error="not_allowed_token_type" — requires an admin/owner user token; bot token not allowed. |
| Get Team DND Info | `listDndTeamInfo` | Get DND status for users on a team. BLOCKED (live 2026-06-05): HTTP 200 ok:false error="missing_scope", needed="dnd:read". configHealthy:true. |
| Get Team Info | `listTeamInfo` | Gets information about the current team. |
| Get Team Profile | `listTeamProfileGet` | Retrieve a team's profile. |
| Get Upload URL External | `getUploadUrlExternal` | Step 1 of Slack's file upload flow (files.getUploadURLExternal). Reserves an upload URL and a file ID for a file of the given name and size. Next, send the raw file bytes with an HTTP POST to the returned upload_url (a plain upload, not a Slack API method), then call Complete Upload External with the returned file_id to finalize and share the file. Replaces the deprecated files.upload method. Requires the files:write scope. |
| Get User Identity | `listUsersIdentity` | Get the identity of the authed user. BLOCKED (live 2026-06-05): HTTP 200 ok:false error="not_allowed_token_type" — requires a user token with identity.basic; connection has a bot token only. |
| Get User Info | `listUsersInfo` | Gets information about a user. |
| Get User Presence | `listUsersGetPresence` | Get a user's presence. Live 2026-06-05 ok:true for user=U0AAPV88L9E. Query param 'user'. Requires users:read (present). |
| Get User Profile | `listUsersProfileGet` | Retrieves a user's profile information. |
| Invalidate Admin User Session | `createAdminUsersSessionInvalidate` | Invalidate a single session for a user by session_id |
| Invite Admin User | `createAdminUsersInvite` | Invite a user to a workspace. |
| Invite To Admin Conversation | `createAdminConversationsInvite` | Invite a user to a public or private channel. |
| Invite Users to Conversation | `createConversationsInvite` | Invites users to a channel. |
| Join Conversation | `createConversationsJoin` | Joins an existing conversation. |
| Kick User From Conversation | `createConversationsKick` | Removes a user from a conversation. |
| Leave Conversation | `createConversationsLeave` | Leaves a conversation. |
| List Admin App Requests | `listAdminAppsRequestsList` | List app requests for a team/workspace. |
| List Admin Conversation Restrict Access Groups | `listAdminConversationsRestrictAccessListGroups` | List all IDP Groups linked to a channel |
| List Admin EKM Connected Channel Info | `listAdminConversationsEkmListOriginalConnectedChannelInfo` | List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM. |
| List Admin Emoji | `listAdminEmojiList` | List emoji for an Enterprise Grid organization. |
| List Admin Invite Requests | `listAdminInviteRequestsList` | List all pending workspace invite requests. |
| List Admin Team Admins | `listAdminTeamsAdminsList` | List all of the admins on a given workspace. |
| List Admin Team Owners | `listAdminTeamsOwnersList` | List all of the owners on a given workspace. |
| List Admin Teams | `listAdminTeamsList` | List all teams on an Enterprise organization |
| List Admin Usergroup Channels | `listAdminUsergroupsListChannels` | List the channels linked to an org-level IDP group (user group). |
| List Admin Users | `listAdminUsersList` | List users on a workspace |
| List App Event Authorizations | `listAppsEventAuthorizationsList` | Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to. |
| List App Permission Resources | `listAppsPermissionsResourcesList` | [DEPRECATED] Retired by Slack. apps.permissions.resources.list belonged to legacy workspace apps, which retired on 2021-08-24 (https://api.slack.com/legacy/workspace-apps, https://api.slack.com/permissions-api). Slack now answers ok:false / unknown_method. No replacement exists; use a modern Slack app with granular bot scopes. |
| List App Permission Scopes | `listAppsPermissionsScopesList` | [DEPRECATED] Retired by Slack. apps.permissions.scopes.list belonged to legacy workspace apps, which retired on 2021-08-24 (https://api.slack.com/legacy/workspace-apps, https://api.slack.com/permissions-api). Slack now answers ok:false / unknown_method. No replacement exists; use a modern Slack app with granular bot scopes. |
| List App Permission Users | `listAppsPermissionsUsersList` | [DEPRECATED] Retired by Slack. apps.permissions.users.list belonged to legacy workspace apps, which retired on 2021-08-24 (https://api.slack.com/legacy/workspace-apps, https://api.slack.com/permissions-api). Slack now answers ok:false / unknown_method. No replacement exists; use a modern Slack app with granular bot scopes. |
| List Approved Admin Apps | `listAdminAppsApprovedList` | List approved apps for an org or workspace. |
| List Approved Admin Invite Requests | `listAdminInviteRequestsApprovedList` | List all approved workspace invite requests. |
| List Conversation History | `listConversationsHistory` | Fetches a conversation's history of messages and events. |
| List Conversation Members | `listConversationsMembers` | Retrieve members of a conversation. |
| List Conversation Replies | `listConversationsReplies` | Retrieve a thread of messages posted to a conversation |
| List Conversations | `listConversationsList` | Lists all channels in a Slack team. |
| List Conversations Flat | `listConversationsListFlat` | Same as List Conversations, but returns the channel array directly (no 'channels' envelope) — used to populate field-picker dropdowns without a 'channels.' prefix. |
| List Denied Admin Invite Requests | `listAdminInviteRequestsDeniedList` | List all denied workspace invite requests. |
| List Emoji | `listEmojiList` | List custom emoji for a team. BLOCKED (live 2026-06-05): HTTP 200 ok:false error="missing_scope", needed="emoji:read" not in bot token scopes. configHealthy:true (wired correctly). Provider account-state block — bot token lacks emoji:read. |
| List Files | `listFilesList` | List for a team, in a channel, or from a user with applied filters. |
| List Pinned Items | `listPinsList` | Lists items pinned to a channel. |
| List Reactions | `listReactionsList` | Lists reactions made by a user. |
| List Reminders | `listRemindersList` | Lists all reminders created by or for a given user. ⛔ VERIFIED-BLOCKED 2026-06-05: not_allowed_token_type — user-token-only. |
| List Remote Files | `listFilesRemoteList` | Lists remote files. VERIFY 2026-06-05: BLOCKED — ok:false error="missing_scope" needed="remote_files:read" (not granted to the bot token). configHealthy:true. |
| List Restricted Admin Apps | `listAdminAppsRestrictedList` | List restricted apps for an org or workspace. |
| List Scheduled Messages | `listChatScheduledMessagesList` | Returns a list of scheduled messages. |
| List Stars | `listStarsList` | Lists stars for a user. ⛔ VERIFIED-BLOCKED 2026-06-05: not_allowed_token_type — user-token-only. |
| List Team Access Logs | `listTeamAccessLogs` | Get the team access logs. BLOCKED (live 2026-06-05): HTTP 200 ok:false error="not_allowed_token_type" — requires admin/owner user token (paid plan); bot token not allowed. |
| List Team Integration Logs | `listTeamIntegrationLogs` | Get the team integration activity logs. BLOCKED (live 2026-06-05): HTTP 200 ok:false error="not_allowed_token_type" — requires admin/owner user token; bot token not allowed. |
| List User Conversations | `listUsersConversations` | List conversations the calling user may access. |
| List User Group Members | `listUsergroupsUsersList` | List users in a User Group. Live 2026-06-05 ok:true for usergroup=S093SALUWNA → users:[ids]. Query param 'usergroup' (required). Requires usergroups:read (present). |
| List User Groups | `listUsergroupsList` | List all User Groups for a team |
| List Users | `listUsersList` | Lists all users in a Slack team. |
| Lookup User By Email | `listUsersLookupByEmail` | Find a user with an email address. |
| Mark Conversation Read | `createConversationsMark` | Sets the read cursor in a channel. |
| Open Conversation | `createConversationsOpen` | Opens or resumes a direct message or multi-person direct message. |
| Open Dialog | `listDialogOpen` | Open a dialog with a user |
| Open View | `listViewsOpen` | Open a view for a user. |
| Pin Message | `createPinsAdd` | Pins an item to a channel. |
| Post Ephemeral Message | `createChatPostEphemeral` | Sends an ephemeral message to a user in a channel. |
| Post Message | `createChatPostMessage` | Sends a message to a channel. |
| Publish View | `listViewsPublish` | Publish a static view for a User. |
| Push View | `listViewsPush` | Push a view onto the stack of a root view. |
| Remove Admin Conversation Restrict Access Group | `createAdminConversationsRestrictAccessRemoveGroup` | Remove a linked IDP group linked from a private channel |
| Remove Admin Emoji | `createAdminEmojiRemove` | Remove an emoji across an Enterprise Grid organization |
| Remove Admin User | `createAdminUsersRemove` | Remove a user from a workspace. |
| Remove Admin Usergroup Channels | `createAdminUsergroupsRemoveChannel` | Remove one or more default channels from an org-level IDP group (user group). |
| Remove Call Participants | `createCallsParticipantsRemove` | Registers participants removed from a Call. ⛔ VERIFIED-BLOCKED 2026-06-05: missing_scope needed=calls:write (same). |
| Remove Pin | `createPinsRemove` | Un-pins an item from a channel. |
| Remove Reaction | `createReactionsRemove` | Removes a reaction from an item. |
| Remove Remote File | `createFilesRemoteRemove` | Removes a remote file. VERIFY 2026-06-05: BLOCKED — ok:false error="missing_scope" needed="remote_files:write" (not granted to the bot token). configHealthy:true. |
| Remove Star | `createStarsRemove` | Removes a star from an item. ⛔ VERIFIED-BLOCKED 2026-06-05: not_allowed_token_type — user-token-only. |
| Rename Admin Conversation | `createAdminConversationsRename` | Rename a public or private channel. |
| Rename Admin Emoji | `createAdminEmojiRename` | Rename an emoji. |
| Rename Conversation | `createConversationsRename` | Renames a conversation. |
| Request App Permissions | `listAppsPermissionsRequest` | [DEPRECATED] Retired by Slack. apps.permissions.request belonged to legacy workspace apps, which retired on 2021-08-24 (https://api.slack.com/legacy/workspace-apps, https://api.slack.com/permissions-api). Slack now answers ok:false / unknown_method. No replacement exists; use a modern Slack app with granular bot scopes. |
| Request App User Permissions | `listAppsPermissionsUsersRequest` | [DEPRECATED] Retired by Slack. apps.permissions.users.request belonged to legacy workspace apps, which retired on 2021-08-24 (https://api.slack.com/legacy/workspace-apps, https://api.slack.com/permissions-api). Slack now answers ok:false / unknown_method. No replacement exists; use a modern Slack app with granular bot scopes. |
| Reset Admin User Session | `createAdminUsersSessionReset` | Wipes all valid sessions on all devices for a given user |
| Restrict Admin App | `createAdminAppsRestrict` | Restrict an app for installation on a workspace. |
| Revoke Auth Token | `listAuthRevoke` | Revokes a token. |
| Revoke File Public URL | `createFilesRevokePublicUrl` | Disables public/external sharing for a file. VERIFY 2026-06-05: BLOCKED — ok:false error="not_allowed_token_type" (user-token-only method; connection holds a bot token xoxb). configHealthy:true. |
| Schedule Message | `createChatScheduleMessage` | Schedules a message to be sent to a channel. |
| Search Admin Conversations | `listAdminConversationsSearch` | Search for public or private channels in an Enterprise organization. |
| Search Messages | `listSearchMessages` | Searches for messages matching a query. |
| Send Me Message | `createChatMeMessage` | Share a me message into a channel. |
| Set Admin Conversation Preferences | `createAdminConversationsSetConversationPref` | Set the posting permissions for a public or private channel. |
| Set Admin Conversation Teams | `createAdminConversationsSetTeam` | Set the workspaces in an Enterprise grid org that connect to a public or private channel. |
| Set Admin Team Default Channels | `createAdminTeamsSettingsSetDefaultChannel` | Set the default channels of a workspace. |
| Set Admin Team Description | `createAdminTeamsSettingsSetDescription` | Set the description of a given workspace. |
| Set Admin Team Discoverability | `createAdminTeamsSettingsSetDiscoverability` | An API method that allows admins to set the discoverability of a given workspace |
| Set Admin Team Icon | `createAdminTeamsSettingsSetIcon` | Sets the icon of a workspace. |
| Set Admin Team Name | `createAdminTeamsSettingsSetName` | Set the name of a given workspace. |
| Set Admin User As Admin | `createAdminUsersSetAdmin` | Set an existing guest, regular user, or owner to be an admin user. |
| Set Admin User As Owner | `createAdminUsersSetOwner` | Set an existing guest, regular user, or admin user to be a workspace owner. |
| Set Admin User As Regular | `createAdminUsersSetRegular` | Set an existing guest user, admin user, or owner to be a regular user. |
| Set Admin User Expiration | `createAdminUsersSetExpiration` | Set an expiration for a guest user |
| Set Conversation Purpose | `createConversationsSetPurpose` | Sets the purpose for a conversation. |
| Set Conversation Topic | `createConversationsSetTopic` | Sets the topic for a conversation. |
| Set Do Not Disturb Snooze | `createDndSetSnooze` | Turn on Do Not Disturb mode for the current user for N minutes. BLOCKED (live 2026-06-05): dnd setters are user-token-only; bot token lacks dnd:write. Provider account-state block. ⛔ VERIFIED-BLOCKED 2026-06-05: not_allowed_token_type — user-token-only (dnd:write). |
| Set User Active (Deprecated) | `createUsersSetActive` | Mark the bot/user as active (legacy presence). Live 2026-06-05 ok:true (no params). Returns only {ok}. |
| Set User Photo | `createUsersSetPhoto` | Set a user's profile photo (multipart image upload). BLOCKED (live 2026-06-05): HTTP 200 ok:false error="not_allowed_token_type" — user-token-only (users.profile:write); bot token. configHealthy:true. |
| Set User Presence | `createUsersSetPresence` | Manually set the bot's presence. Live 2026-06-05 ok:true with presence=auto. Body field 'presence' (enum auto\|away), required. Returns {ok}. |
| Set User Profile | `createUsersProfileSet` | Set a user's profile fields. BLOCKED (live 2026-06-05): HTTP 200 ok:false error="not_allowed_token_type" — users.profile.set is user-token-only (users.profile:write); connection has a bot token. configHealthy:true. Sent {profile}. |
| Share File Public URL | `createFilesSharedPublicUrl` | Enables a file for public/external sharing. VERIFY 2026-06-05: BLOCKED — ok:false error="not_allowed_token_type" (user-token-only method; connection holds a bot token xoxb). configHealthy:true. |
| Share Remote File | `listFilesRemoteShare` | Shares a remote file into channels. VERIFY 2026-06-05: BLOCKED — ok:false error="missing_scope" needed="remote_files:share" (not granted to the bot token). configHealthy:true. |
| Test API | `listApiTest` | Check API calling code. Live 2026-06-05 ok:true: echoes back the args sent. No auth scope required. |
| Test Authentication | `listAuthTest` | Test auth and return identity of the bot/user. Live 2026-06-05 ok:true: returns url, team, user, team_id, user_id, bot_id, is_enterprise_install. Auth via Bearer header (auto-injected). |
| Unarchive Admin Conversation | `createAdminConversationsUnarchive` | Unarchive a public or private channel. |
| Unarchive Conversation | `createConversationsUnarchive` | Reverses conversation archival. |
| Unfurl Message Links | `createChatUnfurl` | Provide custom unfurl behavior for user-posted URLs |
| Uninstall App | `listAppsUninstall` | Uninstalls your app from a workspace. |
| Update Call | `createCallsUpdate` | Updates information about a Call. ⛔ VERIFIED-BLOCKED 2026-06-05: missing_scope needed=calls:write (same). |
| Update Message | `createChatUpdate` | Updates a message. |
| Update Remote File | `createFilesRemoteUpdate` | Updates an existing remote file. VERIFY 2026-06-05: BLOCKED — ok:false error="missing_scope" needed="remote_files:write" (not granted to the bot token). configHealthy:true. |
| Update User Group | `createUsergroupsUpdate` | Update an existing User Group. BLOCKED (live 2026-06-05): HTTP 200 ok:false error="permission_denied" — usergroups write requires paid plan/admin. configHealthy:true. Sent {usergroup, name}. |
| Update User Group Members | `createUsergroupsUsersUpdate` | Update the list of users in a User Group. BLOCKED (live 2026-06-05): HTTP 200 ok:false error="permission_denied" — usergroups write requires paid plan/admin. configHealthy:true. Sent {usergroup, users}. |
| Update View | `listViewsUpdate` | Update an existing view. |
| Update Workflow Step | `listWorkflowsUpdateStep` | [DEPRECATED] Retired by Slack. workflows.updateStep ceased functioning on 2024-09-26 with the Steps from Apps retirement (https://api.slack.com/legacy/workflows/steps/migration); Slack now answers ok:false / unknown_method. There is no direct replacement; use custom functions on the Slack automation platform. |
| Upload File | `createFilesUpload` | DEPRECATED - do not use. Wraps Slack's files.upload, which Slack deprecated and sunset on November 12, 2025; it now always returns ok:false, error "method_deprecated" (re-verified live 2026-09-12). Use the replacement flow instead: 1) Get Upload URL External (filename, length) returns upload_url and file_id; 2) POST the raw file bytes to upload_url; 3) Complete Upload External (files=[{id, title}], optional channel_id, thread_ts, initial_comment). Kept only so existing callers are not broken. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Added To User Group | `subteam_self_added` | You were added to a user group |
| App Home Opened | `app_home_opened` | A user clicked into your App Home |
| App Mention | `app_mention` | Your app or bot was directly mentioned in a message |
| App Uninstalled | `app_uninstalled` | Your Slack app was completely uninstalled from a workspace |
| Channel Archived | `channel_archive` | A public channel was archived |
| Channel Created | `channel_created` | A new channel was created in the workspace |
| Channel Deleted | `channel_deleted` | A channel was deleted from the workspace |
| Channel ID Changed | `channel_id_changed` | A channel ID changed (e.g. due to a workspace migration) |
| Channel Left | `channel_left` | You (the bot/authed user) left a public channel |
| Channel Renamed | `channel_rename` | A channel was renamed in the workspace |
| Channel Shared | `channel_shared` | A channel was shared with an external workspace (Slack Connect) |
| Channel Unarchived | `channel_unarchive` | A public channel was unarchived |
| Channel Unshared | `channel_unshared` | A channel is no longer shared with an external workspace |
| Direct Message | `message.im` | A message was posted in a direct message (IM) channel |
| DM Closed | `im_close` | You closed a direct message channel |
| DM Created | `im_created` | A direct message channel was created |
| DM Opened | `im_open` | You opened a direct message channel |
| Do Not Disturb Updated | `dnd_updated` | Do Not Disturb settings changed for the authed user |
| Do Not Disturb Updated (User) | `dnd_updated_user` | Do Not Disturb settings changed for a member |
| Emoji Changed | `emoji_changed` | A custom emoji was added, removed, or renamed in the workspace |
| File Changed | `file_change` | A file was changed |
| File Created | `file_created` | A file was uploaded/created in Slack |
| File Deleted | `file_deleted` | A file was deleted from the workspace |
| File Made Public | `file_public` | A file was made public |
| File Shared | `file_shared` | A file was shared with workspace members |
| File Unshared | `file_unshared` | A file was unshared |
| Link Shared | `link_shared` | A message was posted containing one or more links matching a registered URL domain (for link unfurling) |
| Member Joined Channel | `member_joined_channel` | A user joined a public channel, private channel, or MPDM |
| Member Left Channel | `member_left_channel` | A user left a public or private channel |
| Message (any conversation) | `message` | Any message event as Slack actually sends it (event.type = 'message'), in public channels, private channels, DMs and group DMs alike; event.channel_type tells them apart. The message.channels/groups/im/mpim entries are Slack's subscription names and never equal the payload's event.type, so a trigger on them cannot match until the ingest maps them; subscribe to this event and filter on channel_type in the workflow. |
| Message in App Home | `message.app_home` | A user sent a message to your Slack app via the App Home interface |
| Message in Private Channel | `message.groups` | A message was posted to a private channel (group) |
| Message in Public Channel | `message.channels` | A message was posted to a public channel |
| Message Metadata Posted | `message_metadata_posted` | A message containing metadata was posted in Slack |
| Multiparty Direct Message | `message.mpim` | A message was posted in a multiparty direct message (MPIM) channel |
| Pin Added | `pin_added` | A pin was added to a channel |
| Pin Removed | `pin_removed` | A pin was removed from a channel |
| Private Channel Archived | `group_archive` | A private channel was archived |
| Private Channel Deleted | `group_deleted` | A private channel was deleted |
| Private Channel Left | `group_left` | You left a private channel |
| Private Channel Opened | `group_open` | You opened a private channel |
| Private Channel Renamed | `group_rename` | A private channel was renamed |
| Private Channel Unarchived | `group_unarchive` | A private channel was unarchived |
| Reaction Added | `reaction_added` | A member added an emoji reaction to an item |
| Reaction Removed | `reaction_removed` | A member removed an emoji reaction from an item |
| Removed From User Group | `subteam_self_removed` | You were removed from a user group |
| Star Added | `star_added` | A star was added to an item by the authed user |
| Star Removed | `star_removed` | A star was removed from an item by the authed user |
| Team Domain Changed | `team_domain_change` | The workspace domain changed |
| Team Member Joined | `team_join` | A new member joined the workspace |
| Team Renamed | `team_rename` | The workspace name changed |
| Tokens Revoked | `tokens_revoked` | API tokens for your app were revoked (user uninstalled or revoked access) |
| User Changed | `user_change` | A workspace member's profile or data was updated |
| User Group Created | `subteam_created` | A user group (subteam) was created |
| User Group Members Changed | `subteam_members_changed` | The membership of an existing user group changed |
| User Group Updated | `subteam_updated` | An existing user group was updated |
| User Huddle Changed | `user_huddle_changed` | A user's huddle status changed |
| User Profile Changed | `user_profile_changed` | A user's profile changed |
| User Status Changed | `user_status_changed` | A user's status changed |
