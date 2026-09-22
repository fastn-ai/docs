---
description: Three ways to put the widget in your product, and how to hand it a token safely.
---

# Embedding the widget

**Widgets → Embed**

<figure><img src="../../.gitbook/assets/widget-embed.jpg" alt="The Embed tab with Iframe selected beside SDK and A2A soon, a USER selector set to NewTest, and an Embed Code block with a Copy button, beside a preview reading TikTok Shop, 0 of 1 connected"><figcaption>The preview follows the selected user, pick one and the panel shows that customer's real connection state, not a mock-up.</figcaption></figure>

## Pick the customer first

The widget is always scoped to **one** of your customers, so the **USER** dropdown at the top is not a preview toggle. It decides who the generated snippet is for.

The dropdown lists the customers on your account, by their identifier, for example `test-tenant`. Selecting one does two things at once:

* the preview beside it shows **that customer's real connection state**, not a mock-up, so `TikTok Shop, 0 of 1 connected` is the truth for that customer
* the **Embed Code** block regenerates with a token scoped to them

If the dropdown is empty, you have no customers yet. Create one under [Customers](../../operate/customers.md) first.

Then choose how to mount it.

| Method     | Requirement                          | Status      |
| ---------- | ------------------------------------ | ----------- |
| **Iframe** | Anywhere you control HTML            | Available   |
| **SDK**    | You can run JavaScript               | Available   |
| **A2A**    | Agent-to-agent                       | Coming soon |

{% hint style="danger" %}
**The snippet on this tab contains a live token.** It is there so you can paste it and see the widget working in seconds, and it is not safe for production: anyone with the URL can act as that customer until the token expires.

For production, mint short-lived tokens from your backend and keep them out of the URL. The [SDK](sdk.md) is built for that pattern, and the [Token API](token-api.md) is how you mint them.
{% endhint %}

## Shareable links

Instead of a snippet, send a link. It keeps working until you revoke it, and the URL carries no token.

{% hint style="warning" %}
The reference in a shareable link *is* the credential. Treat the link itself as a secret: anyone who has it can act as that customer.
{% endhint %}

Create links per customer under **Shareable links** on the Embed tab. Each row offers **Copy**, **Show** and **Revoke**.

A shareable link suits the cases where you cannot embed at all: onboarding a customer before they have access to your product, letting someone connect their accounts from an email, or handing a link to a customer's IT team to authorise on their behalf. **Revoke** is immediate, and it is the only way to withdraw one.

### In this section

* [Iframe](iframe.md)
* [SDK](sdk.md)
* [Token API](token-api.md)
