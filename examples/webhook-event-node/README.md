# Send your product's events to Fastn (Node.js)

Posts an order event to a Fastn webhook trigger, signed for one customer, so the trigger's workflows run with that customer's setup.

## Before you start

* A webhook trigger with **Authentication** set to API key, routed to a published workflow. Copy its URL from the trigger's row menu (**Copy URL**).
* An API key with **Verify caller identity (HMAC)** set to **Monitor only** or **Enforce**, and its identity secret. Without that, `x-org-id` does not name the customer.
* A customer that has connected the apps the workflow uses.
* Node.js 20 or newer.

## Run it

```bash
FASTN_API_KEY=fsk_live_replace_me \
FASTN_IDENTITY_SECRET=replace_me \
FASTN_WEBHOOK_URL='https://webhooks.fastn.dev/prod/triggers/<ORG_ID>/webhooks/<WEBHOOK_ID>' \
CUSTOMER_ID=acme_customer_42 \
node index.mjs
```

**You should see:** `fastn answered` with a success status, then the event in **Operate → Logs → Events** and the run in **Operate → Logs → Executions**.

See [Start an integration from your product's events](https://docs.fastn.ai/how-to-guides/how-to/events-from-your-product).
