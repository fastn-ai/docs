---
description: "Resend is the email platform for developers."
hidden: true
---

# Resend

<img src="../../.gitbook/assets/connectors/lg/resend.png" alt="Resend logo">

Resend is the email platform for developers. Send transactional and marketing emails, manage domains, API keys, audiences, contacts, segments, topics, broadcasts, templates, automations, events and webhooks. — Public 2026-09-29: Send Email verified live (HTTP 200); other endpoints gated by a send-only API key, not a config defect.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [resend.com](https://resend.com) |
| **Authentication** | Bearer token |
| **Slug** | `resend` |

## Use it

Add Resend from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.resend.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Contact To Segment | `addContactToSegment` | Add a contact to a segment. |
| Cancel Email | `cancelEmail` | Cancel the scheduled send of an email. |
| Create API Key | `createApiKey` | Create a new Resend API key. |
| Create Audience | `createAudience` | Create a new audience (a list of contacts). |
| Create Automation | `createAutomation` | Create an automation workflow. Provide steps and connections as JSON arrays. |
| Create Broadcast | `createBroadcast` | Create a broadcast (an email sent to a segment). |
| Create Contact | `createContact` | Create a new contact. |
| Create Contact Property | `createContactProperty` | Create a new custom contact property. |
| Create Domain | `createDomain` | Create (register) a new sending domain. |
| Create Event | `createEvent` | Create a custom event definition. |

<details>

<summary>See 73 more actions</summary>

* **Create Segment** `createSegment`: Create a new segment.
* **Create Template** `createTemplate`: Create a new email template.
* **Create Topic** `createTopic`: Create a new topic for managing contact subscriptions.
* **Create Webhook** `createWebhook`: Register a new webhook endpoint subscribed to a set of event types.
* **Delete API Key** `deleteApiKey`: Remove an existing API key.
* **Delete Audience** `deleteAudience`: Remove an existing audience.
* **Delete Automation** `deleteAutomation`: Delete an automation.
* **Delete Broadcast** `deleteBroadcast`: Remove a broadcast that is in draft status.
* **Delete Contact** `deleteContact`: Remove an existing contact by ID or email.
* **Delete Contact Property** `deleteContactProperty`: Remove an existing contact property.
* **Delete Domain** `deleteDomain`: Remove an existing domain.
* **Delete Event** `deleteEvent`: Delete a custom event definition.
* **Delete Segment** `deleteSegment`: Remove an existing segment.
* **Delete Template** `deleteTemplate`: Remove an existing template.
* **Delete Topic** `deleteTopic`: Remove an existing topic.
* **Delete Webhook** `deleteWebhook`: Remove an existing webhook.
* **Duplicate Template** `duplicateTemplate`: Duplicate an existing template.
* **Get Contact Topics** `getContactTopics`: Retrieve the topic subscriptions for a contact.
* **Get Email Attachment** `getEmailAttachment`: Retrieve a single attachment for a sent email.
* **Get Received Email** `getReceivedEmail`: Retrieve a single received (inbound) email by ID.
* **Get Received Email Attachment** `getReceivedEmailAttachment`: Retrieve a single attachment for a received email.
* **List API Keys** `listApiKeys`: Retrieve a list of all API keys.
* **List Audiences** `listAudiences`: Retrieve a list of all audiences.
* **List Automation Runs** `listAutomationRuns`: Retrieve a list of runs for an automation.
* **List Automations** `listAutomations`: Retrieve a list of automations.
* **List Broadcasts** `listBroadcasts`: Retrieve a list of broadcasts.
* **List Contact Properties** `listContactProperties`: Retrieve a list of contact properties.
* **List Contact Segments** `listContactSegments`: Retrieve the list of segments a contact belongs to.
* **List Contacts** `listContacts`: Retrieve a paginated list of contacts, optionally filtered by segment.
* **List Domains** `listDomains`: Retrieve a list of all domains in the account.
* **List Email Attachments** `listEmailAttachments`: Retrieve the list of attachments for a sent email.
* **List Emails** `listEmails`: Retrieve a paginated list of sent emails.
* **List Events** `listEvents`: Retrieve a list of custom event definitions.
* **List Logs** `listLogs`: Retrieve a list of API request logs.
* **List Received Email Attachments** `listReceivedEmailAttachments`: Retrieve the list of attachments for a received email.
* **List Received Emails** `listReceivedEmails`: Retrieve a paginated list of received (inbound) emails.
* **List Segments** `listSegments`: Retrieve a list of segments.
* **List Templates** `listTemplates`: Retrieve a list of templates.
* **List Topics** `listTopics`: Retrieve a list of topics.
* **List Webhooks** `listWebhooks`: Retrieve a list of registered webhooks.
* **Publish Template** `publishTemplate`: Publish a template so it can be used to send emails.
* **Remove Contact From Segment** `removeContactFromSegment`: Remove a contact from a segment.
* **Retrieve Audience** `getAudience`: Retrieve a single audience by its ID.
* **Retrieve Automation** `getAutomation`: Retrieve a single automation by its ID.
* **Retrieve Automation Run** `getAutomationRun`: Retrieve a single automation run by its ID.
* **Retrieve Broadcast** `getBroadcast`: Retrieve a single broadcast by its ID.
* **Retrieve Contact** `getContact`: Retrieve a single contact by its ID or email address.
* **Retrieve Contact Property** `getContactProperty`: Retrieve a single contact property by its ID.
* **Retrieve Domain** `getDomain`: Retrieve a single domain by its ID.
* **Retrieve Email** `getEmail`: Retrieve a single sent email by its ID.
* **Retrieve Event** `getEvent`: Retrieve a single custom event by its identifier.
* **Retrieve Log** `getLog`: Retrieve a single API request log by its ID.
* **Retrieve Segment** `getSegment`: Retrieve a single segment by its ID.
* **Retrieve Template** `getTemplate`: Retrieve a single template by its ID.
* **Retrieve Topic** `getTopic`: Retrieve a single topic by its ID.
* **Retrieve Webhook** `getWebhook`: Retrieve a single webhook by its ID.
* **Send Batch Emails** `sendBatchEmails`: Send up to 100 emails in a single request. Pass a JSON-encoded array of email objects as the emails input.
* **Send Broadcast** `sendBroadcast`: Send or schedule a broadcast.
* **Send Email** `sendEmail`: Send a transactional email through Resend. Requires from, to and subject; provide html or text (or a published template).
* **Send Event** `sendEvent`: Send (emit) a custom event for a contact or email address.
* **Stop Automation** `stopAutomation`: Stop a running automation, setting its status to disabled.
* **Update Automation** `updateAutomation`: Update an automation. At least one of name, status, or steps+connections must be provided.
* **Update Broadcast** `updateBroadcast`: Update an existing broadcast (draft).
* **Update Contact** `updateContact`: Update a single contact by ID or email. Provide the fields you wish to change.
* **Update Contact Property** `updateContactProperty`: Update an existing contact property's fallback value.
* **Update Contact Topics** `updateContactTopics`: Update the topic subscriptions for a contact. Pass topics as a JSON array of {id, subscription} objects.
* **Update Domain** `updateDomain`: Update settings of an existing domain such as tracking and TLS.
* **Update Email** `updateEmail`: Update a scheduled email, e.g. reschedule its send time.
* **Update Event** `updateEvent`: Update a custom event's payload schema.
* **Update Template** `updateTemplate`: Update an existing template.
* **Update Topic** `updateTopic`: Update an existing topic.
* **Update Webhook** `updateWebhook`: Update an existing webhook's endpoint, events or status.
* **Verify Domain** `verifyDomain`: Trigger verification of an existing domain's DNS records.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Contact Created | `contact.created` | A new contact was created. |
| Contact Deleted | `contact.deleted` | A contact was deleted. |
| Contact Updated | `contact.updated` | A contact was updated. |
| Domain Created | `domain.created` | A new domain was created. |
| Domain Deleted | `domain.deleted` | A domain was deleted. |
| Domain Updated | `domain.updated` | A domain was updated. |
| Email Bounced | `email.bounced` | The recipient's mail server permanently rejected the email. |
| Email Clicked | `email.clicked` | The recipient clicked a link in the email (requires click tracking enabled). |
| Email Complained | `email.complained` | The recipient marked the email as spam. |
| Email Delivered | `email.delivered` | Resend successfully delivered the email to the recipient's mail server. |

<details>

<summary>See 7 more events</summary>

* **Email Delivery Delayed** `email.delivery_delayed`: The email couldn't be delivered to the recipient's mail server because of a temporary issue.
* **Email Failed** `email.failed`: The email could not be sent due to a failure.
* **Email Opened** `email.opened`: The recipient opened the email (requires open tracking enabled).
* **Email Received** `email.received`: An inbound email was received for a configured receiving domain.
* **Email Scheduled** `email.scheduled`: The email has been scheduled to be sent at a later time.
* **Email Sent** `email.sent`: The API request was successful and Resend will attempt to deliver the message to the recipient's mail server.
* **Email Suppressed** `email.suppressed`: The email was suppressed because the recipient is on the suppression list.

</details>
