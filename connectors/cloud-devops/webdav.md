---
description: "WebDAV (Web Distributed Authoring and Versioning) connector for remote file management over HTTP."
hidden: true
---

# WebDAV

WebDAV (Web Distributed Authoring and Versioning) connector for remote file management over HTTP. Supports listing, reading, uploading, moving, copying, and deleting files and directories on any RFC 4918-compliant WebDAV server.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [webdav.org](https://webdav.org) |
| **Authentication** | Digest auth |
| **Actions** | 8 |
| **Events** | 0 |
| **Slug** | `webdav` |

## Use it

Add WebDAV from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.webdav.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Copy Resource | `copyResource` |  |
| Create Directory | `createDirectory` |  |
| Delete Resource | `deleteResource` |  |
| Download File | `downloadFile` |  |
| Get File Properties | `getFileProperties` |  |
| List Directory | `listDirectory` |  |
| Move or Rename | `moveResource` |  |
| Upload File | `uploadFile` |  |
