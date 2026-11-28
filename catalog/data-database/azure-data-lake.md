---
description: "Azure Data Lake Storage holds large amounts of data on Azure. Manage file systems, directories, files and access controls."
hidden: true
---

# Azure Data Lake

<img src="../../.gitbook/assets/connectors/lg/azure-data-lake.png" alt="Azure Data Lake logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [azure.microsoft.com](https://azure.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `azureDataLake` |

## Setup

Your customers sign in to Azure Data Lake through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Azure Data Lake from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Azure Data Lake**.
2. Select **Connect** on the Azure Data Lake card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Azure Data Lake and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Azure Data Lake's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Append Data</td><td><code>appendData</code></td><td>Upload data to be appended to a file at the given offset. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=append&amp;position={offset}. Data must be flushed afterward.</td></tr><tr><td>Create Directory</td><td><code>createDirectory</code></td><td>Create a directory. PUT https://{account}.dfs.core.windows.net/{filesystem}/{path}?resource=directory.</td></tr><tr><td>Create File</td><td><code>createFile</code></td><td>Create a file (empty, to be populated via append/flush). PUT https://{account}.dfs.core.windows.net/{filesystem}/{path}?resource=file.</td></tr><tr><td>Create Filesystem</td><td><code>createFilesystem</code></td><td>Create a new filesystem (container). PUT https://{account}.dfs.core.windows.net/{filesystem}?resource=filesystem.</td></tr><tr><td>Delete Filesystem</td><td><code>deleteFilesystem</code></td><td>Delete a filesystem and all its contents. DELETE https://{account}.dfs.core.windows.net/{filesystem}?resource=filesystem.</td></tr><tr><td>Delete Path</td><td><code>deletePath</code></td><td>Delete a file or directory. DELETE https://{account}.dfs.core.windows.net/{filesystem}/{path}. Use recursive=true to delete a non-empty directory.</td></tr><tr><td>Flush Data</td><td><code>flushData</code></td><td>Flush (commit) previously appended data to a file up to the given position. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=flush&amp;position={length}.</td></tr><tr><td>Get Access Control</td><td><code>getAccessControl</code></td><td>Get the ACL (owner, group, permissions, acl) of a file or directory. NOTE: native ADLS verb is HEAD; modelled here as GET because Fastn does not support HEAD. GET https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=getAccessControl. Values returned as response headers.</td></tr><tr><td>Get Filesystem Properties</td><td><code>getFilesystemProperties</code></td><td>Get properties of a filesystem (user-defined props returned as response headers). NOTE: the native ADLS verb is HEAD; modelled here as GET because Fastn does not support HEAD. GET https://{account}.dfs.core.windows.net/{filesystem}?resource=filesystem.</td></tr><tr><td>Get Path Properties</td><td><code>getPathProperties</code></td><td>Get properties/status/ACL of a file or directory. NOTE: the native ADLS verb is HEAD; modelled here as GET because Fastn does not support HEAD. GET https://{account}.dfs.core.windows.net/{filesystem}/{path}. Use action=getStatus or getAccessControl to control which properties are returned.</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Lease Path</td><td><code>leasePath</code></td><td>Create and manage a lease (acquire/break/change/renew/release) on a file or directory to control write/delete access. POST https://{account}.dfs.core.windows.net/{filesystem}/{path}. Lease action and duration set via headers.</td></tr><tr><td>List Filesystems</td><td><code>listFilesystems</code></td><td>List all filesystems (containers) in the storage account. GET https://{account}.dfs.core.windows.net/?resource=account. Supports prefix/continuation/maxResults paging.</td></tr><tr><td>List Paths</td><td><code>listPaths</code></td><td>List paths (files and directories) in a filesystem, optionally recursively. GET https://{account}.dfs.core.windows.net/{filesystem}?recursive={bool}&amp;resource=filesystem. Supports directory filter, continuation, maxResults, upn.</td></tr><tr><td>Read File</td><td><code>readFile</code></td><td>Read (download) the contents of a file, optionally a byte range. GET https://{account}.dfs.core.windows.net/{filesystem}/{path}. Returns the file content (200 OK, or 206 Partial Content for a range).</td></tr><tr><td>Set Access Control</td><td><code>setAccessControl</code></td><td>Set owner, group, POSIX permissions, or ACL on a single file or directory. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=setAccessControl. Values supplied via x-ms-owner/x-ms-group/x-ms-permissions/x-ms-acl headers.</td></tr><tr><td>Set Access Control Recursive</td><td><code>setAccessControlRecursive</code></td><td>Set/modify/remove ACLs recursively on a directory and its contents. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=setAccessControlRecursive&amp;mode={mode}. ACL supplied via x-ms-acl header.</td></tr><tr><td>Set Filesystem Properties</td><td><code>setFilesystemProperties</code></td><td>Set user-defined properties for a filesystem. PATCH https://{account}.dfs.core.windows.net/{filesystem}?resource=filesystem. Properties supplied via x-ms-properties header.</td></tr><tr><td>Set Path Properties</td><td><code>setPathProperties</code></td><td>Set system/user-defined properties (HTTP headers, metadata) on a file or directory. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=setProperties. Properties supplied via x-ms-properties header.</td></tr></tbody></table>

</details>

