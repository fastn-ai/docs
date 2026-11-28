---
description: "Unsplash is a library of free stock photos. Search and get photos, manage collections and read photo statistics."
hidden: true
---

# Unsplash

<img src="../../.gitbook/assets/connectors/lg/unsplash.png" alt="Unsplash logo">

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [unsplash.com](https://unsplash.com) |
| **Authentication** | Access key |
| **Slug** | `unsplash` |

## Setup

Your customers enter their access key for Unsplash when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Unsplash from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Unsplash**.
2. Select **Connect** on the Unsplash card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Unsplash's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Photo To Collection</td><td><code>addPhotoToCollection</code></td><td>Add a photo to a collection owned by the authenticated user. REQUIRES a full user-scoped OAuth Bearer access token (write_collections scope) - a plain Client-ID (app-level) credential is NOT sufficient and will return 401.</td></tr><tr><td>Create Collection</td><td><code>createCollection</code></td><td>Create a new collection owned by the authenticated user. REQUIRES a full user-scoped OAuth Bearer access token (write_collections scope) - a plain Client-ID (app-level) credential is NOT sufficient and will return 401.</td></tr><tr><td>Delete Collection</td><td><code>deleteCollection</code></td><td>Delete a collection owned by the authenticated user. REQUIRES a full user-scoped OAuth Bearer access token (write_collections scope) - a plain Client-ID (app-level) credential is NOT sufficient and will return 401.</td></tr><tr><td>Get Collection</td><td><code>getCollection</code></td><td>Retrieve a single collection by its id. Public endpoint, Client-ID auth.</td></tr><tr><td>Get Collection Photos</td><td><code>getCollectionPhotos</code></td><td>List the photos in a collection. Public endpoint, Client-ID auth.</td></tr><tr><td>Get Monthly Stats</td><td><code>getMonthlyStats</code></td><td>Retrieve Unsplash platform statistics for the past 30 days. Public endpoint, Client-ID auth.</td></tr><tr><td>Get My Profile</td><td><code>getMyProfile</code></td><td>Retrieve the authenticated user's private profile. REQUIRES a full user-scoped OAuth Bearer access token (read_user scope) - a plain Client-ID (app-level) credential is NOT sufficient and will return 401, since Client-ID has no associated user identity.</td></tr><tr><td>Get Photo</td><td><code>getPhoto</code></td><td>Retrieve full details of a single photo by its id. Public endpoint, Client-ID auth.</td></tr><tr><td>Get Photo Statistics</td><td><code>getPhotoStatistics</code></td><td>Retrieve download/view/like statistics for a photo over a time window. Public endpoint, Client-ID auth.</td></tr><tr><td>Get Random Photo</td><td><code>getRandomPhoto</code></td><td>Retrieve one or more random photos, optionally filtered by collections, topics, username, orientation, content filter, or a search query. Public endpoint, Client-ID auth.</td></tr></tbody></table>

<details>

<summary>View 19 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Related Collections</td><td><code>getRelatedCollections</code></td><td>List collections related to a given collection. Public endpoint, Client-ID auth.</td></tr><tr><td>Get Topic</td><td><code>getTopic</code></td><td>Retrieve a single topic by its id or slug. Public endpoint, Client-ID auth.</td></tr><tr><td>Get Topic Photos</td><td><code>getTopicPhotos</code></td><td>List the photos in a topic. Public endpoint, Client-ID auth.</td></tr><tr><td>Get Total Stats</td><td><code>getTotalStats</code></td><td>Retrieve total Unsplash platform statistics (all-time photo/download/view totals). Public endpoint, Client-ID auth.</td></tr><tr><td>Get User Collections</td><td><code>getUserCollections</code></td><td>List a user's public collections. Public endpoint, Client-ID auth.</td></tr><tr><td>Get User Photos</td><td><code>getUserPhotos</code></td><td>List a user's public photos. Public endpoint, Client-ID auth.</td></tr><tr><td>Get User Public Profile</td><td><code>getUserPublicProfile</code></td><td>Retrieve a user's public profile. Public endpoint, Client-ID auth.</td></tr><tr><td>Get User Statistics</td><td><code>getUserStatistics</code></td><td>Retrieve download/view statistics for a user over a time window. Public endpoint, Client-ID auth.</td></tr><tr><td>List Collections</td><td><code>listCollections</code></td><td>List all public collections, most recently updated first. Public endpoint, Client-ID auth.</td></tr><tr><td>List Photos</td><td><code>listPhotos</code></td><td>List photos from Unsplash's editorial feed, most recent first. Public endpoint, Client-ID auth.</td></tr><tr><td>List Topics</td><td><code>listTopics</code></td><td>List curated topics. Public endpoint, Client-ID auth.</td></tr><tr><td>Remove Photo From Collection</td><td><code>removePhotoFromCollection</code></td><td>Remove a photo from a collection owned by the authenticated user. REQUIRES a full user-scoped OAuth Bearer access token (write_collections scope) - a plain Client-ID (app-level) credential is NOT sufficient and will return 401.</td></tr><tr><td>Search Collections</td><td><code>searchCollections</code></td><td>Search for collections by keyword. Public endpoint, Client-ID auth.</td></tr><tr><td>Search Photos</td><td><code>searchPhotos</code></td><td>Search for photos by keyword, with optional filters for order, orientation, collections, color, content filter, and language. Public endpoint, Client-ID auth.</td></tr><tr><td>Search Users</td><td><code>searchUsers</code></td><td>Search for users by keyword. Public endpoint, Client-ID auth.</td></tr><tr><td>Track Photo Download</td><td><code>trackPhotoDownload</code></td><td>Trigger a download event for a photo, as required by Unsplash API guidelines whenever a photo's download link is used by your application. Public endpoint, Client-ID auth. Returns a temporary download link.</td></tr><tr><td>Update Collection</td><td><code>updateCollection</code></td><td>Update a collection owned by the authenticated user. REQUIRES a full user-scoped OAuth Bearer access token (write_collections scope) - a plain Client-ID (app-level) credential is NOT sufficient and will return 401.</td></tr><tr><td>Update My Profile</td><td><code>updateMyProfile</code></td><td>Update the authenticated user's profile fields. REQUIRES a full user-scoped OAuth Bearer access token (write_user scope) - a plain Client-ID (app-level) credential is NOT sufficient and will return 401.</td></tr><tr><td>Update Photo</td><td><code>updatePhoto</code></td><td>Update metadata of a photo owned by the authenticated user (description, tags, EXIF, location, profile visibility). REQUIRES a full user-scoped OAuth Bearer access token (write_photos scope) for a photo the authenticated user owns - a plain Client-ID (app-level) credential is NOT sufficient and will return 401.</td></tr></tbody></table>

</details>

