---
description: "Tiny Talk AI builds custom AI chat agents for websites: agents answer from a trained knowledge base, capture leads, and hand off to humans."
---

# Tiny Talk AI

Tiny Talk AI builds custom AI chat agents for websites: agents answer from a trained knowledge base, capture leads, and hand off to humans. This connector covers the documented chat API (POST /v1/chat/completions) plus Run Agent, Get Agent and the public agent settings, all authorised with the server API key (api-key header).

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [tinytalk.ai](https://tinytalk.ai) |
| **Authentication** | Credentials you enter |
| **Actions** | 1 |
| **Events** | 5 |
| **Slug** | `tinyTalkAi` |

## Use it

Add Tiny Talk AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.tinyTalkAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Chat Completion | `createChatCompletion` | Send a conversation to a Tiny Talk agent and receive its AI-generated reply, together with token usage and any knowledge-base sources cited. Pass the whole message history so the agent keeps context across turns. Set stream to false to receive one complete JSON response; leaving it unset uses the agent's own streaming setting. Each call consumes one AI response from the workspace message allowance. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Contact Created | `contact.created` | A new contact is created on the Tiny Talk agent. PAYLOAD SCHEMA IS MODELLED, not captured: Tiny Talk's webhook documentation states that the payload structure varies by event type and publishes no sample, and the sample-delivery endpoint relays only the receiver's own response, so no delivery body could be captured from this account. |
| Contact Lead Updated | `contact.lead.updated` | A contact with a lead role is updated, for example when the visitor submits the lead qualification form. PAYLOAD SCHEMA IS MODELLED, not captured, for the reason given on Contact Created. |
| Conversation Created | `conversation.created` | A new conversation is started with the Tiny Talk agent. PAYLOAD SCHEMA IS MODELLED, not captured, for the reason given on Contact Created. |
| Human Takeover Requested | `takeover.request` | A visitor asked to be handed over to a human agent. PAYLOAD SCHEMA IS MODELLED, not captured, for the reason given on Contact Created. |
| Message Created | `message.created` | A new message is created in a conversation, from a visitor, the AI agent or a human agent. PAYLOAD SCHEMA IS MODELLED, not captured, for the reason given on Contact Created. |
