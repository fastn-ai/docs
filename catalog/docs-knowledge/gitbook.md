---
description: "GitBook is a documentation platform. Manage spaces, collections, page content and change requests."
hidden: true
---

# GitBook

<img src="../../.gitbook/assets/connectors/lg/gitbook.png" alt="GitBook logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [gitbook.com](https://gitbook.com) |
| **Authentication** | Access token |
| **Slug** | `gitbook` |

## Setup

Your customers enter their access token for GitBook when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect GitBook from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **GitBook**.
2. Select **Connect** on the GitBook card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use GitBook's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Change Request</td><td><code>createChangeRequest</code></td><td>Create a new change request in a space.</td></tr><tr><td>Create Collection</td><td><code>createCollection</code></td><td>Create a new collection in an organization.</td></tr><tr><td>Create Space</td><td><code>createSpace</code></td><td>Create a new space in an organization. Provide title (optional) and optional parent collection ID.</td></tr><tr><td>Delete Collection</td><td><code>deleteCollection</code></td><td>Delete a collection by its ID.</td></tr><tr><td>Delete Space</td><td><code>deleteSpace</code></td><td>Delete a space (kept for 7-day retention; can be restored).</td></tr><tr><td>Duplicate Space</td><td><code>duplicateSpace</code></td><td>Create a copy of an existing space.</td></tr><tr><td>Get Change Request</td><td><code>getChangeRequest</code></td><td>Get a change request by its ID.</td></tr><tr><td>Get Change Request Content</td><td><code>getChangeRequestContent</code></td><td>Get the latest content revision of a change request.</td></tr><tr><td>Get Collection</td><td><code>getCollection</code></td><td>Get a collection by its ID.</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Get details about the user associated with the API token. FREE read — ideal for credential validation.</td></tr></tbody></table>

<details>

<summary>View 33 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Organization</td><td><code>getOrganization</code></td><td>Get an organization by its ID.</td></tr><tr><td>Get Organization Team</td><td><code>getOrganizationTeam</code></td><td>Get a team in an organization by its ID.</td></tr><tr><td>Get Page By ID</td><td><code>getPageById</code></td><td>Get a page in the current revision of a space by its page ID.</td></tr><tr><td>Get Page By Path</td><td><code>getPageByPath</code></td><td>Get a page in the current revision of a space by its path.</td></tr><tr><td>Get Revision</td><td><code>getRevision</code></td><td>Get a specific revision of a space by its revision ID.</td></tr><tr><td>Get Revision Page By ID</td><td><code>getRevisionPageById</code></td><td>Get a page in a specific revision of a space by its page ID.</td></tr><tr><td>Get Space</td><td><code>getSpace</code></td><td>Get a space by its ID.</td></tr><tr><td>Get Space Content</td><td><code>getSpaceContent</code></td><td>Get the current (primary) revision content of a space, including its page tree.</td></tr><tr><td>Get User By ID</td><td><code>getUserById</code></td><td>Fetch public information about a user by their user ID.</td></tr><tr><td>Import Content</td><td><code>importContent</code></td><td>Import content into a space from a Git repository.</td></tr><tr><td>List Change Request Comments</td><td><code>listChangeRequestComments</code></td><td>List the comments on a change request.</td></tr><tr><td>List Change Request Pages</td><td><code>listChangeRequestPages</code></td><td>List all pages in a change request's content.</td></tr><tr><td>List Change Requests</td><td><code>listChangeRequests</code></td><td>List the change requests of a space.</td></tr><tr><td>List Collection Spaces</td><td><code>listCollectionSpaces</code></td><td>List the spaces contained in a collection.</td></tr><tr><td>List Organization Collections</td><td><code>listOrganizationCollections</code></td><td>List the collections in an organization.</td></tr><tr><td>List Organization Members</td><td><code>listOrganizationMembers</code></td><td>List the members of an organization.</td></tr><tr><td>List Organization Spaces</td><td><code>listOrganizationSpaces</code></td><td>List the spaces in an organization.</td></tr><tr><td>List Organization Teams</td><td><code>listOrganizationTeams</code></td><td>List the teams in an organization.</td></tr><tr><td>List Organizations</td><td><code>listOrganizations</code></td><td>List the organizations the authenticated user is a member of. FREE read — credit-safe for validation.</td></tr><tr><td>List Pages</td><td><code>listPages</code></td><td>List all pages in the current revision of a space.</td></tr><tr><td>List Revision Files</td><td><code>listRevisionFiles</code></td><td>List the files in a specific revision of a space.</td></tr><tr><td>List Revision Pages</td><td><code>listRevisionPages</code></td><td>List the pages in a specific revision of a space.</td></tr><tr><td>List Space Files</td><td><code>listSpaceFiles</code></td><td>List all files (images, assets) in the current revision of a space.</td></tr><tr><td>List Team Members</td><td><code>listTeamMembers</code></td><td>List members of an organization team.</td></tr><tr><td>Merge Change Request</td><td><code>mergeChangeRequest</code></td><td>Merge a change request into the primary revision of its space.</td></tr><tr><td>Move Space</td><td><code>moveSpace</code></td><td>Move a space to a new parent collection and/or position.</td></tr><tr><td>Post Change Request Comment</td><td><code>postChangeRequestComment</code></td><td>Post a comment on a change request.</td></tr><tr><td>Restore Space</td><td><code>restoreSpace</code></td><td>Restore a deleted space within the 7-day retention window.</td></tr><tr><td>Search Organization Content</td><td><code>searchOrganizationContent</code></td><td>Search content across an organization's spaces.</td></tr><tr><td>Search Space Content</td><td><code>searchSpaceContent</code></td><td>Full-text search content within a single space.</td></tr><tr><td>Update Change Request</td><td><code>updateChangeRequest</code></td><td>Update a change request's subject and/or status.</td></tr><tr><td>Update Collection</td><td><code>updateCollection</code></td><td>Update a collection's title, description, or default permission level.</td></tr><tr><td>Update Space</td><td><code>updateSpace</code></td><td>Update a space's properties (title, edit mode, language, emoji). Send only the fields you want to change.</td></tr></tbody></table>

</details>

