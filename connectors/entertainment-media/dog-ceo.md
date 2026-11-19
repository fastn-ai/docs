---
description: "Dog CEO's Dog API is a free, open API with 20,000+ dog images from the Stanford Dogs Dataset."
hidden: true
---

# Dog CEO

<img src="../../.gitbook/assets/connectors/lg/dog-ceo.png" alt="Dog CEO logo">

List breeds and sub-breeds, get random images from all dogs, a breed or a sub-breed, or list every image of a breed. No API key needed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [dog.ceo](https://dog.ceo) |
| **Authentication** | No authentication |
| **Slug** | `dogCeo` |

## Use it

Add Dog CEO from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dogCeo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Multiple Random Breed Images</td><td><code>getRandomBreedImages</code></td><td>Get several random images of a breed (GET /breed/{breed}/images/random/{count}). Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>Get Multiple Random Images</td><td><code>getRandomImages</code></td><td>Get several random dog images from all breeds (GET /breeds/image/random/{count}); maximum 50. Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>Get Multiple Random Sub-Breed Images</td><td><code>getRandomSubBreedImages</code></td><td>Get several random images of a sub-breed (GET /breed/{breed}/{subBreed}/images/random/{count}). Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>Get Random Breed Image</td><td><code>getRandomBreedImage</code></td><td>Get one random image of a breed (GET /breed/{breed}/images/random). Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>Get Random Image</td><td><code>getRandomImage</code></td><td>Get one random dog image from all breeds (GET /breeds/image/random). Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>Get Random Sub-Breed Image</td><td><code>getRandomSubBreedImage</code></td><td>Get one random image of a sub-breed (GET /breed/{breed}/{subBreed}/images/random). Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>List All Breeds</td><td><code>listAllBreeds</code></td><td>List every main breed with its sub-breeds (GET /breeds/list/all). The message object maps each breed to an array of its sub-breeds. Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>List Breed Images</td><td><code>listBreedImages</code></td><td>List every image of a breed, including all its sub-breeds (GET /breed/{breed}/images). Unknown breeds return 404 'Breed not found'. Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>List Sub-Breed Images</td><td><code>listSubBreedImages</code></td><td>List every image of a sub-breed (GET /breed/{breed}/{subBreed}/images). Docs: https://dog.ceo/dog-api/documentation/</td></tr><tr><td>List Sub-Breeds</td><td><code>listSubBreeds</code></td><td>List the sub-breeds of a main breed (GET /breed/{breed}/list). Breeds with no sub-breeds return an empty list. Docs: https://dog.ceo/dog-api/documentation/</td></tr></tbody></table>
