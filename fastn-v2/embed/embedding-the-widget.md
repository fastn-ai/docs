---
description: >-
  Three ways to put the widget in your product, and how to hand it a token
  safely.
---

# Embedding the widget

**Widgets → Embed**

![The Embed tab](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/widget-embed.jpg)

Pick a **USER** at the top — the widget is always scoped to one of your customers, and the selector scopes the snippet the tab generates — then choose how to mount it.

| Method     | Requirement               | Status      |
| ---------- | ------------------------- | ----------- |
| **Iframe** | Anywhere you control HTML | Available   |
| **SDK**    | You can run JavaScript    | Available   |
| **A2A**    | Agent-to-agent            | Coming soon |

***

## Iframe

The simplest option: an HTML tag.

```html
<iframe
  src="https://YOUR_FASTN_HOST/api/v1/embed/iframe?token=YOUR_EMBED_TOKEN"
  style="width:100%; height:600px; border:none"
></iframe>
```

Use it for a CMS block, or anywhere you only control markup.

{% hint style="danger" %}
The snippet the dashboard generates contains a live token in the URL — the tab says so. That is fine for a first run and wrong for production: URLs end up in logs, referrers and browser history. For production, mint tokens from your backend and keep them out of the URL. The SDK exists for exactly that.
{% endhint %}

***

## SDK

![The SDK embed options](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/widget-embed-sdk.jpg)

The SDK mounts the same iframe and adds what a raw tag cannot: events when a user connects an app, token refresh, live theming, and modal mode.

Four variants, depending on how much of the UI you want to own:

| Variant               | Package path               | Use when                                                           |
| --------------------- | -------------------------- | ------------------------------------------------------------------ |
| **React component**   | `@fastn-ai/embed/react`    | Your app is React and you want the whole panel.                    |
| **Connect card**      | `@fastn-ai/embed/react`    | You want the smallest surface: one card, one button.               |
| **Script tag**        | hosted bundle, no install  | Vue, Svelte, Rails, plain HTML — anything that runs JS.            |
| **Build your own UI** | `@fastn-ai/embed/headless` | The integrations screen has to look like the rest of your product. |

### React

The confirmed exports are `FastnConnectCard`, `FastnHub` and `FastnProvider`; the headless entry point exposes the hooks `useConnectors`, `useConnections` and `useConnect`.

`FastnProvider` supplies the session the other components read, so wrap your tree in it rather than mounting `FastnHub` bare. Copy the exact props from the dashboard's generated snippet — they are rendered there for the user you selected.

### Script tag

Not an npm install: a hosted bundle you load with a `<script>` tag.

```html
<script src="https://YOUR_FASTN_HOST/api/v1/embed/assets/fastn-embed.min.js"></script>
```

```javascript
const hub = FastnEmbed.createFastnEmbed({ /* config from the Embed tab */ });

hub.mount('#hub');   // inline
hub.open();          // or as a modal

hub.on('connected', (e) => {
  // Refresh your app's data after the user connects an integration.
});
```

Because fastn hosts the screen, it gains features without you shipping a release, and its styles can never collide with yours.

***

## Tokens

An embed token identifies one of your customers to the widget. The dashboard shows a live 8-hour token so you can try things immediately. Mint your own from your backend for production.

### The Token API

```http
POST /api/v1/embed/token
Authorization: Bearer <API key>
x-org-id: <orgId>
```

```json
{
  "token": "emb_…",
  "endOrgId": "…",
  "role": "end_user",
  "expiresIn": 28800
}
```

`expiresIn` is 28800 seconds — eight hours.

If the API key is pinned to a particular customer, send the customer in the body instead of the header:

```json
{ "endOrgId": "…" }
```

Your API key never reaches the browser. See [API keys](../manage/api-keys.md).

### Refresh, and the session cap

```http
POST /api/v1/embed/token/refresh
```

{% hint style="warning" %}
Refresh is capped at **seven days per session**. At the cap the widget posts `fastn:session-expired` to the parent window and stops. Long-lived sessions do not refresh indefinitely — listen for that message and start a new session by minting a fresh token.
{% endhint %}

The flow for production:

1. Your backend authenticates the user, as it already does.
2. It calls `POST /api/v1/embed/token` with your API key and the customer identifier.
3. It returns the token to your frontend.
4. The SDK mounts with that token and refreshes it, until the seven-day session cap.

***

## Shareable links

Instead of a snippet, send a link. It keeps working until you revoke it, and the URL carries no token.

{% hint style="warning" %}
The reference in a shareable link _is_ the credential. Treat the link itself as a secret — anyone who has it can act as that customer.
{% endhint %}

Create links per customer under **Shareable links** on the Embed tab. Each row offers **Copy**, **Show** and **Revoke**.
