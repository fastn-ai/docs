---
description: >-
  Connect Claude, ChatGPT, Cursor or another AI client to your integrations from
  the widget, with no fastn account.
---

# Connect Claude and other AI clients

Everything you can do in the integrations widget (see your connections, run an action against a connected app, check what synced) you can also do from an AI client such as Claude, ChatGPT or Cursor. The client connects over MCP (the Model Context Protocol) and sees your integrations as tools it can use.

You don't need a fastn account. The connection is scoped to your organization only.

## Connect your AI client

{% stepper %}
{% step %}
### Generate a URL in the widget

Open the integrations widget in the product you use. In the widget header, open the **⋯** menu and click **Generate MCP URL**, then **Copy** the URL.
{% endstep %}

{% step %}
### Add it to your AI client as a custom connector

* **Claude:** add a custom connector in Claude's connector settings, give it a name such as *Integrations*, paste the URL, then connect it.
* **Claude Code:** run `claude mcp add --transport http integrations <the URL you copied>`.
* **ChatGPT, Cursor and other clients:** add a custom MCP connector or server and paste the URL.

The exact menus belong to each client and can change; check the client's own help if you can't find where to add a custom connector.
{% endstep %}

{% step %}
### Ask for what you need

Ask in plain words, for example *Which of my integrations failed this week?* or *Run the contact sync for Acme now.* The client calls your integrations as tools.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
The URL is **valid for 10 minutes and works once**. If it expires before you paste it, generate a new one. Once connected, the connection stays until it is disconnected.
{% endhint %}

## "Could not create a link. Try again."

If this message appears when you click **Generate MCP URL**, try once more. If it keeps appearing, the product's widget session may not be tied to you as a person, which the link needs. That is set up on the product's side, so contact the product's support team.

## No "Generate MCP URL" in the menu?

The product you use decides whether to offer it. If it isn't in the **⋯** menu, ask their support team: they can switch it on in their widget settings, or connect the client for you.

## What the connection can and can't do

* **It reaches only your organization's connections.** It can't see any other customer of the same product.
* **It acts as you.** Anything the client calls runs against your connected apps, including changes such as creating or updating records. Review what you ask it to do.
* **It can be turned off.** The provider of the product can disconnect any AI client from their side at any time. To disconnect yours, ask them.

{% hint style="warning" %}
Treat the URL like a password while it is valid: don't paste it into chats, tickets or documents.
{% endhint %}

## What you can do next

* [Extend a pre-built integration](extending-a-prebuilt-integration.md): change what an integration does, from inside the widget
* [Get alerted](getting-alerted.md): be told when something breaks
