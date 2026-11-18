---
description: "FraudLabs Pro fraud prevention API (v2)."
hidden: true
---

# FraudLabs Pro

FraudLabs Pro fraud prevention API (v2). Screens e-commerce orders and user registrations for chargeback and fraud risk using IP geolocation, proxy detection, email/phone/username reputation, BIN and address checks; submits order, user and payment feedback to tune the scoring model; and runs SMS OTP verification. Auth is a FraudLabs Pro API license key.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [fraudlabspro.com](https://fraudlabspro.com) |
| **Authentication** | API key |
| **Actions** | 11 |
| **Events** | 2 |
| **Slug** | `fraudLabsPro` |

## Use it

Add FraudLabs Pro from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fraudLabsPro.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check API Service Status | `getServiceStatus` | Health check for the FraudLabs Pro API host. Returns the bare plain-text body OK (not JSON) when the service is up. This endpoint is undocumented but live (a nonsense-suffix control on the same prefix returns the host's 404 NOT FOUND envelope, proving it is a real exact route) and it requires no API key, so no credential is sent and none appears in the execution record. Use it to distinguish a FraudLabs Pro outage from a credential or quota problem before retrying a failed screening. NOTE ON THE OUTPUT CONTRACT: the response is a top-level string, which a fastn outputContract cannot express (only type object is accepted), so the contract below is an empty permissive object; read the raw response value, not a field. |
| Get Order Screening Result | `getOrderResult` | Retrieves the stored screening result of an order that was previously submitted to Screen Order for Fraud, without consuming a screening credit. Accepts either the fraudlabspro_id or your own merchant order id. Returns the score, status, triggered rules and the full IP geolocation, address, email, phone, username, credit-card and device breakdown. An unknown id returns 404 error_code 10011 TRANSACTION NOT FOUND. SECURITY: FraudLabs Pro has no header auth form, so this GET carries the API key in the query string and it will appear in the execution record's requestUrl. |
| Get Plan and Quota Usage | `getPlanResult` | Returns the FraudLabs Pro subscription plan attached to the API key and its current usage: the plan name, the monthly screening query limit and how much of it has been consumed, the custom-rule limit and usage, the next renewal date, and the remaining SMS verification balance. Call it before a batch of screenings to check the credit budget, since Screen Order for Fraud consumes one query per call. This endpoint is undocumented but live and stable (verified against the vendor host, with a nonsense-suffix control proving it is an exact route and not prefix matching). SECURITY: the response includes an adv_agent_tok field which, on accounts that use the Advanced Agent, carries an account token - treat the response as sensitive. FraudLabs Pro has no header auth form, so this GET carries the API key in the query string and it will appear in the execution record's requestUrl. |
| Get User Screening Result | `getUserResult` | Retrieves the stored result of a user registration screening by its user_transaction_id, returning the user score, status, triggered rules and the IP geolocation, email, phone and device breakdown. An unknown id returns 404 error_code 10011 TRANSACTION NOT FOUND. Requires a FraudLabs Pro Medium plan or above. SECURITY: FraudLabs Pro has no header auth form, so this GET carries the API key in the query string and it will appear in the execution record's requestUrl. |
| Screen Order for Fraud | `screenOrder` | Submits an e-commerce order to FraudLabs Pro for real-time fraud screening and returns a risk score (0-100), a status of APPROVE / REVIEW / REJECT, the triggered rule list and the full validation breakdown (IP geolocation and proxy detection, billing/shipping address comparison, email, phone, username, credit-card BIN and device checks). Each call consumes one FraudLabs Pro screening credit; the remaining balance is returned in remaining_credits. Record the returned fraudlabspro_id to fetch the result later or to submit feedback. |
| Screen User Registration | `screenUser` | Screens a user sign-up or login for fraud and bot risk using the account's email address and IP, returning a user_score, a user_transaction_id, a user_transaction_status and the list of reasons that fired. Use it at registration time to block disposable emails, proxies and known-bad actors before an order is ever placed. Requires a FraudLabs Pro Medium plan or above; lower plans receive 401 error_code 10061 UNSUPPORTED PLAN. |
| Send SMS Verification OTP | `sendSmsVerification` | Sends a one-time password by SMS to a mobile number for step-up verification and returns a tran_id to check the OTP against, plus the remaining SMS credit balance. The message template must contain the literal placeholder &lt;otp&gt; and is capped at 140 characters. WARNING: with a real phone number this sends a real text message and consumes SMS credits, and FraudLabs Pro imposes a 24-hour cooldown after 10 failed deliveries in a day. Pass tel=+11 to use the vendor's documented sandbox number, which simulates a successful send, deducts no credit and accepts OTP 123456. |
| Submit Order Feedback | `feedbackOrder` | Reports the merchant's final decision on a previously screened order back to FraudLabs Pro, moving it out of manual review and training the scoring model. Use APPROVE to accept the order, REJECT to decline it, or REJECT_BLACKLIST to decline it and add the order's IP, email, phone, card and device to your blacklist. Returns the fraudlabspro_id that was updated. Re-submitting the same decision returns error_code 10012 TRANSACTION IS ALREADY APPROVED/REJECTED. |
| Submit Payment Status Feedback | `feedbackPayment` | Reports the final payment-gateway outcome for a transaction back to FraudLabs Pro, so declined-card and chargeback signals feed the risk model. Send the buyer's email, the gateway status (e.g. declined) and the gateway's own message, optionally tied to a fraudlabspro_id. Requires a FraudLabs Pro plan that includes the Payment Feedback API; other plans receive 401 error_code 10061 UNSUPPORTED PLAN. |
| Submit User Screening Feedback | `feedbackUser` | Reports the merchant's final decision on a screened user registration back to FraudLabs Pro so the model learns from it. Use APPROVE to accept the account, REJECT to decline it, or REJECT_BLACKLIST to decline it and blacklist the user's identifying data. Returns the user_transaction_id that was updated. Requires a FraudLabs Pro Medium plan or above. |
| Verify SMS OTP Code | `getSmsVerificationResult` | Checks the one-time password a user entered against the SMS send identified by tran_id. Returns result 'Y' when the OTP is valid and unexpired. A wrong or expired code returns 400 error_code 10034 INVALID OTP. SECURITY: FraudLabs Pro has no header auth form, so this GET carries the API key in the query string and it will appear in the execution record's requestUrl. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Order Status Changed to Approve | `APPROVE` | FraudLabs Pro POSTs this when a screened order moves to APPROVE (from REVIEW or from REJECT). REGISTRATION IS UI-ONLY - FraudLabs Pro publishes no webhook registration API. Click-path: sign in at https://www.fraudlabspro.com/merchant/sign-in, open the Merchant Area settings page, paste the fastn trigger URL into the order status change callback URL field and save. The vendor sends no signature header, so treat the payload as unauthenticated and re-read the order with Get Order Screening Result before acting on it. Payload schema is MODELLED from https://www.fraudlabspro.com/developer/webhook/order-status-changed - no live delivery was captured, because a delivery requires the portal callback URL to be registered by hand. |
| Order Status Changed to Reject | `REJECT` | FraudLabs Pro POSTs this when a screened order moves to REJECT (from REVIEW or from APPROVE). REGISTRATION IS UI-ONLY - FraudLabs Pro publishes no webhook registration API. Click-path: sign in at https://www.fraudlabspro.com/merchant/sign-in, open the Merchant Area settings page, paste the fastn trigger URL into the order status change callback URL field and save. The vendor sends no signature header, so treat the payload as unauthenticated and re-read the order with Get Order Screening Result before acting on it. Payload schema is MODELLED from https://www.fraudlabspro.com/developer/webhook/order-status-changed - no live delivery was captured, because a delivery requires the portal callback URL to be registered by hand. |
