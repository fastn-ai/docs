---
description: "AlgoDocs document data extraction API."
hidden: true
---

# AlgoDocs

<img src="../../.gitbook/assets/connectors/lg/algodocs.png" alt="AlgoDocs logo">

Upload invoices, receipts, bank statements, purchase orders and other PDFs or images to a trained extractor, then read back the structured fields plus JSON, Excel, XML, TXT and CSV outputs. Base URL https://api.algodocs.com/v1.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [algodocs.com](https://algodocs.com) |
| **Authentication** | API key, Basic auth |
| **Slug** | `algodocs` |

## Use it

Add AlgoDocs from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.algodocs.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Document</td><td><code>deleteDocument</code></td><td>Permanently removes an uploaded AlgoDocs document and its extraction results. Undocumented in the AlgoDocs API reference but proven live: POST is the only verb the route accepts, GET/PUT/DELETE return 405 while a nonsense sibling path returns the host 404. Deletion cannot be undone - confirm with Get Extracted Data By Document afterwards.</td></tr><tr><td>Download Document Output File</td><td><code>downloadDocumentOutput</code></td><td>Downloads one page of an AlgoDocs document in a chosen output format - the original file, or the Excel, JSON, XML, TXT or CSV rendering. The media token comes from the mediaOriginal/mediaExcel/mediaJson/mediaXml/mediaTxt/mediaCsv links on an extraction record. SECURITY: AlgoDocs serves this route without any credential, so anyone holding the link can read the document.</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Returns the full name and email of the AlgoDocs account tied to the supplied credentials. Useful as a health check that authentication is wired up correctly.</td></tr><tr><td>Get Extracted Data By Document</td><td><code>getExtractedDataByDocument</code></td><td>Returns the extraction result for a single AlgoDocs document as a list - one record per page or split section, each with its own pageNumber out of totalPages. Extraction is asynchronous, so poll this action after an upload until the data object is populated. Note that a document whose type the classifier cannot recognise still returns 200, with data.error set instead of the extracted fields.</td></tr><tr><td>Get Extracted Data By Extractor</td><td><code>getExtractedDataByExtractor</code></td><td>Returns extraction results for every document processed by one AlgoDocs extractor, newest records included, optionally narrowed to a folder, to uploads after a given date, or to a maximum record count. Each record carries the extracted data object plus download links for the original file and the Excel, JSON, XML, TXT and CSV outputs.</td></tr><tr><td>List Extractors</td><td><code>listExtractors</code></td><td>Lists every extractor configured on the AlgoDocs account. An extractor is the trained configuration that decides which fields are pulled from a document type. Use the returned id as the extractor_id when uploading a document. Extractors can only be created in the AlgoDocs web dashboard - the API has no create route.</td></tr><tr><td>List Folders</td><td><code>listFolders</code></td><td>Lists the AlgoDocs folders on the account, with the document and page totals held in each. Use a returned folder id as the folder_id when uploading a document or as the folderId filter when listing extracted data. Folders can only be created in the AlgoDocs web dashboard - the API has no create route.</td></tr><tr><td>List Folders Including All Bucket</td><td><code>listFoldersIncludingAll</code></td><td>Undocumented AlgoDocs variant of the folder list that takes a numeric flag. Passing 1 prepends the synthetic "All" bucket (id "all") that aggregates every folder; any other number returns the same list as List Folders. Proven live against api.algodocs.com; a nonsense sibling path returns the host's 404, so this route is real.</td></tr><tr><td>Upload Document As Base64</td><td><code>uploadDocumentBase64</code></td><td>Submits a document to an AlgoDocs extractor as a base64-encoded string plus a filename. Returns the new document id, file size, MD5 checksum and upload timestamp. Extraction is asynchronous - poll Get Extracted Data By Document with the returned id until its data object is populated. Use this route when the file is not reachable by URL.</td></tr><tr><td>Upload Document From URL</td><td><code>uploadDocumentFromUrl</code></td><td>Submits a publicly reachable PDF or image URL to an AlgoDocs extractor for extraction. Returns the new document id, file size, MD5 checksum and upload timestamp. Extraction is asynchronous - poll Get Extracted Data By Document with the returned id until its data object is populated. This is the preferred upload route because it needs no binary file transfer.</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Upload Local Document File</td><td><code>uploadLocalDocument</code></td><td>Uploads a document to an AlgoDocs extractor as a multipart file part. Returns the new document id, file size, MD5 checksum and upload timestamp; extraction is asynchronous, so poll Get Extracted Data By Document afterwards. LIMITATION: the fastn engine can only carry text multipart parts, so this route works for text-safe payloads (for example an ASCII-only PDF) but not for raw binary PDF, PNG or JPEG bytes. For binary files use Upload Document As Base64 or Upload Document From URL instead.</td></tr></tbody></table>

</details>
