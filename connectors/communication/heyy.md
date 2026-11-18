---
description: "Heyy customer-messaging platform (api.heyy.io v3)."
hidden: true
---

# Heyy

<img src="../../.gitbook/assets/connectors/lg/heyy.png" alt="Heyy logo">

Heyy customer-messaging platform (api.heyy.io v3). Manage contacts, labels, custom attributes, chats, channels, message templates, campaigns, journeys, automations, teams, files and API webhooks, and send WhatsApp/omnichannel messages.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [heyy.io](https://heyy.io) |
| **Authentication** | API key |
| **Slug** | `heyy` |

## Use it

Add Heyy from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.heyy.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Campaign Recipients | `addCampaignRecipients` | Add contacts to a fixed-audience campaign's recipient list. Nothing is sent until the campaign is started. |
| Add Labels To Contact | `addLabelsToContact` | Attach one or more existing labels to a contact. |
| Assign Chat To Team | `assignChatToTeam` | Assign a conversation to an agent team rather than an individual. Set triggerAutomations to true to let assignment automations fire. |
| Assign Chat To User | `assignChatToUser` | Assign a conversation to a specific agent. Set triggerAutomations to true to let assignment automations fire. |
| Bulk Upsert Contacts | `bulkUpsertContacts` | Create or update many contacts in one request. Each entry matches on phone number or email and carries optional attributes and labels. |
| Change Chat Status | `changeChatStatus` | Move a conversation to open, closed or snoozed. Set triggerAutomations to true to let status-change automations fire - which may send messages to the contact. |
| Create API Webhook | `createApiWebhook` | Register an outbound webhook URL that Heyy calls for the chosen events (whatsapp_message_received, whatsapp_message_status, message.received, message.sent, message.updated), scoped to specific channel ids. |
| Create Attribute | `createAttribute` | Define a new custom contact attribute of type text, number, single_select, multi_select, date or datetime, with visibility flags and (for select types) its options. |
| Create Campaign | `createCampaign` | Create an outbound campaign that runs an existing automation against a recipient list, optionally scheduled or recurring. Creating a campaign does not send anything until Start Campaign is called. |
| Create Contact | `createContact` | Create a contact from a first/last name, phone number, email, custom attribute values and labels. Fails if a contact with the same phone number or email already exists - use Upsert Contact to create-or-update. |

<details>

<summary>See 62 more actions</summary>

* **Create Label** `createLabel`: Create a label with a name and a hex colour, for tagging contacts and chats.
* **Create Message Template** `createMessageTemplate`: Submit a new WhatsApp message template on a channel, with its body/header/footer/buttons and vendor details (language and category). The template then goes to WhatsApp for approval.
* **Create Team** `createTeam`: Create an agent team with a name, an emoji/icon and an optional list of member user ids. Requires a Heyy plan that includes Teams.
* **Delete API Webhook** `deleteApiWebhook`: Remove an outbound webhook subscription by id so Heyy stops delivering events to it. Returns deletedIds and notFoundIds.
* **Delete Attribute** `deleteAttribute`: Delete a custom contact attribute definition by id, removing its values from every contact. Returns deletedIds and notFoundIds.
* **Delete Campaign** `deleteCampaign`: Delete a campaign by id. Returns deletedIds and notFoundIds.
* **Delete Chat** `deleteChat`: Permanently delete a conversation and its message history by id. Returns deletedIds and notFoundIds.
* **Delete Contact** `deleteContact`: Permanently delete a contact by id. Returns deletedIds and notFoundIds; a missing id is reported in notFoundIds rather than as an error.
* **Delete Label** `deleteLabel`: Delete a label by id. Returns deletedIds and notFoundIds.
* **Delete Message Template** `deleteMessageTemplate`: Delete a message template by id. Returns deletedIds and notFoundIds.
* **Delete Team** `deleteTeam`: Delete an agent team by id. Returns deletedIds and notFoundIds. Requires a Heyy plan that includes Teams.
* **Get Attribute** `getAttribute`: Retrieve one custom contact attribute definition by id, including its data type, visibility flags and select options.
* **Get Automation** `getAutomation`: Retrieve one automation by id, including its name, trigger, paused state and step definition.
* **Get Campaign** `getCampaign`: Retrieve one campaign by id, including its automation, schedule, recurrence rules, audience and run state.
* **Get Channel** `getChannel`: Retrieve one messaging channel by id, including its type, display name and vendor configuration.
* **Get Chat** `getChat`: Retrieve one inbox conversation by id, including its status, channel, contact, assignee and unread state.
* **Get Contact** `getContact`: Retrieve one contact by id, including handles, labels, subscription state and custom attribute values. Note: contact records are personal data.
* **Get File** `getFile`: Retrieve metadata for an uploaded file by its file id (type, name, size and storage details).
* **Get File Public URL** `getFilePublicUrl`: Get a publicly reachable download URL for an uploaded file. WARNING: the returned URL serves the file content without authentication - treat it as a shareable secret.
* **Get Journey** `getJourney`: Retrieve one customer journey by id, including its steps and enrolment rules. Requires a Heyy plan that includes Journeys.
* **Get Label** `getLabel`: Retrieve one label by id, returning its name and hex colour.
* **Get Message Template** `getMessageTemplate`: Retrieve one message template by id, including its body, header, footer, buttons and WhatsApp vendor details.
* **Get Team** `getTeam`: Retrieve one agent team by id, including its icon, name and member list. Requires a Heyy plan that includes Teams.
* **Get User** `getUser`: Retrieve a single Heyy workspace user (agent) by its user id.
* **Get Workspace** `getWorkspace`: Retrieve the Heyy workspace (business) this API key belongs to, including its id, name, timezone and weekly availability schedule.
* **List Users** `listUsers`: List every agent/user in the Heyy workspace with their email, phone number, name, profile picture and roles.
* **Mark Chat As Not Sensitive** `markChatAsNotSensitive`: Clear the sensitive flag on a conversation, returning it to normal agent visibility. Requires a Heyy plan that includes sensitive chats.
* **Mark Chat As Read** `markChatAsRead`: Clear the unread badge on a conversation.
* **Mark Chat As Sensitive** `markChatAsSensitive`: Flag a conversation as sensitive so its contents are restricted to authorised agents. Requires a Heyy plan that includes sensitive chats.
* **Mark Chat As Unread** `markChatAsUnread`: Flag a conversation as unread so it reappears in the agent's unread queue.
* **Pause Automation** `pauseAutomation`: Pause an automation so it stops enrolling contacts and stops sending.
* **Remove Campaign Recipients** `removeCampaignRecipients`: Remove contacts from a campaign's recipient list so they will not be messaged when it runs.
* **Remove Labels From Contact** `removeLabelsFromContact`: Detach one or more labels from a contact. The labels themselves are not deleted.
* **Search API Webhooks** `searchApiWebhooks`: Search the outbound API webhook subscriptions registered on the workspace, with pagination and a sort expression.
* **Search Attributes** `searchAttributes`: Search the workspace's custom contact attribute definitions with pagination, free-text search, a filter query and a sort expression.
* **Search Automations** `searchAutomations`: Search the workspace's automations (message flows) with pagination, a free-text term and a sort expression.
* **Search Campaigns** `searchCampaigns`: Search outbound campaigns with pagination, a free-text term, a filter query and a sort expression.
* **Search Channels** `searchChannels`: Search the messaging channels connected to the workspace (WhatsApp numbers, email, web chat) with pagination and a sort expression.
* **Search Chats** `searchChats`: Search inbox conversations with pagination, a free-text term, a filter query and a sort expression. Returns chats with their status, channel, contact and assignment.
* **Search Contacts** `searchContacts`: Search contacts with pagination, a free-text term, a filter query and a sort expression. Returns contact records including phone number, email, subscription state, handles, labels and custom attribute values.
* **Search Journeys** `searchJourneys`: Search multi-step customer journeys with pagination and a sort expression. Requires a Heyy plan that includes Journeys.
* **Search Labels** `searchLabels`: Search the workspace's contact/chat labels with pagination, a free-text term, a filter query and a sort expression.
* **Search Message Templates** `searchMessageTemplates`: Search the workspace's message templates (including WhatsApp templates and their approval status) with pagination and a sort expression.
* **Search Teams** `searchTeams`: Search agent teams in the workspace with pagination, free-text search, a filter query and a sort expression. Requires a Heyy plan that includes Teams.
* **Send Message** `sendMessage`: Send a free-form message into a conversation, addressed either by chatId or by channelId plus contactId/phoneNumber/email/handleId, with optional attachments, buttons, header, footer, reply-to and schedule. WARNING: this DELIVERS A REAL, BILLABLE MESSAGE to a real person.
* **Send Template Message** `sendTemplateMessage`: Send an approved WhatsApp template message, substituting its variables, to a chat or to a contact on a channel. Use this to open a conversation outside the 24-hour customer-care window. WARNING: this DELIVERS A REAL, BILLABLE MESSAGE to a real person.
* **Start Campaign** `startCampaign`: Launch a campaign. WARNING: this DISPATCHES REAL, BILLABLE MESSAGES to every recipient on the campaign's audience and cannot be undone once delivery begins.
* **Subscribe Contact** `subscribeContact`: Opt a contact back in to marketing and campaign messaging, setting isSubscribed to true.
* **Subscribe Contacts To Journey** `subscribeContactsToJourney`: Enrol contacts into a journey. WARNING: enrolment starts the journey's steps, which DISPATCH REAL, BILLABLE MESSAGES to those contacts. Requires a Heyy plan that includes Journeys.
* **Trigger Automation For Contact** `triggerAutomationForContact`: Run an automation for one contact, optionally at a scheduled time and with template variables. WARNING: this DISPATCHES REAL MESSAGES to the contact's WhatsApp/email and is billable. Only call it with a contact who has consented.
* **Unpause Automation** `unpauseAutomation`: Resume a paused automation. WARNING: once resumed the automation can DISPATCH REAL, BILLABLE MESSAGES to enrolled contacts without further calls.
* **Unsubscribe Contact** `unsubscribeContact`: Opt a contact out of marketing and campaign messaging, setting isSubscribed to false.
* **Unsubscribe Contacts From Journey** `unsubscribeContactsFromJourney`: Remove contacts from a journey so its remaining steps stop firing for them. Requires a Heyy plan that includes Journeys.
* **Update API Webhook** `updateApiWebhook`: Change an outbound webhook's target URL, its subscribed events, or activate/deactivate it via status.
* **Update Attribute** `updateAttribute`: Update a custom contact attribute's display name, description, visibility flags or select options. The attribute's data type cannot be changed.
* **Update Campaign** `updateCampaign`: Update a campaign's name, automation, variables, schedule, recurrence or audience definition before it starts.
* **Update Contact** `updateContact`: Update an existing contact's first name, last name or custom attribute values by contact id.
* **Update Label** `updateLabel`: Rename a label or change its hex colour.
* **Update Message Template** `updateMessageTemplate`: Update a message template's name, content or WhatsApp vendor details. Content changes re-submit the template for approval.
* **Update Team** `updateTeam`: Update an agent team's name, icon or member list. The users array replaces the existing membership. Requires a Heyy plan that includes Teams.
* **Upload File** `uploadFile`: Upload a text-based file (document, image, video or audio classification) to Heyy's asset store so it can be attached to messages or templates. Returns the new file id and a time-limited download URL. Note: Heyy has no delete-file endpoint, so an uploaded file cannot be removed via the API.
* **Upsert Contact** `upsertContact`: Create a contact, or update the existing one that matches the supplied phone number or email. Returns the resulting contact record.

</details>
