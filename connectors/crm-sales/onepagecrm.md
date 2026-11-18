---
description: "OnePageCRM is an action-focused sales CRM."
hidden: true
---

# OnePageCRM

<img src="../../.gitbook/assets/connectors/lg/onepagecrm.png" alt="OnePageCRM logo">

OnePageCRM is an action-focused sales CRM. This connector wraps the OnePageCRM REST API v3 to manage contacts, companies, deals, next actions, notes, calls, meetings, relationships, attachments, pipelines, statuses, lead sources, custom fields, predefined actions and items, filters, notifications, users and webhooks.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [onepagecrm.com](https://onepagecrm.com) |
| **Authentication** | Basic auth |
| **Slug** | `onepagecrm` |

## Use it

Add OnePageCRM from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.onepagecrm.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Call Attachment | `addCallAttachment` | Attaches a file to an existing call. Upload the file to S3 first using Get Attachment Upload Form, or pass an external Dropbox, Google Drive or Evernote link. |
| Add Deal Attachment | `addDealAttachment` | Attaches a file to an existing deal. Upload the file to S3 first using Get Attachment Upload Form, or pass an external Dropbox, Google Drive or Evernote link. |
| Add Meeting Attachment | `addMeetingAttachment` | Attaches a file to an existing meeting. Upload the file to S3 first using Get Attachment Upload Form, or pass an external Dropbox, Google Drive or Evernote link. |
| Add Note Attachment | `addNoteAttachment` | Attaches a file to an existing note. Upload the file to S3 first using Get Attachment Upload Form, or pass an external Dropbox, Google Drive or Evernote link. |
| Assign Contact Tag | `assignContactTag` | Adds a tag to a contact. Tag names match the account's existing tags case-insensitively. |
| Change Contact Owner | `changeContactOwner` | Sets a contact's owner to another user on the account. |
| Change Contact Status | `changeContactStatus` | Sets a contact's status to one of the account's configured statuses. |
| Close Contact Sales Cycle | `closeContactSalesCycle` | Closes the sales cycle for a contact when you are no longer actively selling to them, with an optional closing comment. Fails if the user has any open actions on the contact. |
| Create Action | `createAction` | Creates a next action on a contact. contact_id and text are required (text max 140 characters). status sets the action type: asap, date, date_time, waiting or queued (default date); assignee_id defaults to the calling user. |
| Create Attachment | `createAttachment` | Creates an attachment on a deal, note, call or meeting. Upload the file to S3 first using Get Attachment Upload Form, or pass an external Dropbox, Google Drive or Evernote link. |
| Create Call | `createCall` | Logs a phone call against a contact. contact_id is required; record the outcome with call_result (from the account's configured call results), plus the number dialled and an optional recording link. |
| Create Company Field | `createCompanyField` | Creates a custom field for companies. Admin only. Choices are required for select_box and multiple_choice fields. |
| Create Contact | `createContact` | Creates a contact. Provide last_name or company_name — one of the two is required. owner_id defaults to the calling user and status_id to lead. company_name links the contact to an existing company (matched case-insensitively) or creates one; company_id is ignored on create. |
| Create Contact Action | `createContactAction` | Creates a next action on a contact. text is required (max 140 characters). status sets the action type: asap, date, date_time, waiting or queued (default date); assignee_id defaults to the calling user. |
| Create Contact Call | `createContactCall` | Logs a phone call against a contact. Record the outcome with call_result (from the account's configured call results), plus the number dialled and an optional recording link. |
| Create Contact Deal | `createContactDeal` | Creates a deal on a contact. name is required (max 60 characters). status is pending, won or lost (default pending); stage applies to pending deals only. amount is the per-month value; for recurring deals the total is amount multiplied by months. |
| Create Contact Meeting | `createContactMeeting` | Logs a meeting against a contact. place is free-form text (max 100 characters); meeting_time_int records when it happened. |
| Create Contact Note | `createContactNote` | Logs a note against a contact. text carries the note body; link a deal with linked_deal_id. Logging a note updates the contact's last activity date. |
| Create Contact Photo | `createContactPhoto` | Adds a photo to an existing contact from a Base64-encoded image. Images are cropped to a centered square and resized to 200x200 pixels. |
| Create Contact Relationship | `createContactRelationship` | Links a contact to another contact. related_contacts must hold exactly two entries (one of them this contact), each with the variant_id for its end. A contact can hold at most one relationship with any other contact. |
| Create Custom Field | `createCustomField` | Creates a contact custom field. Admin only. Choices are required for select_box and multiple_choice fields. |
| Create Deal | `createDeal` | Creates a deal on a contact. contact_id and name are required (name up to 60 characters). status defaults to pending; stage is a per-pipeline integer and applies to pending deals only. amount is the per-month value; for recurring deals the total is amount multiplied by months. |
| Create Deal Field | `createDealField` | Creates a custom field for deals. Admin only. Choices are required for select_box and multiple_choice fields. |
| Create Lead Source | `createLeadSource` | Creates a lead source. text is required and limited to 40 characters; the id is server-generated. Admin only. The list is kept in alphabetical order. |
| Create Meeting | `createMeeting` | Logs a meeting against a contact. contact_id is required; place is free-form text (max 100 characters) and meeting_time_int records when it happened. |
| Create Note | `createNote` | Logs a note against a contact. contact_id is required; text carries the note body; link a deal with linked_deal_id. Logging a note updates the contact's last activity date. |
| Create Predefined Action | `createPredefinedAction` | Creates a predefined action template. text (max 140 characters) and days are required; text can embed placeholders like [first name] that are substituted when the action is applied to a contact. |
| Create Predefined Action Group | `createPredefinedActionGroup` | Creates a predefined action group. text is required and action_ids must list at least two existing, currently ungrouped predefined actions. |
| Create Predefined Item | `createPredefinedItem` | Creates a predefined item (product or service template for deal line items). name is required and must be unique on the account; description, cost and price are optional. |
| Create Predefined Item Group | `createPredefinedItemGroup` | Creates a predefined item group that bundles existing predefined items. name is required and must be unique on the account. The group's cost and price are derived from its members. |
| Create Relationship Type | `createRelationshipType` | Creates a relationship type from a variants list: one variant name makes a symmetrical type, two make a directional one. An account is limited to 50 types and variant names to 35 characters. |
| Create Status | `createStatus` | Creates a contact status. text (max 20 characters) and color are required, description (max 33) is optional. Admin only. The system id is server-assigned. |
| Delete Action | `deleteAction` | Deletes a next action. Repeat the same request with undo=true to restore it. |
| Delete Attachment | `deleteAttachment` | Deletes an attachment from the note, call, meeting or deal it was uploaded to. |
| Delete Call | `deleteCall` | Deletes a logged call permanently (no undo via the API). Its attachments are removed with it. |
| Delete Company Field | `deleteCompanyField` | Deletes a company custom field. Admin only. |
| Delete Company Logo | `deleteCompanyLogo` | Deletes a company's logo. On success the company's photo_url is null. |
| Delete Contact | `deleteContact` | Deletes a contact. Only users with the delete_contacts permission can delete contacts. Repeat the same request with undo=true to restore the most recent deletion for that ID — the restore window depends on the account plan, from 1 day up to 60 days. |
| Delete Contact Photo | `deleteContactPhoto` | Removes a contact's photo and returns the updated contact, whose photo_url is then empty. |
| Delete Contact Relationship | `deleteContactRelationship` | Deletes a relationship between two contacts. Repeat the same request with undo=true to restore it. |
| Delete Contacts | `deleteContacts` | Deletes multiple contacts by ID in one request. Only users with the delete_contacts permission can delete contacts. |
| Delete Custom Field | `deleteCustomField` | Deletes a contact custom field. Admin only. |
| Delete Deal | `deleteDeal` | Deletes a deal. Only users with the delete_deals permission can delete deals. |
| Delete Deal Field | `deleteDealField` | Deletes a deal custom field. Admin only. |
| Delete Lead Source | `deleteLeadSource` | Deletes a lead source. Admin only. Contacts referencing it have their lead_source cleared. The last remaining lead source cannot be deleted. |
| Delete Meeting | `deleteMeeting` | Deletes a logged meeting permanently (no undo via the API). Its attachments are removed with it. |
| Delete Note | `deleteNote` | Deletes a note permanently (no undo via the API). Its attachments are removed with it. |
| Delete Predefined Action | `deletePredefinedAction` | Deletes a predefined action template. Actions already created from it on contacts are untouched. If this leaves its group with fewer than two members, the group is dissolved automatically. |
| Delete Predefined Action Group | `deletePredefinedActionGroup` | Deletes a predefined action group. The action templates it contained are kept and become ungrouped. |
| Delete Predefined Item | `deletePredefinedItem` | Deletes a predefined item. Line items already added to deals keep their own copy of the name, cost and price. |
| Delete Predefined Item Group | `deletePredefinedItemGroup` | Deletes a predefined item group. The predefined items it bundled are not deleted — only the grouping is removed. |
| Delete Relationship Type | `deleteRelationshipType` | Deletes a relationship type and every relationship using it, including soft-deleted ones. This cascade is permanent, so check usage before calling it. |
| Delete Status | `deleteStatus` | Deletes a contact status. Admin only. Contacts and companies using it fall back to the lead status. The built-in lead status cannot be deleted. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook subscription. OnePageCRM stops posting events to its target URL. |
| Disable Company Status Sync | `removeCompanySyncedStatus` | Turns off status sync for a company. Contacts keep their current statuses. |
| Enable Company Status Sync | `setCompanySyncedStatus` | Turns on status sync so all contacts in a company share the same status. An initial status_id is required; statuses stay in sync until sync is disabled. |
| Force Close Contact Sales Cycle | `forceCloseContactSalesCycle` | Closes the sales cycle for a contact after first deleting any actions assigned to the contact, with an optional closing comment. |
| Get Account Bootstrap | `getBootstrap` | Returns global account configuration such as lead sources, deal stages, pipelines, custom fields and filters, plus user-specific settings such as date format and time zone. |
| Get Action | `getAction` | Returns one next action, including its status, due date and computed weight (higher means more urgent). |
| Get Action Stream | `getActionStream` | Returns the API user's Action Stream: contacts prioritized by their next action. Supports the same contact filters as List Contacts. |
| Get Attachment Upload Form | `getAttachmentUploadForm` | Returns a pre-authorized S3 upload form for attaching a file to a contact's deal, note, call or meeting. POST the file to the returned URL with every returned field; build key as {contact_id}/{timestamp}/{filename}. |
| Get Call | `getCall` | Returns one logged call — its text, author, result, call time, phone number, the contact it belongs to, and any attachments. |
| Get Company | `getCompany` | Returns one company with its shared details and roll-ups such as contact count and won and pending deal totals. |
| Get Company Field | `getCompanyField` | Returns one company custom field by ID, including its type and, for select_box and multiple_choice fields, the available choices. |
| Get Contact | `getContact` | Returns one contact — names, company link, status, tags, communication lists (phones, emails, urls, addresses) and custom fields. |
| Get Contact Relationship | `getContactRelationship` | Returns one relationship for a contact, naming both parties and the variant label at each end. The path contact must be one of the two parties. |
| Get Custom Field | `getCustomField` | Returns one contact custom field by ID, including its type and, for select_box and multiple_choice fields, the available choices. Anniversary fields also carry reminder_days. |
| Get Deal | `getDeal` | Returns one deal, including its stage, financial fields and any deal items, optionally with stage history. |
| Get Deal Field | `getDealField` | Returns one deal custom field by ID, including its type and, for select_box and multiple_choice fields, the available choices. |
| Get Filter | `getFilter` | Returns all details of a saved filter, along with the contacts that match its criteria. |
| Get Lead Source | `getLeadSource` | Returns one lead source with its contact counts. The path id is the source's system id — the value contacts carry in their lead_source field. Built-in sources use short slugs like advertisement; ones you create get an ObjectId-style id. |
| Get Meeting | `getMeeting` | Returns one meeting — its text, author, meeting time, place, the contact it belongs to, and any attachments. |
| Get Note | `getNote` | Returns one note — its text, author, date, the contact it belongs to, any attachments, and the linked deal if there is one. |
| Get Notification | `getNotification` | Returns one of the API user's notifications by ID. The type field identifies what it is about and read shows whether it has been seen. |
| Get Pipeline | `getPipeline` | Returns one pipeline with its ordered stages. Each stage has a numeric position and a label; a pipeline holds between one and nine stages. |
| Get Predefined Action | `getPredefinedAction` | Returns one predefined action template, including its text, days offset and the action_group_id of the group it belongs to. |
| Get Predefined Action Group | `getPredefinedActionGroup` | Returns one predefined action group, including action_ids — the templates that currently belong to it. |
| Get Predefined Item | `getPredefinedItem` | Returns one predefined item — a reusable product or service with its name, description, cost and price. |
| Get Predefined Item Group | `getPredefinedItemGroup` | Returns one predefined item group with the items it bundles. Its cost and price are the totals of its member items. |
| Get Relationship Type | `getRelationshipType` | Returns one relationship type with its variants. A single variant means the type is symmetrical; two variants mean each end gets a different label. |
| Get Status | `getStatus` | Returns one contact status with its counts. The path id is the status's own ObjectId, not the short system id in the status field. |
| Get Team Stream | `getTeamStream` | Returns the action stream for the entire account in a single list, or for a specific user when user_id is provided. Supports the same contact filters as List Contacts. |
| Get User | `getUser` | Returns one user on your account by ID, including their name, email, photo, role and account rights. bcc_email and google_contacts_email are only included when the ID is your own. |
| Get Webhook | `getWebhook` | Returns one webhook subscription with its name, target URL and secret key. |
| Link Company Contact | `linkCompanyContact` | Links a contact from another company to a company. A contact cannot be linked to the company it already works at, and a company can have at most 100 linked contacts. |
| List Actions | `listActions` | Returns next actions in Action Stream order: ASAP first, then dated actions by due date (overdue first), then waiting-for, then queued actions without a date, then completed. Filter by assignee, contact, company, status and date range. |
| List Call Results | `listCallResults` | Returns the call results configured for the account, with usage counts for the API user and the team. |
| List Calls | `listCalls` | Returns calls logged against your contacts, including the result of each, optionally filtered by contact or company and by date range. |
| List Companies | `listCompanies` | Returns the account's companies sorted by name, filterable by name, phone or first letter. |
| List Company Actions | `listCompanyActions` | Returns next actions across the contacts that belong to a company, with the same paging, sorting and date filters as List Actions. |
| List Company Calls | `listCompanyCalls` | Returns calls logged against the contacts that belong to a company, most recently updated first, with the same paging and date filters as List Calls. |
| List Company Deals | `listCompanyDeals` | Returns deals across the contacts that belong to a company, with the same paging, sorting and filters as List Deals. |
| List Company Fields | `listCompanyFields` | Returns the custom fields defined for companies on your account — id, name, type, position and, for select_box and multiple_choice fields, their choices. |
| List Company Linked Contacts | `listCompanyLinkedContacts` | Returns contacts from other companies that have been linked to a company. Each entry lists which of the company's own contacts it is linked with. |
| List Company Meetings | `listCompanyMeetings` | Returns meetings logged against the contacts that belong to a company, most recently updated first, with the same paging and date filters as List Meetings. |
| List Company Notes | `listCompanyNotes` | Returns notes logged against the contacts that belong to a company, most recently updated first, with the same paging and date filters as List Notes. |
| List Company Pinned Attachments | `listCompanyPinnedAttachments` | Returns attachments pinned to any contact in a company, most recently pinned first. |
| List Contact Actions | `listContactActions` | Returns the next actions on a contact, with the same paging, sorting and date filters as List Actions. |
| List Contact Calls | `listContactCalls` | Returns the calls logged against a contact, most recently updated first, with the same paging and date filters as List Calls. |
| List Contact Deals | `listContactDeals` | Returns the deals on a contact, with the same paging, sorting and filters as List Deals. |
| List Contact Meetings | `listContactMeetings` | Returns the meetings logged against a contact, most recently updated first, with the same paging and date filters as List Meetings. |
| List Contact Notes | `listContactNotes` | Returns the notes logged against a contact, most recently updated first, with the same paging and date filters as List Notes. |
| List Contact Pinned Attachments | `listContactPinnedAttachments` | Returns attachments pinned to a contact, most recently pinned first. |
| List Contact Relationships | `listContactRelationships` | Returns the relationships a contact is part of. Each is a single record naming both contacts with the variant label for each end. Filter by relationship type, other contact, variant or search text. |
| List Contacts | `listContacts` | Returns the contacts you can access, sorted by name. Filter by search text, company, email, phone, tag, status, lead source, owner, starred, actions, pending deals, saved filter and date range. has_actions and has_actions_for_me are mutually exclusive, as are lead_source and lead_source_id. |
| List Contacts Beyond 10000 | `listContactsCascade` | Returns contacts owned by the API user in alphabetical batches of 100, allowing iteration past the 10,000-contact paging limit. Use the last contact ID with List Contacts Beyond 10000 After ID for the next batch. |
| List Contacts Beyond 10000 After ID | `listContactsCascadeAfter` | Returns the next batch of up to 100 contacts after the given contact ID, allowing iteration past the 10,000-contact paging limit. |
| List Contacts By Filter | `listContactsByFilter` | Returns the contacts matching a saved filter, alongside the filter definition. Results come back in Action Stream order, 25 per page. |
| List Countries | `listCountries` | Returns the read-only list of all countries supported by OnePageCRM, sorted by ISO-3166 country code. |
| List Custom Fields | `listCustomFields` | Returns the custom fields defined for contacts on your account — id, name, type, position and, for select_box and multiple_choice fields, their choices. |
| List Deal Fields | `listDealFields` | Returns the custom fields defined for deals on your account — id, name, type, position and, for select_box and multiple_choice fields, their choices. |
| List Deals | `listDeals` | Returns the account's deals, filterable by name, status, stage, pipeline, owner, contact, company, tag and date range. Each deal belongs to one primary contact and moves through a pipeline as pending, then won or lost. |
| List Filters | `listFilters` | Returns the account's saved contact filters, each with its name and the conditions that define it. To get matching contacts, use List Contacts By Filter. |
| List Lead Sources | `listLeadSources` | Returns the account's lead sources with per-user and total contact counts, in alphabetical order. Each id is the source's system id — the value contacts reference in their lead_source field. |
| List Meetings | `listMeetings` | Returns meetings logged against your contacts, optionally filtered by contact or company and by date range. |
| List Notes | `listNotes` | Returns notes logged against your contacts, optionally filtered by contact or company and by date range. A note can also be linked to a deal. |
| List Notifications | `listNotifications` | Returns the API user's in-app notifications (excluding emails and links), such as assigned actions, notes, calls and meetings. |
| List Pipelines | `listPipelines` | Returns the account's deal pipelines, each with its ordered stages. default marks the API user's default pipeline. |
| List Predefined Action Groups | `listPredefinedActionGroups` | Returns the account's predefined action groups. A group bundles two or more predefined action templates so they can all be applied to a contact at once. |
| List Predefined Actions | `listPredefinedActions` | Returns the account's predefined actions — reusable next-action templates, each with the text to apply and a days offset used to calculate the due date. Grouped actions carry their action_group_id. |
| List Predefined Item Groups | `listPredefinedItemGroups` | Returns the account's predefined item groups. A group bundles predefined items under one name; its cost and price are the sums of its members. |
| List Predefined Items | `listPredefinedItems` | Returns the account's predefined items — reusable products or services with a name, description, cost and price that can be added to deals as line items. |
| List Relationship Types | `listRelationshipTypes` | Returns the relationship types defined on your account, each with its variants — the labels used for the two ends of a relationship. One variant means symmetrical (Partner/Partner); two mean directional (Manager/Reports to). |
| List Statuses | `listStatuses` | Returns the account's contact statuses with per-user and total counts, in their configured order. The status field carries the system id (lead, custom1 and so on) that contacts reference. |
| List Users | `listUsers` | Returns every user on your account — name, email, photo, role and account rights. Your own record also includes bcc_email and google_contacts_email. The full team is returned, unpaginated. |
| List Webhooks | `listWebhooks` | Returns the account's webhook subscriptions configured in the Webhooks app — each target URL, name and secret key. |
| Mark Action As Done | `markActionAsDone` | Marks a next action as complete. |
| Mark All Notifications As Read | `markAllNotificationsAsRead` | Marks all of the API user's notifications as read. |
| Mark Notification As Read | `markNotificationAsRead` | Marks one of the API user's notifications as read. |
| Pin Attachment | `pinAttachment` | Pins an attachment so it surfaces on the profile of the contact it belongs to, rather than only on its note, call, meeting or deal. |
| Promote Action | `promoteAction` | Promotes a queued action to be the API user's next action on its contact. Use only when no next action is assigned; otherwise use Swap Action. |
| Regenerate API Key | `changeAuthKey` | Invalidates the current API key and returns a new one. Warning: this logs the user out of all applications, including mobile apps, and breaks any connection still using the old key. |
| Reopen Contact Sales Cycle | `reopenContactSalesCycle` | Reopens a closed sales cycle for a contact, for the calling user. |
| Revert Action Promotion | `revertActionPromotion` | Retained for backwards compatibility: returns the action unmodified. Promotions can no longer be reverted through the API. |
| Save Contact To Google Contacts | `saveContactToGoogleContacts` | Saves a OnePageCRM contact to the user's Google Contacts. OnePageCRM must first be authorized for Google Contacts in the app's Google Contacts integration page. |
| Split Contact | `splitContact` | Removes a contact from its current company and optionally moves it to a new company. Warning: splitting the last contact from a company deletes that company and its data. |
| Star Contact | `starContact` | Stars a contact for the calling user. Starring is per user and does not change how teammates see the contact. |
| Swap Action | `swapAction` | Resolves a date conflict by swapping a dated queued action (queued_with_date) with the current next action (date, date_time or waiting). Both must belong to the API user and the queued action's date must be earlier. |
| Unassign Action | `unassignAction` | Unassigns a next action from its currently assigned user. |
| Unassign Contact Tag | `unassignContactTag` | Removes a tag from a contact. |
| Undo Action Completion | `undoActionCompletion` | Reverts a completed next action to its previous state. |
| Unlink Action | `unlinkAction` | Detaches a next action from the external calendar event it mirrors, making it an ordinary editable action. Nothing is sent to the external provider. |
| Unlink Company Contact | `unlinkCompanyContact` | Unlinks a linked contact from a company. |
| Unpin Attachment | `unpinAttachment` | Unpins an attachment so it no longer surfaces on its contact's profile. The file itself is not deleted. |
| Unstar Contact | `unstarContact` | Removes the calling user's star from a contact. |
| Update Action | `updateAction` | Updates a next action's text, status, due date or assignee, or marks it done. An action cannot be moved to another contact. |
| Update Attachment | `updateAttachment` | Sets or changes an attachment's custom file name. Once set, the custom file name cannot be cleared. |
| Update Call | `updateCall` | Updates a logged call's text, result, time, phone number or recording link. The author stays the original author. |
| Update Company | `updateCompany` | Updates a company's name, description, website, phone, address or company field values. When updating a company field, send its id or name together with the value. |
| Update Company Field | `updateCompanyField` | Updates a company custom field's name, type, position or choices. Admin only. |
| Update Company Logo | `updateCompanyLogo` | Replaces a company's logo with the given Base64-encoded image. The previous logo is removed first. |
| Update Contact | `updateContact` | Updates a contact. Without partial=true the whole record is replaced: omitted writable fields are cleared (tags and communication lists emptied, status reset to lead). Pass partial=true to change only the fields you send; arrays still replace rather than merge. |
| Update Contact Photo | `updateContactPhoto` | Replaces a contact's photo with a Base64-encoded image. The existing photo is removed. Images are cropped to a centered square and resized to 200x200 pixels. |
| Update Contact Relationship | `updateContactRelationship` | Replaces a relationship: send relationship_type_id and both related_contacts entries in full. The type can change and one contact can be swapped, but the path contact must remain a party. |
| Update Custom Field | `updateCustomField` | Updates a contact custom field's name, type, position or choices. Admin only. |
| Update Deal | `updateDeal` | Updates a deal. A deal cannot be moved to another contact. expected_close_date applies to pending deals; close_date is set when the deal becomes won or lost. |
| Update Deal Field | `updateDealField` | Updates a deal custom field's name, type, position or choices. Admin only. |
| Update Lead Source | `updateLeadSource` | Updates a lead source's text (max 40 characters). Admin only. text is required unless partial=true is passed. The list is re-sorted alphabetically afterwards. |
| Update Meeting | `updateMeeting` | Updates a logged meeting's text, place or time. The author stays the original author. |
| Update Note | `updateNote` | Updates a note's text, date or linked deal. The author stays the original author. |
| Update Predefined Action | `updatePredefinedAction` | Updates a predefined action template's text (max 140 characters) or days offset. Group membership is managed through predefined action groups. |
| Update Predefined Action Group | `updatePredefinedActionGroup` | Updates a predefined action group. action_ids is required and replaces the group's membership outright; actions dropped from the list are ungrouped, not deleted. Actions already in another group are rejected. |
| Update Predefined Item | `updatePredefinedItem` | Updates a predefined item. Pass partial=true to leave omitted fields untouched; without it, an omitted description, cost or price is reset to its default. |
| Update Relationship Type | `updateRelationshipType` | Renames a relationship type's variants: send the full set of existing variant IDs with new names. Variants cannot be added or removed. |
| Update Status | `updateStatus` | Updates a contact status. Admin only. text and color are required unless partial=true is passed, and description is cleared if omitted on a non-partial update. |
| Update User | `updateUser` | Updates a user's first name, last name, company name, or regenerates their BCC email address. Each team member can edit their own details; admins can update anyone's. bcc_email can only be regenerated for yourself. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Action Event | `action` | A next action was created, updated, deleted, completed or uncompleted. Check the reason field for the change. |
| Call Event | `call` | A call was created, updated or deleted. Check the reason field for the change. |
| Company Event | `company` | A company was created, updated or deleted. Check the reason field for the change. |
| Contact Event | `contact` | A contact was created, updated, deleted, undeleted or restored. Check the reason field for the change. |
| Deal Event | `deal` | A deal was created, updated, deleted, won, lost, set to pending or had its expected close date changed. Check the reason field for the change. |
| Meeting Event | `meeting` | A meeting was created, updated or deleted. Check the reason field for the change. |
| Note Event | `note` | A note was created, updated or deleted. Check the reason field for the change. |
