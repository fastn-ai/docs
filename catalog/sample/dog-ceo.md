---
description: "Dog CEO is a free collection of dog images. List breeds and sub-breeds and get random dog images by breed."
hidden: true
---

# Dog CEO

<img src="../../.gitbook/assets/connectors/lg/dog-ceo.png" alt="Dog CEO logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [dog.ceo](https://dog.ceo) |
| **Authentication** | No sign-in needed |
| **Slug** | `dogCeo` |

## Setup

Dog CEO needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Dog CEO from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Dog CEO**.
2. Select **Connect** on the Dog CEO card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Dog CEO needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Dog CEO's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Multiple Random Breed Images</td><td><code>getRandomBreedImages</code></td><td>Get several random images of a breed Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>Get Multiple Random Images</td><td><code>getRandomImages</code></td><td>Get several random dog images from all breeds; maximum 50. Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>Get Multiple Random Sub-Breed Images</td><td><code>getRandomSubBreedImages</code></td><td>Get several random images of a sub-breed Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>Get Random Breed Image</td><td><code>getRandomBreedImage</code></td><td>Get one random image of a breed Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>Get Random Image</td><td><code>getRandomImage</code></td><td>Get one random dog image from all breeds Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>Get Random Sub-Breed Image</td><td><code>getRandomSubBreedImage</code></td><td>Get one random image of a sub-breed Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>List All Breeds</td><td><code>listAllBreeds</code></td><td>List every main breed with its sub-breeds The message object maps each breed to an array of its sub-breeds. Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>List Breed Images</td><td><code>listBreedImages</code></td><td>List every image of a breed, including all its sub-breeds Unknown breeds return 404 'Breed not found'. Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>List Sub-Breed Images</td><td><code>listSubBreedImages</code></td><td>List every image of a sub-breed Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>List Sub-Breeds</td><td><code>listSubBreeds</code></td><td>List the sub-breeds of a main breed Breeds with no sub-breeds return an empty list. Docs: https://dog.ceo/dog-api/documentation/</td></tr></tbody></table>

