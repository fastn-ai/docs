---
description: "Klaviyo marketing automation platform."
hidden: true
---

# Klaviyo

<img src="../../.gitbook/assets/connectors/lg/klaviyo.png" alt="Klaviyo logo">

Klaviyo marketing automation platform. Manage profiles, lists, segments, campaigns, flows, events, metrics, templates, catalogs, tags, images, and webhooks via the Klaviyo JSON:API.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [klaviyo.com](https://klaviyo.com) |
| **Authentication** | API key |
| **Slug** | `klaviyo` |

## Use it

Add Klaviyo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.klaviyo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Catalog Category Item Relationships | `addCatalogCategoryItemRelationships` | Add items to a catalog category. |
| Add Catalog Item Category Relationships | `addCatalogItemCategoryRelationships` | Add category relationships to a catalog item. |
| Add Profiles to List | `addProfilesToList` | Add one or more profiles to a list (relationship create). Pass profile IDs. |
| Add Tag to Lists | `tagAddToLists` | Associate a tag with one or more lists (relationship create). |
| Assign Campaign Message Template | `assignCampaignMessageTemplate` | Assign a template to a campaign message. Klaviyo clones the template and assigns the clone to the message. |
| Bulk Create Coupon Codes | `bulkCreateCouponCodes` | Create a bulk coupon code creation job to generate many coupon codes at once. |
| Bulk Create Data Source Records | `bulkCreateDataSourceRecords` | Bulk create multiple data source records in a single job. |
| Bulk Create Events | `bulkCreateEvents` | Create multiple events for one profile in a single request. |
| Bulk Import Profiles | `bulkImportProfiles` | Asynchronously bulk create/update up to 10,000 profiles. Optionally associate them to a list via relationships. |
| Cancel Campaign Send Job | `cancelCampaignSendJob` | Cancel or revert a campaign send job by ID. |
| Clone Template | `cloneTemplate` | Clone an existing template into a new template with a given name. |
| Create Back In Stock Subscription | `createBackInStockSubscription` | Subscribe a profile to back-in-stock notifications for a catalog variant. |
| Create Campaign | `createCampaign` | Create a campaign with name, audiences, send strategy and campaign-messages. |
| Create Campaign Send Job | `createCampaignSendJob` | Trigger sending of a campaign immediately by creating a send job. |
| Create Catalog Category | `createCatalogCategory` | Create a new catalog category. |
| Create Catalog Category Bulk Create Job | `createCatalogCategoryBulkCreateJob` | Bulk create catalog categories via a background job. |
| Create Catalog Category Bulk Delete Job | `createCatalogCategoryBulkDeleteJob` | Bulk delete catalog categories via a background job. |
| Create Catalog Category Bulk Update Job | `createCatalogCategoryBulkUpdateJob` | Bulk update catalog categories via a background job. |
| Create Catalog Item | `createCatalogItem` | Create a new catalog item. Provide attributes (external_id, title, description, url, price, etc.) and the catalog relationship. |
| Create Catalog Item Bulk Create Job | `createCatalogItemBulkCreateJob` | Bulk create catalog items via a background job. |
| Create Catalog Item Bulk Delete Job | `createCatalogItemBulkDeleteJob` | Bulk delete catalog items via a background job. |
| Create Catalog Item Bulk Update Job | `createCatalogItemBulkUpdateJob` | Bulk update catalog items via a background job. |
| Create Catalog Variant | `createCatalogVariant` | Create a new catalog variant linked to a catalog item. |
| Create Catalog Variant Bulk Create Job | `createCatalogVariantBulkCreateJob` | Bulk create catalog variants via a background job. Each variant must reference a parent catalog item. |
| Create Catalog Variant Bulk Delete Job | `createCatalogVariantBulkDeleteJob` | Bulk delete catalog variants via a background job. |
| Create Catalog Variant Bulk Update Job | `createCatalogVariantBulkUpdateJob` | Bulk update catalog variants via a background job. |
| Create Conversation Message | `createConversationMessage` | Send a message to an existing SMS conversation. |
| Create Coupon | `createCoupon` | Create a new coupon. Body must follow Klaviyo JSON:API format with data.type 'coupon'. |
| Create Coupon Code | `createCouponCode` | Create a unique coupon code associated with a coupon, optionally tied to a profile. |
| Create Data Source | `createDataSource` | Create a new data source. |
| Create Data Source Record | `createDataSourceRecord` | Create a single data source record (ingest a record into a data source). |
| Create Event | `createEvent` | Track an event for a profile against a metric. Provide the full event data object (properties, metric, profile, time, value). |
| Create Flow | `createFlow` | Create a new flow with triggers, actions, and optional profile filters. |
| Create Form | `createForm` | Create a new signup form in Klaviyo with the given definition, status, and name. |
| Create List | `createList` | Create a new list with a name. |
| Create or Update Profile | `createOrUpdateProfile` | Upsert a profile by identifier (email/phone_number/external_id). Creates if new, updates if existing. |
| Create Profile | `createProfile` | Create a new profile with attributes such as email, phone_number, first_name, last_name, and custom properties. |
| Create Profile Bulk Import Job | `createProfileBulkImportJob` | Create a new profile bulk import job to import or update profiles. |
| Create Profile Subscription Bulk Create Job | `createProfileSubscriptionBulkCreateJob` | Bulk subscribe profiles to email/SMS channels, optionally adding them to a list. |
| Create Profile Subscription Bulk Delete Job | `createProfileSubscriptionBulkDeleteJob` | Bulk unsubscribe profiles from email/SMS channels. |
| Create Push Token | `createPushToken` | Create or update a push token for a profile. Used to register a device push token from APNS (iOS) or FCM (Android). |
| Create Segment | `createSegment` | Create a new segment with a name and a segment definition (condition groups). |
| Create Tag | `createTag` | Create a new tag, optionally under a tag group. |
| Create Tag Group | `createTagGroup` | Create a new tag group. |
| Create Template | `createTemplate` | Create a new email template with name and HTML content. |
| Create Universal Content | `createUniversalContent` | Create a new template universal content block. |
| Create Web Feed | `createWebFeed` | Create a new web feed. |
| Create Webhook | `createWebhook` | Create a new webhook subscription for selected event topics (POST /api/webhooks). Topics are subscribed via the relationships.webhook-topics.data array. |
| Delete Campaign | `deleteCampaign` | Delete a campaign by ID. |
| Delete Catalog Category | `deleteCatalogCategory` | Delete a catalog category by its compound ID. |
| Delete Catalog Item | `deleteCatalogItem` | Delete a catalog item by its compound ID. |
| Delete Catalog Variant | `deleteCatalogVariant` | Delete a catalog variant by its compound ID. |
| Delete Coupon | `deleteCoupon` | Delete a coupon by ID. Returns 204 No Content on success. |
| Delete Coupon Code | `deleteCouponCode` | Delete a coupon code by ID. Returns 204 No Content on success. |
| Delete Data Source | `deleteDataSource` | Delete a data source by ID. |
| Delete Flow | `deleteFlow` | Delete a flow by ID. |
| Delete Form | `deleteForm` | Delete a form by ID. Returns 204 No Content on success. |
| Delete List | `deleteList` | Delete a list by ID. |
| Delete Push Token | `deletePushToken` | Delete a push token by ID. |
| Delete Segment | `deleteSegment` | Delete a segment by ID. |
| Delete Tag | `deleteTag` | Delete a tag by ID. |
| Delete Tag Group | `deleteTagGroup` | Delete a tag group by ID. |
| Delete Template | `deleteTemplate` | Delete a template by ID. |
| Delete Universal Content | `deleteUniversalContent` | Delete a template universal content block by ID. Returns 204 No Content on success. |
| Delete Web Feed | `deleteWebFeed` | Delete a web feed by ID. |
| Delete Webhook | `deleteWebhook` | Delete a webhook subscription by ID. |
| Get Account | `getAccount` | Get a single account by ID. |
| Get Accounts | `getAccounts` | Get details for the account(s) associated with the API key, including contact info, timezone, and currency. |
| Get All Universal Content | `getUniversalContents` | List all template universal content blocks in the account. Supports filtering, sorting, and cursor-based pagination. |
| Get Bulk Create Coupon Code Jobs | `getBulkCreateCouponCodeJobs` | List all bulk coupon code creation jobs. |
| Get Bulk Create Coupon Codes Job | `getBulkCreateCouponCodesJob` | Get the status of a specific bulk coupon code creation job. |
| Get Campaign | `getCampaign` | Get a single campaign by ID. |
| Get Campaign Message | `getCampaignMessage` | Get a single campaign message by ID. |
| Get Campaigns | `getCampaigns` | List campaigns. Requires a messages.channel filter (e.g. equals(messages.channel,'email')). Supports sort, include, page[cursor]. |
| Get Catalog Categories | `getCatalogCategories` | List catalog categories. |
| Get Catalog Category | `getCatalogCategory` | Get a single catalog category by ID. |
| Get Catalog Category Bulk Create Job | `getCatalogCategoryBulkCreateJob` | Get the status of a catalog category bulk create job. |
| Get Catalog Category Bulk Delete Job | `getCatalogCategoryBulkDeleteJob` | Get the status of a catalog category bulk delete job. |
| Get Catalog Category Bulk Update Job | `getCatalogCategoryBulkUpdateJob` | Get the status of a catalog category bulk update job. |
| Get Catalog Category Item Relationships | `getCatalogCategoryItemRelationships` | Get IDs of all items in a catalog category. |
| Get Catalog Category Items | `getCatalogCategoryItems` | Get all catalog items in a category. |
| Get Catalog Item | `getCatalogItem` | Get a single catalog item by ID. |
| Get Catalog Item Bulk Create Job | `getCatalogItemBulkCreateJob` | Get the status of a catalog item bulk create job. |
| Get Catalog Item Bulk Delete Job | `getCatalogItemBulkDeleteJob` | Get the status of a catalog item bulk delete job. |
| Get Catalog Item Bulk Update Job | `getCatalogItemBulkUpdateJob` | Get the status of a catalog item bulk update job. |
| Get Catalog Item Categories | `getCatalogItemCategories` | Get all categories linked to a catalog item. |
| Get Catalog Item Category Relationships | `getCatalogItemCategoryRelationships` | Get IDs of all categories linked to a catalog item. |
| Get Catalog Item Variant Relationships | `getCatalogItemVariantRelationships` | Get IDs of all variants linked to a catalog item. |
| Get Catalog Item Variants | `getCatalogItemVariants` | Get all variants linked to a catalog item. |
| Get Catalog Items | `getCatalogItems` | List catalog items. Supports filter, sort, fields, include, page[cursor]. |
| Get Catalog Variant | `getCatalogVariant` | Get a single catalog variant by compound ID. |
| Get Catalog Variant Bulk Create Job | `getCatalogVariantBulkCreateJob` | Get the status of a catalog variant bulk create job. |
| Get Catalog Variant Bulk Delete Job | `getCatalogVariantBulkDeleteJob` | Get the status of a catalog variant bulk delete job. |
| Get Catalog Variant Bulk Update Job | `getCatalogVariantBulkUpdateJob` | Get the status of a catalog variant bulk update job. |
| Get Catalog Variants | `getCatalogVariants` | List catalog item variants. |
| Get Coupon | `getCoupon` | Get a single coupon by ID. |
| Get Coupon Code | `getCouponCode` | Get a specific coupon code by ID. |
| Get Coupon Code IDs For Coupon | `getCouponCodeIdsForCoupon` | Get the relationship references (coupon code IDs) for a given coupon. |
| Get Coupon Codes | `getCouponCodes` | Get all coupon codes, with optional filtering by coupon or profile. |
| Get Coupon Codes For Coupon | `getCouponCodesForCoupon` | Get all coupon codes associated with a specific coupon. |
| Get Coupon For Coupon Code | `getCouponForCouponCode` | Get the coupon associated with a specific coupon code. |
| Get Coupon ID For Coupon Code | `getCouponIdForCouponCode` | Get the relationship reference (coupon ID) for a given coupon code. |
| Get Coupons | `getCoupons` | Get all coupons in the account. |
| Get Data Source | `getDataSource` | Get a data source by ID. |
| Get Data Sources | `getDataSources` | Get all data sources. |
| Get Event | `getEvent` | Get a single event by ID. |
| Get Events | `getEvents` | List/query events. Supports filter, sort, fields, include, page[cursor]. |
| Get Flow | `getFlow` | Get a specific flow by ID. Supports sparse fieldsets and includes. |
| Get Flow Action | `getFlowAction` | Get a specific flow action by ID, including its encoded definition. |
| Get Flow Action For Flow Message | `getFlowActionForFlowMessage` | Get the parent flow action for a specific flow message. |
| Get Flow Action ID For Flow Message | `getFlowActionIdForFlowMessage` | Get the relationship data (ID only) for the parent flow action of a flow message. |
| Get Flow Action Messages | `getFlowActionMessages` | Get all flow messages for a specific flow action, with filtering, sorting, and pagination. |
| Get Flow Action Relationships | `getFlowActionRelationships` | Get the relationship data (IDs only) for all flow actions of a flow. |
| Get Flow Actions | `getFlowActions` | Get all flow actions for a specific flow, with filtering, sorting, and pagination. |
| Get Flow For Flow Action | `getFlowForFlowAction` | Get the parent flow for a specific flow action. |
| Get Flow ID For Flow Action | `getFlowIdForFlowAction` | Get the relationship data (ID only) for the parent flow of a flow action. |
| Get Flow Message | `getFlowMessage` | Get a specific flow message by ID, including its encoded definition. |
| Get Flow Message IDs For Flow Action | `getFlowMessageIdsForFlowAction` | Get the relationship data (IDs only) for all flow messages of a flow action. |
| Get Flow Tag Relationships | `getFlowTagRelationships` | Get the relationship data (IDs only) for all tags of a flow. |
| Get Flow Tags | `getFlowTags` | Get all tags associated with a specific flow. |
| Get Flows Triggered by List | `getListFlowTriggers` | Get all flows where the given list ID is being used as the trigger. |
| Get Flows Triggered by Segment | `getSegmentFlowTriggers` | Get all flows where the given segment ID is being used as the trigger. |
| Get Form | `getForm` | Get a single form by ID. |
| Get Form for Form Version | `getFormForFormVersion` | Get the full parent form resource for a given form version ID. |
| Get Form ID for Form Version | `getFormIdForFormVersion` | Get the relationship data (parent form ID + type) for a form version via the relationships endpoint. |
| Get Form Version | `getFormVersion` | Get a single form version by ID. |
| Get Form Versions | `getFormVersions` | Get all versions for a given form. |
| Get Forms | `getForms` | Get all forms in the account, with optional filtering and pagination. |
| Get IDs for Flows Triggered by List | `getListRelationshipsFlowTriggers` | Get the IDs of all flows where the given list is being used as the trigger. |
| Get IDs for Flows Triggered by Segment | `getSegmentRelationshipsFlowTriggers` | Get the IDs of all flows where the given segment is being used as the trigger. |
| Get Image | `getImage` | Get a single image by ID (GET /api/images/{id}). |
| Get Images | `getImages` | Get all images in an account (GET /api/images). Supports cursor pagination, filtering, sorting, and sparse fieldsets. |
| Get List | `getList` | Get a single list by ID. |
| Get Lists | `getLists` | List all lists. Supports filter, sort, fields[list], include, page[cursor]. |
| Get Metric | `getMetric` | Get a single metric by ID. |
| Get Metric for Event | `getEventMetric` | Get the metric associated with a given event. |
| Get Metrics | `getMetrics` | List all metrics on the account. Supports filter, fields[metric], page[cursor]. |
| Get Profile | `getProfile` | Get a single profile by ID. |
| Get Profile Bulk Import Job | `getProfileBulkImportJob` | Get a specific profile bulk import job by ID. |
| Get Profile Bulk Import Job Errors | `getProfileBulkImportJobErrors` | Get import errors for a profile bulk import job. |
| Get Profile Bulk Import Job Lists | `getProfileBulkImportJobLists` | Get the lists associated with a profile bulk import job. |
| Get Profile Bulk Import Job Profiles | `getProfileBulkImportJobProfiles` | Get the profiles associated with a profile bulk import job. |
| Get Profile Bulk Import Job Relationships Lists | `getProfileBulkImportJobRelationshipsLists` | Get list IDs related to a profile bulk import job. |
| Get Profile Bulk Import Job Relationships Profiles | `getProfileBulkImportJobRelationshipsProfiles` | Get profile IDs related to a profile bulk import job. |
| Get Profile Bulk Import Jobs | `getProfileBulkImportJobs` | Get all profile bulk import jobs. |
| Get Profile Conversation | `getProfileConversation` | Get the conversation associated with a profile. |
| Get Profile for Event | `getEventProfile` | Get the profile associated with a given event. |
| Get Profile IDs for List | `getListRelationshipsProfiles` | Get the profile relationship IDs for a list. |
| Get Profile IDs for Segment | `getSegmentRelationshipsProfiles` | Get all profile membership relationship IDs for the given segment ID. |
| Get Profile Lists | `getProfileLists` | Get all lists that a profile is in. |
| Get Profile Push Tokens | `getProfilePushTokens` | Get push tokens associated with a specific profile. |
| Get Profile Relationships Lists | `getProfileRelationshipsLists` | Get list IDs that a profile belongs to (relationships endpoint). |
| Get Profile Relationships Push Tokens | `getProfileRelationshipsPushTokens` | Get push token IDs associated with a profile (relationships endpoint). |
| Get Profile Relationships Segments | `getProfileRelationshipsSegments` | Get segment IDs that a profile belongs to (relationships endpoint). |
| Get Profile Segments | `getProfileSegments` | Get all segments that a profile is in. |
| Get Profile Suppression Bulk Create Job | `getProfileSuppressionBulkCreateJob` | Get a specific profile suppression bulk create job by ID. |
| Get Profile Suppression Bulk Create Jobs | `getProfileSuppressionBulkCreateJobs` | Get all profile suppression bulk create jobs. |
| Get Profile Suppression Bulk Delete Job | `getProfileSuppressionBulkDeleteJob` | Get a specific profile suppression bulk delete (unsuppress) job by ID. |
| Get Profile Suppression Bulk Delete Jobs | `getProfileSuppressionBulkDeleteJobs` | Get all profile suppression bulk delete (unsuppress) jobs. |
| Get Profiles | `getProfiles` | List/query profiles. Supports JSON:API filter, sort, fields, include, additional-fields[profile], and page[cursor]/page[size]. |
| Get Profiles for List | `getListProfiles` | Get all profiles that are members of a given list. |
| Get Profiles for Segment | `getSegmentProfiles` | Get all profiles in a given segment. |
| Get Push Token | `getPushToken` | Get a specific push token by ID. |
| Get Push Token Profile | `getPushTokenProfile` | Get the profile associated with a push token. |
| Get Push Token Relationships Profile | `getPushTokenRelationshipsProfile` | Get the profile ID associated with a push token (relationships endpoint). |
| Get Push Tokens | `getPushTokens` | Get all push notification tokens registered in the account. |
| Get Review | `getReview` | Get a single product review by its ID. |
| Get Reviews | `getReviews` | Get all product reviews. Supports filtering, sorting, and pagination via JSON:API query params. |
| Get Segment | `getSegment` | Get a single segment by ID. |
| Get Segments | `getSegments` | List all segments. Supports filter, sort, fields[segment], include, page[cursor]. |
| Get Tag | `getTag` | Get a single tag by ID. |
| Get Tag Group | `getTagGroup` | Get a tag group by ID. |
| Get Tag Group for Tag | `getTagTagGroup` | Get the tag group resource associated with a given tag. |
| Get Tag Groups | `getTagGroups` | List all tag groups. |
| Get Tag IDs for List | `getListRelationshipsTags` | Return all tag relationship IDs associated with the given list ID. |
| Get Tag IDs for Segment | `getSegmentRelationshipsTags` | Return all tag relationship IDs associated with the given segment ID. |
| Get Tag IDs for Tag Group | `getTagGroupRelationshipsTags` | Get the IDs of all tags associated with a tag group. |
| Get Tag Relationships Campaigns | `getTagRelationshipsCampaigns` | Get the IDs of all campaigns associated with a given tag. |
| Get Tag Relationships Flows | `getTagRelationshipsFlows` | Get the IDs of all flows associated with a given tag. |
| Get Tag Relationships Lists | `getTagRelationshipsLists` | Get the IDs of all lists associated with a given tag. |
| Get Tag Relationships Segments | `getTagRelationshipsSegments` | Get the IDs of all segments associated with a given tag. |
| Get Tag Relationships Tag Group | `getTagRelationshipsTagGroup` | Get the ID of the tag group associated with a given tag. |
| Get Tags | `getTags` | List all tags. Supports filter, sort, fields[tag], include, page[cursor]. |
| Get Tags for List | `getListTags` | Get tags associated with a list. |
| Get Tags for Segment | `getSegmentTags` | Get tags associated with a segment. |
| Get Tags for Tag Group | `getTagGroupTags` | Get all tags associated with a tag group. |
| Get Template | `getTemplate` | Get a single template by ID. |
| Get Template For Flow Message | `getTemplateForFlowMessage` | Get the template associated with a specific flow message. |
| Get Template ID For Flow Message | `getTemplateIdForFlowMessage` | Get the relationship data (ID only) for the template of a flow message. |
| Get Templates | `getTemplates` | List all email templates. Supports filter, sort, fields[template], page[cursor]. |
| Get Tracking Setting | `getTrackingSetting` | Get a tracking setting by ID (account ID). |
| Get Tracking Settings | `getTrackingSettings` | Get all tracking settings for the account. |
| Get Universal Content | `getUniversalContent` | Get a single template universal content block by ID. |
| Get Version IDs for Form | `getFormVersionIds` | Get the relationship IDs (id + type only) of all versions for a given form via the relationships endpoint. |
| Get Web Feed | `getWebFeed` | Get a web feed by ID. |
| Get Web Feeds | `getWebFeeds` | Get all web feeds for the account. |
| Get Webhook | `getWebhook` | Get a single webhook subscription by ID. |
| Get Webhook Topic | `getWebhookTopic` | Get a single webhook topic by ID. |
| Get Webhook Topics | `getWebhookTopics` | List all available webhook topics (event types) that can be subscribed to. |
| Get Webhooks | `getWebhooks` | List all system webhook subscriptions (GET /api/webhooks). Supports include=webhook-topics for topic details. |
| Import Profile (Upsert) | `importProfile` | Create or update a profile. Identifies profiles by email, phone_number, or external_id. Returns 200 if updated, 201 if created. |
| List Catalog Category Bulk Create Jobs | `listCatalogCategoryBulkCreateJobs` | List all catalog category bulk create jobs. |
| List Catalog Category Bulk Delete Jobs | `listCatalogCategoryBulkDeleteJobs` | List all catalog category bulk delete jobs. |
| List Catalog Category Bulk Update Jobs | `listCatalogCategoryBulkUpdateJobs` | List all catalog category bulk update jobs. |
| List Catalog Item Bulk Create Jobs | `listCatalogItemBulkCreateJobs` | List all catalog item bulk create jobs. |
| List Catalog Item Bulk Delete Jobs | `listCatalogItemBulkDeleteJobs` | List all catalog item bulk delete jobs. |
| List Catalog Item Bulk Update Jobs | `listCatalogItemBulkUpdateJobs` | List all catalog item bulk update jobs. |
| List Catalog Variant Bulk Create Jobs | `listCatalogVariantBulkCreateJobs` | List all catalog variant bulk create jobs. |
| List Catalog Variant Bulk Delete Jobs | `listCatalogVariantBulkDeleteJobs` | List all catalog variant bulk delete jobs. |
| List Catalog Variant Bulk Update Jobs | `listCatalogVariantBulkUpdateJobs` | List all catalog variant bulk update jobs. |
| List Flows | `getFlows` | Get all flows in the account. Supports pagination, filtering, sorting, and sparse fieldsets. |
| Merge Profiles | `mergeProfiles` | Merge a source profile into a destination profile. |
| Query Flow Series Report | `queryFlowSeriesReport` | Query time-series flow metrics (daily/hourly/weekly/monthly) for opens, clicks, conversions, etc. |
| Query Flow Values Report | `queryFlowValuesReport` | Query aggregated flow metric values (opens, clicks, conversions, revenue, etc.) for a given timeframe. |
| Query Form Series Report | `queryFormSeriesReport` | Query form analytics as a time series. Returns statistics aggregated by the chosen interval (daily/weekly/monthly/hourly) within the given timeframe. |
| Query Form Values Report | `queryFormValuesReport` | Query form analytics as aggregate totals for a given timeframe, optionally grouped by dimensions. |
| Query Metric Aggregates | `queryMetricAggregates` | Query aggregated metric data (counts, sums) grouped/filtered over time. |
| Query Segment Series | `querySegmentSeries` | Returns the requested segment analytics series data over time intervals. |
| Query Segment Values | `querySegmentValues` | Returns the requested segment analytics values data (total_members, members_added, members_removed, net_members_changed). |
| Remove Catalog Category Item Relationships | `removeCatalogCategoryItemRelationships` | Remove specific items from a catalog category. |
| Remove Catalog Item Category Relationships | `removeCatalogItemCategoryRelationships` | Remove specific category relationships from a catalog item. |
| Remove Profiles from List | `removeProfilesFromList` | Remove one or more profiles from a list (relationship delete). |
| Remove Tag from Campaigns | `removeTagFromCampaigns` | Disassociate a tag from one or more campaigns. |
| Remove Tag from Flows | `removeTagFromFlows` | Disassociate a tag from one or more flows. |
| Remove Tag from Lists | `removeTagFromLists` | Disassociate a tag from one or more lists. |
| Remove Tag from Segments | `removeTagFromSegments` | Disassociate a tag from one or more segments. |
| Render Template | `renderTemplate` | Render a template with example context data to preview the output HTML/text. |
| Request Profile Deletion | `requestProfileDeletion` | Submit a data privacy deletion request for a profile by email, phone number, or profile ID (GDPR/CCPA). |
| Subscribe Profiles | `subscribeProfiles` | Bulk subscribe profiles to email and/or SMS marketing for a given list (creates a subscription job). |
| Suppress Profiles | `suppressProfiles` | Bulk suppress profiles from receiving email marketing for a given list (or globally). |
| Tag Campaigns | `tagCampaigns` | Associate a tag with one or more campaigns. Pass an array of campaign data objects. |
| Tag Flows | `tagFlows` | Associate a tag with one or more flows. Pass an array of flow data objects. |
| Tag Segments | `tagSegments` | Associate a tag with one or more segments. Pass an array of segment data objects. |
| Unsubscribe Profiles | `unsubscribeProfiles` | Bulk unsubscribe profiles from email and/or SMS marketing for a given list. |
| Unsuppress Profiles | `unsuppressProfiles` | Bulk remove email marketing suppressions for profiles. |
| Update Campaign | `updateCampaign` | Update a campaign by ID (name, audiences, send strategy). |
| Update Campaign Message | `updateCampaignMessage` | Update a campaign message's content/label by ID. |
| Update Catalog Category | `updateCatalogCategory` | Update a catalog category's attributes by ID. |
| Update Catalog Category Item Relationships | `updateCatalogCategoryItemRelationships` | Replace all item relationships of a catalog category. |
| Update Catalog Item | `updateCatalogItem` | Update a catalog item by ID. |
| Update Catalog Item Category Relationships | `updateCatalogItemCategoryRelationships` | Replace all category relationships of a catalog item. |
| Update Catalog Variant | `updateCatalogVariant` | Update an existing catalog variant. |
| Update Coupon | `updateCoupon` | Update an existing coupon's attributes by ID. |
| Update Coupon Code | `updateCouponCode` | Update the status or expiry of a coupon code. |
| Update Flow | `updateFlowStatus` | Update the status of a flow (draft, manual, or live). |
| Update Flow Action | `updateFlowAction` | Update a flow action definition by ID. |
| Update Image | `updateImage` | Update an image's name or hidden flag by ID (PATCH /api/images/{id}). Provide the fields to update. |
| Update List | `updateList` | Update a list's name by ID. |
| Update Profile | `updateProfile` | Update an existing profile by ID (PATCH). Pass the attributes to change. |
| Update Review | `updateReview` | Update the status of a review (publish, reject, feature, unpublish, or mark pending). |
| Update Segment | `updateSegment` | Update a segment's name and/or definition by ID. |
| Update Tag | `updateTag` | Update a tag's name by ID. |
| Update Tag Group | `updateTagGroup` | Update a tag group's name. |
| Update Template | `updateTemplate` | Update a template's name and/or HTML by ID. |
| Update Tracking Setting | `updateTrackingSetting` | Update tracking settings for the account. Patch auto_add_parameters and/or UTM parameter configs. |
| Update Universal Content | `updateUniversalContent` | Update an existing template universal content block by ID. |
| Update Web Feed | `updateWebFeed` | Update a web feed. All attributes are optional. |
| Update Webhook | `updateWebhook` | Update a webhook subscription by ID (PATCH /api/webhooks/{id}). All attribute fields and topics are optional. |
| Upload Image From File | `uploadImageFromFile` | Upload an image from a binary file (POST /api/image-upload, multipart/form-data). NOTE: blocked — fastn does not support multipart/form-data uploads. Use uploadImageFromUrl to import from a URL instead. |
| Upload Image From URL | `uploadImageFromUrl` | Import an image into Klaviyo from a URL or data URI (POST /api/images). Supported formats: jpeg, png, gif. Max 5MB. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Profile Added To List | `profile.added_to_list` | A profile is added to a list. |
| Profile Removed From List | `profile.removed_from_list` | A profile is removed from a list. |
| Profile Subscribed To Email Marketing | `profile.subscribed_to_email_marketing` | A profile opts in / is subscribed to email marketing. |
| Profile Subscribed To SMS Marketing | `profile.subscribed_to_sms_marketing` | A profile opts in / is subscribed to SMS marketing. |
| Profile Suppressed | `profile.suppressed` | A profile is suppressed (bounce, spam complaint, manual suppression). |
| Profile Unsubscribed From Email Marketing | `profile.unsubscribed_from_email_marketing` | A profile opts out / is unsubscribed from email marketing. |
| Profile Unsubscribed From SMS Marketing | `profile.unsubscribed_from_sms_marketing` | A profile opts out / is unsubscribed from SMS marketing. |
| Profile Unsuppressed | `profile.unsuppressed` | A previously suppressed profile is unsuppressed and can receive email again. |
