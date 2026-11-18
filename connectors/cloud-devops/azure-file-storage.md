---
description: "Azure File Storage — cloud file shares over SMB/NFS."
hidden: true
---

# Azure File Storage

<img src="../../.gitbook/assets/connectors/azure-file-storage.png" alt="Azure File Storage logo" width="64">

Azure File Storage — cloud file shares over SMB/NFS. List files and directories in a share, read file content, create files, and append content to existing files via the Azure Files REST API ({account}.file.core.windows.net).

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [file.core.windows.net](https://file.core.windows.net) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `azureFileStorage` |

## Use it

Add Azure File Storage from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.azureFileStorage.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Abort Copy File | `abortCopyFile` | Aborts a pending asynchronous file copy and leaves the destination file with zero length and full metadata. Requires the copy identifier, which Copy File returns only in a response header this engine does not surface, so the identifier must be obtained out of band. |
| Copy File | `copyFile` | Starts an asynchronous server-side copy of a source file or blob to a destination file. Engine limitation: the copy identifier and status are returned only in the x-ms-copy-id and x-ms-copy-status response headers, which this engine does not surface, so a copy cannot be polled or aborted from this action's output. |
| Create Directory | `createDirectory` | Creates a new directory directly under the specified share. On SMB shares the file attribute and timestamp headers are optional from x-ms-version 2021-06-08 onward and default to Directory attributes with server-set timestamps. Engine limitation: the request builder percent-encodes a forward slash inside a path input to %2F, so directoryPath must be a single directory name; nested paths such as parent/child cannot be expressed and only directories immediately under the share root can be created. |
| Create File | `createFile` | Creates a new file of the given size within a share or directory. This reserves the byte range but writes no content; use Put Range to write data into the file. An existing file at the same path is overwritten and its content discarded. |
| Create Hard Link | `createHardLink` | Creates a hard link to an existing file within the same share. Available only on NFS file shares, which require a premium file storage account; on an SMB share Azure rejects this operation. |
| Create Share | `createShare` | Creates a new file share under the specified storage account. Share names must be lowercase, 3 to 63 characters, and may contain hyphens. |
| Create Share Snapshot | `createShareSnapshot` | Creates a read-only point-in-time snapshot of a file share. Engine limitation: the snapshot's DateTime identifier is returned only in the x-ms-snapshot response header, which this engine does not surface, so a successful call returns HTTP 201 with an empty body. Recover the identifier by calling List Shares with include set to snapshots and reading the Snapshot element of the matching Share. |
| Create Symbolic Link | `createSymbolicLink` | Creates a symbolic link pointing at a target path. Available only on NFS file shares, which require a premium file storage account; on an SMB share Azure rejects this operation. |
| Delete Directory | `deleteDirectory` | Deletes an empty directory from a file share. The directory must contain no files or subdirectories, otherwise Azure returns 409 DirectoryNotEmpty. directoryPath must be a single path segment because the request builder percent-encodes forward slashes. |
| Delete File | `deleteFile` | Immediately deletes a file from a file share. The delete is not reversible unless share soft-delete retention is enabled on the storage account. |

<details>

<summary>See 33 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Share | `deleteShare` | Marks a file share or share snapshot for deletion; the share and any files it contains are removed during garbage collection. Supply shareSnapshot to delete a single snapshot instead of the share itself. |
| Force Close Directory Handles | `forceCloseDirectoryHandles` | Forcibly closes open SMB handles on a directory, and optionally on everything beneath it. Pass an asterisk as handleId to close every handle. Engine limitation: the number of handles closed is returned only in the x-ms-number-of-handles-closed response header, which this engine does not surface. |
| Force Close File Handles | `forceCloseFileHandles` | Forcibly closes open SMB handles on a file. Pass an asterisk as handleId to close every handle on the file. Engine limitation: the number of handles closed is returned only in the x-ms-number-of-handles-closed response header, which this engine does not surface. |
| Get Directory Metadata | `getDirectoryMetadata` | Returns all user-defined metadata for a directory. Engine limitation: Azure returns metadata in x-ms-meta-{name} response headers, which this engine does not surface, so a successful call returns HTTP 200 with an empty body. |
| Get Directory Properties | `getDirectoryProperties` | Returns all system properties and user-defined metadata for a directory. Engine limitation: Azure returns every property in x-ms-* response headers, which this engine does not surface, so a successful call returns HTTP 200 with an empty body. directoryPath must be a single path segment because the request builder percent-encodes forward slashes. |
| Get File | `getFile` | Reads the content of a file, optionally restricted to a byte range. Text files round-trip correctly; binary content is corrupted by the engine's UTF-8 expansion of non-UTF-8 bytes, so this action is reliable for text files only. |
| Get File Metadata | `getFileMetadata` | Returns all user-defined metadata for a file. Engine limitation: Azure returns metadata in x-ms-meta-{name} response headers, which this engine does not surface, so a successful call returns HTTP 200 with an empty body. |
| Get File Service Properties | `getFileServiceProperties` | Gets the properties of the File service on a storage account, including hour and minute metrics, CORS rules, share soft-delete retention and SMB protocol settings. Returns an XML StorageServiceProperties document. |
| Get Share ACL | `getShareAcl` | Returns the stored access policies specified on a file share, which can be used with shared access signatures. Returns an XML SignedIdentifiers document. |
| Get Share Metadata | `getShareMetadata` | Returns all user-defined metadata for a file share. Engine limitation: Azure returns metadata in x-ms-meta-{name} response headers, which this engine does not surface, so a successful call returns HTTP 200 with an empty body. |
| Get Share Properties | `getShareProperties` | Returns all user-defined metadata and system properties of a file share, including quota, access tier and enabled protocols. Engine limitation: Azure returns every property in x-ms-* response headers, which this engine does not surface, so a successful call returns HTTP 200 with an empty body. |
| Get Share Stats | `getShareStats` | Returns the approximate size of the data stored on a file share, rounded up to the nearest gibibyte. Returns an XML ShareStats document. |
| Lease File | `leaseFile` | Manages a lock on a file for write and delete operations. Supports the acquire, change, release and break lease actions. File leases are always infinite, so leaseDuration must be -1 on acquire; Azure returns 400 MissingRequiredHeader if it is omitted. Engine limitation: the lease identifier is returned only in the x-ms-lease-id response header, which this engine does not surface, so an acquired lease id must be supplied by the caller rather than read from this action's output. |
| Lease Share | `leaseShare` | Manages a lock on a file share to prevent it being deleted. Supports the acquire, renew, change, release and break lease actions. Engine limitation: the lease identifier is returned only in the x-ms-lease-id response header, which this engine does not surface, so an acquired lease id must be supplied by the caller rather than read from this action's output. |
| List Directories And Files | `listDirectoriesAndFiles` | Returns the directories and files under the specified share or directory. Pass an empty directoryPath to list the share root. Engine limitation: the request builder percent-encodes a forward slash inside a path input to %2F, so directoryPath must be a single directory name; nested paths such as parent/child cannot be enumerated. |
| List Directory Handles | `listDirectoryHandles` | Returns the open SMB handles on a directory, and optionally on everything beneath it. Returns an XML EnumerationResults document listing each handle with its HandleId, Path, ClientIp and OpenTime. |
| List File Handles | `listFileHandles` | Returns the open SMB handles on a file. Returns an XML EnumerationResults document listing each handle with its HandleId, Path, ClientIp and OpenTime. |
| List Ranges | `listRanges` | Returns the list of valid byte ranges that contain data for a file. Optionally diffs against a share snapshot to return only the ranges that changed. Returns an XML Ranges document. |
| List Shares | `listShares` | Returns a list of the file shares and share snapshots under the specified Azure Storage account. Returns an XML EnumerationResults document. |
| Put Range | `putRange` | Writes content into a byte range of an existing file, or clears a range. The file must already exist and be large enough; create it first with Create File. Engine limitation: request bodies are UTF-8 encoded, so binary content is corrupted and only text content can be written reliably. |
| Put Range From URL | `putRangeFromUrl` | Writes a byte range into a file by copying it directly from another file or blob URL, without routing the data through the caller. Avoids the engine's text-only body limitation because the content never passes through the request body. |
| Read Symbolic Link | `readSymbolicLink` | Returns the target path a symbolic link points at. Available only on NFS file shares, which require a premium file storage account. Engine limitation: the target is returned only in the x-ms-link-text response header, which this engine does not surface, so a successful call returns an empty body. |
| Rename Directory | `renameDirectory` | Renames a directory within the same file share. The destination is supplied as the directory to create; the directory's current location is supplied as sourceDirectoryPath, a path relative to the share root. sourceDirectoryPath is sent inside a header URI rather than as a URL segment, so it may contain forward slashes and address a nested directory. |
| Rename File | `renameFile` | Renames a file within the same file share. The destination is supplied as the directory and file name to create; the file's current location is supplied as sourceFilePath, a full path relative to the share root. sourceFilePath is sent as a header rather than a URL segment, so unlike the URL path inputs it may contain forward slashes and address a nested directory. |
| Restore Share | `restoreShare` | Restores a previously soft-deleted file share. Requires share soft-delete retention to be enabled on the storage account, and the deleted share's name and version, which are obtained from List Shares with include set to deleted. |
| Set Directory Metadata | `setDirectoryMetadata` | Sets one user-defined metadata name-value pair on a directory. Engine limitation: metadata is carried in dynamically-named x-ms-meta-{name} headers which the templating layer cannot generate, so this action exposes a single fixed header x-ms-meta-value; calling it replaces all existing metadata on the directory. |
| Set Directory Properties | `setDirectoryProperties` | Sets the SMB system properties of a directory, including its file system attributes, creation and last write timestamps, and security descriptor. |
| Set File Metadata | `setFileMetadata` | Sets one user-defined metadata name-value pair on a file. Engine limitation: metadata is carried in dynamically-named x-ms-meta-{name} headers which the templating layer cannot generate, so this action exposes a single fixed header x-ms-meta-value; calling it replaces all existing metadata on the file. |
| Set File Properties | `setFileProperties` | Sets the system properties of a file, including its HTTP content headers, SMB attributes and timestamps, and can resize the file. Shrinking a file with contentLength truncates and discards the bytes beyond the new size. |
| Set File Service Properties | `setFileServiceProperties` | Sets the properties of the File service on a storage account, controlling hour metrics and the share soft-delete retention policy. This rewrites account-wide service configuration and affects every file share in the account. Engine limitation: the templating layer has no loop construct, so CORS rules cannot be expressed and are omitted from the request, which clears any existing CORS configuration. |
| Set Share ACL | `setShareAcl` | Sets a stored access policy on a file share for use with shared access signatures. Engine limitation: the templating layer has no loop construct, so exactly one stored access policy can be set per call; the Azure API accepts up to five and this call replaces all existing policies with the single one supplied. |
| Set Share Metadata | `setShareMetadata` | Sets one user-defined metadata name-value pair on a file share. Engine limitation: metadata is carried in dynamically-named x-ms-meta-{name} headers which the templating layer cannot generate, so this action exposes a single fixed header x-ms-meta-value whose value you supply; calling it replaces all existing metadata on the share. |
| Set Share Properties | `setShareProperties` | Sets the properties of a file share, including its quota in gibibytes and its access tier. |

</details>
