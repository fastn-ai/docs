---
description: Making a connection, from picking the connector to confirming it landed.
---

# Connect a system, step by step

Making a connection is how a connector goes from a definition to something that can actually call an API. There are two ways in — the **Connect** button on the connector itself, or **New connection** on the [Connections](../connections/README.md) page — and both lead to the same authorisation flow.

{% stepper %}
{% step %}
#### Pick the connector

Press **Connect** (or **Add another connection**) on the connector's card or detail header, or open **New connection** and find the system in the **Connect a system** picker — a searchable, A–Z list of every connector in the catalogue.
{% endstep %}

{% step %}
#### Choose the authentication method

If the connector offers more than one method, choose one. The **Auth** tab (above) describes the two shapes in the customer's own terms — *Your customers sign in with the provider and approve access* for OAuth, and *Your customers paste a key they generate themselves* for an API key.
{% endstep %}

{% step %}
#### Provide the credential

**OAuth** sends you to the provider to sign in and approve the requested access; fastn receives the tokens. An **API key** (and the other keyed methods) is entered in the connect form itself. Either way, fastn stores the credential encrypted and never displays it again.
{% endstep %}

{% step %}
#### Confirm it landed

A completed connection appears on the connector's **Connections** tab — which reads `Nobody has connected yet` until the first one — and on the workspace-wide [Connections](../connections/README.md) page, where you can check its status and **Reconnect** or **Disconnect** it.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Customer connections are meant to be made by the customer, through your embedded widget — that is what keeps their credentials theirs. Use **New connection** for links your own organisation owns, such as your own Slack workspace.
{% endhint %}
