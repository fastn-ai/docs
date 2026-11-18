---
description: "Miro REST API v2 connector — boards (CRUD/copy), board members & sharing, all item types (generic items, app cards, cards, documents, embeds, images, shapes,…"
---

# Miro

Miro REST API v2 connector — boards (CRUD/copy), board members & sharing, all item types (generic items, app cards, cards, documents, embeds, images, shapes, sticky notes, text, frames), connectors, tags, item groups, bulk operations, board export, mind-map & flowchart items (experimental), and webhook board subscriptions (experimental). Base https://api.miro.com/v2.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [miro.com](https://miro.com) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Actions** | 123 |
| **Events** | 3 |
| **Slug** | `miro` |

## Use it

Add Miro from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.miro.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Attach Tag To Item | `attachTagToItem` | Attach a tag to an item. POST /v2/boards/{board_id}/items/{item_id}?tag_id=. No body. |
| Copy Board | `copyBoard` | Create a copy of an existing board. The copy_from query param identifies the source board; the body can override name, description, policy, and teamId. |
| Create app card item | `createAppCardItem` | Create an app card item on a board. App cards display title, description, and custom preview fields. |
| Create Board | `createBoard` | Create a new Miro board. Optionally set name, description, sharing/permissions policy, team, and project. |
| Create Board Export Job | `createBoardExportJob` | Create a board export job (Enterprise). POST /v2/orgs/{org_id}/boards/export/jobs?request_id=. |
| Create Board Export Task Export Link | `createBoardExportTaskExportLink` | Create a download export link for a board export task (Enterprise). POST /v2/orgs/{org_id}/boards/export/jobs/{job_id}/tasks/{task_id}/export-link. |
| Create Board Subscription (Webhook) | `createBoardSubscription` | DEPRECATED: Create an experimental webhook subscription for a board. NOTE: Miro discontinued the /v2-experimental/webhooks/board_subscriptions endpoint on December 5, 2025. This action will return 500. The entire experimental webhooks infrastructure has been shut down by Miro. See: https://developers.miro.com/changelog/removed-experimental-webhooks-support |
| Create card item | `createCardItem` | Create a card item on a board. Cards hold a title, description, due date, and assignee. |
| Create Code Widget Item | `createCodeWidgetItem` | Create a code widget item (experimental). POST /v2-experimental/boards/{board_id}/code_widgets. data {code, language, lineNumbersVisible, title}. |
| Create Connector | `createConnector` | Create a connector (line) between two items on a board. POST /v2/boards/{board_id}/connectors. |
| Create document item using URL | `createDocumentItemUsingUrl` | Create a document item on a board from a hosted document URL (e.g. a PDF). |
| Create embed item | `createEmbedItem` | Create an embed item on a board from a valid content URL (e.g. a YouTube video). |
| Create Flowchart Shape | `createFlowchartShape` | Create a flowchart shape item (experimental). POST /v2-experimental/boards/{board_id}/shapes. data {content, shape}. |
| Create Frame | `createFrame` | Create a frame on a Miro board. POST /v2/boards/{board_id}/frames. Body nests data (title/format/type/showContent), style (fillColor), position (x,y), geometry (width,height). |
| Create Group | `createGroup` | Create a group of items on a board. POST /v2/boards/{board_id}/groups. |
| Create Group (SCIM) | `createScimGroup` | Create a new SCIM group. Requires Enterprise plan with SCIM provisioning token. |
| Create image item using URL | `createImageItemUsingUrl` | Create an image item on a board from a hosted image URL. |
| Create Items In Bulk | `createItemsBulk` | Create multiple items in a single call. POST /v2/boards/{board_id}/items/bulk. Body is a JSON array of item objects (each with type/data/style/position/geometry/parent). |
| Create Items In Bulk Using File | `createItemsBulkFile` | Create items in bulk using files from device (multipart/form-data). POST /v2/boards/{board_id}/items/bulk. BLOCKED: Miro requires binary file content (PDFs, images) uploaded as multipart/form-data parts in 'resources'. fastn's tool executor cannot supply binary file attachments — multipart file upload with binary content is not supported. The JSON-only variant (createItemsBulk) is the recommended alternative for JSON-typed items. configHealthy:true confirmed (auth injection and URL routing work correctly). |
| Create Mind Map Node | `createMindmapNode` | Create a mind map node (experimental). POST /v2-experimental/boards/{board_id}/mindmap_nodes. data nests nodeView.data {type:'text',content:'...'}. |
| Create shape item | `createShapeItem` | Create a shape item (rectangle, circle, flowchart shapes, etc.) on a board. |
| Create sticky note item | `createStickyNoteItem` | Create a sticky note item on a board with content, shape, and color. |
| Create Tag | `createTag` | Create a tag on a board. POST /v2/boards/{board_id}/tags. |
| Create text item | `createTextItem` | Create a text item on a board. |
| Create User (SCIM) | `createUser` | Enterprise SCIM: provision a new user in the organization. Requires Enterprise plan + SCIM token. |
| Delete app card item | `deleteAppCardItem` | Delete an app card item from a board by its item ID. |
| Delete Board | `deleteBoard` | Delete a specific board and all its content. This is a soft delete; the board can be restored within a retention period. |
| Delete card item | `deleteCardItem` | Delete a card item from a board by its item ID. |
| Delete Code Widget Item | `deleteCodeWidgetItem` | Delete a code widget item (experimental). DELETE /v2-experimental/boards/{board_id}/code_widgets/{item_id}. |
| Delete Connector | `deleteConnector` | Delete a connector. DELETE /v2/boards/{board_id}/connectors/{connector_id}. |
| Delete document item | `deleteDocumentItem` | Delete a document item from a board by its item ID. |
| Delete embed item | `deleteEmbedItem` | Delete an embed item from a board by its item ID. |
| Delete Flowchart Shape | `deleteFlowchartShape` | Delete a flowchart shape item (experimental). DELETE /v2-experimental/boards/{board_id}/shapes/{item_id}. |
| Delete Frame | `deleteFrame` | Delete a frame. DELETE /v2/boards/{board_id}/frames/{item_id}. |
| Delete Group | `deleteGroup` | Delete a group. DELETE /v2/boards/{board_id}/groups/{group_id}?delete_items=true (required). |
| Delete image item | `deleteImageItem` | Delete an image item from a board by its item ID. |
| Delete item | `deleteItem` | Delete an item (any type) from a board by its item ID. |
| Delete item (experimental) | `deleteItemExperimental` | Experimental delete variant. Deletes a single item from a board using the v2-experimental endpoint. Returns a 204 with an empty body on success. |
| Delete Mind Map Node | `deleteMindmapNode` | Delete a mind map node (experimental). DELETE /v2-experimental/boards/{board_id}/mindmap_nodes/{item_id}. |
| Delete Session | `deleteSession` | Delete (revoke) a user session. BLOCKED: Miro does not expose a public v2 REST endpoint at /v2/sessions/{id} — all attempts return 404 'No endpoint'. The sessions:delete OAuth scope is present but the corresponding API endpoint is not publicly accessible in the v2 REST API. Requires Enterprise plan with correct endpoint discovery. |
| Delete shape item | `deleteShapeItem` | Delete a shape item from a board by its item ID. |
| Delete sticky note item | `deleteStickyNoteItem` | Delete a sticky note item from a board by its item ID. |
| Delete Tag | `deleteTag` | Delete a tag. DELETE /v2/boards/{board_id}/tags/{tag_id}. |
| Delete text item | `deleteTextItem` | Delete a text item from a board by its item ID. |
| Delete User (SCIM) | `deleteUser` | Enterprise SCIM: delete (deprovision) a user by ID. Requires Enterprise plan + SCIM token. |
| Delete Webhook Subscription | `deleteWebhookSubscription` | BLOCKED: Miro discontinued the entire /v2-experimental/webhooks infrastructure on December 5, 2025. This endpoint returns 500 Internal Error. All webhook subscription management (list/get/create/update/delete) is unavailable until Miro ships a stable replacement API. |
| Get Access Token Information | `getTokenInfo` | Retrieve information about the current OAuth access token, including the organization, team, user (the 'me' context), creator, and granted scopes. |
| Get All Groups | `getAllGroups` | Get all groups on a board. GET /v2/boards/{board_id}/groups. |
| Get app card item | `getAppCardItem` | Retrieve a specific app card item from a board by its item ID. |
| Get Audit Logs | `getAuditLogs` | Retrieve audit log events for a Miro organization. Requires auditlogs:read OAuth scope — Enterprise plan only. |
| Get Board Export Job Results | `getBoardExportJobResults` | Get results for a board export job (Enterprise). GET /v2/orgs/{org_id}/boards/export/jobs/{job_id}/results. |
| Get Board Export Job Status | `getBoardExportJobStatus` | Get the status of a board export job (Enterprise). GET /v2/orgs/{org_id}/boards/export/jobs/{job_id}. |
| Get Board Export Job Tasks | `getBoardExportJobTasks` | Get the list of tasks for a board export job (Enterprise). GET /v2/orgs/{org_id}/boards/export/jobs/{job_id}/tasks. |
| Get Board Export Jobs | `getBoardExportJobs` | Get the list of board export jobs (Enterprise). GET /v2/orgs/{org_id}/boards/export/jobs. |
| Get Board Members | `getBoardMembers` | Retrieve a paginated list of members for a specific board. |
| Get Boards | `getBoards` | Retrieve a list of boards that match the search criteria provided in the request. Supports filtering by team, project, owner, free-text query, and sorting/pagination. |
| Get card item | `getCardItem` | Retrieve a specific card item from a board by its item ID. |
| Get Code Widget Item | `getCodeWidgetItem` | Get a code widget item (experimental). GET /v2-experimental/boards/{board_id}/code_widgets/{item_id}. |
| Get Code Widget Items | `getCodeWidgetItems` | List code widget items on a board (experimental). GET /v2-experimental/boards/{board_id}/code_widgets. |
| Get Connector | `getConnector` | Get a specific connector. GET /v2/boards/{board_id}/connectors/{connector_id}. |
| Get Connectors | `getConnectors` | List connectors on a board (cursor-paginated). GET /v2/boards/{board_id}/connectors. |
| Get document item | `getDocumentItem` | Retrieve a specific document item from a board by its item ID. |
| Get embed item | `getEmbedItem` | Retrieve a specific embed item from a board by its item ID. |
| Get Flowchart Shape | `getFlowchartShape` | Get a flowchart shape item (experimental). GET /v2-experimental/boards/{board_id}/shapes/{item_id}. |
| Get Frame | `getFrame` | Get a specific frame. GET /v2/boards/{board_id}/frames/{item_id}. |
| Get Group (SCIM) | `getGroup` | Enterprise SCIM: retrieve a specific group (team) by its server-assigned ID. Requires Enterprise plan + SCIM token. BLOCKED: cannot retrieve a real group ID without listGroups working (requires Enterprise plan and SCIM token). |
| Get Group By ID | `getGroupById` | Get a group by its ID. GET /v2/boards/{board_id}/groups/{group_id}. |
| Get image item | `getImageItem` | Retrieve a specific image item from a board by its item ID. |
| Get Items (Experimental) | `getItemsExperimental` | Get items on a board, experimental endpoint (supports flowchart shapes). GET /v2-experimental/boards/{board_id}/items. |
| Get Items By Group ID | `getItemsByGroupId` | Get items of a group by its ID. GET /v2/boards/{board_id}/groups/items?group_item_id=. |
| Get Items By Tag | `getItemsByTag` | Get items that have a given tag. GET /v2/boards/{board_id}/items?tag_id=. |
| Get items on board | `getItems` | Retrieve a list of all items on a specific board. Optionally filter by item type and paginate with cursor/limit. |
| Get items within frame | `getItemsWithinFrame` | Get items within a frame |
| Get Mind Map Node | `getMindmapNode` | Get a specific mind map node (experimental). GET /v2-experimental/boards/{board_id}/mindmap_nodes/{item_id}. |
| Get Mind Map Nodes | `getMindmapNodes` | Get mind map nodes on a board (experimental). GET /v2-experimental/boards/{board_id}/mindmap_nodes. |
| Get shape item | `getShapeItem` | Retrieve a specific shape item from a board by its item ID. |
| Get Specific Board | `getSpecificBoard` | Retrieve information about a specific board by its board_id. |
| Get Specific Board Member | `getSpecificBoardMember` | Retrieve information about a specific board member, including their role. |
| Get Specific Item (Experimental) | `getSpecificItemExperimental` | Get a specific item on a board, experimental endpoint. GET /v2-experimental/boards/{board_id}/items/{item_id}. |
| Get specific item on board | `getSpecificItem` | Retrieve information for a specific item (any type) on a board by its item ID. |
| Get sticky note item | `getStickyNoteItem` | Retrieve a specific sticky note item from a board by its item ID. |
| Get Tag | `getTag` | Get a specific tag. GET /v2/boards/{board_id}/tags/{tag_id}. |
| Get Tags From Board | `getTagsFromBoard` | List tags on a board. GET /v2/boards/{board_id}/tags. |
| Get Tags From Item | `getTagsFromItem` | Get tags attached to an item. GET /v2/boards/{board_id}/items/{item_id}/tags. |
| Get text item | `getTextItem` | Retrieve a specific text item from a board by its item ID. |
| Get User (SCIM) | `getUser` | Enterprise SCIM: retrieve a specific user by ID. Requires Enterprise plan + SCIM token. |
| Get Webhook Subscription | `getWebhookSubscription` | BLOCKED: Miro discontinued the entire /v2-experimental/webhooks infrastructure on December 5, 2025. This endpoint returns 500 Internal Error. All webhook subscription management (list/get/create/update/delete) is unavailable until Miro ships a stable replacement API. |
| List Card Items | `listCardItems` | Retrieve all card items on a board. Returns paginated list of cards. |
| List Embed Items | `listEmbedItems` | Retrieve all embed items on a board. |
| List Frames | `listFrames` | Retrieve all frame items on a board. |
| List Groups (SCIM) | `listGroups` | Enterprise SCIM: list groups (teams) in the organization. Requires Enterprise plan + SCIM token. Returns a paginated list of SCIM Group resources. BLOCKED: requires Miro Enterprise plan and a dedicated SCIM provisioning token (not standard OAuth). |
| List sticky note items | `listStickyNoteItems` | Retrieve a list of sticky note items for a specific board. Supports pagination and filtering by limit. |
| List Users (SCIM) | `listUsers` | Enterprise SCIM: list users in the organization. Supports attribute selection, filtering, pagination, and sorting. Requires Enterprise plan + SCIM token. |
| List Webhook Subscriptions | `listWebhookSubscriptions` | BLOCKED: Miro discontinued the entire /v2-experimental/webhooks infrastructure on December 5, 2025. This endpoint returns 500 Internal Error. All webhook subscription management (list/get/create/update/delete) is unavailable until Miro ships a stable replacement API. |
| Move Code Widget Item | `moveCodeWidgetItem` | Move a code widget item to a new position (experimental). PATCH /v2-experimental/boards/{board_id}/code_widgets/{item_id}/position. |
| Patch Group (SCIM) | `patchGroup` | Enterprise SCIM: partially update a group (team) using SCIM PatchOp operations (add/remove/replace members or displayName). Requires Enterprise plan + SCIM token. BLOCKED: cannot obtain a real group ID without listGroups working (requires Enterprise plan and SCIM token). |
| Patch User (SCIM) | `patchUser` | Enterprise SCIM: partially update a user via PatchOp operations (e.g. activate/deactivate). Requires Enterprise plan + SCIM token. |
| Remove Board Member | `removeBoardMember` | Remove a specific member from a board. |
| Remove Tag From Item | `removeTagFromItem` | Remove a tag from an item. DELETE /v2/boards/{board_id}/items/{item_id}?tag_id=. |
| Replace User (SCIM) | `replaceUser` | Enterprise SCIM: fully replace a user resource by ID (PUT). Requires Enterprise plan + SCIM token. |
| Revoke Token | `revokeToken` | Revoke an OAuth access token. POST /v1/oauth/revoke?access_token={token}. BLOCKED: Cannot safely test against the live connection token — revoking it would destroy the active connection. Action is correctly configured (auth header, queryParam injection). Any separately-obtained token can be passed as access_token. |
| Share Board (Invite Members) | `shareBoard` | Share a board with one or more users by email, assigning a role. Optionally include an invitation message. |
| Ungroup Items | `ungroupItems` | Ungroup items (group removed, items optionally kept). DELETE /v2/boards/{board_id}/groups/{group_id}?delete_items=. |
| Update app card item | `updateAppCardItem` | Update an existing app card item's data, style, position, or geometry. |
| Update Board | `updateBoard` | Update a specific board. Modify name, description, policy, team, or project. |
| Update Board Export Job Status | `updateBoardExportJobStatus` | Update a board export job status (Enterprise, only CANCELLED supported). PUT /v2/orgs/{org_id}/boards/export/jobs/{job_id}/status. |
| Update Board Member | `updateBoardMember` | Update the role of a specific board member. |
| Update card item | `updateCardItem` | Update an existing card item's data, style, position, or geometry. |
| Update Code Widget Item | `updateCodeWidgetItem` | Update a code widget item (experimental). PATCH /v2-experimental/boards/{board_id}/code_widgets/{item_id}. |
| Update Connector | `updateConnector` | Update a connector. PATCH /v2/boards/{board_id}/connectors/{connector_id}. |
| Update document item using URL | `updateDocumentItemUsingUrl` | Update an existing document item using a new hosted document URL, position, or geometry. |
| Update embed item | `updateEmbedItem` | Update an existing embed item using a new content URL, position, or geometry. |
| Update Flowchart Shape | `updateFlowchartShape` | Update a flowchart shape item (experimental). PATCH /v2-experimental/boards/{board_id}/shapes/{item_id}. |
| Update Frame | `updateFrame` | Update a frame. PATCH /v2/boards/{board_id}/frames/{item_id}. Body nests data, style, position, geometry. |
| Update Group | `updateGroup` | Update a group with new items. PUT /v2/boards/{board_id}/groups/{group_id}. |
| Update image item using URL | `updateImageItemUsingUrl` | Update an existing image item using a new hosted image URL, position, or geometry. |
| Update item position or parent | `updateItemPositionOrParent` | Update the position of an item on a board, or attach/detach it from a parent frame. |
| Update Mindmap Node | `updateMindmapNode` | [DEPRECATED] Not supported by Miro. The experimental Mind Map API provides Create, Read and Delete only - there is no update operation for a mind map node (https://developers.miro.com/docs/mind-maps, https://community.miro.com/developer-platform-and-apis-57/new-in-the-rest-api-experimental-support-for-mind-maps-create-read-delete-14831). Miro answers 405 {"code":"methodNotSupported","message":"Request method 'PUT' not supported for this endpoint"}. To change a node, delete it and create a replacement. |
| Update shape item | `updateShapeItem` | Update an existing shape item's data, style, position, or geometry. |
| Update sticky note item | `updateStickyNoteItem` | Update an existing sticky note item's data, style, position, or geometry. |
| Update Tag | `updateTag` | Update a tag. PATCH /v2/boards/{board_id}/tags/{tag_id}. |
| Update text item | `updateTextItem` | Update an existing text item's data, style, position, or geometry. |
| Update Webhook Subscription | `updateWebhookSubscription` | BLOCKED: Miro discontinued the entire /v2-experimental/webhooks infrastructure on December 5, 2025. This endpoint returns 405 (method not supported) confirming the route no longer exists. All webhook subscription management (list/get/create/update/delete) is unavailable until Miro ships a stable replacement API. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Board Items Created | `board_items_created` | Fired when one or more items are created on a subscribed board. Payload: {eventType:'board_items_created', event:{boardId, items[]}}. |
| Board Items Deleted | `board_items_deleted` | Fired when one or more items are deleted on a subscribed board. Payload: {eventType:'board_items_deleted', event:{boardId, items[]}}. |
| Board Items Updated | `board_items_updated` | Fired when one or more items are updated on a subscribed board. Payload: {eventType:'board_items_updated', event:{boardId, items[]}}. |
