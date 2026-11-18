---
description: "Kommunicate customer messaging and support chat platform."
hidden: true
---

# Kommunicate

Kommunicate customer messaging and support chat platform. Manage conversations (groups), messages, users/visitors, agents, teams, routing, analytics and app settings via the Kommunicate platform REST API at services.kommunicate.io.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [kommunicate.io](https://kommunicate.io) |
| **Authentication** | API key |
| **Actions** | 96 |
| **Events** | 1 |
| **Slug** | `kommunicate` |

## Use it

Add Kommunicate from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.kommunicate.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Or Deactivate User | `setUserActivation` | Deactivate or reactivate a chat user. A deactivated user can no longer start conversations. Do not call this against the account the API key authenticates as. |
| Add Conversation Member | `addConversationMember` | Add a user (agent, bot or visitor) as a member of an existing conversation. Returns AL-U-01 'user already exist' when the user is already a member. |
| Add Conversation Tags | `addConversationTags` | Attach one or more tags to a conversation. The request body is a top-level JSON array of tag objects, passed as a pre-stringified JSON string. Returns the conversation's full tag list after the change. |
| Add Team Members | `addTeamMembers` | Add one or more agents to a team so that conversations routed to the team can reach them. |
| Bulk Delete Custom Routing Rules | `bulkDeleteCustomRoutingRules` | Upload a CSV of custom routing rules to delete them in bulk. Returns 'Custom Routing file deletion initiated'. |
| Bulk Delete Users | `bulkDeleteUsers` | Permanently delete several chat users and their conversation data in one call. DANGEROUS: never pass the userId the API key authenticates as, or the account's only admin - the vendor provides no recovery. |
| Bulk Import Users | `bulkImportUsers` | Start an asynchronous bulk user import from a CSV payload. The first row is the header (userId,displayName,email). Returns 'Import user process initiated'. |
| Bulk Upsert Custom Routing Rules | `bulkUpsertCustomRoutingRules` | Upload a CSV of custom routing rules (key,value,teamId) to create or update them in bulk. Returns 'Custom Routing file Import initiated'. |
| Change Conversation Assignee | `changeConversationAssignee` | Reassign a conversation to a different agent. Set takeOverFromBot true to remove the AI agent from the chat at the same time, and sendNotifyMessage false to suppress the system message. |
| Change Conversation Assignee (v2) | `changeConversationAssigneeV2` | Reassign a conversation using the v2 assignee route, which additionally supports handing the conversation to a team rather than a named agent. |
| Change Conversation Status | `changeConversationStatus` | Open, close or mark a conversation as spam. status 0 = open, 1 = assigned, 2 = closed/resolved, 3 = spam. Set sendNotifyMessage false to change the status without posting a system message into the chat. |
| Change Status Of Multiple Conversations | `changeStatusOfMultipleConversations` | Bulk-change the status of many conversations at once. The body is a top-level JSON array of conversation ids, passed as a pre-stringified JSON string. Processing is asynchronous. |
| Change User Password | `changeUserPassword` | Change the acting user's chat password. DANGEROUS: run against the account this connector authenticates as, it invalidates the stored credential and locks the connection out. |
| Count Messages | `countMessages` | Return the number of messages in a conversation or one-to-one thread without fetching their content. |
| Create Conversation | `createConversation` | Create a support conversation with a named member list. Pass metadata.SKIP_ROUTING 'true' to bypass routing rules and metadata.CONVERSATION_ASSIGNEE to pin an agent. Returns the new conversation id. |
| Create Conversation (v2) | `createConversationV2` | Create a support conversation through the v2 conversation route. The AI agent (bot) is made admin of the resulting conversation. |
| Create Conversation Thread | `createConversationThread` | Create a conversation through the /conversation/create route, an alternative entry point that returns the same group feed. groupName must not be blank. |
| Create Group | `createGroup` | Create a plain chat group (not routed through support conversation rules) with an explicit member list. Returns the new group feed. |
| Create Group (v2) | `createGroupV2` | Create a group using the v2 route, which supports per-member roles and returns the group feed with member user keys. Note: when groupName is omitted the vendor names the group after the admin user. |
| Create Team | `createTeam` | Create an agent team with an optional initial member list and routing mode. Returns the new teamId. |
| Delete All User Data | `deleteAllUserData` | Erase one or more users and all of their conversation data for GDPR right-to-erasure requests. The body is a top-level JSON array of userIds passed as a pre-stringified JSON string. DANGEROUS and irreversible: never include the userId the API key authenticates as, or the account's only admin. |
| Delete Conversation | `deleteConversation` | Permanently delete a conversation and its message history. Destructive and not reversible - confirm the groupId before calling. |
| Delete Message | `deleteMessage` | Delete a single message by its message key. Requires Accept text/plain; returns the bare string 'success'. Destructive and not reversible. |
| Delete Message (v2) | `deleteMessageV2` | Delete a single message by key using the v2 route, which returns the standard status/response envelope instead of a bare string. |
| Delete Team | `deleteTeam` | Delete an agent team by id. Conversations previously routed to the team fall back to default routing. Does not delete the agent accounts. |
| Email Conversation Transcript | `emailConversationTranscript` | Email the full transcript of a conversation to one or more addresses. WARNING: this sends a real email containing real conversation content. The vendor requires groupId and a tos LIST. |
| Filter Messages By Application | `filterMessagesByApplication` | Return messages across the whole application in a time window, for reporting and export. appKey is the Applozic application key from Get Application Settings, not the Kommunicate APP_ID. |
| Filter Users | `filterUsers` | List/filter the application's users (agents, bots and visitors) with paging. Returns userId, displayName, connection state, role and last-seen time. |
| Filter Users (v2) | `filterUsersV2` | List/filter application users using the v2 envelope, which wraps the user array in a status/generatedAt response object. |
| Filter Users (v3 Contact List) | `filterUsersV3` | Contact-list endpoint used by the Kommunicate dashboard: filter users by role with paging and return the full contact record set. |
| Get Agent Activity Analytics | `getAgentActivityAnalytics` | Return per-agent activity analytics (online/away time and handled conversation volume) for an application over a time range. |
| Get Agent Scoreboard | `getAgentScoreboard` | Return the per-agent conversation scoreboard (conversation counts and load) used for routing decisions. |
| Get App Module | `getAppModule` | Fetch an application module (push-notification profile) by its numeric appModuleId. |
| Get Application Settings | `getApplicationSettings` | Fetch the full application record: name, plan, MAU limits, webhook slots, app modules and website URL. SECURITY: the vendor also returns this account's own apiKey and secretKey in the response body - treat the output as a secret and do not log or forward it. |
| Get Application Statistics | `getApplicationStatistics` | Return message/conversation volume statistics for the application over a time range. appKey is the Applozic application key returned by Get Application Settings as 'key', NOT the Kommunicate APP_ID - passing the APP_ID returns a 200 carrying the string UNAUTHORIZED_ACCESS. |
| Get Attachment Download URL | `getAttachmentDownloadUrl` | Exchange an attachment blobKey for a time-limited presigned S3 download URL. Returns the URL as bare text. |
| Get Average Agent Response Time | `getAverageAgentResponseTime` | Return the average first-response time per agent over a date range. The request body is a top-level JSON array of agent userIds, passed as a pre-stringified JSON string. |
| Get Bot Time Saved | `getBotTimeSaved` | Return the number of agent-hours saved by bot automation for the application over a date range. |
| Get Conversation Info | `getConversationInfo` | Fetch a single conversation (group) by groupId or clientGroupId, returning members, admin, metadata, status and conversation assignee. |
| Get Conversation Info (v2) | `getConversationInfoV2` | Fetch one conversation using the v2 payload, which returns memberUserKeys and the conversation part metadata alongside the group feed. |
| Get Conversation Overview | `getConversationOverview` | Return aggregate conversation counters for the application: new, open, old, unanswered, closed and total conversation volumes. |
| Get Conversation Statistics | `getConversationStatistics` | Return conversation performance statistics for the application: average response time, average resolution time, unanswered and closed conversation series. |
| Get Custom Routing Rules | `getCustomRoutingRules` | Return the custom conversation-routing rules configured for the application (conditions that map incoming chats to teams or agents). |
| Get Filtered Statistics | `getFilteredStatistics` | Return the application's statistics series filtered to an explicit time window. appKey is the Applozic application key from Get Application Settings, not the Kommunicate APP_ID. |
| Get Monthly Tracked Users | `getMonthlyTrackedUsers` | Return the account's MTU billing counters: monthly tracked users, channel count and message count. |
| Get Multiple Conversations Info | `getConversationsInfoBulk` | Fetch several conversations in one call by passing a comma-separated list of groupIds. Returns an array of group feeds. |
| Get Service Health | `getServiceHealth` | Health probe for the Kommunicate platform service. Returns the plain text 'platform service is up and running' when the API host is reachable. |
| Get Team | `getTeam` | Fetch a single agent team by teamId, including its routing mode, default assignee and working-hours configuration. |
| Get Team Business Settings | `getTeamBusinessSettings` | Retrieve the business-hours and availability settings that apply to the application's agent teams. |
| Get User Data Export | `getUserDataExport` | Request the GDPR-style data export for one user of the application, identified by email. |
| Get User Details | `getUserDetails` | Fetch detailed profile information for one or more Kommunicate users/visitors by userId, including connection status, last seen time and metadata. Returns EMPTY_LIST when none of the supplied ids exist. |
| Get User Details (v1) | `getUserDetailsV1` | Fetch user profiles by userId using the v1 detail route, which returns a bare array rather than the status/response envelope. |
| Leave Conversation | `leaveConversation` | Remove the acting user (Of-User-Id) from a conversation's member list. Use Add Conversation Member to rejoin. |
| List Analytics Reports | `listAnalyticsReports` | List the Metabase-backed analytics report resources available to this account for embedding in the dashboard. |
| List Conversation Threads | `listConversationThreads` | List conversation threads for the acting agent, returning group feeds with topic and assignee metadata. NOTE: the vendor ignores groupId/startIndex/pageSize on this route and always returns the full list - page client-side. |
| List Conversation Threads (v2) | `listConversationThreadsV2` | List conversation threads using the v2 payload with member user keys. NOTE: the vendor ignores groupId/startIndex/pageSize on this route and always returns the full list - page client-side. |
| List Conversations | `listConversations` | List the conversations (groups) the acting agent is a member of, newest first. |
| List Conversations (v2) | `listConversationsV2` | List the acting agent's conversations using the v2 group payload with member keys and conversation metadata. |
| List Messages | `listMessages` | Fetch the message history of a conversation (or of a one-to-one thread) with optional time-range and paging. WARNING: message bodies are real customer conversation content. |
| List Messages (v2) | `listMessagesV2` | Fetch conversation message history using the v2 envelope (status/generatedAt wrapper around the message array). |
| List Messages (v3) | `listMessagesV3` | Fetch conversation message history using the v3 payload, which returns the flat message/userDetails/groupFeeds structure with conversation proxies. |
| List Open Channels | `listOpenChannels` | List the application's open (public) channels, which any user can join without being added as a member. |
| List Teams | `listTeams` | List all agent teams configured on the Kommunicate application, including teamId, teamName, routing mode and working hours. |
| List Teams (v2) | `listTeamsV2` | List agent teams using the v2 payload, which additionally returns agentRoutingDefault and per-team teammate configuration. |
| List User Application Roles | `listUserApplicationRoles` | Return the Kommunicate applications a given userId belongs to, keyed by applicationId, for the requested roles. |
| List User Roles By Application | `listUserRolesByApplication` | Return a user's roles grouped by role name (APPLICATION_WEB_ADMIN, APPLICATION_ADMIN) with the applications held under each. |
| List Waiting Queue | `listWaitingQueue` | List conversations currently sitting in the routing waiting queue, optionally scoped to one team. |
| Mark Message Read | `markMessageRead` | Mark one message as read for the acting user by its message key. Requires Accept text/plain; the endpoint returns the bare string 'success'. |
| Mute User Notifications | `muteUserNotifications` | Mute chat notifications for a user until a given timestamp. NOTE: on the Kommunicate deployment of this API the endpoint answers 500 AL-I-01 for every documented request shape - treat it as a vendor-side defect. |
| Reassign Waiting Queue | `reassignWaitingQueue` | Trigger a re-run of routing for conversations stuck in the waiting queue, pushing them to available agents. Side-effecting: it reassigns real conversations when the queue is non-empty. |
| Register Chat User | `registerChatUser` | Register (create) a chat user or visitor for the application. SECURITY: the response contains a live authToken (JWT session for that user, ~12h) and a userEncryptionKey - treat the output as a secret, do not log or forward it. |
| Register Chat User (v2) | `registerChatUserV2` | Register a chat user through the v2 route, wrapped in the standard status/response envelope. SECURITY: the response contains a live authToken (JWT session for that user, ~12h) and a userEncryptionKey - treat the output as a secret, do not log or forward it. |
| Remove Conversation Member | `removeConversationMember` | Remove a user from a conversation's member list. The user keeps read access to prior history only if re-added. |
| Remove Conversation Tags | `removeConversationTags` | Detach one or more tags from a conversation. The request body is a top-level JSON array of tag objects passed as a pre-stringified JSON string. Returns the remaining tag list. |
| Remove Team Members | `removeTeamMembers` | Remove one or more agents from a team. This changes only team membership; it does not deactivate or delete the agent account. Returns 'removed' on success. |
| Remove User From Conversation | `removeUserFromConversation` | Remove a named user from a conversation using the group/user/remove route. Returns 'user or userId not exist' when the user is not a member. |
| Search Contacts | `searchContacts` | Search the application's contacts/users by name or email fragment. Returns totalUserCount and matching user detail records. |
| Search Support Conversations | `searchSupportConversations` | Dashboard conversation search: filter support conversations by status, assignee, team and free-text query, with paging. Returns matching group feeds and a conversationCount. |
| Send Campaign Message | `sendCampaignMessage` | Broadcast a campaign message to a list of users. WARNING: this delivers to many real people at once and cannot be recalled. |
| Send Conversation Message | `sendConversationMessage` | Create a conversation and post its first message in one call. WARNING: this delivers to a real person in a live chat. groupName must not be blank. |
| Send Email | `sendEmail` | Send a transactional email through Kommunicate's mail service. WARNING: this delivers a real email to real recipients. The vendor requires from, tos (a LIST of addresses), subject and body. |
| Send Message | `sendMessage` | Post a message into a conversation as a named sender. WARNING: this delivers to a real person in a live chat. Supports attachments via fileMeta and rich message payloads via metadata.contentType. |
| Send Message (v2) | `sendMessageV2` | Post a message into a conversation using the v2 send route, which accepts fromUserName and rich-message metadata. WARNING: this delivers to a real person in a live chat. |
| Sync All Conversations | `syncAllConversations` | Bulk sync endpoint returning every conversation feed plus its latest message for the acting agent, optionally only those updated since a timestamp. |
| Sync User Presence | `syncUserPresence` | Report the acting user's last-seen timestamp and receive the v2 presence delta: online users, changed groups, registered devices and total unread count. |
| Update App Module | `updateAppModule` | Update an application module (push-notification profile) name or description. Returns the stored module record. |
| Update Application Settings | `updateApplicationSettings` | Update the application record (name, website URL, MAU expectations, webhook slots). Send the full application object; omitted fields keep their stored value. SECURITY: the response echoes this account's own apiKey and secretKey. |
| Update Application Settings (v2) | `updateApplicationSettingsV2` | Update the application record through the v2 edit route used by the Kommunicate dashboard, including the webhook URL slots in applicationWebhookPxys. SECURITY: the response echoes this account's own apiKey and secretKey. |
| Update Chat User | `updateChatUser` | Update a chat user's profile through the v2 route, which also accepts role and phone-number changes. The target user is named in the Of-User-Id header. |
| Update Conversation | `updateConversation` | Rename a conversation or change its image and metadata. Send only the fields you intend to change. |
| Update Conversation Topic | `updateConversationTopic` | Update a conversation's topic id and topic detail through the /conversation/update route. All of id, groupId, topicId, topicDetail, userId and groupName must be supplied or the vendor answers AL-AE-01. |
| Update Team | `updateTeam` | Update an agent team's name, routing mode or default assignee. Returns 'updated' on success. |
| Update User Last Seen | `updateUserLastSeen` | Report the acting user's last-seen timestamp and receive the presence delta since then (online users, updated groups, devices). |
| Update User Profile | `updateUserProfile` | Update the profile of the user named in the Of-User-Id header: display name, email, image link and custom metadata shown to agents in the visitor sidebar. |
| Upload Attachment | `uploadAttachment` | Upload a text-based file (CSV, TXT, SVG, ASCII PPM) to Kommunicate storage and receive its blobKey and S3 url for use as a message attachment. Binary formats such as PNG or ZIP are not supported by this transport. |
| Upload Push Certificate | `uploadPushCertificate` | Upload the APNS push certificate for an app module. The vendor expects a binary .p12 part, which the connector transport cannot carry without corruption - use the Kommunicate dashboard for this upload. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Message Received | `message` | Fires for every chat message sent in any conversation of the application. Kommunicate has exactly one webhook event type. payloadSchema is MODELLED from the vendor's documented sample at docs.kommunicate.io/docs/webhooks-configuration - it was not captured from a real delivery, because capturing one requires posting a chat message and that reaches real people. |
