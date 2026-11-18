---
description: "Zendesk Support customer service and ticketing platform."
hidden: true
---

# Zendesk Support

<img src="../../.gitbook/assets/connectors/lg/zendesk-support.png" alt="Zendesk Support logo">

Zendesk Support customer service and ticketing platform. Manage tickets and comments, users and identities, organizations and memberships, groups, ticket fields and forms, macros, views, triggers, automations, SLA policies, satisfaction ratings, requests, brands, tags, ticket audits and metrics, search, file uploads, and webhooks. Base URL is https://{subdomain}.zendesk.com/api/v2.

| | |
| --- | --- |
| **Category** | [IT and service management](README.md) |
| **Website** | [zendesk.com](https://zendesk.com) |
| **Authentication** | Basic auth, OAuth 2.0 |
| **Slug** | `zendeskSupport` |

## Use it

Add Zendesk Support from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zendeskSupport.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Ticket Tags | `addTicketTags` | Adds one or more tags to a ticket without removing existing tags. |
| Apply Macro To Ticket | `applyMacroToTicket` | Returns the changes a macro would make to a specific ticket without saving them. |
| Autocomplete Organizations | `autocompleteOrganizations` | Returns organizations whose name starts with the provided value. |
| Autocomplete Tags | `autocompleteTags` | Returns tags that start with the provided value. |
| Autocomplete Users | `autocompleteUsers` | Returns an abbreviated list of users whose name starts with the provided value. |
| Count Search Results | `countSearchResults` | Returns the number of results a search query would match, without returning the records. |
| Count View Tickets | `countViewTickets` | Returns the number of tickets that match a view. |
| Create Automation | `createAutomation` | Creates a new time-based automation that runs actions when its conditions are met. |
| Create Brand | `createBrand` | Creates a new brand with a name and help center subdomain. |
| Create Group | `createGroup` | Creates a new agent group with the provided name. |
| Create Group Membership | `createGroupMembership` | Adds an agent to a group by creating a group membership. |
| Create Macro | `createMacro` | Creates a new macro with a title and a set of actions to apply to tickets. |
| Create Many Tickets | `createManyTickets` | Creates up to 100 tickets in a single asynchronous job and returns a job status object. |
| Create Many Users | `createManyUsers` | Creates up to 100 users in a single asynchronous job and returns a job status object. |
| Create Or Update Organization | `createOrUpdateOrganization` | Creates an organization, or updates the existing one if a match is found on name or external ID. |
| Create Or Update User | `createOrUpdateUser` | Creates a user, or updates the existing user if one matches on email or external ID. |
| Create Organization | `createOrganization` | Creates a new organization. The organization must have a unique name. |
| Create Organization Membership | `createOrganizationMembership` | Adds a user to an organization by creating an organization membership. |
| Create Request | `createRequest` | Creates a new request (a ticket submitted on behalf of an end user). |
| Create Satisfaction Rating | `createSatisfactionRating` | Creates a satisfaction rating on a solved ticket on behalf of the end user. |
| Create SLA Policy | `createSlaPolicy` | Creates a new SLA policy defining target response and resolution times. |
| Create Target | `createTarget` | Creates a new external target that Zendesk can notify when triggers fire. |
| Create Ticket | `createTicket` | Creates a new ticket in Zendesk Support. The ticket must include an initial comment. |
| Create Ticket Field | `createTicketField` | Creates a new custom ticket field of the specified type. |
| Create Ticket Form | `createTicketForm` | Creates a new ticket form containing a set of ticket fields. |
| Create Trigger | `createTrigger` | Creates a new ticket trigger that runs actions when its conditions are met. |
| Create User | `createUser` | Creates a new user. The user must have a name; agents and admins also require an email. |
| Create User Identity | `createUserIdentity` | Adds a new identity, such as an email address or phone number, to a user. |
| Create View | `createView` | Creates a new view with the specified conditions. |
| Create Webhook | `createWebhook` | Creates a webhook that delivers event notifications to an external endpoint. Used to subscribe to Zendesk events. |
| Delete Automation | `deleteAutomation` | Deletes an automation by its ID. |
| Delete Brand | `deleteBrand` | Deletes a brand by its ID. |
| Delete Group | `deleteGroup` | Deletes an agent group by its ID. |
| Delete Group Membership | `deleteGroupMembership` | Removes an agent from a group by deleting the membership. |
| Delete Macro | `deleteMacro` | Deletes a macro by its ID. |
| Delete Organization | `deleteOrganization` | Permanently deletes an organization by its ID. |
| Delete Organization Membership | `deleteOrganizationMembership` | Removes a user from an organization by deleting the membership. |
| Delete SLA Policy | `deleteSlaPolicy` | Deletes an SLA policy by its ID. |
| Delete Target | `deleteTarget` | Deletes a target by its ID. |
| Delete Ticket | `deleteTicket` | Permanently deletes a ticket by its ID. |
| Delete Ticket Field | `deleteTicketField` | Deletes a ticket field by its ID. |
| Delete Ticket Form | `deleteTicketForm` | Deletes a ticket form by its ID. |
| Delete Trigger | `deleteTrigger` | Deletes a ticket trigger by its ID. |
| Delete Upload | `deleteUpload` | Deletes a previously uploaded file using its upload token. |
| Delete User | `deleteUser` | Soft-deletes a user by their ID. Deleted users are permanently removed after a retention period. |
| Delete User Identity | `deleteUserIdentity` | Removes an identity from a user. |
| Delete View | `deleteView` | Deletes a view by its ID. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook by its ID, stopping event delivery to its endpoint. |
| Execute View | `executeView` | Runs a view and returns the matching tickets with the view's configured columns. |
| Export Search Results | `exportSearchResults` | Runs a search using cursor-based export pagination, suitable for retrieving large result sets of a single record type. |
| Get Help Center Article | `getHelpCenterArticle` | Retrieves a single Help Center (Guide) article by its ID. Used by the real-time event handler to fetch full article content after a webhook fires (Zendesk article webhooks carry only the id, not the body). |
| Import Ticket | `importTicket` | Imports a historical ticket, bypassing triggers and automations, with full control over timestamps and comments. |
| List All Ticket Audits | `listAllTicketAudits` | Retrieves audits across all tickets in the account, ordered by creation time. |
| List Assignable Groups | `listAssignableGroups` | Retrieves the groups that tickets can be assigned to. |
| List Automations | `listAutomations` | Retrieves the time-based automations configured in the account. |
| List Brands | `listBrands` | Retrieves the brands configured in the account. |
| List Custom Roles | `listCustomRoles` | Retrieves the custom agent roles configured in the account. |
| List Group Memberships | `listGroupMemberships` | Retrieves the memberships that associate agents with groups. |
| List Groups | `listGroups` | Retrieves a paginated list of agent groups in the account. |
| List Help Center Articles | `listHelpCenterArticles` | Lists all Help Center (Guide) knowledge base articles across the account, with cursor pagination and sorting. Distinct from the ticketing API. |
| List Macros | `listMacros` | Retrieves the macros available to agents in the account. |
| List Organization Memberships | `listOrganizationMemberships` | Retrieves the memberships that associate users with organizations. |
| List Organization Related Information | `showOrganizationRelated` | Retrieves counts of tickets and users related to an organization. |
| List Organization Users | `listOrganizationUsers` | Retrieves the users that belong to a specific organization. |
| List Organizations | `listOrganizations` | Retrieves a paginated list of organizations in the account. |
| List Request Comments | `listRequestComments` | Retrieves the public comments on a request. |
| List Requests | `listRequests` | Retrieves the requests (end-user view of tickets) submitted through the account. |
| List Satisfaction Ratings | `listSatisfactionRatings` | Retrieves customer satisfaction ratings left on solved tickets. |
| List SLA Policies | `listSlaPolicies` | Retrieves the service level agreement (SLA) policies configured in the account. |
| List Suspended Tickets | `listSuspendedTickets` | Retrieves tickets that were suspended (for example flagged as spam) rather than created. |
| List Tags | `listTags` | Retrieves the most-used tags across the account with their usage counts. |
| List Targets | `listTargets` | Retrieves the external targets (HTTP and email notification endpoints) configured in the account. |
| List Ticket Audits | `listTicketAudits` | Retrieves the audit trail of all changes made to a specific ticket. |
| List Ticket Comments | `listTicketComments` | Retrieves all comments (public and private) on a specific ticket. |
| List Ticket Fields | `listTicketFields` | Retrieves all ticket fields, including system and custom fields, in the account. |
| List Ticket Forms | `listTicketForms` | Retrieves all ticket forms configured in the account. |
| List Ticket Metrics | `listTicketMetrics` | Retrieves metric records (reply times, resolution times, and more) across all tickets. |
| List Ticket Tags | `listTicketTags` | Retrieves the tags currently applied to a specific ticket. |
| List Tickets | `listTickets` | Retrieves a paginated list of tickets in the Zendesk Support account. |
| List Tickets From View | `listTicketsFromView` | Retrieves the tickets that match a view as full ticket objects. |
| List Triggers | `listTriggers` | Retrieves the ticket triggers configured in the account. |
| List User Group Memberships | `listUserGroupMemberships` | Retrieves the group memberships for a specific agent. |
| List User Identities | `listUserIdentities` | Retrieves the identities (email addresses, phone numbers, and more) associated with a user. |
| List User Organization Memberships | `listUserOrganizationMemberships` | Retrieves the organization memberships for a specific user. |
| List User Related Information | `showUserRelated` | Retrieves counts of tickets, entries, and other records related to a user. |
| List Users | `listUsers` | Retrieves a paginated list of users (agents, admins, and end users) in the account. |
| List Views | `listViews` | Retrieves the views (saved ticket filters) in the account. |
| List Webhooks | `listWebhooks` | Retrieves the webhooks configured in the account. Webhooks deliver event notifications to external URLs. |
| Make User Identity Primary | `makeUserIdentityPrimary` | Sets one of a user's identities as the primary identity. |
| Merge Tickets Into Target | `mergeTickets` | Merges one or more source tickets into a target ticket, closing the source tickets. |
| Merge User Into Target | `mergeUser` | Merges an end user into another end user, moving tickets and identities to the target. |
| Redact Comment Attachment | `redactCommentAttachment` | Permanently redacts an attachment from a ticket comment. |
| Remove Ticket Tags | `removeTicketTags` | Removes the specified tags from a ticket. |
| Search | `search` | Runs a unified search across tickets, users, organizations, and groups using Zendesk search syntax. |
| Search Organizations | `searchOrganizations` | Finds organizations by their external ID. |
| Search Users | `searchUsers` | Searches for users by name, email, phone, external ID, or custom fields. |
| Set Ticket Tags | `setTicketTags` | Replaces all tags on a ticket with the provided set of tags. |
| Show Attachment | `showAttachment` | Retrieves the metadata of a single attachment by its ID. |
| Show Automation | `showAutomation` | Retrieves the details of a single automation by its ID. |
| Show Brand | `showBrand` | Retrieves the details of a single brand by its ID. |
| Show Current User | `showCurrentUser` | Retrieves the user record for the currently authenticated account. |
| Show Custom Role | `showCustomRole` | Retrieves the details and permissions of a single custom role by its ID. |
| Show Group | `showGroup` | Retrieves the details of a single agent group by its ID. |
| Show Group Membership | `showGroupMembership` | Retrieves a single group membership by its ID. |
| Show Macro | `showMacro` | Retrieves the details of a single macro by its ID. |
| Show Macro Replica | `showMacroReplica` | Returns the ticket changes a macro would make, without applying them to a specific ticket. |
| Show Many Organizations | `showManyOrganizations` | Retrieves multiple organizations in a single request by their IDs or external IDs. |
| Show Many Users | `showManyUsers` | Retrieves multiple users in a single request by their IDs or external IDs. |
| Show Multiple Tickets | `showManyTickets` | Retrieves multiple tickets in a single request by their IDs. |
| Show Organization | `showOrganization` | Retrieves the details of a single organization by its ID. |
| Show Organization Membership | `showOrganizationMembership` | Retrieves a single organization membership by its ID. |
| Show Request | `showRequest` | Retrieves the details of a single request by its ID. |
| Show Satisfaction Rating | `showSatisfactionRating` | Retrieves a single satisfaction rating by its ID. |
| Show SLA Policy | `showSlaPolicy` | Retrieves the details of a single SLA policy by its ID. |
| Show Target | `showTarget` | Retrieves the details of a single target by its ID. |
| Show Ticket | `showTicket` | Retrieves the details of a single ticket by its ID. |
| Show Ticket Audit | `showTicketAudit` | Retrieves a single audit for a specific ticket. |
| Show Ticket Field | `showTicketField` | Retrieves the details of a single ticket field by its ID. |
| Show Ticket Form | `showTicketForm` | Retrieves the details of a single ticket form by its ID. |
| Show Ticket Metric | `showTicketMetric` | Retrieves the metric record for a single ticket metric by its ID. |
| Show Trigger | `showTrigger` | Retrieves the details of a single ticket trigger by its ID. |
| Show User | `showUser` | Retrieves the details of a single user by their ID. |
| Show User Identity | `showUserIdentity` | Retrieves a single identity belonging to a user. |
| Show View | `showView` | Retrieves the details of a single view by its ID. |
| Show Webhook | `showWebhook` | Retrieves the details of a single webhook by its ID. |
| Update Automation | `updateAutomation` | Updates an existing automation. |
| Update Brand | `updateBrand` | Updates an existing brand. |
| Update Group | `updateGroup` | Updates an existing agent group. |
| Update Macro | `updateMacro` | Updates an existing macro. |
| Update Many Tickets | `updateManyTickets` | Updates a batch of tickets by ID in a single asynchronous job. Provide the ticket IDs and the shared field values to apply. |
| Update Organization | `updateOrganization` | Updates an existing organization. Only the fields provided in the organization object are changed. |
| Update Request | `updateRequest` | Adds a comment to an existing request or solves it on behalf of the end user. |
| Update SLA Policy | `updateSlaPolicy` | Updates an existing SLA policy. |
| Update Target | `updateTarget` | Updates an existing target. |
| Update Ticket | `updateTicket` | Updates an existing ticket. Only the fields provided in the ticket object are changed. |
| Update Ticket Field | `updateTicketField` | Updates an existing ticket field. |
| Update Ticket Form | `updateTicketForm` | Updates an existing ticket form. |
| Update Trigger | `updateTrigger` | Updates an existing ticket trigger. |
| Update User | `updateUser` | Updates an existing user. Only the fields provided in the user object are changed. |
| Update User Identity | `updateUserIdentity` | Updates the value or verification status of a user's identity. |
| Update View | `updateView` | Updates an existing view. |
| Update Webhook | `updateWebhook` | Updates the configuration of an existing webhook. |
| Upload File | `uploadFile` | Uploads a file and returns an upload token that can be attached to a ticket comment. Provide the raw file content and a file name. |
