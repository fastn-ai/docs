---
description: "Google Maps Grounding Lite gives AI agents Google Maps data. Search places, look up weather, compute routes and resolve place names."
hidden: true
---

# Google Maps Grounding Lite

<img src="../../.gitbook/assets/connectors/lg/google-maps-grounding-lite.png" alt="Google Maps Grounding Lite logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [mapstools.googleapis.com](https://mapstools.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleMapsGroundingLite` |

## Setup

Your customers sign in to Google Maps Grounding Lite through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Maps Grounding Lite from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Maps Grounding Lite**.
2. Select **Connect** on the Google Maps Grounding Lite card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Maps Grounding Lite and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Maps Grounding Lite's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

