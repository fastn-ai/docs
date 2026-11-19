---
description: "ImgBB is an image hosting service. Upload an image and get a link to it."
hidden: true
---

# ImgBB

<img src="../../.gitbook/assets/connectors/lg/imgbb.png" alt="ImgBB logo">

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [imgbb.com](https://imgbb.com) |
| **Authentication** | API key |
| **Slug** | `imgbb` |

## Setup

Your customers enter their API key for ImgBB when they connect. Nothing else needs setting up.

## Use it

Add ImgBB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.imgbb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Upload Image</td><td><code>uploadImage</code></td><td>Uploads an image to ImgBB and returns hosted URLs. Accepts the image as base64-encoded data or as a publicly reachable image URL (max 32MB). Optional 'name' sets the filename; optional 'expiration' (60-15552000 seconds) auto-deletes the image after that many seconds. This is the ONLY endpoint ImgBB's public API documents.</td></tr></tbody></table>

## Events

ImgBB has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
