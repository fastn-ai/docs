---
description: "SendPulse is a multi-channel marketing platform for email campaigns, transactional email (SMTP), SMS, Viber, web push notifications, email verification and…"
hidden: true
---

# SendPulse

<img src="../../.gitbook/assets/connectors/send-pulse.png" alt="SendPulse logo" width="64">

SendPulse is a multi-channel marketing platform for email campaigns, transactional email (SMTP), SMS, Viber, web push notifications, email verification and Automation 360 flows. This connector covers the SendPulse Email and Messaging REST API: mailing lists, contacts, campaigns, templates, senders, tags, blacklist, webhooks, transactional email, SMS and Viber campaigns, web push, email verification and automation statistics.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [sendpulse.com](https://sendpulse.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `sendPulse` |

## Use it

Add SendPulse from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.sendPulse.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Sender | `activateSender` | Confirms a SendPulse sender address using the activation code emailed to it. |
| Add Email Addresses to Blacklist | `addToBlacklist` | Adds one or more email addresses to the SendPulse account blacklist so they are excluded from every campaign. |
| Add Emails to Mailing List | `addEmailsToMailingList` | Adds contacts to a SendPulse mailing list. Leave confirmation empty for single opt-in. Set confirmation to force together with sender_email and message_lang to send a double opt-in confirmation email instead. |
| Add Phone Numbers to Mailing List | `addPhonesToMailingList` | Adds phone numbers to a SendPulse mailing list without variables, so the list can be used for SMS campaigns. |
| Add Phone Numbers to SMS Blacklist | `addPhonesToSmsBlacklist` | Adds one or more phone numbers to the SendPulse SMS blacklist so they are excluded from every SMS campaign. |
| Add Phone Numbers to Viber Blacklist | `addPhonesToViberBlacklist` | Adds one or more phone numbers to the Viber blacklist so they are excluded from every Viber campaign. |
| Add Phone Numbers with Variables to Mailing List | `addPhonesWithVariablesToMailingList` | Adds phone numbers to a SendPulse mailing list together with their personalisation variables. Date variables must be supplied as YYYY-MM-DD with no time part. |
| Add Sender | `addSender` | Registers a new sender email address on the SendPulse account. SendPulse emails an activation code to the address, which must then be confirmed with Activate Sender. |
| Add Sender Domain | `addSenderDomain` | Registers a sending domain on the SendPulse account. The DKIM and SPF records must then be published in the domain's DNS before SendPulse will send from it. |
| Assign Tag to Email Address | `pinTagToEmail` | Assigns one or more existing SendPulse tags to an email contact. |

<details>

<summary>See 131 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Assign Tag to Phone Number | `pinTagToPhone` | Assigns one or more existing SendPulse tags to a phone contact. |
| Cancel Campaign | `cancelCampaign` | Cancels a scheduled SendPulse campaign or deletes a draft before it is sent. |
| Cancel SMS Campaign | `cancelSmsCampaign` | Cancels a scheduled SMS campaign before sending has started. |
| Change Phone Number for Contact | `updateContactPhone` | Sets or replaces the phone number stored against a contact in a SendPulse mailing list. |
| Check SMTP Subscription Status | `checkSmtpSubscriptionStatus` | Checks whether one email address appears on the transactional SMTP unsubscribe list. |
| Count Contacts in Mailing List | `getEmailsTotalCount` | Returns the total number of contacts in a SendPulse mailing list, optionally counting only active contacts. |
| Count SMTP Bounces | `getSmtpBouncesTotal` | Returns the total number of transactional email bounces recorded in the most recent 24 hours. |
| Count SMTP Sent Emails | `getSmtpEmailsTotal` | Returns the total number of transactional emails sent through the SendPulse SMTP service. |
| Create Campaign | `createCampaign` | Creates an email campaign in SendPulse and either sends it immediately, schedules it for send_date, or saves it as a draft when type is draft. Supply either body or template_id, and either list_id or segment_id. |
| Create Mailing List | `createMailingList` | Creates a new SendPulse mailing list (address book) and returns its numeric ID. |
| Create Mailing List Verification Report | `createMailingListVerificationReport` | Generates a downloadable report of the verification results for a mailing list. Call this before View Mailing List Verification Report or Download Mailing List Verification Report. |
| Create SMS Campaign for Mailing List | `createSmsCampaign` | Creates an SMS campaign that sends a message to every phone number in a SendPulse mailing list. Set emulate to true to build the campaign without sending it. |
| Create Tag | `createTag` | Creates a contact tag in the SendPulse account. Tags require the Pro plan or above in the Email section. |
| Create Template | `createTemplate` | Saves a new email template in the SendPulse account from a Base64-encoded HTML body. |
| Create Viber Campaign | `createViberCampaign` | Creates a Viber campaign and sends it to a mailing list or to an explicit list of phone numbers. Set emulate to true to validate the campaign without sending it or charging the account. |
| Create Web Push Campaign | `createWebPushCampaign` | Creates a web push campaign for one website. SendPulse allows one campaign per website every 15 minutes; use Automation 360 for triggered campaigns. |
| Create Webhook | `createWebhook` | Registers a handler URL to receive SendPulse email-service events. SendPulse creates one webhook record per action supplied and returns their IDs. |
| Delete Automation Event Log | `deleteAutomationEventLog` | Removes entries from the Automation 360 event log. Supply an event identifier to clear every entry for that event, or a contact identifier to clear that contact's entries across all events, or both to narrow the deletion. |
| Delete Email Address from All Mailing Lists | `deleteEmailGlobally` | Removes an email address from every mailing list in the SendPulse account. |
| Delete Emails from Mailing List | `deleteEmailsFromMailingList` | Removes the given email addresses from a SendPulse mailing list. |
| Delete Mailing List | `deleteMailingList` | Permanently removes a SendPulse mailing list and all of its contacts. |
| Delete Sender | `deleteSender` | Removes a sender email address from the SendPulse account. |
| Delete Sender Domain | `deleteSenderDomain` | Removes a sending domain from the SendPulse account by its numeric domain ID, freeing the sender-domain slot. Read the ID from Get Sender Domains. |
| Delete SMS Campaign | `deleteSmsCampaign` | Deletes an SMS campaign from the SendPulse account. |
| Delete Tag | `deleteTag` | Deletes a contact tag from the SendPulse account. |
| Delete Webhook | `deleteWebhook` | Removes a SendPulse email-service webhook so the handler URL stops receiving that event. |
| Download Mailing List Verification Report | `downloadMailingListVerificationReport` | Downloads a previously generated mailing list verification report as a file. Call Create Mailing List Verification Report first with the same format. Use format 4 (XLSX) or 3 (XLS): SendPulse answers format 2 (CSV) with {"result": false} even when the report exists. SendPulse deletes the report once it has been downloaded, so a second call returns {"result": false}. |
| Edit Mailing List | `updateMailingList` | Renames an existing SendPulse mailing list. |
| Edit Scheduled Campaign | `updateCampaign` | Updates a scheduled SendPulse campaign. The API requires the full message definition on every update, so sender_name, sender_email and body must be supplied along with any changed field. Campaigns already sent, and drafts, cannot be updated and return error code 8023. |
| Edit Template | `updateTemplate` | Replaces the HTML body of an existing SendPulse email template. |
| Get Account Information | `getAccountInformation` | Retrieves profile information for the SendPulse account the connection authenticates as, including the account id, name, email, phone, language, registration date and currency. |
| Get Automation Element Contacts | `getAutomationElementContacts` | Lists the contacts that passed through one element of an Automation 360 flow. Use the flow-operator element type for filter, condition, goal, action and pause elements. |
| Get Automation Element Statistics | `getAutomationElementStats` | Returns the lifetime statistics for one element inside an Automation 360 flow. The element type selects which statistics endpoint is used, so the same action covers the start trigger, email, push, SMS, messenger, Viber, filter, condition, goal, action and pause elements. |
| Get Automation Element Statistics For Period | `getAutomationElementStatsForPeriod` | Returns statistics for one element inside an Automation 360 flow, limited to a date range. The element type selects which statistics endpoint is used. |
| Get Automation Flow | `getAutomationFlow` | Retrieves one Automation 360 flow with its elements, so the element identifiers needed by the element statistics actions can be read from the flow. |
| Get Automation Flow Conversions | `getAutomationFlowConversions` | Returns the conversion totals recorded by an Automation 360 flow, across its start trigger and every goal element. |
| Get Automation Flow Conversions For Period | `getAutomationFlowConversionsForPeriod` | Returns the conversion totals recorded by an Automation 360 flow, limited to a date range. |
| Get Automation Flow Converted Contacts | `getAutomationFlowConvertedContacts` | Lists the contacts that converted in an Automation 360 flow. The scope selects whether the list covers every conversion, only start-trigger conversions, or only goal-element conversions. |
| Get Automation Flow Converted Contacts For Period | `getAutomationFlowConvertedContactsForPeriod` | Lists the contacts that converted in an Automation 360 flow within a date range. The scope selects whether the list covers every conversion, only start-trigger conversions, or only goal-element conversions. |
| Get Automation Flow Statistics For Period | `getAutomationFlowStatsForPeriod` | Returns Automation 360 flow statistics limited to a date range. |
| Get Automation Flow Total Statistics | `getAutomationFlowTotalStats` | Returns the lifetime totals for one Automation 360 flow, such as how many contacts started, are in progress and completed it. |
| Get Automation Flows | `getAutomationFlows` | Lists the Automation 360 flows on the SendPulse account, with the sender, mailing list and schedule configured on each flow. |
| Get Automation Goal Converted Contacts | `getAutomationGoalConvertedContacts` | Lists the contacts that converted through one specific goal element of an Automation 360 flow. |
| Get Automation Goal Converted Contacts For Period | `getAutomationGoalConvertedContactsForPeriod` | Lists the contacts that converted through one specific goal element of an Automation 360 flow within a date range. |
| Get Balance | `getBalance` | Returns the current balance of the SendPulse account in its default currency. |
| Get Balance by Currency | `getBalanceByCurrency` | Returns the SendPulse account balance converted into the requested currency. |
| Get Campaign | `getCampaignById` | Returns the configuration and delivery statistics of a single SendPulse email campaign. |
| Get Campaign Cost for Mailing List | `getCampaignCostByList` | Estimates the cost of sending one campaign to every contact in a SendPulse mailing list under the account's current tariff. |
| Get Campaign Country Statistics | `getCampaignCountryStats` | Returns the number of opens of a SendPulse campaign broken down by recipient country code. |
| Get Campaign Referral Statistics | `getCampaignReferralStats` | Returns the links in a SendPulse campaign together with the number of clicks recorded on each. |
| Get Campaign Statistics for Email Address | `getEmailCampaignStats` | Returns aggregate engagement statistics for one email address across all SendPulse campaigns, plus whether it is blacklisted. |
| Get Campaign Statistics for Multiple Email Addresses | `getMultipleEmailsCampaignStats` | Returns aggregate campaign engagement statistics for a batch of email addresses in one request. |
| Get Campaigns by Mailing List | `getCampaignsByList` | Returns the SendPulse campaigns that were sent to a specific mailing list. |
| Get Contacts by Variable | `getContactsByVariable` | Returns every contact in a SendPulse mailing list whose named variable matches the given value. |
| Get Detailed Balance | `getDetailedBalance` | Returns the SendPulse account balance broken down by main and bonus funds, together with the active tariff and remaining allowances for email, SMTP and web push. |
| Get Detailed Email Address Information | `getEmailDetails` | Returns the subscription history of an email address: which SendPulse mailing lists it joined, when, and from which source. |
| Get Email Address in Campaign | `getEmailCampaignInfo` | Returns the delivery and engagement record of one email address within one SendPulse campaign. |
| Get Email Address in Mailing List | `getEmailFromList` | Returns a single contact record from a SendPulse mailing list, including its phone number, status and variables. |
| Get Email Address Information | `getEmailInfo` | Returns every mailing list that contains the given email address, with its subscription status and variables in each list. |
| Get Email Address Verification Result | `getEmailAddressVerificationResult` | Returns the verification verdict for a single email address, including whether the address is disposable, a webmail address or automatically generated. Call Verify Email Address first. |
| Get Mailing List | `getMailingListById` | Returns detailed information about a single SendPulse mailing list identified by its ID. |
| Get Mailing List Verification Progress | `getMailingListVerificationProgress` | Reports how many addresses of a mailing list currently being verified have been processed so far. |
| Get Mailing List Verification Results | `getMailingListVerificationResults` | Returns the email verification results for a mailing list, with the per-address verdict and the counts of valid, risky and invalid addresses. |
| Get Multiple Email Addresses Information | `getMultipleEmailsInfo` | Returns mailing list membership information for a batch of email addresses in one request. |
| Get Phone Number Information | `getPhoneNumberInfo` | Retrieves the status, variables and date added for one phone number inside a SendPulse mailing list. |
| Get Sender Domains | `getSenderDomains` | Lists the sending domains registered on the SendPulse account, with their DKIM, SPF and DMARC verification state. |
| Get SMS Blacklist | `getSmsBlacklist` | Lists the phone numbers on the SendPulse SMS blacklist, with the description and the date each number was added. |
| Get SMS Blacklist Entries by Number | `getSmsBlacklistByNumbers` | Checks specific phone numbers against the SendPulse SMS blacklist and returns an entry for each number that is blacklisted. |
| Get SMS Campaign Cost | `getSmsCampaignCost` | Calculates what an SMS campaign would cost for a mailing list or an explicit set of phone numbers, without creating the campaign. |
| Get SMS Campaign Information | `getSmsCampaignInfo` | Retrieves one SMS campaign with its price, send date, sender and the delivery status of every recipient phone number. |
| Get SMS Campaigns | `getSmsCampaigns` | Lists SMS campaigns created in a date range, with the price, currency, send date and sender of each campaign. |
| Get SMS Sender IDs | `getSmsSenders` | Lists the alphanumeric sender IDs registered for SMS campaigns on the SendPulse account, with the countries each one is approved for. |
| Get SMTP Bounces for 24-Hour Period | `getSmtpBouncesDay` | Returns the transactional emails that bounced in the 24 hours up to the given date. SendPulse only keeps bounce detail for the most recent 24 hours. |
| Get SMTP Email Information | `getSmtpEmailInfo` | Returns the delivery record and tracking data of a single transactional email sent through the SendPulse SMTP service. |
| Get SMTP Emails in Bulk | `getSmtpEmailsBatchInfo` | Returns the delivery records of several transactional emails in one request, looked up by their message IDs. |
| Get SMTP Sender Addresses | `getSmtpSenderAddresses` | Lists the sender email addresses available to the transactional SMTP service on the account. |
| Get SMTP Sender IP Addresses | `getSmtpSenderIps` | Lists the IP addresses SendPulse uses to deliver transactional SMTP email for the account. |
| Get SMTP Unsubscribed Recipients | `getSmtpUnsubscribed` | Lists the recipients who have unsubscribed from transactional SMTP email, with the reason and date of each unsubscribe. |
| Get Template | `getTemplateById` | Returns a single SendPulse email template, including its HTML body, by template ID. |
| Get Template by Name Slug | `getTemplateBySlug` | Returns a single SendPulse email template looked up by its URL-friendly name slug instead of its ID. |
| Get Verified Mailing Lists | `getVerifiedMailingLists` | Lists the mailing lists that have been through email verification, with the overall verdict and the counts of valid, unconfirmed and invalid addresses for each. |
| Get Viber Blacklist | `getViberBlacklist` | Lists the phone numbers excluded from Viber campaigns on the SendPulse account. |
| Get Viber Campaign Recipients | `getViberCampaignRecipients` | Lists the recipients of a Viber campaign together with the delivery status recorded for each phone number. |
| Get Viber Campaign Statistics | `getViberCampaign` | Retrieves one Viber campaign with its delivery, read and error statistics. |
| Get Viber Campaigns | `getViberCampaigns` | Lists the Viber campaigns on the SendPulse account with their status, send date and recipient counts. |
| Get Viber Sender Name | `getViberSender` | Retrieves a single Viber sender name by its identifier, with its registration status. |
| Get Viber Sender Names | `getViberSenders` | Lists the Viber sender names registered on the SendPulse account, with the status of each one. |
| Get Web Push Campaign Statistics | `getWebPushCampaign` | Retrieves one web push campaign with its delivery and click statistics. |
| Get Web Push Campaigns | `getWebPushCampaigns` | Lists web push campaigns sent from the SendPulse account, optionally narrowed to one website and a date range. A single response returns at most 100 entries. |
| Get Web Push Website Information | `getWebPushWebsiteInfo` | Retrieves one web push website with its URL, status, icon and subscriber counts. |
| Get Web Push Website Script | `getWebPushWebsiteScript` | Returns the JavaScript snippet that collects web push subscribers for a website, as a script URL and a ready-to-paste script tag. |
| Get Web Push Website Subscriber Count | `getWebPushWebsiteSubscribersTotal` | Returns the total number of push subscribers registered for a website. |
| Get Web Push Website Subscribers | `getWebPushWebsiteSubscribers` | Lists the push subscribers of a website, with the browser, operating system, location and status of each subscriber. |
| Get Web Push Website Variables | `getWebPushWebsiteVariables` | Lists the personalisation variables defined for a web push website. |
| Get Web Push Websites | `getWebPushWebsites` | Lists the websites registered for web push notifications on the SendPulse account. |
| Get Web Push Websites Total | `getWebPushWebsitesTotal` | Returns the number of websites registered for web push notifications on the SendPulse account. |
| Get Webhook | `getWebhookById` | Returns a single SendPulse email-service webhook by its ID. |
| List All Senders | `getSenders` | Returns every sender email address registered on the SendPulse account with its activation status. |
| List Automation Events | `getAutomationEvents` | Lists the custom Automation 360 events defined on the SendPulse account, which are the triggers that start automation flows. |
| List Blacklisted Email Addresses | `getBlacklist` | Returns the email addresses on the SendPulse account blacklist, which are excluded from every campaign. |
| List Campaigns | `getCampaigns` | Returns the email campaigns in the SendPulse account with their delivery statistics. Filter by campaign status code using the status[] parameter, for example 26 for drafts and 3 for sent campaigns. |
| List Emails from Mailing List | `getEmailsFromMailingList` | Returns the contacts stored in a SendPulse mailing list with their subscription status and variables. Use the active and not_active filters to narrow the result to subscribed or unsubscribed contacts. |
| List Invited Users | `getInvitedUsers` | Returns the sub-accounts invited to this SendPulse account together with the permissions granted to each. |
| List Mailing Lists | `getMailingLists` | Returns every mailing list (address book) in the SendPulse account with its contact counts and status. |
| List SMTP Emails | `getSmtpEmails` | Returns transactional emails sent through the SendPulse SMTP service, with their delivery status and tracking data. |
| List Tags | `getTags` | Returns the contact tags created in the SendPulse account. Tags require the Pro plan or above in the Email section. |
| List Templates | `getTemplates` | Returns email templates available in SendPulse. Set owner to me for templates saved in the account or sendpulse for the built-in template gallery. SendPulse returns the full gallery in one response; the limit, offset and only_active parameters documented by the vendor are ignored by the API and are therefore not exposed here. |
| List Variables for Mailing List | `getMailingListVariables` | Returns the custom contact variables defined on a SendPulse mailing list, with the data type of each. |
| List Webhooks | `getWebhooks` | Returns every email-service webhook registered on the SendPulse account, one entry per tracked event. |
| Remove Email Addresses from Blacklist | `removeFromBlacklist` | Removes one or more email addresses from the SendPulse account blacklist. |
| Remove Phone Numbers from Mailing List | `removePhonesFromMailingList` | Removes phone numbers from a SendPulse mailing list. |
| Remove Phone Numbers from SMS Blacklist | `removePhonesFromSmsBlacklist` | Removes one or more phone numbers from the SendPulse SMS blacklist so they can receive SMS campaigns again. |
| Remove Phone Numbers from Viber Blacklist | `removePhonesFromViberBlacklist` | Removes one or more phone numbers from the Viber blacklist so they can receive Viber campaigns again. |
| Remove SMTP Recipients from Unsubscribed List | `removeSmtpUnsubscribe` | Removes email addresses from the SendPulse SMTP unsubscribe list so they can receive transactional email again. |
| Request Sender Activation Code | `requestSenderActivationCode` | Asks SendPulse to email a fresh activation code to a registered sender address. Sends a real email to that address. |
| Resubscribe SMTP Recipient | `resubscribeSmtpRecipient` | Sends a resubscription request email to a recipient who previously unsubscribed from transactional SMTP email. SendPulse allows five such emails per account per 24 hours. |
| Send SMS to Phone Numbers | `sendSmsToPhones` | Creates an SMS campaign for an explicit list of phone numbers rather than a saved mailing list. Set emulate to true to build the campaign without sending it. |
| Send SMTP Email | `sendSmtpEmail` | Sends a transactional email through the SendPulse SMTP service. Supply either html and text, or a saved template with its variables. Requires an activated SMTP account on the SendPulse plan. |
| Set Web Push Subscriber State | `setWebPushSubscriberState` | Activates or deactivates a single web push subscriber, controlling whether they continue to receive notifications. |
| Unassign Tag from Email Address | `unpinTagFromEmail` | Removes one or more SendPulse tags from an email contact. |
| Unassign Tag from Phone Number | `unpinTagFromPhone` | Removes one or more SendPulse tags from a phone contact. |
| Unsubscribe Contacts from Mailing List | `unsubscribeEmailsFromMailingList` | Marks the given email addresses as unsubscribed in a SendPulse mailing list without deleting them. |
| Unsubscribe SMTP Recipients | `unsubscribeSmtpRecipients` | Adds recipients to the SendPulse SMTP unsubscribe list so they stop receiving transactional email. |
| Update Phone Contact Variables | `updatePhoneContactVariables` | Updates the variables held against a single phone contact inside a SendPulse mailing list. Date values must use the YYYY-MM-DD format. |
| Update Phone Number Variables | `updatePhoneNumberVariables` | Updates the personalisation variables held against a set of phone numbers in a SendPulse mailing list. |
| Update Tag | `updateTag` | Renames a contact tag or changes its colour in the SendPulse account. |
| Update Variables for Contact in Mailing List | `updateContactVariables` | Updates the value of one or more custom variables for a single contact in a SendPulse mailing list. |
| Update Webhook | `updateWebhook` | Changes the handler URL of an existing SendPulse email-service webhook. |
| Verify Email Address | `verifyEmailAddress` | Submits a single email address to the SendPulse verification service. Read the verdict afterwards with Get Email Address Verification Result. |
| Verify Mailing List | `verifyMailingList` | Submits a mailing list to the SendPulse email verification service. Only one verification can run against a list at a time, and the list must not have been used in a campaign. |
| View Mailing List Verification Report | `viewMailingListVerificationReport` | Returns the contents of a previously generated mailing list verification report, with the verdict for every address it covers. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Campaign Status Changed | `task_status_update` | An email campaign changed status, for example from moderation to sending or to sent. SendPulse posts a JSON array of events every minute, or as soon as 100 events have accumulated. |
| Contact Added | `new_emails` | A contact was added to a mailing list. SendPulse batches deliveries and posts a JSON array of events every minute, or as soon as 100 events have accumulated. |
| Contact Deleted | `delete` | A contact was deleted from a mailing list. SendPulse posts a JSON array of events every minute, or as soon as 100 events have accumulated. |
| Contact Unsubscribed | `unsubscribe` | A contact unsubscribed from a mailing list or from all mailings. SendPulse posts a JSON array of events every minute, or as soon as 100 events have accumulated. |
| Email Delivered | `delivered` | A campaign email was accepted by the recipient's mail server. SendPulse posts a JSON array of events every minute, or as soon as 100 events have accumulated. |
| Email Opened | `open` | A recipient opened a campaign email. SendPulse posts a JSON array of events every minute, or as soon as 100 events have accumulated. |
| Hard Bounce | `hard_bounces` | A campaign email permanently failed to deliver, for example because the mailbox does not exist. SendPulse posts a JSON array of events every minute, or as soon as 100 events have accumulated. |
| Link Clicked | `redirect` | A recipient clicked a link in a campaign email. SendPulse posts a JSON array of events every minute, or as soon as 100 events have accumulated. |
| Marked as Spam | `spam` | A recipient marked a campaign email as spam. SendPulse posts a JSON array of events every minute, or as soon as 100 events have accumulated. |
| Soft Bounce | `soft_bounces` | A campaign email temporarily failed to deliver, for example because the mailbox is full. SendPulse posts a JSON array of events every minute, or as soon as 100 events have accumulated. |
