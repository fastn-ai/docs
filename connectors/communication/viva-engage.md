---
description: "Microsoft Viva Engage is an employee community platform. Create, read and delete communities, and manage community members, admins and roles."
hidden: true
---

# Viva Engage

<img src="../../.gitbook/assets/connectors/lg/viva-engage.png" alt="Viva Engage logo">

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [graph.microsoft.com](https://graph.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `vivaEngage` |

## Setup

Your customers sign in to Viva Engage through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Viva Engage from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.vivaEngage.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Community Admin</td><td><code>addCommunityAdmin</code></td><td>Makes a user an administrator of a Viva Engage community by adding them as an owner of its connected Microsoft 365 group.</td></tr><tr><td>Add Community Member</td><td><code>addCommunityMember</code></td><td>Adds a user to a Viva Engage community by adding them to its connected Microsoft 365 group. The community's membership updates automatically. Microsoft Graph</td></tr><tr><td>Assign Engagement Role</td><td><code>assignEngagementRole</code></td><td>Assigns a predefined Viva Engage role to a user, creating an engagementRoleMember.</td></tr><tr><td>Create Community</td><td><code>createCommunity</code></td><td>Creates a Viva Engage community together with its connected Microsoft 365 group, SharePoint site, OneNote notebook and Planner plan.</td></tr><tr><td>Delete Community</td><td><code>deleteCommunity</code></td><td>Deletes a Viva Engage community along with all of its connected Microsoft 365 content, including the backing group, its OneNote notebook and its Planner plans. This is destructive and cannot be undone.</td></tr><tr><td>Get Community</td><td><code>getCommunity</code></td><td>Retrieves a single Viva Engage community by its ID, including the ID of the Microsoft 365 group used to manage its members and administrators.</td></tr><tr><td>Get Engagement Async Operation</td><td><code>getEngagementAsyncOperation</code></td><td>Reads the status of a Viva Engage long-running operation, such as a community creation started by Create Community. Poll no more often than every 30 seconds; when status is succeeded, resourceId names the community that was created.</td></tr><tr><td>List Communities</td><td><code>listCommunities</code></td><td>Lists the Viva Engage communities in the tenant. Each community carries the ID of the Microsoft 365 group that backs its membership.</td></tr><tr><td>List Community Admins</td><td><code>listCommunityAdmins</code></td><td>Lists the administrators of a Viva Engage community by reading the owners of its connected Microsoft 365 group. Take the Group ID from Get Community.</td></tr><tr><td>List Community Members</td><td><code>listCommunityMembers</code></td><td>Lists the members of a Viva Engage community by reading the members of its connected Microsoft 365 group. Take the Group ID from Get Community.</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Engagement Role Members</td><td><code>listEngagementRoleMembers</code></td><td>Lists the users who hold a specific Viva Engage role, together with the date each assignment was made.</td></tr><tr><td>List Engagement Roles</td><td><code>listEngagementRoles</code></td><td>Lists the predefined Viva Engage roles that can be assigned to users, such as Network Administrator and Verified Administrator. These roles are fixed by Viva Engage and cannot be created or deleted.</td></tr><tr><td>List My Assigned Roles</td><td><code>listMyAssignedRoles</code></td><td>Lists the Viva Engage roles assigned to the signed-in user. Uses the least privileged EngagementRole.Read permission rather than a tenant-wide one.</td></tr><tr><td>List User Assigned Roles</td><td><code>listUserAssignedRoles</code></td><td>Lists the Viva Engage roles assigned to a specified user. Use List My Assigned Roles for the signed-in user.</td></tr><tr><td>Remove Community Admin</td><td><code>removeCommunityAdmin</code></td><td>Removes a user's Viva Engage community administrator rights by removing them as an owner of the connected Microsoft 365 group. The last remaining owner cannot be removed.</td></tr><tr><td>Remove Community Member</td><td><code>removeCommunityMember</code></td><td>Removes a user from a Viva Engage community by removing them from its connected Microsoft 365 group. The community's membership updates automatically.</td></tr><tr><td>Revoke Engagement Role</td><td><code>revokeEngagementRole</code></td><td>Revokes a Viva Engage role from a user by deleting their engagementRoleMember entry.</td></tr><tr><td>Update Community</td><td><code>updateCommunity</code></td><td>Updates the name, description or privacy level of a Viva Engage community. Only the properties you supply are sent. Microsoft Graph</td></tr></tbody></table>

</details>

## Events

Viva Engage has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
