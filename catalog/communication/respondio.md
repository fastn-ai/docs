---
description: "respond.io is a customer messaging platform. Create and update contacts, assign conversations, add comments, and manage tags and custom fields."
hidden: true
---

# respond.io

<img src="../../.gitbook/assets/connectors/lg/respondio.png" alt="respond.io logo">

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [respond.io](https://respond.io) |
| **Authentication** | Access token |
| **Slug** | `respondio` |

## Setup

Your customers enter their access token for respond.io when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect respond.io from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **respond.io**.
2. Select **Connect** on the respond.io card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use respond.io's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Contact Tags</td><td><code>addContactTags</code></td><td>Adds one or more tags to a contact. Tags that do not yet exist are also created as workspace tags. The tags input is a JSON array text, for example ["vip","lead"].</td></tr><tr><td>Assign Conversation</td><td><code>assignConversation</code></td><td>Assigns a contact's conversation to a workspace user by user ID or email, or unassigns it when assignee is null.</td></tr><tr><td>Create Comment</td><td><code>createComment</code></td><td>Adds an internal comment to a contact's conversation.</td></tr><tr><td>Create Contact</td><td><code>createContact</code></td><td>Creates a contact identified by email or phone, with name, language, profile picture, country code and custom field values.</td></tr><tr><td>Create Custom Field</td><td><code>createCustomField</code></td><td>Creates a contact custom field in the workspace. Note: the API has no endpoint to delete custom fields.</td></tr><tr><td>Create Or Update Contact</td><td><code>createOrUpdateContact</code></td><td>Creates a contact identified by email or phone, or updates it when it already exists.</td></tr><tr><td>Create Space Tag</td><td><code>createSpaceTag</code></td><td>Creates a contact tag in the workspace, with optional description, color code and emoji.</td></tr><tr><td>Delete Contact</td><td><code>deleteContact</code></td><td>Deletes a contact by ID, email or phone identifier.</td></tr><tr><td>Delete Space Tag</td><td><code>deleteSpaceTag</code></td><td>Deletes a workspace tag by name.</td></tr><tr><td>Get Contact</td><td><code>getContact</code></td><td>Retrieves a contact by ID, email or phone identifier, including tags, custom fields, assignee, lifecycle and conversation status.</td></tr></tbody></table>

<details>

<summary>View 18 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Custom Field</td><td><code>getCustomField</code></td><td>Retrieves a single workspace custom field by ID.</td></tr><tr><td>Get Message</td><td><code>getMessage</code></td><td>Retrieves a single message of a contact by message ID, including delivery status and sender.</td></tr><tr><td>Get Space User</td><td><code>getSpaceUser</code></td><td>Retrieves a single workspace user by ID, including role, team and restrictions.</td></tr><tr><td>List Closing Notes</td><td><code>listClosingNotes</code></td><td>Retrieves the conversation closing note categories configured in the workspace.</td></tr><tr><td>List Contact Channels</td><td><code>listContactChannels</code></td><td>Retrieves the messaging channels a contact is connected through, with last message times.</td></tr><tr><td>List Contacts</td><td><code>listContacts</code></td><td>Lists contacts matching a search term and filter conditions on contact fields, tags or lifecycle, with cursor paging.</td></tr><tr><td>List Custom Fields</td><td><code>listCustomFields</code></td><td>Retrieves the contact custom fields defined in the workspace, with cursor paging.</td></tr><tr><td>List Message Templates</td><td><code>listMessageTemplates</code></td><td>Retrieves the WhatsApp message templates of a workspace channel, with components, language and approval status.</td></tr><tr><td>List Messages</td><td><code>listMessages</code></td><td>Retrieves the messages exchanged with a contact, newest first, with cursor paging.</td></tr><tr><td>List Space Channels</td><td><code>listSpaceChannels</code></td><td>Retrieves the messaging channels connected to the workspace, such as WhatsApp, Facebook Messenger, Telegram or email.</td></tr><tr><td>List Space Users</td><td><code>listSpaceUsers</code></td><td>Retrieves the users (agents, managers and owners) of the respond.io workspace, with cursor paging.</td></tr><tr><td>Merge Contacts</td><td><code>mergeContacts</code></td><td>Merges two contacts into one, keeping the first contact and optionally overriding its fields with the values sent.</td></tr><tr><td>Open Or Close Conversation</td><td><code>openOrCloseConversation</code></td><td>Opens or closes a contact's conversation. When closing, a closing note category and summary can be recorded.</td></tr><tr><td>Remove Contact Tags</td><td><code>removeContactTags</code></td><td>Removes one or more tags from a contact; the workspace tags themselves are not deleted. The tags input is a JSON array text, for example ["vip"].</td></tr><tr><td>Send Message</td><td><code>sendMessage</code></td><td>Sends a message to a contact through a channel (or the contact's last interacted channel): text, attachment, custom payload, quick reply, email or WhatsApp template.</td></tr><tr><td>Update Contact</td><td><code>updateContact</code></td><td>Updates an existing contact's name, phone, email, language, profile picture, country code or custom field values. Only fields sent are changed.</td></tr><tr><td>Update Contact Lifecycle</td><td><code>updateContactLifecycle</code></td><td>Sets a contact's lifecycle stage by name, or clears it when name is null.</td></tr><tr><td>Update Space Tag</td><td><code>updateSpaceTag</code></td><td>Updates a workspace tag identified by its current name: rename it or change its description, color code or emoji.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Call Ended</td><td><code>call.ended</code></td><td>In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the Fastn trigger URL as Endpoint URL and select the 'Call Ended' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds. This payload has no event_type field; register a dedicated trigger URL for Call Ended.</td></tr><tr><td>Contact Assignee Updated</td><td><code>contact.assignee.updated</code></td><td>In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the Fastn trigger URL as Endpoint URL and select the 'Contact Assignee Updated' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds.</td></tr><tr><td>Contact Tag Updated</td><td><code>contact.tag.updated</code></td><td>In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the Fastn trigger URL as Endpoint URL and select the 'Contact Tag Updated' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds.</td></tr><tr><td>Contact Updated</td><td><code>contact.updated</code></td><td>In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the Fastn trigger URL as Endpoint URL and select the 'Contact Updated' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds.</td></tr><tr><td>Conversation Closed</td><td><code>conversation.closed</code></td><td>In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the Fastn trigger URL as Endpoint URL and select the 'Conversation Closed' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds.</td></tr><tr><td>Conversation Opened</td><td><code>conversation.opened</code></td><td>In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the Fastn trigger URL as Endpoint URL and select the 'Conversation Opened' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds.</td></tr><tr><td>Lifecycle Updated</td><td><code>contact.lifecycle.updated</code></td><td>In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the Fastn trigger URL as Endpoint URL and select the 'Lifecycle Updated' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds.</td></tr><tr><td>New Comment</td><td><code>comment.created</code></td><td>In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the Fastn trigger URL as Endpoint URL and select the 'New Comment' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds.</td></tr><tr><td>New Contact</td><td><code>contact.created</code></td><td>In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the Fastn trigger URL as Endpoint URL and select the 'New Contact' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds.</td></tr><tr><td>New Incoming Message</td><td><code>message.received</code></td><td>In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the Fastn trigger URL as Endpoint URL and select the 'New Incoming Message' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds.</td></tr></tbody></table>

<details>

<summary>View 1 more event</summary>

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>New Outgoing Message</td><td><code>message.sent</code></td><td>In respond.io open Workspace Settings &gt; Integrations &gt; Webhooks, click Connect, then Add Webhook: paste the Fastn trigger URL as Endpoint URL and select the 'New Outgoing Message' event. Requires the Advanced plan. The endpoint must answer 200 within 5 seconds.</td></tr></tbody></table>

</details>
