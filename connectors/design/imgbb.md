---
description: "ImgBB image hosting and upload API."
hidden: true
---

# ImgBB

<img src="../../.gitbook/assets/connectors/imgbb.png" alt="ImgBB logo" width="64">

ImgBB image hosting and upload API. The platform documents a single endpoint (POST /1/upload) that accepts a binary file, base64-encoded image data, or an image URL (max 32MB), with optional filename and auto-expiration. Returns hosted image URLs (direct, viewer, thumbnail) and a delete URL. Auth is an API key sent as the 'key' query parameter.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [imgbb.com](https://imgbb.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `imgbb` |

## Use it

Add ImgBB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.imgbb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Upload Image | `uploadImage` | Uploads an image to ImgBB and returns hosted URLs. Accepts the image as base64-encoded data or as a publicly reachable image URL (max 32MB). Optional 'name' sets the filename; optional 'expiration' (60-15552000 seconds) auto-deletes the image after that many seconds. This is the ONLY endpoint ImgBB's public API documents. |
