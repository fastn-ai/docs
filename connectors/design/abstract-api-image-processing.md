---
description: "AbstractAPI Image Processing and Optimization compresses an image hosted at a URL, with lossless or lossy compression, and returns the size savings and a…"
hidden: true
---

# AbstractAPI Image Processing

AbstractAPI Image Processing and Optimization compresses an image hosted at a URL, with lossless or lossy compression, and returns the size savings and a download link to the optimized image.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 1 |
| **Events** | 0 |
| **Slug** | `abstractApiImageProcessing` |

## Use it

Add AbstractAPI Image Processing from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiImageProcessing.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Optimize Image From URL | `optimizeImageFromUrl` | Compresses an image hosted at a public URL (up to 32 MB) using lossless or lossy compression, and returns the original and final size and dimensions, the bytes saved, and a URL to download the optimized image. Quality and resize options are not exposed by this action. |
