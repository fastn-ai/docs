// Send an event from your product to a fastn webhook trigger, signed for one customer.
// fastn then runs the trigger's workflows with that customer's setup.

import crypto from "node:crypto";

const {
  FASTN_API_KEY,
  FASTN_IDENTITY_SECRET,
  FASTN_WEBHOOK_URL, // from the trigger's row menu: Copy URL
  CUSTOMER_ID,       // your id for the customer
  USER_ID = "demo-user",
} = process.env;

for (const [name, value] of Object.entries({ FASTN_API_KEY, FASTN_IDENTITY_SECRET, FASTN_WEBHOOK_URL, CUSTOMER_ID })) {
  if (!value) {
    console.error(`Set ${name} first.`);
    process.exit(1);
  }
}

const order = { orderId: "ORD-1001", total: 120.5, currency: "USD", email: "jane@example.com" };

const hmac = crypto
  .createHmac("sha256", FASTN_IDENTITY_SECRET)
  .update(`${CUSTOMER_ID}\n${USER_ID}`)
  .digest("hex");

const res = await fetch(FASTN_WEBHOOK_URL, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": FASTN_API_KEY,
    "x-org-id": CUSTOMER_ID,
    "x-user-id": USER_ID,
    "x-identity-hmac": hmac,
  },
  body: JSON.stringify(order), // arrives in the workflow as ctx.input
});

console.log("fastn answered", res.status, await res.text());
