---
description: "Which customer identifier the token request takes in x-org-id, and where to find it."
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

# Find your org identifier

The customer identifier names the customer a widget embed is for, in the `x-org-id` header of the token request. Only the token request needs it: the iframe URL takes the token alone, because the token already carries the customer. The token request fails without the right identifier.

### Two identifiers work

`x-org-id` accepts either:

* **Fastn's id for the customer**, or
* **your external reference**: the id you gave the customer when you registered it (`orgId` on `POST /api/v1/orgs`). Using your own id means you never have to store Fastn's. If you created a customer without one, Fastn stored its slug as the external reference at creation time.

### Where Fastn's id comes from

Each customer in your Fastn workspace has an internal id. You create customers under **Operate → Customers** (see [Manage customers](../saas-admin/managing-customers.md)).

To find it, open **Operate → Customers** in the dashboard and click the customer. The address bar changes to `app.fastn.dev/customers/<id>`: the last part of that URL is the customer's id. Copy it from there.

{% hint style="info" %}
Create a separate test customer for development and use its id locally, so test connections never land on a real customer.
{% endhint %}

### Using it

Once you have the identifier, send it as the `x-org-id` header on the token request, or as `orgId` in the body. A key limited to a single customer is the one exception: it takes only Fastn's id, in `orgId`. See [Generate embed tokens](generating-embed-tokens.md).

In production, look the identifier up per request from the signed-in person's company rather than fixing one value, so each customer gets their own token. For local testing against a single test customer, an environment variable is fine:

```
FASTN_ORG_ID=<test-customer-id>
```
