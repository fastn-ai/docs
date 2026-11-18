---
description: "The Cat API (\"Cat as a Service\") gives access to thousands of cat images, cat breed data, and, for authenticated users, the ability to upload images, tag…"
---

# The Cat API

The Cat API ("Cat as a Service") gives access to thousands of cat images, cat breed data, and, for authenticated users, the ability to upload images, tag breeds on images, favourite images, and vote on images.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [thecatapi.com](https://thecatapi.com) |
| **Authentication** | API key |
| **Actions** | 23 |
| **Events** | 0 |
| **Slug** | `thecatapi` |

## Use it

Add The Cat API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.thecatapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create a Favourite | `createFavourite` | Marks an image as a favourite on your account, optionally scoped to one of your own end users via sub_id. |
| Create a Vote | `createVote` | Casts an up or down vote on an image, optionally scoped to one of your own end users via sub_id. |
| Delete a Favourite | `deleteFavourite` | Removes a favourite record from your account by id. |
| Delete a Vote | `deleteVote` | Removes a vote record from your account by id. |
| Delete an Image | `deleteImage` | Deletes an image from your account by id. Only works for images you uploaded. |
| Get Breed by ID | `getBreedById` | Fetches full profile data for a single cat breed by its breed id. |
| Get Breeds Tagged on an Image | `getImageBreeds` | Lists the breeds currently tagged on a given image. |
| Get Facts About a Breed | `getBreedFacts` | Returns one or more facts about a given breed. This is a premium feature of The Cat API and requires an upgraded/paid account; a free API key returns a 401 'premium feature' error. |
| Get Favourite by ID | `getFavouriteById` | Fetches a single favourite record by its id, including the favourited image. |
| Get Image Analysis | `getImageAnalysis` | Returns the raw computer-vision analysis results (object/label detections and moderation labels) for a previously uploaded image. |
| Get Image by ID | `getImageById` | Fetches a single cat image's metadata (URL, dimensions, and breed data if attached) by its image id. |
| Get Random Cat Facts | `getRandomFacts` | Returns one or more random facts about cats. This is a premium feature of The Cat API and requires an upgraded/paid account; a free API key returns a 401 'premium feature' error. |
| Get Vote by ID | `getVoteById` | Fetches a single vote record by its id, including the voted-on image. |
| List Cat Breeds | `listBreeds` | Lists all cat breeds with their full profile data, temperament, origin, and physical characteristics, paginated. |
| List Categories | `listCategories` | Lists the image categories (e.g. boxes, hats, sinks) that can be used to filter image search results via category_ids. |
| List Favourites | `listFavourites` | Lists images you have favourited on your account, optionally filtered by sub_id. |
| List Votes | `listVotes` | Lists the votes cast on your account, optionally filtered by sub_id. |
| List Your Uploaded Images | `listMyImages` | Lists images uploaded to your own account via the upload endpoint, optionally paginated and ordered. |
| Remove a Breed Tag from an Image | `untagImageBreed` | Removes a breed tag from one of your own uploaded images. Only you can delete breed tags from your own images. |
| Search Breeds | `searchBreeds` | Searches cat breeds by name, optionally attaching a reference image to each result. |
| Search Cat Images | `searchImages` | Searches for cat images, or returns a random selection if no filters are given. With an API key you can page through approved images in the order they were added using order and page. |
| Tag a Breed on an Image | `tagImageBreed` | Tags a breed onto one of your own uploaded images, for now you can only tag your own images. |
| Upload an Image | `uploadImage` | Uploads a new cat image file to your account. Optionally tag it with breed ids and a sub_id to segment images by your own end users. |
