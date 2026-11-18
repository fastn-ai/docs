---
description: "MailerSend is a transactional email and SMS platform."
---

# MailerSend

MailerSend is a transactional email and SMS platform. This connector covers the MailerSend v1 API: sending email and bulk email, templates, domains and their DNS, DKIM and SMTP users, sender identities, recipients and suppression lists, message and activity history, analytics, scheduled messages, email verification, inbound routing, SMS sending with its numbers, recipients and inbound routes, account users and API tokens, and webhook management for both email and SMS.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [mailersend.com](https://mailersend.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 129 |
| **Events** | 12 |
| **Slug** | `mailersend` |

## Use it

Add MailerSend from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mailersend.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Blocklist Recipients | `addBlocklistRecipients` | Adds addresses or domain patterns to the suppression blocklist for a sending domain, so MailerSend stops delivering to them. Supply Recipients for exact addresses, Patterns for wildcard rules such as *@example.com, or both. |
| Add DMARC Favorite IP | `addDmarcFavoriteIp` | Mark a sending IP as favorite. Docs: https://developers.mailersend.com/ |
| Add Domain | `addDomain` | Adds a sending domain to the account. The domain is created unverified; retrieve its DNS records with Get DNS Records, publish them, then poll Get Domain Verification Status. Note that MailerSend counts domains against the account plan. |
| Add Hard Bounces | `addHardBounces` | Manually adds recipients to the hard-bounce suppression list for a sending domain, so MailerSend stops delivering to them. Normally MailerSend populates this list itself from real bounces. |
| Add Inbound Route | `addInboundRoute` | Creates an inbound route that catches mail arriving at a MailerSend address and forwards it to your own endpoint. Inbound routing is a paid feature: on a trial or unentitled account MailerSend answers 403 {"message":"This action is unauthorized."}. |
| Add Sender Identity | `addSenderIdentity` | Adds a sender identity so one specific From address can send without verifying the whole domain. MailerSend emails a confirmation to that address, so only add an address you control - the identity stays unverified until the recipient clicks through. |
| Add SMS Inbound Route | `addSmsInboundRoute` | Creates an SMS inbound route that forwards SMS arriving at a MailerSend number to your own URL. Requires an SMS-enabled plan and an owned number. |
| Add Spam Complaints | `addSpamComplaints` | Manually adds recipients to the spam-complaint suppression list for a sending domain, so MailerSend stops delivering to them. Normally MailerSend populates this list from feedback loops. |
| Add Unsubscribes | `addUnsubscribes` | Manually adds recipients to the unsubscribe suppression list for a sending domain, so MailerSend stops delivering to them. Use this to honour opt-outs collected outside MailerSend. |
| Add User | `addUser` | Invites a person to this MailerSend account with a role and a set of permissions. MailerSend emails an invitation to the address, so only invite someone you intend to give real access to. Adding users requires an owner or admin token and may be gated on trial accounts with 403 {"message":"This action is unauthorized."}. |
| Cancel User Invite | `cancelInvite` | Cancel a user invite. Docs: https://developers.mailersend.com/ |
| Create Blocklist Monitor | `createBlocklistMonitor` | Create a blocklist monitor for an IP or domain. Docs: https://developers.mailersend.com/ |
| Create DMARC Monitor | `createDmarcMonitor` | Create a DMARC monitor for a domain. Docs: https://developers.mailersend.com/ |
| Create Email Verification List | `createEmailVerificationList` | Creates a bulk email-verification list from a set of addresses. Creating the list only uploads it - call Verify Email Verification List to start the run, then poll Get Email Verification List Results. Verification consumes email-verification credits. |
| Create SMS Webhook | `createSmsWebhook` | Registers an SMS webhook on a MailerSend phone number so SMS status events are POSTed to your URL. The response carries a signing secret used to verify each delivery. This is the subscribe call behind the connector's SMS event triggers. |
| Create SMTP User | `createSmtpUser` | Create an SMTP user for a domain. Docs: https://developers.mailersend.com/ |
| Create Template | `createTemplate` | Create an email template. Docs: https://developers.mailersend.com/ |
| Create Token | `createToken` | Creates a new API token with the scopes you choose, optionally limited to one sending domain (domain_id). The secret is returned ONCE in this response and can never be retrieved again, so capture it immediately. Treat the response as a credential. |
| Create Webhook | `createWebhook` | Registers an email webhook on a sending domain so MailerSend POSTs the chosen delivery events to your URL. The response carries a signing_secret used to verify each delivery's Signature header. This is the subscribe call behind the connector's email event triggers. |
| Delete Blocklist Monitor | `deleteBlocklistMonitor` | Delete a blocklist monitor. Docs: https://developers.mailersend.com/ |
| Delete Blocklist Recipients | `deleteBlocklistRecipients` | Removes entries from the suppression blocklist so MailerSend will deliver to those addresses again. Supply Ids to remove specific entries, or set All to true to clear the whole blocklist - which is irreversible and re-opens sending to every address previously blocked. |
| Delete DMARC Monitor | `deleteDmarcMonitor` | Delete a DMARC monitor. Docs: https://developers.mailersend.com/ |
| Delete Domain | `deleteDomain` | DANGER - permanently deletes a sending domain from the account. Everything sent through it stops working immediately and the deletion cannot be undone. On a trial account the auto-provisioned mlsender.net domain is the only way to send at all, so deleting it disables sending entirely. |
| Delete Hard Bounces | `deleteHardBounces` | Removes entries from the hard-bounce suppression list so MailerSend will attempt delivery to those addresses again. Supply Ids for specific entries or set All to true to clear the whole list - clearing it re-opens sending to addresses that genuinely bounced, which harms sender reputation. |
| Delete Inbound Route | `deleteInboundRoute` | Permanently deletes an inbound route. Mail arriving at its catch address stops being forwarded immediately. Inbound routing is a paid feature: on a trial or unentitled account MailerSend answers 403 {"message":"This action is unauthorized."}. |
| Delete On-hold Recipients | `deleteOnHoldList` | Remove recipients from the on-hold list (by ids or all). Docs: https://developers.mailersend.com/ |
| Delete Recipient | `deleteRecipient` | Permanently deletes a recipient and its stored send history from the account. This is the GDPR erasure path and cannot be undone. Returns 204 with no body. |
| Delete Scheduled Message | `deleteScheduledMessage` | Cancels a message that was queued for future delivery so it never sends. Only works while the message is still in the scheduled state; once it has gone out it cannot be recalled. Returns 204 with no body. |
| Delete Sender Identity | `deleteSenderIdentity` | Permanently deletes a sender identity by its id. That From address can no longer be used for sending unless its whole domain is verified. Returns 204 with no body. |
| Delete Sender Identity By Email | `deleteSenderIdentityByEmail` | Permanently deletes a sender identity addressed by its email rather than its id. That From address can no longer send unless its whole domain is verified. Returns 204 with no body. |
| Delete SMS Inbound Route | `deleteSmsInboundRoute` | Permanently deletes an SMS inbound route. SMS arriving at that number stops being forwarded immediately. Returns 204 with no body. |
| Delete SMS Phone Number | `deleteSmsPhoneNumber` | DANGER - permanently releases an SMS phone number from the account. The number is returned to the carrier pool, cannot be reclaimed, and every integration sending from it stops working. Returns 204 with no body. |
| Delete SMS Webhook | `deleteSmsWebhook` | Permanently deletes an SMS webhook. Deliveries to its URL stop immediately and the signing secret is destroyed. This is the unsubscribe call behind the connector's SMS event triggers. Returns 204 with no body. |
| Delete SMTP User | `deleteSmtpUser` | DANGER - permanently deletes an SMTP user from a sending domain. Any system relaying mail with those SMTP credentials stops working immediately and the credentials cannot be recovered. Returns 204 with no body. |
| Delete Spam Complaints | `deleteSpamComplaints` | Removes entries from the spam-complaint suppression list so MailerSend will deliver to those addresses again. Supply Ids for specific entries or set All to true to clear the whole list - re-sending to people who reported spam harms sender reputation. |
| Delete Template | `deleteTemplate` | Permanently deletes an email template. Any integration sending with this template id starts failing immediately. This route is absent from MailerSend's published OpenAPI specification but is live. |
| Delete Token | `deleteToken` | DANGER - permanently revokes an API token. Every integration using it starts failing with 401 immediately and the secret cannot be recovered. Deleting the token this connector authenticates with breaks the connector itself. Returns 200 with an empty body. |
| Delete Unsubscribes | `deleteUnsubscribes` | Removes entries from the unsubscribe suppression list so MailerSend will deliver to those addresses again. Supply Ids for specific entries or set All to true to clear the whole list - re-subscribing people who opted out is usually a compliance breach. |
| Delete User | `deleteUser` | DANGER - permanently removes a person's access to this MailerSend account. They are signed out immediately and must be re-invited to return. Requires an owner or admin token. Returns 204 with no body. |
| Delete Webhook | `deleteWebhook` | Permanently deletes an email webhook. Deliveries to its URL stop immediately and the signing secret is destroyed. This is the unsubscribe call behind the connector's email event triggers. Returns 204 with no body. |
| Get Activity | `getActivity` | Returns a single delivery activity event by its id, including the event type and the message it belongs to. Activity ids come from List Activities. An unknown id returns 404 {"message":"Resource not found."}. |
| Get Activity Data By Date | `getActivityDataByDate` | Returns counts of one delivery event grouped by day, week, month or year over a date range. MailerSend requires the event filter in PHP repeated-key form (event[]=sent); the fastn engine serialises an array query param as a single comma-joined value, which MailerSend rejects with 422 "The event must be an array." - so this action templates ONE event name into the URL and accepts a single Event per call. Call it once per event you need. Date To must be in the past. |
| Get API Quota | `getApiQuota` | Returns the account's API quota - the total allowance, how much remains, and when the counter resets. Useful for checking headroom before a bulk operation. |
| Get Async Email Verification Status | `getEmailVerificationAsyncStatus` | Get the result of an asynchronous email verification. Docs: https://developers.mailersend.com/ |
| Get Blocklist | `getBlocklist` | Returns the suppression blocklist - the addresses and domain patterns MailerSend refuses to send to, whether added manually or automatically. Optionally narrow to one sending domain. |
| Get Blocklist Monitor | `getBlocklistMonitor` | Get one blocklist monitor. Docs: https://developers.mailersend.com/ |
| Get Bulk Email Status | `getBulkEmailStatus` | Returns the state of a bulk email job, including how many messages were accepted, how many were rejected, and the per-message validation errors. This is the only place per-message errors from Send Bulk Email appear, because that call validates asynchronously. |
| Get DMARC Aggregated Report | `getDmarcReport` | Aggregated DMARC report of a monitor. Docs: https://developers.mailersend.com/ |
| Get DMARC Report By IP | `getDmarcReportByIp` | DMARC report rows for one sending IP. Docs: https://developers.mailersend.com/ |
| Get DMARC Report Sources | `getDmarcReportSources` | DMARC report sources (reporting organizations). Docs: https://developers.mailersend.com/ |
| Get DNS Records | `getDnsRecords` | Returns the DNS records that must be published to verify a domain for sending - the SPF, DKIM, Return-Path, custom tracking and inbound routing entries, each with its hostname, type and value. |
| Get Domain | `getDomain` | Returns a single sending domain by its id, with its verification state, tracking settings and delivery counters. |
| Get Domain Verification Status | `getDomainVerificationStatus` | Checks whether a domain's DNS records have propagated and the domain is verified for sending. Poll this after publishing the records returned by Get DNS Records. |
| Get Email | `getEmail` | Get one sent email with recipient and activity. Docs: https://developers.mailersend.com/ |
| Get Email Verification List | `getEmailVerificationList` | Returns a single bulk email-verification list by its id, with its address count, run status and the tally of each verification outcome. |
| Get Email Verification List Results | `getEmailVerificationListResults` | Returns the per-address results of a bulk email-verification list - each address with its individual verdict. Only populated once the run started by Verify Email Verification List has finished. |
| Get Hard Bounces | `getHardBounces` | Returns the hard-bounce suppression list - recipients whose address was permanently rejected by the receiving server, with the bounce reason. MailerSend will not send to these again until they are removed. |
| Get Inbound Route | `getInboundRoute` | Returns a single inbound route by its id, with its catch address, filters and forwarding targets. Inbound routing is a paid feature: on a trial or unentitled account MailerSend answers 403 {"message":"This action is unauthorized."}. |
| Get Message | `getMessage` | Returns one sent message by its id, with its domain, each recipient and that recipient's current delivery status. Message ids come from List Messages. |
| Get On-hold List | `getOnHoldList` | List recipients on hold. Docs: https://developers.mailersend.com/ |
| Get Opens By Country | `getOpensByCountry` | Returns how many opens came from each country over a date range, optionally narrowed to one domain, one set of recipients or one set of tags. Date From and Date To are Unix timestamps and both are required; the range must be at least one day. |
| Get Opens By Reading Environment | `getOpensByReadingEnvironment` | Returns how many opens came from each reading environment - webmail, mobile or desktop - over a date range. Date From and Date To are Unix timestamps and both are required. |
| Get Opens By User Agent | `getOpensByUserAgent` | Returns how many opens came from each email client or browser over a date range - the user-agent name breakdown. Date From and Date To are Unix timestamps and both are required. |
| Get Recipient | `getRecipient` | Returns one recipient by its id, with the address, the domain it belongs to and the recipient's full send history including every message and its status. |
| Get Recipients For Domain | `getRecipientsForDomain` | Returns the recipients that have been emailed through one sending domain, with each recipient's id, email address and creation time. Use List Recipients for the account-wide list. |
| Get Scheduled Message | `getScheduledMessage` | Returns a single scheduled message by its message id, including its subject, recipients, send time and current status. |
| Get Sender Identity | `getSenderIdentity` | Returns a single sender identity by its id, with its name, address, reply-to details and whether the owner has confirmed it. |
| Get Sender Identity By Email | `getSenderIdentityByEmail` | Returns a sender identity looked up by its email address rather than its id - useful when you hold the From address but not the identity id. |
| Get SMS Inbound Route | `getSmsInboundRoute` | Returns a single SMS inbound route by its id, with its filter, forwarding URL, enabled flag and signing secret. |
| Get SMS Message | `getSmsMessage` | Returns one SMS message by its id, with the sending number, the text, every recipient and each recipient's delivery status. |
| Get SMS Phone Number | `getSmsPhoneNumber` | Returns one owned SMS phone number by its id, with its E.164 number and whether sending from it is paused. |
| Get SMS Recipient | `getSmsRecipient` | Returns one SMS recipient by its id, with its phone number, opt-out status and the SMS messages sent to it. |
| Get SMS Webhook | `getSmsWebhook` | Returns a single SMS webhook by its id, with its URL, subscribed events, enabled flag and signing secret. |
| Get SMTP User | `getSmtpUser` | Returns a single SMTP user on a sending domain by its id, with its username, server, port and enabled flag. Ids come from List SMTP Users. |
| Get Spam Complaints | `getSpamComplaints` | Returns the spam-complaint suppression list - recipients who marked mail from this account as spam. MailerSend will not send to them again until they are removed. |
| Get Template | `getTemplate` | Returns a single email template by its id, including its content and the domain it belongs to. This route is absent from MailerSend's published OpenAPI specification but is live: an unknown id returns the JSON resource-404 rather than the HTML router-404. |
| Get Token | `getToken` | Returns a single API token's metadata by its id - name, status, scopes and bound domain. The token secret is never returned. This route is absent from MailerSend's published OpenAPI specification but is live: an unknown id answers with the JSON resource-404 rather than the HTML router-404. |
| Get Unsubscribes | `getUnsubscribes` | Returns the unsubscribe suppression list - recipients who opted out, with the reason they gave. MailerSend will not send to them again until they are removed. |
| Get User | `getUser` | Returns a single account user by id, with their email, role, permissions and the domains and templates they may reach. Ids come from List Users. |
| Get User Invite | `getInvite` | Get one user invite. Docs: https://developers.mailersend.com/ |
| Get Webhook | `getWebhook` | Returns a single email webhook by its id, with its URL, subscribed events, enabled flag and signing secret. |
| List Activities | `listActivities` | Returns the delivery activity for one sending domain - every queued, sent, delivered, soft-bounced, hard-bounced, opened, clicked, unsubscribed, spam-complaint and survey event, newest first. Date From and Date To are Unix timestamps and BOTH ARE REQUIRED: MailerSend answers 422 "The date from field is required. #MS42209" without them, despite its documentation listing them as optional. The window may not be wider than one day, so page through longer periods a day at a time. |
| List Blocklist Monitors | `listBlocklistMonitors` | List IP/domain blocklist monitors. Docs: https://developers.mailersend.com/ |
| List DMARC Monitors | `listDmarcMonitors` | List DMARC monitors. Docs: https://developers.mailersend.com/ |
| List Domains | `listDomains` | Returns the sending domains on the account, each with its DKIM, SPF and DNS verification state, its tracking settings and its lifetime delivery counters. |
| List Email Verification Lists | `listEmailVerificationLists` | Returns the bulk email-verification lists on the account, each with its id, name, total address count, verification status and per-result counts. |
| List Emails | `listEmails` | List sent emails with filters (domain and date range required). Docs: https://developers.mailersend.com/ |
| List Inbound Routes | `listInboundRoutes` | Returns the inbound routes on the account - the rules that forward mail arriving at a MailerSend address to your own endpoint. Inbound routing is a paid feature: on a trial or unentitled account MailerSend answers 403 {"message":"This action is unauthorized."}. |
| List Messages | `listMessages` | Returns the API messages sent from the account, newest first, each with its message id and creation time. A message is one Send Email or Send Bulk Email request; use Get Message for its recipients and per-recipient delivery state. |
| List Recipients | `listRecipients` | Returns every recipient the account has emailed, each with its id, address and creation time. Optionally narrow to one sending domain. |
| List Scheduled Messages | `listScheduledMessages` | Returns messages that were queued with a future Send At and have not gone out yet, with their subject, send time and status. Use Delete Scheduled Message to cancel one before it sends. |
| List Sender Identities | `listSenderIdentities` | Returns the sender identities on the account - individual From addresses that have been confirmed for sending without owning the whole domain. Each carries its id, name, email, verification state and the domain it belongs to. |
| List SMS Activities | `listSmsActivities` | Returns SMS delivery activity across the account, each entry with the message, its recipient and its current status. Requires an SMS-enabled plan. |
| List SMS Inbound Routes | `listSmsInboundRoutes` | Returns the SMS inbound routes on the account - the rules that forward SMS arriving at a MailerSend number to your own endpoint. Requires an SMS-enabled plan. |
| List SMS Messages | `listSmsMessages` | Returns the SMS messages sent from the account, newest first, each with its id and creation time. Requires an SMS-enabled plan. |
| List SMS Phone Numbers | `listSmsPhoneNumbers` | Returns the SMS phone numbers owned by the account, each with its id, E.164 number and paused flag. These are the only valid From values for Send SMS. Requires an SMS-enabled plan. |
| List SMS Recipients | `listSmsRecipients` | Returns the phone numbers the account has sent SMS to, each with its id, number and status - active or opted out. Requires an SMS-enabled plan. |
| List SMS Webhooks | `listSmsWebhooks` | Returns the SMS webhooks registered on one MailerSend phone number, each with its URL, subscribed events, enabled flag and signing secret. SMS Number ID is required - without it MailerSend answers 422. |
| List SMTP Users | `listSmtpUsers` | Returns the SMTP users configured on one sending domain, each with its id, name, username, server, port and enabled flag. These are the credentials used to relay mail through MailerSend's SMTP service rather than the HTTP API. |
| List Templates | `listTemplates` | Returns the email templates on the account, optionally narrowed to one domain. Template ids from here are what Send Email and Send Bulk Email accept as Template ID. |
| List Tokens | `listTokens` | Returns the API tokens on the account, each with its id, name, status, scopes and the domain it is bound to. The token values themselves are never returned - only the metadata. This route is absent from MailerSend's published OpenAPI specification but is live and returns real data. |
| List User Invites | `listInvites` | List pending user invites. Docs: https://developers.mailersend.com/ |
| List Users | `listUsers` | Returns the people with access to this MailerSend account, each with their id, email, name, role, permissions and the domains and templates they may reach. |
| List Webhooks | `listWebhooks` | Returns the email webhooks registered on one sending domain, each with its id, name, URL, subscribed events, enabled flag and signing secret. Domain ID is required - without it MailerSend answers 422. |
| Remove DMARC Favorite IP | `removeDmarcFavoriteIp` | Remove a favorite IP. Docs: https://developers.mailersend.com/ |
| Resend Sender Identity Verification | `resendSenderIdentityVerification` | Resend the confirmation email of a sender identity. Docs: https://developers.mailersend.com/ |
| Resend User Invite | `resendInvite` | Resend a user invite email. Docs: https://developers.mailersend.com/ |
| Send Bulk Email | `sendBulkEmail` | DANGER - sends up to 500 real transactional emails in one request. Every message reaches a real inbox, none can be recalled, and there is no sandbox flag. MailerSend requires the request body to be a BARE JSON ARRAY of messages rather than an object wrapping them, and the fastn engine cannot emit an array-valued input at the body root - so Messages JSON is taken as a raw JSON string and written straight into the body. Pass a JSON array whose entries are shaped exactly like a Send Email request, for example [{"from":{"email":"you@your-domain.com"},"to":[{"email":"a@b.com"}],"subject":"Hi","text":"Hello"}]. The call answers 202 with a bulk_email_id IMMEDIATELY and validates ASYNCHRONOUSLY - a 202 does NOT mean the messages were accepted, so always poll Get Bulk Email Status and check validation_errors_count and total_recipients_count. |
| Send Email | `sendEmail` | DANGER - sends a real transactional email that reaches a real inbox and cannot be recalled. There is no sandbox flag on this endpoint. Trial accounts may only send to the account administrator's own address and are capped by the daily quota. Supply either Text/HTML or a Template ID. Setting Send At schedules the message instead of sending it now, so omitting Send At means it goes immediately. Returns 202 Accepted with the message id in the X-Message-Id response header - which fastn does not expose, so use List Messages to find the id afterwards. |
| Send SMS | `sendSms` | DANGER - sends a real SMS to real phones and costs real money per message; it cannot be recalled and there is no sandbox flag. Requires an SMS-enabled plan and a purchased MailerSend phone number as From. Accounts without SMS get 403 {"message":"This action is unauthorized."}. |
| Send WhatsApp Message | `sendWhatsApp` | Send a WhatsApp template message (paid add-on). Docs: https://developers.mailersend.com/ |
| Update Blocklist Monitor | `updateBlocklistMonitor` | Update a blocklist monitor. Docs: https://developers.mailersend.com/ |
| Update DMARC Monitor | `updateDmarcMonitor` | Set the wanted DMARC record of a monitor. Docs: https://developers.mailersend.com/ |
| Update Domain Settings | `updateDomainSettings` | Updates a domain's sending and tracking settings. Only the fields you supply are changed. WARNING - setting Send Paused to true stops the domain sending any email at all, which silently breaks every integration using it. |
| Update Inbound Route | `updateInboundRoute` | Updates an inbound route's name, filters or forwarding targets. Inbound routing is a paid feature: on a trial or unentitled account MailerSend answers 403 {"message":"This action is unauthorized."}. |
| Update Sender Identity | `updateSenderIdentity` | Updates a sender identity by its id. Changing Email sends a fresh confirmation message to the new address and resets the identity to unverified. |
| Update Sender Identity By Email | `updateSenderIdentityByEmail` | Updates a sender identity addressed by its current email rather than its id. Changing Email sends a fresh confirmation message and resets the identity to unverified. |
| Update SMS Inbound Route | `updateSmsInboundRoute` | Changes an SMS inbound route's name, filter, forwarding URL or enabled flag. Setting Enabled to false silently stops forwarding while leaving the route in place. |
| Update SMS Phone Number | `updateSmsPhoneNumber` | Pauses or resumes an owned SMS phone number. Setting Paused to true stops every send from that number immediately, which silently breaks any integration using it as From. |
| Update SMS Recipient | `updateSmsRecipient` | Changes an SMS recipient's status between active and opted out. Moving someone back to active after they opted out re-opens sending to them and is usually a compliance breach. |
| Update SMS Webhook | `updateSmsWebhook` | Changes an SMS webhook's URL, name, subscribed events or enabled flag. Setting Enabled to false silently stops deliveries while leaving the webhook in place. |
| Update SMTP User | `updateSmtpUser` | Renames an SMTP user or enables and disables it. Setting Enabled to false stops that username relaying mail immediately, which breaks any system using those SMTP credentials. |
| Update Template | `updateTemplate` | Updates an email template in place (PUT /v1/templates/{template_id}). Send only the fields you want to change. Every send already referencing this template id picks up the change immediately. |
| Update Token | `updateToken` | Rename or pause/unpause an API token. Docs: https://developers.mailersend.com/ |
| Update User | `updateUser` | Changes an account user's role, permissions or the domains and templates they may reach. Narrowing a colleague's role revokes their access immediately. Requires an owner or admin token; a token without that privilege gets 403 {"message":"This action is unauthorized."}. |
| Update Webhook | `updateWebhook` | Changes an email webhook's URL, name, subscribed events or enabled flag. Setting Enabled to false silently stops deliveries while leaving the webhook in place. |
| Verify Email | `verifyEmail` | Verifies one email address on the spot and returns its deliverability status - valid, catch_all, mailbox_full, role_based, unknown, failed, disposable, syntax_error, typo, mailbox_not_found or disabled. Each call consumes one email-verification credit. |
| Verify Email Async | `verifyEmailAsync` | Start an asynchronous single-email verification. Docs: https://developers.mailersend.com/ |
| Verify Email Verification List | `verifyEmailVerificationList` | Starts verification of a bulk email-verification list that has already been created. Despite verifying, this is a GET. The run is asynchronous - poll Get Email Verification List for status and Get Email Verification List Results for the per-address verdicts. It consumes one email-verification credit per address. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Email Delivered | `activity.delivered` | The receiving server confirmed delivery to the recipient's mailbox. Modelled from MailerSend's documented webhook sample - not captured live (trial quota). |
| Email Hard Bounced | `activity.hard_bounced` | Delivery failed permanently; MailerSend adds the address to the hard-bounce suppression list. Modelled from MailerSend's documented webhook sample. |
| Email Opened | `activity.opened` | The recipient opened the message; requires open tracking on the domain. Fires on every open. Modelled from MailerSend's documented webhook sample. |
| Email Opened (First Time) | `activity.opened_unique` | The recipient opened the message for the first time. Modelled from MailerSend's documented webhook sample. |
| Email Sent | `activity.sent` | MailerSend accepted the message and handed it to the receiving server. Fires once per recipient. Modelled from MailerSend's documented webhook sample - not captured live, because this trial account's daily API quota does not allow a real delivery to be driven. |
| Email Soft Bounced | `activity.soft_bounced` | Delivery failed for a temporary reason such as a full mailbox and will be retried. Modelled from MailerSend's documented webhook sample. |
| Link Clicked | `activity.clicked` | The recipient clicked a tracked link; requires click tracking on the domain. Modelled from MailerSend's documented webhook sample. |
| Link Clicked (First Time) | `activity.clicked_unique` | The recipient clicked a tracked link for the first time. Modelled from MailerSend's documented webhook sample. |
| Recipient Unsubscribed | `activity.unsubscribed` | The recipient used the unsubscribe link; MailerSend adds them to the unsubscribe suppression list. Modelled from MailerSend's documented webhook sample. |
| Spam Complaint | `activity.spam_complaint` | The recipient marked the message as spam; MailerSend adds them to the spam-complaint suppression list. Modelled from MailerSend's documented webhook sample. |
| Survey Opened | `activity.survey_opened` | The recipient opened an embedded MailerSend survey. Modelled from MailerSend's documented webhook sample. |
| Survey Submitted | `activity.survey_submitted` | The recipient submitted an embedded MailerSend survey. Modelled from MailerSend's documented webhook sample. |
