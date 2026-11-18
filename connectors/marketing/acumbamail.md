---
description: "Acumbamail is a Spanish email and SMS marketing platform."
hidden: true
---

# Acumbamail

<img src="../../.gitbook/assets/connectors/lg/acumbamail.png" alt="Acumbamail logo">

Acumbamail is a Spanish email and SMS marketing platform. This connector covers the full Acumbamail v1 API: subscriber lists, subscribers and merge fields, email campaigns and their statistics, templates, SMS campaigns, transactional SMTP email, and list and SMTP webhook configuration.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [acumbamail.com](https://acumbamail.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `acumbamail` |

## Use it

Add Acumbamail from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.acumbamail.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Merge Tag | `addMergeTag` | Adds a merge field to a subscriber list, so subscribers on that list can carry an extra typed value. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Add Subscriber | `addSubscriber` | Adds a subscriber to a list. WARNING - setting Double Opt-In to 1 makes Acumbamail send a real confirmation email to the address. Merge Fields carries the subscriber's data and must include the email address; pass it as an object, for example {"email": "someone@example.com"}. Requires a paid Acumbamail plan. |
| Batch Add Subscribers | `batchAddSubscribers` | Adds a group of subscribers to a list in one call. Subscribers Data is a JSON-encoded array of objects, one per subscriber, each carrying the list's field names including email. Rate limit: 5 requests per second. Requires a paid Acumbamail plan. |
| Batch Delete Subscribers | `batchDeleteSubscribers` | Removes a group of subscribers from a list in one call. This permanently deletes the named subscribers and cannot be undone. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Configure List Webhook | `configListWebhook` | Sets the webhook for a subscriber list - the URL Acumbamail posts to and which subscriber events it sends. Acumbamail stores ONE webhook per list, so this replaces whatever was configured before rather than adding to it; read the current setting with Get List Webhook first. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Configure SMTP Webhook | `configSMTPWebhook` | Sets the account-wide SMTP webhook - the URL Acumbamail posts transactional email events to and which events it sends. Acumbamail stores ONE SMTP webhook per account, so this replaces the existing configuration rather than adding to it; read the current setting with Get SMTP Webhook first. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Create Campaign | `createCampaign` | DANGER - this creates AND SENDS a campaign. Acumbamail's own documentation describes this function as 'Creates and sends a new campaign', so omitting Date Send dispatches the campaign to every subscriber of the named lists immediately, with no draft step and no recall. Set Date Send to schedule it for later instead. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Create List | `createList` | Creates a new subscriber list. Acumbamail requires the sender's postal identity on the list for anti-spam compliance, so company, country, city, address and phone are part of the call. Rate limit applies. Requires a paid Acumbamail plan. |
| Create Template | `createTemplate` | Creates a reusable email template from HTML. Note that the Acumbamail API exposes no delete-template endpoint, so a template created here can only be removed from the Acumbamail web interface. Rate limit: 10 requests per minute. |
| Delete All Subscribers | `deleteAllSubscribers` | DANGER - removes EVERY subscriber from a list in one call, irreversibly. The list itself is kept. There is no selective form of this call and no confirmation step. Acumbamail runs it in the background and it can take minutes on a large list; poll Get List Stats until total_subscribers reaches 0 to know it has finished. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Delete List | `deleteList` | Permanently deletes a subscriber list and everything in it. This cannot be undone. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Delete Subscriber | `deleteSubscriber` | Permanently removes one subscriber from a list by email address. To stop mailing someone while keeping their record, use Unsubscribe Subscriber instead. Requires a paid Acumbamail plan. |
| Duplicate Template | `duplicateTemplate` | Creates a copy of an existing template under a new name. Note that the Acumbamail API exposes no delete-template endpoint, so the copy can only be removed from the Acumbamail web interface. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get Campaign Basic Information | `getCampaignBasicInformation` | Returns the headline figures for one campaign - the counts of sends, opens, clicks and bounces. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get Campaign Clicks | `getCampaignClicks` | Returns the subscribers who clicked a link in a campaign and when each of them did so. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get Campaign Information By ISP | `getCampaignInformationByISP` | Returns a campaign's delivery and engagement figures broken down by recipient mail provider, which is how deliverability problems at one ISP are spotted. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get Campaign Links | `getCampaignLinks` | Returns each tracked URL in a campaign together with the subscribers who clicked it. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get Campaign Openers | `getCampaignOpeners` | Returns the subscribers who opened a campaign and when each of them did so. Set Exclude Clickers to leave out those who also clicked. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get Campaign Openers By Browser | `getCampaignOpenersByBrowser` | Returns a campaign's opens broken down by the browser or mail client used. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get Campaign Openers By Countries | `getCampaignOpenersByCountries` | Returns the number of times a campaign was opened in each country. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get Campaign Openers By OS | `getCampaignOpenersByOs` | Returns a campaign's opens broken down by the operating system of the device that opened it. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get Campaign Soft Bounces | `getCampaignSoftBounces` | Returns the current soft bounces recorded for a campaign - addresses that failed temporarily rather than permanently. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get Campaign Total Information | `getCampaignTotalInformation` | Returns the complete statistics for one campaign, the fullest view Acumbamail offers in a single call. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get Campaigns | `getCampaigns` | Returns the campaigns in the account, keyed by campaign id, with optional date and status filters. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get Campaigns Public URLs | `getCampaignsPublicUrls` | Gets the public address and thumbnail of sent campaigns, newest first, for a newsletter archive. Rate limit 5 requests per second. |
| Get Email Status | `getEmailStatus` | Returns the delivery status of a transactional email previously sent through the SMTP service, looked up by the key that send returned. Requires a paid Acumbamail plan. |
| Get Fields | `getFields` | Returns the merge fields defined on a subscriber list and the data type of each. Use these field names as the keys of Merge Fields when adding a subscriber. Rate limit: 10 requests per minute. |
| Get Forms | `getForms` | Returns the subscription forms in the account, or only those attached to one list when List ID is supplied. The response is an object keyed by form id. Rate limit: 5 requests per second. |
| Get Inactive Subscribers | `getInactiveSubscribers` | Returns every subscriber who became inactive between two dates - unsubscribed, complained, or hard bounced - across the account. Useful for syncing suppressions back to your own system. Requires a paid Acumbamail plan. |
| Get List Fields | `getListFields` | Returns the merge fields of a subscriber list together with their configuration. This is the richer counterpart of Get Fields, which returns only the name-to-type mapping. |
| Get List Segments | `getListSegments` | Returns the segments defined on a subscriber list. An unknown list id is answered with HTTP 404 and the message 'You do not have a list with that id'. |
| Get List Stats | `getListStats` | Returns the statistics of a subscriber list, including total_subscribers. Poll this after Delete All Subscribers to see when the background purge has finished. Requires a paid Acumbamail plan. |
| Get List Subscriber Stats | `getListSubsStats` | Returns subscriber-level statistics for a list, broken down by subscriber activity. Requires a paid Acumbamail plan. |
| Get List Webhook | `getListWebhook` | Returns the webhook configuration of a subscriber list - its callback URL and which subscriber events are switched on. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get Lists | `getLists` | Returns every subscriber list in the Acumbamail account. The response is an object keyed by list id rather than an array, so each property name is a list id and its value holds that list's details. |
| Get Merge Fields | `getMergeFields` | Returns the merge fields available on a subscriber list. Requires a paid Acumbamail plan. |
| Get SMS Campaigns | `getSMSCampaigns` | Returns the SMS campaigns sent between two optional dates, each with a brief summary. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get SMS Credits | `getCreditsSMS` | Returns the number of SMS credits remaining on the account. Check this before a bulk send. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get SMS Quick Subscriber Report | `getSMSQuickSubscriberReport` | Returns the subscribers who received quick SMS campaigns between two dates. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get SMS Simple Report | `getSMSSimpleReport` | Returns the delivery information for one already-sent SMS. Requires a paid Acumbamail plan. |
| Get SMS Subscriber Report | `getSMSSubscriberReport` | Returns every subscriber who received a given SMS campaign. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get SMTP Credits | `getCreditsSMTP` | Returns the number of transactional SMTP email credits remaining on the account. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get SMTP Webhook | `getSMTPWebhook` | Returns the account-wide SMTP webhook configuration - the URL Acumbamail posts transactional email events to and which of those events are switched on. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Get Stats By Date | `getStatsByDate` | Returns the combined statistics of the campaigns sent to one list over a date range. Requires a paid Acumbamail plan. |
| Get Subscriber Details | `getSubscriberDetails` | Returns the full detail of one subscriber, including their merge field values and status. Requires a paid Acumbamail plan. |
| Get Subscribers | `getSubscribers` | Returns the subscribers of a list. Requires a paid Acumbamail plan. |
| Get Templates | `getTemplates` | Returns the saved email templates in the account, with their ids and whether each is available for use. Rate limit: 1 request per second. Requires a paid Acumbamail plan. |
| Search Subscriber | `searchSubscriber` | Finds a subscriber across the account's lists by email address. Requires a paid Acumbamail plan. |
| Send Certified Email | `sendCertifiedEmail` | DANGER - sends one real certified email, a legally evidenced delivery that cannot be recalled and is charged at a higher rate than an ordinary transactional message. Omitting Program Date sends it immediately. Acumbamail requires the SMTP service to be activated on the account. Requires a paid Acumbamail plan. |
| Send SMS | `sendSMS` | DANGER - sends one or more real SMS messages to real mobile numbers and consumes SMS credits. There is no test mode on this endpoint and a sent message cannot be recalled. Acumbamail also requires the SMS service to be activated on the account before this works. Requires a paid Acumbamail plan. |
| Send Template Campaign | `sendTemplateCampaign` | DANGER - creates and sends a campaign from a saved template. Acumbamail's documentation describes this as 'Creates and sends a new campaign with a template', so omitting Date Send dispatches it to every subscriber of the named lists immediately, with no draft step and no recall. Rate limit: 10 requests per minute. Requires a paid Acumbamail plan. |
| Send Transactional Email | `sendOne` | DANGER - sends one real transactional email to a real inbox and consumes an SMTP credit. It cannot be recalled. Supply either Body as HTML or a Template ID. Setting Program Date schedules it instead of sending immediately, so omitting that field means the message goes out now. Acumbamail requires the SMTP service to be activated on the account. Requires a paid Acumbamail plan. |
| Send Transactional Emails | `sendTransactionalEmails` | DANGER - sends one or more real transactional emails through Acumbamail's SMTP service. Every message in the batch is delivered to a real inbox and cannot be recalled, and each consumes an SMTP credit. Acumbamail requires the SMTP service to be activated on the account before this works. Requires a paid Acumbamail plan. |
| Unsubscribe Subscriber | `unsubscribeSubscriber` | Marks a subscriber as unsubscribed on a list so they stop receiving campaigns, while keeping their record. Prefer this over Delete Subscriber when you need to retain the suppression. Requires a paid Acumbamail plan. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Campaign Opened | `opens` | Fires when a subscriber on the watched list opens a campaign. Acumbamail stores ONE webhook per list, so this replaces any other event subscription on the same list. The payload format is undocumented by Acumbamail and no delivery could be captured, so no payload schema is declared. Requires a paid Acumbamail plan. |
| Hard Bounce | `hard_bounce` | Fires when a message to a subscriber on the watched list hard bounces. Acumbamail stores ONE webhook per list, so this replaces any other event subscription on the same list. The payload format is undocumented by Acumbamail and no delivery could be captured, so no payload schema is declared. Requires a paid Acumbamail plan. |
| Link Clicked | `click` | Fires when a subscriber on the watched list clicks a tracked link. Acumbamail stores ONE webhook per list, so this replaces any other event subscription on the same list. The payload format is undocumented by Acumbamail and no delivery could be captured, so no payload schema is declared. Requires a paid Acumbamail plan. |
| Soft Bounce | `soft_bounce` | Fires when a message to a subscriber on the watched list soft bounces. Acumbamail stores ONE webhook per list, so this replaces any other event subscription on the same list. The payload format is undocumented by Acumbamail and no delivery could be captured, so no payload schema is declared. Requires a paid Acumbamail plan. |
| Spam Complaint | `complain` | Fires when a recipient marks a message from the watched list as spam. Acumbamail stores ONE webhook per list, so this replaces any other event subscription on the same list. The payload format is undocumented by Acumbamail and no delivery could be captured, so no payload schema is declared. Requires a paid Acumbamail plan. |
| Subscriber Added | `subscribes` | Fires when someone subscribes to the watched Acumbamail list. Set the List ID input to the list to watch - Acumbamail stores ONE webhook per list, so subscribing a second event on the same list REPLACES the first rather than adding to it; to receive several event types on one list, configure them together with the Configure List Webhook action instead. Acumbamail does not publish the payload format for list webhooks and no delivery could be captured on this account, so no payload schema is declared here rather than inventing one. Requires a paid Acumbamail plan: on a free plan the registration call returns 401 'This endpoint is not available for non-paying customers'. |
| Subscriber Unsubscribed | `unsubscribes` | Fires when someone unsubscribes from the watched Acumbamail list. Acumbamail stores ONE webhook per list, so this replaces any other event subscription on the same list; use Configure List Webhook directly to enable several event types at once. The payload format is undocumented by Acumbamail and no delivery could be captured, so no payload schema is declared. Requires a paid Acumbamail plan. |
