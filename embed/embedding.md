---
description: Four ways to put the widget in your product, and how to hand it a token safely.
---

# Embedding the widget

**Widgets → Embed**

<figure><img src="../.gitbook/assets/widget-embed.jpg" alt="The Embed tab"><figcaption></figcaption></figure>

Pick a **USER** at the top — the widget is always scoped to one of your customers — then choose how to mount it.

| Method     | Requirement                          | Status      |
| ---------- | ------------------------------------ | ----------- |
| **Iframe** | Anywhere you control HTML            | Available   |
| **SDK**    | You can run JavaScript               | Available   |
| **A2A**    | Agent-to-agent                       | Coming soon |

---

## Iframe

The simplest option: an HTML tag.

```html
<iframe
  src="https://YOUR_FASTN_HOST/api/v1/embed/iframe?token=YOUR_EMBED_TOKEN"
  style="width:100%; height:600px; border:none"
  allow="clipboard-write"
></iframe>
```

Use it for email, a CMS block, or anywhere you only control markup.

{% hint style="danger" %}
The snippet the dashboard generates contains a live token in the URL. That is fine for a first run and wrong for production — URLs end up in logs, referrers and browser history. For production, mint short-lived tokens from your backend and keep them out of the URL. The SDK exists for exactly that.
{% endhint %}

---

## SDK

<figure><img src="../.gitbook/assets/widget-embed-sdk.jpg" alt="The SDK embed options"><figcaption></figcaption></figure>

```bash
npm install @fastn-ai/embed
```

The SDK mounts the same iframe and adds what a raw tag cannot: events when a user connects an app, silent token refresh so long sessions do not dead-end, live theming, and modal mode.

Four entry points, depending on how much of the UI you want to own:

| Entry point                  | Package path              | Use when                                                         |
| ---------------------------- | ------------------------- | ------------------------------------------------------------------ |
| **React component**          | `@fastn-ai/embed/react`   | Your app is React and you want the whole panel.                   |
| **Connect card**             | `@fastn-ai/embed/react`   | You want the smallest surface: one card, one button.              |
| **Script tag**               | `@fastn-ai/embed`         | Vue, Svelte, Rails, plain HTML — anything that runs JS.           |
| **Build your own UI**        | `@fastn-ai/embed/headless` | The integrations screen has to look like the rest of your product. |

### React

```tsx
import { FastnHub } from '@fastn-ai/embed/react';

export function Integrations() {
  return (
    <FastnHub
      baseUrl="https://dev.gcp.fastn.ai"
      orgId="YOUR_ORG_ID"
      token={embedToken}
      onConnected={(e) => {
        // Refresh your app's data after the user connects an integration.
      }}
    />
  );
}
```

`baseUrl` points at a specific deployment. On fastn production the SDK defaults to it, so that line can go.

Because fastn hosts the screen, it gains features without you shipping a release, and its styles can never collide with yours.

---

## Tokens

An embed token identifies one of your customers to the widget. The dashboard shows a live one so you can try things immediately; it is short-lived and not meant for shipping.

For production, use the **Token API** to mint a token from your backend for each user session:

1. Your backend authenticates the user, as it already does.
2. It calls fastn's token endpoint with your API key and the customer identifier.
3. It returns the short-lived token to your frontend.
4. The SDK mounts with that token and refreshes it silently.

Your API key never reaches the browser. See [API keys](../manage/api-keys.md).

---

## Shareable links

Instead of a snippet, send a link. It keeps working until you revoke it, and the URL carries no token.

{% hint style="warning" %}
The reference in a shareable link *is* the credential. Treat the link itself as a secret — anyone who has it can act as that customer.
{% endhint %}

Create links per customer under **Shareable links** on the Embed tab, and revoke them there.

---

## Branding the OAuth screen

By default, your customers see **fastn.ai** on the provider's consent screen. To show your own brand, register your own OAuth app for that connector under its **Auth** tab. See [Connectors](../build/connectors.md).
