---
description: "Mailercloud email marketing platform."
hidden: true
---

# Mailercloud

Mailercloud email marketing platform. Manage lists, contacts, custom properties, segments, tags, senders, webforms, templates, automations and campaigns; send transactional and personalized email; and subscribe to delivery webhooks.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [mailercloud.com](https://mailercloud.com) |
| **Authentication** | API key |
| **Actions** | 65 |
| **Events** | 7 |
| **Slug** | `mailercloud` |

## Use it

Add Mailercloud from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mailercloud.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add a Domain | `addDomain` | Add a sending domain to your account and get the DNS records to publish at your DNS provider. The domain goes through exactly the same checks as **Account Settings → Domains** in the app (format, blocked and ISP domains, subdomain depth, duplicates and your plan's domain limit), and the same DNS records are generated. The response is the same domain object as **Get a Domain**: `status` is `not_verified` and each record is `pending` (the second DKIM record is `optional`), with a `message` saying what to do at your DNS provider. Open tracking is off for a new domain. After adding the records at your DNS provider, verify the domain from **Account Settings → Domains**. **Notes** - The domain is case-insensitive and a leading `www.` is removed (`WWW.Example.com` is saved as `example.com`). - Subdomains up to 3 levels below the root are allowed (`news.example.com`, `a.b.c.example.com`). - A |
| Add Email Suppressions | `addSuppressions` | Add email addresses to the Email API suppression list so no further mail is delivered to them on the chosen message stream. |
| Create Automation | `createAutomation` | Create an automation workflow from a trigger node and the action nodes that follow it. Every node needs a caller-supplied id that child nodes reference as parent_id, and list, webform, campaign and tag node fields take the object's NAME, not its id. Set auto_publish to false to save it as a draft. Mailercloud has no API to delete an automation, so anything created here must be removed in the web app. |
| Create Campaign | `createCampaign` | Create an email campaign against one or more lists. Prefer Create Campaign V2, which supports exclusions, tags, tracking and publish control. The sender email must already be verified on the account. |
| Create Campaign V2 | `createCampaignV2` | Create an email campaign with the newer endpoint: supports list, segment and tag targeting, exclusions, frequency capping, open and click tracking, and saving as a draft instead of publishing. The sender email must already be verified on the account. |
| Create Contact | `createContact` | Add a contact to a list. Email and list_id are required. If the contact already exists in the list the API answers with an 'already exists' message. Custom property values are passed in custom_fields keyed by property id. |
| Create Contact Property | `createContactProperty` | Create a custom contact property. Up to 100 custom properties can exist on an account. The property type cannot be changed after creation. |
| Create Contacts In Batch | `createBatchContacts` | Add many contacts to one list in a single call. Returns how many rows were submitted, inserted, updated and skipped. |
| Create List | `createList` | Create a new contact list. A list is where Mailercloud stores and manages the contacts you send campaigns to. |
| Create Or Update Contact | `upsertContact` | Create a contact if it does not exist in the list, or update it if it does. Returns the contact id and whether it was created or updated. |
| Create Segment | `createSegment` | Create a contact segment: a saved filter over one or more lists built from contact-detail, contact-property, tag or activity rules. The lists array takes list NAMES, not list ids. |
| Create Tag | `createTag` | Create a contact tag. Tags group contacts across lists and can be used as segment criteria. |
| Create Template | `createTemplate` | Create a reusable email template from HTML and plain text, filed under a template category. |
| Create Webhook | `createWebhook` | Register a webhook so an external system receives real-time notifications when the selected Mailercloud events occur. Returns the new webhook's id. |
| Delete Contact | `deleteContact` | Permanently delete a contact by its contact id. |
| Delete Contact Property | `deleteContactProperty` | Delete a custom contact property by id. A property that is in use by a webform cannot be deleted. |
| Delete List | `deleteList` | Permanently delete a contact list and its membership by id. Contacts that belong only to this list are removed with it. |
| Delete Tag | `deleteTag` | Delete a contact tag by id. The tag is detached from every contact that carries it. |
| Delete Webhook | `deleteWebhook` | Permanently delete a webhook subscription by id. No further events are delivered to its URL. |
| Find Template By Name Or ID | `findTemplate` | Look up a single email template by its exact name or by its id, returning the full template including AMP content. |
| Get a Domain | `getDomain` | Get one domain with its DNS records and the status of each record — the same records as **Account Settings → Domains** in the app. The response is the same domain object as **Add a Domain**. The statuses come from the last DNS check (domains are re-checked automatically). Each record has a `status` (`pending`, `verified`, `invalid`, or `optional` for the second DKIM record), a `message` saying what to do at your DNS provider (left out when the record is verified), and an `error_message` only when the record is `invalid`. **Tracking host (`mc.`)** - For a domain such as `example.com`, the tracking record's host is `mc.example.com`. - For a subdomain that already exists in your DNS, the host gets a `mc-` prefix instead, e.g. `mc-news.example.com`. - `mc.example.com` is never treated as `example.com`. If it is not used as a tracking host, it can be added as its own domain: it keeps its f |
| Get Automation | `getAutomation` | Get a single automation's details by id: its status, timing, contact counts, nodes, triggers and any campaigns it sends. |
| Get Campaign | `getCampaign` | Get a single campaign's full details by id, including its content, recipients, sender, schedule, status and report summary. |
| Get Campaign Domain Report | `getCampaignDomainReport` | Break a campaign's results down by recipient mailbox domain: sends, opens, clicks, bounces, spam complaints and unsubscribes per domain, with percentages. |
| Get Client Plan | `getClientPlan` | Get the Mailercloud account owner's details and contact quota: account email, name, plan name, and total, used and remaining contact allowance. Use it as a lightweight credential and quota check. |
| Get Contact | `getContact` | Get a contact's full details by contact id or by email address. Returns profile fields, list membership, tags, custom fields and tracking consent. |
| Get Inbox Tracking Report | `getInboxTrackingReport` | Get inbox placement statistics for a date range: the share of mail landing in the inbox, in spam or missed, broken down by campaign and by mailbox provider. |
| Get List | `getList` | Get the details of a single contact list by its id, including its name, type, status, contact count and open percentage. |
| Get Template | `getTemplate` | Get a single email template by id, including its HTML and plain-text bodies, category and status. |
| Get Template Categories | `getTemplateCategories` | List the template categories Mailercloud supports, each with its numeric id for use as categoryId when creating a template. |
| Get Webhook | `getWebhook` | Get a single webhook's details by id: its name, delivery URL, subscribed events and status. |
| List Campaign Clicks | `listCampaignClicks` | Page through the contacts who clicked a link in a given campaign, optionally restricted to a date range. |
| List Campaign Opens | `listCampaignOpens` | Page through the contacts who opened a given campaign, optionally restricted to a date range. |
| List Campaign Unsubscribes | `listCampaignUnsubscribes` | Page through the contacts who unsubscribed via a given campaign, with the reason each gave. |
| List Campaigns | `listCampaigns` | Search and page through the campaigns on the account, with each campaign's recipients, sender, schedule, status and full report summary. |
| List Contact Properties | `listContactProperties` | List the custom contact properties defined on the account. Properties store extra information on contact records and can be used to build segments. |
| List Contacts In List | `listContactsInList` | Page through all the contacts that belong to a given list, optionally narrowed by a search term matching name or email. |
| List Domains | `listDomains` | List the sending domains in your account with their status — the same domains and statuses as **Account Settings → Domains** in the app. Filter by `status` to find the domains that still need DNS work, and search by name. Each item has `id`, `domain`, `status`, `open_tracking` and `created_at` (in your account timezone, `YYYY-MM-DD HH:MM:SS`). Use **Get a Domain** for the DNS records. Domain status: - `verified` — the domain is authenticated and ready to send. - `not_verified` — the DNS records are not all in place yet (or not checked yet). - `failed` — at least one DNS record was found but is wrong (that record's `status` is `invalid`; see its `error_message` in Get a Domain). |
| List Email API Inbox Tracking Campaigns | `listEmailApiInboxTracking` | Page through inbox-placement results for Email API sends, with per-provider inbox, spam and missed percentages for each tracked campaign. |
| List Lists | `listLists` | Search and page through the contact lists in the Mailercloud account. Returns each list's id, name, type, status, contact count and open percentage. |
| List Reply Emails | `listReplyEmails` | List the reply-to email addresses registered on the account, with their verification status. |
| List Segments | `listSegments` | Search and page through the contact segments on the account. Returns each segment's name, source list and active contact count. |
| List Senders | `listSenders` | List the verified sender identities on the account. Only a verified sender email can be used as the from address of a campaign. |
| List Tags | `listTags` | Search and page through the contact tags defined on the account. |
| List Templates | `listTemplates` | Search and page through the email templates on the account, optionally including their HTML, AMP and plain-text content. |
| List Testmail Groups | `listTestmailGroups` | List the saved test-mail groups on the account. A test-mail group is a named set of addresses that campaign test sends can target. |
| List Webforms | `listWebforms` | List the signup webforms on the account with their embed code, linked list, status and view, submission and new-contact counts. |
| List Webhooks | `listWebhooks` | Search and page through the webhooks registered on the account. Also returns the account's webhook count and maximum webhook limit. |
| Reactivate Suppressed Recipient | `reactivateSuppression` | Remove one address from the Email API suppression list so it can receive mail again. |
| Remove Contact Tag | `removeContactTag` | Detach one or more tags from a single contact. Identify the contact with id and the tags to remove either by their tag ids or by their tag names. |
| Schedule Campaign | `scheduleCampaign` | Schedule a campaign for delivery. Omitting scheduled_at sends the campaign immediately, so only call this when you intend the campaign to go out to its real recipients. |
| Search Email Suppressions | `searchSuppressions` | List the recipients on the Email API suppression list, newest first, narrowed by search term, suppression reason, stream scope or date range. A suppressed recipient is rejected on every future send. |
| Send Campaign Test Email | `sendCampaignTestEmail` | Send a preview copy of a campaign to a single address or to a saved test-mail group. This delivers real mail, so only use addresses you control. |
| Send Personalized Email | `sendPersonalizedEmail` | Send one mail-merge email per recipient through the Email API, substituting each recipient's merge_vars into the subject and body. Delivers real mail to every recipient listed. |
| Send Transactional Email | `sendEmail` | Send a transactional email through the Mailercloud Email API: order confirmations, one-time passcodes, notifications. Delivers real mail to every recipient listed. |
| Test Webhook | `testWebhook` | Send a sample event payload to a registered webhook's delivery URL so you can confirm your endpoint receives and parses it. |
| Toggle Webhook Status | `toggleWebhookStatus` | Activate or pause a webhook without deleting it. |
| Update Campaign | `updateCampaign` | Update a campaign's content, recipients, sender or schedule. Lists, segments, pause rules and send rules cannot be changed while the campaign is sending; pause it first to edit its scheduled date. |
| Update Contact | `updateContact` | Update a contact's details by contact id or email. The list id and the email address themselves cannot be changed with this endpoint. |
| Update Contact Property | `updateContactProperty` | Rename a custom contact property or change its description. The property type cannot be edited. |
| Update List | `updateList` | Rename an existing contact list. Returns the updated list details. |
| Update Segment | `updateSegment` | Replace the name, match mode, source lists and rules of an existing segment. |
| Update Tag | `updateTag` | Rename an existing contact tag by id. |
| Update Template | `updateTemplate` | Update an existing email template's name, HTML, plain text or category. name is always required. Identify the template by its id or by its current name. VENDOR BLOCKER: as of 2026-09-22 this endpoint returns HTTP 500 for every well-formed request, including with a nonexistent id, while every other template endpoint works. |
| Update Webhook | `updateWebhook` | Replace a webhook's name, delivery URL and subscribed event list. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Campaign Error | `campaign_error` | Fired when a campaign fails to process or send. Payload schema is MODELLED from the Mailercloud webhook guide; no delivery was captured during build. |
| Campaign Link Clicked | `campaign_clicked` | Fired when a recipient clicks a link in a campaign. Payload schema is MODELLED from the Mailercloud webhook guide; no delivery was captured during build. |
| Campaign Opened | `campaign_opened` | Fired when a recipient opens a campaign email. Payload schema is MODELLED from the Mailercloud webhook guide; no delivery was captured during build. |
| Campaign Sent | `campaign_sent` | Fired for each recipient a campaign is delivered to. Payload schema below is MODELLED from the Mailercloud webhook guide - the vendor publishes no payload reference and no delivery could be captured during build. |
| Contact Unsubscribed | `unsubscribe` | Fired when a recipient unsubscribes via a campaign. Payload schema is MODELLED from the Mailercloud webhook guide; no delivery was captured during build. |
| Hard Bounce | `hard_bounce` | Fired when a campaign email permanently bounces. Payload schema is MODELLED from the Mailercloud webhook guide; no delivery was captured during build. |
| Spam Complaint | `spam` | Fired when a recipient marks a campaign as spam. Payload schema is MODELLED from the Mailercloud webhook guide; no delivery was captured during build. |
