---
description: "Microsoft Entra ID (formerly Azure Active Directory) identity and directory management via the Microsoft Graph v1.0 API (https://graph.microsoft.com/v1.0)."
hidden: true
---

# Microsoft Entra ID

<img src="../../.gitbook/assets/connectors/microsoft-entra-id.png" alt="Microsoft Entra ID logo" width="64">

Microsoft Entra ID (formerly Azure Active Directory) identity and directory management via the Microsoft Graph v1.0 API (https://graph.microsoft.com/v1.0). Manage users (create, read, update, delete, password change, licence assignment, manager and direct reports, sponsors, profile photo, sign-in session revocation), groups (create, read, update, delete, members, owners, settings, lifecycle policies, licences, mail senders), directory roles and role templates, administrative units and scoped role members, applications and service principals with their owners, keys, secrets and app role assignments, OAuth2 permission grants, organization branding and settings, verified domains, org contacts, devices, subscribed SKUs, and the directory audit and sign-in logs. Connect with a Microsoft work or school account using Entra ID OAuth 2.0. IMPORTANT: every directory permission this connector requests needs tenant administrator consent - a non-admin user cannot authorize it on their own.

| | |
| --- | --- |
| **Category** | [IT and service management](README.md) |
| **Website** | [graph.microsoft.com](https://graph.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `microsoftEntraId` |

## Use it

Add Microsoft Entra ID from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.microsoftEntraId.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Directory Role | `activateDirectoryRole` | Activates a directory role in the tenant from its role template, making it available for member assignment. Role Template ID is the only property the API accepts. The Company Administrator and implicit user roles are activated by default. |
| Add Administrative Unit Member | `addAdministrativeUnitMember` | Adds an existing user, group or device to a Microsoft Entra ID administrative unit, bringing it into that unit's administrative scope. |
| Add Application Password | `addApplicationPassword` | Generates a new client secret for a Microsoft Entra ID application registration. The secretText value is returned only in this response and cannot be read again, so capture it immediately. |
| Add Directory Role Member | `addDirectoryRoleMember` | Assigns a user, group or service principal to an activated directory role, granting them that administrative role in the tenant. |
| Add Group Member | `addGroupMember` | Adds a directory object to a Microsoft Entra ID group. Microsoft 365 groups accept only users; security groups also accept groups, devices, service principals and organizational contacts. |
| Add Group Owner | `addGroupOwner` | Adds a user or service principal as an owner of a Microsoft Entra ID group. |
| Add Service Principal App Role Assigned To | `addServicePrincipalAppRoleAssignedTo` | Grants a user, group or service principal one of the application roles a service principal exposes, giving them access to that enterprise application. |
| Add User App Role Assignment | `addUserAppRoleAssignment` | Grants a Microsoft Entra ID user an application role, which is how an application is assigned to a user. Use the app role's default GUID of all zeros when the application exposes no roles. |
| Add User Sponsor | `addUserSponsor` | Assigns a user or group as a sponsor of a Microsoft Entra ID user, typically to attribute a guest account to an internal owner. |
| Assign Group Licence | `assignGroupLicense` | Adds or removes subscription licences on a Microsoft Entra ID group, so that every member inherits them. Remove Licences is required and may be an empty array. |

<details>

<summary>See 97 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Assign User Licence | `assignUserLicense` | Adds or removes subscription licences for a Microsoft Entra ID user. The user must have a usageLocation set first. Remove Licences is required and may be an empty array. |
| Assign User Manager | `assignUserManager` | Sets or replaces the manager of a Microsoft Entra ID user. The manager must be referenced by its full Graph read URL. |
| Change My Password | `changeMyPassword` | Changes the password of the signed-in user, who must supply their current password. Microsoft Graph v1.0 offers this only for the signed-in user; to reset another user's password, set passwordProfile with Update User. |
| Check User Member Groups | `checkUserMemberGroups` | Checks which of a supplied list of groups a user belongs to, directly or through nesting. Returns only the matching group IDs. Up to 20 groups may be checked in one call. |
| Create Administrative Unit | `createAdministrativeUnit` | Creates a Microsoft Entra ID administrative unit. Display Name is required. Member Management Restricted is immutable once set and cannot be changed later. |
| Create Application | `createApplication` | Creates an application registration in Microsoft Entra ID. Display Name is the only required property. A service principal must be created separately before the application can be used in the tenant. |
| Create Domain | `createDomain` | Adds an unverified domain to the Microsoft Entra ID tenant. The fully qualified domain name is the only property the API accepts. Publish the DNS record from List Domain Verification DNS Records, then call Verify Domain. |
| Create Group | `createGroup` | Creates a Microsoft Entra ID group. Display Name, Mail Enabled, Mail Nickname and Security Enabled are required. For a Microsoft 365 group set Group Types to ["Unified"] and Mail Enabled to true; for a security group leave Group Types empty and set Security Enabled to true. Creating the group does not add you as a member. |
| Create Group Setting | `createGroupSetting` | Creates a directory-level group setting from a template, for example to enable the Microsoft 365 group naming or classification policy. Only the values may differ from the template's defaults. |
| Create OAuth2 Permission Grant | `createOauth2PermissionGrant` | Grants a client application delegated permissions on a resource API, which is how consent is recorded without an interactive prompt. Set Consent Type to AllPrincipals for tenant-wide consent, or to Principal together with a Principal ID for one user. |
| Create Service Principal | `createServicePrincipal` | Creates a service principal in the tenant for an existing application registration, which is what makes the application usable here. Application (Client) ID is the only required property. |
| Create User | `createUser` | Creates a user account in Microsoft Entra ID. Account Enabled, Display Name, Mail Nickname, User Principal Name and Password Profile are required. The domain of the user principal name must be one of the tenant's verified domains. |
| Delete Administrative Unit | `deleteAdministrativeUnit` | Deletes a Microsoft Entra ID administrative unit. The users and groups it scoped are not deleted, but role assignments scoped to the unit are removed. |
| Delete Application | `deleteApplication` | Deletes a Microsoft Entra ID application registration. It moves to the deleted items container for 30 days, where it can be restored before permanent removal. |
| Delete Group | `deleteGroup` | Deletes a Microsoft Entra ID group. A deleted Microsoft 365 group moves to the deleted items container for 30 days and can be restored; security groups are removed permanently. |
| Delete OAuth2 Permission Grant | `deleteOauth2PermissionGrant` | Revokes a delegated permission grant, withdrawing the consent a client application held against a resource API. The application loses that access immediately. |
| Delete Service Principal | `deleteServicePrincipal` | Deletes a Microsoft Entra ID service principal, removing the application from the tenant. The underlying application registration is not deleted. |
| Delete User | `deleteUser` | Deletes a Microsoft Entra ID user. The account moves to the deleted items container for 30 days, where it can be read or restored with the deleted items actions before it is purged permanently. |
| Delete User Photo | `deleteUserPhoto` | Removes the profile photo of a Microsoft Entra ID user. |
| Get Administrative Unit | `getAdministrativeUnit` | Retrieves a single Microsoft Entra ID administrative unit by object ID. |
| Get Application | `getApplication` | Retrieves a single Microsoft Entra ID application registration by its directory object ID, including its redirect URIs, exposed app roles and requested API permissions. |
| Get Deleted Directory Item | `getDeletedDirectoryItem` | Retrieves a single recently deleted directory object by its object ID, including the date it was deleted. |
| Get Device | `getDevice` | Retrieves a single device registered with Microsoft Entra ID by its directory object ID. |
| Get Directory Audit Log | `getDirectoryAuditLog` | Retrieves a single directory audit log entry by its ID, with the full list of properties the operation modified. |
| Get Directory Objects By IDs | `getDirectoryObjectsByIds` | Resolves up to 1000 directory object IDs to their full objects in a single call, optionally narrowing the search to particular resource types. Useful for turning a list of member IDs into names. |
| Get Directory Role | `getDirectoryRole` | Retrieves a single activated directory role by its object ID. |
| Get Domain | `getDomain` | Retrieves a single domain registered with the Microsoft Entra ID tenant, by its fully qualified domain name. |
| Get Group | `getGroup` | Retrieves a single Microsoft Entra ID group by object ID. Properties such as allowExternalSenders and autoSubscribeNewMembers are returned only when named explicitly in Select. |
| Get My Profile | `getMyProfile` | Retrieves the profile of the signed-in user. This is the cheapest call for verifying that a connection works, and needs only the User.Read permission. |
| Get OAuth2 Permission Grant | `getOauth2PermissionGrant` | Retrieves a single delegated permission grant by its ID, showing which scopes a client application holds against a resource API. |
| Get Organization | `getOrganization` | Retrieves the tenant's organization record, which carries the company name, address, verified domains, technical contacts and assigned licences. Microsoft Entra ID always contains exactly one organization object. |
| Get Organizational Contact | `getOrgContact` | Retrieves a single organizational contact from the Microsoft Entra ID directory by its object ID. |
| Get Service Principal | `getServicePrincipal` | Retrieves a single Microsoft Entra ID service principal by its object ID, including the app roles and delegated scopes it exposes. |
| Get Sign-In Log | `getSignInLog` | Retrieves a single sign-in event by its ID, including the conditional access policies that were evaluated. |
| Get User | `getUser` | Retrieves a single Microsoft Entra ID user by object ID or user principal name. Some properties, such as aboutMe and birthday, are returned only when named explicitly in Select. |
| Get User Manager | `getUserManager` | Retrieves the manager assigned to a Microsoft Entra ID user. Returns 404 when the user has no manager. |
| Get User Member Groups | `getUserMemberGroups` | Returns the IDs of every group and directory role a user is a member of, including nested memberships. Set Security Enabled Only to true to limit the result to security groups. |
| Get User Photo | `getUserPhoto` | Downloads the profile photo of a Microsoft Entra ID user as binary image data. The response is a file rather than JSON, so it is returned as a file reference. |
| Get User Photo Metadata | `getUserPhotoMetadata` | Retrieves the metadata of a Microsoft Entra ID user's profile photo: its dimensions and content type. Use Get User Photo to download the image itself. |
| List Administrative Unit Members | `listAdministrativeUnitMembers` | Lists the users, groups and devices scoped by a Microsoft Entra ID administrative unit. |
| List Administrative Units | `listAdministrativeUnits` | Lists the administrative units in the Microsoft Entra ID directory. An administrative unit scopes a set of users, groups or devices so that a role assignment applies only to them. |
| List Application Owners | `listApplicationOwners` | Lists the users and service principals who own a Microsoft Entra ID application registration. |
| List Applications | `listApplications` | Lists the application registrations in the Microsoft Entra ID tenant. |
| List Deleted Directory Items | `listDeletedDirectoryItems` | Lists recently deleted directory objects of one type, which stay recoverable for 30 days. Object Type must be one of the Microsoft Graph type names, for example microsoft.graph.user or microsoft.graph.group. |
| List Devices | `listDevices` | Lists the devices registered or joined to the Microsoft Entra ID tenant, with their operating system, trust type and compliance state. |
| List Directory Audit Logs | `listDirectoryAuditLogs` | Lists the directory audit log entries for the tenant, recording who changed what in Microsoft Entra ID and when. Requires the AuditLog.Read.All permission and a Microsoft Entra ID P1 or P2 licence. |
| List Directory Role Members | `listDirectoryRoleMembers` | Lists the users, groups and service principals assigned to an activated directory role. |
| List Directory Role Scoped Members | `listDirectoryRoleScopedMembers` | Lists the scoped members of a directory role, which are assignments limited to an administrative unit rather than the whole tenant. |
| List Directory Role Templates | `listDirectoryRoleTemplates` | Lists every directory role template available in Microsoft Entra ID. A template's ID is what Activate Directory Role needs to bring a role into the tenant. |
| List Directory Roles | `listDirectoryRoles` | Lists the directory roles that are activated in the tenant. Roles that have never been used do not appear until they are activated with Activate Directory Role. |
| List Domain Verification DNS Records | `listDomainVerificationDnsRecords` | Lists the DNS records that must be published at the domain registrar to prove ownership of a domain before it can be verified. |
| List Domains | `listDomains` | Lists the domains registered with the Microsoft Entra ID tenant, showing which are verified and which is the default for new user principal names. |
| List Group Lifecycle Policies | `listGroupLifecyclePolicies` | Lists the Microsoft 365 group expiration policies for the tenant, which control how long a group lives before it must be renewed. |
| List Group Member Of | `listGroupMemberOf` | Lists the groups and administrative units a Microsoft Entra ID group is a direct member of. |
| List Group Members | `listGroupMembers` | Lists the direct members of a Microsoft Entra ID group. Members may be users, other groups, devices, service principals or organizational contacts. |
| List Group Owners | `listGroupOwners` | Lists the owners of a Microsoft Entra ID group. Owners can manage the group's membership and settings. |
| List Group Setting Templates | `listGroupSettingTemplates` | Lists the group setting templates available in the tenant, with the settings each defines and their default values. A template's ID is what Create Group Setting needs. |
| List Group Settings | `listGroupSettings` | Lists the directory-level group settings for the tenant, such as the Microsoft 365 group creation and naming policies. |
| List Group Transitive Member Of | `listGroupTransitiveMemberOf` | Lists every group and administrative unit a Microsoft Entra ID group belongs to, including memberships inherited through nested groups. |
| List Group Transitive Members | `listGroupTransitiveMembers` | Lists every member of a Microsoft Entra ID group, including members inherited through nested groups. |
| List Groups | `listGroups` | Lists the groups in the Microsoft Entra ID directory, including Microsoft 365 groups, security groups and distribution lists. Advanced queries and Search require Count set to true. |
| List OAuth2 Permission Grants | `listOauth2PermissionGrants` | Lists the delegated permission grants in the tenant, which record the API scopes each client application has been consented to on behalf of users. |
| List Organizational Contacts | `listOrgContacts` | Lists the organizational contacts in the Microsoft Entra ID directory, which are people outside the tenant that appear in the address book. |
| List Service Principal App Role Assigned To | `listServicePrincipalAppRoleAssignedTo` | Lists the users, groups and service principals assigned to the application roles this service principal exposes. This is the list of who has access to an enterprise application. |
| List Service Principals | `listServicePrincipals` | Lists the service principals in the Microsoft Entra ID tenant, which are the local instances of applications, including enterprise apps and managed identities. |
| List Sign-In Logs | `listSignInLogs` | Lists the interactive sign-in events recorded for the tenant, including the application, device, location and conditional access outcome. Requires the AuditLog.Read.All permission and a Microsoft Entra ID P1 or P2 licence. |
| List Subscribed SKUs | `listSubscribedSkus` | Lists the subscription SKUs the tenant has purchased, with the number of units bought and consumed. The skuId values here are what Assign User Licence and Assign Group Licence take. |
| List User App Role Assignments | `listUserAppRoleAssignments` | Lists the application roles granted directly to a Microsoft Entra ID user, which is how applications are assigned to a user. |
| List User Direct Reports | `listUserDirectReports` | Lists the users and organizational contacts who report directly to a Microsoft Entra ID user. |
| List User Licence Details | `listUserLicenseDetails` | Lists the subscription licences assigned to a Microsoft Entra ID user, including the individual service plans within each licence and their provisioning status. |
| List User Member Of | `listUserMemberOf` | Lists the groups, directory roles and administrative units a Microsoft Entra ID user is a direct member of. Use List User Transitive Member Of to include nested memberships. |
| List User Owned Objects | `listUserOwnedObjects` | Lists the directory objects a Microsoft Entra ID user owns, such as groups, applications and service principals. Useful before deleting an account. |
| List User Registered Devices | `listUserRegisteredDevices` | Lists the devices registered to a Microsoft Entra ID user. |
| List User Sponsors | `listUserSponsors` | Lists the users and groups sponsoring a Microsoft Entra ID user, which is how guest accounts are attributed to an internal owner. |
| List User Transitive Member Of | `listUserTransitiveMemberOf` | Lists every group, directory role and administrative unit a Microsoft Entra ID user belongs to, including memberships inherited through nested groups. |
| List Users | `listUsers` | Lists the user accounts in the Microsoft Entra ID directory. Advanced queries using Filter with a not, ne, endsWith or count clause also require Count set to true and the ConsistencyLevel eventual header. |
| Permanently Delete Directory Item | `permanentlyDeleteDirectoryItem` | Permanently removes an object from the deleted items container before its 30-day retention expires. This is irreversible and the object can never be restored afterwards. |
| Remove Administrative Unit Member | `removeAdministrativeUnitMember` | Removes a user, group or device from a Microsoft Entra ID administrative unit. The object itself is not deleted. |
| Remove Application Password | `removeApplicationPassword` | Deletes a client secret from a Microsoft Entra ID application registration. Any service authenticating with that secret stops working immediately. |
| Remove Directory Role Member | `removeDirectoryRoleMember` | Removes a principal from an activated directory role, revoking that administrative role. |
| Remove Group Member | `removeGroupMember` | Removes a member from a Microsoft Entra ID group. Members of a dynamic group cannot be removed this way; change the membership rule instead. |
| Remove Group Owner | `removeGroupOwner` | Removes an owner from a Microsoft Entra ID group. The last remaining user owner of a group cannot be removed. |
| Remove Service Principal App Role Assigned To | `removeServicePrincipalAppRoleAssignedTo` | Revokes an application role assignment from a service principal, removing that principal's access to the enterprise application. |
| Remove User App Role Assignment | `removeUserAppRoleAssignment` | Revokes an application role from a Microsoft Entra ID user, removing that application assignment. |
| Remove User Manager | `removeUserManager` | Removes the manager assigned to a Microsoft Entra ID user, leaving the user with no manager. |
| Remove User Sponsor | `removeUserSponsor` | Removes a sponsor from a Microsoft Entra ID user. |
| Renew Group | `renewGroup` | Renews a Microsoft 365 group's expiration, resetting its lifecycle timer so it is not deleted by the group expiration policy. |
| Restore Deleted Directory Item | `restoreDeletedDirectoryItem` | Restores a recently deleted user, group, application, service principal or administrative unit from the deleted items container, returning it to the active directory. |
| Revoke User Sign-In Sessions | `revokeUserSignInSessions` | Invalidates all refresh tokens and session cookies issued to a Microsoft Entra ID user, forcing every application to re-authenticate. Use this when an account is compromised or an employee leaves. |
| Update Administrative Unit | `updateAdministrativeUnit` | Updates a Microsoft Entra ID administrative unit. Only the properties you supply are sent. Member Management Restricted cannot be changed after creation. |
| Update Application | `updateApplication` | Updates a Microsoft Entra ID application registration. Only the properties you supply are sent. Supplying a collection such as redirectUris or appRoles replaces that whole collection. |
| Update Group | `updateGroup` | Updates a Microsoft Entra ID group. Only the properties you supply are sent, so untouched settings keep their values. Group Types cannot be changed after creation. |
| Update OAuth2 Permission Grant | `updateOauth2PermissionGrant` | Changes the set of delegated permissions an existing grant carries. Supplying Scopes replaces the whole space-separated list. |
| Update Organization | `updateOrganization` | Updates the tenant's organization record. Microsoft Graph v1.0 allows only the notification contact lists and the privacy profile to be changed here; the technical and marketing notification lists are not nullable. |
| Update Service Principal | `updateServicePrincipal` | Updates a Microsoft Entra ID service principal, for example to disable it, require app role assignment or change its single sign-on settings. Only the properties you supply are sent. |
| Update User | `updateUser` | Updates a Microsoft Entra ID user. Only the properties you supply are sent, so untouched attributes keep their values. Changing accountEnabled or passwordProfile requires a higher privileged administrator role than ordinary attribute edits. |
| Verify Domain | `verifyDomain` | Verifies ownership of a domain after its DNS verification record has been published. Set Force Takeover only when taking over a domain currently linked to an unmanaged tenant that you own. |

</details>
