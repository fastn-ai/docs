---
description: "Dog images, breed data, breed facts, health tips, legislation/breed-ban lookups, favourites, votes, and AI-powered pet analysis (portraits, genealogy, body…"
hidden: true
---

# The Dog API

<img src="../../.gitbook/assets/connectors/thedogapi.png" alt="The Dog API logo" width="64">

Dog images, breed data, breed facts, health tips, legislation/breed-ban lookups, favourites, votes, and AI-powered pet analysis (portraits, genealogy, body condition, age, weight estimation) from TheDogAPI by That API Company - the sister product to The Cat API on the same platform.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [thedogapi.com](https://thedogapi.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `thedogapi` |

## Use it

Add The Dog API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.thedogapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Image Public Request | `cancelImagePublicRequest` | Cancels a pending request to make an uploaded image public. |
| Create Favourite | `createFavourite` | Marks an image as a favourite for the authenticated account, optionally grouped under a custom sub-identifier. |
| Create Image Public Request | `createImagePublicRequest` | Requests that an uploaded image be reviewed and made public in the shared image library. The image must already have passed content review. |
| Create Pet | `createPet` | Creates a pet profile for the authenticated account. Photos can be attached separately afterwards via Upload Pet Images. |
| Create Vote | `createVote` | Casts an upvote or downvote on an image. |
| Delete Favourite | `deleteFavourite` | Removes a favourite by its identifier. |
| Delete Image | `deleteImage` | Deletes an image previously uploaded by the authenticated account. |
| Delete Pet | `deletePet` | Deletes a pet profile and its associated photos and analyses. |
| Generate Body Condition Score | `generateBodyConditionScore` | Uses AI to analyse a pet's uploaded photos and estimate its WSAVA Body Condition Score (1-9). |
| Generate Estimated Age | `generateEstimatedAge` | Uses AI to analyse a pet's uploaded photos and estimate its age. |

<details>

<summary>See 47 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Generate Estimated Weight | `generateEstimatedWeight` | Uses AI to analyse a pet's uploaded photos and estimate its weight and size classification. |
| Generate Genealogy | `generateGenealogy` | Uses AI to analyse all of a pet's uploaded photos and infer its likely breed mix, plus fun creative descriptions. |
| Generate Muscle Condition Score | `generateMuscleConditionScore` | Uses AI to analyse a pet's uploaded photos and flag muscle-wasting risk. |
| Generate Portrait | `generatePortrait` | Generates an AI portrait of a pet in a chosen style, optionally from specific reference photos. |
| Get Account Features | `getAccountFeatures` | Lists the feature flags enabled for the authenticated account, such as analytics access. |
| Get Account Overview | `getAccountOverview` | Retrieves admin-level usage and activity statistics for a given account. Admin only - requires internal admin authorization beyond a standard developer API key. |
| Get Account Quota | `getAccountQuota` | Retrieves the account's current monthly image upload quota, usage, and remaining allowance. |
| Get Breed | `getBreed` | Retrieves full details for a single dog breed by its identifier. |
| Get Breed Bans By Breed | `getBreedBansByBreed` | Retrieves every ban or legislative restriction recorded globally for a specific breed. Requires the account-level banned_breed_endpoints entitlement, which is not included on the free plan. |
| Get Breed Bans By Country | `getBreedBansByCountry` | Retrieves breed-specific legislation and ban details for a given country. Requires the account-level banned_breed_endpoints entitlement, which is not included on the free plan. |
| Get Breed Colours | `getBreedColours` | Lists the registered colour and pattern variants recognized for a specific breed. |
| Get Category | `getCategory` | Retrieves a single image category by its identifier. |
| Get Fact By ID | `getFactById` | Retrieves a single dog fact by its identifier. Not available on the free plan; requires a paid TheDogAPI plan. |
| Get Facts By Breed | `getFactsByBreed` | Lists dog facts specific to a breed. Not available on the free plan; requires a paid TheDogAPI plan. |
| Get Favourite | `getFavourite` | Retrieves a single favourite by its identifier, including the associated image. |
| Get Health Tip By ID | `getHealthTipById` | Retrieves a single health tip by its identifier. Requires the account-level enable_health_tips entitlement, which is not included on the free plan. |
| Get Health Tips By Breed | `getHealthTipsByBreed` | Lists health tips specific to a breed. Requires the account-level enable_health_tips entitlement, which is not included on the free plan. |
| Get Image | `getImage` | Retrieves a single image by its identifier, including tagged breeds, categories, and colours. |
| Get Image Labels | `getImageLabels` | Retrieves the latest AI breed-identification labels generated for an uploaded image. Requires the account-level image analysis entitlement, which is not included on the free plan. |
| Get Image Public Request Status | `getImagePublicRequestStatus` | Retrieves the current status of a public-visibility request for an uploaded image. |
| Get Image Upload Status | `getImageUploadStatus` | Retrieves the content-review and analysis processing status of an uploaded image. |
| Get Pet | `getPet` | Retrieves a single pet profile by its identifier. |
| Get Pet Health Tips | `getPetHealthTips` | Retrieves personalised health tips for a pet, based on its photos and any generated health scores. |
| Get Pet Portraits | `getPetPortraits` | Retrieves only the AI-generated portraits previously created for a pet. |
| Get Random Fact | `getRandomFact` | Retrieves a single random dog fact. Not available on the free plan; requires a paid TheDogAPI plan. |
| Get Random Fact By Breed | `getRandomFactByBreed` | Retrieves a single random fact for a specific breed. Not available on the free plan; requires a paid TheDogAPI plan. |
| Get Random Fact By Species | `getRandomFactBySpecies` | Retrieves a single random fact for a specific species. Not available on the free plan; requires a paid TheDogAPI plan. |
| Get Sub Identifiers | `getSubIds` | Lists the sub-identifiers used in the account with usage counts, useful for tracking per-user or per-app activity. |
| Get Vote | `getVote` | Retrieves a single vote by its identifier. |
| List Breed Ban Countries | `listBreedBanCountries` | Lists the countries that have breed-specific legislation or bans on record. Requires the account-level banned_breed_endpoints entitlement, which is not included on the free plan. |
| List Breed Groups | `listBreedGroups` | Lists the distinct breed group names available (e.g. Toy, Hound, Working), optionally filtered by species. |
| List Breeds | `listBreeds` | Lists dog breeds with their temperament, origin, physical traits, and a reference image. Supports pagination, ordering, and filtering by species, breed group, and extinction status. |
| List Categories | `listCategories` | Lists the image categories (visual tags such as accessories or settings) available on the platform. |
| List Facts | `listFacts` | Lists dog facts with optional filtering by breed, species, and category. Not available on the free plan; requires a paid TheDogAPI plan. |
| List Favourites | `listFavourites` | Lists the images the authenticated account has favourited, with optional filtering by image, sub-identifier, and deletion state. |
| List Health Tips | `listHealthTips` | Lists general dog health tips with optional filtering by breed and species. Requires the account-level enable_health_tips entitlement, which is not included on the free plan. |
| List Pets | `listPets` | Lists the pet profiles registered for the authenticated account, with optional filtering by breed, species, and sub-identifier. |
| List Portrait Styles | `listPortraitStyles` | Lists the AI portrait styles available for generating a pet portrait. |
| List Votes | `listVotes` | Lists the votes cast by the authenticated account, with optional filtering by species, breed group, and sub-identifier. |
| Search Breeds | `searchBreeds` | Searches dog breeds by name, with optional filtering by species and breed group. |
| Search Images | `searchImages` | Searches the public dog image library with extensive filtering by breed, colour, category, age, and sub-identifier. |
| Update Account Quota | `updateAccountQuota` | Updates an account's monthly image upload quota. Admin only - requires internal admin authorization beyond a standard developer API key. |
| Update Pet | `updatePet` | Updates metadata for an existing pet profile. Only the supplied fields are changed. |
| Upload Image | `uploadImage` | Uploads a base64-encoded image for asynchronous content review and breed analysis. Counts against the account's monthly image upload quota. |
| Upload Image Sync | `uploadImageSync` | Uploads a base64-encoded image and waits for content review and breed analysis to complete before returning. Counts against the account's monthly image upload quota. |
| Upload Pet Images | `uploadPetImages` | Uploads additional photos for an existing pet as a multipart file set, optionally tagged with the pet's age and pose at the time. |
| Upload Pet Video | `uploadPetVideo` | Uploads an additional video for an existing pet as a multipart file, optionally tagged with the pet's age at the time. |

</details>
