# Embed token server (Python)

A Flask route, `GET /api/fastn-token`, that mints a Fastn embed token for the signed-in customer and user. Point your frontend's iframe at it, as in the [embed-node](../embed-node) example's `public/index.html`.

## Before you start

* An API key from **Embed → API keys** in the [Fastn dashboard](https://app.fastn.dev). Use **Test** mode while you try it.
* A test customer from **Operate → Customers → Create customer**.
* Python 3.10 or newer.

## Run it

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
export FASTN_API_KEY=fsk_test_replace_me
export DEMO_CUSTOMER_ID=demo-customer
python app.py
```

Then:

```bash
curl http://localhost:3000/api/fastn-token
```

**You should see:** `{"token": "..."}`.

## Identity verification

If your key has **Verify caller identity (HMAC)** set to **Monitor only** or **Enforce**, also set `FASTN_IDENTITY_SECRET`. The server then sends `x-user-id` and `x-identity-hmac`, the HMAC-SHA256 of `customer_id + "\n" + user_id`. See [Authentication](https://docs.fastn.ai/get-started/authentication-and-api-keys).
