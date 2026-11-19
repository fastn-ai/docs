---
description: "Connect Hugging Face to your product with fastn."
hidden: true
---

# Hugging Face

<img src="../../.gitbook/assets/connectors/lg/huggingface.png" alt="Hugging Face logo">

Hugging Face connector covering the Hub API (whoami, models, datasets, spaces, repos, refs, commits) and Inference Providers router (OpenAI-compatible chat completions, feature-extraction embeddings). Auth: bearer hf_ token.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [huggingface.co](https://huggingface.co) |
| **Authentication** | Bearer token |
| **Slug** | `huggingface` |

## Use it

Add Hugging Face from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.huggingface.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Chat Completions</td><td><code>chatCompletions</code></td><td>OpenAI-compatible chat completion via the Inference Providers router. INCURS CREDITS. Body: required model + messages only.</td></tr><tr><td>Create Repo</td><td><code>createRepo</code></td><td>Create a new model, dataset, or space repository. Body: required name + type only (optional organization/private/sdk omitted by default).</td></tr><tr><td>Delete Repo</td><td><code>deleteRepo</code></td><td>Delete a model, dataset, or space repository. Body: required name + type only.</td></tr><tr><td>Feature Extraction (Embeddings)</td><td><code>featureExtraction</code></td><td>Generate embeddings for text via the hf-inference router feature-extraction pipeline. INCURS CREDITS. Body: required inputs; model id in the path.</td></tr><tr><td>Get Dataset</td><td><code>getDataset</code></td><td>Get metadata for a single dataset repo by owner namespace and repository name (e.g. stanfordnlp / imdb).</td></tr><tr><td>Get Model</td><td><code>getModel</code></td><td>Get metadata for a single model repo by owner namespace and repository name (e.g. openai-community / gpt2).</td></tr><tr><td>Get Space</td><td><code>getSpace</code></td><td>Get metadata for a single Space repo by id (e.g. huggingface/openapi).</td></tr><tr><td>List Datasets</td><td><code>listDatasets</code></td><td>List/search datasets on the Hub. FREE / zero-cost. Supports search, author, filter, sort, direction, limit, full.</td></tr><tr><td>List Model Commits</td><td><code>listModelCommits</code></td><td>List commits on a given revision (branch, tag or commit) of a model repo, identified by owner namespace and repository name.</td></tr><tr><td>List Model Refs</td><td><code>listModelRefs</code></td><td>List git refs (branches, tags, converts and, with includePrs, pull-request refs) for a model repo, identified by owner namespace and repository name.</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Models</td><td><code>listModels</code></td><td>List/search models on the Hub. FREE / zero-cost. Supports search, author, filter (tags), sort, direction, limit, full, config.</td></tr><tr><td>List Router Models</td><td><code>listRouterModels</code></td><td>List models available through the Inference Providers router (OpenAI /v1/models style), including per-provider pricing/context.</td></tr><tr><td>List Spaces</td><td><code>listSpaces</code></td><td>List/search Spaces on the Hub. FREE / zero-cost. Supports search, author, filter, sort, direction, limit, full.</td></tr><tr><td>Who Am I</td><td><code>whoami</code></td><td>Return the authenticated user/org info for the hf_ token. FREE / zero-cost — ideal for validating a connection.</td></tr></tbody></table>

</details>
