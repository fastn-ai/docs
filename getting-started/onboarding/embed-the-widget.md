---
description: Setup step 3 and the going-live item that follows it. Put the widget inside your product, with the five-part developer setup.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Set up and add the widget

Put your integrations inside your product. The widget is the panel where your customers find, connect, and customize integrations, under your brand, without signing in to fastn. It holds your connectors, the workflows behind them, and the widget assistant your customers use to adjust them.

**Required to go live.** You embed the widget once. Integrations you add later, and changes to the widget, appear in it without a release of your product.

### What it's made of

| Component | Where it lives | What it does |
| --- | --- | --- |
| Widget | Inside your product | The panel your customers use to connect and customize integrations |
| Widget builder | fastn | Sets the widget's look, features, and **Allowed Origins** (which sites can show it) |
| API key and identity secret | Your backend | Authenticate your server, and sign which customer and user each call is for |
| Customer | fastn, registered by your backend | One of your customers; their connections and data stay separate |
| Embed token | Your backend, then your page | Short-lived and for one customer; a new one on every page load |
| Iframe or SDK | Your frontend | Shows the widget with the embed token |

### Ways to do it

| Way | Best when |
| --- | --- |
| Iframe | Anywhere you control HTML: one tag with the embed token |
| SDK | You want events, token refresh, live theming, or your own UI (check the docs for availability) |
| Shareable link | No developer yet: send a customer a link, and revoke it when done |
| MCP URL | Customers want their own AI tools to use their connections |

### Use cases and scenarios

| Use case | How you set it up |
| --- | --- |
| Settings page in a B2B product | The iframe on your settings page, with each embed token minted for the signed-in customer |
| Plans and tiers | Register each customer with a tier and connection limit; show some integrations to specific customers only |
| Integrations that start from your product | Your backend calls a webhook trigger on each event (part 5 below) |

### Developer setup

Five parts, each done once; part 5 is optional. Keep the API key and identity secret on your backend: only the embed token reaches the browser.

**1 · Create an API key.** In **Embed** → **API keys**, create a key with the **Embed backend** permissions (it mints embed tokens) that can reach **Every customer**, and turn on **Verify caller identity (HMAC)**. The other permission options are Admin, Developer, Operator, Viewer, End User, and Custom. You get an API key and an identity secret (shown once). Don't limit the key to specific customers: your backend uses this one key for every customer, including ones you register later, and the identity hash says which customer each call is for. A key limited to specific customers can't get embed tokens for customers it doesn't list.

Registering customers (part 2) needs a second key with the **Admin** preset, because setting a customer's tier and limits needs full access. Leaving **Verify caller identity (HMAC)** off on this key is simplest, because a key that enforces it refuses every call without identity headers. Keep it in your backend's provisioning code only. See [API keys](../../manage/api-keys.md).

**2 · Register each customer** (backend, once per customer, with the **Admin** key), with your own ID for them, their tier and connection limit. The **Embed backend** key gets `403` here.

```bash
curl -X POST https://api.fastn.dev/api/v1/orgs \
  -H "Authorization: Bearer $FASTN_ADMIN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "Northwind", "orgId": "northwind", "tier": "pro", "limits": {"connections": 3}}'
```

`orgId` is your own reference for the customer. If you leave it out, fastn uses the customer's slug as its external reference. Later calls (`x-org-id`) accept either fastn's customer id or that external reference. You don't send a `plan` for a customer: a paid plan in this call is refused with `403`.

If your Admin key has **Verify caller identity (HMAC)** set to enforce, this call needs identity headers too. There is no customer yet, so send `x-user-id` and `x-identity-hmac`, leave out `x-org-id`, and sign an empty org id: `hmac("\n" + userId)`. See [Register with an enforcing key](../../embed/embedding/integration-flow.md#register-with-an-enforcing-key).

Already hold a customer's credentials, such as a token for your own product? Create the connection for them with `POST /api/v1/connections`. See [Create a connection for a customer](../../embed/embedding/integration-flow.md#create-a-connection-for-a-customer).

**3 · Get an embed token** (backend, every page load). Name the customer and user in the `x-org-id` and `x-user-id` headers, and sign them with your identity secret in `x-identity-hmac`. The key from part 1 refuses the call without them, and no body is needed. [Generate embed tokens](../../tutorials/developer/generating-embed-tokens.md) is the full reference: every field and error, and the request for a key without identity verification.

```javascript
const hmac = crypto.createHmac("sha256", process.env.FASTN_IDENTITY_SECRET)
  .update(`${orgId}\n${userId}`).digest("hex");   // orgId + "\n" + userId

const res = await fetch("https://api.fastn.dev/api/v1/embed/token", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.FASTN_API_KEY}`,
    "x-org-id": orgId,     // the orgId from part 2, or fastn's customer id
    "x-user-id": userId,
    "x-identity-hmac": hmac,
  },
});
const json = await res.json();
const token = json.data.token;
```

**4 · Add the widget** (frontend, once) on the page where customers manage settings:

```html
<iframe
  src="https://api.fastn.dev/api/v1/embed/iframe?token=<token>"
  style="width:100%;height:600px;border:none"
  allow="clipboard-write">
</iframe>
```

**5 · Send your product's events (optional).** For an integration that starts when something happens in your product, call its webhook trigger on each event. Copy the URL from the trigger's row menu (**Copy URL**) and send the same identity headers as part 3, with the event as the JSON body. The API key goes in `x-api-key`, as below, or as `Authorization: Bearer`:

```bash
curl --location 'https://webhooks.fastn.dev/prod/triggers/<WORKSPACE_ID>/webhooks/<WEBHOOK_ID>' \
--header 'Content-Type: application/json' \
--header 'x-api-key: <YOUR_API_KEY>' \
--header 'x-org-id: <ORG_ID>' \
--header 'x-user-id: <USER_ID>' \
--header 'x-identity-hmac: <IDENTITY_HASH>' \
--data '{
}'
```

See [Call a webhook trigger](../../operate/triggers/using-a-webhook-trigger.md). Before going live, set **Allowed Origins** in the widget builder to your product's domains.

### In the onboarding

Setup step 3, **Set up the widget**, is yours. Make the widget match your product with **Customize it in** your AI tool, or **Or change it in the widget builder**. Then, under **Who adds it to** your product, choose **I'll add it**, **My developer**, or **My AI tool**. It is done once the widget loads in your product or a customer connects through it, and earns 5 AI credits.

The going-live item **Add the widget to** your product is your developer's. It has **Preview the widget**, **Open the widget builder**, and **Send to your developer**, which copies a link to the page, then parts 1 to 4 above with their code. The API key it creates is a live, full-access key with identity verification required, not the **Embed backend** preset described in part 1. It shows "Widget found" once the widget loads on your domain, and earns no AI credits.

### Related docs

[How embedding works](../../tutorials/developer/how-embedding-works.md) · [API keys](../../manage/api-keys.md) · [Customers and isolation](../../tutorials/developer/understanding-tenancy.md) · [Widget builder](../../embed/widget-builder/README.md) · [Webhook triggers](../../build/triggers/webhooks.md)
