---
description: "Fireworks AI runs fast generative AI models. Create chat and text completions, embeddings and images, and manage deployments, datasets and fine-tuning."
hidden: true
---

# Fireworks AI

<img src="../../.gitbook/assets/connectors/lg/fireworksai.png" alt="Fireworks AI logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [fireworks.ai](https://fireworks.ai) |
| **Authentication** | Access token |
| **Slug** | `fireworksai` |

## Setup

Your customers enter their access token for Fireworks AI when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Fireworks AI from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Fireworks AI**.
2. Select **Connect** on the Fireworks AI card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Fireworks AI's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Batch Job</td><td><code>createBatchJob</code></td><td>Create a batch inference job that runs a model over a JSONL input dataset asynchronously (dataset must be &lt; 500MB). Control-plane base https://api.fireworks.ai/v1.</td></tr><tr><td>Create Chat Completion</td><td><code>createChatCompletion</code></td><td>Generate a chat completion from a list of messages using an OpenAI-compatible chat endpoint. Inference base https://api.fireworks.ai/inference/v1. Cheapest small chat model: accounts/fireworks/models/llama-v3p1-8b-instruct. Returns assistant message(s), token usage and finish reason. Set stream=true for SSE streaming.</td></tr><tr><td>Create Deployment</td><td><code>createDeployment</code></td><td>Create an on-demand deployment of a base model. Control-plane base https://api.fireworks.ai/v1. Pass deploymentId as a query param to set a custom id, or omit for a random one.</td></tr><tr><td>Create Embeddings</td><td><code>createEmbeddings</code></td><td>Create embedding vectors for input text. Inference base https://api.fireworks.ai/inference/v1. Cheapest embedding model: nomic-ai/nomic-embed-text-v1.5. Returns a list of float embedding vectors and token usage.</td></tr><tr><td>Create Supervised Fine-tuning Job</td><td><code>createSupervisedFineTuningJob</code></td><td>Create a supervised fine-tuning (SFT) job from a dataset. Control-plane base https://api.fireworks.ai/v1. Provide exactly one of baseModel or warmStartFrom.</td></tr><tr><td>Create Text Completion</td><td><code>createCompletion</code></td><td>Generate a text completion for a prompt (non-chat). Inference base https://api.fireworks.ai/inference/v1. Cheapest small model: accounts/fireworks/models/llama-v3p1-8b-instruct. Returns completion text, usage and finish reason.</td></tr><tr><td>Delete Dataset</td><td><code>deleteDataset</code></td><td>Delete a dataset by id. Control-plane base https://api.fireworks.ai/v1.</td></tr><tr><td>Delete Deployment</td><td><code>deleteDeployment</code></td><td>Delete an on-demand deployment by id. Control-plane base https://api.fireworks.ai/v1.</td></tr><tr><td>Delete Supervised Fine-tuning Job</td><td><code>deleteSupervisedFineTuningJob</code></td><td>Delete a supervised fine-tuning job by id. Control-plane base https://api.fireworks.ai/v1.</td></tr><tr><td>Generate Image (FLUX Schnell)</td><td><code>generateImageFluxSchnell</code></td><td>[DEPRECATED] Retired by Fireworks AI. The changelog entry "Audio inference and image generation are deprecated" (https://docs.fireworks.ai/updates/changelog) removed image generation from the platform; the flux-1-schnell-fp8 workflow now answers {"error":{"message":"Model not found, inaccessible, and/or not deployed","code":"NOT_FOUND"}}. No supported replacement on this connector.</td></tr></tbody></table>

<details>

<summary>View 13 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Account</td><td><code>getAccount</code></td><td>Get account details (display name, state, billing tier). Control-plane base https://api.fireworks.ai/v1.</td></tr><tr><td>Get Batch Job</td><td><code>getBatchJob</code></td><td>Get a single batch inference job by id, including state and output dataset. Control-plane base https://api.fireworks.ai/v1.</td></tr><tr><td>Get Dataset</td><td><code>getDataset</code></td><td>Get a single dataset by id. Control-plane base https://api.fireworks.ai/v1.</td></tr><tr><td>Get Deployment</td><td><code>getDeployment</code></td><td>Get a single deployment's configuration and state by id. Control-plane base https://api.fireworks.ai/v1.</td></tr><tr><td>Get Model</td><td><code>getModel</code></td><td>Get a single model's metadata and capabilities by id. Control-plane base https://api.fireworks.ai/v1.</td></tr><tr><td>Get Supervised Fine-tuning Job</td><td><code>getSupervisedFineTuningJob</code></td><td>Get a single supervised fine-tuning job by id, including state and progress. Control-plane base https://api.fireworks.ai/v1.</td></tr><tr><td>List Batch Jobs</td><td><code>listBatchJobs</code></td><td>List batch inference jobs in an account. Control-plane base https://api.fireworks.ai/v1.</td></tr><tr><td>List Datasets</td><td><code>listDatasets</code></td><td>List datasets in an account (used for fine-tuning and batch jobs). Control-plane base https://api.fireworks.ai/v1.</td></tr><tr><td>List Deployments</td><td><code>listDeployments</code></td><td>List on-demand deployments in an account. Control-plane base https://api.fireworks.ai/v1.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>List models available to an account. Control-plane base https://api.fireworks.ai/v1. Returns paginated model objects with capability flags. Use accountId 'fireworks' to browse public serverless models.</td></tr><tr><td>List Supervised Fine-tuning Jobs</td><td><code>listSupervisedFineTuningJobs</code></td><td>List supervised fine-tuning (SFT) jobs in an account. Control-plane base https://api.fireworks.ai/v1.</td></tr><tr><td>Transcribe Audio</td><td><code>transcribeAudio</code></td><td>[DEPRECATED] Retired by Fireworks AI. No supported replacement on this connector.</td></tr><tr><td>Translate Audio</td><td><code>translateAudio</code></td><td>[DEPRECATED] Retired by Fireworks AI. No supported replacement on this connector.</td></tr></tbody></table>

</details>

