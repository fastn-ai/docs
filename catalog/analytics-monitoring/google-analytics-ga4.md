---
description: "Google Analytics 4 measures website and app traffic. Run reports, read metadata, and manage accounts, properties and data streams."
hidden: true
---

# Google Analytics GA4

<img src="../../.gitbook/assets/connectors/lg/google-analytics-ga4.png" alt="Google Analytics GA4 logo">

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [analytics.google.com](https://analytics.google.com) |
| **Authentication** | Access token, OAuth 2.0 |
| **Slug** | `googleAnalyticsGa4` |

## Setup

Your customers sign in to Google Analytics GA4 through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Analytics GA4 from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleAnalyticsGa4.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Run Reports</td><td><code>batchRunReports</code></td><td>Run multiple reports in one call</td></tr><tr><td>Check Compatibility</td><td><code>checkCompatibility</code></td><td>Check which dimensions/metrics are compatible</td></tr><tr><td>Create Data Stream</td><td><code>createDataStream</code></td><td>Create a data stream</td></tr><tr><td>Create Property</td><td><code>createProperty</code></td><td>Create a GA4 property</td></tr><tr><td>Delete Property</td><td><code>deleteProperty</code></td><td>Soft-delete (mark for deletion) a GA4 property Returns the property in its soft-deleted state with deleteTime and expireTime set.</td></tr><tr><td>Get Metadata</td><td><code>getMetadata</code></td><td>List available dimensions and metrics for a property</td></tr><tr><td>Get Property</td><td><code>getProperty</code></td><td>Get a GA4 property</td></tr><tr><td>List Account Summaries</td><td><code>listAccountSummaries</code></td><td>List GA4 account summaries (GET analyticsadmin /v1beta/accountSummaries). Read-only.</td></tr><tr><td>List Accounts</td><td><code>listAccounts</code></td><td>List GA4 accounts (GET analyticsadmin /v1beta/accounts).</td></tr><tr><td>List Data Streams</td><td><code>listDataStreams</code></td><td>List data streams for a property</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Google Ads Links</td><td><code>listGoogleAdsLinks</code></td><td>List Google Ads links for a property</td></tr><tr><td>List Properties</td><td><code>listProperties</code></td><td>List GA4 properties under an account</td></tr><tr><td>Provision Account Ticket</td><td><code>provisionAccountTicket</code></td><td>Request a GA4 account-creation ticket (POST analyticsadmin /v1beta/accounts:provisionAccountTicket). Requires the analytics.edit write scope. Returns only a transient accountTicketId - no GA4 account is created unless a human afterwards accepts the Terms of Service via the ticket link.</td></tr><tr><td>Run Access Report</td><td><code>runAccessReport</code></td><td>Run a data access audit report</td></tr><tr><td>Run Pivot Report</td><td><code>runPivotReport</code></td><td>Run a pivot report</td></tr><tr><td>Run Realtime Report</td><td><code>runRealtimeReport</code></td><td>Run a realtime Google Analytics 4 report on a property for the last 30 minutes, with dimension and metric filters, sorting, row limit, totals and custom minute ranges.</td></tr><tr><td>Run Report</td><td><code>runReport</code></td><td>Run a Google Analytics 4 report on a property: pick dimensions, metrics and date ranges, with dimension and metric filters, sorting, paging (limit, offset) and totals.</td></tr><tr><td>Update Property</td><td><code>updateProperty</code></td><td>Update a GA4 property</td></tr></tbody></table>

</details>

## Events

Google Analytics GA4 has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
