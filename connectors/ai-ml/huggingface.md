---
description: "Hugging Face connector covering the Hub API (whoami, models, datasets, spaces, repos, refs, commits) and Inference Providers router (OpenAI-compatible chat…"
hidden: true
---

# Hugging Face

Hugging Face connector covering the Hub API (whoami, models, datasets, spaces, repos, refs, commits) and Inference Providers router (OpenAI-compatible chat completions, feature-extraction embeddings). Auth: bearer hf_ token.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [huggingface.co](https://huggingface.co) |
| **Authentication** | Bearer token |
| **Actions** | 14 |
| **Events** | 0 |
| **Slug** | `huggingface` |

## Use it

Add Hugging Face from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.huggingface.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Chat Completions | `chatCompletions` | OpenAI-compatible chat completion via the Inference Providers router. INCURS CREDITS. Body: required model + messages only. |
| Create Repo | `createRepo` | Create a new model, dataset, or space repository. Body: required name + type only (optional organization/private/sdk omitted by default). |
| Delete Repo | `deleteRepo` | Delete a model, dataset, or space repository. Body: required name + type only. |
| Feature Extraction (Embeddings) | `featureExtraction` | Generate embeddings for text via the hf-inference router feature-extraction pipeline. INCURS CREDITS. Body: required inputs; model id in the path. |
| Get Dataset | `getDataset` | Get metadata for a single dataset repo by owner namespace and repository name (e.g. stanfordnlp / imdb). |
| Get Model | `getModel` | Get metadata for a single model repo by owner namespace and repository name (e.g. openai-community / gpt2). |
| Get Space | `getSpace` | Get metadata for a single Space repo by id (e.g. huggingface/openapi). |
| List Datasets | `listDatasets` | List/search datasets on the Hub. FREE / zero-cost. Supports search, author, filter, sort, direction, limit, full. |
| List Model Commits | `listModelCommits` | List commits on a given revision (branch, tag or commit) of a model repo, identified by owner namespace and repository name. |
| List Model Refs | `listModelRefs` | List git refs (branches, tags, converts and, with includePrs, pull-request refs) for a model repo, identified by owner namespace and repository name. |
| List Models | `listModels` | List/search models on the Hub. FREE / zero-cost. Supports search, author, filter (tags), sort, direction, limit, full, config. |
| List Router Models | `listRouterModels` | List models available through the Inference Providers router (OpenAI /v1/models style), including per-provider pricing/context. |
| List Spaces | `listSpaces` | List/search Spaces on the Hub. FREE / zero-cost. Supports search, author, filter, sort, direction, limit, full. |
| Who Am I | `whoami` | Return the authenticated user/org info for the hf_ token. FREE / zero-cost — ideal for validating a connection. |
