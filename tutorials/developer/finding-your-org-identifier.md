# Finding Your Org Identifier

The `endOrgId` identifies the customer a widget embed is for. Both the token endpoint and the iframe URL require it. Getting the right identifier is necessary for anything to work.

### It must be the customer UUID

`endOrgId` must be the customer's internal UUID. The customer **slug** (e.g., `katana-customer`) does not work in its place.

### Where the UUID comes from

Each customer in your Fastn workspace has an internal UUID. You create customers under **Settings → Customers** (see [Managing Customers](https://claude.ai/fastn/tutorials/saas-admin/managing-customers)).

The customer record in the dashboard shows: Name, Slug, Status, Customer Admin, and Created date. It does **not** display the UUID — there is no UUID or External ID field in the Customers UI.

To retrieve the UUID today, open the customer in the dashboard and read it from the page state using your browser's developer tools.

> **VERIFY:** This is a confirmed gap — the customer UUID is not exposed anywhere in the Customers UI (validated on the live platform). The Embed tab refers to this value as `YOUR_CUSTOMER_ID` / `customer_id`. Confirm the recommended retrieval method, and update this page if the UUID becomes available directly in the UI or via an API endpoint.

### Using it

Once you have the UUID, pass it as `endOrgId` in:

* The token request body (`{ endOrgId, userEmail, userName }`)
* The iframe URL for user-level embeds (`?tenant-id=<endOrgId>&token=<token>`)

Store it in an environment variable rather than hardcoding it, so it can change per environment (test customer vs production customer).

```
FASTN_END_ORG_ID=<customer-uuid>
```
