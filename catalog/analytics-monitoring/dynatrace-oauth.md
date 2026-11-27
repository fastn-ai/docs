---
description: "Dynatrace is an observability platform. Run and manage Grail queries, and list environments, management zones and managed clusters."
hidden: true
---

# Dynatrace (OAuth)

<img src="../../.gitbook/assets/connectors/lg/dynatrace-oauth.png" alt="Dynatrace (OAuth) logo">

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [dynatrace.com](https://dynatrace.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `dynatraceOAuth` |

## Setup

Your customers sign in to Dynatrace (OAuth) through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Dynatrace (OAuth) from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Dynatrace (OAuth)**.
2. Select **Connect** on the Dynatrace (OAuth) card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Dynatrace (OAuth) and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Dynatrace (OAuth)'s actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Autocomplete Grail Query</td><td><code>autocompleteGrailQuery</code></td><td>Returns a list of Dynatrace Query Language completion suggestions for the query text at the given cursor position, useful for building query editors.</td></tr><tr><td>Cancel Grail Query</td><td><code>cancelGrailQuery</code></td><td>Cancels a running Grail query by its request token. If the query already finished, returns its final result instead of cancelling anything; if it is still running, Grail stops execution and discards the result.</td></tr><tr><td>Execute Grail Query</td><td><code>executeGrailQuery</code></td><td>Starts a Dynatrace Query Language (DQL) query against Grail and returns a request token plus, if the query finishes quickly, the result. Only queries against tables covered by the granted scopes (the entities and metrics tables) will succeed; other Grail tables (logs, events, spans, business events) return a permission error. Use Poll Grail Query Result to fetch the final result with the returned request token.</td></tr><tr><td>Get Environment IP Allowlist</td><td><code>getIpAllowlist</code></td><td>Reads the IP allowlist configuration for your Dynatrace environment, including whether it is enabled and the allowed CIDR ranges. Requires the account-env-read scope.</td></tr><tr><td>List Environments</td><td><code>listEnvironments</code></td><td>Lists every Dynatrace environment belonging to your account, including each environment's ID, name, active status, and URL. Requires the account-env-read scope.</td></tr><tr><td>List Environments and Management Zones</td><td><code>listEnvironmentsV1</code></td><td>Lists all environments and management zones of your account using the legacy v1 Environment Management API. Requires the account-env-read scope.</td></tr><tr><td>List Managed Clusters</td><td><code>listClusters</code></td><td>Lists all Dynatrace Managed clusters registered to your account. This endpoint only applies to self-hosted Dynatrace Managed accounts; on a SaaS-only account (like this one) it Requires the account-env-read scope.</td></tr><tr><td>Parse Grail Query</td><td><code>parseGrailQuery</code></td><td>Creates a tree of the canonical form of a Dynatrace Query Language statement, with node references to the token positions in the original string. Useful for building query editors and hover tooling.</td></tr><tr><td>Poll Grail Query Result</td><td><code>pollGrailQuery</code></td><td>Retrieves the current status and, once finished, the final result of a Grail query previously started with Execute Grail Query. Pass the requestToken returned by that action. Poll at an interval under one minute, since finished results are only guaranteed to remain available for one minute.</td></tr><tr><td>Verify Grail Query</td><td><code>verifyGrailQuery</code></td><td>Checks a Dynatrace Query Language statement for syntax and permission errors without executing it, returning any validation notifications.</td></tr></tbody></table>

