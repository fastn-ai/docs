---
description: "Artificial Analysis provides independent benchmarks of AI models."
hidden: true
---

# Artificial Analysis

<img src="../../.gitbook/assets/connectors/lg/artificial-analysis.png" alt="Artificial Analysis logo">

Artificial Analysis provides independent benchmarks of AI models. This connector covers the free Artificial Analysis Data API: LLM intelligence, speed and pricing metrics, and Elo leaderboards for text-to-image, image-editing, text-to-speech, text-to-video and image-to-video models, plus the CritPt benchmark batch evaluation endpoint for approved research accounts.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [artificialanalysis.ai](https://artificialanalysis.ai) |
| **Authentication** | Credentials you enter |
| **Slug** | `artificialAnalysis` |

## Use it

Add Artificial Analysis from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.artificialAnalysis.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Evaluate CritPt Submissions | `evaluateCritptSubmissions` | Submits a batch of code generation submissions for grading against the CritPt benchmark private evaluation set and returns aggregate accuracy, timeout and judge-error statistics. Every problem in the public set must be included in one batch. Grading access is restricted to labs and researchers approved by Artificial Analysis (accounts without approval receive a 403), it is rate-limited to 10 requests per 24 hours, and requests can take a long time to complete. |
| List Image Editing Models | `listImageEditingModels` | Returns the Artificial Analysis Image Arena leaderboard for image editing models: Elo rating, rank, 95% confidence interval, arena appearances and release date for every current first-party model holding a leaderboard rank. |
| List Image-to-Video Models | `listImageToVideoModels` | Returns the Artificial Analysis Video Arena leaderboard for image-to-video models: Elo rating, rank, 95% confidence interval, arena appearances and release date for every current model holding a leaderboard rank. Optionally includes a breakdown of Elo scores by style, subject-matter and format category. |
| List LLM Models | `listLlmModels` | Returns every large language model benchmarked by Artificial Analysis with its intelligence, coding and math index scores, individual evaluation results, pricing per million tokens, and median speed and latency figures. Speed and latency use the medium (1,000 input token) prompt length. Use the stable model and creator ids as identifiers; slugs and names may change. |
| List Text-to-Image Models | `listTextToImageModels` | Returns the Artificial Analysis Image Arena leaderboard for text-to-image models: Elo rating, rank, 95% confidence interval, arena appearances and release date for every current first-party model holding a leaderboard rank. Optionally includes a breakdown of Elo scores by style and subject-matter category. |
| List Text-to-Speech Models | `listTextToSpeechModels` | Returns the Artificial Analysis Speech Arena leaderboard for text-to-speech models: Elo rating, rank and 95% confidence interval for each ranked model. |
| List Text-to-Video Models | `listTextToVideoModels` | Returns the Artificial Analysis Video Arena leaderboard for text-to-video models: Elo rating, rank, 95% confidence interval, arena appearances and release date for every current model holding a leaderboard rank. Optionally includes a breakdown of Elo scores by style, subject-matter and format category. |
