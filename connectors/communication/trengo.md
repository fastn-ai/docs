---
description: "Trengo is a multichannel customer engagement and helpdesk platform unifying WhatsApp, email, SMS, live chat, voice, and social channels into one team inbox."
---

# Trengo

Trengo is a multichannel customer engagement and helpdesk platform unifying WhatsApp, email, SMS, live chat, voice, and social channels into one team inbox. This connector wraps the Trengo REST API v2 for tickets, contacts, profiles, messages, WhatsApp, SMS, team chat, labels, teams, users, custom fields, quick replies, help center, and webhooks.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [trengo.com](https://trengo.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 32 |
| **Events** | 0 |
| **Slug** | `trengo` |

## Use it

Add Trengo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.trengo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Contact | `createContact` | Create a new contact. |
| Create Label | `createLabel` | Create a new label. |
| Create Team | `createTeam` | Create a new team. |
| Create Webhook | `createWebhook` | Register a new webhook subscription. Trengo will POST an event payload to the given URL when the specified event type occurs, signed with a 'Trengo-Signature' header ({timestamp};{hex_hmac_sha256} over '{timestamp}.{body}' using the returned signing_secret). |
| Delete Contact | `deleteContact` | Delete a contact by id. |
| Delete Label | `deleteLabel` | Delete a label by id. |
| Delete Team | `deleteTeam` | Delete a team by id. |
| Delete Webhook | `deleteWebhook` | Delete a registered webhook subscription by its id. Returns an empty object on success. |
| Get Contact | `getContact` | Get a single contact by id, including profile, channels, and notes. |
| Get Ticket | `getTicket` | Get a single ticket (conversation) by id. |
| Get User | `getUser` | Get a single user (agent) by id. |
| Get Webhook | `getWebhook` | Get a single registered webhook subscription by its id, including its title, target URL, event type and signing secret. |
| List Boards | `listBoards` | List all boards (kanban-style task boards) in the Trengo account. |
| List Business Hours | `listBusinessHours` | List all business hours schedules configured in the Trengo account. |
| List Contact Groups | `listContactGroups` | List all contact groups in the Trengo account. |
| List Contacts | `listContacts` | List all contacts in the Trengo account. |
| List CSAT Ratings | `listCsat` | List customer satisfaction (CSAT) ratings collected in the Trengo account. |
| List Custom Fields | `listCustomFields` | List all custom fields defined for tickets, contacts, or profiles. |
| List Help Centers | `listHelpCenters` | List all help center articles/pages configured in the Trengo account. |
| List Labels | `listLabels` | List all labels available in the Trengo account. |
| List Profiles | `listProfiles` | List all profiles (merged contact identities) in the Trengo account. |
| List Quick Replies | `listQuickReplies` | List all quick replies (canned responses) in the Trengo account. |
| List SMS Messages | `getSmsBalance` | List all outbound SMS messages sent from the Trengo account. |
| List Teams | `listTeams` | List all teams in the Trengo account. |
| List Ticket Messages | `listTicketMessages` | List all messages within a ticket (conversation). |
| List Ticket Results | `listTicketResults` | List ticket results (outcome tags used when closing tickets). |
| List Tickets | `listTickets` | List tickets (conversations) in the Trengo account. |
| List Users | `listUsers` | List all users (agents) in the Trengo account. Supports pagination and sorting. |
| List Webhooks | `listWebhooks` | List all registered webhook subscriptions in the Trengo account. |
| Update Contact | `updateContact` | Update an existing contact's name. |
| Update Label | `updateLabel` | Update an existing label's name or color. |
| Update Webhook | `updateWebhook` | Update the name, target URL and event type of an existing webhook subscription. All three body fields are required by Trengo. |
