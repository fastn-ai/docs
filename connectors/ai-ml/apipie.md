---
description: "APIpie.ai is a unified gateway to hundreds of AI models from OpenAI, Anthropic, Google, Meta, Mistral and more behind an OpenAI-compatible API."
hidden: true
---

# APIpie.ai

<img src="../../.gitbook/assets/connectors/lg/apipie.png" alt="APIpie.ai logo">

APIpie.ai is a unified gateway to hundreds of AI models from OpenAI, Anthropic, Google, Meta, Mistral and more behind an OpenAI-compatible API. This connector covers the complete APIpie REST API: chat completions with memory, RAG, integrity voting and inline web search, embeddings, image generation, text to speech, audio transcription, the model catalog, usage history, per-app and per-user state settings, web search, AI search answers, web scraping, text anonymization, document parsing, RAG tuning collections, vector collections, file sharing, and the job-search and real-estate data APIs.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [apipie.ai](https://apipie.ai) |
| **Authentication** | Bearer token |
| **Slug** | `apipie` |

## Use it

Add APIpie.ai from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.apipie.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Document to RAG Collection | `addDocumentToRagCollection` | Downloads a document (PDF, DOC, DOCX, TXT, CSV, XLS or XLSX) from a URL, extracts its content and stores embeddings in a RAG tuning collection that chat completions can use through the rag_tune parameter. The collection is created on first use. |
| Anonymize Text | `anonymizeText` | Detects personally identifiable information in text with Microsoft Presidio and replaces each entity with a truncated SHA-256 hash, returning the anonymized text together with a mapping from original values to replacements so results can be re-identified later. |
| Answer with Search | `answerWithSearch` | Generates an AI-written answer to a question grounded in live search results from the Valyu provider, returning the answer with its sources and usage. Supports web, news, proprietary or combined search, source whitelists, blacklists and biases, time ranges and custom system instructions. |
| Create Chat Completion | `createChatCompletion` | Sends a chat conversation to any language or vision model available through APIpie and returns the completion in OpenAI format, with usage, cost and latency. Supports provider routing, integrated memory, RAG tuning collections, inline web search with whitelists, tool calling, integrity voting and streaming. Up to five comma-separated models return an array of responses. Charges credits. |
| Create Embeddings | `createEmbeddings` | Generates an embedding vector for the given input text using the specified embedding model (see List Models with type embedding). Optionally set the encoding format and, for OpenAI models, the number of dimensions. Charges credits. |
| Create Speech | `createSpeech` | Converts text to speech with the specified provider, model and voice (list voices with List Models and the voices parameter) and returns the audio file, e.g. MP3, with usage details in the response headers. Supports ElevenLabs voice settings and OpenAI speed and format options. Charges credits. |
| Create Vector Collection | `createVectorCollection` | Creates a new vector collection on Pinecone or Qdrant with the given embedding dimension, for storing and querying your own embeddings or for use as a RAG tuning source in chat completions. |
| Delete RAG Collection | `deleteRagCollection` | Deletes an entire RAG tuning collection, or only specific records in it by id or metadata filter. |
| Delete State Settings | `deleteStateSettings` | Deletes stored state records. With user it deletes that end-user's state record; without user it deletes all state records for the current API key (app-level and every user). Use Update State Settings with delete for partial key removal instead. |
| Delete Vectors | `deleteVectors` | Deletes specific vectors from a collection by id or metadata filter, or the entire collection when delete_all is true. |

<details>

<summary>See 22 more actions</summary>

* **Fetch Vectors** `fetchVectors`: Fetches specific vectors from a collection by id, returning each vector's stored values and metadata (data and metatag).
* **Generate Image** `generateImage`: Generates an image from a text prompt using an image model available through APIpie (DALL-E, Flux, Stable Diffusion, Leonardo and more; see List Models with type image), returning the image URL or base64 data. Model-specific options such as size, quality, style, seed, steps, LoRAs, strength and aspect ratio apply only where the chosen model supports them. Charges credits.
* **Get Property by Address** `getPropertyByAddress`: Looks up detailed property information for a full street address, including price, estimates, size, status, listing details and photos.
* **Get State Settings** `getStateSettings`: Returns the stored state settings that are applied to chat completions by default. Without parameters it returns the app-level state for the API key; pass user to read a specific end-user's state, or app_name to target a named app.
* **List Detailed Models** `listDetailedModels`: Returns the model catalog with extended metadata: input and output modalities, pool, quantization, benchmark scores, per-prompt limits, capability flags and pricing. Filter by type, provider or model name.
* **List Models** `listModels`: Returns the catalog of models available through APIpie with type, subtype, provider, route, token limits, pricing, average cost, latency and availability. Filter by type, subtype, provider, combination or enabled state. Pass voices to list available text-to-speech voices, or restrictions to list country restrictions, without any other filter.
* **List Query History** `listQueryHistory`: Returns the history of API queries made with your account, newest first, as raw records or hourly, daily or weekly aggregates, with provider, model, token counts, cost and latency. Filter by user, app (API key name), provider or route and page with limit and offset.
* **List RAG Collections** `listRagCollections`: Lists the RAG tuning collections associated with the API key, optionally for a specific vector provider.
* **List Vector Collections** `listVectorCollections`: Lists the vector collections owned by the API key, with their provider and dimension.
* **List Vector IDs** `listVectorIds`: Lists the vector ids stored in a collection, optionally filtered by id prefix and paginated with a limit and pagination token.
* **Parse Document** `parseDocument`: Extracts metadata and text content from an uploaded document (PDF, DOC, DOCX, PPT, PPTX, XLS, XLSX, TXT, RTF, ODT, ODP, ODS, EPUB, HTML or XML) using Apache Tika. The file is sent as multipart form data.
* **Query Vectors** `queryVectors`: Finds the vectors most similar to a query embedding in a collection, optionally filtered by metadata or metatag, returning the top matches with their scores and, on request, values and metadata.
* **Scrape Web Page** `scrapeWebPage`: Scrapes a web page through Bright Data or Valyu and returns either the raw HTML or parsed content (title, text, excerpt and links), optionally rendering JavaScript first and limiting the extracted length.
* **Search Jobs** `searchJobs`: Searches job postings from a free-form query (ideally including a job title and location), with filters for country, language, posting date, remote work, employment type, requirements, radius and publishers, returning up to 10 jobs per page.
* **Search Real Estate by Coordinates** `searchRealEstateByCoordinates`: Searches property listings within a circular area defined by latitude, longitude and diameter in miles, with the same status, type, price, size, listing-type and HOA filters as the location search, returning up to 41 properties per page.
* **Search Real Estate by Location** `searchRealEstateByLocation`: Searches property listings in a county, neighbourhood or zip code with filters for status (for sale, for rent, recently sold), type, price, monthly payment, bedrooms, bathrooms, size, lot size, listing type, sale flags and HOA fees, returning up to 41 properties per page.
* **Search Real Estate by Polygon** `searchRealEstateByPolygon`: Searches property listings inside a polygon given as a coordinates string, with the same status, type, price, size, listing-type and HOA filters as the location search, returning up to 41 properties per page.
* **Search Web** `searchWeb`: Performs a web search through Google or Valyu and returns ranked results with URL, title, description and, for Valyu, extracted page content. Supports localisation, result count, safe search, source whitelists and blacklists, date ranges, reranking instructions and relevance thresholds.
* **Transcribe Audio** `transcribeAudio`: Transcribes an uploaded audio file (max 25 MB, multipart form data) to text with whisper-1, gpt-4o-transcribe or gpt-4o-mini-transcribe, optionally with a guiding prompt, language, temperature, output format and word or segment timestamps. Charges credits.
* **Update State Settings** `updateStateSettings`: Creates or merges the stored state settings that are applied to chat completions by default, at app level or, with enable_user_states and user, per end-user. Only the settings keys you send are changed; list keys in delete to remove them. Returns the resulting state.
* **Upload File for URL** `uploadFileForUrl`: Uploads an image file (PNG, JPG, JPEG, SVG, GIF, BMP, TIF, TIFF or WebP) as multipart form data and returns a shareable URL that can be passed to vision models and other APIpie endpoints.
* **Upsert Vector** `upsertVector`: Inserts or updates a single vector in a collection, storing the embedding together with its text payload and an optional metadata tag. The embedding length must match the collection's dimension.

</details>
