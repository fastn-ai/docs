---
description: "Pushwoosh customer engagement platform — send push notifications, emails, and multichannel messages; manage devices, tags, segments, presets, events,…"
hidden: true
---

# Pushwoosh

Pushwoosh customer engagement platform — send push notifications, emails, and multichannel messages; manage devices, tags, segments, presets, events, campaigns, and delivery statistics via the Pushwoosh Messaging and Device APIs (json/1.3 and api/v2).

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [pushwoosh.com](https://pushwoosh.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 60 |
| **Events** | 0 |
| **Slug** | `pushwoosh` |

## Use it

Add Pushwoosh from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pushwoosh.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Tag | `addTag` | Creates a new tag (custom attribute) on the account for segmenting devices and users. |
| Application Open | `applicationOpen` | Logs an application open event for a device, used for engagement and last-open analytics. |
| Bulk Register Devices | `bulkRegisterDevice` | Registers multiple devices in a single asynchronous request (Audience API v2). Returns a request_id to poll for status. |
| Bulk Set Tags | `bulkSetTags` | Sets tag values for multiple devices in a single asynchronous request (Audience API v2). Requires at least 50 devices. |
| Bulk Unregister Devices | `bulkUnregisterDevice` | Unregisters multiple devices in a single asynchronous request (Audience API v2). Returns a request_id to poll for status. |
| Cancel Message | `cancelMessage` | Cancels a scheduled message before it is delivered, by its message code. |
| Create Application | `createApplication` | Creates a new application in the Pushwoosh account and returns its application code. |
| Create Campaign | `createCampaign` | Creates a new push campaign for the application. Messages can be grouped under a campaign for reporting. |
| Create Email Message | `createEmailMessage` | Creates and sends an email message based on an email preset. The notifications array carries per-message subject, content, recipients, and scheduling. |
| Create Event | `createEvent` | Creates an event type for the application that can later be posted from devices to trigger automations. |
| Create Filter | `createFilter` | Creates a segment (filter) from a segmentation expression that can be reused to target messages. |
| Create Message | `createMessage` | Creates and sends one or more push notifications to the application audience. The notifications array carries per-message content, targeting, scheduling, and platform options. |
| Create Preset | `createPreset` | Creates a reusable message preset with predefined content and segmentation for the application. |
| Create Targeted Message | `createTargetedMessage` | Creates a push notification targeted by a devices filter expression rather than an explicit device list. Deprecated in favor of Create Message but still supported. |
| Create Test Device | `createTestDevice` | Registers a test device for the application, used to preview and QA push notifications. |
| Delete Application | `deleteApplication` | Deletes an application from the account by its application code. |
| Delete Campaign | `deleteCampaign` | Deletes a push campaign by its campaign code. |
| Delete Device | `deleteDevice` | Deletes a device and all of its associated data from the application (Device API v2). |
| Delete Email | `deleteEmail` | Removes an email address from the application's subscriber database (Email channel). |
| Delete Filter | `deleteFilter` | Deletes a segment (filter) by its name. |
| Delete Message | `deleteMessage` | Deletes a scheduled message that has not yet been delivered, by its message code. |
| Delete Preset | `deletePreset` | Deletes a message preset by its preset code. |
| Delete Tag | `deleteTag` | Deletes a tag and all its associated values from the account. |
| Delete User | `deleteUser` | Deletes a user and all devices associated with the specified external user ID (Device API v2, asynchronous). |
| Export Segment | `exportSegment` | Schedules an export of subscribers matching a segment/filter expression (Audience API v2). Returns a task_id to fetch the result. |
| Get Application | `getApplication` | Retrieves configuration and platform details for a single application by its code. |
| Get Application File | `getApplicationFile` | Retrieves a configuration file (certificate or private key) associated with an application platform. |
| Get Applications | `getApplications` | Retrieves all applications in the Pushwoosh account. |
| Get Bounced Emails | `bouncedEmails` | Retrieves email bounce, complaint, and bounce-reason information for a date range (Statistics API v2, Email channel). |
| Get Bulk Register Status | `bulkRegisterDeviceStatus` | Retrieves the status and progress of a bulk device registration request by its request_id (Audience API v2). |
| Get Bulk Set Tags Status | `bulkSetTagsStatus` | Retrieves the status and progress of a bulk set tags request by its request_id (Audience API v2). |
| Get Bulk Unregister Status | `bulkUnregisterDeviceStatus` | Retrieves the status and progress of a bulk device unregistration request by its request_id (Audience API v2). |
| Get Campaigns | `getCampaigns` | Retrieves the list of campaigns configured for the application, with pagination support. |
| Get Email Link Interactions | `linksInteractions` | Retrieves email link-click metrics grouped by link template (Statistics API v2, Email channel). |
| Get Export Segment Result | `exportSegmentResult` | Retrieves the CSV download link and device count for a completed segment export (Audience API v2). |
| Get Inbox Messages | `getInboxMessages` | Retrieves the list of Message Inbox items for a specific user or device. |
| Get Message Details | `getMessageDetails` | Retrieves the details and current status of a previously created message by its message code. |
| Get Message Log | `getMessageLog` | Retrieves a detailed, per-device delivery/interaction log for messages in a date range (Statistics API v2). |
| Get Message Totals By Intervals | `totalsByIntervals` | Retrieves hourly-aggregated metrics and conversion data for a specific message (Statistics API v2). |
| Get Preset | `getPreset` | Retrieves a message preset's parameters by its preset code. |
| Get Push History | `getPushHistory` | Retrieves the account push message history. Deprecated but supported for legacy reporting. |
| Get Tags | `getTags` | Retrieves the tag values currently set for a device (by hwid) or user. |
| List Filters | `listFilters` | Retrieves all segments (filters) available for the application. |
| List Messages | `messagesList` | Retrieves a paginated list of sent messages with optional details and metrics (Statistics API v2). |
| List Presets | `listPresets` | Retrieves all message presets configured for the application. |
| List Tags | `listTags` | Retrieves the list of tags configured on the Pushwoosh account, each with its name and data type. |
| List Test Devices | `listTestDevices` | Retrieves all test devices registered for the application. |
| Message Delivery Event | `messageDeliveryEvent` | Registers a push delivery event for a device, using the push hash tag delivered with the notification. |
| Post Event | `postEvent` | Triggers an in-app event for a device/user, optionally carrying attributes, to drive event-based automations. |
| Push Stat | `pushStat` | Records a push notification open event for a device, using the push hash tag delivered with the notification. |
| Register Device | `registerDevice` | Registers a device (push token) for the application, optionally with user, language, timezone, and tags. |
| Register Email | `registerEmail` | Registers an email address as a subscriber for the application (Email channel). |
| Register Email User | `registerEmailUser` | Associates an external user ID with a registered email address (Email channel). |
| Register User | `registerUser` | Associates an external user ID with a device (hwid), enabling user-centric messaging across devices. |
| Set Badge | `setBadge` | Sets the current application icon badge value for a device (iOS badge counter). |
| Set Email Tags | `setEmailTags` | Sets tag values for a registered email address (Email channel). |
| Set Tags | `setTags` | Assigns tag values to a device (by hwid) or user for segmentation and personalization. |
| Unregister Device | `unregisterDevice` | Removes a device's push token from the application so it stops receiving notifications. |
| Update Application | `updateApplication` | Updates settings of an existing application, such as its title. |
| Update Inbox Status | `inboxStatus` | Updates the status of a specific Message Inbox item (delivered, read, opened, or deleted) for a user/device. |
