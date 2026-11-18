---
description: "Azure Data Lake Storage Gen2 DataLake REST API."
---

# Azure Data Lake

Azure Data Lake Storage Gen2 DataLake REST API. Manage filesystems, directories, files, and ACLs over the DFS endpoint (https://{account}.dfs.core.windows.net). Authenticates with Microsoft Entra ID (Azure AD) OAuth2 bearer tokens.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [azure.microsoft.com](https://azure.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 18 |
| **Events** | 0 |
| **Slug** | `azureDataLake` |

## Use it

Add Azure Data Lake from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.azureDataLake.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Append Data | `appendData` | Upload data to be appended to a file at the given offset. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=append&position={offset}. Data must be flushed afterward. Returns 202 Accepted. |
| Create Directory | `createDirectory` | Create a directory. PUT https://{account}.dfs.core.windows.net/{filesystem}/{path}?resource=directory. Returns 201 Created. |
| Create File | `createFile` | Create a file (empty, to be populated via append/flush). PUT https://{account}.dfs.core.windows.net/{filesystem}/{path}?resource=file. Returns 201 Created. |
| Create Filesystem | `createFilesystem` | Create a new filesystem (container). PUT https://{account}.dfs.core.windows.net/{filesystem}?resource=filesystem. Returns 201 Created. |
| Delete Filesystem | `deleteFilesystem` | Delete a filesystem and all its contents. DELETE https://{account}.dfs.core.windows.net/{filesystem}?resource=filesystem. Returns 202 Accepted. |
| Delete Path | `deletePath` | Delete a file or directory. DELETE https://{account}.dfs.core.windows.net/{filesystem}/{path}. Use recursive=true to delete a non-empty directory. Returns 200 OK. |
| Flush Data | `flushData` | Flush (commit) previously appended data to a file up to the given position. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=flush&position={length}. Returns 200 OK. |
| Get Access Control | `getAccessControl` | Get the ACL (owner, group, permissions, acl) of a file or directory. NOTE: native ADLS verb is HEAD; modelled here as GET because fastn does not support HEAD. GET https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=getAccessControl. Values returned as response headers. |
| Get Filesystem Properties | `getFilesystemProperties` | Get properties of a filesystem (user-defined props returned as response headers). NOTE: the native ADLS verb is HEAD; modelled here as GET because fastn does not support HEAD. GET https://{account}.dfs.core.windows.net/{filesystem}?resource=filesystem. |
| Get Path Properties | `getPathProperties` | Get properties/status/ACL of a file or directory. NOTE: the native ADLS verb is HEAD; modelled here as GET because fastn does not support HEAD. GET https://{account}.dfs.core.windows.net/{filesystem}/{path}. Use action=getStatus or getAccessControl to control which properties are returned. |
| Lease Path | `leasePath` | Create and manage a lease (acquire/break/change/renew/release) on a file or directory to control write/delete access. POST https://{account}.dfs.core.windows.net/{filesystem}/{path}. Lease action and duration set via headers. |
| List Filesystems | `listFilesystems` | List all filesystems (containers) in the storage account. GET https://{account}.dfs.core.windows.net/?resource=account. Supports prefix/continuation/maxResults paging. |
| List Paths | `listPaths` | List paths (files and directories) in a filesystem, optionally recursively. GET https://{account}.dfs.core.windows.net/{filesystem}?recursive={bool}&resource=filesystem. Supports directory filter, continuation, maxResults, upn. |
| Read File | `readFile` | Read (download) the contents of a file, optionally a byte range. GET https://{account}.dfs.core.windows.net/{filesystem}/{path}. Returns the file content (200 OK, or 206 Partial Content for a range). |
| Set Access Control | `setAccessControl` | Set owner, group, POSIX permissions, or ACL on a single file or directory. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=setAccessControl. Values supplied via x-ms-owner/x-ms-group/x-ms-permissions/x-ms-acl headers. Returns 200 OK. |
| Set Access Control Recursive | `setAccessControlRecursive` | Set/modify/remove ACLs recursively on a directory and its contents. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=setAccessControlRecursive&mode={mode}. ACL supplied via x-ms-acl header. Returns 200 OK with counts. |
| Set Filesystem Properties | `setFilesystemProperties` | Set user-defined properties for a filesystem. PATCH https://{account}.dfs.core.windows.net/{filesystem}?resource=filesystem. Properties supplied via x-ms-properties header. |
| Set Path Properties | `setPathProperties` | Set system/user-defined properties (HTTP headers, metadata) on a file or directory. PATCH https://{account}.dfs.core.windows.net/{filesystem}/{path}?action=setProperties. Properties supplied via x-ms-properties header. Returns 200 OK. |
