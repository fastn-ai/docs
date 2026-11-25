// Find or create a contact in whichever CRM a customer connected, then add a note to it.
// The same code works for HubSpot, Salesforce and the other CRMs in fastn's unified API.

import { FastnClient } from "@fastn-ai/sdk";

const { FASTN_API_KEY, CUSTOMER_ID, CONTACT_EMAIL = "jane@example.com" } = process.env;
if (!FASTN_API_KEY || !CUSTOMER_ID) {
  console.error("Set FASTN_API_KEY and CUSTOMER_ID first.");
  process.exit(1);
}

const fastn = new FastnClient({ apiKey: FASTN_API_KEY });
const customer = fastn.customer(CUSTOMER_ID); // your id for the customer

const { records } = await customer.crm.contacts.find({ email: CONTACT_EMAIL });

const contact =
  records[0] ??
  (await customer.crm.contacts.create({ first_name: "Jane", last_name: "Doe", email: CONTACT_EMAIL }));

console.log("Contact:", contact.id, contact.provider);

await customer.crm.notes.add({
  body: "Added by the fastn crm-contacts example",
  parent_id: contact.id,
  parent_type: "contact",
});

console.log("Note added.");
