---
description: "Pexels stock photo and video API."
hidden: true
---

# Pexels

<img src="../../.gitbook/assets/connectors/lg/pexels.png" alt="Pexels logo">

Pexels stock photo and video API. Search and browse free-to-use photos, videos, and curated collections contributed by photographers and videographers on Pexels.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [pexels.com](https://pexels.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `pexels` |

## Use it

Add Pexels from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pexels.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Curated Photos | `curatedPhotos` | Returns a curated, hand-picked list of current photos from Pexels, similar to the discovery feed shown on the Pexels homepage. |
| Featured Collections | `featuredCollections` | Returns Pexels' curated list of featured collections, each a themed group of photos and videos. |
| Get Collection Media | `getCollectionMedia` | Returns all the photos and/or videos within a single Pexels collection, identified by its id. |
| Get Photo | `getPhoto` | Retrieves a single Pexels photo by its numeric id. |
| Get Video | `getVideo` | Retrieves a single Pexels video by its numeric id. |
| List My Collections | `listMyCollections` | Returns the collections belonging to the Pexels account that owns the connected API key. |
| Popular Videos | `popularVideos` | Returns the current popular videos on Pexels, with optional filters for minimum width, height, and duration. |
| Search Photos | `searchPhotos` | Searches the Pexels photo library for photos matching a text query, with optional filters for orientation, size, color, and locale. |
| Search Videos | `searchVideos` | Searches the Pexels video library for videos matching a text query, with optional filters for orientation, size, and locale. |
