---
description: "Zoho Vault is Zoho's workforce password management service."
hidden: true
---

# Zoho Vault

<img src="../../.gitbook/assets/connectors/lg/zoho-vault.png" alt="Zoho Vault logo">

Zoho Vault is Zoho's workforce password management service. This connector wraps the Zoho Vault REST API v1 (vault.zoho.com/api/rest/json/v1): secrets (passwords), secret sharing with users, user groups and third parties, folders (chambers) and folder sharing, users and user groups, and the password, folder, user, misc and activity audit trails. Note that Vault secret payloads are client-side encrypted; secretdata, securenote, customcolumn and file values are exchanged as encrypted strings.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [vault.zoho.com](https://vault.zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `zohoVault` |

## Use it

Add Zoho Vault from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoVault.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Share Passwords With User Groups | `bulkSharePasswordsWithUserGroups` | Shares a set of passwords with multiple Zoho Vault user groups in one call, assigning each group of user groups a logon, view, modify or manage access level across all of the listed passwords. |
| Bulk Share Passwords With Users | `bulkSharePasswordsWithUsers` | Shares a set of passwords with multiple Zoho Vault users in one call, assigning each group of users a logon, view, modify or manage access level across all of the listed passwords. |
| Create Folder | `createFolder` | Creates a folder (chamber) in Zoho Vault to group related passwords, optionally adding an initial set of passwords to it. |
| Create Password | `createPassword` | Creates a new password (secret) in the connected Zoho Vault account. Secret values are client-side encrypted by Zoho Vault, so username, password, file, secure note and custom column values must be supplied already encrypted with the account's org key or master key. |
| Create User Group | `createUserGroup` | Creates a new user group in the connected Zoho Vault account, optionally seeding it with an initial set of members. |
| Delete Folder | `deleteFolder` | Deletes a folder (chamber) from the connected Zoho Vault account by its folder ID. |
| Delete Password | `deletePassword` | Deletes a password (secret) from the connected Zoho Vault account by its password ID. The response returns the deleted password ID. |
| Get Folder | `getFolder` | Returns the details of a single folder (chamber) in Zoho Vault, including the passwords it contains, with optional sorting and pagination of those passwords. |
| Get Folder User Group Sharing | `getFolderUserGroupSharing` | Returns the per-user-group sharing configuration of a folder (chamber), listing which user groups hold view, logon, modify or manage access and which groups the folder is not shared with. |
| Get Folder User Sharing | `getFolderUserSharing` | Returns the per-user sharing configuration of a folder (chamber), listing which users hold view, logon, modify or manage access and which users the folder is not shared with. |
| Get Password | `getPassword` | Retrieves a single password (secret) from Zoho Vault by its password ID, including its encrypted secret data and sharing level. |
| Get Password User Group Sharing | `getPasswordUserGroupSharing` | Returns the per-user-group sharing configuration of a password, listing which user groups hold view, logon, modify or manage access and which groups the password is not shared with. |
| Get Password User Sharing | `getPasswordUserSharing` | Returns the per-user sharing configuration of a password, listing which users hold view, logon, modify or manage access and which users the password is not shared with. |
| Get User | `getUser` | Returns the details of a single Zoho Vault user, identified by their Zoho user ID (ZUID). |
| Get User Group | `getUserGroup` | Returns the details of a single Zoho Vault user group, including its name, description and member list. |
| List Audit Activity | `listAuditActivity` | Returns the audit activity log for the connected Zoho Vault account, recording who viewed each audit trail. Supports date range, operation type, user name and IP filtering with sorting and pagination. |
| List Folder Audit | `listFolderAudit` | Returns the folder (chamber) audit trail for the connected Zoho Vault account, recording every folder operation with the operator, IP address and timestamp. Supports date range, operation type, operator, folder name and IP filtering with sorting and pagination. |
| List Folders | `listFolders` | Searches and lists the folders (chambers) in the connected Zoho Vault account, with optional name search, a shared-only filter, sorting and pagination. |
| List Miscellaneous Audit | `listMiscAudit` | Returns the miscellaneous audit trail for the connected Zoho Vault account, covering settings-level events such as password policy changes, master password changes and two-factor authentication enforcement. Supports date range, operation type, operated-on, operator, user name and IP filtering with sorting and pagination. |
| List Password Audit | `listPasswordAudit` | Returns the password audit trail for the connected Zoho Vault account, recording every password operation with the operator, IP address, agent and timestamp. Supports date range, operation type, operator, password name and IP filtering with sorting and pagination. |
| List Passwords | `listPasswords` | Returns the passwords (secrets) visible to the connected Zoho Vault user, with optional name search, folder and type filtering, sorting and pagination. |
| List Passwords Shared With User | `listPasswordsSharedWithUser` | Returns the passwords that have been shared with a specific Zoho Vault user, identified by email address, with optional name search, sorting and pagination. |
| List User Audit | `listUserAudit` | Returns the user audit trail for the connected Zoho Vault account, recording user administration events such as users added, deleted or having their role changed. Supports date range, operation type, operator, user name and IP filtering with sorting and pagination. |
| List User Groups | `listUserGroups` | Returns all user groups configured in the connected Zoho Vault account. |
| List Users | `listUsers` | Returns the users in the connected Zoho Vault account with their role, email and enabled state, with optional name or email search, sorting and pagination. |
| Share Password With Third Party | `sharePasswordWithThirdParty` | Shares a single password with an external recipient (a third party outside the Vault organization) by email. The password data is re-encrypted client-side with a passphrase, so the caller must supply the derived key authentication string, salt and iteration count. |
| Share Passwords With User | `sharePasswordsWithUser` | Shares one or more passwords with a single Zoho Vault user, granting each listed password the logon, view, modify or manage access level. Secret objects only need to be supplied when the passwords are not encrypted with the organization key. |
| Update Folder | `updateFolder` | Updates an existing folder (chamber) in Zoho Vault, changing its name, description or the set of passwords it contains. Only the fields supplied are sent. |
| Update Folder User Group Sharing | `updateFolderUserGroupSharing` | Replaces the per-user-group sharing configuration of a folder (chamber), setting which user groups hold logon, view, modify or manage access to the folder and its passwords. |
| Update Folder User Sharing | `updateFolderUserSharing` | Replaces the per-user sharing configuration of a folder (chamber), setting which users hold logon, view, modify or manage access to the folder and its passwords. |
| Update Password | `updatePassword` | Updates an existing password (secret) in Zoho Vault. Only the fields supplied are sent, so omitted fields keep their current values. Zoho's published sample spells the payload keys "secertdata" and "secreters"; this action sends the consistent "secretdata" and "secreturls" keys used by the create endpoint. |
| Update Password User Group Sharing | `updatePasswordUserGroupSharing` | Replaces the per-user-group sharing configuration of a password, setting which user groups hold logon, view, modify or manage access. |
| Update Password User Sharing | `updatePasswordUserSharing` | Replaces the per-user sharing configuration of a password, setting which users hold logon, view, modify or manage access. |
| Update Shared File Data | `updateSharedFileData` | Updates the encrypted file attachment data of a password that is encrypted with the organization key. The endpoint expects a top-level JSON array, so the file data must be supplied as a pre-serialized JSON array string. |
| Update User Group | `updateUserGroup` | Updates an existing Zoho Vault user group, changing its name, description or membership. Only the fields supplied are sent. |
