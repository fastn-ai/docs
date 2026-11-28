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

## Connect in Fastn

Your customers connect Tiny Talk AI from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Tiny Talk AI**.
2. Select **Connect** on the Tiny Talk AI card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Tiny Talk AI's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Chat Completion</td><td><code>createChatCompletion</code></td><td>Send a conversation to a Tiny Talk agent and receive its AI-generated reply, together with token usage and any knowledge-base sources cited. Pass the whole message history so the agent keeps context across turns. Set stream to false to receive one complete JSON response; leaving it unset uses the agent's own streaming setting. Each call consumes one AI response from the workspace message allowance.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Contact Created</td><td><code>contact.created</code></td><td>A new contact is created on the Tiny Talk agent.</td></tr><tr><td>Contact Lead Updated</td><td><code>contact.lead.updated</code></td><td>A contact with a lead role is updated, for example when the visitor submits the lead qualification form.</td></tr><tr><td>Conversation Created</td><td><code>conversation.created</code></td><td>A new conversation is started with the Tiny Talk agent.</td></tr><tr><td>Human Takeover Requested</td><td><code>takeover.request</code></td><td>A visitor asked to be handed over to a human agent.</td></tr><tr><td>Message Created</td><td><code>message.created</code></td><td>A new message is created in a conversation, from a visitor, the AI agent or a human agent.</td></tr></tbody></table>
