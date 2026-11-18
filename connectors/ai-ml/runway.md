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

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel or Delete Task | `cancelOrDeleteTask` | Cancels a task that is still running or deletes the record of a completed task by its id. Returns no content on success. This is a free operation that does not consume credits. |
| Create Character Performance Task | `characterPerformance` | Starts a new Act-Two task that drives a character image or video with the performance from a reference video. Returns a task id to poll with Get Task. Consumes organization credits when a valid job is submitted. |
| Create Image to Video Task | `imageToVideo` | Starts a new task that generates a video from a starting image (and optional text prompt) using a Runway video model. Returns a task id to poll with Get Task. Consumes organization credits when a valid job is submitted. |
| Create Image Upscale Task | `imageUpscale` | Starts a new task that upscales and enhances an input image using a Runway upscaling model. Returns a task id to poll with Get Task. Consumes organization credits when a valid job is submitted. |
| Create Text to Image Task | `textToImage` | Starts a new task that generates an image from a text prompt using a Runway image model. Returns a task id to poll with Get Task. Consumes organization credits when a valid job is submitted. |
| Create Text to Video Task | `textToVideo` | Starts a new task that generates a video directly from a text prompt using a Runway video model. Returns a task id to poll with Get Task. Consumes organization credits when a valid job is submitted. |
| Create Video to Video Task | `videoToVideo` | Starts a new task that restyles or transforms an input video into a new video using a Runway video-to-video model. Returns a task id to poll with Get Task. Consumes organization credits when a valid job is submitted. |
| Create Video Upscale Task | `videoUpscale` | Starts a new task that upscales and enhances an input video using a Runway video upscaling model. Returns a task id to poll with Get Task. Consumes organization credits when a valid job is submitted. |
| Get Organization | `getOrganization` | Retrieves information about the Runway organization tied to the API key, including its tier and remaining credit balance. |
| Get Organization Usage | `getOrganizationUsage` | Queries credit usage for the Runway organization over a date range, broken down by day and model. This is a free read that does not consume credits. |
| Get Task | `getTask` | Retrieves the status and result of a generation task by its id. Poll this until the task status is SUCCEEDED or FAILED. This is a free read that does not consume credits. |
