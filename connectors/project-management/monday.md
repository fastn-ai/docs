---
description: "Monday.com Work OS GraphQL API connector."
---

# Monday.com

Monday.com Work OS GraphQL API connector. Single endpoint https://api.monday.com/v2 (all POST). Manage boards, groups, items, subitems, columns, updates, users, teams, workspaces, tags, docs, notifications and webhooks.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [monday.com](https://monday.com) |
| **Authentication** | Bearer token |
| **Actions** | 50 |
| **Events** | 20 |
| **Slug** | `monday` |

## Use it

Add Monday.com from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.monday.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Board | `archiveBoard` | Archive a board by id. Returns the board id and new state. |
| Archive Group | `archiveGroup` | Archive a group in a board. Returns the group id and archived flag. |
| Archive Item | `archiveItem` | Archive an item by id. Returns the item id and new state. |
| Change Column Metadata | `changeColumnMetadata` | Change a column's metadata attribute (title or description). column_property is one of title, description. Returns the updated column. |
| Change Column Title | `changeColumnTitle` | Change the title of a column. Returns the column id and new title. |
| Change Multiple Column Values | `changeColumnValues` | Update multiple column values of an item at once. column_values is a JSON-encoded string mapping column ids to values. Returns updated item. |
| Change Simple Column Value | `changeSimpleColumnValue` | Update a single column value using a plain string value (simpler than JSON). Returns updated item. |
| Change Single Column Value | `changeColumnValue` | Update a single column value of an item. value is a JSON-encoded string for that column type. Returns updated item. |
| Create Board | `createBoard` | Create a new board. board_kind is one of public, private, share. Returns the new board id and name. |
| Create Column | `createColumn` | Create a column on a board. column_type is a ColumnType enum (e.g. text, status, numbers, date, people, dropdown, checkbox, long_text, email, phone, link, timeline, tags). Returns the new column id, title and type. |
| Create Doc | `createDoc` | Creates a monday doc in a workspace, with its sharing kind set explicitly. |
| Create Group | `createGroup` | Create a new group in a board. Returns the new group id and title. |
| Create Item | `createItem` | Create a new item on a board. column_values is a JSON-encoded string mapping column ids to values (per monday column-value formats). Returns the new item id and name. |
| Create Notification | `createNotification` | Send a notification to a user. target_type is one of Project (item/board) or Post (update). Returns the notification id and text. |
| Create or Get Tag | `createOrGetTag` | Create a new tag or get an existing one by name (create_or_get_tag). Returns the tag id, name and color. |
| Create Subitem | `createSubitem` | Create a subitem under a parent item. column_values is a JSON-encoded string. Returns the new subitem id, name and its board id. |
| Create Update | `createUpdate` | Create an update (post) on an item. Returns the new update id and body. |
| Create Webhook | `createWebhook` | Register a webhook on a board for a given event (e.g. create_item, change_column_value, create_update). Returns the new webhook id, board_id and event. |
| Create Workspace | `createWorkspace` | Create a workspace. kind is one of open, closed. Returns the new workspace id, name and kind. |
| Delete Board | `deleteBoard` | Delete a board by id. Returns the board id and new state. |
| Delete Column | `deleteColumn` | Delete a column from a board. Returns the deleted column id and title. |
| Delete Group | `deleteGroup` | Delete a group from a board. Returns the group id and deleted flag. |
| Delete Item | `deleteItem` | Delete an item by id. Returns the item id and new state. |
| Delete Update | `deleteUpdate` | Delete an update by id. Returns the deleted update id. |
| Delete Webhook | `deleteWebhook` | Delete a registered webhook by id. Returns the deleted webhook id and board_id. |
| Delete Workspace | `deleteWorkspace` | Delete a workspace by id. Returns the deleted workspace id. |
| Duplicate Board | `duplicateBoard` | Duplicate an existing board. duplicate_type is one of duplicate_board_with_structure, duplicate_board_with_pulses, duplicate_board_with_pulses_and_updates. |
| Duplicate Group | `duplicateGroup` | Duplicate a group within its board. Returns the new group id and title. |
| Get Board | `getBoard` | Get a single board by id, including its columns, groups, owners and workspace. |
| Get Item | `getItem` | Get one or more items by id, including column values, group, board, creator and updates. |
| Get Me | `getMe` | Get the currently authenticated user (me). Returns id, name, email, account and is_admin. |
| Like Update | `likeUpdate` | Like an update by id. Returns the update id. |
| List Board Views | `listBoardViews` | Lists the views configured on a board, including each view's name, type and settings. |
| List Boards | `listBoards` | Query boards. Returns boards with id, name, state, board_kind, description, and workspace. Supports pagination via limit and page. |
| List Columns | `listColumns` | List the columns of a board. Returns each column's id, title, type, description and settings_str. |
| List Docs | `listDocs` | List docs with pagination. Returns id, object_id, name, doc_kind, created_at and the workspace. |
| List Folders | `listFolders` | Lists the folders in the account, optionally limited to one workspace, with their names, colors and parent folders. |
| List Groups | `listGroups` | List the groups of a board. Returns each group's id, title, color and position. |
| List Items (Items Page) | `listItems` | List items on a board using items_page with pagination. Returns a cursor and the items with id, name, state and column values. |
| List Items By Column Values | `listItemsByColumnValues` | Finds items on a board whose column holds one of the supplied values, returning a page of matching items with their column values. |
| List Tags | `listTags` | List public (account-level) tags by ids, or all when omitted. Returns id, name and color. |
| List Teams | `listTeams` | List teams in the account. Returns id, name, picture_url and members. |
| List Updates | `listUpdates` | List updates (posts) across the account or for a specific item, with pagination. Returns update id, body, creator and created_at. |
| List Users | `listUsers` | List users in the account with pagination. Returns id, name, email, enabled, is_admin, is_guest. |
| List Webhooks | `listWebhooks` | List the webhooks registered on a board. Returns each webhook id, event, board_id and config. |
| List Workspaces | `listWorkspaces` | List workspaces with pagination. Returns id, name, kind and description. |
| Move Item To Board | `moveItemToBoard` | Move an item to a different board and group. Returns the moved item id. |
| Move Item To Group | `moveItemToGroup` | Move an item to a different group on the same board. Returns the item id. |
| Update Board | `updateBoard` | Update a board attribute. board_attribute is one of name, description, communication. Returns a JSON string result. |
| Update Group | `updateGroup` | Update a group attribute. group_attribute is one of title, color, position, relative_position_after, relative_position_before. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Column Created | `create_column` | A new column is created on the board. |
| Column Deleted | `delete_column` | A column is deleted from the board. |
| Column Value Changed | `change_column_value` | Any column value on an item changes. |
| Item Archived | `item_archived` | An item is archived. |
| Item Created | `create_item` | A new item is created on the board. |
| Item Deleted | `item_deleted` | An item is deleted. |
| Item Moved To Any Group | `item_moved_to_any_group` | An item is moved to any group. |
| Item Moved To Specific Group | `item_moved_to_specific_group` | An item is moved to a specific (chosen) group. |
| Item Name Changed | `change_name` | An item's name changes. |
| Specific Column Changed | `change_specific_column_value` | A specific column (chosen at subscription) value changes. |
| Status Column Changed | `change_status_column_value` | A status column value changes. |
| Subitem Archived | `subitem_archived` | A subitem is archived. |
| Subitem Column Changed | `change_subitem_column_value` | A subitem column value changes. |
| Subitem Created | `create_subitem` | A new subitem is created. |
| Subitem Deleted | `subitem_deleted` | A subitem is deleted. |
| Subitem Moved | `move_subitem` | A subitem is moved. |
| Subitem Name Changed | `change_subitem_name` | A subitem's name changes. |
| Update Created | `create_update` | A new update/post is created on an item. |
| Update Deleted | `delete_update` | An update is deleted. |
| Update Edited | `edit_update` | An existing update is edited. |
