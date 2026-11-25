// A minimal backend for the fastn widget.
// GET /api/fastn-token mints an embed token for the signed-in customer and user.
// The API key and identity secret stay on the server: only the token reaches the browser.

const crypto = require("crypto");
const path = require("path");
const express = require("express");

const {
  FASTN_API_KEY,               // fsk_test_... or fsk_live_...
  FASTN_IDENTITY_SECRET = "",  // only needed if the key verifies caller identity (HMAC)
  FASTN_API_URL = "https://api.fastn.dev",
  PORT = 3000,
} = process.env;

if (!FASTN_API_KEY) {
  console.error("Set FASTN_API_KEY first. See .env.example.");
  process.exit(1);
}

const app = express();
app.use(express.static(path.join(__dirname, "public")));

// Replace this with however your app knows who is signed in.
function currentUser(req) {
  return {
    customerId: process.env.DEMO_CUSTOMER_ID || "demo-customer", // your id for the customer (x-org-id)
    userId: process.env.DEMO_USER_ID || "demo-user",
  };
}

async function getFastnToken({ customerId, userId }) {
  const headers = {
    Authorization: `Bearer ${FASTN_API_KEY}`,
    "Content-Type": "application/json",
    "x-org-id": customerId,
  };
  if (FASTN_API_KEY.startsWith("fsk_test_")) headers["X-fastn-Test-Mode"] = "true";
  if (FASTN_IDENTITY_SECRET) {
    headers["x-user-id"] = userId;
    headers["x-identity-hmac"] = crypto
      .createHmac("sha256", FASTN_IDENTITY_SECRET)
      .update(`${customerId}\n${userId}`)
      .digest("hex");
  }

  const res = await fetch(`${FASTN_API_URL}/api/v1/embed/token`, {
    method: "POST",
    headers,
    body: JSON.stringify({ userId }),
  });
  const json = await res.json();
  if (!res.ok) throw new Error(`fastn answered ${res.status}: ${JSON.stringify(json)}`);
  return json.data.token; // the token is nested under data
}

app.get("/api/fastn-token", async (req, res) => {
  try {
    res.json({ token: await getFastnToken(currentUser(req)) });
  } catch (err) {
    console.error(err);
    res.status(502).json({ error: "Could not get a fastn token" });
  }
});

app.listen(PORT, () => console.log(`Open http://localhost:${PORT}`));
