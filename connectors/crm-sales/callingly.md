---
description: "Callingly is a lead response and speed-to-lead calling platform that instantly connects new inbound leads with available sales agents by phone and SMS."
---

# Callingly

Callingly is a lead response and speed-to-lead calling platform that instantly connects new inbound leads with available sales agents by phone and SMS. This connector covers the full Callingly REST API (v1): calls, leads, SMS, teams, team agent routing and caps, agents (users) and their availability schedules, agency client accounts, and outbound webhook subscriptions for call completed, lead created and lead updated events. Authenticates with a Callingly API key sent as a Bearer token.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [callingly.com](https://callingly.com) |
| **Authentication** | Bearer token |
| **Actions** | 32 |
| **Events** | 4 |
| **Slug** | `callingly` |

## Use it

Add Callingly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.callingly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Agent | `createAgent` | Creates a new agent (user) in Callingly who can receive routed lead calls. Returns the new agent's id. |
| Create Call | `createCall` | Submits a new lead to Callingly and places a real phone call: Callingly immediately rings the team's available agents and connects them to the lead, or schedules the call for a later time. Also creates the lead record. |
| Create Client | `createClient` | Agency partners: creates a new client account under your Callingly agency, with the client owner's name, company, email, phone number and login password. Callingly returns HTTP 200 with success false when the account cannot be created. |
| Create Team | `createTeam` | Creates a new call routing team in Callingly with its call mode, recording, whisper message, language, and agent and lead retry settings. Callingly offers no API to delete a team. |
| Create Webhook | `createWebhook` | Subscribes a URL to a Callingly event (call completed, SMS, lead created or lead updated), with optional filters on call direction, call status, lead status, team, inbound number or a changed lead field. |
| Delete Agent | `deleteAgent` | Permanently deletes an agent (user) from the Callingly account. |
| Delete Client | `deleteClient` | Agency partners: deletes a client account managed under your Callingly agency. |
| Delete Lead | `deleteLead` | Deletes a lead from Callingly. |
| Delete Webhook | `deleteWebhook` | Deletes a Callingly webhook subscription so its target URL stops receiving events. |
| Get Agent | `getAgent` | Retrieves a single Callingly agent (user) by id, including contact details, timezone, do-not-disturb flag and availability. |
| Get Agent Schedule | `getAgentSchedule` | Retrieves an agent's weekly availability schedule in Callingly, with the available time windows for each day of the week. |
| Get Call | `getCall` | Retrieves a single Callingly call by id, including status, lead outcome, duration, recording and waveform URLs, transcript, the agent, the lead and the team. |
| Get Lead | `getLead` | Retrieves a single Callingly lead by id, including contact details, status, result, team, tags, stage, scheduled call time and whether calling is stopped or the lead is blocked. |
| Get Team | `getTeam` | Retrieves a single Callingly team by id, including its call mode, recording setting, whisper text, language, retry schedule and agent availability. |
| Get Webhook | `getWebhook` | Retrieves a single Callingly webhook subscription by id. |
| List Agents | `listAgents` | Lists all agents (users) in the Callingly account with their contact details, extension, timezone, do-not-disturb flag and current availability. |
| List Calls | `listCalls` | Lists calls in the Callingly account, newest first, with optional date range and team filters and page-based pagination. Each call includes direction, status, lead outcome, duration, source and recording URL. |
| List Clients | `listClients` | Agency partners: lists the client accounts managed under your Callingly agency account, with each client's id, name, email and billed user and number counts. |
| List Leads | `listLeads` | Lists leads in the Callingly account with optional created-date range and phone number filters. Each lead includes contact details, status, result, team, tags, stage, recent calls, scheduled call time and lead owner. |
| List Team Agents | `listTeamAgents` | Lists the agents assigned to a Callingly team, with each agent's routing priority and daily call cap. |
| List Teams | `listTeams` | Lists all call routing teams in the Callingly account, returning each team's id, account id and name. |
| List Webhooks | `listWebhooks` | Lists all outbound webhook subscriptions in the Callingly account, with each webhook's event, target URL, filters and delivery health. |
| Remove Team Agent | `removeTeamAgent` | Removes a single agent from a Callingly team. The agent's user account is not deleted. |
| Send SMS | `sendSms` | Sends a real SMS text message from one of your Callingly numbers to a lead's phone number. Returns the lead, conversation and SMS ids. |
| Set Client Active Status | `setClientActiveStatus` | Agency partners: activates or deactivates a client account managed under your Callingly agency. |
| Update Agent | `updateAgent` | Updates a Callingly agent's name, phone number, extension, timezone or do-not-disturb status. Only the fields you pass are changed. |
| Update Agent Schedule | `updateAgentSchedule` | Replaces an agent's weekly availability schedule in Callingly. Pass every day with its availability and time windows; days you omit revert to Callingly's default of available all day. |
| Update Lead | `updateLead` | Updates a Callingly lead's contact details, source, company, status, result or stage, and can stop automatic calling or block the lead. Only the fields you pass are sent. |
| Update Team | `updateTeam` | Updates an existing Callingly team's name, call mode, recording, whisper message, language, and agent and lead retry settings. Only the fields you pass are sent. |
| Update Team Agent Settings | `updateTeamAgentSettings` | Updates an agent's routing priority and lead cap within a specific Callingly team. |
| Update Team Agents | `updateTeamAgents` | Replaces the set of agents assigned to a Callingly team. Agents not included in the list are removed from the team, so always pass the complete list of agent ids. |
| Update Webhook | `updateWebhook` | Partially updates a Callingly webhook subscription. Only the fields you pass are changed; when changing any event-specific filter (direction, call status, lead status, team, number, field or filter) also pass the webhook's event, because Callingly validates filters against the event in the same request. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Call Completed | `call_completed` | Fires when a Callingly call finishes (inbound or outbound). Registered through POST /v1/webhooks with event call_completed; each registration targets one event, so routing is per subscription. Callingly does not document the delivered payload or sign deliveries. The schema below is modelled on the documented Get Call response and has not been reconciled against a live delivery, because triggering one requires placing a real phone call. |
| Lead Created | `lead_created` | Fires when a new lead is created in Callingly. Registered with event lead_created; routing is per subscription. The schema below is modelled on the documented Get Lead response and has not been reconciled against a live delivery, because Callingly only creates leads through a real call or inbound lead source. |
| Lead Updated | `lead_updated` | Fires when a Callingly lead changes. Registered with event lead_updated, optionally narrowed with Create Webhook's field (lead_owner, result, stage, status, tags) and filter. Routing is per subscription. The schema below is modelled on the documented Get Lead response and has not been reconciled against a live delivery. |
| SMS Sent or Received | `sms` | Fires for Callingly SMS messages. This event value is accepted by the live Callingly webhooks API (verified by validation) but is not described in the public documentation. Routing is per subscription. The schema below is modelled on the documented Send SMS response and has not been reconciled against a live delivery, because triggering one requires sending a real SMS. |
