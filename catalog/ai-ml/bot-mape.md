---
description: "BotMape is a platform for custom AI chat agents. Create and manage agents and their knowledge, capture leads, book appointments and read analytics."
hidden: true
---

# BotMape

<img src="../../.gitbook/assets/connectors/lg/bot-mape.png" alt="BotMape logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [botmape.com](https://botmape.com) |
| **Authentication** | API key |
| **Slug** | `botMape` |

## Setup

Your customers enter their API key for BotMape when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect BotMape from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **BotMape**.
2. Select **Connect** on the BotMape card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use BotMape's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Knowledge Entry</td><td><code>addKnowledgeEntry</code></td><td>Adds training content (FAQ text, documentation, policies) to an AI agent's knowledge base. The content is automatically embedded so the agent can use it in answers. Returns the created entries.</td></tr><tr><td>Create AI Agent</td><td><code>createAiAgent</code></td><td>Creates a new AI agent (chatbot) with a name and optional description, welcome message, system prompt and widget color. Returns the created agent. Free-plan accounts are limited to one agent; BotMape responds 403 when the plan limit is reached.</td></tr><tr><td>Create Appointment</td><td><code>createAppointment</code></td><td>Books a new appointment for a customer on a given date and time, attached to an AI agent. When called with an API key the agent id is required so BotMape can determine the owning account. Returns the created appointment with status pending.</td></tr><tr><td>Create Lead</td><td><code>createLead</code></td><td>Creates a new lead in the BotMape CRM with contact details, status and notes. Use it to push leads from other tools into BotMape. Returns the created lead.</td></tr><tr><td>Delete AI Agent</td><td><code>deleteAiAgent</code></td><td>Permanently deletes an AI agent (chatbot) and its knowledge base, conversations and analytics. This cannot be undone.</td></tr><tr><td>Delete Knowledge Entry</td><td><code>deleteKnowledgeEntry</code></td><td>Removes a single knowledge base entry from an AI agent's training data. BotMape returns success even when the entry id no longer exists.</td></tr><tr><td>Get AI Agent</td><td><code>getAiAgent</code></td><td>Retrieves the full configuration of a single AI agent (chatbot) by its id, including personality, widget appearance, lead capture and integration settings.</td></tr><tr><td>Get AI Agent Analytics</td><td><code>getAiAgentAnalytics</code></td><td>Returns usage analytics for a single AI agent: total conversations, total messages and the number of currently active conversations.</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Returns the BotMape account that owns the API key, including the account id, email, name and subscription plan. Useful for verifying credentials.</td></tr><tr><td>Get Platform Analytics</td><td><code>getPlatformAnalytics</code></td><td>Returns aggregate analytics across all AI agents in the account: total conversations and messages, daily trends and a per-agent breakdown.</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List AI Agents</td><td><code>listAiAgents</code></td><td>Returns all AI agents (chatbots) owned by the authenticated BotMape account, with their configuration, widget appearance and integration settings.</td></tr><tr><td>List Appointments</td><td><code>listAppointments</code></td><td>Returns all appointments booked in the account, whether scheduled by an AI agent during a conversation or added manually, with customer details, date, time, service and status.</td></tr><tr><td>List Captured Leads For Agent</td><td><code>listCapturedLeadsForAgent</code></td><td>Returns the visitor contact details captured during conversations with a specific AI agent, one entry per conversation that supplied a name, email or phone.</td></tr><tr><td>List Conversations</td><td><code>listConversations</code></td><td>Returns all conversations held with an AI agent, newest first, with visitor details and timestamps of the first and latest message.</td></tr><tr><td>List Knowledge Entries</td><td><code>listKnowledgeEntries</code></td><td>Returns every knowledge base entry that trains an AI agent's responses, including the stored content, metadata and embedding vector for each entry.</td></tr><tr><td>List Leads</td><td><code>listLeads</code></td><td>Returns all CRM leads in the account, whether captured by an AI agent during a conversation or added manually, with status, source, score and notes.</td></tr><tr><td>Send Chat Message</td><td><code>sendChatMessage</code></td><td>Sends a visitor message to an AI agent and returns the AI-generated reply together with the conversation id. Pass the returned conversation id on later calls to continue the same conversation.</td></tr><tr><td>Update AI Agent</td><td><code>updateAiAgent</code></td><td>Updates an existing AI agent's name, description, welcome message, system prompt, widget color, website URL or active status. Only the fields you supply are changed. Returns the updated agent.</td></tr></tbody></table>

</details>

