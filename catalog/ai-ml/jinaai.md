---
description: "Jina AI provides search and language tools. Create embeddings, rerank and classify text, split text into chunks, read web pages and search the web."
hidden: true
---

# Jina AI

<img src="../../.gitbook/assets/connectors/lg/jinaai.png" alt="Jina AI logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [jina.ai](https://jina.ai) |
| **Authentication** | Access token |
| **Slug** | `jinaai` |

## Setup

Your customers enter their access token for Jina AI when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Jina AI from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Jina AI**.
2. Select **Connect** on the Jina AI card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Jina AI's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Classify (Few-Shot)</td><td><code>classifyFewShot</code></td><td>Few-shot classification using a previously trained classifier via api.jina.ai/v1/classify. Send input + classifier_id (no model, no labels). Train the classifier first with Train Classifier to obtain classifier_id. Base host: https://api.jina.ai.</td></tr><tr><td>Classify (Zero-Shot)</td><td><code>classifyZeroShot</code></td><td>Zero-shot classification of text/images against candidate labels via api.jina.ai/v1/classify. Send model + input + labels (no training). Up to 256 classes, up to 1024 inputs. Cheapest text model: 'jina-embeddings-v3'; use 'jina-clip-v2' or 'jina-embeddings-v4' for images. Base host: https://api.jina.ai.</td></tr><tr><td>Create Embeddings</td><td><code>createEmbeddings</code></td><td>Convert text and/or images into embedding vectors via api.jina.ai/v1/embeddings. Cheapest validation path: model 'jina-embeddings-v3' with a tiny single-string input (lowest credit cost). Use 'retrieval.passage' task for indexing and 'retrieval.query' for queries. Multimodal input objects ({text}/{image}) require jina-embeddings-v4, jina-clip-v2, or jina-clip-v1. Base host: https://api.jina.ai.</td></tr><tr><td>DeepSearch</td><td><code>deepSearch</code></td><td>OpenAI-compatible deep reasoning search: iteratively searches, reads, and reasons until it answers via deepsearch.jina.ai/v1/chat/completions. Model 'jina-deepsearch-v1'. Long-running (avg ~57s); set stream=false for a single JSON response. Higher credit cost than embeddings/segment. Base host: https://deepsearch.jina.ai.</td></tr><tr><td>Ground Statement (Factcheck)</td><td><code>groundStatement</code></td><td>Fact-check a statement by grounding it against real-time web search via g.jina.ai. Returns a factuality score, boolean verdict, reasoning, and supporting/contradicting references. ~300K tokens per request (higher cost). Optionally restrict grounding to provided reference URLs. Base host: https://g.jina.ai.</td></tr><tr><td>Read URL</td><td><code>readUrl</code></td><td>Read/convert a URL to clean LLM-friendly text (markdown by default) via r.jina.ai. Set Accept: application/json (configured) for the structured envelope. Optional X-* option headers control engine, selectors, link/image summaries, and output format. Base host: https://r.jina.ai.</td></tr><tr><td>Rerank Documents</td><td><code>rerankDocuments</code></td><td>Rerank a list of documents by relevance to a query via api.jina.ai/v1/rerank. Cheapest model: 'jina-reranker-v2-base-multilingual'. For multimodal query/documents ({text}/{image}) use 'jina-reranker-m0'. Base host: https://api.jina.ai.</td></tr><tr><td>Search Web</td><td><code>searchWeb</code></td><td>Web search returning LLM-friendly results, each Reader-extracted, via s.jina.ai. Set Accept: application/json (configured) for the structured envelope. Use X-Respond-With: no-content to get SERP metadata only (cheaper, no per-page fetch). Base host: https://s.jina.ai.</td></tr><tr><td>Segment Text</td><td><code>segmentText</code></td><td>Tokenize and/or chunk text into semantically meaningful segments via api.jina.ai/v1/segment. Free endpoint (usage.tokens reports 0) - ideal for zero/low-cost validation. Base host: https://api.jina.ai.</td></tr><tr><td>Train Classifier (Few-Shot)</td><td><code>trainClassifier</code></td><td>Train/update a few-shot classifier with labeled examples via api.jina.ai/v1/train. Returns a classifier_id to use with Classify (Few-Shot). Call repeatedly to add examples/classes (max 16 classes / 16 classifiers). Base host: https://api.jina.ai.</td></tr></tbody></table>

