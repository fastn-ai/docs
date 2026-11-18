---
description: "Fireworks AI — fast generative AI inference and platform management."
hidden: true
---

# Fireworks AI

<img src="../../.gitbook/assets/connectors/lg/fireworksai.png" alt="Fireworks AI logo">

Fireworks AI — fast generative AI inference and platform management. Covers the OpenAI-compatible Inference API (chat/text completions, embeddings, image generation, audio transcription/translation) at https://api.fireworks.ai/inference/v1 and the Control Plane (models, deployments, datasets, supervised fine-tuning jobs, batch jobs) at https://api.fireworks.ai/v1. Auth: API key as Bearer token.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [fireworks.ai](https://fireworks.ai) |
| **Authentication** | Bearer token |
| **Slug** | `fireworksai` |

## Use it

Add Fireworks AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fireworksai.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Batch Job | `createBatchJob` | Create a batch inference job that runs a model over a JSONL input dataset asynchronously (dataset must be &lt; 500MB). Control-plane base https://api.fireworks.ai/v1. |
| Create Chat Completion | `createChatCompletion` | Generate a chat completion from a list of messages using an OpenAI-compatible chat endpoint. Inference base https://api.fireworks.ai/inference/v1. Cheapest small chat model: accounts/fireworks/models/llama-v3p1-8b-instruct. Returns assistant message(s), token usage and finish reason. Set stream=true for SSE streaming. |
| Create Deployment | `createDeployment` | Create an on-demand deployment of a base model. Control-plane base https://api.fireworks.ai/v1. Pass deploymentId as a query param to set a custom id, or omit for a random one. |
| Create Embeddings | `createEmbeddings` | Create embedding vectors for input text. Inference base https://api.fireworks.ai/inference/v1. Cheapest embedding model: nomic-ai/nomic-embed-text-v1.5. Returns a list of float embedding vectors and token usage. |
| Create Supervised Fine-tuning Job | `createSupervisedFineTuningJob` | Create a supervised fine-tuning (SFT) job from a dataset. Control-plane base https://api.fireworks.ai/v1. Provide exactly one of baseModel or warmStartFrom. |
| Create Text Completion | `createCompletion` | Generate a text completion for a prompt (non-chat). Inference base https://api.fireworks.ai/inference/v1. Cheapest small model: accounts/fireworks/models/llama-v3p1-8b-instruct. Returns completion text, usage and finish reason. |
| Delete Dataset | `deleteDataset` | Delete a dataset by id. Control-plane base https://api.fireworks.ai/v1. |
| Delete Deployment | `deleteDeployment` | Delete an on-demand deployment by id. Control-plane base https://api.fireworks.ai/v1. |
| Delete Supervised Fine-tuning Job | `deleteSupervisedFineTuningJob` | Delete a supervised fine-tuning job by id. Control-plane base https://api.fireworks.ai/v1. |
| Generate Image (FLUX Schnell) | `generateImageFluxSchnell` | [DEPRECATED] Retired by Fireworks AI. The changelog entry "Audio inference and image generation are deprecated" (https://docs.fireworks.ai/updates/changelog) removed image generation from the platform; the flux-1-schnell-fp8 workflow now answers {"error":{"message":"Model not found, inaccessible, and/or not deployed","code":"NOT_FOUND"}}. No supported replacement on this connector. |
| Get Account | `getAccount` | Get account details (display name, state, billing tier). Control-plane base https://api.fireworks.ai/v1. |
| Get Batch Job | `getBatchJob` | Get a single batch inference job by id, including state and output dataset. Control-plane base https://api.fireworks.ai/v1. |
| Get Dataset | `getDataset` | Get a single dataset by id. Control-plane base https://api.fireworks.ai/v1. |
| Get Deployment | `getDeployment` | Get a single deployment's configuration and state by id. Control-plane base https://api.fireworks.ai/v1. |
| Get Model | `getModel` | Get a single model's metadata and capabilities by id. Control-plane base https://api.fireworks.ai/v1. |
| Get Supervised Fine-tuning Job | `getSupervisedFineTuningJob` | Get a single supervised fine-tuning job by id, including state and progress. Control-plane base https://api.fireworks.ai/v1. |
| List Batch Jobs | `listBatchJobs` | List batch inference jobs in an account. Control-plane base https://api.fireworks.ai/v1. |
| List Datasets | `listDatasets` | List datasets in an account (used for fine-tuning and batch jobs). Control-plane base https://api.fireworks.ai/v1. |
| List Deployments | `listDeployments` | List on-demand deployments in an account. Control-plane base https://api.fireworks.ai/v1. |
| List Models | `listModels` | List models available to an account. Control-plane base https://api.fireworks.ai/v1. Returns paginated model objects with capability flags. Use accountId 'fireworks' to browse public serverless models. |
| List Supervised Fine-tuning Jobs | `listSupervisedFineTuningJobs` | List supervised fine-tuning (SFT) jobs in an account. Control-plane base https://api.fireworks.ai/v1. |
| Transcribe Audio | `transcribeAudio` | [DEPRECATED] Retired by Fireworks AI. The changelog entry "Audio inference and image generation are deprecated" (https://docs.fireworks.ai/updates/changelog) removed audio inference from the platform; the audio-prod.api.fireworks.ai host is decommissioned and answers 401 Unauthorized on every path even with a key that authenticates fine against api.fireworks.ai. No supported replacement on this connector. |
| Translate Audio | `translateAudio` | [DEPRECATED] Retired by Fireworks AI. The changelog entry "Audio inference and image generation are deprecated" (https://docs.fireworks.ai/updates/changelog) removed audio inference from the platform; the audio-prod.api.fireworks.ai host is decommissioned and answers 401 Unauthorized on every path even with a key that authenticates fine against api.fireworks.ai. No supported replacement on this connector. |
