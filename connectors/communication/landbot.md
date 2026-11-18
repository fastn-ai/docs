---
description: "Landbot is a no-code conversational app builder for websites, WhatsApp and Messenger."
---

# Landbot

Landbot is a no-code conversational app builder for websites, WhatsApp and Messenger. This connector covers the Landbot Platform API v1: listing and retrieving messaging channels, browsing bots and agents, reading and managing customers and their message history, archiving, blocking, assigning and unassigning conversations to agents or bots, sending text, image, location and WhatsApp template messages, managing WhatsApp opt-out, reading and writing custom customer fields, and registering message hooks that deliver conversation events to an external endpoint.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Authentication** | Credentials you enter |
| **Actions** | 31 |
| **Events** | 0 |
| **Slug** | `landbot` |

## Use it

Add Landbot from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.landbot.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Customer | `archiveCustomer` | Archives a Landbot customer's conversation, removing it from the active inbox. |
| Assign Customer To Agent | `assignCustomerToAgent` | Assigns a Landbot conversation to a specific human agent. |
| Assign Customer To Available Agent | `assignCustomer` | Assigns a Landbot conversation to whichever human agent is next available, according to the account's routing rules. |
| Assign Customer To Bot | `assignCustomerToBot` | Hands a Landbot conversation back to a bot, which resumes the automated flow from its start. |
| Block Customer | `blockCustomer` | Blocks a Landbot customer so they can no longer send messages to the account. |
| Create Customer Field | `createCustomerField` | Creates a custom field on a Landbot customer's profile and sets its initial value. Use Update Customer Field to change the value of a field that already exists. |
| Create Message Hook | `createMessageHook` | Registers a message hook on a Landbot channel so that every message moving through it is POSTed to your endpoint. Supply a token to have Landbot echo it back as an Authorization header on each delivery. |
| Delete Customer | `deleteCustomer` | Permanently deletes a Landbot customer and their entire conversation history. This cannot be undone. |
| Delete Customer Field | `deleteCustomerField` | Removes a custom field and its value from a Landbot customer's profile. |
| Delete Message Hook | `deleteMessageHook` | Removes a message hook from a Landbot channel, stopping further deliveries to its endpoint. |
| Get Bot | `getBot` | Retrieves a single Landbot bot by its numeric identifier. |
| Get Channel | `getChannel` | Retrieves a single Landbot messaging channel by its numeric identifier. |
| Get Customer | `getCustomer` | Retrieves a single Landbot customer by numeric identifier, including their custom fields, assigned agent and conversation state. |
| Get Customer Field | `getCustomerField` | Retrieves the value of a single custom field on a Landbot customer's profile. |
| Get Message Hook | `getMessageHook` | Retrieves a single message hook registered on a Landbot channel. |
| List Agents | `listAgents` | Retrieves the human agents on the Landbot account who can be assigned conversations, including their name, email address and role. |
| List Bots | `listBots` | Retrieves every bot built in the Landbot account, including its identifier and name. |
| List Channels | `listChannels` | Retrieves every messaging channel connected to the Landbot account, such as WhatsApp, web chat and Messenger channels. |
| List Customer Messages | `listCustomerMessages` | Retrieves the message history of a Landbot customer's conversation, newest first. |
| List Customers | `listCustomers` | Retrieves the customers (contacts) on the Landbot account, with optional filtering by channel, assigned agent, archive status, WhatsApp opt-in status, and a prefix search over name, email or phone. |
| List Message Hooks | `listMessageHooks` | Retrieves the message hooks registered on a Landbot channel. Each hook receives an HTTP POST for every message that moves through the channel. |
| List WhatsApp Templates | `listWhatsappTemplates` | Retrieves the WhatsApp message templates approved for the account, which are required to open a conversation outside the 24-hour customer service window. |
| Opt Out Customer | `optOutCustomer` | Marks a Landbot customer as opted out of WhatsApp messaging. Once opted out, template messages can no longer be delivered to them. |
| Send Image Message | `sendImageMessage` | Sends an image to a Landbot customer through their channel, referenced by a publicly reachable URL. |
| Send Location Message | `sendLocationMessage` | Sends a geographic location to a Landbot customer through their channel, rendered as a map pin. |
| Send Template Message | `sendTemplateMessage` | Sends an approved WhatsApp template message to a Landbot customer. This is the only way to open a WhatsApp conversation outside the 24-hour customer service window. |
| Send Text Message | `sendTextMessage` | Sends a plain text message to a Landbot customer through their channel. On WhatsApp this only succeeds inside the 24-hour customer service window; outside it, use Send Template Message instead. |
| Unarchive Customer | `unarchiveCustomer` | Returns a previously archived Landbot conversation to the active inbox. |
| Unassign Customer | `unassignCustomer` | Removes the current agent or bot assignment from a Landbot conversation, returning it to the unassigned queue. |
| Unblock Customer | `unblockCustomer` | Unblocks a previously blocked Landbot customer, allowing them to message again. |
| Update Customer Field | `updateCustomerField` | Updates the value of an existing custom field on a Landbot customer's profile. |
