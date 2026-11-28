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

## Connect in Fastn

Your customers connect Artificial Analysis from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Artificial Analysis**.
2. Select **Connect** on the Artificial Analysis card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Artificial Analysis's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Evaluate CritPt Submissions</td><td><code>evaluateCritptSubmissions</code></td><td>Submits a batch of code generation submissions for grading against the CritPt benchmark private evaluation set and returns aggregate accuracy, timeout and judge-error statistics. Every problem in the public set must be included in one batch. Grading access is restricted to labs and researchers approved by Artificial Analysis (accounts without approval receive a 403), it is rate-limited to 10 requests per 24 hours, and requests can take a long time to complete.</td></tr><tr><td>List Image Editing Models</td><td><code>listImageEditingModels</code></td><td>Returns the Artificial Analysis Image Arena leaderboard for image editing models: Elo rating, rank, 95% confidence interval, arena appearances and release date for every current first-party model holding a leaderboard rank.</td></tr><tr><td>List Image-to-Video Models</td><td><code>listImageToVideoModels</code></td><td>Returns the Artificial Analysis Video Arena leaderboard for image-to-video models: Elo rating, rank, 95% confidence interval, arena appearances and release date for every current model holding a leaderboard rank. Optionally includes a breakdown of Elo scores by style, subject-matter and format category.</td></tr><tr><td>List LLM Models</td><td><code>listLlmModels</code></td><td>Returns every large language model benchmarked by Artificial Analysis with its intelligence, coding and math index scores, individual evaluation results, pricing per million tokens, and median speed and latency figures. Speed and latency use the medium (1,000 input token) prompt length. Use the stable model and creator ids as identifiers; slugs and names may change.</td></tr><tr><td>List Text-to-Image Models</td><td><code>listTextToImageModels</code></td><td>Returns the Artificial Analysis Image Arena leaderboard for text-to-image models: Elo rating, rank, 95% confidence interval, arena appearances and release date for every current first-party model holding a leaderboard rank. Optionally includes a breakdown of Elo scores by style and subject-matter category.</td></tr><tr><td>List Text-to-Speech Models</td><td><code>listTextToSpeechModels</code></td><td>Returns the Artificial Analysis Speech Arena leaderboard for text-to-speech models: Elo rating, rank and 95% confidence interval for each ranked model.</td></tr><tr><td>List Text-to-Video Models</td><td><code>listTextToVideoModels</code></td><td>Returns the Artificial Analysis Video Arena leaderboard for text-to-video models: Elo rating, rank, 95% confidence interval, arena appearances and release date for every current model holding a leaderboard rank. Optionally includes a breakdown of Elo scores by style, subject-matter and format category.</td></tr></tbody></table>

