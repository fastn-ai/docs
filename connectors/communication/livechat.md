---
description: "LiveChat (Text) API v3.6."
hidden: true
---

# LiveChat

LiveChat (Text) API v3.6. Manage agents, bots, groups, tags, greetings, auto access rules, customer bans, properties and webhooks via the Configuration API; work with chats, threads, events, transfers, customers and routing statuses via the Agent Chat API; and pull chat, agent, customer and tag analytics from the Reports API.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [livechat.com](https://livechat.com) |
| **Authentication** | Basic auth |
| **Actions** | 124 |
| **Events** | 0 |
| **Slug** | `livechat` |

## Use it

Add LiveChat from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.livechat.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Auto Access Rule | `addAutoAccess` | Creates an auto access rule that assigns groups to a chat based on the customer's page URL and geolocation. |
| Add User to Chat | `addUserToChat` | Adds an agent or a customer to an active chat. A chat can hold only one customer, who must be added with visibility all. |
| Approve Agent | `approveAgent` | Approves an agent who is awaiting approval, allowing them to use the application. |
| Approve Agents (Batch) | `batchApproveAgents` | Approves several agents in one request. Each entry takes the same payload as Approve Agent. |
| Ban Customer | `banCustomer` | Bans a customer for a number of days, immediately disconnecting their active sessions. |
| Check Product Limits for Plan | `checkProductLimitsForPlan` | Compares the organization's current resource usage against a subscription plan and returns the resources that exceed that plan's limits. |
| Create Agent | `createAgent` | Creates a new agent within the license. |
| Create Agents (Batch) | `batchCreateAgents` | Creates several agents in one request. Each entry takes the same payload as Create Agent. |
| Create Bot | `createBot` | Creates a new bot agent on the license. Use Set Routing Status afterwards to make it available for chats. |
| Create Bot Template | `createBotTemplate` | Creates a bot template for an application. A bot based on the template is created automatically on every license that installs the application. One Client ID can hold up to five templates. |
| Create Bots (Batch) | `batchCreateBots` | Creates several bot agents in one request. Each entry takes the same payload as Create Bot. |
| Create Greeting | `createGreeting` | Creates a greeting campaign that is shown to customers when its rules match. |
| Create Group | `createGroup` | Creates a new group of agents. |
| Create Tag | `createTag` | Creates a chat tag. Matching an existing tag name is case insensitive. |
| Deactivate Chat | `deactivateChat` | Closes the chat's active thread so no more messages can be sent to it. |
| Delete Agent | `deleteAgent` | Deletes an agent from the license. |
| Delete Agents (Batch) | `batchDeleteAgents` | Deletes several agents in one request. Each entry takes the same payload as Delete Agent. |
| Delete Auto Access Rule | `deleteAutoAccess` | Deletes an auto access rule. |
| Delete Bot | `deleteBot` | Deletes a bot agent from the license. |
| Delete Bot Template | `deleteBotTemplate` | Deletes a bot template. The bots created from it are removed only when affect_existing_installations is true. |
| Delete Bots (Batch) | `batchDeleteBots` | Deletes several bot agents in one request. Each entry takes the same payload as Delete Bot. |
| Delete Chat Properties | `deleteChatProperties` | Deletes property values from a chat. |
| Delete Event Properties | `deleteEventProperties` | Deletes property values from an event. |
| Delete Greeting | `deleteGreeting` | Deletes a greeting. |
| Delete Group | `deleteGroup` | Deletes a group. |
| Delete Group Properties | `deleteGroupProperties` | Deletes property values from a group. |
| Delete License Properties | `deleteLicenseProperties` | Deletes property values from the license. |
| Delete Tag | `deleteTag` | Deletes a chat tag. The tag name is matched case sensitively. |
| Delete Thread Properties | `deleteThreadProperties` | Deletes property values from a thread. |
| Disable License Webhooks | `disableLicenseWebhooks` | Disables webhooks on the license. They stay disabled even after the application is reinstalled. |
| Enable License Webhooks | `enableLicenseWebhooks` | Re-enables webhooks that were disabled on the license. |
| Follow Chat | `followChat` | Follows a chat so the requester receives all of its updates until the chat is reactivated or unfollowed. |
| Get Agent | `getAgent` | Returns the details of a single agent. |
| Get Bot | `getBot` | Returns the details of a single bot agent. |
| Get Chat | `getChat` | Returns a chat together with one of its threads. |
| Get Customer | `getCustomer` | Returns the details of a customer, including their statistics, most recent visit and chat IDs. |
| Get Greeting | `getGreeting` | Returns the details of a single greeting. |
| Get Group | `getGroup` | Returns the details of a single group. |
| Get License Webhooks State | `getLicenseWebhooksState` | Returns whether an application's webhooks are currently enabled on the license. |
| Get Product Source | `getProductSource` | Returns the source parameters recorded when the LiveChat product was activated. |
| Issue Bot Token | `issueBotToken` | Issues a 24-hour access token for a bot. The token carries the chats--access:rw, agents-bot--my:rw and customers:rw scopes and cannot be revoked. |
| List Agents | `listAgents` | Returns all agents within the LiveChat license, optionally filtered by group or suspension state. |
| List Agents for Transfer | `listAgentsForTransfer` | Returns the agents a chat can be transferred to, sorted by how many active chats they have. Offline agents are not returned. |
| List Archives | `listArchives` | Searches archived chats. Each result pairs one chat with one of its threads, so the same chat can appear more than once. |
| List Auto Access Rules | `listAutoAccesses` | Returns all auto access rules configured on the license, in evaluation order. |
| List Bot Templates | `listBotTemplates` | Returns the bot templates registered for an application. |
| List Bots | `listBots` | Returns the bot agents created on the license. |
| List Channels | `listChannels` | Returns a summary of the communication channels used on the LiveChat license. |
| List Chats | `listChats` | Returns summaries of the chats the authorized agent has access to. |
| List Customer Bans | `listCustomerBans` | Returns every active customer ban on the license. |
| List Greetings | `listGreetings` | Returns the greetings configured on the license. |
| List Group Properties | `listGroupsProperties` | Returns the property values set on the given groups. |
| List Groups | `listGroups` | Returns every group on the license. |
| List License Properties | `listLicenseProperties` | Returns the property values set on the license, falling back to each property's default value. |
| List Properties | `listProperties` | Returns the private and public properties owned by an application. |
| List Routing Statuses | `listRoutingStatuses` | Returns the current routing status of every agent matching the filters. |
| List Tags | `listTags` | Returns the chat tags configured on the license. |
| List Threads | `listThreads` | Returns the threads of a chat that the authorized agent has access to. |
| List Webhook Names | `listWebhookNames` | Returns every webhook action supported by an API version, together with the filters each one accepts. |
| List Webhooks | `listWebhooks` | Returns the webhooks registered for an application. |
| Mark Events as Seen | `markEventsAsSeen` | Marks the chat's events up to a given time as seen by the requester. |
| Multicast | `multicast` | Sends a chat-unrelated message to selected agents. Multicast messages are not stored. |
| Publish Property | `publishProperty` | Publishes a private property so any application can access it. Publishing cannot be undone. |
| Reactivate Email | `reactivateEmail` | Reactivates an agent's email address after it has bounced. |
| Register Property | `registerProperty` | Registers a new private property for an application. |
| Register Webhook | `registerWebhook` | Registers a webhook for an application. One Client ID can register up to three webhooks per action. |
| Remove User from Chat | `removeUserFromChat` | Removes an agent from a chat. The customer cannot be removed. |
| Report: Agent Availability | `reportAgentAvailability` | Returns how long each agent was available to accept chats. |
| Report: Agent Performance | `reportAgentPerformance` | Returns each agent's chat performance metrics. |
| Report: Chat Duration | `reportChatDuration` | Returns the average chat duration of agents within the license. |
| Report: Chat Engagement | `reportChatEngagement` | Returns how chats were started, split by engagement type. |
| Report: Chat First Response Time | `reportChatFirstResponseTime` | Returns the average time it took agents to send their first response. |
| Report: Chat Forms | `reportChatForms` | Returns how many pre-chat and post-chat surveys were filled in. |
| Report: Chat Ranking | `reportChatRanking` | Returns the chat satisfaction ranking, calculated from good and bad ratings. |
| Report: Chat Ratings | `reportChatRatings` | Returns how customers rated chats, split into good, bad and unrated. |
| Report: Chat Response Time | `reportChatResponseTime` | Returns the average agent response time in chats. |
| Report: Chat Tags | `reportChatTags` | Returns how many chats were marked with each tag. |
| Report: Chats by Group | `reportChatsByGroup` | Returns how chats were distributed across groups. |
| Report: Greetings Conversion | `reportGreetingsConversion` | Returns how many greetings were displayed, accepted, closed and ignored. |
| Report: Queued Visitors | `reportQueuedVisitors` | Returns how many visitors waited in the chat queue and how long they waited. |
| Report: Queued Visitors Left | `reportQueuedVisitorsLeft` | Returns how many visitors left the chat queue before being served. |
| Report: Tag Chat Usage | `reportTagChatUsage` | Returns how often each tag was used on chats. |
| Report: Total Chats | `reportTotalChats` | Returns the total number of chats in the reporting range. |
| Report: Unique Visitors | `reportUniqueVisitors` | Returns how many unique visitors viewed the website. |
| Request Agent Unsuspension | `requestAgentUnsuspension` | Sends an unsuspension request from the currently suspended agent to the license owners and vice owners. |
| Request Thread Summary | `requestThreadSummary` | Requests an AI-generated summary of a thread. The summary is delivered as a system event inside the thread. A deactivated thread can be summarized only once. |
| Reset Bot Secret | `resetBotSecret` | Generates a new secret for a bot agent. |
| Reset Bot Template Secret | `resetBotTemplateSecret` | Generates a new secret for a bot template. |
| Resume Chat | `resumeChat` | Restarts an archived chat by opening a new thread on it. |
| Send Event | `sendEvent` | Sends an event, such as a message, to a chat. The author must already be a user of the chat. |
| Send Event Preview | `sendEventPreview` | Sends a message preview that is not stored in the chat. Use it to stream a partial response before sending the final message. |
| Send Rich Message Postback | `sendRichMessagePostback` | Sends a postback for a rich message button. |
| Send Thinking Indicator | `sendThinkingIndicator` | Shows a thinking indicator in a chat, for example while a bot prepares an answer. |
| Send Typing Indicator | `sendTypingIndicator` | Shows or hides the typing indicator in a chat. |
| Set Routing Status | `setRoutingStatus` | Changes the routing status of an agent or a bot agent. |
| Start Chat | `startChat` | Starts a new chat. Every author of the initial events other than the requester must be listed in the chat users. |
| Suspend Agent | `suspendAgent` | Suspends an agent, blocking their access to the application. |
| Suspend Agents (Batch) | `batchSuspendAgents` | Suspends several agents in one request. Each entry takes the same payload as Suspend Agent. |
| Tag Thread | `tagThread` | Adds a tag to a thread. The tag must already exist and share at least one group with the thread. |
| Transfer Chat | `transferChat` | Transfers an active chat to another agent or group. |
| Unban Customer | `unbanCustomer` | Lifts a ban from a customer. Provide exactly one of IP address or customer ID. |
| Unfollow Chat | `unfollowChat` | Removes the requester from the chat followers. Chat members cannot unfollow their own chats. |
| Unregister Property | `unregisterProperty` | Unregisters a private property. Published properties cannot be unregistered. |
| Unregister Webhook | `unregisterWebhook` | Unregisters a previously registered webhook. |
| Unsuspend Agent | `unsuspendAgent` | Lifts the suspension from an agent. |
| Unsuspend Agents (Batch) | `batchUnsuspendAgents` | Unsuspends several agents in one request. Each entry takes the same payload as Unsuspend Agent. |
| Untag Thread | `untagThread` | Removes a tag from a thread. |
| Update Agent | `updateAgent` | Updates the properties of an existing agent. Only the fields you send are changed. |
| Update Agents (Batch) | `batchUpdateAgents` | Updates several agents in one request. Each entry takes the same payload as Update Agent. |
| Update Auto Access Rule | `updateAutoAccess` | Updates an auto access rule. Only the fields you send are overwritten. Sending next_id also reorders the rule. |
| Update Bot | `updateBot` | Updates an existing bot agent. |
| Update Bot Template | `updateBotTemplate` | Updates an existing bot template. |
| Update Bots (Batch) | `batchUpdateBots` | Updates several bot agents in one request. Each entry takes the same payload as Update Bot. |
| Update Chat Properties | `updateChatProperties` | Sets property values on a chat. |
| Update Company Details | `updateCompanyDetails` | Updates the company details stored on the license. |
| Update Customer | `updateCustomer` | Updates a customer's details. Besides the ID, at least one other field must be sent. |
| Update Event Properties | `updateEventProperties` | Sets property values on an event. |
| Update Greeting | `updateGreeting` | Updates an existing greeting. Only the fields you send are changed. |
| Update Group | `updateGroup` | Updates an existing group. Only the fields you send are changed. |
| Update Group Properties | `updateGroupProperties` | Sets property values on a group. Existing values that you do not send are left untouched. |
| Update License Properties | `updateLicenseProperties` | Sets property values on the license. Existing values that you do not send are left untouched. |
| Update Tag | `updateTag` | Updates the groups a chat tag is assigned to. The tag name is matched case sensitively. |
| Update Thread Properties | `updateThreadProperties` | Sets property values on a thread. |
| Upload File | `uploadFile` | Uploads a file and returns a temporary URL valid for 24 hours. The URL becomes permanent once it is used in a file event sent with Send Event. Maximum size 10MB; executable files are rejected. |
