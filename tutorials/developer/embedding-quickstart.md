---
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

# Embedding Quickstart

In this quickstart you mint an embed token from your backend, render the widget in your page, and connect an app as a customer would. It takes about ten minutes, and you can do all of it from a fresh account.

<figure><img src="../../.gitbook/assets/diagrams/auth-flow.svg" alt="How authentication works: your backend mints an embed token from fastn with your API key, passes only the token to your frontend, which opens the widget; the customer signs in to their app and fastn saves the credential."><figcaption><p>Your API key stays on your backend. Only the short-lived token reaches the browser.</p></figcaption></figure>

The finished code is in the runnable [embed-node](https://github.com/fastn-ai/docs/tree/main/examples/embed-node) example, with a Python backend in [token-server-python](https://github.com/fastn-ai/docs/tree/main/examples/token-server-python).

### Before you start

Set up three things in the dashboard. Each takes a minute.

1. **An API key.** In **Embed → API keys**, click **Create key** and choose **Test** mode. Copy the key: it is shown once. This quickstart uses a key without identity verification. A key with **Verify caller identity (HMAC)** set to Enforce also needs a signed `x-identity-hmac` header: see [Generating Embed Tokens](generating-embed-tokens.md).
2. **A test customer.** In **Operate → Customers**, click **Create customer**, and note its id or the External ID you gave it. See [Managing customers](../saas-admin/managing-customers.md).
3. **A widget with one integration.** In **Embed → Widget**, click **Add** under INTEGRATIONS and pick any integration. See [Build your widget](../saas-admin/building-your-widget.md).

You also need a backend: any server where you can make an HTTP request with a secret API key.

### Step 0: Check the token with curl

Before writing code, mint a token from your terminal. Replace the key and the customer id:

```bash
curl -X POST https://api.fastn.dev/api/v1/embed/token \
  -H "Authorization: Bearer fsk_test_<your-key>" \
  -H "X-fastn-Test-Mode: true" \
  -H "x-org-id: <your-customer-id>" \
  -H "Content-Type: application/json" \
  -d '{"userId": "test-user"}'
```

**You should see:** a JSON response with the token at `data.token`. A `403` with *Test API keys require X-fastn-Test-Mode: true header* means the test-mode header is missing.

### Step 1: Generate a token from your backend

Create a server-side function that calls the fastn token endpoint. Keep the API key in an environment variable - never in client code.

```javascript
// Server-side only
async function getFastnToken({ customerId, userId, userEmail, userName }) {
  const res = await fetch("https://api.fastn.dev/api/v1/embed/token", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.FASTN_API_KEY}`,
      "Content-Type": "application/json",
      // Required only for fsk_test_ keys:
      "X-fastn-Test-Mode": "true",
      "x-org-id": customerId, // fastn id or your external reference
    },
    body: JSON.stringify({
      userId,               // the signed-in person; keys per-user isolation
      userEmail,
      userName,
    }),
  });

  const json = await res.json();
  // The token is nested under `data`
  return json.data.token;
}
```

> Note: the response nests the token under `data` - read `json.data.token`, not `json.token`.

### Step 2: Expose the token to your frontend

Create an endpoint your frontend can call to get a fresh token. Return only the token, as `{ "token": "emb_..." }`, never the API key.

```javascript
// Example route
app.get("/api/fastn-token", async (req, res) => {
  const token = await getFastnToken({
    customerId: req.user.companyId, // however your app knows the customer
    userId: req.user.id,
    userEmail: req.user.email,
    userName: req.user.name,
  });
  res.json({ token });
});
```

### Step 3: Render the iframe

On your frontend, fetch a token and render the fastn iframe with it.

```javascript
const { token } = await fetch("/api/fastn-token").then(r => r.json());

const iframe = document.createElement("iframe");
// The token carries the customer and user, so the URL needs nothing else
iframe.src = `https://api.fastn.dev/api/v1/embed/iframe?token=${token}`;
iframe.style.width = "100%";
iframe.style.height = "100%";
iframe.style.border = "none";
document.getElementById("integrations").appendChild(iframe);
```

### Step 4: Verify

**You should see:** the fastn widget inside your page, listing the integration you added with a **Connect** button.

Click Connect on one, complete the authentication popup, and confirm the app shows as Connected.

### If the iframe is blank

The most common cause is an expired or hardcoded token. Confirm your frontend fetches a fresh token on each load rather than reusing one. See [Troubleshooting](troubleshooting.md).
