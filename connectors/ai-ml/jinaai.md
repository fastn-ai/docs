---
description: "Jina AI search-foundation and frontier APIs: Embeddings, Reranker, Classifier, Segmenter, Reader (URL to LLM-friendly text), Search (web search), DeepSearch…"
hidden: true
---

# Jina AI

Jina AI search-foundation and frontier APIs: Embeddings, Reranker, Classifier, Segmenter, Reader (URL to LLM-friendly text), Search (web search), DeepSearch (OpenAI-compatible reasoning search), and Grounding/Factcheck. Auth via Bearer API key from jina.ai/api-dashboard.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [jina.ai](https://jina.ai) |
| **Authentication** | Bearer token |
| **Actions** | 10 |
| **Events** | 0 |
| **Slug** | `jinaai` |

## Use it

Add Jina AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.jinaai.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Classify (Few-Shot) | `classifyFewShot` | Few-shot classification using a previously trained classifier via api.jina.ai/v1/classify. Send input + classifier_id (no model, no labels). Train the classifier first with Train Classifier to obtain classifier_id. Base host: https://api.jina.ai. |
| Classify (Zero-Shot) | `classifyZeroShot` | Zero-shot classification of text/images against candidate labels via api.jina.ai/v1/classify. Send model + input + labels (no training). Up to 256 classes, up to 1024 inputs. Cheapest text model: 'jina-embeddings-v3'; use 'jina-clip-v2' or 'jina-embeddings-v4' for images. Base host: https://api.jina.ai. |
| Create Embeddings | `createEmbeddings` | Convert text and/or images into embedding vectors via api.jina.ai/v1/embeddings. Cheapest validation path: model 'jina-embeddings-v3' with a tiny single-string input (lowest credit cost). Use 'retrieval.passage' task for indexing and 'retrieval.query' for queries. Multimodal input objects ({text}/{image}) require jina-embeddings-v4, jina-clip-v2, or jina-clip-v1. Base host: https://api.jina.ai. |
| DeepSearch | `deepSearch` | OpenAI-compatible deep reasoning search: iteratively searches, reads, and reasons until it answers via deepsearch.jina.ai/v1/chat/completions. Model 'jina-deepsearch-v1'. Long-running (avg ~57s); set stream=false for a single JSON response. Higher credit cost than embeddings/segment. Base host: https://deepsearch.jina.ai. |
| Ground Statement (Factcheck) | `groundStatement` | Fact-check a statement by grounding it against real-time web search via g.jina.ai. Returns a factuality score, boolean verdict, reasoning, and supporting/contradicting references. ~300K tokens per request (higher cost). Optionally restrict grounding to provided reference URLs. Base host: https://g.jina.ai. |
| Read URL | `readUrl` | Read/convert a URL to clean LLM-friendly text (markdown by default) via r.jina.ai. Set Accept: application/json (configured) for the structured envelope. Optional X-* option headers control engine, selectors, link/image summaries, and output format. Base host: https://r.jina.ai. |
| Rerank Documents | `rerankDocuments` | Rerank a list of documents by relevance to a query via api.jina.ai/v1/rerank. Cheapest model: 'jina-reranker-v2-base-multilingual'. For multimodal query/documents ({text}/{image}) use 'jina-reranker-m0'. Base host: https://api.jina.ai. |
| Search Web | `searchWeb` | Web search returning LLM-friendly results, each Reader-extracted, via s.jina.ai. Set Accept: application/json (configured) for the structured envelope. Use X-Respond-With: no-content to get SERP metadata only (cheaper, no per-page fetch). Base host: https://s.jina.ai. |
| Segment Text | `segmentText` | Tokenize and/or chunk text into semantically meaningful segments via api.jina.ai/v1/segment. Free endpoint (usage.tokens reports 0) - ideal for zero/low-cost validation. Base host: https://api.jina.ai. |
| Train Classifier (Few-Shot) | `trainClassifier` | Train/update a few-shot classifier with labeled examples via api.jina.ai/v1/train. Returns a classifier_id to use with Classify (Few-Shot). Call repeatedly to add examples/classes (max 16 classes / 16 classifiers). Base host: https://api.jina.ai. |
