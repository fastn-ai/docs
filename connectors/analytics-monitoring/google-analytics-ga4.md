---
description: "Google Analytics 4 — Data API v1 (analyticsdata.googleapis.com: runReport, batchRunReports, runRealtimeReport, runPivotReport, checkCompatibility, metadata,…"
hidden: true
---

# Google Analytics GA4

<img src="../../.gitbook/assets/connectors/lg/google-analytics-ga4.png" alt="Google Analytics GA4 logo">

Google Analytics 4 — Data API v1 (analyticsdata.googleapis.com: runReport, batchRunReports, runRealtimeReport, runPivotReport, checkCompatibility, metadata, runAccessReport) and Admin API v1 (analyticsadmin.googleapis.com: accounts, properties, data streams, Google Ads links). Auth: Google OAuth 2.0 bearer access token (scope analytics.readonly / analytics.edit). No webhooks.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [analytics.google.com](https://analytics.google.com) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Slug** | `googleAnalyticsGa4` |

## Use it

Add Google Analytics GA4 from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleAnalyticsGa4.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Run Reports</td><td><code>batchRunReports</code></td><td>Run multiple reports in one call (POST /v1beta/properties/{propertyId}:batchRunReports).</td></tr><tr><td>Check Compatibility</td><td><code>checkCompatibility</code></td><td>Check which dimensions/metrics are compatible (POST /v1beta/properties/{propertyId}:checkCompatibility).</td></tr><tr><td>Create Data Stream</td><td><code>createDataStream</code></td><td>Create a data stream (POST /v1beta/properties/{propertyId}/dataStreams).</td></tr><tr><td>Create Property</td><td><code>createProperty</code></td><td>Create a GA4 property (POST /v1beta/properties).</td></tr><tr><td>Delete Property</td><td><code>deleteProperty</code></td><td>Soft-delete (mark for deletion) a GA4 property (DELETE /v1beta/properties/{propertyId}). Returns the property in its soft-deleted state with deleteTime and expireTime set.</td></tr><tr><td>Get Metadata</td><td><code>getMetadata</code></td><td>List available dimensions and metrics for a property (GET /v1beta/properties/{propertyId}/metadata).</td></tr><tr><td>Get Property</td><td><code>getProperty</code></td><td>Get a GA4 property (GET /v1beta/properties/{propertyId}).</td></tr><tr><td>List Account Summaries</td><td><code>listAccountSummaries</code></td><td>List GA4 account summaries (GET analyticsadmin /v1beta/accountSummaries). Read-only.</td></tr><tr><td>List Accounts</td><td><code>listAccounts</code></td><td>List GA4 accounts (GET analyticsadmin /v1beta/accounts).</td></tr><tr><td>List Data Streams</td><td><code>listDataStreams</code></td><td>List data streams for a property (GET /v1beta/properties/{propertyId}/dataStreams).</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Google Ads Links</td><td><code>listGoogleAdsLinks</code></td><td>List Google Ads links for a property (GET /v1beta/properties/{propertyId}/googleAdsLinks).</td></tr><tr><td>List Properties</td><td><code>listProperties</code></td><td>List GA4 properties under an account (GET /v1beta/properties?filter=parent:accounts/{id}).</td></tr><tr><td>Provision Account Ticket</td><td><code>provisionAccountTicket</code></td><td>Request a GA4 account-creation ticket (POST analyticsadmin /v1beta/accounts:provisionAccountTicket). Requires the analytics.edit write scope. Returns only a transient accountTicketId - no GA4 account is created unless a human afterwards accepts the Terms of Service via the ticket link.</td></tr><tr><td>Run Access Report</td><td><code>runAccessReport</code></td><td>Run a data access audit report (POST /v1beta/properties/{propertyId}:runAccessReport).</td></tr><tr><td>Run Pivot Report</td><td><code>runPivotReport</code></td><td>Run a pivot report (POST /v1beta/properties/{propertyId}:runPivotReport).</td></tr><tr><td>Run Realtime Report</td><td><code>runRealtimeReport</code></td><td>Run a realtime Google Analytics 4 report on a property for the last 30 minutes, with dimension and metric filters, sorting, row limit, totals and custom minute ranges.</td></tr><tr><td>Run Report</td><td><code>runReport</code></td><td>Run a Google Analytics 4 report on a property: pick dimensions, metrics and date ranges, with dimension and metric filters, sorting, paging (limit, offset) and totals.</td></tr><tr><td>Update Property</td><td><code>updateProperty</code></td><td>Update a GA4 property (PATCH /v1beta/properties/{propertyId}?updateMask=).</td></tr></tbody></table>

</details>
