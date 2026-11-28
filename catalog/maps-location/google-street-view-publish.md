---
description: "Google Street View Publish manages 360 photos on Google Maps. List and read published photos and start new photo uploads."
hidden: true
---

# Google Street View Publish

<img src="../../.gitbook/assets/connectors/lg/google-street-view-publish.png" alt="Google Street View Publish logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [streetviewpublish.googleapis.com](https://streetviewpublish.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleStreetViewPublish` |

## Setup

Your customers sign in to Google Street View Publish through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Street View Publish from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Street View Publish**.
2. Select **Connect** on the Google Street View Publish card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Street View Publish and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Street View Publish's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Photo</td><td><code>getPhoto</code></td><td>Gets the metadata of one Street View 360 photo the connected user created (pose, places, connections, share/thumbnail links, view count, Maps publish status). Returns PERMISSION_DENIED for photos the user did not create. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/streetviewpublish.</td></tr><tr><td>List Photos</td><td><code>listPhotos</code></td><td>Lists the 360 photos the connected user has published to Google Street View, with photo IDs, capture/upload times, pose, places, share and thumbnail links, view counts and Maps publish status. Optionally filter by placeId or a latitude/longitude bounding box. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/streetviewpublish.</td></tr><tr><td>Start Photo Upload</td><td><code>startUpload</code></td><td>Starts an upload session for a new Street View 360 photo and returns an uploadUrl (upload reference) to which the photo bytes are sent. Nothing is published by this call alone: a photo only appears after its bytes are uploaded to the uploadUrl and a photo is created with that reference, so it is safe to demo. Requires the Google OAuth scope https://www.googleapis.com/auth/streetviewpublish.</td></tr></tbody></table>

