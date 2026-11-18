---
description: "Kit (formerly ConvertKit) email marketing platform for creators."
---

# Kit

Kit (formerly ConvertKit) email marketing platform for creators. Manage subscribers, tags, custom fields, broadcasts, forms, sequences, purchases, segments, snippets, email templates, account stats, and webhooks via the Kit V4 API.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [kit.com](https://kit.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 72 |
| **Events** | 0 |
| **Slug** | `kit` |

## Use it

Add Kit from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.kit.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Subscriber to Form | `addSubscriberToForm` | Adds an existing subscriber to a form by subscriber id. The subscriber must already exist. |
| Add Subscriber to Form by Email Address | `addSubscriberToFormByEmail` | Adds an existing subscriber to a form by email address. The subscriber must already exist. Double opt-in forms trigger an incentive email. |
| Add Subscriber to Sequence | `addSubscriberToSequence` | Adds an existing subscriber to a sequence by subscriber id. The subscriber must already exist. |
| Add Subscriber to Sequence by Email Address | `addSubscriberToSequenceByEmail` | Adds an existing subscriber to a sequence by email address. The subscriber must already exist. |
| Bulk Create Custom Fields | `bulkCreateCustomFields` | Creates up to 100 custom fields in one asynchronous request. Provide an optional callback_url to receive completion results. |
| Bulk Create Subscribers | `bulkCreateSubscribers` | Creates up to 100 subscribers in one asynchronous request. Provide an optional callback_url to receive completion results. |
| Bulk Create Tags | `bulkCreateTags` | Creates up to 100 tags in one asynchronous request. Provide an optional callback_url to receive completion results. |
| Bulk Delete Tags | `bulkDeleteTags` | Deletes up to 100 tags in one asynchronous request by id. Provide an optional callback_url to receive completion results. |
| Bulk Remove Tags from Subscribers | `bulkRemoveTagsFromSubscribers` | Removes tags from subscribers in bulk. Each tagging pairs a tag_id with a subscriber_id. |
| Bulk Tag Subscribers | `bulkTagSubscribers` | Applies tags to subscribers in bulk. Each tagging pairs a tag_id with a subscriber_id. Subscribers must already exist. |
| Bulk Update Subscriber Custom Field Values | `bulkUpdateSubscriberCustomFields` | Creates or updates custom field values for many subscribers in one request. Each entry pairs a subscriber_id with a subscriber_custom_field_id and value. Requires OAuth authentication. |
| Create Broadcast | `createBroadcast` | Creates a broadcast. Leave send_at null to save a draft, set public true to publish to the web, or provide send_at to schedule sending. |
| Create Custom Field | `createCustomField` | Creates a custom field with a unique label. Kit generates the key and name automatically from the label. |
| Create Purchase | `createPurchase` | Records a purchase against a subscriber identified by email address. If no subscriber with that email exists, one is created. Syncs order data into Kit. |
| Create Sequence | `createSequence` | Creates an empty sequence — the container that holds sequence emails. Populate it afterward with Create Sequence Email. |
| Create Sequence Email | `createSequenceEmail` | Adds one email to a sequence. Position, delay_value, delay_unit, and send_days control when it fires relative to the subscriber's journey. |
| Create Snippet | `createSnippet` | Creates a reusable inline snippet with a name and Liquid-enabled text content. |
| Create Subscriber | `createSubscriber` | Creates or upserts a subscriber by email address. If the email exists, updates the first name; otherwise creates a new subscriber in the given state. |
| Create Tag | `createTag` | Creates a tag with the given name. Idempotent on name (case-insensitive): returns the existing tag if one already matches. |
| Create Webhook | `createWebhook` | Registers a webhook that POSTs subscriber data to target_url when the given event fires. Some events require an extra id (form_id, tag_id, sequence_id, product_id, initiator_value, or custom_field_id) in the event object. |
| Delete Broadcast | `deleteBroadcast` | Permanently deletes a draft or scheduled broadcast. This is a hard delete and returns 204 No Content on success. |
| Delete Custom Field | `deleteCustomField` | Deletes a custom field and removes all of its data from every subscriber. Returns 204 No Content on success. |
| Delete Sequence | `deleteSequence` | Soft-deletes a sequence, removing it from active delivery immediately. Returns 204 No Content on success. |
| Delete Sequence Email | `deleteSequenceEmail` | Permanently removes one email from a sequence. Returns 204 No Content on success. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook and stops all future deliveries of its subscribed events. Returns 204 No Content on success. |
| Filter Subscribers | `filterSubscribers` | Returns subscribers matching an advanced filter built from engagement, sign-up date, state, tags, and custom field conditions. |
| Get Broadcast | `getBroadcast` | Returns a single broadcast's full record: subject, content, preview text, targeting, template, schedule, and web-publishing details. |
| Get Creator Profile | `getCreatorProfile` | Returns the account's public-facing Creator Profile: display name, byline, bio, image URL, and public profile URL. |
| Get Current Account | `getAccount` | Returns the authenticated Kit account and user, including account id, name, plan type, primary email address, timezone, and sending addresses. |
| Get Email Stats | `getEmailStats` | Returns account-level email performance for the last 90 days: sent, opened, and clicked counts plus open, click, unsubscribe, and bounce rates. |
| Get Growth Stats | `getGrowthStats` | Returns subscriber growth stats for a time period (defaults to the last 90 days): cancellations, new and net-new subscribers, and total subscribers. |
| Get Link Clicks for a Broadcast | `getBroadcastClicks` | Returns the link-click breakdown for a single broadcast. |
| Get Post | `getPost` | Returns a single post's full record, including its content HTML, status, slug, SEO fields, thumbnail, is_paid flag, and public URL. |
| Get Purchase | `getPurchase` | Returns a single purchase's details including buyer, monetary breakdown, transaction time, and purchased products. |
| Get Sequence | `getSequence` | Fetches a single sequence by id with its schedule, active/repeat/hold flags, sending address, template, and excluded sources. |
| Get Sequence Email | `getSequenceEmail` | Fetches a single sequence email by id, always including its full content. |
| Get Snippet | `getSnippet` | Fetches a single snippet by id, always including its full content and document. |
| Get Stats for a Broadcast | `getBroadcastStats` | Returns performance stats for a single broadcast (recipients, opens, clicks, unsubscribes, bounces, and rates). |
| Get Stats for a List of Broadcasts | `listBroadcastStats` | Returns a cursor-paginated list of broadcasts each with its stats, subject, and send time. Filter by status and sent date range. |
| Get Subscriber | `getSubscriber` | Returns a single subscriber's record by id: first name, email address, state, creation date, and custom field values. |
| List Brand Colors | `listColors` | Returns the account's saved brand color palette as an array of up to 10 hex codes. |
| List Broadcasts | `listBroadcasts` | Returns a cursor-paginated list of broadcasts with content, targeting, template, and web-publishing settings. Filter by lifecycle status and sent date range. |
| List Custom Fields | `listCustomFields` | Returns a cursor-paginated list of the account's custom fields with their id, name, key, and label. |
| List Email Templates | `listEmailTemplates` | Returns a cursor-paginated list of the account's email templates with each template's id, name, is_default flag, and category. |
| List Forms | `listForms` | Returns a cursor-paginated list of forms and landing pages. Filter with type=embed for forms or type=hosted for landing pages, and status to widen beyond active. |
| List Posts | `listPosts` | Returns a cursor-paginated list of the account's posts (content published to the creator's Kit site and/or sent by email). |
| List Purchases | `listPurchases` | Returns a cursor-paginated list of purchases recorded in the account, typically imported from e-commerce platforms. |
| List Segments | `listSegments` | Returns a cursor-paginated list of all segments in the account with their id, name, and creation date. |
| List Sequence Emails | `listSequenceEmails` | Returns every email inside a sequence, ordered by position, with timing, publish state, and metadata. |
| List Sequences | `listSequences` | Returns every sequence on the account with schedule settings, active/repeat/hold flags, email and subscriber counts. |
| List Snippets | `listSnippets` | Returns every snippet on the account. |
| List Stats for a Subscriber | `getSubscriberStats` | Returns email engagement stats for a single subscriber, optionally limited to emails sent within a date range. |
| List Subscribers | `listSubscribers` | Returns a cursor-paginated list of subscribers. Filter by status, email address, and creation/update date ranges, and sort with sort_field/sort_order. |
| List Subscribers for a Form | `listFormSubscribers` | Returns a cursor-paginated list of subscribers who joined through or were added to a form. Filter by status and date ranges. |
| List Subscribers for a Sequence | `listSequenceSubscribers` | Returns a cursor-paginated list of subscribers in a sequence, each with an added_at timestamp. Filter by status and date ranges. |
| List Subscribers for a Tag | `listTagSubscribers` | Returns a cursor-paginated list of subscribers who have a given tag. Filter by status and tagged/created date ranges. |
| List Tags | `listTags` | Returns a cursor-paginated list of all tags with their id, name, and creation date. Add include=subscriber_count to embed each tag's subscriber count. |
| List Tags for a Subscriber | `listSubscriberTags` | Returns a cursor-paginated list of the tags currently applied to a subscriber, including when each was applied. |
| List Webhooks | `listWebhooks` | Returns a cursor-paginated list of the account's webhooks with their id, event, and target URL. |
| Remove Tag from Subscriber | `removeTagFromSubscriber` | Removes a tag from a subscriber by subscriber id. The subscriber and their other tags are retained. |
| Remove Tag from Subscriber by Email Address | `removeTagFromSubscriberByEmail` | Removes a tag from a subscriber identified by email address. The subscriber and their other tags are retained. |
| Tag a Subscriber | `tagSubscriber` | Applies a tag to an existing subscriber identified by subscriber id. The subscriber must already exist. |
| Tag a Subscriber by Email Address | `tagSubscriberByEmail` | Applies a tag to an existing subscriber identified by email address. The subscriber must already exist. |
| Unsubscribe Subscriber | `unsubscribeSubscriber` | Unsubscribes a subscriber from all future emails, moving them to the cancelled state. The record, history, and tags are retained. |
| Update Brand Colors | `updateColors` | Replaces the account's brand color palette with the provided array of up to 10 hex codes and returns the updated list. |
| Update Broadcast | `updateBroadcast` | Updates an existing broadcast. Only fields included in the request change. Set public true and provide send_at to schedule sending. |
| Update Custom Field | `updateCustomField` | Updates a custom field's label. The key changes to match the new label but the name is preserved. |
| Update Sequence | `updateSequence` | Updates sequence settings such as name, sending address, schedule, template, and active/repeat/hold flags. Only fields included change. |
| Update Sequence Email | `updateSequenceEmail` | Updates any field on a sequence email. Only fields included in the request change; everything else is preserved. |
| Update Snippet | `updateSnippet` | Renames a snippet or replaces its inline content. Changes apply on the next send of any email referencing the snippet. |
| Update Subscriber | `updateSubscriber` | Updates a subscriber's first name, email address, and custom field values. Only fields included in the request change. |
| Update Tag Name | `updateTag` | Renames a tag. The tag keeps its id and all subscribers; only the name changes. |
