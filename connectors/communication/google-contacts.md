---
description: "Google People API v1 — manage the authenticated user's contacts, contact groups, other contacts, and read domain directory profiles."
hidden: true
---

# Google Contacts

Google People API v1 — manage the authenticated user's contacts, contact groups, other contacts, and read domain directory profiles.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [people.googleapis.com](https://people.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 24 |
| **Events** | 0 |
| **Slug** | `googleContacts` |

## Use it

Add Google Contacts from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleContacts.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Create Contacts | `batchCreateContacts` | Creates up to 200 contacts in a single request and returns a person response for each one. Mutating requests for the same user should be sent sequentially to avoid contention. |
| Batch Delete Contacts | `batchDeleteContacts` | Deletes up to 500 contacts in a single request. Profile data that is not contact data is not deleted. Returns an empty body on success. |
| Batch Get Contact Groups | `batchGetContactGroups` | Retrieves one contact group by resource name and returns it inside a per-group response with its own status. Pass one resource name per call; to read several groups, call this action once per group. |
| Batch Get People | `batchGetPeople` | Retrieves one person by resource name and returns it inside a per-person response with its own status. A field mask (Person Fields) is required. Pass one resource name per call; to read several people, call this action once per person. |
| Batch Update Contacts | `batchUpdateContacts` | Updates up to 200 existing contacts in a single request and returns a person response for each one. The contacts are supplied as a map keyed by resource name, and each person must carry its current etag. |
| Copy Other Contact To My Contacts | `copyOtherContactToMyContacts` | Promotes an Other Contact into a real contact in the user's myContacts group, copying the field families named in the copy mask. |
| Create Contact | `createContact` | Creates a new contact in the authenticated user's contacts and returns the created person. Each singleton field family such as biographies, birthdays, and genders accepts at most one entry for a contact source. |
| Create Contact Group | `createContactGroup` | Creates a new contact group owned by the authenticated user. Group names must be unique within the user's contact groups, and a duplicate name returns an HTTP 409 error. |
| Delete Contact | `deleteContact` | Deletes a contact from the authenticated user's contacts. Profile data that is not contact data is not deleted. |
| Delete Contact Group | `deleteContactGroup` | Deletes a contact group owned by the authenticated user, and optionally deletes the contacts that belong to it. System contact groups cannot be deleted. |
| Delete Contact Photo | `deleteContactPhoto` | Removes a contact's photo, reverting the contact to the default placeholder image. |
| Get Contact Group | `getContactGroup` | Retrieves a single contact group owned by the authenticated user, optionally including the resource names of its members. |
| Get Person | `getPerson` | Retrieves a single person by id. Use the person id 'me' to fetch the authenticated user's own profile. A field mask is required, and the request fails with 400 if it is omitted. |
| List Connections | `listConnections` | Lists the authenticated user's contacts, with paging and optional incremental sync. A field mask is required. Sync tokens expire 7 days after the full sync. |
| List Contact Groups | `listContactGroups` | Lists all contact groups owned by the authenticated user, including the system groups such as My Contacts and Starred. Group members are not populated by this call. |
| List Directory People | `listDirectoryPeople` | Lists the domain profiles and domain contacts in the authenticated user's Google Workspace directory. Requires a Google Workspace account with directory sharing enabled. |
| List Other Contacts | `listOtherContacts` | Lists the authenticated user's Other Contacts, which are the auto-created contacts from interactions such as email that do not belong to any contact group. Sync tokens expire 7 days after the full sync. |
| Modify Contact Group Members | `modifyContactGroupMembers` | Adds contacts to and removes contacts from a contact group. Among system groups only contactGroups/myContacts and contactGroups/starred accept member changes. At most 1000 contacts may be added and 1000 removed per request. |
| Search Contacts | `searchContacts` | Searches the authenticated user's contacts by prefix match against names, nicknames, email addresses, phone numbers, and organizations. Send an empty query first to warm the search cache, as newly changed contacts can take several seconds to become searchable. |
| Search Directory People | `searchDirectoryPeople` | Searches the domain profiles and domain contacts in the authenticated user's Google Workspace directory. Requires a Google Workspace account with directory sharing enabled. |
| Search Other Contacts | `searchOtherContacts` | Searches the authenticated user's Other Contacts by prefix match against names, email addresses, and phone numbers. Send an empty query first to warm the search cache. |
| Update Contact | `updateContact` | Updates an existing contact in the authenticated user's contacts. Every field family named in the update mask is replaced wholesale, so send the complete desired set of entries for each one. The contact's current etag must be supplied. |
| Update Contact Group | `updateContactGroup` | Renames an existing contact group owned by the authenticated user. The new name must be unique among the user's contact groups, and the group's current etag must be supplied. |
| Update Contact Photo | `updateContactPhoto` | Sets or replaces a contact's photo from raw image bytes. The image must be supplied base64-encoded and be a JPEG, PNG, or similar raster format. |
