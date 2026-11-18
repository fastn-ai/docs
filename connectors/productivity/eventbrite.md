---
description: "Eventbrite events platform connector for the Eventbrite API v3."
hidden: true
---

# Eventbrite

<img src="../../.gitbook/assets/connectors/eventbrite.png" alt="Eventbrite logo" width="64">

Eventbrite events platform connector for the Eventbrite API v3. Manage events, ticket classes, venues, organizers, orders, attendees, discounts, media, webhooks, and reference data (categories, formats, timezones).

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [eventbrite.com](https://eventbrite.com) |
| **Authentication** | Bearer token |
| **Slug** | `eventbrite` |

## Use it

Add Eventbrite from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.eventbrite.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Event | `cancelEvent` | Cancel an Eventbrite event. Cancelling refunds is not automatic; the event stays visible with a cancelled status. |
| Copy Event | `copyEvent` | Create a new draft event by copying an existing Eventbrite event, optionally overriding the name and dates. |
| Create Discount | `createDiscount` | Create a discount code for an Eventbrite event or ticket group. Provide either a percentage or a fixed amount off. Percent values are strings like '25.00'; amount values are in the form 'CURRENCY,cents'. |
| Create Event | `createEvent` | Create a new event under an Eventbrite organization. The event is created as a draft; add ticket classes and publish it separately. Times must be ISO 8601 UTC (e.g. 2026-09-01T18:00:00Z) with a matching IANA timezone. |
| Create Organizer | `createOrganizer` | Create a new organizer profile under an Eventbrite organization. Organizers present events to attendees. |
| Create Ticket Class | `createTicketClass` | Create a new ticket class (ticket type) for an Eventbrite event. Set free=true for a free ticket, or provide cost in the form 'CURRENCY,cents' (e.g. USD,1000 for $10.00). |
| Create Venue | `createVenue` | Create a new venue under an Eventbrite organization. Venues can then be attached to events. |
| Create Webhook | `createWebhook` | Register a webhook for an Eventbrite organization so your endpoint is notified when the selected events occur. 'actions' is a comma-separated list of event types, e.g. 'order.placed,event.published'. |
| Delete Discount | `deleteDiscount` | Delete an Eventbrite discount by its ID. |
| Delete Event | `deleteEvent` | Delete an Eventbrite event. Only draft events with no completed orders can be deleted. |

<details>

<summary>See 44 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Ticket Class | `deleteTicketClass` | Delete a ticket class from an Eventbrite event. Only possible when no tickets of that class have been sold. |
| Delete Webhook | `deleteWebhook` | Delete (unregister) an Eventbrite webhook by its ID. |
| Get Category | `getCategory` | Retrieve a single Eventbrite category by its ID. |
| Get Current User | `getCurrentUser` | Retrieve the Eventbrite user profile associated with the authenticated private token. |
| Get Discount | `getDiscount` | Retrieve a single Eventbrite discount by its ID. |
| Get Event | `getEvent` | Retrieve a single Eventbrite event by its ID, optionally expanding related objects. |
| Get Event Attendee | `getEventAttendee` | Retrieve a single attendee for an Eventbrite event by attendee ID. |
| Get Event Description | `getEventDescription` | Retrieve the full (long) description of an Eventbrite event. |
| Get Event Team | `getEventTeam` | Retrieve a single team for a team-based Eventbrite event by team ID. |
| Get Format | `getFormat` | Retrieve a single Eventbrite event format by its ID. |
| Get Media | `getMedia` | Retrieve metadata for an uploaded Eventbrite media image by its ID. |
| Get Media Upload Instructions | `getMediaUploadInstructions` | Get instructions (upload URL, token, and form fields) for uploading an image to Eventbrite. Pass the media type, then POST the image to the returned upload_url, and finalize with Notify Media Upload. |
| Get Order | `getOrder` | Retrieve a single Eventbrite order by its ID, optionally expanding related objects like attendees. |
| Get Organizer | `getOrganizer` | Retrieve a single Eventbrite organizer profile by its ID. |
| Get Subcategory | `getSubcategory` | Retrieve a single Eventbrite subcategory by its ID. |
| Get Ticket Class | `getTicketClass` | Retrieve a single ticket class for an Eventbrite event by its ID. |
| Get User | `getUser` | Retrieve an Eventbrite user profile by user ID. |
| Get Venue | `getVenue` | Retrieve a single Eventbrite venue by its ID. |
| Get Webhook | `getWebhook` | Retrieve a single Eventbrite webhook by its ID. |
| List Categories | `listCategories` | List all Eventbrite event categories (e.g. Music, Business, Food & Drink). |
| List Discounts | `listDiscounts` | List all discounts belonging to an Eventbrite organization. |
| List Event Attendees | `listEventAttendees` | List all attendees (ticket holders) for an Eventbrite event. |
| List Event Orders | `listEventOrders` | List all orders (ticket purchases) placed for an Eventbrite event. |
| List Event Questions | `listEventQuestions` | List the custom registration questions configured for an Eventbrite event. |
| List Event Teams | `listEventTeams` | List the teams configured for a team-based (group registration) Eventbrite event. |
| List Events | `listEvents` | List events belonging to an Eventbrite organization, with optional status and ordering filters. |
| List Formats | `listFormats` | List all Eventbrite event formats (e.g. Conference, Seminar, Networking). |
| List Organization Orders | `listOrganizationOrders` | List all orders across all events belonging to an Eventbrite organization. |
| List Organizations | `listOrganizations` | List the Eventbrite organizations that the authenticated user belongs to. |
| List Organizers | `listOrganizers` | List all organizer profiles belonging to an Eventbrite organization. |
| List Owned Events | `listOwnedEvents` | DEPRECATED - DO NOT USE. GET /v3/users/me/owned_events/ is retired. Eventbrite moved the platform to an organizations structure in February 2020 and the user-owned-events endpoints reached end of life on 2020-06-01; the endpoint now answers 404 {"status_code":404,"error_description":"The user_id you requested does not exist.","error":"NOT_FOUND"} for every token, which is a retirement response, not a data problem. Use List Events By Organization (GET /v3/organizations/{organization_id}/events/) instead - get the organization id from List Organizations. Refs: https://www.eventbrite.com/platform/docs/organizations, https://www.eventbrite.com/platform/docs/changelog |
| List Subcategories | `listSubcategories` | List all Eventbrite event subcategories across every category. |
| List Ticket Classes | `listTicketClasses` | List all ticket classes (ticket types) for an Eventbrite event. |
| List Timezones | `listTimezones` | List all IANA timezones supported by Eventbrite for scheduling events. |
| List Venue Events | `listVenueEvents` | List all events taking place at a specific Eventbrite venue. |
| List Venues | `listVenues` | List all venues belonging to an Eventbrite organization. |
| List Webhooks | `listWebhooks` | List all webhooks registered for an Eventbrite organization. |
| Publish Event | `publishEvent` | Publish an Eventbrite event so attendees can find and register for it. The event must have at least one ticket class and a venue (or be marked online). |
| Unpublish Event | `unpublishEvent` | Unpublish a live Eventbrite event, hiding it from the public. Only possible when the event has no completed orders. |
| Update Discount | `updateDiscount` | Update an existing Eventbrite discount. Only the fields you provide are changed. |
| Update Event | `updateEvent` | Update an existing Eventbrite event. Only the fields you provide are changed (partial update). Times must be ISO 8601 UTC with a matching IANA timezone. |
| Update Organizer | `updateOrganizer` | Update an existing Eventbrite organizer profile. Only the fields you provide are changed. |
| Update Ticket Class | `updateTicketClass` | Update an existing ticket class for an Eventbrite event. Only the fields you provide are changed. |
| Update Venue | `updateVenue` | Update an existing Eventbrite venue. Only the fields you provide are changed. |

</details>
