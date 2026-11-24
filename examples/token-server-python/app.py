"""A minimal Flask backend that mints a fastn embed token for one customer and user.

The API key and identity secret stay on the server. The browser only ever gets the token.
"""
import hashlib
import hmac
import os

import requests
from flask import Flask, jsonify

FASTN_API_KEY = os.environ["FASTN_API_KEY"]  # fsk_test_... or fsk_live_...
FASTN_IDENTITY_SECRET = os.environ.get("FASTN_IDENTITY_SECRET", "")
FASTN_API_URL = os.environ.get("FASTN_API_URL", "https://api.fastn.dev")

app = Flask(__name__)


def current_user():
    """Replace this with however your app knows who is signed in."""
    return {
        "customer_id": os.environ.get("DEMO_CUSTOMER_ID", "demo-customer"),  # your id for the customer
        "user_id": os.environ.get("DEMO_USER_ID", "demo-user"),
    }


def identity_hash(customer_id: str, user_id: str) -> str:
    """HMAC-SHA256 of the customer and user ids, newline-joined, signed with the identity secret."""
    message = f"{customer_id}\n{user_id}".encode()
    return hmac.new(FASTN_IDENTITY_SECRET.encode(), message, hashlib.sha256).hexdigest()


def get_fastn_token(customer_id: str, user_id: str) -> str:
    headers = {
        "Authorization": f"Bearer {FASTN_API_KEY}",
        "Content-Type": "application/json",
        "x-org-id": customer_id,
    }
    if FASTN_API_KEY.startswith("fsk_test_"):
        headers["X-fastn-Test-Mode"] = "true"
    if FASTN_IDENTITY_SECRET:
        headers["x-user-id"] = user_id
        headers["x-identity-hmac"] = identity_hash(customer_id, user_id)

    res = requests.post(
        f"{FASTN_API_URL}/api/v1/embed/token",
        headers=headers,
        json={"userId": user_id},
        timeout=30,
    )
    res.raise_for_status()
    return res.json()["data"]["token"]  # the token is nested under data


@app.get("/api/fastn-token")
def fastn_token():
    user = current_user()
    try:
        return jsonify(token=get_fastn_token(user["customer_id"], user["user_id"]))
    except requests.RequestException as err:
        app.logger.error("fastn token request failed: %s", err)
        return jsonify(error="Could not get a fastn token"), 502


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", "3000")))
