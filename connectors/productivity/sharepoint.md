---
description: "Microsoft SharePoint via Microsoft Graph v1.0 — sites, lists, list items, columns, content types, document libraries (drives), pages, site permissions,…"
hidden: true
---

# SharePoint

<img src="../../.gitbook/assets/connectors/lg/sharepoint.png" alt="SharePoint logo">

Microsoft SharePoint via Microsoft Graph v1.0 — sites, lists, list items, columns, content types, document libraries (drives), pages, site permissions, followed sites, and change-notification subscriptions (webhooks).

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [sharepoint.com](https://sharepoint.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `sharepoint` |

## Use it

Add SharePoint from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.sharepoint.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Copy Drive Item (Async) | `copyDriveItem` | Copy a driveItem to a target folder (asynchronous). POST /drives/{drive-id}/items/{item-id}/copy. Returns 202 Accepted with a Location header monitor URL (no 200 body). Only parentReference is templated; supply it to choose the destination. |
| Create Folder / Child Item | `createDriveItemChild` | Create a new folder (or child driveItem) inside a folder. POST /drives/{drive-id}/items/{parent-id}/children. Body marks it as a folder via empty folder object. Returns the created driveItem. |
| Create List | `createList` | Create a new list in a SharePoint site. POST /sites/{site-id}/lists. Requires displayName; optional columns array and list.template. Scope Sites.Manage.All. |
| Create List Column | `createListColumn` | Create a column on a list. POST /sites/{site-id}/lists/{list-id}/columns. Requires name plus exactly ONE type facet, supplied via typeFacetName + typeFacet. |
| Create List Item | `createListItem` | Create a new item in a SharePoint list. The 'fields' object maps column internal names to typed values. Returns the created listItem. |
| Create Page | `createPage` | Create a SharePoint site page. POST /sites/{site-id}/pages. Body must include @odata.type cast #microsoft.graph.sitePage. Returns the created sitePage. |
| Create Permission | `createPermission` | Create an application permission on a SharePoint site. POST /sites/{site-id}/permissions. Requires Sites.FullControl.All. Returns the created permission. |
| Create Site Column | `createSiteColumn` | Create a site column. POST /sites/{site-id}/columns. Requires name plus exactly ONE type facet (text/number/boolean/choice/dateTime/currency/personOrGroup/lookup/hyperlinkOrPicture). Pass the chosen facet object in 'typeFacet' along with 'typeFacetName'. |
| Create Site Content Type | `createSiteContentType` | Create a content type on a site. POST /sites/{site-id}/contentTypes. Requires name and a base content type ({ name, id }). Optional description, group, parentId, hidden. |
| Create Subscription | `createSubscription` | Create a change-notification subscription (webhook) on a SharePoint resource such as a list (sites/{site-id}/lists/{list-id}) or document library drive (drives/{drive-id}/root). On create Graph immediately POSTs a validationToken to notificationUrl which must be echoed back within 10s. For SharePoint list/driveItem changeType must be 'updated' and expirationDateTime must be under ~30 days. |

<details>

<summary>See 58 more actions</summary>

* **Delete Drive Item** `deleteDriveItem`: Delete a driveItem (file or folder), moving it to the recycle bin. DELETE /drives/{drive-id}/items/{item-id}. Returns 204 No Content.
* **Delete List** `deleteList`: Delete a list. DELETE /sites/{site-id}/lists/{list-id}. Returns 204 No Content.
* **Delete List Column** `deleteListColumn`: Delete a column from a list. DELETE /sites/{site-id}/lists/{list-id}/columns/{column-id}. Returns 204 No Content.
* **Delete List Item** `deleteListItem`: Delete a list item by id. Returns 204 No Content on success.
* **Delete Page** `deletePage`: Delete a SharePoint site page. DELETE /sites/{site-id}/pages/{page-id}. Returns 204 No Content.
* **Delete Permission** `deletePermission`: Delete a site application permission. DELETE /sites/{site-id}/permissions/{permission-id}. Returns 204 No Content. [BLOCKED 2026-06-05: 403 accessDenied — the /sites/{id}/permissions API requires Sites.FullControl.All (or Sites.Selected admin grant) which this delegated connection lacks. wiring correct, provider scope/account-state gated. Cannot obtain a real permissionId because listPermissions is 403-blocked by the same scope.]
* **Delete Subscription** `deleteSubscription`: Delete (unsubscribe) a change-notification subscription by id. Returns 204 No Content on success.
* **Download Drive Item Content** `downloadDriveItemContent`: Download the raw bytes of a file driveItem. GET /drives/{drive-id}/items/{item-id}/content. Graph 302-redirects to a pre-authenticated download URL, then returns the file content.
* **Follow Sites** `followSites`: Follow one or more sites for the signed-in user. POST /me/followedSites/add. Body has value[] of { id }. Returns value[] of followed sites.
* **Get Default Document Library (Drive)** `getSiteDefaultDrive`: Get the default document library (drive) for a SharePoint site. GET /sites/{site-id}/drive. Returns a single drive resource.
* **Get Drive By ID** `getDriveById`: Get a drive (document library) by its drive id. GET /drives/{drive-id}. Returns a single drive resource.
* **Get Drive Item By ID** `getDriveItemById`: Get a driveItem (file or folder) by its id. GET /drives/{drive-id}/items/{item-id}. Returns a single driveItem resource.
* **Get Drive Item By Path** `getDriveItemByPath`: Get a driveItem by its server-relative path. GET /drives/{drive-id}/root:/{path}. The path uses colon syntax. Returns a single driveItem.
* **Get List** `getList`: Get metadata for a single list. GET /sites/{site-id}/lists/{list-id}. list-id may be the GUID or the list display name. Supports $select, $expand.
* **Get List Column** `getListColumn`: Get a single column of a list. GET /sites/{site-id}/lists/{list-id}/columns/{column-id}. Returns the columnDefinition.
* **Get List Item** `getListItem`: Get a single list item by id. Use $expand=fields to return column values. Returns the listItem resource.
* **Get Me** `getMe`: Get the signed-in user profile. Used as the auth/connection smoke test. Returns id, displayName, userPrincipalName, mail and other profile fields.
* **Get Page By ID** `getPageById`: Get a SharePoint site page with full content. GET /sites/{site-id}/pages/{page-id}/microsoft.graph.sitePage. Use $expand=canvasLayout for sections/webParts.
* **Get Permission By ID** `getPermissionById`: Get a single site application permission. GET /sites/{site-id}/permissions/{permission-id}. Returns the permission. [BLOCKED 2026-06-05: 403 accessDenied — the /sites/{id}/permissions API requires Sites.FullControl.All (or Sites.Selected admin grant) which this delegated connection lacks. wiring correct, provider scope/account-state gated. Cannot obtain a real permissionId because listPermissions is 403-blocked by the same scope.]
* **Get Root Site** `getRootSite`: Get the tenant root SharePoint site. GET /sites/root. Optional OData $select/$expand query params. Returns the site resource.
* **Get Site Activities By Interval** `getSiteActivitiesByInterval`: Get itemActivityStat collection for a site over a date range/interval. GET /sites/{site-id}/getActivitiesByInterval(startDateTime='...',endDateTime='...',interval='...').
* **Get Site Analytics** `getSiteAnalytics`: Get analytics (itemAnalytics) for a SharePoint site. GET /sites/{site-id}/analytics. Returns allTime and lastSevenDays access stats.
* **Get Site By ID** `getSiteById`: Get a SharePoint site by its composite site id. GET /sites/{site-id}. site-id is {hostname},{siteCollectionGuid},{siteGuid} (or 'root'). Optional $select/$expand.
* **Get Site By Path** `getSiteByPath`: Get a SharePoint site by hostname + server-relative path. GET /sites/{hostname}:/{relative-path}. e.g. hostname=contoso.sharepoint.com relativePath=teams/1drvteam.
* **Get Site Content Type** `getSiteContentType`: Get a single content type on a site. GET /sites/{site-id}/contentTypes/{ct-id}. Supports $select, $expand. Returns the contentType resource.
* **Get Subscription** `getSubscription`: Get a single change-notification subscription by its id. Returns the subscription resource.
* **List All Sites** `listAllSites`: List all sites across geographies in the tenant (app-only oriented). GET /sites/getAllSites. Returns value[] of site.
* **List Content Type Columns** `listContentTypeColumns`: List columns associated with a site content type. GET /sites/{site-id}/contentTypes/{ct-id}/columns. Returns value[] of columnDefinition.
* **List Document Libraries (Drives)** `listSiteDrives`: List all document libraries (drives) for a SharePoint site. GET /sites/{site-id}/drives. Returns a collection of drive resources.
* **List Drive Item Children** `listDriveItemChildren`: List children of a folder driveItem. GET /drives/{drive-id}/items/{item-id}/children. Returns a collection of driveItem resources.
* **List Drive Root Children** `listDriveRootChildren`: List the items (files and folders) at the root of a drive. GET /drives/{drive-id}/root/children. Returns a collection of driveItem resources.
* **List Followed Sites** `listFollowedSites`: List the sites followed by the signed-in user. GET /me/followedSites. Returns value[] of site.
* **List List Columns** `listListColumns`: List columns of a list. GET /sites/{site-id}/lists/{list-id}/columns. Supports $select (include hidden), $top. Returns value[] of columnDefinition.
* **List List Content Types** `listListContentTypes`: List content types associated with a list. GET /sites/{site-id}/lists/{list-id}/contentTypes. Returns value[] of contentType.
* **List List Items** `listListItems`: List all items in a SharePoint list. Use $expand=fields to return column values. Returns value[] of listItem plus @odata.nextLink for paging.
* **List List Items Delta** `listListItemsDelta`: Track additions, deletions and updates to list items via delta query. Returns value[] of changed items plus @odata.deltaLink / @odata.nextLink. Use token=latest to fetch only the deltaLink.
* **List Lists** `listLists`: List all lists in a SharePoint site. GET /sites/{site-id}/lists. Supports OData $select, $filter, $top, $expand (e.g. columns,contentTypes). Returns value[] of list resources.
* **List Pages** `listPages`: List pages of a SharePoint site. GET /sites/{site-id}/pages/microsoft.graph.sitePage (sitePage cast). Returns value[] of sitePage.
* **List Permissions** `listPermissions`: List the application permissions on a SharePoint site. GET /sites/{site-id}/permissions. Returns value[] of permission.
* **List Site Columns** `listSiteColumns`: List site columns. GET /sites/{site-id}/columns. Supports $select (include hidden to see hidden columns), $top. Returns value[] of columnDefinition.
* **List Site Content Types** `listSiteContentTypes`: List content types defined on a site. GET /sites/{site-id}/contentTypes. Supports $select, $expand (columns,base,baseTypes). Returns value[] of contentType.
* **List Sites Delta** `listSitesDelta`: Track changes to sites in the tenant. GET /sites/delta. Returns value[] of changed sites plus @odata.deltaLink.
* **List Subscriptions** `listSubscriptions`: List all active change-notification subscriptions (webhooks) for the signed-in app/user. Returns subscription objects wrapped in value[]. Used to discover existing webhook subscriptions.
* **List Subsites** `listSubsites`: List subsites of a SharePoint site. GET /sites/{site-id}/sites. Returns value[] of site.
* **Publish Page** `publishPage`: Publish a SharePoint site page. POST /sites/{site-id}/pages/{page-id}/microsoft.graph.sitePage/publish. No body. Returns 204 No Content.
* **Reauthorize Subscription** `reauthorizeSubscription`: Reauthorize a subscription after a reauthorizationRequired lifecycle notification. No body. Returns 204 No Content. Typically followed by a PATCH to renew expirationDateTime.
* **Search Drive Items** `searchDriveItems`: Search items within a drive. GET /drives/{drive-id}/root/search(q='{query}'). Returns a collection of driveItem with searchResult facet.
* **Search Sites** `searchSites`: Search for SharePoint sites across the tenant. GET /sites?search={query}. Returns value[] of site plus @odata.nextLink.
* **Unfollow Sites** `unfollowSites`: Unfollow one or more sites for the signed-in user. POST /me/followedSites/remove. Body has value[] of { id }. Returns 204 No Content.
* **Update / Rename / Move Drive Item** `updateDriveItem`: Update a driveItem: rename via name, or move via parentReference. PATCH /drives/{drive-id}/items/{item-id}. Returns the updated driveItem. Only name is templated; supply name to rename.
* **Update List** `updateList`: Update writable properties of a list (displayName, description). PATCH /sites/{site-id}/lists/{list-id}. Returns the updated list resource.
* **Update List Column** `updateListColumn`: Update writable properties of a list column (cannot change the type facet kind). PATCH /sites/{site-id}/lists/{list-id}/columns/{column-id}. Pass only the props you want changed via 'patch'.
* **Update List Item Fields** `updateListItemFields`: Update the column values (fieldValueSet) of a list item. Body is the fieldValueSet directly (no 'fields' wrapper). Returns the updated fieldValueSet.
* **Update Page** `updatePage`: Update a SharePoint site page. PATCH /sites/{site-id}/pages/{page-id}/microsoft.graph.sitePage. Returns the updated sitePage.
* **Update Permission** `updatePermission`: Update the roles of a site application permission. PATCH /sites/{site-id}/permissions/{permission-id}. Returns the updated permission. [BLOCKED 2026-06-05: 403 accessDenied — the /sites/{id}/permissions API requires Sites.FullControl.All (or Sites.Selected admin grant) which this delegated connection lacks. configHealthy:true; requestBody echoed {"roles":["read"]} field-by-field so inputContract/bodyTemplate are correctly wired. Provider scope/account-state gated. Cannot obtain a real permissionId because listPermissions is 403-blocked by the same scope.]
* **Update Subscription** `updateSubscription`: Renew or update a change-notification subscription. Primary use is renewing expirationDateTime before it lapses. Optionally update notificationUrl. Returns the updated subscription.
* **Upload Drive Item Content (Replace by ID)** `uploadDriveItemContent`: Upload/replace the content of an existing file driveItem (&lt;=250 MB). PUT /drives/{drive-id}/items/{item-id}/content. Body is the raw file bytes (not JSON). Returns the driveItem of the uploaded file.
* **Upload File By Path** `uploadDriveItemByPath`: Upload a new file (or replace) by server-relative path (&lt;=250 MB). PUT /drives/{drive-id}/root:/{path}:/content. Body is the raw file bytes (not JSON). Returns the driveItem of the uploaded file.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Resource Created | `created` | A monitored resource emitted a created change notification (for resources that support the 'created' changeType). Payload shape mirrors the updated notification. |
| Resource Deleted | `deleted` | A monitored resource emitted a deleted change notification (for resources that support the 'deleted' changeType). Payload shape mirrors the updated notification. |
| Resource Updated | `updated` | A monitored SharePoint resource (list item changed in a list, or a driveItem changed in a document library) was updated. SharePoint list/driveItem only support the 'updated' changeType; the notification signals that the list/drive changed and the app should call the items/driveItem delta to find what changed. |
