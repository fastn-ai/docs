---
description: "eSputnik, now branded Yespo, is an omnichannel marketing automation platform for Email, SMS, Web Push, Mobile Push, Viber, Telegram and App Inbox campaigns."
hidden: true
---

# eSputnik (Yespo)

<img src="../../.gitbook/assets/connectors/esputnik.png" alt="eSputnik (Yespo) logo" width="64">

eSputnik, now branded Yespo, is an omnichannel marketing automation platform for Email, SMS, Web Push, Mobile Push, Viber, Telegram and App Inbox campaigns. This connector wraps the full Yespo REST API v1/v2/v3: contact and segment management, message templates for every channel, broadcasts and transactional sends, orders and behavioural events, promo codes, product feeds, site and web-push domains, account balance and billing history.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [yespo.io](https://yespo.io) |
| **Authentication** | Basic auth |
| **Slug** | `esputnik` |

## Use it

Add eSputnik (Yespo) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.esputnik.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Application Tokens | `addApplicationTokens` | Registers Telegram bot tokens against contacts for an application, in batches of up to 3000 per request. Each token is tied to a contact by contact id, external customer id, phone or email. |
| Add Emails To Unsubscribed List | `addEmailsToUnsubscribed` | Adds email addresses to the organization's unsubscribed list, so no further bulk campaigns are sent to them. |
| Add Or Update App Inbox Message Translation | `upsertAppInboxMessageTranslation` | Adds or replaces a language version of a base App Inbox message. The language is an ISO 639-1 code and the full message content for that language must be supplied. |
| Add Or Update Contact | `addContact` | Creates a contact or updates an existing one in real time. The contact is matched on the internal contact id, the external customer id or a media channel value. At least one media channel must be supplied. Returns the contact id. |
| Add Or Update Contacts In Bulk | `bulkUpdateContacts` | Adds or updates up to 3000 contacts in one asynchronous import. Contacts are matched on the field named by Dedupe On, which is itself never updated; when a contact carries an external customer id that is used instead. Returns an async session id to poll with Get Import Status. |
| Add Or Update Email Message Translation | `upsertEmailMessageTranslation` | Adds or replaces a language version of a base Email message. The language is an ISO 639-1 code and the full message content for that language must be supplied. From is always required here, even for templates, and must exactly match an existing Email interface from List Email Interfaces. |
| Add Or Update Mobile Push Message Translation | `upsertMobilePushMessageTranslation` | Adds or replaces a language version of a base Mobile Push message. The language is an ISO 639-1 code and the full message content for that language must be supplied. |
| Add Or Update SMS Message Translation | `upsertSmsMessageTranslation` | Adds or replaces a language version of a base SMS message. The language is an ISO 639-1 code and the full message content for that language must be supplied. |
| Add Or Update Telegram Message Translation | `upsertTelegramMessageTranslation` | Adds or replaces a language version of a base Telegram bot message. The language is an ISO 639-1 code and the full message content for that language must be supplied. |
| Add Or Update Viber Message Translation | `upsertViberMessageTranslation` | Adds or replaces a language version of a base Viber message. The language is an ISO 639-1 code and the full message content for that language must be supplied. |

<details>

<summary>See 106 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Add Orders | `addOrders` | Transfers up to 1000 orders into Yespo. Sending an order again with the same external order id updates the existing record instead of creating a duplicate. Each order must identify its customer by external customer id, email or phone. This endpoint only writes orders; reading them back requires a BigQuery export. Returns the orders that could not be stored. |
| Add Site Domain | `addSiteDomain` | Registers a website domain for the organization so the web tracking script and widgets can be generated for it. Only one domain can be registered per organization, and Yespo provides no API to remove it; posting again replaces the existing domain. |
| Add Web Push Domain | `addWebPushDomain` | Registers a single HTTPS domain for web push notifications, together with the service worker file name, path and scope that Yespo should expect on that site. Returns the domains that were accepted and those that were rejected. |
| Add Web Push Domains | `addWebPushDomains` | Registers several HTTPS domains for web push notifications in one call. Each entry carries the domain plus its service worker file name, path and scope. Returns the domains that were accepted and those that were rejected. |
| Attach Contacts To Segment | `attachContactsToSegment` | Adds contacts to a static segment, identified either by Yespo contact ids or by your own external customer ids. At most 500 contacts per call. Dynamic and combined segments cannot be edited this way. |
| Cancel Broadcast | `cancelBroadcast` | Cancels a scheduled broadcast by its id, so the messages are never sent. A broadcast that has already started cannot be cancelled. |
| Configure Product Feeds | `configureProductFeeds` | Replaces the organization's product feed configuration with the supplied list of feeds. At least one feed is required; an empty list is rejected. Each feed URL must be publicly reachable over HTTP or HTTPS and must serve an XML product feed that validates against Yespo's product feed schema. |
| Count Promo Codes | `countPromoCodes` | Returns how many promotional codes are available, optionally narrowed by type, remaining active days or discount amount. The API returns a bare integer body. |
| Create App Inbox Message | `createAppInboxMessage` | Creates a base App Inbox message with title, text and optional logo image, click-through link and custom data. Returns the new message id. |
| Create Broadcast | `createBroadcast` | Schedules a broadcast of an existing message to one or more segments, for the Email, SMS, Mobile Push, Web Push, Viber or Telegram channel. Omitting Start Date starts the broadcast immediately, so set a future date when you do not want it to go out at once. Returns the broadcast id. |
| Create Email Message | `createEmailMessage` | Creates a base Email message. Set Template to true to create a reusable template, otherwise a regular message is created and added to the message list. From is required for a regular message and must exactly match an existing Email interface from List Email Interfaces; for a template it may be omitted, in which case the organization's first sender is used. Returns the new message id. |
| Create Mobile Push Message | `createMobilePushMessage` | Creates a base Mobile Push message with title, text and optional deep link, imagery, action buttons and custom data. Returns the new message id. |
| Create SMS Message | `createSmsMessage` | Creates a base SMS message. The sender name must be one of the organization's registered SMS interfaces, available from List SMS Interfaces. Returns the new message id. |
| Create Telegram Message | `createTelegramMessage` | Creates a base Telegram bot message with optional image and action buttons. Each button carries either a link or callback data. Returns the new message id. |
| Create Viber Message | `createViberMessage` | Creates a base Viber message. The sender name must be a Viber sender provisioned for your account by the provider. Besides name, sender and text you must supply either all three of Image URL, Button Caption and Button Link, or a carousel of two to five cards; the API rejects the call otherwise with "Name, from, text, img, caption, and action must be set". Returns the new message id. |
| Delete App Inbox Message | `deleteAppInboxMessage` | Deletes a base App Inbox message and all of its language versions, identified by its internal id. |
| Delete App Inbox Message Translation | `deleteAppInboxMessageTranslation` | Deletes one language version of a base App Inbox message, leaving the base message intact. |
| Delete Contact | `deleteContact` | Deletes a contact identified by its internal contact id. By default the contact is withdrawn from active use but its identifiers are retained; set Erase to true to permanently remove the profile, activity and tracking data, which cannot be undone. |
| Delete Contact By External Customer ID | `deleteContactByExternalCustomerId` | Deletes a contact identified by the external customer id held in your own system. By default the contact is withdrawn from active use but its email and external customer id are retained; set Erase to true to permanently remove all of its data. |
| Delete Email Message | `deleteEmailMessage` | Deletes a base Email message and all of its language versions, identified by its internal id. |
| Delete Email Message Translation | `deleteEmailMessageTranslation` | Deletes one language version of a base Email message, leaving the base message intact. |
| Delete Mobile Push Message | `deleteMobilePushMessage` | Deletes a base Mobile Push message and all of its language versions, identified by its internal id. |
| Delete Mobile Push Message Translation | `deleteMobilePushMessageTranslation` | Deletes one language version of a base Mobile Push message, leaving the base message intact. |
| Delete Orders | `deleteOrders` | Schedules an asynchronous job that deletes orders, either one order by its external order id or every order whose timestamp falls inside a date range. Supply either External Order ID, or both From and To. |
| Delete Past Events | `deletePastEvents` | Deletes every event that occurred inside the given period. The range is inclusive at both ends and the deletion cannot be undone. |
| Delete SMS Message | `deleteSmsMessage` | Deletes a base SMS message and all of its language versions, identified by its internal id. |
| Delete SMS Message Translation | `deleteSmsMessageTranslation` | Deletes one language version of a base SMS message, leaving the base message intact. |
| Delete Telegram Message | `deleteTelegramMessage` | Deletes a base Telegram bot message and all of its language versions, identified by its internal id. |
| Delete Telegram Message Translation | `deleteTelegramMessageTranslation` | Deletes one language version of a base Telegram bot message, leaving the base message intact. |
| Delete Viber Message | `deleteViberMessage` | Deletes a base Viber message and all of its language versions, identified by its internal id. |
| Delete Viber Message Translation | `deleteViberMessageTranslation` | Deletes one language version of a base Viber message, leaving the base message intact. |
| Delete Web Push Domain | `deleteWebPushDomain` | Removes a domain from the organization's web push notification configuration. Web push subscriptions collected on that domain stop being usable. |
| Detach Contacts From Segment | `detachContactsFromSegment` | Removes contacts from a static segment, identified either by Yespo contact ids or by your own external customer ids, at most 500 per call. Supplying neither list removes every contact from the segment. |
| Generate API Token | `generateApiToken` | Mints a bearer token for the event endpoints, as an alternative to HTTP Basic. The token authorizes only Generate Event, Generate Past Events and Delete Past Events. This connector authenticates with Basic everywhere, so the token is only needed for callers outside fastn. |
| Generate Event V1 (Deprecated) | `generateEventV1` | Deprecated first version of the event API, kept for existing integrations; new work should use Generate Event V3. Raises a behavioural event that can start a workflow or feed segmentation. Parameters are name and value pairs and the request body is limited to 20 kB. |
| Generate Event V2 (Deprecated) | `generateEventV2` | Deprecated second version of the event API, kept for existing integrations; new work should use Generate Event V3. Parameters are name and value pairs where the value may itself be an object, and nested JSON needs no escaping. |
| Generate Event V3 | `generateEventV3` | Raises a behavioural event in the account, which can start a workflow or feed segmentation. This is the current version of the event API: parameters are a flat key and value object needing no nested JSON escaping. The parameters must include a contact identifier such as email, phone, contactId or externalCustomerId. |
| Generate Past Events V1 (Deprecated) | `generatePastEventsV1` | Deprecated first version of the historical event import, kept for existing integrations; new work should use Generate Past Events V3. Imports up to 500 events per call without starting workflows. Parameters are name and value pairs. |
| Generate Past Events V2 (Deprecated) | `generatePastEventsV2` | Deprecated second version of the historical event import, kept for existing integrations; new work should use Generate Past Events V3. Imports up to 500 events per call without starting workflows, and nested JSON in parameter values needs no escaping. |
| Generate Past Events V3 | `generatePastEventsV3` | Imports up to 500 historical events per call, for example from a CRM, so they count towards segmentation. Workflows are not started for these events. This is the current version: parameters are a flat key and value object needing no nested JSON escaping. |
| Get Account Info | `getAccountInfo` | Returns identifying information about the Yespo organization the API key belongs to: the numeric organization id, the owner's email address and the organization name. Useful as a credential health check. |
| Get Additional Fields | `getAdditionalFields` | Returns the contact additional fields defined for the organization, grouped into lists, including each field key, type, allowed values and validation metadata. Use it to discover which custom contact fields you may set. |
| Get App Inbox Message | `getAppInboxMessage` | Returns one App Inbox message by its internal id, including title, text, link, logo and any language versions. |
| Get Billing History | `getBillingHistory` | Returns the organization's billing history broken down by day, optionally limited to a date range. Dates must be supplied as plain calendar dates in yyyy-MM-dd format; a full ISO 8601 timestamp makes the API return 500. |
| Get Broadcast | `getBroadcast` | Returns details of one broadcast by its id, including the message it sends, the target segment, the start date and any throttling settings. |
| Get Contact | `getContact` | Returns everything Yespo holds about one contact, identified by its internal contact id: names, media channels, additional field values, address and segment membership. |
| Get Contact Activity | `getContactActivity` | Returns activity records for messages sent to your contacts over a date range, each carrying a status such as DELIVERED, READ, CLICKED or SPAM. Narrow the result by contact identifier, message tag or status, and page through large results with the offset returned by the previous call. |
| Get Contact Emails | `getContactEmails` | Returns the email addresses of one or more contacts, looked up by their internal contact ids. Note that Yespo returns a single object rather than an array when exactly one contact matches. |
| Get Contact ID By Mobile Push Token | `getContactIdByToken` | Returns the Yespo contact id linked to a Mobile Push token, looked up by the application UUID and the token id. |
| Get Contact Message History | `getContactMessageHistory` | Returns the messages sent to one contact over a date range, across Email, SMS, Viber, Mobile Push, Web Push, App Inbox and Telegram. Identify the contact by contact id, external customer id, email or phone. |
| Get Contact Recommendations | `getContactRecommendations` | Returns product recommendations for a contact from a recommendation data source, based on web tracking behaviour. At least one contact identifier must be supplied. Product-based algorithms also need Products, and category-based algorithms need Category. |
| Get Contact Subscriptions | `getContactSubscriptions` | Returns the subscription categories a contact is currently subscribed to, identified by the internal contact id. The API returns a bare JSON array, empty when the contact holds no subscriptions. |
| Get Email Message | `getEmailMessage` | Returns one Email message by its internal id, including subject, sender, HTML body and CSS separately, tags and any language versions. Rate limited to 500 requests per hour. |
| Get Email Message View Link | `getEmailMessageViewLink` | Returns a shareable web link that renders an Email message as it will appear to recipients. This is the static template preview, unlike the personalized viewMessageLink delivered in webhook activity data. Rate limited to 500 requests per hour. |
| Get Import Status | `getImportStatus` | Returns the progress of an asynchronous contact import, identified by the session id returned from a bulk or file import. Status is one of STARTED, IMPORTING, FINISHED or ERROR. |
| Get Message Status | `getMessageStatus` | Returns the delivery status of transactional messages queued by Send Email Message, Send SMS Message, Send Viber Message or Send Prepared Message, looked up by the request ids those calls returned. |
| Get Mobile Push Message | `getMobilePushMessage` | Returns one Mobile Push message by its internal id, including title, text, buttons, imagery and any language versions. |
| Get Mobile Push Token Activity | `getTokenActivity` | Returns whether a mobile push token is currently active, as {"active": true} or {"active": false}. |
| Get Organization Balance | `getOrganizationBalance` | Returns the current account balance, credit limit and currency for the organization, together with any balance reserved per media type and sender. |
| Get Preprocessor File Status | `getPreprocessorFileStatus` | Returns the progress of a preprocessor file upload session, identified by the async session id returned from Upload or Update Preprocessor File. |
| Get Product Feed Configuration | `getProductFeedConfiguration` | Returns the product feed configuration for the organization, including each configured feed's identifier, URL and update schedule. |
| Get Segment Contacts | `getSegmentContacts` | Returns the contacts that belong to a segment, with paging and optional ordering by the time each contact was added to the segment. At most 500 contacts are returned per call. |
| Get Site Domain | `getSiteDomains` | Returns the website domain registered for the organization's web tracking script. Yespo allows only one domain per organization, so the body is a single object once a domain exists and an empty array when none has been added. |
| Get SMS Message | `getSmsMessage` | Returns one SMS message by its internal id, including sender, text, tags and any language versions. |
| Get Telegram Message | `getTelegramMessage` | Returns one Telegram bot message by its internal id, including text, image, buttons and any language versions. |
| Get Viber Message | `getViberMessage` | Returns one Viber message by its internal id, including sender, text, button or carousel settings and any language versions. |
| Get Web Push Domains | `getWebPushDomains` | Returns the list of domains registered for web push notifications in the organization. |
| Get Web Push Script | `getWebPushScript` | Returns the web push subscription script and the service worker file contents for a domain already registered for web push. The domain must be passed with its scheme, for example https://example.com; passing the bare host returns 400 Domain not found. |
| Get Web Tracking Script | `getSiteScript` | Returns the JavaScript web tracking script for the organization as plain text. A site domain must already be registered before a script can be generated. |
| Import Contacts From File | `importContactsFromFile` | Imports or updates contacts from a comma-delimited file hosted at a publicly reachable link. The file must have a .csv or .zip extension and be no larger than 100 MB. Column names must follow Yespo's import naming rules, with additional fields named KEY_PROFILE.KEY_CUSTOMFIELD. Returns the import id to poll with Get Import Status. |
| List Broadcasts | `listBroadcasts` | Returns the organization's broadcasts with paging. At most 500 broadcasts are returned per call. Yespo returns a single object rather than an array when exactly one broadcast exists, and an empty array when none do. |
| List Catalogs | `listCatalogs` | Returns the organization's catalogs (address books). A catalog groups the additional fields available for contacts. Note that Yespo returns a single object rather than an array when only one catalog exists. |
| List Email Interfaces | `listEmailInterfaces` | Returns the Email interfaces (sender names and addresses) configured for the organization. Use an interface id when creating or sending an Email message. |
| List Promo Codes | `listPromoCodes` | Returns the promotional codes available in the organization, optionally filtered by type, usage state, remaining active days or discount amount. The API returns a bare JSON array of promo code objects. |
| List SMS Interfaces | `listSmsInterfaces` | Returns the SMS interfaces (alpha names) configured for the organization. Use an interface id when creating or sending an SMS message. |
| List Subscription Categories | `listSubscriptionCategories` | Returns the subscription categories defined for the organization. Category keys returned here are the values used when reading or updating a contact's subscriptions. |
| Mute Application Token | `muteApplicationToken` | Stops Telegram notifications reaching the user behind a token, either for a set number of seconds or permanently when no duration is given. |
| Remove Emails From Unsubscribed List | `removeEmailsFromUnsubscribed` | Removes email addresses from the organization's unsubscribed list, making those contacts eligible for bulk campaigns again. |
| Search App Inbox Messages | `searchAppInboxMessages` | Searches the organization's App Inbox messages by part of their name or by tag, with paging. At most 500 messages are returned per call. |
| Search Contacts | `searchContacts` | Searches contacts by external customer id, email, phone number or name, with paging. At most 500 contacts are returned per call; the total match count is returned in the TotalCount response header, which this connector cannot expose. |
| Search Email Messages | `searchEmailMessages` | Searches the organization's Email messages by part of their name or by tag, with paging. At most 500 messages are returned per call, and the endpoint is rate limited to 500 requests per hour. |
| Search Mobile Push Messages | `searchMobilePushMessages` | Searches the organization's Mobile Push messages by part of their name or by tag, with paging. At most 500 messages are returned per call. |
| Search Segments | `searchSegments` | Searches the organization's contact segments, optionally filtering by name and paging through results. Returns each segment's id, name and type. |
| Search SMS Messages | `searchSmsMessages` | Searches the organization's SMS messages by part of their name or by tag, with paging. At most 500 messages are returned per call. |
| Search Telegram Messages | `searchTelegramMessages` | Searches the organization's Telegram bot messages by part of their name or by tag, with paging. At most 500 messages are returned per call. |
| Search Viber Messages | `searchViberMessages` | Searches the organization's Viber messages by part of their name or by tag, with paging. At most 500 messages are returned per call. |
| Search Workflows | `searchWorkflows` | Searches the organization's automation workflows, optionally filtering by name and paging through results. Returns each workflow's id, name and status. |
| Send Email Message | `sendEmailMessage` | Sends a transactional Email immediately to one or more addresses, creating a contact for any address that is not yet known. The sender must be a registered Email interface. Yespo advises against this route for one-time passwords because the full HTML travels in every request; use Send Prepared Message instead. |
| Send Prepared Message | `sendPreparedMessage` | Sends an existing Email, SMS, Mobile Push, Web Push, Viber or Telegram message to one or many recipients, with per-recipient parameters for dynamic content. Each recipient is addressed by contact id, external customer id or media-channel locator such as an email address or phone number. |
| Send SMS Message | `sendSmsMessage` | Sends a transactional SMS immediately to a list of phone numbers or to every contact in a segment, creating a contact for any number that is not yet known. Supply either Phone Numbers or Segment ID. The sender must be a registered SMS interface, and each message consumes SMS credit. |
| Send Viber Message | `sendViberMessage` | Sends a transactional Viber message immediately to a list of phone numbers or to every contact in a segment, creating a contact for any number that is not yet known. Supply either Phone Numbers or Segment ID. A carousel of two to five cards can replace the single image and button, in which case the image, caption and action are used only for the SMS fallback. |
| Set Mobile Push Token Activity | `setTokenActivity` | Activates or deactivates a mobile push token. Deactivating a token stops push notifications being delivered to that device. |
| Subscribe Contact | `subscribeContact` | Registers a subscription from a sign-up form, implementing double opt-in. A new contact is created unconfirmed and cannot receive bulk campaigns until it confirms, though it can receive triggered messages. An event is generated automatically so a confirmation campaign can be triggered. |
| Unmute Application Token | `unmuteApplicationToken` | Resumes Telegram notifications to the user behind a token that was previously muted. |
| Update App Inbox Message | `updateAppInboxMessage` | Updates a base App Inbox message identified by its internal id. The API replaces the message, so name, title and text must all be supplied. |
| Update Contact | `updateContact` | Updates a contact identified by its internal contact id. Every field except the contact id itself can be changed, and a previously deleted contact is restored by this call. At least one media channel must be supplied. |
| Update Contact Subscriptions | `updateContactSubscriptions` | Replaces the set of subscription categories a contact belongs to. Category keys come from List Subscription Categories. |
| Update Email Message | `updateEmailMessage` | Updates a base Email message identified by its internal id. The API replaces the message content, so supply every field you want to keep. From must match an existing Email interface and is required unless the message is a template. |
| Update Interaction Status | `updateInteractionStatus` | Reports the delivery status of a message back to Yespo using the interaction id that was delivered alongside the message payload, for example the es_interaction_id field in a Mobile Push. Use it when your app, rather than Yespo, observes the delivery outcome. |
| Update Mobile Push Message | `updateMobilePushMessage` | Updates a base Mobile Push message identified by its internal id. The API replaces the message, so name, title and text must all be supplied. |
| Update Preprocessor File | `updatePreprocessorFile` | Replaces the data of a preprocessor file that was previously uploaded, addressed by the file id returned from Upload Preprocessor File. |
| Update SMS Message | `updateSmsMessage` | Updates a base SMS message identified by its internal id. The API replaces the message, so name, sender and text must all be supplied. |
| Update Telegram Message | `updateTelegramMessage` | Updates a base Telegram bot message identified by its internal id. The API replaces the message, so supply every field you want to keep. |
| Update Viber Message | `updateViberMessage` | Updates a base Viber message identified by its internal id. The API replaces the message, so name, sender and text must all be supplied. |
| Upload Preprocessor File | `uploadPreprocessorFile` | Loads a preprocessor data file from an external repository so message content can be personalised from it. The link must end in .json and be publicly reachable. Choose Key to look rows up by a key, or Random to pick a row at random. Returns the file id and the async session id. |
| Upload Promo Codes | `uploadPromoCodes` | Uploads promotional codes to the organization's promo code pool as a JSON list. Codes that already exist are updated rather than duplicated. The expiration date and discount amount apply to every code in the batch. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Contact Unsubscribed | `UNSUBSCRIBED` | The contact unsubscribed from the broadcasting list. Arm it by hand: my.yespo.io, account Settings, Data export tab, New data export, choose Webhook, paste the fastn webhook URL as the Callback URL, tick UNSUBSCRIBED under Export Activity Statuses, Test, then Save and close. Payload schema modelled from Yespo's documented test payload. |
| Link Clicked | `CLICKED` | The contact clicked a link in the message; one event is generated per click on every link, and clickEventLink carries the URL. UTM tags are present only on click events. Arm it by hand: my.yespo.io, account Settings, Data export tab, New data export, choose Webhook, paste the fastn webhook URL as the Callback URL, tick CLICKED under Export Activity Statuses, Test, then Save and close. Payload schema modelled from Yespo's documented test payload. |
| Marked As Spam | `SPAM` | The contact reported the message as spam. Arm it by hand: my.yespo.io, account Settings, Data export tab, New data export, choose Webhook, paste the fastn webhook URL as the Callback URL, tick SPAM under Export Activity Statuses, Test, then Save and close. Payload schema modelled from Yespo's documented test payload. |
| Message Delivered | `DELIVERED` | A message was delivered to the contact. Yespo has no webhook registration API, so the customer arms this by hand: open my.yespo.io, go to account Settings, open the Data export tab, click New data export, choose Webhook, give it a name and paste the fastn webhook URL as the Callback URL, optionally enable Authentication and add up to 5 headers, leave DELIVERED ticked under Export Activity Statuses, click Test then Save and close. Deliveries arrive as a POST carrying a JSON array of activity objects. Payload schema modelled from Yespo's documented test payload, not a captured delivery. |
| Message Read | `READ` | The contact opened the message. Arm it by hand: my.yespo.io, account Settings, Data export tab, New data export, choose Webhook, paste the fastn webhook URL as the Callback URL, tick READ under Export Activity Statuses, Test, then Save and close. Payload schema modelled from Yespo's documented test payload. |
| Message Undelivered | `UNDELIVERED` | A message could not be delivered; statusDescription carries the reason and, for Email, hardBounce distinguishes a permanent failure from a temporary one. Arm it by hand: my.yespo.io, account Settings, Data export tab, New data export, choose Webhook, paste the fastn webhook URL as the Callback URL, tick UNDELIVERED under Export Activity Statuses, Test, then Save and close. Payload schema modelled from Yespo's documented test payload. |
| Mobile Push Sent | `SENT` | A Mobile Push message was handed to the push provider. Yespo generates this status for the Mobile Push channel only. Arm it by hand: my.yespo.io, account Settings, Data export tab, New data export, choose Webhook, paste the fastn webhook URL as the Callback URL, tick SENT under Export Activity Statuses, Test, then Save and close. Payload schema modelled from Yespo's documented test payload. |
| Subscription Changed | `SUBSCRIPTION_CHANGED` | The contact changed their subscription categories; subscriptions carries the category keys they now hold. Arm it by hand: my.yespo.io, account Settings, Data export tab, New data export, choose Webhook, paste the fastn webhook URL as the Callback URL, tick SUBSCRIPTION_CHANGED under Export Activity Statuses, Test, then Save and close. Payload schema modelled from Yespo's documented test payload. |
