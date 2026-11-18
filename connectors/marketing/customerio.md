---
description: "Customer.io marketing automation and customer messaging platform."
hidden: true
---

# Customer.io

<img src="../../.gitbook/assets/connectors/customerio.png" alt="Customer.io logo" width="64">

Customer.io marketing automation and customer messaging platform. Covers the Track API (people, events, devices, manual segments, merge, suppression, v2 entity/batch) using HTTP Basic auth, and the App/Journeys API (transactional send, broadcasts, customers, campaigns, newsletters, segments, messages, activities, exports, collections, snippets, sender identities, transactional templates, reporting webhooks) using Bearer auth.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [customer.io](https://customer.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `customerio` |

## Use it

Add Customer.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.customerio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Device | `addDevice` | Register or update a device token for a person to enable push notifications. |
| Add People to Manual Segment | `addCustomersToSegment` | Add one or more people to a manual segment via the Track API. |
| Create Collection | `createCollection` | Create a reusable data collection with inline data. |
| Create Manual Segment | `createSegment` | Create a manual segment that people can be added to or removed from via the Track API. |
| Create or Update Snippet | `updateSnippets` | Create or update a reusable content snippet (upsert by name). |
| Create Reporting Webhook | `createReportingWebhook` | Create a reporting webhook that posts selected email/message events to an endpoint URL. |
| Delete Collection | `deleteCollection` | Delete a data collection. |
| Delete Device | `deleteDevice` | Remove a device token from a person. |
| Delete Person | `deleteCustomer` | Delete a person from the Customer.io workspace via the Track API. |
| Delete Reporting Webhook | `deleteReportingWebhook` | Delete a reporting webhook configuration. |

<details>

<summary>See 82 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Segment | `deleteSegment` | Delete a manual segment. |
| Delete Snippet | `deleteSnippet` | Delete a content snippet by name. |
| Download Export | `downloadExport` | Get a signed download URL for a completed export. |
| Export Deliveries | `exportDeliveries` | Start an export of message deliveries matching the given criteria. |
| Export People | `exportCustomers` | Start an export of people matching a filter. |
| Get Account Region | `getAccountRegion` | Return the Customer.io data region (us or eu) and region-specific API hosts for the workspace associated with the Track API credentials. Useful for verifying Track API credentials and determining the correct regional host. |
| Get Archived Message | `getArchivedMessage` | Get the archived (full rendered) content of a sent message. |
| Get Broadcast | `getBroadcast` | Get a single broadcast by ID. |
| Get Broadcast Actions | `getBroadcastActions` | List the actions (messages) that make up a broadcast. |
| Get Broadcast Messages | `getBroadcastMessages` | List messages sent as part of a broadcast. |
| Get Broadcast Metrics | `getBroadcastMetrics` | Get aggregate metrics for a broadcast. |
| Get Broadcast Trigger Errors | `getBroadcastTriggerErrors` | List per-recipient data errors for a broadcast trigger. |
| Get Broadcast Trigger Status | `getBroadcastTriggerStatus` | Get the status of a specific broadcast trigger. |
| Get Campaign | `getCampaign` | Get a single campaign by ID. |
| Get Campaign Action | `getCampaignAction` | Get a single action (message) within a campaign. |
| Get Campaign Action Messages | `getCampaignActionMessages` | List messages sent by a specific campaign action. |
| Get Campaign Action Metrics | `getCampaignActionMetrics` | Get metrics for a specific campaign action. |
| Get Campaign Actions | `getCampaignActions` | List the actions (messages) in a campaign. |
| Get Campaign Journey Metrics | `getCampaignJourneyMetrics` | Get journey (per-step conversion) metrics for a campaign. |
| Get Campaign Messages | `getCampaignMessages` | List messages sent by a campaign. |
| Get Campaign Metrics | `getCampaignMetrics` | Get aggregate metrics for a campaign. |
| Get Collection | `getCollection` | Get a single data collection's metadata by ID. |
| Get Collection Content | `getCollectionContent` | Get the data rows stored in a collection. |
| Get Export | `getExport` | Get the status and metadata of an export job. |
| Get Message | `getMessage` | Get a single sent message by its delivery ID. |
| Get Newsletter | `getNewsletter` | Get a single newsletter by ID. |
| Get Newsletter Messages | `getNewsletterMessages` | List messages sent as part of a newsletter. |
| Get Newsletter Metrics | `getNewsletterMetrics` | Get aggregate metrics for a newsletter. |
| Get Newsletter Variant Metrics | `getNewsletterVariantMetrics` | Get metrics for a specific newsletter content variant. |
| Get Newsletter Variants | `getNewsletterVariants` | List the content variants of a newsletter. |
| Get Person Activities | `getCustomerActivities` | Get the activity history (events, attribute changes, messages) for a person. |
| Get Person Attributes | `getCustomerAttributes` | Get a person's attributes, timestamps, and identifiers by their id. |
| Get Person Messages | `getCustomerMessages` | Get the messages delivered to a person. |
| Get Person Segments | `getCustomerSegments` | Get the segments a person belongs to. |
| Get Reporting Webhook | `getReportingWebhook` | Get a single reporting webhook configuration by ID. |
| Get Segment | `getSegment` | Get a single segment by ID. |
| Get Segment Customer Count | `getSegmentCustomerCount` | Get the number of people in a segment. |
| Get Segment Membership | `getSegmentMembership` | List the people who are members of a segment. |
| Get Segment Usage | `getSegmentUsedBy` | Return the campaigns, sent newsletters, and draft newsletters that reference a segment (GET /v1/segments/{segment_id}/used_by). |
| Get Sender Identity | `getSenderIdentity` | Get a single sender identity by ID. |
| Get Sender Identity Messages | `getSenderIdentityMessages` | List messages sent from a sender identity. |
| Get Sender Identity Metrics | `getSenderIdentityMetrics` | Get metrics for a sender identity. |
| Get Sender Identity Usage | `getSenderIdentityUsedBy` | Return the campaigns, newsletters, and transactional messages that use a sender identity (GET /v1/sender_identities/{sender_id}/used_by). |
| Get Sending IP Addresses | `getIpAddresses` | Return the list of IP addresses Customer.io uses to send webhooks and other outbound requests, for firewall allowlisting (GET /v1/info/ip_addresses). |
| Get Transactional Message | `getTransactionalMessage` | Get a single transactional message template by ID. |
| Get Transactional Message Deliveries | `getTransactionalMessageMessages` | List messages/deliveries sent from a transactional message template. |
| Get Transactional Message Metrics | `getTransactionalMessageMetrics` | Get metrics for a transactional message template. |
| Identify Person | `identifyCustomer` | Create or update a person and their attributes in Customer.io via the Track API. |
| List Activities | `listActivities` | List activities (events, attribute changes, message events) across the workspace. |
| List Broadcasts | `listBroadcasts` | List all broadcasts in the workspace. |
| List Campaigns | `listCampaigns` | List all campaigns in the workspace. |
| List Collections | `listCollections` | List reusable data collections in the workspace. |
| List Exports | `listExports` | List export jobs in the workspace. |
| List Messages | `listMessages` | List sent messages across the workspace, filterable by type, campaign, or newsletter. |
| List Newsletters | `listNewsletters` | List all newsletters in the workspace. |
| List Object Types | `listObjectTypes` | List the object types (non-person entities) defined in the workspace. |
| List Reporting Webhooks | `listReportingWebhooks` | List reporting webhook configurations. Reporting webhooks post message and email events to your endpoint. |
| List Segments | `listSegments` | List all segments (manual and data-driven) in the workspace. |
| List Sender Identities | `listSenderIdentities` | List sender identities (from addresses) configured in the workspace. |
| List Snippets | `listSnippets` | List reusable content snippets in the workspace. |
| List Subscription Topics | `listSubscriptionTopics` | List the subscription topics configured in the workspace subscription center (GET /v1/subscription_topics). |
| List Transactional Messages | `listTransactionalMessages` | List transactional message templates in the workspace. |
| List Workspaces | `listWorkspaces` | List the workspaces in the account with message, people, and object counts (GET /v1/workspaces). |
| Look Up People by Email or ID | `lookupCustomers` | Look up the Customer.io identifiers for people matching an email address or id. |
| Merge People | `mergeCustomers` | Merge a secondary person into a primary person, combining their data and history. |
| Remove People from Manual Segment | `removeCustomersFromSegment` | Remove one or more people from a manual segment via the Track API. |
| Search People | `searchCustomers` | Search for people by attributes, segment membership, and other filters using the App API. |
| Send Transactional Email | `sendTransactionalEmail` | Send a single transactional email using a transactional message template or an inline body. |
| Send Transactional Push | `sendTransactionalPush` | Send a transactional push notification using a transactional push template. |
| Send Transactional SMS | `sendTransactionalSms` | Send a transactional SMS using a transactional SMS template. |
| Suppress Person | `suppressCustomer` | Suppress a person, deleting them and preventing re-creation until unsuppressed. |
| Track Anonymous Event | `trackAnonymousEvent` | Send an event not yet attributed to a known person; it can later be merged onto an identified person. |
| Track Batch (v2) | `trackBatchV2` | Submit multiple person/object/event operations in a single Track API v2 batch request. |
| Track Customer Event | `trackCustomerEvent` | Send a behavioral event attributed to a known person to trigger campaigns and update segments. |
| Track Entity (v2) | `trackEntityV2` | Create, update, or delete a person or object entity using the Track API v2 single-payload endpoint. |
| Track Page View | `trackPageView` | Record a page-view event for a known person via the Track API. |
| Trigger Broadcast | `triggerBroadcast` | Trigger an API-driven broadcast, optionally passing liquid data and per-recipient data. |
| Unsuppress Person | `unsuppressCustomer` | Remove a person from the suppression list so they can be tracked again. |
| Update Campaign Action | `updateCampaignAction` | Update the content of a campaign action (message). |
| Update Collection | `updateCollection` | Update a data collection's name and inline data. |
| Update Collection Content | `updateCollectionContent` | Replace the data rows stored in a collection. |
| Update Reporting Webhook | `updateReportingWebhook` | Update a reporting webhook's endpoint, event subscriptions, or state. |

</details>
