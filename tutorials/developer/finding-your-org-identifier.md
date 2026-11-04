---
---

# Finding Your Org Identifier

The customer identifier names the customer a widget embed is for, in the `x-org-id` header of the token request. Only the token request needs it: the iframe URL takes the token alone, because the token already carries the customer. Getting the right identifier is necessary for anything to work.

### Two identifiers work

`x-org-id` accepts either:

* **fastn's id for the customer**, or
* **your external reference**: the id you gave the customer when you registered it (`orgId` on `POST /api/v1/orgs`). Using your own id means you never have to store fastn's. If you created a customer without one, fastn stored its slug as the external reference at creation time.

### Where fastn's id comes from

Each customer in your fastn workspace has an internal id. You create customers under **Operate → Customers** (see [Managing Customers](../saas-admin/managing-customers.md)).

To find it, open **Operate → Customers** in the dashboard and click the customer. The address bar changes to `app.fastn.dev/customers/<id>`: the last part of that URL is the customer's id. Copy it from there.

{% hint style="info" %}
Create a separate test customer for development and use its id locally, so test connections never land on a real customer.
{% endhint %}

### Using it

Once you have the identifier, send it as the `x-org-id` header on the token request. (Only an API key pinned to one customer sends it as `endOrgId` in the body instead, because a pinned key rejects the header.) Nothing else needs it: the iframe URL is just `?token=<token>`.

In production, look the identifier up per request from the signed-in person's company rather than fixing one value, so each customer gets their own token. For local testing against a single test customer, an environment variable is fine:

```
FASTN_END_ORG_ID=<test-customer-id>
```
