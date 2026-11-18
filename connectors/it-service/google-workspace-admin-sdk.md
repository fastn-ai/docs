---
description: "Administer a Google Workspace account with the Admin SDK."
hidden: true
---

# Google Workspace Admin SDK

<img src="../../.gitbook/assets/connectors/lg/google-workspace-admin-sdk.png" alt="Google Workspace Admin SDK logo">

Administer a Google Workspace account with the Admin SDK. Provision and manage users, aliases, photos, groups, group members, organizational units, roles and role assignments, privileges, domains, ChromeOS and mobile devices, application-specific passwords, tokens, verification codes, custom user schemas, calendar resources (buildings, features, calendars), Chrome printers and print servers, and cross-user data transfers. Requires a Google Workspace administrator account and the customer identifier my_customer.

| | |
| --- | --- |
| **Category** | [IT and service management](README.md) |
| **Website** | [admin.google.com](https://admin.google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleWorkspaceAdminSdk` |

## Use it

Add Google Workspace Admin SDK from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleWorkspaceAdminSdk.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Group Member | `insertMember` | Add a member (user, group, or external address) to a group. |
| Batch Change ChromeOS Device Status | `batchChangeChromeOsDeviceStatus` | Change the status (deprovision, disable, re-enable) of a batch of ChromeOS devices in one call. |
| Batch Create Print Servers | `batchCreatePrintServers` | Create a batch of Chrome print servers in one call. |
| Batch Create Printers | `batchCreatePrinters` | Create a batch of Chrome printers in one call (up to 50). |
| Batch Delete Print Servers | `batchDeletePrintServers` | Delete a batch of Chrome print servers in one call. |
| Batch Delete Printers | `batchDeletePrinters` | Delete a batch of Chrome printers in one call (up to 100). |
| Check Group Membership | `hasMember` | Check whether a user is a member of a group, including indirect membership via nested groups. |
| Create Building | `insertBuilding` | Create a new building for organizing calendar resources. |
| Create Calendar Resource | `insertCalendarResource` | Create a new calendar resource such as a conference room. |
| Create Contact Delegate | `createContactDelegate` | Grant a user access to manage another user's contacts by creating a contact delegate. Both users must belong to the same Google Workspace organization, and contact sharing must be turned on for the organization in the Admin console. |
| Create Custom User Schema | `insertSchema` | Create a custom user schema to store additional structured data on user profiles. |
| Create Data Transfer | `insertTransfer` | Request a data transfer, moving application data (such as Drive or Calendar) from one user to another. |
| Create Domain | `insertDomain` | Add a secondary domain to the account. The domain must be verified before it can be used. |
| Create Domain Alias | `insertDomainAlias` | Add a domain alias for an existing domain in the account. |
| Create Feature | `insertFeature` | Create a new calendar resource feature. |
| Create Group | `insertGroup` | Create a new group. The email address must use a domain that belongs to the account. |
| Create Group Alias | `insertGroupAlias` | Add an alias email address for a group. |
| Create Organizational Unit | `insertOrgUnit` | Create a new organizational unit under a parent org unit. |
| Create Print Server | `createPrintServer` | Create a Chrome print server configuration. |
| Create Printer | `createPrinter` | Create a Chrome printer configuration. |
| Create Role | `insertRole` | Create a custom administrator role with a set of privileges. |
| Create Role Assignment | `insertRoleAssignment` | Assign an administrator role to a user or group, scoped to the whole customer or an organizational unit. |
| Create User | `insertUser` | Create a new user in the Google Workspace account. Requires a primary email, given and family name, and a password. |
| Create User Alias | `insertUserAlias` | Add an alias email address for a user. |
| Delete Application-Specific Password | `deleteAsp` | Revoke an application-specific password for a user. |
| Delete Building | `deleteBuilding` | Delete a building. The building must not contain any calendar resources. |
| Delete Calendar Resource | `deleteCalendarResource` | Delete a calendar resource. |
| Delete Chrome Browser Device | `deleteChromeBrowserDevice` | Remove a Chrome browser device from Chrome Enterprise Core, unenrolling it from cloud management. The browser stops receiving cloud policy and no longer reports to the Admin console. |
| Delete Contact Delegate | `deleteContactDelegate` | Revoke a contact delegate's access to manage a given user's contacts. |
| Delete Custom User Schema | `deleteSchema` | Delete a custom user schema. |
| Delete Domain | `deleteDomain` | Remove a secondary domain from the account. |
| Delete Domain Alias | `deleteDomainAlias` | Remove a domain alias from the account. |
| Delete Feature | `deleteFeature` | Delete a calendar resource feature. |
| Delete Group | `deleteGroup` | Permanently delete a group. |
| Delete Group Alias | `deleteGroupAlias` | Remove an alias email address from a group. |
| Delete Mobile Device | `deleteMobileDevice` | Remove a mobile device from management. |
| Delete OAuth Token | `deleteToken` | Revoke an OAuth token a user issued to a third-party application. |
| Delete Organizational Unit | `deleteOrgUnit` | Delete an organizational unit. The unit must not contain any users or child units. |
| Delete Print Server | `deletePrintServer` | Delete a Chrome print server configuration. |
| Delete Printer | `deletePrinter` | Delete a Chrome printer configuration. |
| Delete Role | `deleteRole` | Delete a custom administrator role. |
| Delete Role Assignment | `deleteRoleAssignment` | Remove an administrator role assignment. |
| Delete User | `deleteUser` | Permanently delete a user. The account cannot be undeleted after 20 days. |
| Delete User Alias | `deleteUserAlias` | Remove an alias email address from a user. |
| Delete User Photo | `deleteUserPhoto` | Remove the user's profile photo. The user is then shown a default silhouette. |
| Generate Verification Codes | `generateVerificationCodes` | Generate a new set of backup verification codes for a user, invalidating any existing set. |
| Get Application-Specific Password | `getAsp` | Retrieve a single application-specific password by its code ID. |
| Get Building | `getBuilding` | Retrieve a single building by ID. |
| Get Calendar Resource | `getCalendarResource` | Retrieve a single calendar resource by ID. |
| Get Chrome Browser Device | `getChromeBrowserDevice` | Retrieve the properties of a single Chrome browser device enrolled in Chrome Enterprise Core (Chrome Browser Cloud Management). |
| Get ChromeOS Device | `getChromeOsDevice` | Retrieve a single managed ChromeOS device by device ID. |
| Get Custom User Schema | `getSchema` | Retrieve a single custom user schema by name or ID. |
| Get Customer | `getCustomer` | Retrieve the Google Workspace customer account details. |
| Get Customer Usage Report | `getCustomerUsageReport` | Retrieves account-wide (customer-level) usage statistics for the Google Workspace organization on a given date, such as total accounts, active users and app usage counts, from the Admin SDK Reports API customerUsageReports.get. Read-only. Google scope: admin.reports.usage.readonly. Requires a Workspace administrator. Use a date at least 2-3 days in the past (Pacific time). Returns usageReports[] with parameters[] name/value pairs, warnings[] and nextPageToken. |
| Get Data Transfer | `getTransfer` | Retrieve a single data transfer request by ID. |
| Get Data Transfer Application | `getTransferApplication` | Retrieve a single data-transfer-capable application by ID. |
| Get Domain | `getDomain` | Retrieve a single domain of the account. |
| Get Domain Alias | `getDomainAlias` | Retrieve a single domain alias of the account. |
| Get Entity Usage Report | `getEntityUsageReport` | Retrieves usage statistics for entities (objects shared by users, such as Google Currents communities) on a given date from the Admin SDK Reports API entityUsageReports.get. Read-only. Google scope: admin.reports.usage.readonly. Requires a Workspace administrator. Google currently documents only entityType gplus_communities, so most organizations get an empty report or a warning. Returns usageReports[], warnings[] and nextPageToken. |
| Get Feature | `getFeature` | Retrieve a single calendar resource feature by name. |
| Get Group | `getGroup` | Retrieve a single group by email address or immutable group ID. |
| Get Group Member | `getMember` | Retrieve a single group member. |
| Get Mobile Device | `getMobileDevice` | Retrieve a single managed mobile device by resource ID. |
| Get OAuth Token | `getToken` | Retrieve a single OAuth token a user issued to an application, identified by client ID. |
| Get Organizational Unit | `getOrgUnit` | Retrieve a single organizational unit by path or ID. |
| Get Print Server | `getPrintServer` | Retrieve a single Chrome print server by ID. |
| Get Printer | `getPrinter` | Retrieve a single Chrome printer by ID. |
| Get Role | `getRole` | Retrieve a single administrator role by ID. |
| Get Role Assignment | `getRoleAssignment` | Retrieve a single role assignment by ID. |
| Get User | `getUser` | Retrieve a single user by primary email, alias email or immutable user ID. |
| Get User Photo | `getUserPhoto` | Retrieve the user's profile photo (thumbnail). |
| Get User Usage Report | `getUserUsageReport` | Retrieves per-user usage statistics (e.g. Gmail messages sent, Drive files created, last login time) for one user or all users on a given date from the Admin SDK Reports API userUsageReport.get. Read-only. Google scope: admin.reports.usage.readonly. Requires a Workspace administrator. Reports lag by about 2-3 days, so use a date at least 3 days ago (dates are in Pacific time). Returns usageReports[] (entity + parameters[] name/value pairs), warnings[] and nextPageToken. |
| Invalidate Verification Codes | `invalidateVerificationCodes` | Invalidate the current backup verification codes for a user. |
| List Activities | `listActivities` | Retrieves audit log activity events for a Google Workspace application (Admin console, login, Drive, Gmail, Calendar, Meet, Chat, tokens, etc.) from the Admin SDK Reports API activities.list, for all users or one user. Read-only. Google scope: admin.reports.audit.readonly. Requires a Workspace administrator with reports privileges. Example: applicationName=login, userKey=all, maxResults=10. Returns items[] (each with id.time, actor.email, ipAddress and events[] with name and parameters) plus nextPageToken. |
| List Application-Specific Passwords | `listAsps` | List the application-specific passwords (ASPs) issued for a user. |
| List Buildings | `listBuildings` | List the buildings defined for the account. |
| List Calendar Resources | `listCalendarResources` | List the calendar resources (rooms and other bookable resources) of the account. |
| List Chrome Browser Devices | `listChromeBrowserDevices` | List the Chrome browser devices enrolled in Chrome Enterprise Core (Chrome Browser Cloud Management) for the account, with optional filtering by organizational unit, group or search query. |
| List ChromeOS Devices | `listChromeOsDevices` | List the ChromeOS devices managed for the account. |
| List Contact Delegates | `listContactDelegates` | List the contact delegates of a given user. A contact delegate is another user in the same Google Workspace organization who has been granted access to manage that user's contacts. |
| List Custom User Schemas | `listSchemas` | List the custom user schemas defined for the account. |
| List Data Transfer Applications | `listTransferApplications` | List the applications that support data transfer for the account. |
| List Data Transfers | `listTransfers` | List the data transfer requests for the account. |
| List Domain Aliases | `listDomainAliases` | List the domain aliases of the account, optionally filtered by parent domain. |
| List Domains | `listDomains` | List the domains of the account. |
| List Features | `listFeatures` | List the calendar resource features (equipment or amenities) defined for the account. |
| List Group Aliases | `listGroupAliases` | List all alias email addresses for a group. |
| List Group Members | `listMembers` | List the members of a group, optionally filtered by role. |
| List Groups | `listGroups` | List groups in the account or domain, optionally filtered to those a specific member belongs to. |
| List Mobile Devices | `listMobileDevices` | List the mobile devices managed for the account. |
| List OAuth Tokens | `listTokens` | List the OAuth access tokens a user has issued to third-party applications. |
| List Organizational Units | `listOrgUnits` | List the organizational units of an account, optionally under a parent path. |
| List Print Servers | `listPrintServers` | List the Chrome print servers configured for the account. |
| List Printer Models | `listPrinterModels` | List the supported printer makes and models for Chrome printer configuration. |
| List Printers | `listPrinters` | List the Chrome printers configured for the account. |
| List Privileges | `listPrivileges` | List all privileges that can be assigned to administrator roles in the account. |
| List Role Assignments | `listRoleAssignments` | List administrator role assignments, optionally filtered by role or user. |
| List Roles | `listRoles` | List the administrator roles defined for the account. |
| List User Aliases | `listUserAliases` | List all alias email addresses for a user. |
| List Users | `listUsers` | Retrieve a paginated list of users in a Google Workspace account or domain. Supply customer=my_customer to list all users in the account, or a domain to scope the results. |
| List Verification Codes | `listVerificationCodes` | List the current set of valid backup verification codes for a user. |
| Make User Super Admin | `makeAdminUser` | Grant or revoke a user's super administrator status. |
| Move Chrome Browser Devices To Org Unit | `moveChromeBrowserDevicesToOu` | Move a batch of Chrome browser devices from their current organizational unit to another one. A maximum of 600 devices may be moved in a single request. |
| Move ChromeOS Devices To Organizational Unit | `moveChromeOsDevicesToOu` | Move one or more ChromeOS devices to a different organizational unit. |
| Patch Building | `patchBuilding` | Partially update a building. |
| Patch Calendar Resource | `patchCalendarResource` | Partially update a calendar resource. |
| Patch ChromeOS Device | `patchChromeOsDevice` | Partially update the administrator-editable fields of a ChromeOS device. |
| Patch Custom User Schema | `patchSchema` | Partially update a custom user schema. |
| Patch Customer | `patchCustomer` | Partially update the customer account's contact and address details. |
| Patch Feature | `patchFeature` | Partially update a calendar resource feature. |
| Patch Group | `patchGroup` | Partially update an existing group. |
| Patch Group Member | `patchMember` | Partially update a group member's role or delivery settings. |
| Patch Organizational Unit | `patchOrgUnit` | Partially update an organizational unit. Moving it is done by changing parentOrgUnitPath. |
| Patch Role | `patchRole` | Partially update a custom administrator role. |
| Patch User | `patchUser` | Partially update an existing user. Only supplied fields are changed when patching. |
| Patch User Photo | `patchUserPhoto` | Partially update the user's profile photo. The photo data must be web-safe base64 encoded. |
| Remove Group Member | `deleteMember` | Remove a member from a group. |
| Rename Feature | `renameFeature` | Rename a calendar resource feature. |
| Sign Out User | `signOutUser` | Sign a user out of all web and device sessions and reset their sign-in cookies. |
| Take Action On ChromeOS Device | `actionChromeOsDevice` | Take an action on a ChromeOS device, such as deprovisioning, disabling or re-enabling it. |
| Take Action On Mobile Device | `actionMobileDevice` | Perform a remote action on a managed mobile device, such as wiping or blocking it. |
| Turn Off Two-Step Verification | `turnOffTwoStepVerification` | Turn off two-step verification enrollment for a user. |
| Undelete User | `undeleteUser` | Undelete a recently deleted user. The userKey must be the immutable user ID of the deleted user, not the email address. |
| Update Building | `updateBuilding` | Update a building. |
| Update Calendar Resource | `updateCalendarResource` | Update a calendar resource. |
| Update Chrome Browser Device | `updateChromeBrowserDevice` | Update the administrator-annotated fields of a Chrome browser device enrolled in Chrome Enterprise Core. Only the annotated fields can be changed; all other properties are reported by the device itself. This endpoint replaces the annotated values, so supply every annotated field you want to keep, not only the ones you are changing. |
| Update ChromeOS Device | `updateChromeOsDevice` | Update the administrator-editable fields of a ChromeOS device. |
| Update Custom User Schema | `updateSchema` | Update a custom user schema. |
| Update Customer | `updateCustomer` | Update the customer account's contact and address details. |
| Update Feature | `updateFeature` | Update a calendar resource feature. |
| Update Group | `updateGroup` | Fully update an existing group. |
| Update Group Member | `updateMember` | Update a group member's role or delivery settings. |
| Update Organizational Unit | `updateOrgUnit` | Update an organizational unit. Moving it is done by changing parentOrgUnitPath. |
| Update Print Server | `patchPrintServer` | Partially update a Chrome print server configuration. |
| Update Printer | `patchPrinter` | Partially update a Chrome printer configuration. |
| Update Role | `updateRole` | Update a custom administrator role. |
| Update User | `updateUser` | Fully update an existing user. Only supplied fields are changed when patching. |
| Update User Photo | `updateUserPhoto` | Set the user's profile photo. The photo data must be web-safe base64 encoded. |
| Watch User Aliases | `watchUserAliases` | Subscribe to change notifications for a user's aliases via a webhook channel. Requires a verified HTTPS webhook receiver. Core channel fields only. |
| Watch Users | `watchUsers` | Subscribe to change notifications for user resources via a webhook channel. Requires a verified, HTTPS webhook receiver domain. Core channel fields only. |
