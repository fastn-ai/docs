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

## Connect in Fastn

Your customers connect Google Analytics GA4 from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Analytics GA4**.
2. Select **Connect** on the Google Analytics GA4 card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Google Analytics GA4 offers more than one sign-in method. Choose one in **Auth Method**, then:

   * For a key or credential method, fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

     <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

   * For OAuth 2.0, keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Analytics GA4 and approve access in the window that opens.

     <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Analytics GA4's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Run Reports</td><td><code>batchRunReports</code></td><td>Run multiple reports in one call</td></tr><tr><td>Check Compatibility</td><td><code>checkCompatibility</code></td><td>Check which dimensions/metrics are compatible</td></tr><tr><td>Create Data Stream</td><td><code>createDataStream</code></td><td>Create a data stream</td></tr><tr><td>Create Property</td><td><code>createProperty</code></td><td>Create a GA4 property</td></tr><tr><td>Delete Property</td><td><code>deleteProperty</code></td><td>Soft-delete (mark for deletion) a GA4 property Returns the property in its soft-deleted state with deleteTime and expireTime set.</td></tr><tr><td>Get Metadata</td><td><code>getMetadata</code></td><td>List available dimensions and metrics for a property</td></tr><tr><td>Get Property</td><td><code>getProperty</code></td><td>Get a GA4 property</td></tr><tr><td>List Account Summaries</td><td><code>listAccountSummaries</code></td><td>List GA4 account summaries (GET analyticsadmin /v1beta/accountSummaries). Read-only.</td></tr><tr><td>List Accounts</td><td><code>listAccounts</code></td><td>List GA4 accounts (GET analyticsadmin /v1beta/accounts).</td></tr><tr><td>List Data Streams</td><td><code>listDataStreams</code></td><td>List data streams for a property</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Google Ads Links</td><td><code>listGoogleAdsLinks</code></td><td>List Google Ads links for a property</td></tr><tr><td>List Properties</td><td><code>listProperties</code></td><td>List GA4 properties under an account</td></tr><tr><td>Provision Account Ticket</td><td><code>provisionAccountTicket</code></td><td>Request a GA4 account-creation ticket (POST analyticsadmin /v1beta/accounts:provisionAccountTicket). Requires the analytics.edit write scope. Returns only a transient accountTicketId - no GA4 account is created unless a human afterwards accepts the Terms of Service via the ticket link.</td></tr><tr><td>Run Access Report</td><td><code>runAccessReport</code></td><td>Run a data access audit report</td></tr><tr><td>Run Pivot Report</td><td><code>runPivotReport</code></td><td>Run a pivot report</td></tr><tr><td>Run Realtime Report</td><td><code>runRealtimeReport</code></td><td>Run a realtime Google Analytics 4 report on a property for the last 30 minutes, with dimension and metric filters, sorting, row limit, totals and custom minute ranges.</td></tr><tr><td>Run Report</td><td><code>runReport</code></td><td>Run a Google Analytics 4 report on a property: pick dimensions, metrics and date ranges, with dimension and metric filters, sorting, paging (limit, offset) and totals.</td></tr><tr><td>Update Property</td><td><code>updateProperty</code></td><td>Update a GA4 property</td></tr></tbody></table>

</details>

