---
description: "Microsoft Viva Engage (formerly Yammer) communities and roles via the Microsoft Graph v1.0 API (https://graph.microsoft.com/v1.0/employeeExperience)."
hidden: true
---

# Viva Engage

<img src="../../.gitbook/assets/connectors/viva-engage.png" alt="Viva Engage logo" width="64">

Microsoft Viva Engage (formerly Yammer) communities and roles via the Microsoft Graph v1.0 API (https://graph.microsoft.com/v1.0/employeeExperience). Create, read, update and delete Viva Engage communities, poll the long-running community-creation operation, list the predefined Viva Engage roles and their members, assign and revoke a role for a user, and read the roles assigned to the signed-in user or any user. Community membership and ownership are managed through the connected Microsoft 365 group, so this connector also lists, adds and removes community members and administrators through the group endpoints, as the Viva Engage API overview prescribes. Uses Microsoft Graph rather than the legacy api.yammer.com REST API, whose OAuth 2.0 application platform Microsoft retired on 30 June 2025. Connect with a Microsoft work or school account using Entra ID OAuth 2.0; the Viva Engage network must be in native mode, and every permission requested needs tenant administrator consent.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [graph.microsoft.com](https://graph.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `vivaEngage` |

## Use it

Add Viva Engage from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.vivaEngage.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Community Admin | `addCommunityAdmin` | Makes a user an administrator of a Viva Engage community by adding them as an owner of its connected Microsoft 365 group. |
| Add Community Member | `addCommunityMember` | Adds a user to a Viva Engage community by adding them to its connected Microsoft 365 group. The community's membership updates automatically. Microsoft Graph returns 204 No Content on success. |
| Assign Engagement Role | `assignEngagementRole` | Assigns a predefined Viva Engage role to a user, creating an engagementRoleMember. |
| Create Community | `createCommunity` | Creates a Viva Engage community together with its connected Microsoft 365 group, SharePoint site, OneNote notebook and Planner plan. This is a long-running operation: Microsoft Graph answers 202 Accepted with a Location header pointing at an engagementAsyncOperation, which you then poll with Get Engagement Async Operation until its status is succeeded. |
| Delete Community | `deleteCommunity` | Deletes a Viva Engage community along with all of its connected Microsoft 365 content, including the backing group, its OneNote notebook and its Planner plans. This is destructive and cannot be undone. |
| Get Community | `getCommunity` | Retrieves a single Viva Engage community by its ID, including the ID of the Microsoft 365 group used to manage its members and administrators. |
| Get Engagement Async Operation | `getEngagementAsyncOperation` | Reads the status of a Viva Engage long-running operation, such as a community creation started by Create Community. Poll no more often than every 30 seconds; when status is succeeded, resourceId names the community that was created. |
| List Communities | `listCommunities` | Lists the Viva Engage communities in the tenant. Each community carries the ID of the Microsoft 365 group that backs its membership. |
| List Community Admins | `listCommunityAdmins` | Lists the administrators of a Viva Engage community by reading the owners of its connected Microsoft 365 group. Take the Group ID from Get Community. |
| List Community Members | `listCommunityMembers` | Lists the members of a Viva Engage community by reading the members of its connected Microsoft 365 group. Take the Group ID from Get Community. |

<details>

<summary>See 8 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Engagement Role Members | `listEngagementRoleMembers` | Lists the users who hold a specific Viva Engage role, together with the date each assignment was made. |
| List Engagement Roles | `listEngagementRoles` | Lists the predefined Viva Engage roles that can be assigned to users, such as Network Administrator and Verified Administrator. These roles are fixed by Viva Engage and cannot be created or deleted. |
| List My Assigned Roles | `listMyAssignedRoles` | Lists the Viva Engage roles assigned to the signed-in user. Uses the least privileged EngagementRole.Read permission rather than a tenant-wide one. |
| List User Assigned Roles | `listUserAssignedRoles` | Lists the Viva Engage roles assigned to a specified user. Use List My Assigned Roles for the signed-in user. |
| Remove Community Admin | `removeCommunityAdmin` | Removes a user's Viva Engage community administrator rights by removing them as an owner of the connected Microsoft 365 group. The last remaining owner cannot be removed. |
| Remove Community Member | `removeCommunityMember` | Removes a user from a Viva Engage community by removing them from its connected Microsoft 365 group. The community's membership updates automatically. |
| Revoke Engagement Role | `revokeEngagementRole` | Revokes a Viva Engage role from a user by deleting their engagementRoleMember entry. |
| Update Community | `updateCommunity` | Updates the name, description or privacy level of a Viva Engage community. Only the properties you supply are sent. Microsoft Graph returns 204 No Content on success. |

</details>
