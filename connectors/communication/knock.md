---
description: "Knock notification infrastructure API."
hidden: true
---

# Knock

Knock notification infrastructure API. Covers recipients (users and custom objects), channel data, preference sets and per-category, per-channel-type and per-workflow preferences, in-app feeds and feed settings, guides, messages and their content, activities, events and delivery logs, message engagement status changes in single and batch form, subscriptions and audiences, tenants, schedules, workflow triggers and cancellations, workflow recipient runs, bulk operations, Slack and Microsoft Teams provider endpoints, and the Census and Hightouch reverse-ETL integration endpoints. Authenticates with a Knock environment secret key sent as an Authorization Bearer token; keys are scoped to a single Knock environment.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [knock.app](https://knock.app) |
| **Authentication** | Credentials you enter |
| **Actions** | 118 |
| **Events** | 0 |
| **Slug** | `knock` |

## Use it

Add Knock from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.knock.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Audience Members | `addAudienceMembers` | Adds one or more members to the specified audience. |
| Add Subscriptions For Object | `addSubscriptionsForObject` | Add subscriptions for an object. If a subscription already exists, it will be updated. This endpoint also handles inline identifications for the recipient. |
| Archive Message | `archiveMessage` | Archives a message for the user. Archived messages are hidden from the default message list in the feed but can still be accessed and unarchived later. |
| Batch Get Message Contents | `batchGetMessageContents` | Get the contents of multiple messages in a single request. |
| Batch Mark Messages As Archived | `batchMarkMessagesAsArchived` | Marks the given messages as archived. Archived messages are hidden from the default message list in the feed but can still be accessed and unarchived later. |
| Batch Mark Messages As Interacted | `batchMarkMessagesAsInteracted` | Marks the given messages as interacted with by the user. This can include any user action on the message, with optional metadata about the specific interaction. Cannot include more than 5 key-value pairs, must not contain nested data. Read more about message engagement statuses here. |
| Batch Mark Messages As Read | `batchMarkMessagesAsRead` | Marks the given messages as read. Read more about message engagement statuses here. |
| Batch Mark Messages As Seen | `batchMarkMessagesAsSeen` | Marks the given messages as seen. This indicates that the user has viewed the message in their feed or inbox. Read more about message engagement statuses here. |
| Batch Mark Messages As Unarchived | `batchMarkMessagesAsUnarchived` | Marks the given messages as unarchived. This reverses the archived state. Archived messages are hidden from the default message list in the feed but can still be accessed and unarchived later. |
| Batch Mark Messages As Unread | `batchMarkMessagesAsUnread` | Marks the given messages as unread. This reverses the read state. Read more about message engagement statuses here. |
| Batch Mark Messages As Unseen | `batchMarkMessagesAsUnseen` | Marks the given messages as unseen. This reverses the seen state. Read more about message engagement statuses here. |
| Bulk Add Subscriptions | `bulkAddSubscriptions` | Add subscriptions for all objects in a single collection. If a subscription for an object in the collection already exists, it will be updated. This endpoint also handles inline identifications for the recipient field. |
| Bulk Create Schedules | `bulkCreateSchedules` | Bulk creates up to 1,000 schedules at a time. This endpoint also handles inline identifications for the actor, recipient, and tenant fields. |
| Bulk Delete Objects | `bulkDeleteObjects` | Bulk deletes objects from the specified collection. |
| Bulk Delete Subscriptions | `bulkDeleteSubscriptions` | Delete subscriptions for many objects in a single collection type. If a subscription for an object in the collection doesn't exist, it will be skipped. |
| Bulk Delete Tenants | `bulkDeleteTenants` | Delete up to 1,000 tenants at a time in a single operation. This operation cannot be undone. |
| Bulk Delete Users | `bulkDeleteUsers` | Permanently deletes up to 1,000 users at a time. |
| Bulk Identify Users | `bulkIdentifyUsers` | Identifies multiple users in a single operation. Allows creating or updating up to 1,000 users in a single batch with various properties, preferences, and channel data. |
| Bulk Set Objects | `bulkSetObjects` | Bulk sets up to 1,000 objects at a time in the specified collection. |
| Bulk Set Tenants | `bulkSetTenants` | Set or update up to 1,000 tenants in a single operation. |
| Bulk Set User Preferences | `bulkSetUserPreferences` | Bulk sets the preferences for up to 1,000 users at a time. The preference set :id can be either default or a tenant.id. Learn more about per-tenant preferences. Note that this is a destructive operation and will replace any existing users' preferences with the preferences sent. |
| Bulk Update Messages For Channel | `bulkUpdateMessagesForChannel` | Bulk update the status of messages for a specific channel. The channel is specified by the channel_id parameter. The action to perform is specified by the action parameter, where the action is a status change action (e.g. archive, unarchive). |
| Cancel Workflow | `cancelWorkflow` | When invoked for a workflow using a specific workflow key and cancellation key, will cancel any queued workflow runs associated with that key/cancellation key pair. Can optionally be provided one or more recipients to scope the request to. |
| Cancel Workflow Via Notify Endpoint | `cancelWorkflowViaNotify` | Cancels a previously triggered workflow using the provided cancellation key. |
| Create Schedules | `createSchedules` | Creates one or more schedules for a workflow with the specified recipients, timing, and data. Schedules can be one-time or recurring. This endpoint also handles inline identifications for the actor, recipient, and tenant fields. |
| Delete Object | `deleteObject` | Permanently removes an object from the specified collection. This operation cannot be undone. |
| Delete Object Preference Set | `deleteObjectPreferenceSet` | Unsets the preference set for the object, removing it entirely. |
| Delete Schedules | `deleteSchedules` | Permanently deletes one or more schedules identified by the provided schedule IDs. This operation cannot be undone. |
| Delete Subscriptions For Object | `deleteSubscriptionsForObject` | Delete subscriptions for the specified recipients from an object. Returns the list of deleted subscriptions. |
| Delete Tenant | `deleteTenant` | Delete a tenant and all associated data. This operation cannot be undone. |
| Delete User | `deleteUser` | Permanently delete a user and all associated data. |
| Delete User Preference Set | `deleteUserPreferenceSet` | Unsets the preference set for the user, removing it entirely. |
| Generate Preference Center Signed URL | `generatePreferenceCenterSignedUrl` | Generates a signed preference center URL and token for the given user in the current environment. |
| Get Bulk Operation | `getBulkOperation` | Retrieves a bulk operation (if it exists) and displays the current state of it. |
| Get Message | `getMessage` | Retrieves a specific message by its ID. |
| Get Message Contents | `getMessageContents` | Returns the fully rendered contents of a message, where the response depends on which channel the message was sent through. |
| Get Object | `getObject` | Retrieves a specific object by its ID from the specified collection. Returns the object with all its properties. |
| Get Object Channel Data | `getObjectChannelData` | Returns the channel data for the specified object and channel. |
| Get Object Preference Set | `getObjectPreferenceSet` | Returns the preference set for the specified object and preference set id. |
| Get Preference Center Config | `getPreferenceCenterConfig` | Returns the preference center config with environment metadata for the given user. |
| Get Tenant | `getTenant` | Get a tenant by ID. |
| Get User | `getUser` | Retrieve a specific user by their ID. |
| Get User Channel Data | `getUserChannelData` | Retrieves the channel data for a specific user and channel ID. |
| Get User In App Feed Settings | `getUserInAppFeedSettings` | Returns the feed settings for a user. |
| Get User Preference Set | `getUserPreferenceSet` | Retrieves a specific preference set for a user identified by the preference set ID. |
| Get Workflow Recipient Run | `getWorkflowRecipientRun` | Returns a single workflow recipient run with its associated events. |
| Identify User | `identifyUser` | Create or update a user with the provided identification data. When you identify an existing user, the system merges the properties you specific with what is currently set on the user, updating only the fields included in your requests. |
| List Audience Members | `listAudienceMembers` | Returns a paginated list of members for the specified audience. |
| List Channels For MS Teams Provider | `listChannelsForMsTeamsProvider` | List the Microsoft Teams channels within a team. By default, archived and private channels are excluded from the results. |
| List Channels For Slack Provider | `listChannelsForSlackProvider` | List Slack channels for a Slack workspace. |
| List Message Activities | `listMessageActivities` | Returns a paginated list of activities for the specified message. |
| List Message Delivery Logs | `listMessageDeliveryLogs` | Returns a paginated list of delivery logs for the specified message. |
| List Message Events | `listMessageEvents` | Returns a paginated list of events for the specified message. |
| List Messages | `listMessages` | Returns a paginated list of messages for the current environment. |
| List Messages For Object | `listMessagesForObject` | Returns a paginated list of messages for a specific object in the given collection. Allows filtering by message status and provides various sorting options. |
| List Messages For User | `listMessagesForUser` | Returns a paginated list of messages for a specific user. Messages are sorted with the most recent ones appearing first. Messages outside the account's retention window will not be included in the results. |
| List Object Preference Sets | `listObjectPreferenceSets` | Returns a paginated list of preference sets for the specified object. |
| List Object Schedules | `listObjectSchedules` | Returns a paginated list of schedules for an object. |
| List Objects | `listObjects` | Returns a paginated list of objects from the specified collection. Optionally includes preference data for the objects. |
| List Schedules | `listSchedules` | Returns a paginated list of schedules for the current environment, filtered by workflow and optionally by recipients and tenant. |
| List Subscriptions For Object | `listSubscriptionsForObject` | List subscriptions for an object. Either list the recipients that subscribe to the provided object, or list the objects that the provided object is subscribed to. Determined by the mode query parameter. |
| List Subscriptions For User | `listSubscriptionsForUser` | Retrieves a paginated list of subscriptions for a specific user, in descending order. |
| List Teams For MS Teams Provider | `listTeamsForMsTeamsProvider` | Get a list of teams belonging to the Microsoft Entra tenant. By default, archived and private channels are excluded from the results. |
| List Tenants | `listTenants` | List tenants for the current environment. |
| List User Guides | `listUserGuides` | Returns a list of eligible in-app guides for a specific user and channel. |
| List User In App Feed Items | `listUserInAppFeedItems` | Returns a paginated list of feed items for a user in reverse chronological order, including metadata about the feed. If the user has not yet been identified within Knock, an empty feed will be returned. You can customize the response using response filters to exclude or only include specific properties on your resources. **Notes:** * When making this call from a client-side environment, use your publishable key along with a user token. * This endpoint’s rate limit is always scoped per-user and per-environment. This is true even for requests made without a signed user token. * Any attachments present in trigger data are automatically excluded from both the data and activities fields of UserInAppFeedResponse. |
| List User Preference Sets | `listUserPreferenceSets` | Retrieves a list of all preference sets for a specific user. |
| List User Schedules | `listUserSchedules` | Returns a paginated list of schedules for a specific user, in descending order. |
| List Users | `listUsers` | Retrieve a paginated list of users in the environment. Defaults to 50 users per page. |
| List Workflow Recipient Runs | `listWorkflowRecipientRuns` | Returns a paginated list of workflow recipient runs for the current environment. |
| Mark Message As Unread | `markMessageAsUnread` | Marks a message as unread. This reverses the read state. Read more about message engagement statuses here. |
| Mark Message As Unread Via Unread Path | `markMessageAsUnreadViaUnreadPath` | Marks a message as unread. This reverses the read state. Read more about message engagement statuses here. |
| Mark Message As Unseen | `markMessageAsUnseen` | Marks a message as unseen. This reverses the seen state. Read more about message engagement statuses here. |
| Mark Message As Unseen Via Seen Path | `markMessageAsUnseenViaSeenPath` | Marks a message as unseen. This reverses the seen state. Read more about message engagement statuses here. |
| Mark Message Interacted | `markMessageInteracted` | Marks a message as interacted with by the user. This can include any user action on the message, with optional metadata about the specific interaction. Cannot include more than 5 key-value pairs, must not contain nested data. Read more about message engagement statuses here. |
| Mark Message Read | `markMessageRead` | Marks a message as read. This indicates that the user has read the message content. Read more about message engagement statuses here. |
| Mark Message Seen | `markMessageSeen` | Marks a message as seen. This indicates that the user has viewed the message in their feed or inbox. Read more about message engagement statuses here. |
| Mark User Guide As Archived By Filters | `markUserGuideAsArchivedByFilters` | Records that a guide has been archived by a user, triggering any associated archived events. |
| Mark User Guide As Interacted By Filters | `markUserGuideAsInteractedByFilters` | Records that a user has interacted with a guide, triggering any associated interacted events. |
| Mark User Guide As Seen By Filters | `markUserGuideAsSeenByFilters` | Records that a guide has been seen by a user, triggering any associated seen events. |
| Mark User Guide As Unarchived | `markUserGuideAsUnarchived` | Records that a guide has been unarchived, triggering any associated unarchived events. |
| Mark User Guide Message As Archived | `markUserGuideMessageAsArchived` | Records that a guide has been archived by a user, triggering any associated archived events. |
| Mark User Guide Message As Interacted | `markUserGuideMessageAsInteracted` | Records that a user has interacted with a guide, triggering any associated interacted events. |
| Mark User Guide Message As Seen | `markUserGuideMessageAsSeen` | Records that a guide has been seen by a user, triggering any associated seen events. |
| Merge User | `mergeUser` | Merge two users together, where the user specified with the from_user_id param will be merged into the user specified by user_id. |
| MS Teams Provider Auth Check | `msTeamsProviderAuthCheck` | Check if a connection to Microsoft Teams has been authorized for a given Microsoft Teams tenant object. |
| MS Teams Provider Revoke Access | `msTeamsProviderRevokeAccess` | Remove a Microsoft Entra tenant ID from a Microsoft Teams tenant object. |
| Process Census RPC Request | `processCensusRpcRequest` | Processes a Census custom destination RPC request. |
| Process Hightouch RPC Request | `processHightouchRpcRequest` | Processes a Hightouch embedded destination RPC request. |
| Remove Audience Members | `removeAudienceMembers` | Removes one or more members from the specified audience. |
| Reset User Guide Engagement | `resetUserGuideEngagement` | Resets the engagement state of a guide for a user, removing the guide's engagement log entry so the next interaction creates a fresh engagement. |
| Set Object | `setObject` | Creates a new object or updates an existing one in the specified collection. This operation is used to identify objects with their properties, as well as optional preferences and channel data. |
| Set Object Channel Data | `setObjectChannelData` | Sets the channel data for the specified object and channel. If no object exists in the current environment for the given collection and object_id, Knock will create the object as part of this request. |
| Set Tenant | `setTenant` | Sets a tenant within an environment, performing an upsert operation. Any existing properties will be merged with the incoming properties. |
| Set User Channel Data | `setUserChannelData` | Updates or creates channel data for a specific user and channel ID. If no user exists in the current environment for the given user_id, Knock will create the user entry as part of this request. |
| Slack Provider Auth Check | `slackProviderAuthCheck` | Check if a Slack channel is authenticated. |
| Slack Provider Revoke Access | `slackProviderRevokeAccess` | Revoke access for a Slack channel. |
| Trigger Workflow | `triggerWorkflow` | Trigger a workflow (specified by the key) to run for the given recipients, using the parameters provided. Returns an identifier for the workflow run request. All workflow runs are executed asynchronously. This endpoint also handles inline identifications for the actor, recipient, and tenant fields. |
| Trigger Workflow Via Notify Endpoint | `triggerWorkflowViaNotify` | Triggers a workflow with the given key, actor, recipients, and optional data. |
| Unarchive Message | `unarchiveMessage` | Removes a message from the archived state, making it visible in the default message list in the feed again. |
| Unarchive Message Via Archived Path | `unarchiveMessageViaArchivedPath` | Removes a message from the archived state, making it visible in the default message list in the feed again. |
| Unset Object Channel Data | `unsetObjectChannelData` | Unsets the channel data for the specified object and channel. |
| Unset User Channel Data | `unsetUserChannelData` | Deletes channel data for a specific user and channel ID. |
| Update Object Preference Categories | `updateObjectPreferenceCategories` | Updates the category preferences for an object's preference set. This endpoint is marked deprecated in the Knock API specification. |
| Update Object Preference Category | `updateObjectPreferenceCategory` | Updates a specific category preference for an object's preference set. Deprecated. This endpoint is marked deprecated in the Knock API specification. |
| Update Object Preference Channel Type | `updateObjectPreferenceChannelType` | Updates a specific channel type preference for an object's preference set. This endpoint is marked deprecated in the Knock API specification. |
| Update Object Preference Channel Types | `updateObjectPreferenceChannelTypes` | Updates the channel type preferences for an object's preference set. This endpoint is marked deprecated in the Knock API specification. |
| Update Object Preference Set | `updateObjectPreferenceSet` | Sets preferences within the given preference set. By default, this is a destructive operation and will replace any existing preferences with the preferences given. Use '__persistence_strategy': 'merge' to merge with existing preferences instead. If no object exists in the current environment for the given :collection and :object_id, Knock will create the object as part of this request. The preference set :id can be either default or a tenant.id. Learn more about per-tenant preferences. |
| Update Object Preference Workflow | `updateObjectPreferenceWorkflow` | Updates a specific workflow preference for an object's preference set. This endpoint is marked deprecated in the Knock API specification. |
| Update Object Preference Workflows | `updateObjectPreferenceWorkflows` | Updates the workflow preferences for an object's preference set. This endpoint is marked deprecated in the Knock API specification. |
| Update Schedules | `updateSchedules` | Updates one or more existing schedules with new timing, data, or other properties. All specified schedule IDs will be updated with the same values. This endpoint also handles inline identifications for the actor, recipient, and tenant fields. |
| Update User Preference Categories | `updateUserPreferenceCategories` | Updates the categories in a specific user preference set. This operation is deprecated. This endpoint is marked deprecated in the Knock API specification. |
| Update User Preference Category | `updateUserPreferenceCategory` | Updates a single category in a specific user preference set. This operation is deprecated. This endpoint is marked deprecated in the Knock API specification. |
| Update User Preference Channel Type | `updateUserPreferenceChannelType` | Updates a single channel type in a specific user preference set. This operation is deprecated. This endpoint is marked deprecated in the Knock API specification. |
| Update User Preference Channel Types | `updateUserPreferenceChannelTypes` | Updates the channel types in a specific user preference set. This operation is deprecated. This endpoint is marked deprecated in the Knock API specification. |
| Update User Preference Set | `updateUserPreferenceSet` | Updates a complete preference set for a user. By default, this is a destructive operation and will replace any existing preferences with the preferences given. Use '__persistence_strategy__': 'merge' to merge with existing preferences instead. |
| Update User Preference Workflow | `updateUserPreferenceWorkflow` | Updates a single workflow in a specific user preference set. This operation is deprecated. This endpoint is marked deprecated in the Knock API specification. |
| Update User Preference Workflows | `updateUserPreferenceWorkflows` | Updates the workflows in a specific user preference set. This operation is deprecated. This endpoint is marked deprecated in the Knock API specification. |
