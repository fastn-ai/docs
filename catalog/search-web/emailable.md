---
description: "Emailable verifies email addresses. Verify single emails, run batch verifications and check account details."
hidden: true
---

# Emailable

<img src="../../.gitbook/assets/connectors/lg/emailable.png" alt="Emailable logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [emailable.com](https://emailable.com) |
| **Authentication** | API key, OAuth 2.0 |
| **Slug** | `emailable` |

## Setup

Your customers sign in to Emailable through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Emailable from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.emailable.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Batch Verification</td><td><code>createBatchVerification</code></td><td>Submit a list of up to 50,000 email addresses for bulk verification and receive the batch id used to poll the results. Verification runs asynchronously; poll Get Batch Status with the returned id, or supply a callback URL to have the completed results POSTed to you. Each address in the batch consumes one account credit, so check Get Account Info first. Batches cannot be cancelled or deleted through the API.</td></tr><tr><td>Create OAuth Device Code</td><td><code>createOauthDeviceCode</code></td><td>Start Emailable's OAuth 2 Device Authorization Grant (RFC 8628) for an input-constrained client such as a CLI or CI job. Returns a device_code to poll Exchange OAuth Token with, and a short user_code plus verification URL to show the user. The OAuth App must have the device authorization grant enabled in its settings, otherwise the call fails with invalid_client. Does not consume verification credits.</td></tr><tr><td>Exchange OAuth Token</td><td><code>exchangeOauthToken</code></td><td>Exchange an Emailable OAuth 2 authorization grant for an access token and refresh token, or refresh an existing access token. One endpoint serves three grant types: 'authorization_code' (send code, client_id, client_secret, redirect_uri and, if PKCE was used, code_verifier), 'urn:ietf:params:oauth:grant-type:device_code' (send device_code and client_id only - no client secret), and 'refresh_token' (send refresh_token, client_id and client_secret). Authorization codes are single-use and expire after 10 minutes. Does not consume verification credits.</td></tr><tr><td>Get Account Info</td><td><code>getAccountInfo</code></td><td>Retrieve general information about the authenticated Emailable account, including the account owner's email address and the number of verification credits remaining. Takes no input. Use it to check the credit balance before running verifications, since every single-email verification and every address in a batch consumes one credit.</td></tr><tr><td>Get Account Info (POST)</td><td><code>getAccountInfoPost</code></td><td>Retrieve the authenticated Emailable account's owner email and remaining verification credits using the POST form of the account endpoint. Identical result to Get Account Info; provided for clients that cannot issue a GET with credentials. Prefer Get Account Info unless you specifically need POST.</td></tr><tr><td>Get Batch Status</td><td><code>getBatchStatus</code></td><td>Poll the status and results of a bulk verification batch created with Create Batch Verification. While the batch is still running the response carries a progress message; once complete it carries the per-address results. Batches of up to 1,000 addresses return an 'emails' array (for 30 days, then aggregate counts only); larger batches return a 'download_file' URL to a ZIP-compressed CSV (for 5 days, then aggregate counts only). Reading a batch status does not consume credits.</td></tr><tr><td>Revoke OAuth Token</td><td><code>revokeOauthToken</code></td><td>Revoke an Emailable OAuth 2 access token so it can no longer authenticate API requests. Requires the OAuth App client credentials that the token was issued to. Returns an empty JSON object on success. Does not consume verification credits.</td></tr><tr><td>Verify Email</td><td><code>verifyEmail</code></td><td>Verify a single email address in real time and return its deliverability state, reason, quality score, mail-server details and inferred name/gender data. Uses the query-string form of Every verification of a real, resolvable domain consumes one account credit. If the response is HTTP 249 the verification is still running - resend the identical request for up to five minutes and it will not be charged again.</td></tr><tr><td>Verify Email (JSON Body)</td><td><code>verifyEmailJson</code></td><td>Verify a single email address using the JSON-body form of the Emailable verify endpoint Functionally identical to Verify Email, but every parameter except the address itself is genuinely optional, so Emailable's own defaults apply to anything you leave out. Returns the same deliverability result. Every verification of a real, resolvable domain consumes one account credit.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Batch Verification Completed</td><td><code>Batch verification completed.</code></td><td>Fires when an Emailable bulk verification batch finishes. Emailable has NO webhook registration, list or delete API: the callback is registered per batch by passing the Callback URL below as the 'url' field on Create Batch Verification. Copy the webhook URL from this trigger and pass it as 'url' every time you create a batch you want notified about. The payload is identical to the Get Batch Status response. Emailable expects HTTP 200; any other status makes it redeliver hourly for up to 3 days after the batch finishes verifying, after which delivery stops permanently. To stop receiving events, simply stop passing the URL on new batches - there is nothing to unregister.</td></tr></tbody></table>
