---
---

# Embedding Quickstart

This walks through the shortest path to a working embed: generate a token from your backend, render the iframe, and see a connection. It assumes you have a published widget and an API key.

### Before you start

You'll need:

* **An API key** - From **Embed → API keys and MCP**. Use a `fsk_test_` key while developing. See [Authentication & API Keys](authentication-and-api-keys.md).
* **The customer identifier (`endOrgId`)** - fastn's id for the customer the widget is for, or the external reference you registered that customer under (`orgId` on `POST /api/v1/orgs`). See [Finding Your Org Identifier](finding-your-org-identifier.md).
* **A backend** - Any server environment where you can make an HTTP request with a secret API key.

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
    },
    body: JSON.stringify({
      endOrgId: customerId, // fastn id or your external reference
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

Create an endpoint your frontend can call to get a fresh token. Return only the token, never the API key.

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

Load the page. The fastn widget should render inside your application. You should see the integrations you added to the widget, each with a Connect button.

Click Connect on one, complete the authentication popup, and confirm the app shows as Connected.

### If the iframe is blank

The most common cause is an expired or hardcoded token. Confirm your frontend fetches a fresh token on each load rather than reusing one. See [Troubleshooting](troubleshooting.md).
