---
description: "BotMape is an AI agent platform for training custom chat agents on your own content and deploying them on the web, WhatsApp, Slack and Telegram, with built-in…"
hidden: true
---

# BotMape

<img src="../../.gitbook/assets/connectors/lg/bot-mape.png" alt="BotMape logo">

BotMape is an AI agent platform for training custom chat agents on your own content and deploying them on the web, WhatsApp, Slack and Telegram, with built-in CRM, lead capture and appointment booking. This connector covers the BotMape REST API: AI agents, knowledge base entries, chat messaging, conversations, leads, appointments and analytics.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [botmape.com](https://botmape.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `botMape` |

## Use it

Add BotMape from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.botMape.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Knowledge Entry | `addKnowledgeEntry` | Adds training content (FAQ text, documentation, policies) to an AI agent's knowledge base. The content is automatically embedded so the agent can use it in answers. Returns the created entries. |
| Create AI Agent | `createAiAgent` | Creates a new AI agent (chatbot) with a name and optional description, welcome message, system prompt and widget color. Returns the created agent. Free-plan accounts are limited to one agent; BotMape responds 403 when the plan limit is reached. |
| Create Appointment | `createAppointment` | Books a new appointment for a customer on a given date and time, attached to an AI agent. When called with an API key the agent id is required so BotMape can determine the owning account. Returns the created appointment with status pending. |
| Create Lead | `createLead` | Creates a new lead in the BotMape CRM with contact details, status and notes. Use it to push leads from other tools into BotMape. Returns the created lead. |
| Delete AI Agent | `deleteAiAgent` | Permanently deletes an AI agent (chatbot) and its knowledge base, conversations and analytics. This cannot be undone. |
| Delete Knowledge Entry | `deleteKnowledgeEntry` | Removes a single knowledge base entry from an AI agent's training data. BotMape returns success even when the entry id no longer exists. |
| Get AI Agent | `getAiAgent` | Retrieves the full configuration of a single AI agent (chatbot) by its id, including personality, widget appearance, lead capture and integration settings. |
| Get AI Agent Analytics | `getAiAgentAnalytics` | Returns usage analytics for a single AI agent: total conversations, total messages and the number of currently active conversations. |
| Get Current User | `getCurrentUser` | Returns the BotMape account that owns the API key, including the account id, email, name and subscription plan. Useful for verifying credentials. |
| Get Platform Analytics | `getPlatformAnalytics` | Returns aggregate analytics across all AI agents in the account: total conversations and messages, daily trends and a per-agent breakdown. |

<details>

<summary>See 8 more actions</summary>

* **List AI Agents** `listAiAgents`: Returns all AI agents (chatbots) owned by the authenticated BotMape account, with their configuration, widget appearance and integration settings.
* **List Appointments** `listAppointments`: Returns all appointments booked in the account, whether scheduled by an AI agent during a conversation or added manually, with customer details, date, time, service and status.
* **List Captured Leads For Agent** `listCapturedLeadsForAgent`: Returns the visitor contact details captured during conversations with a specific AI agent, one entry per conversation that supplied a name, email or phone.
* **List Conversations** `listConversations`: Returns all conversations held with an AI agent, newest first, with visitor details and timestamps of the first and latest message.
* **List Knowledge Entries** `listKnowledgeEntries`: Returns every knowledge base entry that trains an AI agent's responses, including the stored content, metadata and embedding vector for each entry.
* **List Leads** `listLeads`: Returns all CRM leads in the account, whether captured by an AI agent during a conversation or added manually, with status, source, score and notes.
* **Send Chat Message** `sendChatMessage`: Sends a visitor message to an AI agent and returns the AI-generated reply together with the conversation id. Pass the returned conversation id on later calls to continue the same conversation.
* **Update AI Agent** `updateAiAgent`: Updates an existing AI agent's name, description, welcome message, system prompt, widget color, website URL or active status. Only the fields you supply are changed. Returns the updated agent.

</details>
