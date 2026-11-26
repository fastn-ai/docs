---
description: "Google Network Management checks network reachability on Google Cloud. Create, list, get and delete connectivity tests."
hidden: true
---

# Google Network Management

<img src="../../.gitbook/assets/connectors/lg/google-network-management.png" alt="Google Network Management logo">

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [networkmanagement.googleapis.com](https://networkmanagement.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleNetworkManagement` |

## Setup

Your customers sign in to Google Network Management through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Network Management from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleNetworkManagement.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Connectivity Test</td><td><code>createConnectivityTest</code></td><td>Creates a Connectivity Test and runs a static reachability analysis between a source and destination; it sends no traffic and changes no network configuration. Example: source {"projectId": "my-project", "network": "projects/my-project/global/networks/default", "ipAddress": "10.128.0.2"}, destination {"ipAddress": "8.8.8.8", "port": 443}, protocol 'TCP'. Returns a long-running operation; poll it with Get Operation, then read the result with Get Connectivity Test and clean up with Delete Connectivity Test. Test runs may be billed under Network Intelligence Center pricing. Requires the Google OAuth scope https://www.googleapis.com/auth/cloud-network-insights.</td></tr><tr><td>Delete Connectivity Test</td><td><code>deleteConnectivityTest</code></td><td>Deletes a Connectivity Test (use it to clean up the test made by Create Connectivity Test). Returns a long-running operation; poll it with Get Operation. Requires the Google OAuth scope https://www.googleapis.com/auth/cloud-network-insights.</td></tr><tr><td>Get Connectivity Test</td><td><code>getConnectivityTest</code></td><td>Gets one Connectivity Test by ID, including its source, destination, protocol and the reachability analysis result from its latest run (REACHABLE, UNREACHABLE, AMBIGUOUS or UNDETERMINED, with traces). Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/cloud-network-insights.</td></tr><tr><td>Get Operation</td><td><code>getOperation</code></td><td>Gets the status of a Network Management long-running operation, such as the one returned by Create or Delete Connectivity Test. Returns done, and either the result in response or the failure in error. Requires the Google OAuth scope https://www.googleapis.com/auth/cloud-network-insights.</td></tr><tr><td>List Connectivity Tests</td><td><code>listConnectivityTests</code></td><td>Lists the Network Intelligence Center Connectivity Tests in a Google Cloud project, with each test's source, destination, protocol and latest reachability result. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/cloud-network-insights.</td></tr><tr><td>List Connectivity Tests (MCP)</td><td><code>listConnectivityTestsMcp</code></td><td>Lists Connectivity Tests in a project by calling the list_connectivity_tests tool on Google's Network Management remote MCP endpoint (https://networkmanagement.googleapis.com/mcp, JSON-RPC tools/call). Read-only. Returns a JSON-RPC result whose structuredContent holds the tests.</td></tr><tr><td>List Network Monitoring Providers</td><td><code>listNetworkMonitoringProviders</code></td><td>Lists the Cloud Network Insights network monitoring providers (the AppNeta-backed monitoring setups) in a Google Cloud project and location. Read-only. Part of Cloud Network Insights; intended to demonstrate the https://www.googleapis.com/auth/cloud-network-insights scope.</td></tr></tbody></table>

## Events

Google Network Management has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
