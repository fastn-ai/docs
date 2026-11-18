---
description: "respond.io is a conversational CRM and customer messaging platform."
hidden: true
---

# respond.io

respond.io is a conversational CRM and customer messaging platform. This connector wraps the respond.io Developer API v2: contacts (create, update, create-or-update, merge, list, delete), contact tags, contact channels and lifecycle stages, conversations (assign and open/close), messaging (send, get and list messages), comments, and workspace resources (users, custom fields, closing notes, channels, WhatsApp message templates and space tags). It also defines the respond.io webhook events (contact, conversation, message, comment, lifecycle, tag and call events) registered in Workspace Settings. Authenticates with a workspace API access token sent as a Bearer token.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [respond.io](https://respond.io) |
| **Authentication** | Bearer token |
| **Actions** | 28 |
| **Events** | 11 |
| **Slug** | `respondio` |

## Use it

Add respond.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.respondio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Contact Tags | `addContactTags` | Adds one or more tags to a contact. Tags that do not yet exist are also created as workspace tags. The tags input is a JSON array text, for example ["vip","lead"]. |
| Assign Conversation | `assignConversation` | Assigns a contact's conversation to a workspace user by user ID or email, or unassigns it when assignee is null. |
| Create Comment | `createComment` | Adds an internal comment to a contact's conversation. |
| Create Contact | `createContact` | Creates a contact identified by email or phone, with name, language, profile picture, country code and custom field values. |
| Create Custom Field | `createCustomField` | Creates a contact custom field in the workspace. Note: the API has no endpoint to delete custom fields. |
| Create Or Update Contact | `createOrUpdateContact` | Creates a contact identified by email or phone, or updates it when it already exists. |
| Create Space Tag | `createSpaceTag` | Creates a contact tag in the workspace, with optional description, color code and emoji. |
| Delete Contact | `deleteContact` | Deletes a contact by ID, email or phone identifier. |
| Delete Space Tag | `deleteSpaceTag` | Deletes a workspace tag by name. |
| Get Contact | `getContact` | Retrieves a contact by ID, email or phone identifier, including tags, custom fields, assignee, lifecycle and conversation status. |
| Get Custom Field | `getCustomField` | Retrieves a single workspace custom field by ID. |
| Get Message | `getMessage` | Retrieves a single message of a contact by message ID, including delivery status and sender. |
| Get Space User | `getSpaceUser` | Retrieves a single workspace user by ID, including role, team and restrictions. |
| List Closing Notes | `listClosingNotes` | Retrieves the conversation closing note categories configured in the workspace. |
| List Contact Channels | `listContactChannels` | Retrieves the messaging channels a contact is connected through, with last message times. |
| List Contacts | `listContacts` | Lists contacts matching a search term and filter conditions on contact fields, tags or lifecycle, with cursor paging. |
| List Custom Fields | `listCustomFields` | Retrieves the contact custom fields defined in the workspace, with cursor paging. |
| List Message Templates | `listMessageTemplates` | Retrieves the WhatsApp message templates of a workspace channel, with components, language and approval status. |
| List Messages | `listMessages` | Retrieves the messages exchanged with a contact, newest first, with cursor paging. |
| List Space Channels | `listSpaceChannels` | Retrieves the messaging channels connected to the workspace, such as WhatsApp, Facebook Messenger, Telegram or email. |
| List Space Users | `listSpaceUsers` | Retrieves the users (agents, managers and owners) of the respond.io workspace, with cursor paging. |
| Merge Contacts | `mergeContacts` | Merges two contacts into one, keeping the first contact and optionally overriding its fields with the values sent. |
| Open Or Close Conversation | `openOrCloseConversation` | Opens or closes a contact's conversation. When closing, a closing note category and summary can be recorded. |
| Remove Contact Tags | `removeContactTags` | Removes one or more tags from a contact; the workspace tags themselves are not deleted. The tags input is a JSON array text, for example ["vip"]. |
| Send Message | `sendMessage` | Sends a message to a contact through a channel (or the contact's last interacted channel): text, attachment, custom payload, quick reply, email or WhatsApp template. |
| Update Contact | `updateContact` | Updates an existing contact's name, phone, email, language, profile picture, country code or custom field values. Only fields sent are changed. |
| Update Contact Lifecycle | `updateContactLifecycle` | Sets a contact's lifecycle stage by name, or clears it when name is null. |
| Update Space Tag | `updateSpaceTag` | Updates a workspace tag identified by its current name: rename it or change its description, color code or emoji. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Call Ended | `call.ended` | In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the fastn trigger URL as Endpoint URL and select the 'Call Ended' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds. This payload has no event_type field; register a dedicated trigger URL for Call Ended. |
| Contact Assignee Updated | `contact.assignee.updated` | In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the fastn trigger URL as Endpoint URL and select the 'Contact Assignee Updated' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds. |
| Contact Tag Updated | `contact.tag.updated` | In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the fastn trigger URL as Endpoint URL and select the 'Contact Tag Updated' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds. |
| Contact Updated | `contact.updated` | In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the fastn trigger URL as Endpoint URL and select the 'Contact Updated' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds. |
| Conversation Closed | `conversation.closed` | In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the fastn trigger URL as Endpoint URL and select the 'Conversation Closed' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds. |
| Conversation Opened | `conversation.opened` | In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the fastn trigger URL as Endpoint URL and select the 'Conversation Opened' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds. |
| Lifecycle Updated | `contact.lifecycle.updated` | In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the fastn trigger URL as Endpoint URL and select the 'Lifecycle Updated' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds. |
| New Comment | `comment.created` | In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the fastn trigger URL as Endpoint URL and select the 'New Comment' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds. |
| New Contact | `contact.created` | In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the fastn trigger URL as Endpoint URL and select the 'New Contact' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds. |
| New Incoming Message | `message.received` | In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the fastn trigger URL as Endpoint URL and select the 'New Incoming Message' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds. |
| New Outgoing Message | `message.sent` | In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the fastn trigger URL as Endpoint URL and select the 'New Outgoing Message' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds. |
