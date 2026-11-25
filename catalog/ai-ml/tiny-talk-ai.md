---
description: "Tiny Talk AI builds AI chat agents for websites. Send messages to your agent and get chat replies."
hidden: true
---

# Tiny Talk AI

<img src="../../.gitbook/assets/connectors/lg/tiny-talk-ai.png" alt="Tiny Talk AI logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [tinytalk.ai](https://tinytalk.ai) |
| **Authentication** | API key |
| **Slug** | `tinyTalkAi` |

## Setup

Your customers enter their API key for Tiny Talk AI when they connect. Nothing else needs setting up.

## Use it

Add Tiny Talk AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.tinyTalkAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Chat Completion</td><td><code>createChatCompletion</code></td><td>Send a conversation to a Tiny Talk agent and receive its AI-generated reply, together with token usage and any knowledge-base sources cited. Pass the whole message history so the agent keeps context across turns. Set stream to false to receive one complete JSON response; leaving it unset uses the agent's own streaming setting. Each call consumes one AI response from the workspace message allowance.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Contact Created</td><td><code>contact.created</code></td><td>A new contact is created on the Tiny Talk agent.</td></tr><tr><td>Contact Lead Updated</td><td><code>contact.lead.updated</code></td><td>A contact with a lead role is updated, for example when the visitor submits the lead qualification form.</td></tr><tr><td>Conversation Created</td><td><code>conversation.created</code></td><td>A new conversation is started with the Tiny Talk agent.</td></tr><tr><td>Human Takeover Requested</td><td><code>takeover.request</code></td><td>A visitor asked to be handed over to a human agent.</td></tr><tr><td>Message Created</td><td><code>message.created</code></td><td>A new message is created in a conversation, from a visitor, the AI agent or a human agent.</td></tr></tbody></table>
