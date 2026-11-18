---
description: "Google Network Management API (networkmanagement.googleapis.com v1), part of Network Intelligence Center."
hidden: true
---

# Google Network Management

<img src="../../.gitbook/assets/connectors/lg/google-network-management.png" alt="Google Network Management logo">

Google Network Management API (networkmanagement.googleapis.com v1), part of Network Intelligence Center. List, get, create and delete Connectivity Tests, which run static reachability analysis between a source and destination (IP addresses, VM instances, load balancers and more) in a Google Cloud project, and poll the long-running operations they return. Authorizes with Google OAuth 2.0 using the scope https://www.googleapis.com/auth/cloud-network-insights.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [networkmanagement.googleapis.com](https://networkmanagement.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleNetworkManagement` |

## Use it

Add Google Network Management from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleNetworkManagement.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Connectivity Test | `createConnectivityTest` | Creates a Connectivity Test and runs a static reachability analysis between a source and destination; it sends no traffic and changes no network configuration. Example: source {"projectId": "my-project", "network": "projects/my-project/global/networks/default", "ipAddress": "10.128.0.2"}, destination {"ipAddress": "8.8.8.8", "port": 443}, protocol 'TCP'. Returns a long-running operation; poll it with Get Operation, then read the result with Get Connectivity Test and clean up with Delete Connectivity Test. Test runs may be billed under Network Intelligence Center pricing. Requires the Google OAuth scope https://www.googleapis.com/auth/cloud-network-insights. |
| Delete Connectivity Test | `deleteConnectivityTest` | Deletes a Connectivity Test (use it to clean up the test made by Create Connectivity Test). Returns a long-running operation; poll it with Get Operation. Requires the Google OAuth scope https://www.googleapis.com/auth/cloud-network-insights. |
| Get Connectivity Test | `getConnectivityTest` | Gets one Connectivity Test by ID, including its source, destination, protocol and the reachability analysis result from its latest run (REACHABLE, UNREACHABLE, AMBIGUOUS or UNDETERMINED, with traces). Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/cloud-network-insights. |
| Get Operation | `getOperation` | Gets the status of a Network Management long-running operation, such as the one returned by Create or Delete Connectivity Test. Returns done, and either the result in response or the failure in error. Requires the Google OAuth scope https://www.googleapis.com/auth/cloud-network-insights. |
| List Connectivity Tests | `listConnectivityTests` | Lists the Network Intelligence Center Connectivity Tests in a Google Cloud project, with each test's source, destination, protocol and latest reachability result. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/cloud-network-insights. |
| List Connectivity Tests (MCP) | `listConnectivityTestsMcp` | Lists Connectivity Tests in a project by calling the list_connectivity_tests tool on Google's Network Management remote MCP endpoint (https://networkmanagement.googleapis.com/mcp, JSON-RPC tools/call). Read-only. Returns a JSON-RPC result whose structuredContent holds the tests. |
| List Network Monitoring Providers | `listNetworkMonitoringProviders` | Lists the Cloud Network Insights network monitoring providers (the AppNeta-backed monitoring setups) in a Google Cloud project and location. Read-only. Part of Cloud Network Insights; intended to demonstrate the https://www.googleapis.com/auth/cloud-network-insights scope. |
