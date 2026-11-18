---
description: "Eden AI is a unified AI gateway giving access to 500+ models from 50+ providers through one API."
hidden: true
---

# Eden AI

<img src="../../.gitbook/assets/connectors/eden-ai.png" alt="Eden AI logo" width="64">

Eden AI is a unified AI gateway giving access to 500+ models from 50+ providers through one API. This connector covers the full Eden AI v3 API: OpenAI-compatible chat completions, responses, embeddings, moderation, Anthropic messages, image generation and editing, audio transcription and speech, video generation, the Universal AI expert-model endpoint (text analysis, web scraping and search, OCR and document parsing, image analysis, translation, text-to-speech) with typed actions per feature, asynchronous jobs, collections, file uploads, model and feature catalogs, and the organization Management API (API keys, management keys, members, groups and usage).

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [edenai.co](https://edenai.co) |
| **Authentication** | Bearer token |
| **Slug** | `edenAi` |

## Use it

Add Eden AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.edenAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Collection Item | `addCollectionItem` | Adds a file (upload file id or URL) to a collection; the file is indexed on the collection's provider and the provider-side item ids are returned (one image can yield several faces). |
| Anonymize Image | `anonymizeImage` | Blurs faces and license plates in an image and returns the anonymized image with the detected regions. Runs the image/anonymization expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Batch Scrape Web Pages | `batchScrapeWebPages` | Starts an asynchronous scrape of several URLs; returns a job id to poll with Get Async Job. Runs the web/batch_scrape_async expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Check Spelling | `checkSpelling` | Detects spelling and grammar mistakes in a text and suggests corrections. Runs the text/spell_check expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Compare Faces | `compareFaces` | Compares the faces found in two images and returns similarity confidences with bounding boxes. Runs the image/face_compare expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Convert Text To Speech | `convertTextToSpeech` | Synthesizes speech audio from text with an expert text-to-speech model and returns an audio URL. Runs the audio/tts expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Count Anthropic Tokens | `countAnthropicTokens` | Counts the input tokens an Anthropic-format request would consume without running the model. |
| Crawl Website | `crawlWebsite` | Starts an asynchronous crawl of a website and its linked pages; returns a job id to poll with Get Async Job. Runs the web/crawl_async expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Create Anthropic Message | `createAnthropicMessage` | Creates a message using the Anthropic Messages API shape (native pass-through), with provider routing and fallbacks. Consumes AI credit. |
| Create API Key | `createApiKey` | Creates a new API key for the organization, optionally attributed to a member and with spending controls. The secret is returned only once. Requires a Management Key connection (manage:write). |

<details>

<summary>See 85 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Async Job | `createAsyncJob` | Creates an asynchronous expert-model job (speech-to-text, multipage OCR, table extraction, web crawl, batch scrape, structured extraction, deep research, video generation, video deepfake detection). Returns a job id to poll with Get Async Job; optionally notifies a webhook URL on completion. Typed per-feature actions are also available. |
| Create Audio Transcription | `createAudioTranscription` | Transcribes audio referenced by an upload file id or URL into text using an OpenAI-compatible speech-to-text model. Consumes AI credit. |
| Create Chat Completion | `createChatCompletion` | Creates an OpenAI-compatible chat completion with any of the 500+ LLMs available through Eden AI, with provider routing, fallbacks, tools, structured output and prompt caching. Consumes AI credit. |
| Create Collection | `createCollection` | Creates a provider-bound collection (for example image/face_recognition/amazon) used to index items for recognition features. Returns the collection id to use in item operations and inference calls. |
| Create Embeddings | `createEmbeddings` | Creates vector embeddings for text input using an OpenAI-compatible embeddings model. Consumes AI credit. |
| Create Management Key | `createManagementKey` | Creates a management key with manage:read and/or manage:write scopes so an automated system can manage the organization. The secret is returned only once. Requires a Management Key connection with the manage:mint scope. |
| Create Moderation | `createModeration` | Classifies text or multimodal content for harmful categories using an OpenAI-compatible moderation model. |
| Create Response | `createResponse` | Creates a model response using the OpenAI Responses API shape, supporting multi-turn conversations via previous_response_id, tools and background execution. Consumes AI credit. |
| Create Speech | `createSpeech` | Synthesizes text into speech audio with an OpenAI-compatible text-to-speech model and returns the raw audio bytes (cost and provider are reported in x-edenai-* response headers). Consumes AI credit. |
| Create Video | `createVideo` | Starts an asynchronous video generation job from a prompt and optional reference image. Poll Retrieve Video until the status is completed, then use Download Video Content. Consumes AI credit. |
| Delete All Files | `deleteAllFiles` | Permanently deletes every uploaded file of the caller. This cannot be undone. |
| Delete Async Job | `deleteAsyncJob` | Deletes a finished asynchronous expert-model job by id. Jobs still processing cannot be deleted (409). |
| Delete Collection | `deleteCollection` | Deletes a collection by id on the provider and in Eden AI. Idempotent: a collection already gone on the provider still has its record removed. |
| Delete Collection Item | `deleteCollectionItem` | Deletes one item from a collection by its provider-side item id. |
| Delete Files By Ids | `deleteFilesByIds` | Permanently deletes the uploaded files with the given ids (1-100). Files that do not exist or are not owned by the caller are ignored. |
| Delete Response | `deleteResponse` | Deletes a stored model response by its id. |
| Delete Video | `deleteVideo` | Deletes a finished video generation job by id. Jobs still in progress cannot be deleted. |
| Detect AI Generated Image | `detectAiGeneratedImage` | Estimates whether an image was generated by AI. Runs the image/ai_detection expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Detect AI Generated Text | `detectAiGeneratedText` | Estimates whether a text was written by an AI model. Runs the text/ai_detection expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Detect Explicit Content | `detectExplicitContent` | Detects explicit, adult or violent content in an image and returns per-category likelihoods. Runs the image/explicit_content expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Detect Faces | `detectFaces` | Detects faces in an image with landmarks, attributes (emotions, age, accessories) and bounding boxes. Runs the image/face_detection expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Detect Image Deepfake | `detectImageDeepfake` | Estimates whether an image is a deepfake. Runs the image/deepfake_detection expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Detect Logos | `detectLogos` | Detects brand logos in an image with confidence scores and bounding polygons. Runs the image/logo_detection expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Detect Objects | `detectObjects` | Detects objects in an image with labels, confidence and bounding boxes. Runs the image/object_detection expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Detect Plagiarism | `detectPlagiarism` | Checks a text for plagiarism against web sources. Runs the text/plagia_detection expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Detect Video Deepfake | `detectVideoDeepfake` | Starts an asynchronous deepfake-detection job on a video; returns a job id to poll with Get Async Job. Runs the video/deepfake_detection_async expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Download Video Content | `downloadVideoContent` | Downloads the finished MP4 of a completed video generation job (redirects to the file while its link is valid, otherwise streams the bytes). |
| Edit Images | `editImages` | Edits one or more input images (referenced by upload file id or URL) according to a prompt, with an optional mask. Consumes AI credit. |
| Extract Structured Web Data | `extractStructuredWebData` | Starts an asynchronous structured-data extraction from web pages using a prompt and/or JSON schema; returns a job id to poll with Get Async Job. Runs the web/structured_extraction_async expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Extract Tables From Document | `extractTablesFromDocument` | Starts an asynchronous table extraction job on a PDF or image document; returns a job id to poll with Get Async Job. Runs the ocr/ocr_tables_async expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Extract Text From Document | `extractTextFromDocument` | Starts an asynchronous multipage OCR job on a PDF or image document; returns a job id to poll with Get Async Job. Runs the ocr/ocr_async expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Extract Text From Image | `extractTextFromImage` | Runs OCR on an image or single-page document and returns the detected text with bounding boxes. Runs the ocr/ocr expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Extract Topics | `extractTopics` | Extracts the main topics discussed in a text. Runs the text/topic_extraction expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Generate Image | `generateImage` | Generates one or more images from a text prompt with an expert image model, optionally guided by reference images and a mask. Runs the image/generation expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Generate Images | `generateImages` | Generates images from a text prompt using an OpenAI-compatible image model (provider/model). Consumes AI credit. |
| Generate Video | `generateVideo` | Starts an asynchronous video generation job from a text prompt and optional reference image; returns a job id to poll with Get Async Job. Runs the video/generation_async expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Get API Key Usage | `getApiKeyUsage` | Returns the consumption of one API key over a date window as a time series at the requested granularity, optionally narrowed by feature, subfeature, provider or phase. Requires a Management Key connection (manage:read). |
| Get Async Job | `getAsyncJob` | Retrieves the status and output of an asynchronous expert-model job by id. |
| Get Collection | `getCollection` | Retrieves one of the caller collections by id. |
| Get Feature Info | `getFeatureInfo` | Returns the detailed contract of one feature/subfeature: endpoints, input schema, output schema and the providers and models that serve it, with pricing. |
| Get Organization Usage | `getOrganizationUsage` | Returns the organization aggregated consumption over a date window as a time series per API key, or one total per member with group_by=user; narrow by feature, subfeature, provider, phase, member or key. Requires a Management Key connection (manage:read). |
| Inspect Management Key | `inspectManagementKey` | Returns the organization, scopes and expiry of the management key used for the request. A convenient connectivity check; requires a connection made with a Management Key. |
| List API Keys | `listApiKeys` | Lists every API key of the organization, including revoked ones (revoked: true). Secrets are never returned; use masked to identify a key. Requires a Management Key connection (manage:read). |
| List Async Jobs | `listAsyncJobs` | Lists the caller asynchronous expert-model jobs with optional feature, subfeature and status filters and pagination. |
| List Collection Items | `listCollectionItems` | Lists the provider-side item ids stored in a collection (live from the provider). |
| List Collections | `listCollections` | Lists the caller collections with optional model filter and pagination. |
| List Embeddings Models | `listEmbeddingsModels` | Lists the embeddings models available to the caller, with capabilities and pricing. |
| List Features | `listFeatures` | Lists every expert-model feature (text, web, ocr, image, translation, audio, video) with its subfeatures, execution mode and available provider models. |
| List Files | `listFiles` | Lists the caller uploaded, non-expired files, newest first, with optional purpose filter and pagination. |
| List Groups | `listGroups` | Lists the organization groups synced from the identity provider (directory sync), ordered by name, with their active member emails. Requires a Management Key connection (manage:read). |
| List Image Models | `listImageModels` | Lists the image generation and editing models available in the caller region, with capabilities and pricing. |
| List Management Keys | `listManagementKeys` | Lists the organization management keys, newest first, including revoked ones. Secrets are never returned. Requires a Management Key connection with the manage:mint scope. |
| List Members | `listMembers` | Lists the organization active members, including the owner, with role, rate limits, directory groups and API keys. Requires a Management Key connection (manage:read). |
| List Models | `listModels` | Lists every LLM model available through Eden AI with capabilities, context length, pricing and regions. |
| List Moderation Models | `listModerationModels` | Lists the moderation models available to the caller, with capabilities and pricing. |
| List Speech Models | `listSpeechModels` | Lists the text-to-speech models available in the caller region, with capabilities and pricing. |
| List Subfeatures | `listSubfeatures` | Lists the subfeatures of one expert-model feature (for example text, image, ocr or translation) with their execution mode and available provider models. |
| List Transcription Models | `listTranscriptionModels` | Lists the speech-to-text models available in the caller region, with capabilities and pricing. |
| List Video Models | `listVideoModels` | Lists the video generation models available in the caller region, with pricing. Each id is the provider/model value to pass to Create Video. |
| List Videos | `listVideos` | Lists the caller video generation jobs, newest first, with cursor pagination. |
| Map Website | `mapWebsite` | Discovers the URLs of a website (site map). Runs the web/map expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Moderate Text | `moderateText` | Scans text for offensive, hateful, sexual, violent or otherwise harmful content and returns per-category likelihoods. Runs the text/moderation expert-model feature; consumes AI credit according to the chosen provider's pricing (text/moderation/openai is free). |
| Parse Financial Document | `parseFinancialDocument` | Extracts structured fields (customer and merchant information, totals, taxes, line items, dates) from an invoice or receipt. Runs the ocr/financial_parser expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Parse Identity Document | `parseIdentityDocument` | Extracts structured fields (names, birth date, document id, dates, address, MRZ) from an identity document such as an ID card, passport or driving licence. Runs the ocr/identity_parser expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Parse Resume | `parseResume` | Extracts structured fields (personal information, work experience, education, skills, languages, certifications) from a resume. Runs the ocr/resume_parser expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Recognize Faces | `recognizeFaces` | Searches a face-recognition collection for the faces found in an image and returns matching face ids with confidence. Runs the image/face_recognition expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Recognize Named Entities | `recognizeNamedEntities` | Extracts named entities (people, organizations, places, dates and more) from a text. Runs the text/named_entity_recognition expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Remove Image Background | `removeImageBackground` | Removes the background from an image and returns the result as base64 and a URL. Runs the image/background_removal expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Retrieve API Key | `retrieveApiKey` | Returns one API key of the organization by id (secret never included). Requires a Management Key connection (manage:read). |
| Retrieve Group | `retrieveGroup` | Returns one directory-synced group of the organization by its identity-provider id, with its active member emails. Requires a Management Key connection (manage:read). |
| Retrieve Response | `retrieveResponse` | Retrieves a stored model response by its id. |
| Retrieve Video | `retrieveVideo` | Retrieves a video generation job by id; poll until status is completed or failed. |
| Revoke API Key | `revokeApiKey` | Permanently revokes an API key; it stops authenticating immediately and stays listed with revoked: true. Requires a Management Key connection (manage:write). |
| Revoke Management Key | `revokeManagementKey` | Permanently revokes a manage:read/manage:write management key of the organization. Keys with the manage:mint scope cannot be revoked here. Requires a Management Key connection with the manage:mint scope. |
| Rotate API Key | `rotateApiKey` | Replaces the secret of an API key while keeping its identity, name, budget and settings. The previous secret stops working immediately; the new one is returned only once. Requires a Management Key connection (manage:write). |
| Run Deep Research | `runDeepResearch` | Starts an asynchronous deep-research task that searches the web and synthesizes an answer with sources; returns a job id to poll with Get Async Job. Runs the web/research_async expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Run Universal AI | `runUniversalAi` | Runs any synchronous expert-model feature (text analysis, web scraping and search, OCR and document parsing, image analysis and generation, translation, text-to-speech) through the Universal AI endpoint. Set model to feature/subfeature/provider[/model] and pass the feature-specific fields in input; use Get Feature Info to discover them. Typed per-feature actions are also available. |
| Scrape Web Page | `scrapeWebPage` | Scrapes a web page and returns its content as LLM-ready text with title, links and images. Runs the web/scraping expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Search Web | `searchWeb` | Performs a web search and returns ranked results with content, and an answer with sources where the provider supports it. Runs the web/search expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Set Member Role | `setMemberRole` | Assigns a role (by role id) to an organization member identified by email and returns the updated member. Role-based access control must be enabled for the organization. Requires a Management Key connection (manage:write). |
| Transcribe Audio | `transcribeAudio` | Starts an asynchronous speech-to-text job on an audio or video file with optional speaker diarization; returns a job id to poll with Get Async Job. Runs the audio/speech_to_text_async expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Translate Document | `translateDocument` | Translates a document (PDF, DOCX, PPTX) into a target language and returns the translated file. Runs the translation/document_translation expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Translate Text | `translateText` | Translates text into a target language. Runs the translation/automatic_translation expert-model feature; consumes AI credit according to the chosen provider's pricing. |
| Update API Key | `updateApiKey` | Updates the display name and spending controls of an API key; only the fields you send are changed. The environment (token_type) cannot be changed. Requires a Management Key connection (manage:write). |
| Upload File | `uploadFile` | Uploads a file (multipart form-data) for persistent storage of up to 30 days and returns a file id usable in expert-model, image edit, transcription and collection calls. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Async Job Completed | `async_job_completed` | Sent by Eden AI when an asynchronous Universal AI job (speech-to-text, multipage OCR, table extraction, web crawl/batch scrape/structured extraction/deep research, video generation, video deepfake detection) finishes with status success or fail. Eden AI has no webhook registration API: pass this trigger's webhook URL as webhook_receiver (and optionally user_webhook_parameters for correlation) in Create Async Job or any typed async action such as Transcribe Audio, Extract Text From Document or Crawl Website. Each delivery is a JSON POST with headers X-Edenai-Webhook: true, X-Edenai-Signature (RSA PKCS1 v1.5 / SHA-256 hex signature of the canonical JSON body, verified with the public key obtained from Eden AI support) and X-Edenai-Hash-Algorithm: SHA256. RSA signature verification is not expressible in fastn's HMAC verification, so it is left unset here; verify downstream if required. Payload shape modelled from the official webhook documentation (https://www.edenai.co/docs/v3/expert-models/webhooks) because job creation is credit-gated on the test account. |
