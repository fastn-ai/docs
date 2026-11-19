---
description: "Dynatrace unified observability platform, accessed through an Account Management OAuth2 client (client_credentials)."
hidden: true
---

# Dynatrace

<img src="../../.gitbook/assets/connectors/lg/dynatrace-oauth.png" alt="Dynatrace logo">

Dynatrace unified observability platform, accessed through an Account Management OAuth2 client (client_credentials). Covers the Account Management Environment Management API (list environments, list Managed clusters, read the environment IP allowlist) and the Grail Query Execution API (execute, poll, cancel, verify, parse, and autocomplete Dynatrace Query Language queries against the metrics and entities tables). Scoped strictly to the OAuth client scopes account-env-read, storage:metrics:read, and storage:entities:read - the classic per-environment Environment API v2 (problems, events, synthetic, SLO, settings, users) requires a classic API token or different OAuth scopes and is out of scope for this credential.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [dynatrace.com](https://dynatrace.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `dynatraceOAuth` |

## Use it

Add Dynatrace from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dynatraceOAuth.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Autocomplete Grail Query</td><td><code>autocompleteGrailQuery</code></td><td>Returns a list of Dynatrace Query Language completion suggestions for the query text at the given cursor position, useful for building query editors.</td></tr><tr><td>Cancel Grail Query</td><td><code>cancelGrailQuery</code></td><td>Cancels a running Grail query by its request token. If the query already finished, returns its final result instead of cancelling anything; if it is still running, Grail stops execution and discards the result.</td></tr><tr><td>Execute Grail Query</td><td><code>executeGrailQuery</code></td><td>Starts a Dynatrace Query Language (DQL) query against Grail and returns a request token plus, if the query finishes quickly, the result. Only queries against tables covered by the granted scopes (the entities and metrics tables) will succeed; other Grail tables (logs, events, spans, business events) return a permission error. Use Poll Grail Query Result to fetch the final result with the returned request token.</td></tr><tr><td>Get Environment IP Allowlist</td><td><code>getIpAllowlist</code></td><td>Reads the IP allowlist configuration for your Dynatrace environment, including whether it is enabled and the allowed CIDR ranges. Requires the account-env-read scope.</td></tr><tr><td>List Environments</td><td><code>listEnvironments</code></td><td>Lists every Dynatrace environment belonging to your account, including each environment's ID, name, active status, and URL. Requires the account-env-read scope.</td></tr><tr><td>List Environments and Management Zones</td><td><code>listEnvironmentsV1</code></td><td>Lists all environments and management zones of your account using the legacy v1 Environment Management API. Requires the account-env-read scope.</td></tr><tr><td>List Managed Clusters</td><td><code>listClusters</code></td><td>Lists all Dynatrace Managed clusters registered to your account. This endpoint only applies to self-hosted Dynatrace Managed accounts; on a SaaS-only account (like this one) it returns a 404, which is the documented, expected behavior rather than a wiring defect - confirmed by comparing against the router's generic 404 signature for a nonexistent path. Requires the account-env-read scope.</td></tr><tr><td>Parse Grail Query</td><td><code>parseGrailQuery</code></td><td>Creates a tree of the canonical form of a Dynatrace Query Language statement, with node references to the token positions in the original string. Useful for building query editors and hover tooling.</td></tr><tr><td>Poll Grail Query Result</td><td><code>pollGrailQuery</code></td><td>Retrieves the current status and, once finished, the final result of a Grail query previously started with Execute Grail Query. Pass the requestToken returned by that action. Poll at an interval under one minute, since finished results are only guaranteed to remain available for one minute.</td></tr><tr><td>Verify Grail Query</td><td><code>verifyGrailQuery</code></td><td>Checks a Dynatrace Query Language statement for syntax and permission errors without executing it, returning any validation notifications.</td></tr></tbody></table>
