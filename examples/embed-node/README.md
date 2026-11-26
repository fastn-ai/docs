# Embed the Fastn widget (Node.js)

A web page that shows the Fastn widget, and the Express route that mints its embed token. Your API key stays on the server; only the short-lived token reaches the browser.

## Before you start

In the [Fastn dashboard](https://app.fastn.dev):

1. **An API key:** **Embed → API keys → Create key**, in **Test** mode.
2. **A test customer:** **Operate → Customers → Create customer**. Note the id you give it.
3. **A widget with one integration:** **Embed → Widget**, then **Add** under INTEGRATIONS.

You also need Node.js 20.6 or newer.

## Run it

```bash
cp .env.example .env    # then fill in FASTN_API_KEY and DEMO_CUSTOMER_ID
npm install
npm start
```

Open http://localhost:3000.

**You should see:** the widget listing the integration you added, with a **Connect** button.

## How it works

* `server.js` calls `POST /api/v1/embed/token` with your API key and the customer in `x-org-id`, and returns only `data.token`.
* `public/index.html` fetches a fresh token on every load and opens `https://api.fastn.dev/api/v1/embed/iframe?token=...`.
* If your key verifies caller identity, set `FASTN_IDENTITY_SECRET` and the server signs `x-org-id` and `x-user-id` as `x-identity-hmac`.

Before going live, replace `currentUser()` with your own session lookup, and set **Allowed Origins** in the widget builder to your domains. See the [embedding quickstart](https://docs.fastn.ai/embed/embedding/embedding-quickstart).
