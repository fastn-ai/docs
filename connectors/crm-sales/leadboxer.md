---
description: "LeadBoxer is a B2B lead identification and behavioural analytics platform."
hidden: true
---

# LeadBoxer

<img src="../../.gitbook/assets/connectors/lg/leadboxer.png" alt="LeadBoxer logo">

LeadBoxer is a B2B lead identification and behavioural analytics platform. This connector wraps the LeadBoxer Platform API: leads, sessions and events, lead tags and assignment, lead exclusions, IP and domain company lookup, credit grants, datasets and form tracking, users and dataset access, segments, custom tracking domains and onboarding signup, plus the Track API for server-side events and email-open tracking. Authenticates with an account API key sent in the x-api-key header.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [leadboxer.com](https://leadboxer.com) |
| **Authentication** | API key |
| **Slug** | `leadboxer` |

## Use it

Add LeadBoxer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.leadboxer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Custom Tracking Domain | `addCustomTrackingDomain` | Adds a custom tracking domain to a dataset and starts certificate generation, which can take several minutes. The response reports success, an error, or required DNS configuration. |
| Add User To Dataset | `addUserToDataset` | Grants a LeadBoxer user access to a dataset. |
| Assign Lead | `assignLead` | Assigns a lead in a dataset to a LeadBoxer user by user ID. |
| Create Dataset | `createDataset` | Creates a new dataset (tracked website) in the account and associates it with the given users. |
| Create Or Associate User | `createOrAssociateUser` | Creates a new LeadBoxer user, or associates an existing user, with an account and datasets. Optionally sends the user an invitation email. |
| Create Segment | `createSegment` | Creates a segment (saved lead filter) for an account and dataset, with optional text, number, time, field, exit-link, lead score and display filters and email notification preferences. |
| Delete Custom Tracking Domain | `deleteCustomTrackingDomain` | Deletes a custom tracking domain entry from a dataset. |
| Delete Dataset | `deleteDataset` | Deletes a dataset from the account. |
| Delete Segment | `deleteSegment` | Deletes a segment by ID. |
| Delete User | `deleteUser` | Removes a user from the LeadBoxer account and revokes their access to all associated datasets. |
| Export Leads CSV | `exportLeadsCsv` | Exports a filtered list of leads for a dataset as CSV text, with the same filters as List Leads plus separator, date format and columns. Anonymous leads have no default columns, so pass additionalCsvFields (for example use_id,lastEvent) to guarantee rows. |
| Get Credit Grants | `getCreditGrants` | Retrieves the credit grants for the LeadBoxer account: credits granted, used and available per grant, with source and validity dates. |
| Get Lead | `getLead` | Retrieves the full detail record of a single lead in a dataset by lead ID. |
| Hide Leads | `hideLeads` | Adds a lead exclusion rule to a dataset so matching leads are hidden, by lead ID, organization name, organization domain or most likely company. |
| List Account User Datasets | `listAccountUserDatasets` | Retrieves every user-to-dataset association in a LeadBoxer account, with user, team and dataset details. |
| List Custom Tracking Domains | `listCustomTrackingDomains` | Retrieves all custom tracking domains configured for a dataset. |
| List Lead Exclusions | `listLeadExclusions` | Retrieves the lead exclusion (hide) rules of a dataset, optionally filtered by rule type. |
| List Lead Sessions | `listLeadSessions` | Retrieves the sessions of a lead in a dataset, optionally filtered by segment and minimum session duration, with token paging. |
| List Leads | `listLeads` | Retrieves leads for a dataset as JSON with search, time, text, number, field, exit-link, lead score and display filters, sorting and token paging. |
| List My Datasets | `listMyDatasets` | Retrieves the datasets the given LeadBoxer user has access to, with name and time zone. |
| List Segments | `listSegments` | Retrieves the segments (saved lead filters) of a dataset for a LeadBoxer user, including filters and notification settings. |
| List Session Events | `listSessionEvents` | Retrieves the events recorded in a lead session, optionally filtered by segment. |
| Lookup Domain | `lookupDomain` | Retrieves firmographic organization details for a company domain: name, type, industry, employee range, address, social links and specialties. Consumes lookup credits. |
| Lookup IP Address | `lookupIpAddress` | Retrieves organization, geolocation, ISP and IP range details for an IPv4 or IPv6 address. Consumes lookup credits. |
| Process User Signup | `processUserSignup` | Registers a new LeadBoxer user and account with a trial, returning the account ID, user ID, dataset ID and trial end date. |
| Remove User From Dataset | `removeUserFromDataset` | Revokes a LeadBoxer user's access to a dataset. |
| Rename Dataset | `renameDataset` | Updates the human-readable name of a dataset. |
| Resend User Invitation | `resendUserInvitation` | Resends the invitation email to a LeadBoxer user. |
| Track Email Open | `trackEmailOpen` | Records an email open event for a recipient in a dataset through the LeadBoxer email tracking pixel endpoint. Returns a 1x1 transparent pixel. |
| Track Event | `trackEvent` | Sends a server-side event to the LeadBoxer Track API for a dataset. Events attach to a user and session (generated when not supplied). Set json to true to receive the event id as JSON instead of a tracking pixel. |
| Unhide Leads | `unhideLeads` | Deletes a lead exclusion rule from a dataset so matching leads are shown again. |
| Update Custom Tracking Domain | `updateCustomTrackingDomain` | Updates the description of an existing custom tracking domain entry for a dataset. |
| Update Form Tracking | `updateFormTracking` | Updates the form tracking configuration of a dataset: form tracking on or off, IP masking, and the form input attribute used to capture fields. |
| Update Lead Tags | `updateLeadTags` | Sets the tags of a lead in a dataset. The leadTags value replaces the lead's tag list; send an empty string to remove all tags. |
| Update Segment | `updateSegment` | Updates an existing segment's name, visibility, filter criteria and email notification preferences. |
| Update Segment User | `updateSegmentUser` | Changes the user associated with a segment, giving that user access to it. |
| Update User Name | `updateUserName` | Updates the first and last name of an existing LeadBoxer user. |
| Validate Custom Tracking Domain | `validateCustomTrackingDomain` | Validates a custom tracking domain for a dataset and returns DNS configuration suggestions. responseCode 0 means valid; messageType ERROR or WARNING describes problems. |
