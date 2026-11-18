---
description: "Airship (Urban Airship) customer engagement platform — send and schedule push notifications, manage channels and named users, segments, static lists, tags,…"
---

# Airship

Airship (Urban Airship) customer engagement platform — send and schedule push notifications, manage channels and named users, segments, static lists, tags, attributes, subscription lists, automation, custom events, message center, templates, and reporting via the Airship Engage REST API.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [airship.com](https://airship.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 133 |
| **Events** | 0 |
| **Slug** | `airship` |

## Use it

Add Airship from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.airship.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Associate Named User | `associateNamedUser` | Associate a channel with a named user, linking the device to that identity. |
| Batch Delete Inbox Messages | `batchDeleteInboxMessages` | Delete multiple Message Center messages from inboxes in one call. |
| Bulk Send | `bulkSend` | Send a message to a previously uploaded bulk audience referenced by bulk_id. |
| Create and Send | `createAndSend` | Create audience records and send a message to email, SMS, MMS, or open channels in a single call. |
| Create Attribute List | `createAttributeList` | Create an attribute list for bulk attribute updates via CSV. |
| Create Content Template | `createContentTemplate` | Create a reusable content template (snippet) of a given channel type. |
| Create Custom Events | `createCustomEvent` | Ingest one or more custom events for analytics and automation triggers. Provide a JSON array string of event objects. |
| Create Email Attachment | `createEmailAttachment` | Upload an attachment (base64-encoded) that can be referenced in email notifications. |
| Create Experiment | `createExperiment` | Create an A/B test experiment with multiple message variants. |
| Create Pipeline | `createPipeline` | Create an automation pipeline (automated message triggered by events or behavior). |
| Create Schedule | `createSchedule` | Schedule a push notification to be delivered at a specified time. |
| Create Segment | `createSegment` | Create an audience segment from tag/attribute criteria. |
| Create Static List | `createList` | Create a static list of channels or named users. |
| Create Tag List | `createTagList` | Create a tag list for bulk tag add/remove/set via CSV. |
| Create Template | `createTemplate` | Create a personalization message template with variables and a push payload. |
| Delete Content Template | `deleteContentTemplate` | Delete a content template by template ID. |
| Delete Content Template by External ID | `deleteContentTemplateByExternal` | Delete a content template by its type and external ID. |
| Delete Inbox Message | `deleteInboxMessage` | Delete a single Message Center message from a user's inbox by push ID. |
| Delete Pipeline | `deletePipeline` | Delete an automation pipeline by pipeline ID. |
| Delete Schedule | `deleteSchedule` | Delete a scheduled push by schedule ID. |
| Delete Scheduled Experiment | `deleteScheduledExperiment` | Delete a scheduled A/B test experiment by experiment ID. |
| Delete Segment | `deleteSegment` | Delete a segment by segment ID. |
| Delete Static List | `deleteList` | Delete a static list by name. |
| Delete Tag List | `deleteTagList` | Delete a tag list by name. |
| Delete Template | `deleteTemplate` | Delete a personalization template by template ID. |
| Disassociate Named User | `disassociateNamedUser` | Remove the association between a channel and its named user. |
| Download Static List CSV | `downloadListCsv` | Download the channels in a static list as CSV. |
| Get Activity Details Report | `getActivityDetails` | Retrieve a detailed activity log of message sends over a time period. |
| Get App Opens Report | `getOpensReport` | Retrieve the number of times the app was opened over a time period. |
| Get Attribute List Errors | `getAttributeListErrors` | Retrieve processing errors and status for an attribute list. |
| Get Channel | `getChannel` | Look up a single channel (device registration) by its channel ID. |
| Get Content Template | `getContentTemplate` | Retrieve a single content template by template ID. |
| Get Content Template by External ID | `getContentTemplateByExternal` | Retrieve a content template by its type and external ID. |
| Get Custom Events Per Group Summary | `getCustomEventsPerGroup` | Retrieve custom event summary attributed to a push group. |
| Get Custom Events Per Push Summary | `getCustomEventsPerPush` | Retrieve custom event summary attributed to a single push. |
| Get Custom Events Report | `getCustomEventsReport` | Retrieve custom event counts and values over a time period. |
| Get Devices Report | `getDevicesReport` | Retrieve device counts (opted-in, uninstalled, etc.) for a given date. |
| Get Email Channel | `getEmailChannel` | Look up an email channel by its email address. |
| Get Experiment | `getExperiment` | Retrieve a single A/B test experiment by experiment ID. |
| Get Experiment Overview Report | `getExperimentOverview` | Retrieve the overview report for an A/B test experiment by push ID. |
| Get Experiment Variant Report | `getExperimentVariantReport` | Retrieve the report for a single variant of an A/B test experiment. |
| Get Named User | `getNamedUser` | Look up a single named user and its associated channels by named user ID. |
| Get Named User Subscription Lists | `getNamedUserSubscriptionLists` | Retrieve the subscription lists a named user is subscribed to. |
| Get Opt-ins Report | `getOptinsReport` | Retrieve the number of opt-ins over a time period, by platform. |
| Get Opt-outs Report | `getOptoutsReport` | Retrieve the number of opt-outs over a time period, by platform. |
| Get Per Group Detail Report | `getPerGroupDetail` | Retrieve detailed statistics for a push group by group ID. |
| Get Per Group Series Report | `getPerGroupSeries` | Retrieve a time series of statistics for a push group by group ID. |
| Get Per Push Body Report | `getPerPushBody` | Retrieve the message body that was sent for a single push by push ID. |
| Get Per Push Detail Report | `getPerPushDetail` | Retrieve detailed statistics for a single push by push ID. |
| Get Per Push Series Report | `getPerPushSeries` | Retrieve a time series of statistics for a single push by push ID. |
| Get Pipeline | `getPipeline` | Retrieve a single automation pipeline by pipeline ID. |
| Get Pipeline Constraints | `getPipelineConstraints` | List automation pipeline rate constraints. |
| Get Pipeline Limits | `getPipelineLimits` | Retrieve automation pipeline limits for the project. |
| Get Push Response Report | `getResponseReport` | Retrieve response statistics for a single push by push ID. |
| Get Region | `getRegion` | Retrieve a single region by region ID. |
| Get Response List | `getResponseList` | List individual push responses over a time period. |
| Get Responses Report | `getResponsesReport` | Retrieve direct and influenced response counts over a time period. |
| Get Schedule | `getSchedule` | Retrieve a single scheduled push by schedule ID. |
| Get Segment | `getSegment` | Retrieve a single segment's name and criteria by segment ID. |
| Get Sends Report | `getSendsReport` | Retrieve the number of push messages sent over a time period, by platform. |
| Get SMS Channel | `getSmsChannel` | Look up an SMS channel by mobile number and sender. |
| Get Static List | `getList` | Retrieve metadata and status for a single static list by name. |
| Get Tag List Errors | `getTagListErrors` | Download processing errors for a tag list as CSV. |
| Get Template | `getTemplate` | Retrieve a single personalization template by template ID. |
| Get Time in App Report | `getTimeInAppReport` | Retrieve time-in-app metrics over a time period. |
| Get Web Interaction Report | `getWebInteractionReport` | Retrieve web notification interaction (clicks and sessions) statistics over a time period. |
| List Attribute Lists | `listAttributeLists` | List all attribute lists in the project. |
| List Channels | `listChannels` | List all channels (device registrations) for the Airship project, with pagination. |
| List Content Templates | `listContentTemplates` | List reusable content templates (snippets) in the project. |
| List Deleted Pipelines | `listDeletedPipelines` | List automation pipelines that have been deleted. |
| List Experiments | `listExperiments` | List A/B test experiments in the project. |
| List Filtered Pipelines | `listFilteredPipelines` | List automation pipelines matching filter criteria. |
| List Named Users | `listNamedUsers` | List all named users for the Airship project, with pagination. |
| List Pipelines | `listPipelines` | List automation pipelines (automated messages) in the project. |
| List Regions | `listRegions` | List geofence/beacon regions defined for the project. |
| List Scheduled Experiments | `listScheduledExperiments` | List scheduled A/B test experiments. |
| List Schedules | `listSchedules` | List all scheduled push notifications, with pagination. |
| List Segments | `listSegments` | List all audience segments defined for the project. |
| List Static Lists | `listLists` | List all static lists in the project. |
| List Subscription Lists | `listSubscriptionLists` | List all subscription lists defined for the Airship project. |
| List Tag Lists | `listTagLists` | List all tag lists in the project. |
| List Templates | `listTemplates` | List personalization message templates (with variables) in the project. |
| Opt Out SMS Channel | `optOutSmsChannel` | Opt an SMS channel out of receiving messages for a given sender. |
| Pause Schedule | `pauseSchedule` | Pause a recurring scheduled push by schedule ID. |
| Push to Template | `pushTemplate` | Send a push using a personalization template with variable substitutions. |
| Register Email Channel | `registerEmailChannel` | Register an email channel (email address) and its opt-in state. |
| Register Open Channel | `registerOpenChannel` | Create or update an open channel for a custom (open) platform. The open platform must be configured in the Airship project. |
| Register SMS Channel | `registerSmsChannel` | Register an SMS channel (opt in a mobile number) for a configured SMS sender. |
| Replace Email Channel | `replaceEmailChannel` | Replace an existing email channel's address and registration by channel ID. |
| Resume Schedule | `resumeSchedule` | Resume a paused recurring scheduled push by schedule ID. |
| Schedule Bulk Send | `scheduleBulkSend` | Schedule a bulk-send message for future delivery to a bulk audience. |
| Schedule Create and Send | `scheduleCreateAndSend` | Schedule a create-and-send message for future delivery to email or SMS channels. |
| Schedule Templated Push | `scheduleTemplatePush` | Schedule one or more templated pushes for future delivery. Provide a JSON array string of scheduled template push objects. |
| Send Push | `sendPush` | Send a push notification immediately to a specified audience across one or more device types. |
| Set Channel Attributes | `setChannelAttributes` | Set or remove attributes on one or more channels. |
| Set Named User Attributes | `setNamedUserAttributes` | Set or remove attributes on one or more named users. |
| Suppress Email Channel | `suppressEmailChannel` | Suppress an email address so Airship stops sending to it, with a reason. |
| Uninstall Channel | `uninstallChannel` | Uninstall (deactivate) one or more channels so they no longer receive messages. |
| Uninstall Email Channel | `uninstallEmailChannel` | Uninstall an email channel by email address so it no longer receives messages. |
| Uninstall Named User | `uninstallNamedUser` | Uninstall one or more named users (removes the identity and its data). |
| Uninstall Open Channel | `uninstallOpenChannel` | Uninstall an open channel identified by address and open platform name. |
| Uninstall SMS Channel | `uninstallSmsChannel` | Uninstall an SMS channel for a given sender and mobile number. |
| Unsuppress Email Channel | `unsuppressEmailChannel` | Remove a suppression from an email address so Airship can send to it again. |
| Update Channel Subscription Lists | `updateChannelSubscriptionLists` | Subscribe or unsubscribe one or more channels to subscription lists. |
| Update Channel Tags | `updateChannelTags` | Add, remove, or set tags on one or more channels within specified tag groups. |
| Update Content Template | `updateContentTemplate` | Update a content template by template ID. |
| Update Email Channel | `updateEmailChannel` | Update an existing email channel's registration details by channel ID. |
| Update Email Tags | `updateEmailTags` | Add, remove, or set tags on an email channel identified by email address. |
| Update Named User | `updateNamedUser` | Bulk update a named user's tags, attributes, and channel associations in one call. |
| Update Named User Subscription Lists | `updateNamedUserSubscriptionLists` | Subscribe or unsubscribe one or more named users to subscription lists. |
| Update Named User Subscription Lists (Scoped) | `scopedNamedUserSubscriptionLists` | Subscribe or unsubscribe a named user to subscription lists per channel scope. |
| Update Named User Tags | `updateNamedUserTags` | Add, remove, or set tags on one or more named users within tag groups. |
| Update Open Channel Tags | `updateOpenChannelTags` | Add, remove, or set tags on an open channel identified by address and platform. |
| Update Pipeline | `updatePipeline` | Update an automation pipeline by pipeline ID. |
| Update Pipeline Constraints | `updatePipelineConstraints` | Update automation pipeline rate constraints. |
| Update Schedule | `updateSchedule` | Update an existing scheduled push by schedule ID. |
| Update Segment | `updateSegment` | Update a segment's display name and criteria by segment ID. |
| Update SMS Channel | `updateSmsChannel` | Update an existing SMS channel's registration details by channel ID. |
| Update SMS Tags | `updateSmsTags` | Add, remove, or set tags on an SMS channel identified by mobile number and sender. |
| Update Static List | `updateList` | Update a static list's name, description, or metadata. |
| Update Template | `updateTemplate` | Update a personalization template by template ID. |
| Upload Attribute List CSV | `uploadAttributeListCsv` | Upload attribute values for an attribute list as CSV. |
| Upload Bulk Audience | `uploadBulkAudience` | Upload a CSV audience for a platform and receive a bulk_id to use with bulk-send. |
| Upload Named Users | `uploadNamedUsers` | Bulk create or update named users, their tags, attributes, and subscription lists in a single upload. |
| Upload Static List CSV | `uploadListCsv` | Upload the contents (identifiers) of a static list as CSV. |
| Upload Tag List CSV | `uploadTagListCsv` | Upload the members of a tag list as CSV. |
| Upsert Content Template by External ID | `upsertContentTemplateByExternal` | Create or update a content template by its type and external ID. |
| Validate Bulk Send | `validateBulkSend` | Validate a bulk-send payload without delivering it. |
| Validate Create and Send | `validateCreateAndSend` | Validate a create-and-send payload without delivering it. |
| Validate Experiment | `validateExperiment` | Validate an A/B test experiment definition without creating it. |
| Validate Pipeline | `validatePipeline` | Validate an automation pipeline definition without creating it. |
| Validate Push | `validatePush` | Validate a push notification payload without sending it. |
| Validate Template Push | `validateTemplatePush` | Validate a templated push without sending it. |
