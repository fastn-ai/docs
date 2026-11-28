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

## Connect in Fastn

Your customers connect WebDAV from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **WebDAV**.
2. Select **Connect** on the WebDAV card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use WebDAV's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Copy Resource</td><td><code>copyResource</code></td><td></td></tr><tr><td>Create Directory</td><td><code>createDirectory</code></td><td></td></tr><tr><td>Delete Resource</td><td><code>deleteResource</code></td><td></td></tr><tr><td>Download File</td><td><code>downloadFile</code></td><td></td></tr><tr><td>Get File Properties</td><td><code>getFileProperties</code></td><td></td></tr><tr><td>List Directory</td><td><code>listDirectory</code></td><td></td></tr><tr><td>Move or Rename</td><td><code>moveResource</code></td><td></td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td></td></tr></tbody></table>

