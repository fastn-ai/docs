---
description: "Intercom customer messaging and support platform."
hidden: true
---

# Intercom

Intercom customer messaging and support platform. Manage contacts, companies, conversations, messages, admins, tags, segments, notes, data events, articles, tickets, and data attributes via the Intercom REST API (api.intercom.io, Intercom-Version 2.15).

| | |
| --- | --- |
| **Category** | [IT and service management](README.md) |
| **Website** | [intercom.com](https://intercom.com) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Actions** | 82 |
| **Events** | 44 |
| **Slug** | `intercom` |

## Use it

Add Intercom from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.intercom.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Contact | `archiveContact` | Archive a contact by id. |
| Assign Conversation | `assignConversation` | Assign a conversation to an admin and/or team via the parts endpoint. |
| Attach Contact to Company | `attachContactToCompany` | Attach a contact to a company. |
| Attach Contact to Conversation | `attachContactToConversation` | Add a contact participant to a conversation. |
| Close Conversation | `closeConversation` | Close a conversation via the parts endpoint. |
| Convert Conversation to Ticket | `convertConversationToTicket` | Convert a conversation into a ticket of a given ticket type. |
| Create Article | `createArticle` | Create a help center article. |
| Create Contact | `createContact` | Create a new contact (user or lead) in Intercom. |
| Create Conversation | `createConversation` | Create a conversation initiated by a contact. |
| Create Data Attribute | `createDataAttribute` | Create a custom data attribute. |
| Create Help Center Collection | `createCollection` | Create a help center collection. |
| Create Message | `createMessage` | Send an outbound in-app or email message from an admin to a contact. |
| Create Note | `createNote` | Create a note on a contact. |
| Create or Update Company | `createOrUpdateCompany` | Create a company, or update it if company_id already exists. |
| Create or Update Tag | `createTag` | Create a new tag or update an existing one by passing its id. |
| Create Ticket | `createTicket` | Create a ticket. |
| Create Ticket Type | `createTicketType` | Create a new ticket type. |
| Delete Article | `deleteArticle` | Delete an article by id. |
| Delete Company | `deleteCompany` | Delete a company by id. |
| Delete Contact | `deleteContact` | Permanently delete a contact by id. |
| Delete Conversation | `deleteConversation` | Permanently delete a conversation by id. |
| Delete Help Center Collection | `deleteCollection` | Delete a help center collection by id. |
| Delete Tag | `deleteTag` | Delete a tag by id. |
| Find Contact by External ID | `findContactByExternalId` | Retrieve a contact by its external_id. |
| Get Admin | `getAdmin` | Retrieve a single admin by id. |
| Get Article | `getArticle` | Retrieve an article by id. |
| Get Company | `getCompany` | Retrieve a company by Intercom company id. |
| Get Contact | `getContact` | Retrieve a single contact by Intercom contact id. |
| Get Conversation | `getConversation` | Retrieve a single conversation by id. |
| Get Help Center Collection | `getCollection` | Retrieve a help center collection by id. |
| Get Note | `getNote` | Retrieve a single note by id. |
| Get Segment | `getSegment` | Retrieve a single segment by id. |
| Get Team | `getTeam` | Retrieve a single team by id. |
| Get Ticket | `getTicket` | Retrieve a ticket by id. |
| Get Ticket Type | `getTicketType` | Retrieve a single ticket type by id. |
| Identify Admin (Me) | `getMe` | Identify the admin/workspace that owns the current access token. |
| List Admin Activity Logs | `listActivityLogs` | List admin activity logs within a date range (created_at_after required, unix timestamp). |
| List Admins | `listAdmins` | List all admins in the workspace. |
| List Articles | `listArticles` | List all help center articles with pagination. |
| List Attached Contacts | `listAttachedContacts` | List contacts attached to a company. |
| List Away Status Reasons | `listAwayStatusReasons` | List all away status reasons for the workspace. |
| List Companies | `listCompanies` | List companies with pagination. |
| List Company Contacts | `listCompanyContacts` | List contacts attached to a company. |
| List Company Segments | `listCompanySegments` | List segments associated with a company. |
| List Contact Companies | `listContactCompanies` | List companies attached to a contact. |
| List Contact Segments | `listContactSegments` | List segments a contact belongs to. |
| List Contact Subscriptions | `listContactSubscriptions` | List subscription types a contact is opted into. |
| List Contact Tags | `listContactTags` | List tags attached to a contact. |
| List Contacts | `listContacts` | List all contacts with cursor pagination. |
| List Conversations | `listConversations` | Search conversations. Intercom's GET /conversations list is plan-restricted on some workspaces; this uses the always-available search endpoint. Pass an Intercom search query AST and optional pagination. |
| List Data Attributes | `listDataAttributes` | List data attributes for contacts/companies/conversations. |
| List Data Events | `listEvents` | List data events for a contact. |
| List Help Center Collections | `listCollections` | List all help center collections. |
| List News Items | `listNewsItems` | List all news items. |
| List Newsfeeds | `listNewsfeeds` | List all newsfeeds. |
| List Notes | `listNotes` | List notes for a contact. |
| List Segments | `listSegments` | List all contact/company segments. |
| List Subscription Types | `listSubscriptionTypes` | List all subscription types in the workspace. |
| List Tags | `listTags` | List all tags in the workspace. |
| List Teams | `listTeams` | List all teams in the workspace. |
| List Ticket Types | `listTicketTypes` | List all ticket types for the workspace. |
| List Webhook Subscriptions | `listWebhookSubscriptions` | List webhook subscriptions for the app. Note: topic subscriptions are primarily managed in the Developer Hub; this read endpoint surfaces current subscriptions where supported. |
| Merge Contacts | `mergeContacts` | Merge a lead into a user contact. |
| Open Conversation | `openConversation` | Open (reopen) a snoozed or closed conversation. |
| Reply to Conversation | `replyConversation` | Reply to a conversation as an admin or as a contact/user. |
| Search Articles | `searchArticles` | Search help center articles by phrase or state. |
| Search Contacts | `searchContacts` | Search contacts using a query object with operators and cursor pagination. |
| Search Conversations | `searchConversations` | Search conversations using a query object with cursor pagination (per_page and the starting_after cursor from pages.next). |
| Set Admin Away | `setAdminAway` | Set an admin to away mode. |
| Snooze Conversation | `snoozeConversation` | Snooze a conversation until a future unix timestamp. |
| Submit Data Event | `submitEvent` | Submit a data event for a contact (returns 202 with empty body). |
| Tag Contact | `tagContact` | Add a tag to a contact. |
| Tag Conversation | `tagConversation` | Add a tag to a conversation. |
| Unarchive Contact | `unarchiveContact` | Unarchive a previously archived contact. |
| Untag Contact | `untagContact` | Remove a tag from a contact. |
| Untag Conversation | `untagConversation` | Remove a tag from a conversation. |
| Update Article | `updateArticle` | Update an existing article. |
| Update Contact | `updateContact` | Update an existing contact by id. |
| Update Data Attribute | `updateDataAttribute` | Update a custom data attribute by id. |
| Update Help Center Collection | `updateCollection` | Update a help center collection by id. |
| Update Ticket | `updateTicket` | Update a ticket (state, attributes, assignment). |
| Update Ticket Type | `updateTicketType` | Update an existing ticket type. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Admin Added to Workspace | `admin.added_to_workspace` | An admin was added to the workspace. |
| Admin Away Mode Updated | `admin.away_mode_updated` | An admin's away status changed. |
| Admin Created Conversation | `conversation.admin.single.created` | An admin started a new outbound conversation. |
| Admin Replied to Conversation | `conversation.admin.replied` | An admin replied to a conversation. |
| Article Created | `article.created` | A help center article was created. |
| Article Deleted | `article.deleted` | A help center article was deleted. |
| Article Published | `article.published` | A help center article was published. |
| Article Updated | `article.updated` | A help center article was updated. |
| Company Created | `company.created` | A company was created. |
| Company Deleted | `company.deleted` | A company was deleted. |
| Company Updated | `company.updated` | A company was updated. |
| Contact Archived | `contact.archived` | A contact was archived. |
| Contact Attached to Company | `company.contact.attached` | A contact was attached to a company. |
| Contact Attached to Conversation | `conversation.contact.attached` | A contact was added as a participant to a conversation. |
| Contact Deleted | `contact.deleted` | A contact was permanently deleted. |
| Contact Detached from Company | `company.contact.detached` | A contact was detached from a company. |
| Contact Detached from Conversation | `conversation.contact.detached` | A contact was removed from a conversation. |
| Contact Email Updated | `contact.email.updated` | A contact's email address changed. |
| Contact Subscribed | `contact.subscribed` | A contact subscribed to a subscription type. |
| Contact Unarchived | `contact.unarchive` | A contact was unarchived. |
| Contact Unsubscribed | `contact.unsubscribed` | A contact unsubscribed from a subscription type. |
| Contacts Merged | `contact.merged` | A lead was merged into a user contact. |
| Conversation Assigned | `conversation.admin.assigned` | A conversation was assigned to an admin or team. |
| Conversation Closed | `conversation.admin.closed` | An admin closed a conversation. |
| Conversation Created by User | `conversation.user.created` | A user or lead started a new conversation. |
| Conversation Opened | `conversation.admin.opened` | An admin reopened a conversation. |
| Conversation Rating Added | `conversation.rating.added` | A user rated a conversation. |
| Conversation Snoozed | `conversation.admin.snoozed` | An admin snoozed a conversation. |
| Conversation Tagged | `conversation_part.tag.created` | A tag was added to a conversation part. |
| Conversation Unsnoozed | `conversation.admin.unsnoozed` | A snoozed conversation reopened. |
| Lead Added Email | `contact.lead.added_email` | An email was added to a lead. |
| Lead Contact Created | `contact.lead.created` | A new lead-type contact was created. |
| Lead Contact Updated | `contact.lead.updated` | A lead-type contact was updated. |
| Lead Signed Up | `contact.lead.signed_up` | A lead converted/signed up as a user. |
| Lead Tagged | `contact.lead.tag.created` | A tag was added to a lead contact. |
| Note Added to Conversation | `conversation.admin.noted` | An admin added a note to a conversation. |
| Ticket Assigned | `ticket.admin.assigned` | A ticket was assigned to an admin or team. |
| Ticket Created | `ticket.created` | A ticket was created. |
| Ticket State Updated | `ticket.state.updated` | A ticket's state changed. |
| User Contact Created | `contact.user.created` | A new user-type contact was created. |
| User Contact Updated | `contact.user.updated` | A user-type contact was updated. |
| User Replied to Conversation | `conversation.user.replied` | A user or lead replied to a conversation. |
| User Tagged | `contact.user.tag.created` | A tag was added to a user contact. |
| User Untagged | `contact.user.tag.deleted` | A tag was removed from a user contact. |
