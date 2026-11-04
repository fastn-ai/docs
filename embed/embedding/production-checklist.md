---
description: >-
  What to check before your customers see the widget: tokens, tenancy, hosts,
  OAuth branding, share links and the problems real deployments hit.
---

# Embedding in production

The [iframe](iframe.md) is one HTML tag, and a first run takes minutes. Going live for real customers takes a few more decisions. This page collects them, along with the problems teams have actually hit when embedding fastn in production.

## Before you go live

{% stepper %}
{% step %}
### Mint a token per customer, on your backend

Never ship the dashboard's sample snippet: it contains a live token in the URL, and URLs end up in logs, referrers and browser history. Your backend calls the token endpoint with your API key, scoped to the signed-in customer, and passes only the short-lived token to the browser. Tokens last eight hours and a session can be refreshed for up to seven days. Mint a fresh token per session, or use the [SDK](sdk.md), which refreshes silently and tells you when the session ends. See [Generate embed tokens](../../tutorials/developer/generating-embed-tokens.md).
{% endstep %}

{% step %}
### Scope every token to exactly one customer

A token must identify one customer. If an API key covers several customers and you don't say which one, the widget cannot know whose connections to show. Name the customer on every mint. Either create it first under **Operate → Customers**, or let the token call register it on first use with `createIfMissing` (needs the **Embed backend** preset or another key with `customers.create`, `endOrgId` in the body rather than `x-org-id`, and a key without enforced identity verification). See [Tokens](token-api.md) and [Customers and tenancy](../../tutorials/developer/understanding-tenancy.md).
{% endstep %}

{% step %}
### Use the current host

All embed and token calls go to `https://api.fastn.dev`. Older snippets that point at `live.gcp.fastn.ai` stop working when that host is switched off, so search your codebase for it before launch.
{% endstep %}

{% step %}
### Brand the OAuth consent screen

Unless you register your own OAuth app for a connector, your customers see **fastn.ai** on the provider's consent screen (for example, "fastn.ai wants to access your HubSpot account"). For production, set up your own OAuth app under the connector's **Auth** tab so the consent screen shows your product's name. See [Auth methods and providers](../../build/connectors/auth-methods.md).
{% endstep %}

{% step %}
### Allow the widget origin and clipboard

Keep `allow="clipboard-write"` (and the dashboard snippet's `referrerpolicy="strict-origin-when-cross-origin"`) on the iframe so customers can copy webhook URLs and keys out of the widget. If your product sets a Content Security Policy, add `https://api.fastn.dev` to `frame-src`.
{% endstep %}

{% step %}
### Publish, then test as a customer

Customers only see what you have saved and published in the widget builder. Use **Preview** and the customer selector (it reads **View as admin** until you pick a customer) in the widget builder to see exactly what a customer sees, then connect a real test account end to end before you announce it.
{% endstep %}
{% endstepper %}

## Common problems and how to avoid them

| What happens | Why | What to do |
| --- | --- | --- |
| The widget shows your admin integrations, or the wrong customer's | The token was minted without a customer, or with a key shared across customers | Mint one token per customer, from your backend, every session |
| The embed worked last month and is now blank | The snippet points at a retired host | Use `https://api.fastn.dev` for every embed and token call |
| Customers are confused by "fastn.ai" on the Google or HubSpot login | No custom OAuth app is registered for that connector | Register your own OAuth app on the connector's **Auth** tab |
| A customer needs integrations before you have shipped the embed | Your engineering team has not added the iframe yet | Send a [shareable link](README.md) from **Embed > Widget > Embed** for a pilot. Treat the link as a secret, set an expiry, and revoke it when the pilot ends |
| A connection needs two logins (for example HubSpot, then an app ID and API key for the second system) | The integration uses two connectors | Tell customers up front that the widget asks for both, in order |
| Events from the source app never arrive | The source app has no API to register webhooks, so registration is manual | Show customers where to copy the webhook URL in the widget and where to paste it in the source app |
| You need a layout the iframe cannot do | The iframe has one general-purpose design, styled through the widget builder | Use the [SDK](sdk.md) for events, theming and modal mode, or build your own UI on the headless package |

{% hint style="info" %}
Share links skip your backend entirely. They are right for pilots, proofs of concept and customers who cannot change their code yet. For anything long-lived, embed the widget with a per-customer token instead.
{% endhint %}

## Related

{% content-ref url="../../tutorials/developer/embedding-quickstart.md" %}
[Embedding quickstart](../../tutorials/developer/embedding-quickstart.md)
{% endcontent-ref %}

{% content-ref url="token-api.md" %}
[Token API](token-api.md)
{% endcontent-ref %}
