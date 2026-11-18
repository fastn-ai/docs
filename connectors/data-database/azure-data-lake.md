---
description: "Azure Data Lake Storage Gen2 DataLake REST API."
hidden: true
---

# Azure Data Lake

<img src="../../.gitbook/assets/connectors/lg/azure-data-lake.png" alt="Azure Data Lake logo">

Azure Data Lake Storage Gen2 DataLake REST API. Manage filesystems, directories, files, and ACLs over the DFS endpoint (https://{account}.dfs.core.windows.net). Authenticates with Microsoft Entra ID (Azure AD) OAuth2 bearer tokens.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [azure.microsoft.com](https://azure.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `azureDataLake` |

## Use it

Add Azure Data Lake from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.azureDataLake.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Append Data</td><td><code>appendData</code></td><td>Upload data to be appended to a file at the given offset. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=append&amp;position={offset}. Data must be flushed afterward. Returns 202 Accepted.</td></tr><tr><td>Create Directory</td><td><code>createDirectory</code></td><td>Create a directory. PUT https://{account}.dfs.core.windows.net/{filesystem}/{path}?resource=directory. Returns 201 Created.</td></tr><tr><td>Create File</td><td><code>createFile</code></td><td>Create a file (empty, to be populated via append/flush). PUT https://{account}.dfs.core.windows.net/{filesystem}/{path}?resource=file. Returns 201 Created.</td></tr><tr><td>Create Filesystem</td><td><code>createFilesystem</code></td><td>Create a new filesystem (container). PUT https://{account}.dfs.core.windows.net/{filesystem}?resource=filesystem. Returns 201 Created.</td></tr><tr><td>Delete Filesystem</td><td><code>deleteFilesystem</code></td><td>Delete a filesystem and all its contents. DELETE https://{account}.dfs.core.windows.net/{filesystem}?resource=filesystem. Returns 202 Accepted.</td></tr><tr><td>Delete Path</td><td><code>deletePath</code></td><td>Delete a file or directory. DELETE https://{account}.dfs.core.windows.net/{filesystem}/{path}. Use recursive=true to delete a non-empty directory. Returns 200 OK.</td></tr><tr><td>Flush Data</td><td><code>flushData</code></td><td>Flush (commit) previously appended data to a file up to the given position. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=flush&amp;position={length}. Returns 200 OK.</td></tr><tr><td>Get Access Control</td><td><code>getAccessControl</code></td><td>Get the ACL (owner, group, permissions, acl) of a file or directory. NOTE: native ADLS verb is HEAD; modelled here as GET because fastn does not support HEAD. GET https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=getAccessControl. Values returned as response headers.</td></tr><tr><td>Get Filesystem Properties</td><td><code>getFilesystemProperties</code></td><td>Get properties of a filesystem (user-defined props returned as response headers). NOTE: the native ADLS verb is HEAD; modelled here as GET because fastn does not support HEAD. GET https://{account}.dfs.core.windows.net/{filesystem}?resource=filesystem.</td></tr><tr><td>Get Path Properties</td><td><code>getPathProperties</code></td><td>Get properties/status/ACL of a file or directory. NOTE: the native ADLS verb is HEAD; modelled here as GET because fastn does not support HEAD. GET https://{account}.dfs.core.windows.net/{filesystem}/{path}. Use action=getStatus or getAccessControl to control which properties are returned.</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Lease Path</td><td><code>leasePath</code></td><td>Create and manage a lease (acquire/break/change/renew/release) on a file or directory to control write/delete access. POST https://{account}.dfs.core.windows.net/{filesystem}/{path}. Lease action and duration set via headers.</td></tr><tr><td>List Filesystems</td><td><code>listFilesystems</code></td><td>List all filesystems (containers) in the storage account. GET https://{account}.dfs.core.windows.net/?resource=account. Supports prefix/continuation/maxResults paging.</td></tr><tr><td>List Paths</td><td><code>listPaths</code></td><td>List paths (files and directories) in a filesystem, optionally recursively. GET https://{account}.dfs.core.windows.net/{filesystem}?recursive={bool}&amp;resource=filesystem. Supports directory filter, continuation, maxResults, upn.</td></tr><tr><td>Read File</td><td><code>readFile</code></td><td>Read (download) the contents of a file, optionally a byte range. GET https://{account}.dfs.core.windows.net/{filesystem}/{path}. Returns the file content (200 OK, or 206 Partial Content for a range).</td></tr><tr><td>Set Access Control</td><td><code>setAccessControl</code></td><td>Set owner, group, POSIX permissions, or ACL on a single file or directory. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=setAccessControl. Values supplied via x-ms-owner/x-ms-group/x-ms-permissions/x-ms-acl headers. Returns 200 OK.</td></tr><tr><td>Set Access Control Recursive</td><td><code>setAccessControlRecursive</code></td><td>Set/modify/remove ACLs recursively on a directory and its contents. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=setAccessControlRecursive&amp;mode={mode}. ACL supplied via x-ms-acl header. Returns 200 OK with counts.</td></tr><tr><td>Set Filesystem Properties</td><td><code>setFilesystemProperties</code></td><td>Set user-defined properties for a filesystem. PATCH https://{account}.dfs.core.windows.net/{filesystem}?resource=filesystem. Properties supplied via x-ms-properties header.</td></tr><tr><td>Set Path Properties</td><td><code>setPathProperties</code></td><td>Set system/user-defined properties (HTTP headers, metadata) on a file or directory. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=setProperties. Properties supplied via x-ms-properties header. Returns 200 OK.</td></tr></tbody></table>

</details>
