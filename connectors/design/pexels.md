---
description: "Pexels stock photo and video API."
hidden: true
---

# Pexels

<img src="../../.gitbook/assets/connectors/lg/pexels.png" alt="Pexels logo">

Search and browse free-to-use photos, videos, and curated collections contributed by photographers and videographers on Pexels.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [pexels.com](https://pexels.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `pexels` |

## Use it

Add Pexels from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pexels.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Curated Photos</td><td><code>curatedPhotos</code></td><td>Returns a curated, hand-picked list of current photos from Pexels, similar to the discovery feed shown on the Pexels homepage.</td></tr><tr><td>Featured Collections</td><td><code>featuredCollections</code></td><td>Returns Pexels' curated list of featured collections, each a themed group of photos and videos.</td></tr><tr><td>Get Collection Media</td><td><code>getCollectionMedia</code></td><td>Returns all the photos and/or videos within a single Pexels collection, identified by its id.</td></tr><tr><td>Get Photo</td><td><code>getPhoto</code></td><td>Retrieves a single Pexels photo by its numeric id.</td></tr><tr><td>Get Video</td><td><code>getVideo</code></td><td>Retrieves a single Pexels video by its numeric id.</td></tr><tr><td>List My Collections</td><td><code>listMyCollections</code></td><td>Returns the collections belonging to the Pexels account that owns the connected API key.</td></tr><tr><td>Popular Videos</td><td><code>popularVideos</code></td><td>Returns the current popular videos on Pexels, with optional filters for minimum width, height, and duration.</td></tr><tr><td>Search Photos</td><td><code>searchPhotos</code></td><td>Searches the Pexels photo library for photos matching a text query, with optional filters for orientation, size, color, and locale.</td></tr><tr><td>Search Videos</td><td><code>searchVideos</code></td><td>Searches the Pexels video library for videos matching a text query, with optional filters for orientation, size, and locale.</td></tr></tbody></table>
