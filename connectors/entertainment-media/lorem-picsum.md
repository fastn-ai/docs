---
description: "Lorem Picsum is a free placeholder photo service built on Unsplash images."
hidden: true
---

# Lorem Picsum

<img src="../../.gitbook/assets/connectors/lorem-picsum.png" alt="Lorem Picsum logo" width="64">

Lorem Picsum is a free placeholder photo service built on Unsplash images. List the available images with paging and get details for an image by id or by seed. No API key needed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [picsum.photos](https://picsum.photos) |
| **Authentication** | No authentication |
| **Slug** | `loremPicsum` |

## Use it

Add Lorem Picsum from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.loremPicsum.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Image Details | `getImageInfo` | Get author, size and links for one image by its id (GET /id/{id}/info). Docs: https://picsum.photos/ |
| Get Seeded Image Details | `getSeedImageInfo` | Get details of the image that a given seed always maps to (GET /seed/{seed}/info). Docs: https://picsum.photos/ |
| List Images | `listImages` | List the images available on Lorem Picsum with author, size and links, 30 per page by default (GET /v2/list). Docs: https://picsum.photos/ |
