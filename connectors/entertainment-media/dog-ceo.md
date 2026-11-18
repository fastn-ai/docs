---
description: "Dog CEO's Dog API is a free, open API with 20,000+ dog images from the Stanford Dogs Dataset."
hidden: true
---

# Dog CEO

<img src="../../.gitbook/assets/connectors/lg/dog-ceo.png" alt="Dog CEO logo">

Dog CEO's Dog API is a free, open API with 20,000+ dog images from the Stanford Dogs Dataset. List breeds and sub-breeds, get random images from all dogs, a breed or a sub-breed, or list every image of a breed. No API key needed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [dog.ceo](https://dog.ceo) |
| **Authentication** | No authentication |
| **Slug** | `dogCeo` |

## Use it

Add Dog CEO from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dogCeo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Multiple Random Breed Images | `getRandomBreedImages` | Get several random images of a breed (GET /breed/{breed}/images/random/{count}). Docs: https://dog.ceo/dog-api/documentation/ |
| Get Multiple Random Images | `getRandomImages` | Get several random dog images from all breeds (GET /breeds/image/random/{count}); maximum 50. Docs: https://dog.ceo/dog-api/documentation/ |
| Get Multiple Random Sub-Breed Images | `getRandomSubBreedImages` | Get several random images of a sub-breed (GET /breed/{breed}/{subBreed}/images/random/{count}). Docs: https://dog.ceo/dog-api/documentation/ |
| Get Random Breed Image | `getRandomBreedImage` | Get one random image of a breed (GET /breed/{breed}/images/random). Docs: https://dog.ceo/dog-api/documentation/ |
| Get Random Image | `getRandomImage` | Get one random dog image from all breeds (GET /breeds/image/random). Docs: https://dog.ceo/dog-api/documentation/ |
| Get Random Sub-Breed Image | `getRandomSubBreedImage` | Get one random image of a sub-breed (GET /breed/{breed}/{subBreed}/images/random). Docs: https://dog.ceo/dog-api/documentation/ |
| List All Breeds | `listAllBreeds` | List every main breed with its sub-breeds (GET /breeds/list/all). The message object maps each breed to an array of its sub-breeds. Docs: https://dog.ceo/dog-api/documentation/ |
| List Breed Images | `listBreedImages` | List every image of a breed, including all its sub-breeds (GET /breed/{breed}/images). Unknown breeds return 404 'Breed not found'. Docs: https://dog.ceo/dog-api/documentation/ |
| List Sub-Breed Images | `listSubBreedImages` | List every image of a sub-breed (GET /breed/{breed}/{subBreed}/images). Docs: https://dog.ceo/dog-api/documentation/ |
| List Sub-Breeds | `listSubBreeds` | List the sub-breeds of a main breed (GET /breed/{breed}/list). Breeds with no sub-breeds return an empty list. Docs: https://dog.ceo/dog-api/documentation/ |
