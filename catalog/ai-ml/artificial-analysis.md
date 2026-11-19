---
description: "Artificial Analysis publishes independent benchmarks of AI models. List rankings for language, image, video and speech models."
hidden: true
---

# Artificial Analysis

<img src="../../.gitbook/assets/connectors/lg/artificial-analysis.png" alt="Artificial Analysis logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [artificialanalysis.ai](https://artificialanalysis.ai) |
| **Authentication** | API key |
| **Slug** | `artificialAnalysis` |

## Setup

Your customers enter their API key for Artificial Analysis when they connect. Nothing else needs setting up.

## Use it

Add Artificial Analysis from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.artificialAnalysis.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Evaluate CritPt Submissions</td><td><code>evaluateCritptSubmissions</code></td><td>Submits a batch of code generation submissions for grading against the CritPt benchmark private evaluation set and returns aggregate accuracy, timeout and judge-error statistics. Every problem in the public set must be included in one batch. Grading access is restricted to labs and researchers approved by Artificial Analysis (accounts without approval receive a 403), it is rate-limited to 10 requests per 24 hours, and requests can take a long time to complete.</td></tr><tr><td>List Image Editing Models</td><td><code>listImageEditingModels</code></td><td>Returns the Artificial Analysis Image Arena leaderboard for image editing models: Elo rating, rank, 95% confidence interval, arena appearances and release date for every current first-party model holding a leaderboard rank.</td></tr><tr><td>List Image-to-Video Models</td><td><code>listImageToVideoModels</code></td><td>Returns the Artificial Analysis Video Arena leaderboard for image-to-video models: Elo rating, rank, 95% confidence interval, arena appearances and release date for every current model holding a leaderboard rank. Optionally includes a breakdown of Elo scores by style, subject-matter and format category.</td></tr><tr><td>List LLM Models</td><td><code>listLlmModels</code></td><td>Returns every large language model benchmarked by Artificial Analysis with its intelligence, coding and math index scores, individual evaluation results, pricing per million tokens, and median speed and latency figures. Speed and latency use the medium (1,000 input token) prompt length. Use the stable model and creator ids as identifiers; slugs and names may change.</td></tr><tr><td>List Text-to-Image Models</td><td><code>listTextToImageModels</code></td><td>Returns the Artificial Analysis Image Arena leaderboard for text-to-image models: Elo rating, rank, 95% confidence interval, arena appearances and release date for every current first-party model holding a leaderboard rank. Optionally includes a breakdown of Elo scores by style and subject-matter category.</td></tr><tr><td>List Text-to-Speech Models</td><td><code>listTextToSpeechModels</code></td><td>Returns the Artificial Analysis Speech Arena leaderboard for text-to-speech models: Elo rating, rank and 95% confidence interval for each ranked model.</td></tr><tr><td>List Text-to-Video Models</td><td><code>listTextToVideoModels</code></td><td>Returns the Artificial Analysis Video Arena leaderboard for text-to-video models: Elo rating, rank, 95% confidence interval, arena appearances and release date for every current model holding a leaderboard rank. Optionally includes a breakdown of Elo scores by style, subject-matter and format category.</td></tr></tbody></table>

## Events

Artificial Analysis has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
