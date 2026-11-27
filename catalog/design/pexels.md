---
description: "Pexels is a library of free stock photos and videos. Search and browse photos, videos and collections."
hidden: true
---

# Pexels

<img src="../../.gitbook/assets/connectors/lg/pexels.png" alt="Pexels logo">

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [pexels.com](https://pexels.com) |
| **Authentication** | API key |
| **Slug** | `pexels` |

## Setup

Your customers enter their API key for Pexels when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Pexels from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Pexels**.
2. Select **Connect** on the Pexels card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Pexels's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Curated Photos</td><td><code>curatedPhotos</code></td><td>Returns a curated, hand-picked list of current photos from Pexels, similar to the discovery feed shown on the Pexels homepage.</td></tr><tr><td>Featured Collections</td><td><code>featuredCollections</code></td><td>Returns Pexels' curated list of featured collections, each a themed group of photos and videos.</td></tr><tr><td>Get Collection Media</td><td><code>getCollectionMedia</code></td><td>Returns all the photos and/or videos within a single Pexels collection, identified by its id.</td></tr><tr><td>Get Photo</td><td><code>getPhoto</code></td><td>Retrieves a single Pexels photo by its numeric id.</td></tr><tr><td>Get Video</td><td><code>getVideo</code></td><td>Retrieves a single Pexels video by its numeric id.</td></tr><tr><td>List My Collections</td><td><code>listMyCollections</code></td><td>Returns the collections belonging to the Pexels account that owns the connected API key.</td></tr><tr><td>Popular Videos</td><td><code>popularVideos</code></td><td>Returns the current popular videos on Pexels, with optional filters for minimum width, height, and duration.</td></tr><tr><td>Search Photos</td><td><code>searchPhotos</code></td><td>Searches the Pexels photo library for photos matching a text query, with optional filters for orientation, size, color, and locale.</td></tr><tr><td>Search Videos</td><td><code>searchVideos</code></td><td>Searches the Pexels video library for videos matching a text query, with optional filters for orientation, size, and locale.</td></tr></tbody></table>

