---
description: "Gist is an all-in-one customer engagement platform covering live chat, email marketing, knowledge base and marketing automation."
hidden: true
---

# Gist

Gist is an all-in-one customer engagement platform covering live chat, email marketing, knowledge base and marketing automation. This connector covers the documented Gist API: contacts and batch contact imports, tags, segments, custom events, forms and form submissions, campaigns and subscriptions, subscription types, the conversations inbox with messages, assignment, priority and tagging, teams and teammates, knowledge base articles and collections, workspace metadata, and the ecommerce surface of stores, customers, products, variants, categories, carts and orders.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Authentication** | Credentials you enter |
| **Actions** | 75 |
| **Events** | 0 |
| **Slug** | `gist` |

## Use it

Add Gist from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.gist.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Assign Conversation | `assignConversation` | Assigns a conversation to a teammate or a team, or clears the assignment. |
| Create Article | `createArticle` | Creates a knowledge base article, with one content block per locale. |
| Create Conversation | `createConversation` | Starts a conversation in the workspace inbox on a contact's behalf. |
| Create Ecommerce Customer | `createEcommerceCustomer` | Adds a customer to a connected ecommerce store. |
| Create Ecommerce Order | `createEcommerceOrder` | Create an order in an ecommerce store (POST /ecommerce/stores/{store_id}/orders). Body keys follow the Gist API reference "Create an order": order_id, customer_id, currency_code, order_total, discount_total, tax_total, shipping_total, financial_status, fulfillment_status, order_url, tracking_number, tracking_carrier, tracking_url, processed_at, billing_address, shipping_address, line_items. Orders appear on the contact's activity timeline; financial_status transitions generate tracking events. |
| Create Ecommerce Product | `createEcommerceProduct` | Adds a product, together with its variants, to a connected ecommerce store. |
| Create Ecommerce Product Category | `createEcommerceProductCategory` | Adds a product category to a connected ecommerce store. |
| Create Ecommerce Product Variant | `createEcommerceProductVariant` | Adds a purchasable variant to a product in a connected ecommerce store. |
| Create Ecommerce Store | `createEcommerceStore` | Connects an ecommerce store to the workspace so its customers, products and orders can be synced. |
| Create Or Update Cart | `createOrUpdateCart` | Create or update the cart of an ecommerce customer (POST /ecommerce/stores/{store_id}/customers/{customer_id}/cart). Body keys follow the Gist API reference "Create or update a cart": checkout_url, currency_code, order_total, discount_total, line_items. |
| Create Or Update Collection | `createOrUpdateCollection` | Creates a knowledge base collection, or updates the existing one when an identifier is supplied. Content is supplied per locale. |
| Create Or Update Contact | `createOrUpdateContact` | Creates a contact, or updates the existing one when the email address already exists. Gist treats the email address as the primary identifier and de-duplicates on it. |
| Create Or Update Contacts In Batch | `createOrUpdateContactsBatch` | Creates or updates many contacts in one request and returns a job the batch is processed under. |
| Delete Article | `deleteArticle` | Permanently deletes a knowledge base article. |
| Delete Cart | `deleteCart` | Deletes the open cart recorded for a customer, for example once the order has been placed. |
| Delete Collection | `deleteCollection` | Permanently deletes a knowledge base collection. |
| Delete Contact | `deleteContact` | Permanently deletes a contact and the activity recorded against it. |
| Delete Conversation | `deleteConversation` | Permanently deletes a conversation and its messages from the inbox. |
| Delete Tag | `deleteTag` | Permanently deletes a tag and removes it from every contact carrying it. |
| Get Article | `getArticle` | Retrieves a single knowledge base article and all of its translations. |
| Get Campaign | `getCampaign` | Retrieves a single campaign and its engagement statistics by identifier. |
| Get Collection | `getCollection` | Retrieves a single knowledge base collection and all of its translations. |
| Get Contact | `getContact` | Retrieves a single contact by its Gist identifier. |
| Get Contacts Batch Status | `getContactsBatchStatus` | Retrieves the progress of a queued contact batch import, including how many records succeeded and failed. |
| Get Conversation | `getConversation` | Retrieves a single conversation and its metadata by identifier. |
| Get Conversation Counts | `getConversationCounts` | Retrieves workspace-wide conversation counts broken down by state. |
| Get Ecommerce Customer | `getEcommerceCustomer` | Retrieves a single ecommerce customer within a store. |
| Get Ecommerce Product | `getEcommerceProduct` | Retrieves a single product within a connected ecommerce store. |
| Get Ecommerce Product Category | `getEcommerceProductCategory` | Retrieves a single product category within a connected ecommerce store. |
| Get Ecommerce Product Variant | `getEcommerceProductVariant` | Retrieves a single product variant within a connected ecommerce store. |
| Get Ecommerce Store | `getEcommerceStore` | Retrieves a single connected ecommerce store by identifier. |
| Get Form | `getForm` | Retrieves a single form and its field definitions. The form id appears in the Gist app URL when editing the embedded form. |
| Get Knowledge Base Settings | `getKnowledgeBaseSettings` | Retrieves the knowledge base configuration, including its domain, visibility and language settings. |
| Get Segment | `getSegment` | Retrieves a single contact segment by its identifier. |
| Get Subscription Type | `getSubscriptionType` | Retrieves a single subscription type by its identifier. |
| Get Team | `getTeam` | Retrieves a single team and its members by identifier. |
| Get Team Conversation Counts | `getTeamConversationCounts` | Retrieves conversation counts broken down by team. |
| Get Teammate | `getTeammate` | Retrieves a single teammate by identifier. |
| Get Teammate Conversation Counts | `getTeammateConversationCounts` | Retrieves conversation counts broken down by teammate. |
| Get Workspace Metadata | `getWorkspaceMeta` | Retrieves the workspace the access token belongs to, together with the token type and expiry. |
| List Articles | `listArticles` | Retrieves the knowledge base articles in the workspace, one page at a time. |
| List Campaigns | `listCampaigns` | Retrieves the email campaigns in the workspace, one page at a time. |
| List Collections | `listCollections` | Retrieves the knowledge base collections in the workspace, one page at a time. |
| List Contacts | `listContacts` | Retrieves the contacts in the workspace, optionally narrowed to users or leads, one page at a time. |
| List Conversation Messages | `listConversationMessages` | Retrieves every message exchanged within a conversation. |
| List Conversations | `listConversations` | Retrieves the conversations in the workspace inbox, one page at a time. |
| List Ecommerce Stores | `listEcommerceStores` | Retrieves the ecommerce stores connected to the workspace. |
| List Events | `listEvents` | Retrieves the event names recorded in the workspace, one page at a time. |
| List Form Submissions | `listFormSubmissions` | Retrieves the submissions received by a form, including the field values each visitor supplied. |
| List Forms | `listForms` | Retrieves the forms defined in the workspace, one page at a time. |
| List Segments | `listSegments` | Retrieves the contact segments defined in the workspace, one page at a time. |
| List Subscription Types | `listSubscriptionTypes` | Retrieves the subscription types contacts can opt into from the preference centre. |
| List Tags | `listTags` | Retrieves the tags defined in the workspace, one page at a time. |
| List Teammates | `listTeammates` | Retrieves the teammates with access to the workspace. |
| List Teams | `listTeams` | Retrieves the teams configured in the workspace. |
| Prioritize Conversation | `prioritizeConversation` | Marks a conversation as a priority, or clears the priority flag. |
| Reply To Conversation | `replyToConversation` | Adds a reply or an internal note to a conversation. A reply is delivered to the contact, so send one only to a recipient who expects it. |
| Search Articles | `searchArticles` | Searches knowledge base articles by free text within a locale. |
| Search Conversations | `searchConversations` | Search conversations (POST /conversations/search). The body carries filter_query: an array of clause groups, each with a criteria array of {key, operator, value} conditions (e.g. key contact.id, teammate_assigned_id, channel; operators =, IN, NIN). Groups are ORed, criteria within a group are ANDed. Optional query params order (asc\|desc), order_by (created_at\|updated_at\|waiting_longest), status (all\|open\|closed\|snoozed) and page control ordering and pagination. |
| Set Contact Subscription | `setContactSubscription` | Opts a contact into or out of a subscription type. |
| Subscribe Contact To Campaign | `subscribeContactToCampaign` | Subscribes a contact to a campaign, which starts delivering that campaign's emails to them. |
| Subscribe Contact To Form | `subscribeContactToForm` | Submits a form on a contact's behalf, which creates or updates the contact and triggers whatever follow-up the form is configured to send. |
| Tag Conversation | `tagConversation` | Applies one or more tags to a conversation. POST https://api.getgist.com/conversations/{conversation_id}/tags with a JSON body carrying tags (a comma-separated string of tag NAMES, required) and an optional message_id; if message_id is omitted the tag is applied to the last message of the conversation. Per the current Gist API reference, section "Tag a conversation" (https://developers.getgist.com/api/). Fixed 2026-09-03: bodyTemplate was null, so nothing at all was sent and Gist answered 422 internal_error. Gist takes tag NAMES here, not a tag id - the tag is created if it does not exist. |
| Tag Or Untag Contacts | `tagContacts` | Creates a tag when it does not yet exist and applies it to, or removes it from, a set of contacts. Set untag on a contact entry to remove the tag instead of applying it. Gist recommends no more than fifty contacts per request. |
| Track Event | `trackEvent` | Records a custom event against a contact, which can then drive segments, campaigns and workflows. |
| Unsubscribe Contact From Campaign | `unsubscribeContactFromCampaign` | Unsubscribes a contact from a campaign so they stop receiving its emails. |
| Untag Conversation | `untagConversation` | Removes a tag from a conversation. DELETE https://api.getgist.com/conversations/{conversation_id}/tags with a JSON body carrying tag_id (required) and an optional message_id; if message_id is omitted the tag is removed from every message of the conversation. Per the current Gist API reference, section "Untag a conversation" (https://developers.getgist.com/api/). Fixed 2026-09-03: the bodyTemplate was the hardcoded string "{}", so the tag id was discarded and Gist answered 422 internal_error because no tag was named. |
| Update Article | `updateArticle` | Updates a knowledge base article, including its collection placement and per-locale content. |
| Update Conversation | `updateConversation` | Updates a conversation, for example to open, close or snooze it. |
| Update Ecommerce Customer | `updateEcommerceCustomer` | Updates a customer within a connected ecommerce store. |
| Update Ecommerce Order | `updateEcommerceOrder` | Update an existing order in an ecommerce store (PATCH /ecommerce/stores/{store_id}/orders/{order_id}). Send only the fields to change; body keys follow the Gist API reference "Update an order". |
| Update Ecommerce Product | `updateEcommerceProduct` | Updates a product within a connected ecommerce store. |
| Update Ecommerce Product Category | `updateEcommerceProductCategory` | Updates a product category within a connected ecommerce store. |
| Update Ecommerce Product Variant | `updateEcommerceProductVariant` | Updates a product variant within a connected ecommerce store. |
| Update Ecommerce Store | `updateEcommerceStore` | Updates the details of a connected ecommerce store. |
