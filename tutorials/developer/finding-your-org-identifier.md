---
---

# Finding Your Org Identifier

The `endOrgId` identifies the customer a widget embed is for. Both the token endpoint and the iframe URL require it. Getting the right identifier is necessary for anything to work.

### It must be the customer UUID

`endOrgId` must be the customer's internal UUID. The customer **slug** (e.g., `katana-customer`) does not work in its place.

### Where the UUID comes from

Each customer in your fastn workspace has an internal UUID. You create customers under **Operate → Customers** (see [Managing Customers](../saas-admin/managing-customers.md)).

To find it, open **Operate → Customers** in the dashboard and click the customer. The address bar changes to `app.fastn.dev/customers/<id>`: the last part of that URL is the customer's UUID. Copy it from there.

{% hint style="info" %}
Create a separate test customer for development and use its UUID locally, so test connections never land on a real customer.
{% endhint %}

### Using it

Once you have the UUID, pass it as `endOrgId` in:

* The token request body (`{ endOrgId, userEmail, userName }`)
* The iframe URL for user-level embeds (`?tenant-id=<endOrgId>&token=<token>`)

Store it in an environment variable rather than hardcoding it, so it can change per environment (test customer vs production customer).

```
FASTN_END_ORG_ID=<customer-uuid>
```
