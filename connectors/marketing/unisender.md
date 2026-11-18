---
description: "Unisender email and SMS marketing platform."
hidden: true
---

# Unisender

<img src="../../.gitbook/assets/connectors/unisender.png" alt="Unisender logo" width="64">

Unisender email and SMS marketing platform. Single-URL RPC API at https://api.unisender.com/ru/api/&lt;method&gt; covering contact lists, subscribers, custom fields, tags, notes, email/SMS messages, campaigns, templates and delivery statistics.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [unisender.com](https://unisender.com) |
| **Authentication** | API key |
| **Slug** | `unisender` |

## Use it

Add Unisender from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.unisender.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Campaign | `cancelCampaign` | Cancels a scheduled campaign that has not started sending yet. Campaigns already in progress or finished cannot be cancelled. |
| Check Contact List Membership | `isContactInLists` | Checks whether a contact belongs to the given lists and returns a single boolean. With condition 'and' the contact must be in every list, with 'or' in at least one. |
| Check Email Delivery Status | `checkEmail` | Returns the delivery status of one or more individual emails previously sent with Send Email, looked up by the email_id those calls returned. |
| Check SMS Delivery Status | `checkSms` | Returns the delivery status of an individual SMS previously sent with Send SMS, looked up by the sms_id that call returned. |
| Create Campaign | `createCampaign` | Schedules a stored message for delivery to its list, immediately when start_time is omitted. This dispatches real mail or SMS to every contact in the list and consumes quota or balance. Returns the campaign_id and recipient count. |
| Create Contact List | `createList` | Creates a new contact list. The title must be unique within the account or Unisender returns an invalid_arg error. Returns the new list id. |
| Create Custom Field | `createField` | Creates a new custom contact field. The name is the substitution variable and must be unique, start with a Latin letter and contain only Latin letters, digits and underscores. Returns the new field id. |
| Create Email Message | `createEmailMessage` | Creates a reusable email message tied to a list. The message is stored only; nothing is sent until Create Campaign schedules it. The sender email must already be a confirmed return address on the account. Returns the new message_id. |
| Create Email Template | `createEmailTemplate` | Creates a reusable email template that Create Email Message can later be based on. Returns the new template id. |
| Create SMS Message | `createSmsMessage` | Creates a reusable SMS message tied to a list. The message is stored only; nothing is sent until Create Campaign schedules it. The sender alias must be registered with Unisender. Returns the new message_id. |

<details>

