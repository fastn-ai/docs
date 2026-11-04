---
---

# Finding Your Org Identifier

The `endOrgId` identifies the customer a widget embed is for. Only the token request needs it: the iframe URL takes the token alone, because the token already carries the customer. Getting the right identifier is necessary for anything to work.

### Two identifiers work

`endOrgId` (or the `x-org-id` header) accepts either:

* **fastn's id for the customer**, or
* **your external reference**: the id you gave the customer when you registered it (`orgId` on `POST /api/v1/orgs`). Using your own id means you never have to store fastn's. If you created a customer without one, fastn stored its slug as the external reference at creation time.

### Where fastn's id comes from

Each customer in your fastn workspace has an internal id. You create customers under **Operate → Customers** (see [Managing Customers](../saas-admin/managing-customers.md)).

To find it, open **Operate → Customers** in the dashboard and click the customer. The address bar changes to `app.fastn.dev/customers/<id>`: the last part of that URL is the customer's id. Copy it from there.

{% hint style="info" %}
Create a separate test customer for development and use its id locally, so test connections never land on a real customer.
{% endhint %}

### Using it

Once you have the identifier, pass it as `endOrgId` in the token request body (`{ endOrgId, userId, userEmail, userName }`) or as the `x-org-id` header. Nothing else needs it: the iframe URL is just `?token=<token>`.

In production, look the identifier up per request from the signed-in person's company rather than fixing one value, so each customer gets their own token. For local testing against a single test customer, an environment variable is fine:

```
FASTN_END_ORG_ID=<test-customer-id>
```
