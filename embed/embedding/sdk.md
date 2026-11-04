---
description: The SDK mounts the same iframe and adds events, token refresh, theming and modal mode.
---

# SDK

The SDK mounts the same iframe and adds what a raw tag cannot: events when a customer connects an app, token refresh, live theming, and modal mode.

{% hint style="info" %}
This page is the browser widget package, `@fastn-ai/embed`. The server-side package that calls the fastn API from your backend is `@fastn-ai/sdk`: see [SDK](../../reference/sdk/README.md).
{% endhint %}

Four variants, depending on how much of the UI you want to own:

| Variant                  | Package path                | Use when                                                          |
| ------------------------ | --------------------------- | ------------------------------------------------------------------- |
| **React component**      | `@fastn-ai/embed/react`     | Your app is React and you want the whole panel.                    |
| **Connect card**         | `@fastn-ai/embed/react`     | You want the smallest surface: one card, one button.               |
| **Script tag**           | hosted bundle, no install   | Vue, Svelte, Rails, plain HTML: anything that runs JS.            |
| **Build your own UI**    | `@fastn-ai/embed/headless`  | The integrations screen has to look like the rest of your product.  |

### React

`@fastn-ai/embed/react` exports `FastnHub`, `FastnHubModal`, `FastnConnectCard` and the `useFastnHub` hook. `FastnHub` and `FastnConnectCard` mount on their own, with no provider around them: pass the customer as `orgId`, and either a `token` or a `getToken` function that fetches one from your backend.

```tsx
import { FastnHub } from '@fastn-ai/embed/react';

<FastnHub
  orgId={customerId}
  getToken={() => fetch('/api/fastn-token').then(r => r.json()).then(d => d.token)}
  onConnected={({ connectorId }) => refetch()}
/>
```

Here `/api/fastn-token` is your own backend route, which mints a token with the [Token API](token-api.md) and returns `{ "token": "emb_..." }` to the browser, never the API key. Copy the exact props from the dashboard's generated snippet. They are rendered there for the customer you selected.

### Build your own UI

`FastnProvider` and the hooks `useConnectors`, `useConnections` and `useConnect` come from `@fastn-ai/embed/headless/react`, and are only for the **Build your own UI** variant, where you render every pixel and fastn supplies the data, the auth and the OAuth popup. Your page's origin has to be registered on the API key that mints your tokens, or the browser blocks the calls before they are sent.

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
  // Refresh your app's data after the customer connects an integration.
});
```

Because fastn hosts the screen, it gains features without you shipping a release, and its styles can never collide with yours.
