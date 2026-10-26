---
description: >-
  Serve many customer organisations and end users from one agent with a
  multi-tenant access key and the X-Org-Id and X-User-Id headers.
---

# Multi-tenant agents

**What this page answers**

* How does one key serve all my customers?
* Which headers do I send, and when?
* How are two customers kept apart?
* How do I stop a caller from claiming to be another customer or user?

### When you need it

You are building a product or agent that serves *your* customers, and each customer (and each of their users) has their own accounts in the apps the agent uses. Rather than one key per customer, create **one** key with **Tenancy** set to **Multi-tenant**, and name the customer and user on each call.

### The words

| Term | Meaning | How it is named |
| --- | --- | --- |
| **Organisation** | You, the Fastn Connect customer. | The gateway URL |
| **Workspace** | A division of your organisation (optional). | The URL path: `/<your-org>/<workspace>` |
| **End-org** | One of *your* customers. | `X-Org-Id` header |
| **End-user** | A person inside that customer. | `X-User-Id` header |

### Send the headers

```http
POST https://mcp.fastn.dev/<your-org>
Authorization: Bearer ucl_<multi-tenant-key>
X-Org-Id: acme
X-User-Id: alice@acme.com
```

Create **one MCP client per end user** and bind the headers when the client connects:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

const transport = new StreamableHTTPClientTransport(new URL("https://mcp.fastn.dev/<your-org>"), {
  requestInit: {
    headers: {
      Authorization: "Bearer ucl_<multi-tenant-key>",
      "X-Org-Id": customerId, // which of your customers
      "X-User-Id": userId,    // which of their users
    },
  },
});
const client = new Client({ name: "my-agent", version: "1.0.0" });
await client.connect(transport);
```

### Which account each call uses

The connector's [sign-in mode](../tools/sign-in-modes.md) decides:

| Connector mode | The call runs with |
| --- | --- |
| **One shared account** | Your organisation's one shared account, for every customer. |
| **Each customer org** | The account that customer (`X-Org-Id`) connected. |
| **Each person signs in** | The account that user (`X-User-Id`) connected. If they have not connected, the tool returns a connect link for the agent to pass on. |
| **The caller brings a token** | The token your agent sends. |

Customers are namespaced under your organisation, so your customer `acme` never shares credentials with another Fastn Connect customer's `acme`. Each call only resolves connectors, policies and accounts inside the `X-Org-Id` you sent.

If one user or customer has more than one account for the same app, send `X-Connection-Id` to pick one.

### Org rules

Set these on the create form. Afterwards, **More actions** → **Edit org rules** changes **Allowed orgs** and **Require an end user**; **Allow new orgs** can only be set when the key is created.

* **Allow new orgs** (on by default). The first time the agent names an `X-Org-Id` Fastn Connect has not seen, it creates that customer automatically. Turn it off to reject unknown orgs.
* **Allowed orgs**. A list such as `acme, globex`. Empty means any.
* **Require an end user**. Every call must name an `X-User-Id`.

### Verify caller identity (HMAC)

Headers are just strings. If the code that sets them can be influenced by a user, that user could name another customer. Identity verification closes this:

1. Turn on **Verify caller identity (HMAC)** when creating the key and pick **Enforce** or **Monitor only**. (**Enable verification** on the key-created screen turns it on in **Enforce** mode straight away.)
2. Copy the **identity-verification secret** (*shown once*) and keep it on your backend only.
3. On every call, sign the org and user and send the result as `X-Identity-Hmac`:

```javascript
const crypto = require("crypto");
const IDV_SECRET = process.env.FASTN_IDV_SECRET; // never ship to clients

function identityHash(orgId = "", userId = "") {
  return crypto.createHmac("sha256", IDV_SECRET)
    .update(`${orgId}\n${userId}`)
    .digest("hex");
}
// headers: X-Org-Id, X-User-Id, and X-Identity-Hmac: identityHash(orgId, userId)
```

The message is `<org id>` + newline + `<user id>`; either may be empty. The key creation screen shows the same code in Node, Python and Go.

To roll out safely, create the key with **Monitor only** (*Log mismatches, don't block*), check Monitor for mismatches, then use **More actions** → **Enforce verification** (*Reject a bad or missing hash*). With enforcement on, a bad or missing hash is answered `401`. Use **Rotate secret** to replace the secret.
