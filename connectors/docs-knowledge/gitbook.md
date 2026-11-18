---
description: "GitBook documentation platform API connector."
hidden: true
---

# GitBook

<img src="../../.gitbook/assets/connectors/lg/gitbook.png" alt="GitBook logo">

GitBook documentation platform API connector. Manage organizations, spaces, collections, pages/content, revisions, and change requests via the GitBook REST API (https://api.gitbook.com/v1). Authenticates with a GitBook personal access token (gb_api_ ...) via Bearer auth.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [gitbook.com](https://gitbook.com) |
| **Authentication** | Bearer token |
| **Slug** | `gitbook` |

## Use it

Add GitBook from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.gitbook.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Change Request | `createChangeRequest` | Create a new change request in a space. |
| Create Collection | `createCollection` | Create a new collection in an organization. |
| Create Space | `createSpace` | Create a new space in an organization. Provide title (optional) and optional parent collection ID. |
| Delete Collection | `deleteCollection` | Delete a collection by its ID. |
| Delete Space | `deleteSpace` | Delete a space (kept for 7-day retention; can be restored). |
| Duplicate Space | `duplicateSpace` | Create a copy of an existing space. |
| Get Change Request | `getChangeRequest` | Get a change request by its ID. |
| Get Change Request Content | `getChangeRequestContent` | Get the latest content revision of a change request. |
| Get Collection | `getCollection` | Get a collection by its ID. |
| Get Current User | `getCurrentUser` | Get details about the user associated with the API token. FREE read — ideal for credential validation. |
| Get Organization | `getOrganization` | Get an organization by its ID. |
| Get Organization Team | `getOrganizationTeam` | Get a team in an organization by its ID. |
| Get Page By ID | `getPageById` | Get a page in the current revision of a space by its page ID. |
| Get Page By Path | `getPageByPath` | Get a page in the current revision of a space by its path. |
| Get Revision | `getRevision` | Get a specific revision of a space by its revision ID. |
| Get Revision Page By ID | `getRevisionPageById` | Get a page in a specific revision of a space by its page ID. |
| Get Space | `getSpace` | Get a space by its ID. |
| Get Space Content | `getSpaceContent` | Get the current (primary) revision content of a space, including its page tree. |
| Get User By ID | `getUserById` | Fetch public information about a user by their user ID. |
| Import Content | `importContent` | Import content into a space from a Git repository. |
| List Change Request Comments | `listChangeRequestComments` | List the comments on a change request. |
| List Change Request Pages | `listChangeRequestPages` | List all pages in a change request's content. |
| List Change Requests | `listChangeRequests` | List the change requests of a space. |
| List Collection Spaces | `listCollectionSpaces` | List the spaces contained in a collection. |
| List Organization Collections | `listOrganizationCollections` | List the collections in an organization. |
| List Organization Members | `listOrganizationMembers` | List the members of an organization. |
| List Organization Spaces | `listOrganizationSpaces` | List the spaces in an organization. |
| List Organization Teams | `listOrganizationTeams` | List the teams in an organization. |
| List Organizations | `listOrganizations` | List the organizations the authenticated user is a member of. FREE read — credit-safe for validation. |
| List Pages | `listPages` | List all pages in the current revision of a space. |
| List Revision Files | `listRevisionFiles` | List the files in a specific revision of a space. |
| List Revision Pages | `listRevisionPages` | List the pages in a specific revision of a space. |
| List Space Files | `listSpaceFiles` | List all files (images, assets) in the current revision of a space. |
| List Team Members | `listTeamMembers` | List members of an organization team. |
| Merge Change Request | `mergeChangeRequest` | Merge a change request into the primary revision of its space. |
| Move Space | `moveSpace` | Move a space to a new parent collection and/or position. |
| Post Change Request Comment | `postChangeRequestComment` | Post a comment on a change request. |
| Restore Space | `restoreSpace` | Restore a deleted space within the 7-day retention window. |
| Search Organization Content | `searchOrganizationContent` | Search content across an organization's spaces. |
| Search Space Content | `searchSpaceContent` | Full-text search content within a single space. |
| Update Change Request | `updateChangeRequest` | Update a change request's subject and/or status. |
| Update Collection | `updateCollection` | Update a collection's title, description, or default permission level. |
| Update Space | `updateSpace` | Update a space's properties (title, edit mode, language, emoji). Send only the fields you want to change. |
