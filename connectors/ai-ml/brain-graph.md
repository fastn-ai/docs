---
description: "BrainGraph is an AI digital brain platform that turns documents, transcripts, web pages, YouTube videos and voice notes into a personal knowledge graph that…"
hidden: true
---

# BrainGraph

<img src="../../.gitbook/assets/connectors/brain-graph.png" alt="BrainGraph logo" width="64">

BrainGraph is an AI digital brain platform that turns documents, transcripts, web pages, YouTube videos and voice notes into a personal knowledge graph that AI agents can query. This connector covers the BrainGraph public API: document ingestion (text, base64 files, web URLs, YouTube, audio URLs), processing status, brains, document library, natural-language search, entity resolution, pattern discovery, document images, answer-graph rendering and async job polling.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [itsbraingraph.ai](https://itsbraingraph.ai) |
| **Authentication** | Credentials you enter |
| **Slug** | `brainGraph` |

## Use it

Add BrainGraph from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.brainGraph.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Document | `deleteDocument` | Permanently deletes an uploaded document (transcript) by id. Only the owner of the document can delete it. |
| Detect Entity Communities | `detectEntityCommunities` | Detects communities of related entities active in a recent time window using label propagation. Returns each community with its size and member entities plus timing statistics. |
| Find Semantic Patterns | `findSemanticPatterns` | Finds semantically similar relationship patterns in the knowledge graph within a time window by clustering path signatures with vector embeddings. Returns each pattern cluster with its signatures, frequency and example paths. |
| Get API Capabilities | `getApiCapabilities` | Returns BrainGraph's machine-readable capability index for AI agents: the available endpoints with their scopes, the scope definitions, upload caps per plan, async job conventions and accepted auth headers. |
| Get Document Images | `getDocumentImages` | Fetches the embedded images (figures, diagrams, screenshots) of one of your documents, identified by document id or a filename substring. Returns one-hour signed URLs that can be fetched and rendered inline. |
| Get Document Progress | `getDocumentProgress` | Returns the ingestion status of an uploaded document. Status moves through queued, processing, syncing and analyzed (or transcribing for audio, failed on error). Once analyzed, the analysis field carries the extraction summary and the document is searchable. |
| Get Job Result | `getJobResult` | Polls an asynchronous agent job (meeting prep, opportunities, content ideas) by its job id and returns its status and result. Results are kept for 30 minutes; poll about every 5 seconds. |
| Get Structural Patterns | `getStructuralPatterns` | Returns the recurring structural patterns discovered in the knowledge graph within a time window, with a plain-language summary and pattern count. |
| Ingest Web Page | `ingestWebPage` | Fetches a public web page (article, blog post or docs page), extracts the main body and ingests it as an HTML document. Paywalled, login-only or JavaScript-only pages are rejected with a 400 without consuming an upload slot. Returns the document id; poll Get Document Progress for completion. Limited to 20 submissions per 5 minutes. |
| Ingest YouTube Video | `ingestYouTubeVideo` | Ingests a YouTube video by URL: BrainGraph fetches the transcript and metadata, resolves speakers and adds it to the brain. Each video is processed once per account and counts against the upload cap. On a fresh ingest BrainGraph streams Server-Sent Events (connected, transcript_created, persisted, queued or error); when the video is already in the brain it returns a JSON record with status exists. |

<details>

<summary>See 7 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Brains | `listBrains` | Lists the separate brains (knowledge sub-graphs) in the account, default brain first, with their ids, names and document counts. Use a brain id with brainIds on search or brainId on uploads to target a specific brain. Accounts without multiple brains enabled receive a 404. |
| List Documents | `listDocuments` | Lists the documents uploaded to the account, newest first, with filename, upload time, ingestion status, source URL and the brain each landed in. Filter by a filename or notes substring with query; this is a library lookup, not a content search. Supports paging with limit and offset. |
| Render Answer Graph Image | `renderAnswerGraphImage` | Renders an answer graph (the nodes, edges and queries returned by Search Brain with includeGraph) to a PNG image. This is a pure renderer over the payload you send; it reads nothing from the brain. Returns the image as base64 with its dimensions. |
| Resolve Entity | `resolveEntity` | Finds a person, company, topic or project in the knowledge graph by exact name and returns its canonical uuid, type, role, organization and summary. Returns found false with reason ambiguous (plus a matches list) or not_found when the name does not resolve to exactly one entity. |
| Search Brain | `searchBrain` | Asks a natural-language question across everything captured in the brain. Returns matching facts with relevance scores and the source and target entities involved. Set includeGraph to true to also receive the entities, relationships and source documents behind the answer. |
| Transcribe Audio URL | `transcribeAudioUrl` | Transcribes an audio recording that lives at a public URL (mp3, m4a, wav, ogg, webm, aac, flac, opus) with speaker diarization and ingests the transcript into the brain. Returns immediately with status transcribing; poll Get Document Progress as it advances to processing and analyzed. A failed transcription refunds the upload slot. |
| Upload Text Document | `uploadTextDocument` | Uploads a document as JSON: plain text in content, or a base64-encoded PDF/DOCX/PPTX/EML/HTML file in pdfBase64 with isPdf set to true. Returns immediately with the document id and status processing; poll Get Document Progress until the status is analyzed. Counts against the plan's upload cap. |

</details>
