---
description: "Tiny Talk AI builds custom AI chat agents for websites: agents answer from a trained knowledge base, capture leads, and hand off to humans."
hidden: true
---

# Tiny Talk AI

<img src="../../.gitbook/assets/connectors/lg/tiny-talk-ai.png" alt="Tiny Talk AI logo">

This connector covers the documented chat API (POST /v1/chat/completions) plus Run Agent, Get Agent and the public agent settings, all authorised with the server API key (api-key header).

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [tinytalk.ai](https://tinytalk.ai) |
| **Authentication** | Credentials you enter |
| **Slug** | `tinyTalkAi` |

## Use it

Add Tiny Talk AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.tinyTalkAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Chat Completion</td><td><code>createChatCompletion</code></td><td>Send a conversation to a Tiny Talk agent and receive its AI-generated reply, together with token usage and any knowledge-base sources cited. Pass the whole message history so the agent keeps context across turns. Set stream to false to receive one complete JSON response; leaving it unset uses the agent's own streaming setting. Each call consumes one AI response from the workspace message allowance.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Contact Created</td><td><code>contact.created</code></td><td>A new contact is created on the Tiny Talk agent. PAYLOAD SCHEMA IS MODELLED, not captured: Tiny Talk's webhook documentation states that the payload structure varies by event type and publishes no sample, and the sample-delivery endpoint relays only the receiver's own response, so no delivery body could be captured from this account.</td></tr><tr><td>Contact Lead Updated</td><td><code>contact.lead.updated</code></td><td>A contact with a lead role is updated, for example when the visitor submits the lead qualification form. PAYLOAD SCHEMA IS MODELLED, not captured, for the reason given on Contact Created.</td></tr><tr><td>Conversation Created</td><td><code>conversation.created</code></td><td>A new conversation is started with the Tiny Talk agent. PAYLOAD SCHEMA IS MODELLED, not captured, for the reason given on Contact Created.</td></tr><tr><td>Human Takeover Requested</td><td><code>takeover.request</code></td><td>A visitor asked to be handed over to a human agent. PAYLOAD SCHEMA IS MODELLED, not captured, for the reason given on Contact Created.</td></tr><tr><td>Message Created</td><td><code>message.created</code></td><td>A new message is created in a conversation, from a visitor, the AI agent or a human agent. PAYLOAD SCHEMA IS MODELLED, not captured, for the reason given on Contact Created.</td></tr></tbody></table>
