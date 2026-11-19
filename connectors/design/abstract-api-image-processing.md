---
description: "AbstractAPI Image Processing compresses and resizes images. Optimize an image from a URL."
hidden: true
---

# AbstractAPI Image Processing

<img src="../../.gitbook/assets/connectors/lg/abstract-api-image-processing.png" alt="AbstractAPI Image Processing logo">

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | API key |
| **Slug** | `abstractApiImageProcessing` |

## Setup

Your customers enter their API key for AbstractAPI Image Processing when they connect. Nothing else needs setting up.

## Use it

Add AbstractAPI Image Processing from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiImageProcessing.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Optimize Image From URL</td><td><code>optimizeImageFromUrl</code></td><td>Compresses an image hosted at a public URL (up to 32 MB) using lossless or lossy compression, and returns the original and final size and dimensions, the bytes saved, and a URL to download the optimized image. Quality and resize options are not exposed by this action.</td></tr></tbody></table>

## Events

AbstractAPI Image Processing has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
