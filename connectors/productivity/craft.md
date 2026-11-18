---
description: "Craft is a document and note-taking workspace."
hidden: true
---

# Craft

<img src="../../.gitbook/assets/connectors/lg/craft.png" alt="Craft logo">

Craft is a document and note-taking workspace. This connector wraps the Craft Connect Space API to manage documents, folders, blocks (document content), tasks, collections (structured tables) with their items, views and schemas, comments, and whiteboards across an entire Craft space.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [craft.do](https://craft.do) |
| **Authentication** | Credentials you enter |
| **Slug** | `craft` |

## Use it

Add Craft from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.craft.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Collection Items | `addCollectionItems` | Adds new items (rows) to a collection. Each item should match the collection's schema. Two-way relations sync automatically - set only one side. |
| Add Comments | `addComments` | Adds comments to blocks. Experimental Craft endpoint. |
| Add Tasks | `addTasks` | Creates new tasks in the inbox, a Daily Note, or a specific document. Tasks can include schedule dates, deadlines and repeat configuration. |
| Add Whiteboard Elements | `addWhiteboardElements` | Appends Excalidraw elements to a whiteboard without removing existing ones. Experimental Craft endpoint. |
| Create Collection | `createCollection` | Creates a new collection (structured table) in any document, defining its schema (name and typed columns) and insert position. Experimental Craft endpoint. |
| Create Collection View | `createCollectionView` | Creates a collection view definition (table, gallery, or kanban). Stores configuration only. Kanban requires exactly one group rule. Experimental Craft endpoint. |
| Create Documents | `createDocuments` | Creates one or more documents in the Craft space at the given destination ('unsorted' by default, 'templates', or a folder). Cannot create in trash. |
| Create Folders | `createFolders` | Creates one or more folders at the root level or nested inside an existing folder. Cannot create inside built-in locations. |
| Create Whiteboard | `createWhiteboard` | Creates a new empty whiteboard block at a target position. Use Add Whiteboard Elements to populate it. Experimental Craft endpoint. |
| Delete Blocks | `deleteBlocks` | Deletes blocks from any document in the space by their IDs. |

<details>

<summary>See 30 more actions</summary>

* **Delete Collection Items** `deleteCollectionItems`: Deletes items (rows) from a collection, including the content inside each item.
* **Delete Collection View** `deleteCollectionView`: Deletes one collection view definition by view ID. Cannot delete the last stored view. If the active view is deleted, the first remaining view becomes active. Experimental Craft endpoint.
* **Delete Documents** `deleteDocuments`: Soft-deletes documents by moving them to trash. Use Move Documents to restore them.
* **Delete Folders** `deleteFolders`: Deletes folders. Documents and subfolders are moved to the parent folder (or Unsorted for a top-level folder). Cannot delete built-in locations.
* **Delete Tasks** `deleteTasks`: Deletes tasks by their IDs from any location in the space.
* **Delete Whiteboard Elements** `deleteWhiteboardElements`: Removes Excalidraw elements from a whiteboard by their element IDs. Experimental Craft endpoint.
* **Get Blocks** `getBlocks`: Fetches the content (blocks) of any document or page in the space by its ID. A document ID is the same as its root block ID. Optionally fetch a Daily Note by date instead.
* **Get Collection Items** `getCollectionItems`: Gets all items (rows) from a collection.
* **Get Collection Schema** `getCollectionSchema`: Gets a collection's schema, in either the editable collection-schema structure or JSON-Schema form.
* **Get Connection Info** `getConnectionInfo`: Returns connection metadata: space ID and name, timezone, current time, and URL templates for constructing deep links to blocks.
* **Get Tasks** `getTasks`: Retrieves tasks from across the space by scope. Use scope 'document' with a documentId for a specific document; scope 'all' returns every task block in the whole space.
* **Get Whiteboard Elements** `getWhiteboardElements`: Gets all Excalidraw elements and app state from a whiteboard block. Experimental Craft endpoint.
* **Insert Blocks** `insertBlocks`: Inserts content into any document in the space at a target position (inside a parent page, relative to a sibling block, or in a Daily Note). Provide structured 'blocks' or a raw 'markdown' string. Returns the inserted blocks with their new IDs.
* **List Collection Views** `listCollectionViews`: Lists the table, gallery and kanban view definitions for a collection (configuration only; does not execute filters/sorts or return items). Experimental Craft endpoint.
* **List Collections** `listCollections`: Lists collections (structured tables) across the entire space, or within specific documents.
* **List Documents** `listDocuments`: Lists documents across the Craft space. Without a location or folderId filter, returns all documents in the space (may be large); use List Folders first to see available locations and document counts.
* **List Folders** `listFolders`: Lists all locations in the space with document counts, including built-in locations (Unsorted, Trash, Templates) and user-created folders with their hierarchy.
* **Move Blocks** `moveBlocks`: Moves blocks to reorder them within a document or move them between documents across the space.
* **Move Documents** `moveDocuments`: Moves documents between locations in the space (also used to restore documents from trash). Destination cannot be trash - use Delete Documents instead. Daily notes cannot be moved.
* **Move Folders** `moveFolders`: Moves folders within the hierarchy, to the root or inside another folder. Cannot move built-in locations.
* **Search Documents** `searchDocuments`: Searches content across all documents in the space with relevance-based ranking (top 20 results). At least one 'include' term or 'regexps' pattern is required. Supports date-range and location filters.
* **Search Within Document** `searchInDocument`: Searches within a single document or page. Use Search Documents first to find a document, then this action for surrounding context (before/after blocks).
* **Set Active Collection View** `setActiveCollectionView`: Sets which stored view is marked as the collection's active view. Does not execute the view or change items. Experimental Craft endpoint.
* **Update Blocks** `updateBlocks`: Updates content in any document in the space. Provide each block's ID and only the fields to change (e.g. updated markdown, styling, task info). Only provided fields are updated.
* **Update Collection Items** `updateCollectionItems`: Updates items (rows) in a collection. Each item needs an id and the properties to change. Two-way relations sync automatically - set only one side.
* **Update Collection Schema** `updateCollectionSchema`: Replaces a collection's schema entirely - include all fields to keep. Keep property keys stable for existing properties. Experimental Craft endpoint.
* **Update Collection View** `updateCollectionView`: Updates one collection view definition by view ID. Omitted settings are preserved; pass empty arrays/objects to clear list-like settings. Experimental Craft endpoint.
* **Update Tasks** `updateTasks`: Updates existing tasks across the space - content, state, schedule dates, deadlines, repeat, and location (to move tasks). Marking inbox tasks done/canceled moves them to the logbook.
* **Update Whiteboard Elements** `updateWhiteboardElements`: Updates specific Excalidraw elements in a whiteboard by their ID. Elements not included remain unchanged. Experimental Craft endpoint.
* **Upload File** `uploadFile`: Uploads a file and inserts it at a target position (a page, a Daily Note date, or relative to a sibling block). Send the file's raw bytes as the request body. Note: the fastn executor sends the body as text, so binary files may be corrupted - reliable for text-based files.

</details>
