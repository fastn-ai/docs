# Read and write a customer's CRM contacts (Node.js)

Finds a contact by email in whichever CRM a customer connected, creates it if it is not there, then adds a note to it. It uses the fastn SDK's typed CRM methods, so the same code works for HubSpot, Salesforce and other CRMs.

## Before you start

* An API key from **Embed → API keys** in the [fastn dashboard](https://app.fastn.dev), one that can act for more than one customer.
* A customer that has connected a CRM, in the widget or with a connection you created for them.
* Node.js 20 or newer.

## Run it

```bash
npm install
FASTN_API_KEY=fsk_live_replace_me CUSTOMER_ID=acme_customer_42 npm start
```

**You should see:** `Contact: <id> <provider>` and `Note added.`, and the contact and note in the customer's CRM.

If the customer connected more than one CRM, pass `{ provider: "hubspot" }` as the last argument to calls on a single record. See [Read and write a customer's CRM records](https://docs.fastn.ai/how-to-guides/how-to/crm-records).
