---
description: "Google Analytics 4 — Data API v1 (analyticsdata.googleapis.com: runReport, batchRunReports, runRealtimeReport, runPivotReport, checkCompatibility, metadata,…"
hidden: true
---

# Google Analytics GA4

<img src="../../.gitbook/assets/connectors/google-analytics-ga4.png" alt="Google Analytics GA4 logo" width="64">

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

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Run Reports | `batchRunReports` | Run multiple reports in one call (POST /v1beta/properties/{propertyId}:batchRunReports). |
| Check Compatibility | `checkCompatibility` | Check which dimensions/metrics are compatible (POST /v1beta/properties/{propertyId}:checkCompatibility). |
| Create Data Stream | `createDataStream` | Create a data stream (POST /v1beta/properties/{propertyId}/dataStreams). |
| Create Property | `createProperty` | Create a GA4 property (POST /v1beta/properties). |
| Delete Property | `deleteProperty` | Soft-delete (mark for deletion) a GA4 property (DELETE /v1beta/properties/{propertyId}). Returns the property in its soft-deleted state with deleteTime and expireTime set. |
| Get Metadata | `getMetadata` | List available dimensions and metrics for a property (GET /v1beta/properties/{propertyId}/metadata). |
| Get Property | `getProperty` | Get a GA4 property (GET /v1beta/properties/{propertyId}). |
| List Account Summaries | `listAccountSummaries` | List GA4 account summaries (GET analyticsadmin /v1beta/accountSummaries). Read-only. |
| List Accounts | `listAccounts` | List GA4 accounts (GET analyticsadmin /v1beta/accounts). |
| List Data Streams | `listDataStreams` | List data streams for a property (GET /v1beta/properties/{propertyId}/dataStreams). |

<details>

<summary>See 8 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Google Ads Links | `listGoogleAdsLinks` | List Google Ads links for a property (GET /v1beta/properties/{propertyId}/googleAdsLinks). |
| List Properties | `listProperties` | List GA4 properties under an account (GET /v1beta/properties?filter=parent:accounts/{id}). |
| Provision Account Ticket | `provisionAccountTicket` | Request a GA4 account-creation ticket (POST analyticsadmin /v1beta/accounts:provisionAccountTicket). Requires the analytics.edit write scope. Returns only a transient accountTicketId - no GA4 account is created unless a human afterwards accepts the Terms of Service via the ticket link. |
| Run Access Report | `runAccessReport` | Run a data access audit report (POST /v1beta/properties/{propertyId}:runAccessReport). |
| Run Pivot Report | `runPivotReport` | Run a pivot report (POST /v1beta/properties/{propertyId}:runPivotReport). |
| Run Realtime Report | `runRealtimeReport` | Run a realtime Google Analytics 4 report on a property for the last 30 minutes, with dimension and metric filters, sorting, row limit, totals and custom minute ranges. |
| Run Report | `runReport` | Run a Google Analytics 4 report on a property: pick dimensions, metrics and date ranges, with dimension and metric filters, sorting, paging (limit, offset) and totals. |
| Update Property | `updateProperty` | Update a GA4 property (PATCH /v1beta/properties/{propertyId}?updateMask=). |

</details>