<summary>See 50 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Subscriber Note | `createSubscriberNote` | Attaches a free-text note to one contact. Returns the new note id. |
| Delete Contact List | `deleteList` | Permanently deletes a contact list. Contacts themselves are not deleted, only their membership of this list. Returns an empty result object on success. |
| Delete Contact Tag | `deleteTag` | Permanently deletes a contact tag and removes it from every contact it was applied to. |
| Delete Custom Field | `deleteField` | Permanently deletes a custom contact field and all values stored in it for every contact. |
| Delete Email Template | `deleteTemplate` | Permanently deletes a user email template. Messages already created from it are not affected. |
| Delete Message | `deleteMessage` | Permanently deletes a stored email or SMS message. Messages already used by a sent campaign cannot be removed. |
| Delete Subscriber Note | `deleteSubscriberNote` | Permanently deletes one contact note by its id. |
| Exclude Contact From Lists | `exclude` | Removes a contact from the given lists without marking it unsubscribed, so its subscription status elsewhere is untouched. Omit list ids to exclude the contact from every list. |
| Export Contacts | `asyncExportContacts` | Queues an asynchronous export of contact data and returns a task_uuid. Poll Get Task Result with that uuid, or supply notify_url to be called when the export file is ready. Limited to 20 requests per minute by Unisender. |
| Get Actual Message Version | `getActualMessageVersion` | Returns the id of the currently active version of a stored message, so edits made after a campaign was created can be detected. |
| Get Async Task Result | `asyncGetTaskResult` | Returns the status and, once ready, the download URL of an asynchronous job started by Export Contacts or Get Campaign Delivery Stats. Status moves from new to processing to completed. |
| Get Campaign Common Stats | `getCampaignCommonStats` | Returns aggregate delivery statistics for one campaign: totals for sent, delivered, read, clicked, unsubscribed, spam complaints and errors. |
| Get Campaign Delivery Stats | `asyncGetCampaignDeliveryStats` | Queues an asynchronous per-recipient delivery report for one campaign and returns a task_uuid. Poll Get Async Task Result with that uuid, or supply notify_url. Only campaigns sent within the last 180 days can be reported on. |
| Get Campaign Status | `getCampaignStatus` | Returns the current sending status of one campaign, such as waiting, scheduled, in_progress, completed or cancelled, together with its creation and start times. |
| Get Campaign Web Version | `getWebVersion` | Returns the public web-version URL of a sent campaign, the page recipients reach through the 'view in browser' link. |
| Get Campaigns | `getCampaigns` | Returns campaigns created in the given time window with their id, start time, status, message id, subject, sender and recipient count. Without a window Unisender returns the most recent campaigns. |
| Get Contact | `getContact` | Returns a single contact looked up by email address, optionally including its list memberships, custom field values and extended details such as delivery history. |
| Get Contact Count In List | `getContactCount` | Returns how many contacts are in one list, optionally narrowed by tag, by channel type (address or phone) and by an email or phone substring search. |
| Get Contact Field Values | `getContactFieldValues` | Returns the values a single contact holds for the requested custom fields, keyed by field id. Identify the contact by email address. |
| Get Contact Lists | `getLists` | Returns every contact list in the Unisender account as an array of objects with id and title. Use the returned id wherever a list_id is required. |
| Get Contact Tags | `getTags` | Returns every contact tag defined in the account with its id and name. Tags are created implicitly by Subscribe Contact and Import Contacts. |
| Get Custom Fields | `getFields` | Returns every custom contact field defined in the account, with its id, substitution name, public name, type, visibility and sort order. |
| Get Email Template | `getTemplate` | Returns one email template in full, including its HTML body. Pass either a user template id or a Unisender system template id. |
| Get Message | `getMessage` | Returns one stored email or SMS message in full, including subject, body, sender and the list it belongs to. |
| Get Messages With Bodies | `getMessages` | Returns stored messages created in a date window, including their full bodies. Both date bounds are required. Use List Messages instead when only the metadata is needed. |
| Get Sender Domain List | `getSenderDomainList` | Returns the sender domains registered on the account with their DKIM, SPF and DMARC verification status, so a caller can tell which from-addresses are usable. |
| Get Subscriber Note | `getSubscriberNote` | Returns one contact note by its id, with its content and creation and update timestamps. |
| Get Subscriber Notes | `getSubscriberNotes` | Returns every note attached to one contact, paged and sortable by creation or update time. |
| Get Templates | `getTemplates` | Returns the full list of email templates in the account, including each template's body. Optionally filter by template type (user or system) and creation date range, and page with limit and offset. |
| Get Total Contacts Count | `getTotalContactsCount` | Returns the total number of contacts stored in an account, across every list. Pass the account login returned by Get User Info. |
| Get User Info | `getUserInfo` | Returns the Unisender account profile for the API key: id, login, email, tariff plan, balance, currency, email quota used and remaining, and subscriber counts. |
| Get Visited Links | `getVisitedLinks` | Returns the link clicks recorded for one campaign, either one row per click with the recipient email, or aggregated per URL when grouping is requested. |
| Import Contacts | `importContacts` | Bulk-adds or updates up to three contacts per call. Name the columns in the field_names slots (the first must be 'email') and fill the matching data cells for each row. Rows whose email is new are added; existing emails are updated. No confirmation email is sent by this method. Returns inserted, updated and new_emails counts plus per-row log entries. |
| List Email Templates | `listTemplates` | Returns email templates as a lightweight list without their bodies. Use Get Templates when the HTML body is needed too. |
| List Messages | `listMessages` | Returns stored messages as a lightweight list without their bodies: id, sub_user_login, list_id, segment, created, updated, service_type, active_version_id, message_format, type, name and subject. |
| List Webhook Handlers | `listHooks` | Returns every webhook handler registered on the account with its id, URL, payload format, subscribed events and active status. |
| Remove Webhook Handler | `removeHook` | Deletes the webhook handler registered for a URL, stopping all event delivery to it. The URL is the handler's identifier. |
| Send Email | `sendEmail` | Sends a single transactional email immediately to one recipient and returns its email_id. This dispatches real mail and consumes the account's email quota - it is not a draft. The sender address must be a confirmed return address. Use Check Email Delivery Status afterwards to follow the outcome. |
| Send SMS | `sendSms` | Sends an SMS immediately to one or more phone numbers and returns its sms_id. This dispatches real text messages and charges the account balance. The sender alias must be registered with Unisender. |
| Send Test Email | `sendTestEmail` | Sends a preview copy of a stored email message to one or more addresses. This dispatches real mail; the recipients must already exist as contacts in the account. |
| Set Webhook Handler | `setHook` | Registers or replaces the webhook handler for a URL and selects which events it receives. Unisender first sends an empty GET to the URL and only accepts the handler if it answers 200. Calling it again with the same hook_url replaces the existing handler. |
| Subscribe Contact | `subscribe` | Adds a single contact to one or more lists and sets its field values and tags. WARNING: double_optin 0 or 4 causes Unisender to send a real confirmation email to the address. Use double_optin 3 to add the contact silently. Returns the person_id of the contact. |
| Track Customer Event | `trackEvent` | Sends a customer behaviour event (purchase, abandoned cart, registration) to the Unisender Event Tracking API on event.unisender.com, attaching it to a contact by email so it can be used for segmentation. The event name must already exist in the account's Event Manager. This endpoint authenticates with a Bearer header rather than the api_key parameter used by the main API. |
| Unsubscribe Contact | `unsubscribe` | Marks a contact as unsubscribed from the given lists, or from every list when no list ids are supplied. The contact record is kept but will no longer receive campaigns. |
| Update Contact List | `updateList` | Renames an existing contact list or changes its before/after subscribe redirect URLs. Returns an empty result object on success. |
| Update Custom Field | `updateField` | Renames an existing custom contact field and updates its display label. The field type cannot be changed. |
| Update Email Message | `updateEmailMessage` | Edits a stored email message that has not been sent yet. Only the supplied fields are changed. Returns the message id. |
| Update Email Template | `updateEmailTemplate` | Edits an existing email template. Only the supplied fields are changed; everything else keeps its current value. |
| Update Opt-In Confirmation Email | `updateOptInEmail` | Replaces the double opt-in confirmation email that Unisender sends to new subscribers of one list. |
| Update Subscriber Note | `updateSubscriberNote` | Replaces the text of an existing contact note. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Account Payment Recorded | `user_payment` | A payment was credited to the Unisender account. event_data carries the payment amount and currency. payloadSchema MODELLED from the vendor's documented sample. |
| Account Profile Changed | `user_info` | The Unisender account profile or tariff changed. event_data carries the changed profile fields. payloadSchema MODELLED from the vendor's documented sample. |
| Campaign Status Changed | `campaign_status` | A campaign changed state (scheduled, in progress, completed, cancelled). event_data carries campaign_id and status. payloadSchema MODELLED from the vendor's documented sample. |
| Contact Subscribed | `subscribe` | A contact subscribed or confirmed a subscription (delivered as event_name 'activate' for double opt-in confirmations). event_data carries email and list_id. payloadSchema MODELLED from the vendor's documented sample. |
| Contact Unsubscribed | `unsubscribe` | A contact unsubscribed. event_data carries email, campaign_id and list_id ('0' means unsubscribed from every list). payloadSchema MODELLED from the vendor's documented sample. |
| Email Address Check Completed | `email_check` | An address-verification check finished. event_data carries email and the check result. payloadSchema MODELLED from the vendor's documented sample. |
| Email Delivery Status Changed | `email_status` | Delivery status of a message changed (sent, delivered, opened, bounced, ...). event_data carries email, status, status_group and either email_id (sendEmail) or campaign_id (createCampaign). payloadSchema is MODELLED from Unisender's documented sample, not captured - the sandbox account cannot dispatch mail (no confirmed sender). |
| Spam Complaint Received | `spam` | A recipient reported a message as spam. event_data carries email and campaign_id. payloadSchema MODELLED from the vendor's documented sample. |
