---
description: "Runway generative AI API for video and image creation."
hidden: true
---

# Runway

<img src="../../.gitbook/assets/connectors/lg/runway.png" alt="Runway logo">

Runway generative AI API for video and image creation. Start generation tasks (text-to-image, image-to-video, video-to-video, upscaling, character performance), track task status, and query organization credit usage.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [runwayml.com](https://runwayml.com) |
| **Authentication** | Bearer token |
| **Slug** | `runway` |

## Use it

Add Runway from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.runway.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Cancel or Delete Task</td><td><code>cancelOrDeleteTask</code></td><td>Cancels a task that is still running or deletes the record of a completed task by its id. Returns no content on success. This is a free operation that does not consume credits.</td></tr><tr><td>Create Character Performance Task</td><td><code>characterPerformance</code></td><td>Starts a new Act-Two task that drives a character image or video with the performance from a reference video. Returns a task id to poll with Get Task. Consumes organization credits when a valid job is submitted.</td></tr><tr><td>Create Image to Video Task</td><td><code>imageToVideo</code></td><td>Starts a new task that generates a video from a starting image (and optional text prompt) using a Runway video model. Returns a task id to poll with Get Task. Consumes organization credits when a valid job is submitted.</td></tr><tr><td>Create Image Upscale Task</td><td><code>imageUpscale</code></td><td>Starts a new task that upscales and enhances an input image using a Runway upscaling model. Returns a task id to poll with Get Task. Consumes organization credits when a valid job is submitted.</td></tr><tr><td>Create Text to Image Task</td><td><code>textToImage</code></td><td>Starts a new task that generates an image from a text prompt using a Runway image model. Returns a task id to poll with Get Task. Consumes organization credits when a valid job is submitted.</td></tr><tr><td>Create Text to Video Task</td><td><code>textToVideo</code></td><td>Starts a new task that generates a video directly from a text prompt using a Runway video model. Returns a task id to poll with Get Task. Consumes organization credits when a valid job is submitted.</td></tr><tr><td>Create Video to Video Task</td><td><code>videoToVideo</code></td><td>Starts a new task that restyles or transforms an input video into a new video using a Runway video-to-video model. Returns a task id to poll with Get Task. Consumes organization credits when a valid job is submitted.</td></tr><tr><td>Create Video Upscale Task</td><td><code>videoUpscale</code></td><td>Starts a new task that upscales and enhances an input video using a Runway video upscaling model. Returns a task id to poll with Get Task. Consumes organization credits when a valid job is submitted.</td></tr><tr><td>Get Organization</td><td><code>getOrganization</code></td><td>Retrieves information about the Runway organization tied to the API key, including its tier and remaining credit balance.</td></tr><tr><td>Get Organization Usage</td><td><code>getOrganizationUsage</code></td><td>Queries credit usage for the Runway organization over a date range, broken down by day and model. This is a free read that does not consume credits.</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Task</td><td><code>getTask</code></td><td>Retrieves the status and result of a generation task by its id. Poll this until the task status is SUCCEEDED or FAILED. This is a free read that does not consume credits.</td></tr></tbody></table>

</details>
