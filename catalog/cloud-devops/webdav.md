---
description: "WebDAV is a standard for managing files on a web server. List directories, upload, download, copy, move and delete files, and read file properties."
hidden: true
---

# WebDAV

<img src="../../.gitbook/assets/connectors/lg/webdav.png" alt="WebDAV logo">

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [webdav.org](https://webdav.org) |
| **Authentication** | Username and password |
| **Slug** | `webdav` |

## Setup

Your customers enter their username and password for WebDAV when they connect. Nothing else needs setting up.

## Use it

Add WebDAV from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.webdav.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Copy Resource</td><td><code>copyResource</code></td><td></td></tr><tr><td>Create Directory</td><td><code>createDirectory</code></td><td></td></tr><tr><td>Delete Resource</td><td><code>deleteResource</code></td><td></td></tr><tr><td>Download File</td><td><code>downloadFile</code></td><td></td></tr><tr><td>Get File Properties</td><td><code>getFileProperties</code></td><td></td></tr><tr><td>List Directory</td><td><code>listDirectory</code></td><td></td></tr><tr><td>Move or Rename</td><td><code>moveResource</code></td><td></td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td></td></tr></tbody></table>

## Events

WebDAV has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
