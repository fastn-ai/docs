# Embedding Quickstart

This walks through the shortest path to a working embed: generate a token from your backend, render the iframe, and see a connection. It assumes you have a published widget and an API key.

### Before you start

You'll need:

* **An API key** — From Settings → API Keys. Use a `fsk_test_` key while developing. See [Authentication & API Keys](https://claude.ai/fastn/tutorials/developer/authentication-and-api-keys).
* **Your org identifier (`endOrgId`)** — The internal UUID for the customer the widget is for. See [Finding Your Org Identifier](https://claude.ai/fastn/tutorials/developer/finding-your-org-identifier).
* **A backend** — Any server environment where you can make an HTTP request with a secret API key.

### Step 1: Generate a token from your backend

Create a server-side function that calls the Fastn token endpoint. Keep the API key in an environment variable — never in client code.

```javascript
// Server-side only
async function getFastnToken({ userEmail, userName }) {
  const res = await fetch("https://live.gcp.fastn.ai/api/v1/embed/token", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.FASTN_API_KEY}`,
      "Content-Type": "application/json",
      // Required only for fsk_test_ keys:
      "X-fastn-Test-Mode": "true",
    },
    body: JSON.stringify({
      endOrgId: process.env.FASTN_END_ORG_ID,
      userEmail,
      userName,
    }),
  });

  const json = await res.json();
  // The token is nested under `data`
  return json.data.token;
}
```

> Note: the response nests the token under `data` — read `json.data.token`, not `json.token`.

### Step 2: Expose the token to your frontend

Create an endpoint your frontend can call to get a fresh token. Return only the token, never the API key.

```javascript
// Example route
app.get("/api/fastn-token", async (req, res) => {
  const token = await getFastnToken({
    userEmail: req.user.email,
    userName: req.user.name,
  });
  res.json({ token });
});
```

### Step 3: Render the iframe

On your frontend, fetch a token and render the Fastn iframe with it.

```javascript
const { token } = await fetch("/api/fastn-token").then(r => r.json());

const iframe = document.createElement("iframe");
// Org-level (shared) embed — see the Tenancy guide for user-level
iframe.src = `https://live.gcp.fastn.ai/api/v1/embed/iframe?token=${token}`;
iframe.style.width = "100%";
iframe.style.height = "100%";
iframe.style.border = "none";
document.getElementById("integrations").appendChild(iframe);
```

### Step 4: Verify

Load the page. The Fastn widget should render inside your application. You should see the integrations you added to the widget, each with a Connect button.

Click Connect on one, complete the authentication popup, and confirm the app shows as Connected.

### If the iframe is blank

The most common cause is an expired or hardcoded token. Confirm your frontend fetches a fresh token on each load rather than reusing one. See [Troubleshooting](https://claude.ai/fastn/tutorials/developer/troubleshooting).
