---
description: "Raindrop.io is a bookmark manager for saving, organising and sharing links, articles, photos and files."
hidden: true
---

# Raindrop.io

<img src="../../.gitbook/assets/connectors/raindrop-io.png" alt="Raindrop.io logo" width="64">

Raindrop.io is a bookmark manager for saving, organising and sharing links, articles, photos and files. This connector covers the full Raindrop.io v1 REST API: collections with nested structure, sharing and covers, raindrops (bookmarks) singly and in bulk, highlights, tags, filters, the authenticated user, URL and file import, export and backups.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [raindrop.io](https://raindrop.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `raindropIo` |

## Use it

Add Raindrop.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.raindropIo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Highlight | `addHighlight` | Adds a text highlight to a bookmark. Existing highlights on the bookmark are preserved - Raindrop.io merges the new entry into the list. |
| Change Collaborator Access | `changeCollaboratorAccess` | Changes one collaborator's access level on a shared collection, between member (can add and edit bookmarks) and viewer (read only). |
| Check URLs Exist | `checkUrlsExist` | Checks whether the given URLs are already bookmarked in the account, and returns the matching bookmarks. Use it to avoid creating duplicates before calling Create Raindrop. |
| Connect Social Account | `connectSocialAccount` | Starts linking a social login provider to the Raindrop.io account. The endpoint returns a redirect to the provider's consent screen, so it must be opened in a browser rather than called headlessly. |
| Create Collection | `createCollection` | Creates a new collection. Supply a Parent Collection ID to nest it under an existing collection, or omit it to create a root collection. Note that Raindrop.io ignores the view style on create - set it afterwards with Update Collection - and ignores per-collection sort order entirely; use Reorder All Collections instead. |
| Create Many Raindrops | `createManyRaindrops` | Saves up to 100 bookmarks in a single call. Each item accepts the same fields as Create Raindrop. |
| Create Raindrop | `createRaindrop` | Saves a new bookmark. Only the link is required - Raindrop.io parses the page for the title, excerpt, cover and type unless you set Please Parse to false and supply them yourself. |
| Delete Collection | `deleteCollection` | Removes a collection. The raindrops it held are moved to Trash rather than deleted outright. |
| Delete Many Raindrops | `deleteManyRaindrops` | Removes many bookmarks from a collection at once. They are moved to Trash unless the collection is Trash (-99), in which case they are deleted permanently. Supply Raindrop IDs to target specific bookmarks, or omit it to remove every bookmark in the collection. |
| Delete Multiple Collections | `deleteMultipleCollections` | Removes several collections at once. The raindrops they held are moved to Trash rather than deleted outright. |

<details>

<summary>See 42 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Raindrop | `deleteRaindrop` | Removes a bookmark. It is moved to Trash first; calling this on a bookmark already in Trash deletes it permanently. |
| Disconnect Social Account | `disconnectSocialAccount` | Unlinks a social login provider from the Raindrop.io account, so it can no longer be used to sign in. |
| Download Backup | `downloadBackup` | Downloads a generated backup in the chosen format. Raindrop.io redirects to signed storage and fastn follows the redirect, returning the file body as a plain string. |
| Empty Trash | `emptyTrash` | Permanently deletes every raindrop in Trash. This cannot be undone. |
| Expand Or Collapse All Collections | `expandCollapseCollections` | Expands or collapses every collection that has children in the Raindrop.io sidebar, in one call. |
| Export Raindrops | `exportRaindrops` | Exports the bookmarks of a collection as a CSV, HTML or Zip file, honouring the same search and sort options as List Raindrops. The file body is returned as a plain string. |
| Generate Backup | `generateBackup` | Starts generating a fresh backup of every bookmark in the account. Raindrop.io emails the account owner a download link when it is ready; how long that takes depends on the number of bookmarks. |
| Get All Highlights | `listHighlights` | Returns every text highlight across all of the account's bookmarks, with pagination. |
| Get Authenticated User | `getUser` | Returns the Raindrop.io account the access token belongs to, including plan status, storage usage, connected social accounts and configuration. |
| Get Collection | `getCollection` | Returns a single collection by id. The system collections can also be read: 0 is Unsorted, -1 is All bookmarks and -99 is Trash. |
| Get Collection Collaborators | `getCollaborators` | Returns the people a collection is shared with, each with their access level and whether they have accepted the invitation. |
| Get Collection Highlights | `listCollectionHighlights` | Returns every text highlight on the bookmarks in a single collection, with pagination. |
| Get Filters | `getFilters` | Returns the aggregated counts Raindrop.io uses to build its filter sidebar for a collection - broken links, duplicates, favourites, untagged bookmarks, tags, content types, domains and creation dates. |
| Get Permanent Copy | `getPermanentCopy` | Returns a redirect to the permanent cached copy Raindrop.io keeps of a bookmarked page. Permanent copies require a Pro subscription. |
| Get Raindrop | `getRaindrop` | Returns a single bookmark by id, including its tags, note, media, collection and any highlights on it. |
| Get System Collection Counts | `getSystemCollectionCounts` | Returns the raindrop count for each system collection - Unsorted (0), All bookmarks (-1) and Trash (-99) - along with account-level totals. |
| Get Tags | `getTags` | Returns the tags used in a collection, each with how many bookmarks carry it. Omit the Collection ID to get the tags across the whole account. |
| Get User By ID | `getUserByName` | Returns the public profile of another Raindrop.io user by their numeric user id. Despite the documentation naming this parameter a username, the live API only accepts a numeric id - a username returns the router-level 404. Reading other users requires a confirmed email on your own account. |
| List Backups | `listBackups` | Returns the backups Raindrop.io has generated for the account, newest first. Use Download Backup with an id to fetch one. |
| List Child Collections | `listChildCollections` | Returns every nested collection in the account - those that have a parent. Combine with List Root Collections to rebuild the full sidebar tree. |
| List Featured Collection Covers | `listFeaturedCovers` | Returns the featured cover sets Raindrop.io offers for collections, such as the colour circles and icon packs shown in the cover picker. |
| List Raindrops | `listRaindrops` | Returns the bookmarks in a collection, with full-text search, sorting and pagination. Use collection 0 for Unsorted, -1 for All bookmarks or -99 for Trash. The search syntax supports operators such as #tag, type:article, created:2026 and match phrases in quotes. |
| List Root Collections | `listRootCollections` | Returns every top-level collection in the account - those with no parent. Use List Child Collections for the nested ones. |
| Merge Collections | `mergeCollections` | Moves all raindrops from the listed collections into a target collection and removes the emptied source collections. |
| Merge Tags | `mergeTags` | Merges several tags into one. Every bookmark carrying any of the listed tags ends up with the replacement tag instead. Omit the Collection ID to merge across the whole account. |
| Parse URL | `parseUrl` | Fetches a URL and returns the title, excerpt, cover, media and content type Raindrop.io extracts from it, without saving a bookmark. Use it to preview what Create Raindrop would store. |
| Remove All Empty Collections | `removeEmptyCollections` | Removes every collection in the account that contains no raindrops, and returns how many were removed. |
| Remove Collaborator | `removeCollaborator` | Removes one collaborator from a shared collection. They lose access immediately; the collection and its bookmarks are untouched. |
| Remove Highlight | `removeHighlight` | Removes a highlight from a bookmark. Raindrop.io deletes a highlight by sending its id with empty text, which this action does for you. |
| Remove Tags | `removeTags` | Removes the listed tags from every bookmark in a collection. The bookmarks themselves are untouched. Omit the Collection ID to remove the tags across the whole account. |
| Rename Tag | `renameTag` | Renames a tag across the bookmarks in a collection. Omit the Collection ID to rename it everywhere in the account. |
| Reorder All Collections | `reorderCollections` | Reorders every collection in the sidebar at once by the chosen criterion. This is the only way to change collection ordering through the API - the sort field on Create Collection and Update Collection is ignored by Raindrop.io. |
| Search Collection Covers | `searchCollectionCovers` | Searches Raindrop.io's icon library for collection cover images matching a keyword, returning icon sets you can use as a collection cover. |
| Share Collection | `shareCollection` | Shares a collection at the chosen access level and returns a join token and invite link. Any valid email addresses supplied are also emailed an invitation. Only the collection owner can share it. |
| Suggest For Existing Bookmark | `suggestForExistingBookmark` | Returns the collections and tags Raindrop.io suggests for a bookmark you have already saved, so you can offer to re-file or re-tag it. |
| Suggest For New Bookmark | `suggestForNewBookmark` | Returns the collections and tags Raindrop.io suggests for a URL you have not saved yet, so you can offer them before creating the bookmark. |
| Unshare Or Leave Collection | `unshareCollection` | Stops sharing a collection. When called by the owner it removes every collaborator; when called by a collaborator it removes only them, so they leave the collection. |
| Update Collection | `updateCollection` | Updates an existing collection. Only the fields supplied are sent, so untouched settings keep their current values. Raindrop.io ignores per-collection sort order, so use Reorder All Collections to change ordering. |
| Update Highlight | `updateHighlight` | Changes the text, note or colour of an existing highlight on a bookmark, identified by its highlight id. |
| Update Many Raindrops | `updateManyRaindrops` | Applies the same change to many bookmarks in a collection at once - move them, tag them, favourite them or send them to Trash. Supply Raindrop IDs to target specific bookmarks, or omit it to apply the change to every bookmark in the collection. |
| Update Raindrop | `updateRaindrop` | Updates an existing bookmark. Only the fields supplied are sent, so untouched fields keep their current values. Set In Trash to true to move it to Trash, or false to restore it. |
| Update User | `updateUser` | Updates the authenticated user's own profile and app configuration - name, email, password and the Raindrop.io interface settings held in config. |

</details>
