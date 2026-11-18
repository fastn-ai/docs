---
description: "Onpipeline is a sales pipeline CRM."
hidden: true
---

# Onpipeline

Onpipeline is a sales pipeline CRM. This connector covers the complete Onpipeline REST API: persons (contacts), organizations, deals (including undelete), calendar events, notes, invoices and invoice lines, users, teams, pipelines and stages, products, last-updated records, inbound leads, custom fields, action menu links, widgets, history log entries, call tracking and recording, and webhooks. Every Onpipeline endpoint is a POST with a JSON body, authenticated with a personal API token sent in the Authorization header.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [onpipeline.com](https://onpipeline.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 38 |
| **Events** | 4 |
| **Slug** | `onpipeline` |

## Use it

Add Onpipeline from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.onpipeline.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Action Menu Link | `createActionMenuLink` | Adds a custom link to the Onpipeline actions menu of persons, organizations or deals. The URL can contain shortcuts such as {ID} that Onpipeline replaces with the record ID. Each zone accepts at most 10 links. |
| Create Custom Field | `createCustomField` | Creates a new text custom field on persons, organizations or deals in Onpipeline. The API can only create text fields. |
| Create Deal | `createDeal` | Creates a new deal in an Onpipeline pipeline stage, owned by a user and optionally linked to a person, involved persons and products. Pipeline and stage IDs come from List Pipelines; owner IDs come from List Users. Onpipeline's DealAdd endpoint rejects any organization ID with "LinkedOrgID: invalid id", whether sent alone or with a person, so link the organization afterwards with Update Deal, which accepts it. Returns the new deal ID. |
| Create History Log Entry | `createHistoryLogEntry` | Adds an entry to the activity history of a person, organization or deal in Onpipeline, for example an order received in an external app. The entry date is set automatically. Log entries cannot be deleted through the API, so use a distinctive app name. |
| Create Lead | `createLead` | Submits a new inbound lead into Onpipeline with contact name, organization, address, emails, phones and custom fields. Lead Source tokens issued to third parties can only call this action. The Onpipeline API has no endpoint to delete leads. |
| Create Note | `createNote` | Adds a note to a person, organization or deal in Onpipeline. The Onpipeline API has no endpoint to delete notes. |
| Create Organization | `createOrganization` | Creates a new organization in Onpipeline. Supply a Postcode if you want Onpipeline to reject duplicates (the duplicate check matches on name and postcode). Returns the new organization ID. |
| Create Person | `createPerson` | Creates a new contact person in Onpipeline, optionally linked to an existing organization and with email addresses, phone numbers and custom field values. Returns the new person ID. |
| Create Webhook | `createWebhook` | Registers a webhook in Onpipeline that POSTs the full record JSON to your HTTPS URL whenever a person, organization, deal or calendar event in the chosen zone changes. The response includes an X-Signature secret for verifying deliveries. In testing Onpipeline answered HTTP 500 with an empty body for some target URLs (for example a URL that returns 404 or one already registered before), so use a reachable, previously unused endpoint. |
| Create Widget | `createWidget` | Adds an embedded frame widget to Onpipeline person, organization or deal pages. Each zone accepts at most 10 widgets. |
| Delete Action Menu Link | `deleteActionMenuLink` | Removes a custom link from the Onpipeline actions menu by link ID. |
| Delete Custom Field | `deleteCustomField` | Deletes a custom field from Onpipeline by field ID, removing its values from all records. |
| Delete Deal | `deleteDeal` | Deletes a deal in Onpipeline by ID. This is a soft delete: the deal stays in the account with status "deleted" (visible through List Deals) and can be restored with Restore Deal. The API offers no permanent delete. |
| Delete Organization | `deleteOrganization` | Permanently deletes an organization in Onpipeline by ID. This cannot be undone. |
| Delete Person | `deletePerson` | Permanently deletes a contact person in Onpipeline by ID. This cannot be undone. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook from Onpipeline by webhook ID. |
| Delete Widget | `deleteWidget` | Removes an embedded frame widget from Onpipeline by widget ID. |
| List Action Menu Links | `listActionMenuLinks` | Lists the custom links added to the Onpipeline actions menu of persons, organizations and deals. |
| List Custom Fields | `listCustomFields` | Lists the custom fields defined for persons, organizations or deals in Onpipeline. The returned IDs are used in the Extra arrays of create, update and list actions. |
| List Deals | `listDeals` | Lists deals in Onpipeline, optionally filtered by deal ID, status, owner, linked person or organization, pipeline name, stage name, product, or closing, creation and next-event date ranges. Pass a DealID to fetch a single deal. |
| List Events | `listEvents` | Lists calendar events (tasks, calls, emails, meetings and deadlines) in Onpipeline, optionally filtered by event ID, owner, name, time, type, linked deal, person or organization, and creation date range. |
| List Invoice Lines | `listInvoiceLines` | Lists the line items of one Onpipeline invoice, with description, unit price, quantity, discount, tax and line total. |
| List Invoices | `listInvoices` | Lists Onpipeline invoice headers issued within an invoice date range, including client, totals, tax, due date and paid amount. Use List Invoice Lines with an invoice ID to get its line items. |
| List Notes | `listNotes` | Lists notes attached to persons, organizations or deals in Onpipeline, optionally filtered by record type, linked record ID and creation date range. |
| List Organizations | `listOrganizations` | Lists organizations in Onpipeline, optionally filtered by ID, name, address fields or creation date range. Pass an OrgID to fetch a single organization. Returns the matching organizations with address, deal counts and custom field values. |
| List Persons | `listPersons` | Lists contact persons in Onpipeline, optionally filtered by person ID, organization ID or name, full name, creation date or next event date. Pass a PersonID to fetch a single person, or an OrgID to list the people of one organization. |
| List Pipelines | `listPipelines` | Lists the sales pipelines of the Onpipeline account with their stages. Pipeline and stage IDs are required to create deals. |
| List Products | `listProducts` | Lists the product names (deal categories) defined in the Onpipeline account, which can be linked to deals. |
| List Recently Updated Records | `listRecentlyUpdatedRecords` | Lists persons, organizations or deals that were updated within the last 3, 6, 12 or 24 hours, for syncing changes to other applications. The records have the same shape as the corresponding list action. |
| List Teams | `listTeams` | Lists the teams of the Onpipeline account with their members and team leaders. |
| List Users | `listUsers` | Lists the users of the Onpipeline account with their status, administrator flag and permissions. User IDs are used as deal and event owners. |
| List Webhooks | `listWebhooks` | Lists the webhooks registered in Onpipeline, with the zone (person, org, deal or event), target URL, creation time and last run time. |
| List Widgets | `listWidgets` | Lists the embedded frame widgets added to Onpipeline person, organization and deal pages. |
| Record Call | `recordCall` | Logs an inbound or outbound phone call in Onpipeline, optionally with the base64-encoded MP3 recording (up to 70 MB) and a comment. The phone numbers are matched by digits to attach the call to the right person, organization and deal; unrecognized numbers are rejected with error 406. |
| Restore Deal | `restoreDeal` | Restores a previously deleted Onpipeline deal by ID and sets its status back to open. |
| Update Deal | `updateDeal` | Updates an existing Onpipeline deal, including its name, status (open, won or lost), value, probability, stage, owner, linked records, expected closing date, products and custom fields. Send only the fields you are changing: re-sending unchanged values is rejected with error 406. |
| Update Organization | `updateOrganization` | Updates an existing organization in Onpipeline. Send only the fields you are changing: Onpipeline rejects a request that re-sends unchanged values with error 406. |
| Update Person | `updatePerson` | Updates an existing contact person in Onpipeline. Send only the fields you are changing: Onpipeline rejects a request that re-sends unchanged values with error 406. Email, Phone and Extra replace the corresponding lists. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Calendar Event Changed | `event` | Fires when a calendar event (task, call, email, meeting or deadline) is created or updated in Onpipeline (Zone=event). The POST body is the event object as returned by List Events. No event-type field is sent. Payload modelled from the documented object; not yet captured from a live delivery. |
| Deal Changed | `deal` | Fires when a deal is created, updated or deleted in Onpipeline. Onpipeline registers one webhook per zone (Zone=deal) and POSTs the deal object exactly as returned by List Deals. The payload carries no event-type field, so routing relies on the per-zone subscription. Payload shape modelled from the documented List Deals object; not yet captured from a live delivery. |
| Organization Changed | `org` | Fires when an organization is created, updated or deleted in Onpipeline (Zone=org). The POST body is the organization object as returned by List Organizations. No event-type field is sent. Payload modelled from the documented object; not yet captured from a live delivery. |
| Person Changed | `person` | Fires when a contact person is created, updated or deleted in Onpipeline (Zone=person). The POST body is the person object as returned by List Persons. No event-type field is sent. Payload modelled from the documented object; not yet captured from a live delivery. |
