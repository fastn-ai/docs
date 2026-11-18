---
description: "Microsoft Outlook Contacts (personal contacts in Outlook and Microsoft 365) via Microsoft Graph v1.0 (https://graph.microsoft.com/v1.0)."
hidden: true
---

# Microsoft Outlook Contacts

Microsoft Outlook Contacts (personal contacts in Outlook and Microsoft 365) via Microsoft Graph v1.0 (https://graph.microsoft.com/v1.0). Contacts create, read, update, delete and permanent delete; contact folders and child folders; contacts scoped to a folder or child folder; delta queries for incremental contact and folder sync; contact photo retrieval; open extensions; and single- and multi-value extended properties. Microsoft Graph provides no delete operation for an Outlook contact photo, and setting a contact photo requires a raw binary upload that this integration engine cannot currently deliver intact.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [graph.microsoft.com](https://graph.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 34 |
| **Events** | 0 |
| **Slug** | `microsoftOutlookContacts` |

## Use it

Add Microsoft Outlook Contacts from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.microsoftOutlookContacts.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Child Contact Folder | `createChildContactFolder` | Creates a new contact folder as a child of an existing contact folder in the signed-in user's mailbox. |
| Create Contact | `createContact` | Creates a contact in the signed-in user's default Outlook Contacts folder. Only the fields supplied are sent, so a minimal contact is accepted; Microsoft Graph requires no specific field, but the request body cannot be empty, so supply at least one property. |
| Create Contact Folder | `createContactFolder` | Creates a new top-level contact folder in the signed-in user's mailbox. |
| Create Contact In Folder | `createContactInFolder` | Creates a contact inside a specific contact folder in the signed-in user's mailbox. Only the fields supplied are sent, so a minimal contact is accepted; Microsoft Graph requires no specific field, but the request body cannot be empty, so supply at least one property. |
| Create Contact Open Extension | `createContactOpenExtension` | Adds an open extension to a contact so you can store your own custom properties alongside it. Microsoft Graph accepts arbitrary custom property names at the top level of the extension, so the extension body is supplied as a JSON object string, for example {"@odata.type":"microsoft.graph.openTypeExtension","extensionName":"com.contoso.loyalty","tier":"gold","points":120}. The extension name must be unique within the contact. |
| Delete Contact | `deleteContact` | Deletes a contact from the signed-in user's default Outlook Contacts folder. The contact is moved to Deleted Items and can still be recovered by the user; use Permanently Delete Contact to purge it. Returns 204 No Content with an empty body on success. |
| Delete Contact Folder | `deleteContactFolder` | Deletes a contact folder from the signed-in user's mailbox, along with the contacts it contains. The folder is moved to Deleted Items and can still be recovered by the user. Returns 204 No Content on success. |
| Delete Contact In Folder | `deleteContactInFolder` | Deletes a contact from a specific contact folder in the signed-in user's mailbox. The contact is moved to Deleted Items and can still be recovered by the user. Returns 204 No Content on success. |
| Delete Contact Open Extension | `deleteContactOpenExtension` | Removes an open extension and all the custom properties it holds from a contact. Returns 204 No Content on success. |
| Find Contacts By Extended Property | `findContactsByExtendedProperty` | Finds contacts in the signed-in user's default Contacts folder that carry a single-value MAPI extended property with a given value. Supply the filter expression Microsoft Graph documents, for example singleValueExtendedProperties/Any(ep: ep/id eq 'String {66f5a359-4659-4830-9070-00047ec6ac6e} Name CustomField' and ep/value eq 'Gold'). |
| Get Contact | `getContact` | Retrieves a single contact from the signed-in user's default Outlook Contacts folder by its contact ID. |
| Get Contact Delta | `getContactDelta` | Tracks incremental changes to the contacts in a specific contact folder. Call it once without a token to start a round, then follow the returned next link or delta link token on later calls to get only contacts added, changed or deleted since the previous call. Deleted contacts appear as entries carrying an @removed annotation. |
| Get Contact Folder | `getContactFolder` | Retrieves a single contact folder from the signed-in user's mailbox by its folder ID. Works for top-level folders and for child folders, since a child folder is addressable by its own ID. |
| Get Contact Folder Delta | `getContactFolderDelta` | Tracks incremental changes to the contact folders in the signed-in user's mailbox. Call it once without a token to start a round, then follow the returned next link or delta link token on later calls to get only folders added, renamed or deleted since the previous call. |
| Get Contact Folder With Extended Properties | `getContactFolderWithExtendedProperties` | Retrieves a contact folder together with a named MAPI extended property. Supply the expand expression Microsoft Graph documents for extended properties on a contact folder. |
| Get Contact In Child Folder | `getContactInChildFolder` | Retrieves a single contact from a child folder nested under a top-level contact folder in the signed-in user's mailbox. |
| Get Contact In Folder | `getContactInFolder` | Retrieves a single contact from a specific contact folder in the signed-in user's mailbox. |
| Get Contact Open Extension | `getContactOpenExtension` | Retrieves a single open extension on a contact by its extension name, together with the custom properties it holds. |
| Get Contact Photo | `getContactPhoto` | Downloads the picture attached to a contact in the signed-in user's default Outlook Contacts folder. The image is returned as binary content; Microsoft Graph responds 404 when the contact has no picture. |
| Get Contact Photo Metadata | `getContactPhotoMetadata` | Retrieves the metadata of a contact's picture, including its dimensions, without downloading the image bytes. Microsoft Graph responds 404 when the contact has no picture. |
| Get Contact With Extended Properties | `getContactWithExtendedProperties` | Retrieves a contact together with a named MAPI extended property. Supply the expand expression Microsoft Graph documents for extended properties, for example singleValueExtendedProperties($filter=id eq 'String {66f5a359-4659-4830-9070-00047ec6ac6e} Name CustomField') or the equivalent multiValueExtendedProperties expression. |
| List Child Contact Folders | `listChildContactFolders` | Lists the child folders directly underneath a given contact folder in the signed-in user's mailbox. |
| List Contact Folders | `listContactFolders` | Lists the top-level contact folders in the signed-in user's mailbox. Use the returned folder IDs with the folder-scoped contact actions. |
| List Contacts | `listContacts` | Lists the contacts in the signed-in user's default Outlook Contacts folder. Supports OData paging, sorting, field selection and filtering; note that Microsoft Graph only allows $filter on the address sub-property of emailAddresses using any() with eq. |
| List Contacts In Child Folder | `listContactsInChildFolder` | Lists the contacts held in a child folder nested under a top-level contact folder in the signed-in user's mailbox. |
| List Contacts In Folder | `listContactsInFolder` | Lists the contacts held in a specific contact folder in the signed-in user's mailbox. Supports OData paging, sorting and field selection; Microsoft Graph only allows $filter on the address sub-property of emailAddresses using any() with eq. |
| Permanently Delete Child Contact Folder | `permanentlyDeleteChildContactFolder` | Permanently deletes a child contact folder and removes its contacts from the signed-in user's mailbox. This is irreversible for the user; requires the Contacts.ReadWrite permission and returns 204 No Content on success. |
| Permanently Delete Contact | `permanentlyDeleteContact` | Permanently deletes a contact from the signed-in user's default Outlook Contacts folder and places it in the purges folder of the recoverable items area, where Outlook clients cannot reach it. This is irreversible for the user; requires the Contacts.ReadWrite permission and returns 204 No Content on success. |
| Permanently Delete Contact Folder | `permanentlyDeleteContactFolder` | Permanently deletes a contact folder and removes its contacts from the signed-in user's mailbox. This is irreversible for the user; requires the Contacts.ReadWrite permission and returns 204 No Content on success. |
| Permanently Delete Contact In Folder | `permanentlyDeleteContactInFolder` | Permanently deletes a contact from a specific contact folder and places it in the purges folder of the recoverable items area, where Outlook clients cannot reach it. This is irreversible for the user; requires the Contacts.ReadWrite permission and returns 204 No Content on success. |
| Update Contact | `updateContact` | Updates a contact in the signed-in user's default Outlook Contacts folder. This is a partial update: only the fields supplied are sent to Microsoft Graph, and fields left blank are not changed. Always include Display Name if the contact has one you want preserved, because Outlook can regenerate it when other name fields change. |
| Update Contact Folder | `updateContactFolder` | Renames a contact folder in the signed-in user's mailbox. Display name is the only writable property on a contact folder. |
| Update Contact In Folder | `updateContactInFolder` | Updates a contact held in a specific contact folder in the signed-in user's mailbox. This is a partial update: only the fields supplied are sent, and fields left blank are not changed. Collection fields such as email addresses and phone numbers are replaced in full when supplied. |
| Update Contact Open Extension | `updateContactOpenExtension` | Updates the custom properties stored in an open extension on a contact. The body must repeat "@odata.type": "microsoft.graph.openTypeExtension" and the "extensionName", otherwise Microsoft Graph rejects the custom properties with "The property 'x' does not exist on type 'microsoft.graph.extension'". Properties you do not name are left unchanged. |
