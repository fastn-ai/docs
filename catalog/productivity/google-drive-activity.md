---
description: "Google Drive Activity records changes to Drive files and folders. Query edits, moves, renames, comments and permission changes."
hidden: true
---

# Google Drive Activity

<img src="../../.gitbook/assets/connectors/lg/google-drive-activity.png" alt="Google Drive Activity logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [driveactivity.googleapis.com](https://driveactivity.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleDriveActivity` |

## Setup

Your customers sign in to Google Drive Activity through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Drive Activity from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Drive Activity**.
2. Select **Connect** on the Google Drive Activity card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Drive Activity and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Drive Activity's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Query Drive Activity</td><td><code>queryDriveActivity</code></td><td>Queries the Google Drive activity record and returns a page of activities. Supply either itemName to scope the query to a single Drive item or ancestorName to scope it to a folder and all of its descendants; exactly one of the two must be provided. Results can be narrowed with a filter expression on time and action type, consolidated with a consolidation strategy, and paged with pageSize and pageToken.</td></tr></tbody></table>

