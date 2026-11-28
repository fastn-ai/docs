---
description: "Kickbox verifies email addresses. Verify single emails or batches, get threat scores, check disposable domains and view your balance."
hidden: true
---

# Kickbox

<img src="../../.gitbook/assets/connectors/lg/kickbox.png" alt="Kickbox logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [kickbox.com](https://kickbox.com) |
| **Authentication** | Access token |
| **Slug** | `kickbox` |

## Setup

Your customers enter their access token for Kickbox when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Kickbox from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Kickbox**.
2. Select **Connect** on the Kickbox card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Kickbox's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check Disposable Email Domain</td><td><code>checkDisposableEmail</code></td><td>Free open endpoint (open.kickbox.com, no authentication, no credits) that reports whether an email address is hosted on a known disposable/throwaway domain. GET https://open.kickbox.com/v1/disposable/{email}. Returns {disposable: true|false}.</td></tr><tr><td>Get Balance</td><td><code>getBalance</code></td><td>Returns the number of verification credits remaining on the Kickbox account. No inputs.</td></tr><tr><td>Get Batch Verification Status</td><td><code>getBatchVerificationStatus</code></td><td>Returns the status of a batch verification job. Status is one of starting, processing, completed or failed. When processing it carries a progress breakdown; when completed it carries stats and a download_url valid for one hour (re-call this action for a freshly signed URL).</td></tr><tr><td>Get Email Threat Score</td><td><code>getEmailThreatScore</code></td><td>Returns ONLY the Email Threat Score for an address, without running a standard verification. with threat_only=true. Mutually exclusive with include_threat. Consumes credits.</td></tr><tr><td>Start Batch Verification</td><td><code>startBatchVerification</code></td><td>Submits a list of email addresses for asynchronous batch verification. with a text/csv body of one email address per line (max 1 million addresses / 250MB). Returns the job id used by Get Batch Verification Status. Set callbackUrl to receive a POST when the job completes (pass an empty string for no callback); set filename to name the downloadable result file.</td></tr><tr><td>Start Batch Verification With Threat Score</td><td><code>startBatchVerificationWithThreatScore</code></td><td>Same as Start Batch Verification but with include_threat=true, so the result file also carries threat_score and threat_level columns for every address. with a text/csv body of one email per line. Returns the job id.</td></tr><tr><td>Verify Email</td><td><code>verifyEmail</code></td><td>Verifies a single email address in real time. Returns result (deliverable|undeliverable|risky|unknown), reason, role, free, disposable, accept_all, did_you_mean, sendex, user, domain. Consumes one verification credit.</td></tr><tr><td>Verify Email With Threat Score</td><td><code>verifyEmailWithThreatScore</code></td><td>Runs a full single-address verification AND returns the Email Threat Score. with include_threat=true. Returns the standard verification fields plus threat_score and threat_level. Consumes credits.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Batch Verification Completed</td><td><code>completed</code></td><td>Fires when a Kickbox batch verification job finishes successfully. SETUP (Kickbox has no webhook registration API - the callback URL is set per job): copy this trigger's Fastn webhook URL, then pass it as the `callbackUrl` input of the `Start Batch Verification` (or `Start Batch Verification With Threat Score`) action for every job you want notified. Kickbox sends the completion payload as a POST to that URL and requires a 2xx response. There is nothing to register in the Kickbox dashboard and nothing to unsubscribe - stop passing the URL and deliveries stop. Note: `download_url` in the payload is valid for one hour; after that call `Get Batch Verification Status` for a freshly signed URL.</td></tr><tr><td>Batch Verification Failed</td><td><code>failed</code></td><td>Fires when a Kickbox batch verification job ends in failure; `error` carries the vendor's description. SETUP is identical to Batch Verification Completed: Kickbox has no webhook registration API, so copy this trigger's Fastn webhook URL and pass it as the `callbackUrl` input of `Start Batch Verification` for each job. Nothing is registered in the Kickbox dashboard and there is nothing to unsubscribe.</td></tr></tbody></table>
