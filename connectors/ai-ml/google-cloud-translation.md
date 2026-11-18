---
description: "Translate text and documents, detect languages, romanize text, and manage glossaries, custom AutoML models, datasets, Adaptive MT resources and long-running…"
hidden: true
---

# Google Cloud Translation

Translate text and documents, detect languages, romanize text, and manage glossaries, custom AutoML models, datasets, Adaptive MT resources and long-running operations using the Google Cloud Translation API v3.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [translation.googleapis.com](https://translation.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 54 |
| **Events** | 0 |
| **Slug** | `googleCloudTranslation` |

## Use it

Add Google Cloud Translation from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudTranslation.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Translate Document | `batchTranslateDocument` | Starts an asynchronous batch translation of PDF, DOCX, PPTX and XLSX documents stored in Cloud Storage into up to ten target languages, writing the translated documents back to Cloud Storage. Returns a long-running operation to poll. Sends X-Goog-User-Project: {project} so the job is billed to and runs as that project (without it Google answers 400 'Project id is different from the project associated with the request'). |
| Batch Translate Text | `batchTranslateText` | Starts an asynchronous batch translation of plain text, HTML or TSV files stored in Cloud Storage into up to ten target languages, writing results back to Cloud Storage. Returns a long-running operation to poll. Sends X-Goog-User-Project: {project} so the job is billed to and runs as that project (without it Google answers 400 'Project id is different from the project associated with the request'). |
| Cancel Operation | `cancelOperation` | Requests cancellation of a long-running Translation API operation. Cancellation is best effort and is not guaranteed; poll Get Operation afterwards to see whether the operation stopped. |
| Create Adaptive MT Dataset | `createAdaptiveMtDataset` | Creates an Adaptive MT dataset, which holds the reference translations used to adapt translation output to a customer's style and terminology. |
| Create Dataset | `createDataset` | Creates a dataset that will host the sentence pairs used to train a custom AutoML Translation model. Returns a long-running operation. |
| Create Glossary | `createGlossary` | Creates a glossary from a TSV, CSV or TMX file in Cloud Storage. Supply languagePair for a unidirectional glossary or languageCodesSet for an equivalent term set glossary. Returns a long-running operation that completes once the glossary is built. |
| Create Glossary Entry | `createGlossaryEntry` | Adds a single entry to an existing glossary. Supply termsPair for a unidirectional glossary or termsSet for an equivalent term set glossary. |
| Create Model | `createModel` | Starts training a custom AutoML Translation model from an existing dataset. Returns a long-running operation that completes when training has finished. |
| Delete Adaptive MT Dataset | `deleteAdaptiveMtDataset` | Permanently deletes an Adaptive MT dataset and all of the files and sentences it contains. Returns an empty response on success. |
| Delete Adaptive MT File | `deleteAdaptiveMtFile` | Permanently deletes a file and its sentences from an Adaptive MT dataset. Returns an empty response on success. |
| Delete Dataset | `deleteDataset` | Permanently deletes an AutoML Translation dataset and all of its examples. Returns a long-running operation. |
| Delete Glossary | `deleteGlossary` | Permanently deletes a glossary and all of its entries. Returns a long-running operation that completes once the glossary has been removed. |
| Delete Glossary Entry | `deleteGlossaryEntry` | Permanently deletes a single entry from a glossary. Returns an empty response on success. glossaryEntryId is the numeric id Google assigns. |
| Delete Model | `deleteModel` | Permanently deletes a custom AutoML Translation model. Returns a long-running operation that completes once the model has been removed. |
| Delete Operation | `deleteOperation` | Deletes the record of a long-running Translation API operation. This removes the bookkeeping entry only and does not cancel work that is still running. |
| Detect Language | `detectLanguage` | Detects the language of a piece of text or of a document within a specific Google Cloud location. Returns the single most probable language together with a confidence score. |
| Detect Language (Basic v2) | `detectLanguageBasicV2` | Detect the language of text with Cloud Translation - Basic (v2) (POST /language/translate/v2/detect). Docs: https://cloud.google.com/translate/docs/reference/rest/v2/detect |
| Detect Language For Project | `detectLanguageForProject` | Detects the language of a piece of text or of a document using the project-scoped endpoint, which does not require a location to be chosen. |
| Export Dataset Data | `exportDatasetData` | Exports the sentence pairs held in an AutoML Translation dataset to a Cloud Storage directory. Returns a long-running operation. |
| Get Adaptive MT Dataset | `getAdaptiveMtDataset` | Retrieves a single Adaptive MT dataset by its project, location and dataset ID. |
| Get Adaptive MT File | `getAdaptiveMtFile` | Retrieves a single file that was imported into an Adaptive MT dataset, including its entry count. |
| Get Dataset | `getDataset` | Retrieves a single AutoML Translation dataset by its project, location and dataset ID, including its language pair and example counts. |
| Get Glossary | `getGlossary` | Retrieves a single glossary by its project, location and glossary ID, including its language configuration and entry count. |
| Get Glossary Entry | `getGlossaryEntry` | Retrieves a single glossary entry by its project, location, glossary ID and entry ID. glossaryEntryId is the numeric id Google assigns. |
| Get Location | `getLocation` | Retrieves metadata about a single Google Cloud location in which the Translation API is available. |
| Get Model | `getModel` | Retrieves a single custom AutoML Translation model by its project, location and model ID, including its language pair and training statistics. |
| Get Operation | `getOperation` | Retrieves the current state of a long-running Translation API operation. Poll this action to find out whether a batch translation, glossary creation or model training job has finished. |
| Get Supported Languages | `getSupportedLanguages` | Returns the list of languages supported for translation in a given Google Cloud location, indicating for each whether it can be used as a source language, a target language, or both. |
| Get Supported Languages For Project | `getSupportedLanguagesForProject` | Returns the list of languages supported for translation using the project-scoped endpoint, which does not require a location to be chosen. |
| Import Adaptive MT File | `importAdaptiveMtFile` | Imports a file of reference sentences into an Adaptive MT dataset, either from Cloud Storage or supplied inline. Returns the imported file record. |
| Import Dataset Data | `importDatasetData` | Imports sentence pairs from Cloud Storage files into an existing AutoML Translation dataset, optionally assigning each file to the training, validation or test split. Returns a long-running operation. |
| List Adaptive MT Datasets | `listAdaptiveMtDatasets` | Lists the Adaptive MT datasets in a project and location, with optional filtering and paging. |
| List Adaptive MT Files | `listAdaptiveMtFiles` | Lists the files imported into an Adaptive MT dataset, with paging. |
| List Adaptive MT Sentences | `listAdaptiveMtSentences` | Lists every reference sentence held in an Adaptive MT dataset, across all of its files, with paging. |
| List Adaptive MT Sentences By File | `listAdaptiveMtSentencesByFile` | Lists the reference sentences that came from one specific file within an Adaptive MT dataset, with paging. |
| List Dataset Examples | `listDatasetExamples` | Lists the sentence pairs held in an AutoML Translation dataset, with optional filtering by usage split and paging. |
| List Datasets | `listDatasets` | Lists the AutoML Translation datasets in a project and location, with paging. |
| List Glossaries | `listGlossaries` | Lists the glossaries defined in a project and location, with optional filtering and paging. |
| List Glossary Entries | `listGlossaryEntries` | Lists the entries defined in a glossary, with paging. |
| List Languages (Basic v2) | `listLanguagesBasicV2` | List languages supported by Cloud Translation - Basic (v2) (GET /language/translate/v2/languages). Docs: https://cloud.google.com/translate/docs/reference/rest/v2/languages |
| List Locations | `listLocations` | Lists the Google Cloud locations in which the Translation API is available for a project, with optional filtering and paging. |
| List Models | `listModels` | Lists the custom AutoML Translation models in a project and location, with optional filtering and paging. |
| List Operations | `listOperations` | Lists the long-running Translation API operations in a project and location, such as batch translation, glossary creation and model training jobs. |
| Refine Text | `refineText` | Refines existing translations by sending source texts together with their original translations and receiving improved translations back. RefineText is an allow-listed feature; projects without access get 501 'RefineText API is not enabled'. |
| Romanize Text | `romanizeText` | Converts text written in a non-Latin script into its romanized (Latin script) form within a specific Google Cloud location. |
| Romanize Text For Project | `romanizeTextForProject` | Converts text written in a non-Latin script into its romanized form using the project-scoped endpoint, which does not require a location to be chosen. |
| Translate Document | `translateDocument` | Synchronously translates a single PDF, DOCX, PPTX or XLSX document supplied inline or from Cloud Storage, preserving its formatting. Returns the translated document as a byte stream and optionally writes it to Cloud Storage. |
| Translate Text | `translateText` | Translates one or more strings of text into a target language within a specific Google Cloud location. Supports the built-in NMT and Translation LLM models, AutoML custom models, glossaries and transliteration. |
| Translate Text (Basic v2) | `translateTextBasicV2` | Translate text with Cloud Translation - Basic (v2) (POST /language/translate/v2). Docs: https://cloud.google.com/translate/docs/reference/rest/v2/translate |
| Translate Text For Project | `translateTextForProject` | Translates one or more strings of text using the project-scoped endpoint, which does not require a location to be chosen. Use Translate Text instead when a specific regional location, an AutoML model or a glossary is required. |
| Translate With Adaptive MT | `adaptiveMtTranslate` | Translates text using an Adaptive MT dataset so that the output matches the style and terminology of previously supplied reference translations. Optionally accepts inline reference sentence pairs and a glossary. The dataset must hold at least 5 sentence pairs, otherwise Google returns 400 'Dataset has less than 5 sentences'. |
| Update Glossary | `updateGlossary` | Updates the mutable fields of an existing glossary. Only the fields named in updateMask are changed; the API currently supports updating displayName and inputConfig. Returns a long-running operation. |
| Update Glossary Entry | `updateGlossaryEntry` | Updates an existing glossary entry, replacing its terms and description. Supply termsPair for a unidirectional glossary or termsSet for an equivalent term set glossary. glossaryEntryId is the numeric id Google assigns. |
| Wait For Operation | `waitOperation` | Blocks until a long-running Translation API operation completes or the requested timeout elapses, then returns its latest state. This is a best-effort convenience over polling Get Operation. |
