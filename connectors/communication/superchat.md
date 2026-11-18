---
description: "Superchat is a unified business messaging platform that brings WhatsApp, SMS, email, Instagram, Facebook Messenger, Telegram, Google Business Messages and…"
hidden: true
---

# Superchat

<img src="../../.gitbook/assets/connectors/lg/superchat.png" alt="Superchat logo">

Superchat is a unified business messaging platform that brings WhatsApp, SMS, email, Instagram, Facebook Messenger, Telegram, Google Business Messages and live chat into one shared inbox. This connector covers the complete Superchat Public API v1.0: contacts and contact handles, contact lists, custom attributes, conversations, conversation notes and exports, messages and message analytics, channels, inboxes, labels, templates and template folders, files, users, and webhook subscriptions.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [superchat.com](https://superchat.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `superchat` |

## Use it

Add Superchat from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.superchat.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Contact To Contact List | `addContactToContactList` | Adds an existing contact to an existing contact list. |
| Create Contact | `createContact` | Creates a contact in the workspace. At least one messaging handle is required; name, gender and custom attribute values are optional. Custom attributes must already exist - create them with Create Custom Attribute first. |
| Create Conversation Export | `createConversationExport` | Starts an export of a conversation's message history for a given time range. The export is processed asynchronously - poll Get Conversation Export until its status is done, then use the returned link. |
| Create Conversation Note | `createConversationNote` | Adds an internal note to a conversation. Notes are visible to your team only and are never delivered to the contact. |
| Create Custom Attribute | `createCustomAttribute` | Creates a custom contact attribute. Supply option_values only for single_select and multi_select attributes; the other types ignore it. |
| Create Template | `createTemplate` | Creates a message template. A generic_template needs a body and its variables array; a whats_app_template additionally needs a category and language and is submitted to Meta for approval before it can be sent. |
| Create Template Folder | `createTemplateFolder` | Creates a folder for organising message templates. Send parent_id as null to create the folder at the root. |
| Create Webhook Subscription | `createWebhookSubscription` | Registers a webhook subscription so Superchat posts the chosen events to your HTTPS endpoint. The target URL must be a public HTTPS address and may not be a superchat.com, superchat.de, superchat.tech or superchat.cloud host. |
| Delete Contact | `deleteContact` | Permanently deletes a contact from the workspace. This cannot be undone. |
| Delete Conversation | `deleteConversation` | Permanently deletes a conversation and its message history. This cannot be undone. |
| Delete Conversation Note | `deleteConversationNote` | Permanently deletes an internal note from a conversation. |
| Delete Custom Attribute | `deleteCustomAttribute` | Permanently deletes a custom contact attribute and the values stored for it on every contact. |
| Delete File | `deleteFile` | Permanently deletes a file from the workspace. Messages and notes that reference it will lose the attachment. |
| Delete Template | `deleteTemplate` | Permanently deletes a message template. Deleting a WhatsApp template also removes it from the connected WhatsApp Business Account. |
| Delete Template Folder | `deleteTemplateFolder` | Permanently deletes a template folder. |
| Delete Webhook Subscription | `deleteWebhookSubscription` | Deletes a webhook subscription so Superchat stops posting events to its target URL. |
| Get Channel | `getChannel` | Retrieves a single messaging channel configuration by its ID. The fields returned beyond id, name, type and inbox depend on the channel type. |
| Get Contact | `getContact` | Retrieves a single contact by its ID, including messaging handles and custom attribute values. |
| Get Contact List | `getContactList` | Retrieves a single contact list by its ID. |
| Get Conversation | `getConversation` | Retrieves a single conversation by its ID, with its status, channel, inbox, labels, assigned users, linked contacts and reply time window. |
| Get Conversation Export | `getConversationExport` | Returns the current status of a conversation export and, once it is done, the download link for the export file. |
| Get Conversation Note | `getConversationNote` | Retrieves a single internal note on a conversation by its note ID. |
| Get Current User | `getCurrentUser` | Returns the Superchat user that the connected API key belongs to, together with the workspace it operates in. Useful for verifying a connection. |
| Get File | `getFile` | Retrieves a single file's metadata and a fresh time-limited download link. |
| Get Inbox | `getInbox` | Retrieves a single shared inbox by its ID, including the users assigned to it. |
| Get Label | `getLabel` | Retrieves a single conversation label by its ID. |
| Get Message Analytics | `getMessageAnalytics` | Returns delivery and engagement analytics for specific messages, such as when each message was delivered, read and clicked. |
| Get Template | `getTemplate` | Retrieves a single message template by its ID, including its content, approval status, folder and available channels. |
| Get Template Analytics | `getTemplateAnalytics` | Returns aggregated send, delivery, read and click analytics for specific message templates over a date range. |
| Get Template Folder | `getTemplateFolder` | Retrieves a single template folder by its ID. |
| Get User | `getUser` | Retrieves a single user of the connected Superchat workspace by their user ID. |
| Get Webhook Subscription | `getWebhookSubscription` | Retrieves a single webhook subscription by its ID, including its delivery state and subscribed events. |
| List Channels | `listChannels` | Returns a cursor-paginated list of the messaging channels connected to the workspace, such as WhatsApp, SMS, email, Instagram, Facebook Messenger, Telegram, live chat and Google Business Messages. Use a channel ID from here as the from.channel_id when sending a message. |
| List Contact Lists | `listContactLists` | Returns a cursor-paginated list of all contact lists in the workspace. Contact lists are created in the Superchat app; the API is read-only for the lists themselves. |
| List Contact Lists For Contact | `listContactListsForContact` | Returns the contact lists a specific contact belongs to, cursor-paginated. |
| List Contacts | `listContacts` | Returns a cursor-paginated list of all contacts in the workspace, each with their messaging handles and custom attribute values. |
| List Conversation Messages | `listConversationMessages` | Returns the messages in a conversation, cursor-paginated and optionally restricted to a creation time range. Inbound and outbound messages are returned together and distinguished by the direction field. |
| List Conversation Notes | `listConversationNotes` | Returns the internal notes attached to a conversation, cursor-paginated. Notes are visible to your team only and are never sent to the contact. |
| List Conversations | `listConversations` | Returns a cursor-paginated list of all conversations in the workspace, with their status, channel, inbox, labels, assigned users and linked contacts. |
| List Conversations For Contact | `listConversationsForContact` | Returns the conversations linked to a specific contact, cursor-paginated. |
| List Custom Attributes | `listCustomAttributes` | Returns a cursor-paginated list of the custom contact attributes defined in the workspace, including the allowed options of select attributes. |
| List Files | `listFiles` | Returns a cursor-paginated list of the files stored in the workspace, each with a time-limited download link. |
| List Inboxes | `listInboxes` | Returns a cursor-paginated list of all shared inboxes in the workspace, each with the users assigned to it. |
| List Labels | `listLabels` | Returns a cursor-paginated list of all conversation labels defined in the workspace. |
| List Template Folders | `listTemplateFolders` | Returns a cursor-paginated list of template folders, optionally restricted to the children of one parent folder. |
| List Templates | `listTemplates` | Returns a cursor-paginated list of message templates, optionally filtered by template type, folder or channel. |
| List Users | `listUsers` | Returns a cursor-paginated list of all users in the connected Superchat workspace. |
| List Webhook Subscriptions | `listWebhookSubscriptions` | Returns a cursor-paginated list of the webhook subscriptions registered on the workspace, with their target URL, delivery state and subscribed events. |
| Remove Contact From Contact List | `removeContactFromContactList` | Removes a contact from a contact list. The contact itself is not deleted. |
| Search Contacts | `searchContacts` | Finds contacts by an exact match on an email address, a phone number, an Instagram username or a custom attribute value. Exactly one search expression may be supplied per request. |
| Send Message | `sendMessage` | Sends a message to one recipient through a connected Superchat channel - WhatsApp, SMS, email, Instagram, Facebook Messenger, Telegram, live chat or Google Business Messages. The content object's type field selects the payload shape. Exactly one recipient is allowed per request. |
| Update Contact | `updateContact` | Updates a contact. Verified live: this is a partial update - omitted fields keep their current values, and the handles array is ADDITIVE, so handles you leave out are not removed. Send only the fields you want to change. |
| Update Conversation | `updateConversation` | Updates a conversation: change its status, move it to another inbox, snooze it until a given time, or replace its assigned users and labels. Omit a field to leave it unchanged; assigned_users and labels are full replacements. |
| Update Conversation Note | `updateConversationNote` | Replaces the content and attachments of an internal conversation note. |
| Update Custom Attribute | `updateCustomAttribute` | Renames a custom contact attribute and, for select attributes, replaces its list of options. Include the id of each existing option you want to keep; omit the id to add a new option. |
| Update Template | `updateTemplate` | Renames a message template, moves it to another folder, or replaces its file attachments. Omit a field to leave it unchanged. Verified live: sending folder_id as null does NOT move the template to the root - it is treated as "no change". Pass a real folder id to move it. |
| Update Template Folder | `updateTemplateFolder` | Renames a template folder. |
| Update Webhook Subscription | `updateWebhookSubscription` | Updates a webhook subscription's target URL and the set of events it receives. The events array is a full replacement of the current subscription list. |
| Upload File | `uploadFile` | Uploads a file to the workspace so it can be attached to a message or a note. Superchat accepts this endpoint as multipart/form-data only. Allowed types include application/pdf, application/rtf, application/msword, image/jpeg, image/png, image/gif, audio/mpeg, audio/ogg, audio/webm, audio/aac, video/mp4 and video/quicktime. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| AI Call Completed | `ai_call_completed` | Fires when a Superchat AI voice agent finishes a call, with the recording, transcript and summary. Requires the AI calling feature to be enabled on the workspace. Payload schema modelled from Superchat's documented sample at https://developers.superchat.com/reference/webhook-payload-model, not from a captured delivery. |
| Contact Created | `contact_created` | Fires when a contact is added to the workspace, whether manually, by an inbound message or through the API. Payload schema modelled from Superchat's documented sample at https://developers.superchat.com/reference/webhook-payload-model, not from a captured delivery. |
| Contact Deleted | `contact_deleted` | Fires when a contact is removed from the workspace. The payload carries the contact as it was immediately before deletion. Payload schema modelled from Superchat's documented sample at https://developers.superchat.com/reference/webhook-payload-model, not from a captured delivery. |
| Contact Updated | `contact_updated` | Fires when any field, handle or custom attribute of a contact changes. Payload schema modelled from Superchat's documented sample at https://developers.superchat.com/reference/webhook-payload-model, not from a captured delivery. |
| Conversation Deleted | `conversation_deleted` | Fires when a conversation is deleted. The payload carries the conversation as it was immediately before deletion. Payload schema modelled from Superchat's documented sample at https://developers.superchat.com/reference/webhook-payload-model, not from a captured delivery. |
| Conversation Marked Done | `conversation_done` | Fires when a conversation is marked done. Payload schema modelled from Superchat's documented sample at https://developers.superchat.com/reference/webhook-payload-model, not from a captured delivery. |
| Conversation Opened | `conversation_opened` | Fires when a conversation moves into the open state, for example when a new inbound message reopens it. Payload schema modelled from Superchat's documented sample at https://developers.superchat.com/reference/webhook-payload-model, not from a captured delivery. |
| Conversation Snoozed | `conversation_snoozed` | Fires when a conversation is snoozed until a later time. The conversation's snoozed_until field carries that time. Payload schema modelled from Superchat's documented sample at https://developers.superchat.com/reference/webhook-payload-model, not from a captured delivery. |
| Message Failed | `message_failed` | Fires when an outbound message could not be delivered by the underlying channel. The message status is sending_failed. Payload schema modelled from Superchat's documented samples at https://developers.superchat.com/reference/webhook-payload-model, not from a captured delivery. |
| Message Received | `message_inbound` | Fires when a contact sends a message to one of your connected channels. The message.content.type field selects the content shape: text, media, email, generic_template, whats_app_quick_reply, whats_app_template, whats_app_list, instagram_story_reply or instagram_comment. Payload schema modelled from Superchat's documented samples at https://developers.superchat.com/reference/webhook-payload-model, not from a captured delivery. |
| Message Sent | `message_outbound` | Fires when a message is sent from one of your connected channels, whether from the Superchat app, an automation or the API. Payload schema modelled from Superchat's documented samples at https://developers.superchat.com/reference/webhook-payload-model, not from a captured delivery. |
| Note Created | `note_created` | Fires when a team member adds an internal note to a conversation. Payload schema modelled from Superchat's documented sample at https://developers.superchat.com/reference/webhook-payload-model, not from a captured delivery. |
