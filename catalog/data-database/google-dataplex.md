---
description: "Google Dataplex is a data catalog and governance service. List lakes and create, get, list and delete entry groups."
hidden: true
---

# Google Dataplex

<img src="../../.gitbook/assets/connectors/lg/google-dataplex.png" alt="Google Dataplex logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [dataplex.googleapis.com](https://dataplex.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleDataplex` |

## Setup

Your customers sign in to Google Dataplex through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Dataplex from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Dataplex**.
2. Select **Connect** on the Google Dataplex card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Dataplex and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Dataplex's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Entry Group</td><td><code>createEntryGroup</code></td><td>Creates an empty Dataplex Universal Catalog entry group (a logical container for catalog entries) with the given ID. Returns a long-running operation; poll it with Get Operation, then read the group with Get Entry Group. Safe to demo: an empty entry group holds no data and can be removed with Delete Entry Group. Requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.read-write.</td></tr><tr><td>Delete Entry Group</td><td><code>deleteEntryGroup</code></td><td>Deletes a Dataplex Universal Catalog entry group (use it to clean up the group made by Create Entry Group). The entry group must be empty. Returns a long-running operation; poll it with Get Operation. Requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.read-write.</td></tr><tr><td>Get Entry Group</td><td><code>getEntryGroup</code></td><td>Retrieves one Dataplex Universal Catalog entry group by project, location and entry group ID. Use it to confirm an entry group exists (for example after Create Entry Group's operation completes) and to read its etag. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.readonly (or dataplex.read-write).</td></tr><tr><td>Get Operation</td><td><code>getOperation</code></td><td>Gets the status of a Dataplex long-running operation, such as the one returned by Create Entry Group or Delete Entry Group. Returns done, and either the result in response or the failure in error. Requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.read-write.</td></tr><tr><td>List Entry Groups</td><td><code>listEntryGroups</code></td><td>Lists the Dataplex Universal Catalog entry groups in a Google Cloud project and location (for example 'global' or 'us-central1'). Returns each entry group's resource name, display name, description, labels and timestamps. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.readonly (or dataplex.read-write).</td></tr><tr><td>List Lakes</td><td><code>listLakes</code></td><td>Lists the Dataplex lakes in a Google Cloud project and region, including each lake's display name, state, metastore settings and asset status. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/dataplex.readonly (or dataplex.read-write).</td></tr></tbody></table>

