---
hidden: true
---

# Finding Your Org Identifier

The `endOrgId` identifies the customer a widget embed is for. Both the token endpoint and the iframe URL require it. Getting the right identifier is necessary for anything to work.

### Your id, or fastn's

`endOrgId` takes either of a customer's two identifiers:

* **The id you registered them under**: the `orgId` you sent to `POST /api/v1/orgs`, shown as **External ID** on the customer in the dashboard. Register each customer under your own id for them and you never need to look one up.
* **fastn's own id**: a UUID, returned as `id` when you register the customer, and as `endOrgId` in every token response.

The token request looks the value up among your own customers only, so another account using the same id never reaches yours. The `x-org-id` header takes the same values.

### Where to find it

You create customers under **Settings → Customers** (see [Managing Customers](../saas-admin/managing-customers.md)), or from your backend with `POST /api/v1/orgs`. Open a customer in the dashboard: its details show the **External ID** it was registered under.

### Using it

Pass it as `endOrgId` in:

* The token request body (`{ endOrgId, userId, userEmail, userName }`), or as the `x-org-id` header with a key that verifies caller identity. See [Generating Embed Tokens](generating-embed-tokens.md).
* The iframe URL for user-level embeds (`?tenant-id=<endOrgId>&token=<token>`)

Store it in an environment variable rather than hardcoding it, so it can change per environment (test customer vs production customer).

```
FASTN_END_ORG_ID=<customer id>
```
