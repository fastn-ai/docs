---
description: "Unsplash stock photo / image API."
---

# Unsplash

Unsplash stock photo / image API. Browse, search, and manage photos, collections, topics, and users on Unsplash. Public-scope reads use an application Access Key (Client-ID); a subset of write endpoints (own profile, own photos, own collections) require a full user-scoped OAuth Bearer token which this app does not currently mint.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [unsplash.com](https://unsplash.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 29 |
| **Events** | 0 |
| **Slug** | `unsplash` |

## Use it

Add Unsplash from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.unsplash.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Photo To Collection | `addPhotoToCollection` | Add a photo to a collection owned by the authenticated user. REQUIRES a full user-scoped OAuth Bearer access token (write_collections scope) - a plain Client-ID (app-level) credential is NOT sufficient and will return 401. |
| Create Collection | `createCollection` | Create a new collection owned by the authenticated user. REQUIRES a full user-scoped OAuth Bearer access token (write_collections scope) - a plain Client-ID (app-level) credential is NOT sufficient and will return 401. |
| Delete Collection | `deleteCollection` | Delete a collection owned by the authenticated user. REQUIRES a full user-scoped OAuth Bearer access token (write_collections scope) - a plain Client-ID (app-level) credential is NOT sufficient and will return 401. |
| Get Collection | `getCollection` | Retrieve a single collection by its id. Public endpoint, Client-ID auth. |
| Get Collection Photos | `getCollectionPhotos` | List the photos in a collection. Public endpoint, Client-ID auth. |
| Get Monthly Stats | `getMonthlyStats` | Retrieve Unsplash platform statistics for the past 30 days. Public endpoint, Client-ID auth. |
| Get My Profile | `getMyProfile` | Retrieve the authenticated user's private profile. REQUIRES a full user-scoped OAuth Bearer access token (read_user scope) - a plain Client-ID (app-level) credential is NOT sufficient and will return 401, since Client-ID has no associated user identity. |
| Get Photo | `getPhoto` | Retrieve full details of a single photo by its id. Public endpoint, Client-ID auth. |
| Get Photo Statistics | `getPhotoStatistics` | Retrieve download/view/like statistics for a photo over a time window. Public endpoint, Client-ID auth. |
| Get Random Photo | `getRandomPhoto` | Retrieve one or more random photos, optionally filtered by collections, topics, username, orientation, content filter, or a search query. Public endpoint, Client-ID auth. |
| Get Related Collections | `getRelatedCollections` | List collections related to a given collection. Public endpoint, Client-ID auth. |
| Get Topic | `getTopic` | Retrieve a single topic by its id or slug. Public endpoint, Client-ID auth. |
| Get Topic Photos | `getTopicPhotos` | List the photos in a topic. Public endpoint, Client-ID auth. |
| Get Total Stats | `getTotalStats` | Retrieve total Unsplash platform statistics (all-time photo/download/view totals). Public endpoint, Client-ID auth. |
| Get User Collections | `getUserCollections` | List a user's public collections. Public endpoint, Client-ID auth. |
| Get User Photos | `getUserPhotos` | List a user's public photos. Public endpoint, Client-ID auth. |
| Get User Public Profile | `getUserPublicProfile` | Retrieve a user's public profile. Public endpoint, Client-ID auth. |
| Get User Statistics | `getUserStatistics` | Retrieve download/view statistics for a user over a time window. Public endpoint, Client-ID auth. |
| List Collections | `listCollections` | List all public collections, most recently updated first. Public endpoint, Client-ID auth. |
| List Photos | `listPhotos` | List photos from Unsplash's editorial feed, most recent first. Public endpoint, Client-ID auth. |
| List Topics | `listTopics` | List curated topics. Public endpoint, Client-ID auth. |
| Remove Photo From Collection | `removePhotoFromCollection` | Remove a photo from a collection owned by the authenticated user. REQUIRES a full user-scoped OAuth Bearer access token (write_collections scope) - a plain Client-ID (app-level) credential is NOT sufficient and will return 401. |
| Search Collections | `searchCollections` | Search for collections by keyword. Public endpoint, Client-ID auth. |
| Search Photos | `searchPhotos` | Search for photos by keyword, with optional filters for order, orientation, collections, color, content filter, and language. Public endpoint, Client-ID auth. |
| Search Users | `searchUsers` | Search for users by keyword. Public endpoint, Client-ID auth. |
| Track Photo Download | `trackPhotoDownload` | Trigger a download event for a photo, as required by Unsplash API guidelines whenever a photo's download link is used by your application. Public endpoint, Client-ID auth. Returns a temporary download link. |
| Update Collection | `updateCollection` | Update a collection owned by the authenticated user. REQUIRES a full user-scoped OAuth Bearer access token (write_collections scope) - a plain Client-ID (app-level) credential is NOT sufficient and will return 401. |
| Update My Profile | `updateMyProfile` | Update the authenticated user's profile fields. REQUIRES a full user-scoped OAuth Bearer access token (write_user scope) - a plain Client-ID (app-level) credential is NOT sufficient and will return 401. |
| Update Photo | `updatePhoto` | Update metadata of a photo owned by the authenticated user (description, tags, EXIF, location, profile visibility). REQUIRES a full user-scoped OAuth Bearer access token (write_photos scope) for a photo the authenticated user owns - a plain Client-ID (app-level) credential is NOT sufficient and will return 401. |
