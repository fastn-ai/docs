---
description: "Lorem Picsum is a free placeholder photo service. List images and get image details by ID or seed."
hidden: true
---

# Lorem Picsum

<img src="../../.gitbook/assets/connectors/lg/lorem-picsum.png" alt="Lorem Picsum logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [picsum.photos](https://picsum.photos) |
| **Authentication** | No sign-in needed |
| **Slug** | `loremPicsum` |

## Setup

Lorem Picsum needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Lorem Picsum from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.loremPicsum.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Image Details</td><td><code>getImageInfo</code></td><td>Get author, size and links for one image by its id Docs: https://picsum.photos/</td></tr><tr><td>Get Seeded Image Details</td><td><code>getSeedImageInfo</code></td><td>Get details of the image that a given seed always maps to Docs: https://picsum.photos/</td></tr><tr><td>List Images</td><td><code>listImages</code></td><td>List the images available on Lorem Picsum with author, size and links, 30 per page by default Docs: https://picsum.photos/</td></tr></tbody></table>

## Events

Lorem Picsum has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
