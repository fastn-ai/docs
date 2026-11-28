---
description: "The Cat API serves cat images and breed data. Get breeds and facts, and manage images, favourites and votes."
hidden: true
---

# The Cat API

<img src="../../.gitbook/assets/connectors/lg/thecatapi.png" alt="The Cat API logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [thecatapi.com](https://thecatapi.com) |
| **Authentication** | API key |
| **Slug** | `thecatapi` |

## Setup

Your customers enter their API key for The Cat API when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect The Cat API from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **The Cat API**.
2. Select **Connect** on the The Cat API card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use The Cat API's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create a Favourite</td><td><code>createFavourite</code></td><td>Marks an image as a favourite on your account, optionally scoped to one of your own end users via sub_id.</td></tr><tr><td>Create a Vote</td><td><code>createVote</code></td><td>Casts an up or down vote on an image, optionally scoped to one of your own end users via sub_id.</td></tr><tr><td>Delete a Favourite</td><td><code>deleteFavourite</code></td><td>Removes a favourite record from your account by id.</td></tr><tr><td>Delete a Vote</td><td><code>deleteVote</code></td><td>Removes a vote record from your account by id.</td></tr><tr><td>Delete an Image</td><td><code>deleteImage</code></td><td>Deletes an image from your account by id. Only works for images you uploaded.</td></tr><tr><td>Get Breed by ID</td><td><code>getBreedById</code></td><td>Fetches full profile data for a single cat breed by its breed id.</td></tr><tr><td>Get Breeds Tagged on an Image</td><td><code>getImageBreeds</code></td><td>Lists the breeds currently tagged on a given image.</td></tr><tr><td>Get Facts About a Breed</td><td><code>getBreedFacts</code></td><td>Returns one or more facts about a given breed. This is a premium feature of The Cat API and requires an upgraded/paid account; a free API key</td></tr><tr><td>Get Favourite by ID</td><td><code>getFavouriteById</code></td><td>Fetches a single favourite record by its id, including the favourited image.</td></tr><tr><td>Get Image Analysis</td><td><code>getImageAnalysis</code></td><td>Returns the raw computer-vision analysis results (object/label detections and moderation labels) for a previously uploaded image.</td></tr></tbody></table>

<details>

<summary>View 13 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Image by ID</td><td><code>getImageById</code></td><td>Fetches a single cat image's metadata (URL, dimensions, and breed data if attached) by its image id.</td></tr><tr><td>Get Random Cat Facts</td><td><code>getRandomFacts</code></td><td>Returns one or more random facts about cats. This is a premium feature of The Cat API and requires an upgraded/paid account; a free API key</td></tr><tr><td>Get Vote by ID</td><td><code>getVoteById</code></td><td>Fetches a single vote record by its id, including the voted-on image.</td></tr><tr><td>List Cat Breeds</td><td><code>listBreeds</code></td><td>Lists all cat breeds with their full profile data, temperament, origin, and physical characteristics, paginated.</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>Lists the image categories (e.g. boxes, hats, sinks) that can be used to filter image search results via category_ids.</td></tr><tr><td>List Favourites</td><td><code>listFavourites</code></td><td>Lists images you have favourited on your account, optionally filtered by sub_id.</td></tr><tr><td>List Votes</td><td><code>listVotes</code></td><td>Lists the votes cast on your account, optionally filtered by sub_id.</td></tr><tr><td>List Your Uploaded Images</td><td><code>listMyImages</code></td><td>Lists images uploaded to your own account via the upload endpoint, optionally paginated and ordered.</td></tr><tr><td>Remove a Breed Tag from an Image</td><td><code>untagImageBreed</code></td><td>Removes a breed tag from one of your own uploaded images. Only you can delete breed tags from your own images.</td></tr><tr><td>Search Breeds</td><td><code>searchBreeds</code></td><td>Searches cat breeds by name, optionally attaching a reference image to each result.</td></tr><tr><td>Search Cat Images</td><td><code>searchImages</code></td><td>Searches for cat images, or returns a random selection if no filters are given. With an API key you can page through approved images in the order they were added using order and page.</td></tr><tr><td>Tag a Breed on an Image</td><td><code>tagImageBreed</code></td><td>Tags a breed onto one of your own uploaded images, for now you can only tag your own images.</td></tr><tr><td>Upload an Image</td><td><code>uploadImage</code></td><td>Uploads a new cat image file to your account. Optionally tag it with breed ids and a sub_id to segment images by your own end users.</td></tr></tbody></table>

</details>

