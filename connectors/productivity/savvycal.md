---
description: "SavvyCal is a scheduling platform for booking meetings on your own terms."
hidden: true
---

# SavvyCal

SavvyCal is a scheduling platform for booking meetings on your own terms. This connector covers the complete SavvyCal Meetings REST API (https://api.savvycal.com/v1): the current user profile, scheduling links (list, get, create in personal or team scope, update, duplicate, toggle active/disabled, delete), available time slots, events (list, get, create a booking, cancel), the IANA time-zone directory with localized names and DST detail, workflows and their rules, and webhook subscription management. Authentication is a SavvyCal personal access token sent as a Bearer token.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [savvycal.com](https://savvycal.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 24 |
| **Events** | 16 |
| **Slug** | `savvycal` |

## Use it

Add SavvyCal from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.savvycal.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Event | `cancelEvent` | Cancels a scheduled meeting, releasing the time on the organizer's calendar and notifying the attendees. Supply a cancellation reason to include it in the notification. Returns the event with state 'canceled'. |
| Create Event | `createEvent` | Books a meeting on a scheduling link on a scheduler's behalf. This is a real booking: it holds the time on the organizer's calendar and SavvyCal emails the scheduler a confirmation. Start and end times must match an available slot, so call List Available Slots first and pass its start_at and end_at verbatim. Conferencing details are generated from the link's own settings. |
| Create Personal Scheduling Link | `createPersonalSchedulingLink` | Creates a new scheduling link in the authenticated user's personal scope. Choose a multi-use (recurring) link that anyone can book repeatedly, or a single-use link that expires after one booking. Use Create Scheduling Link In Scope to create one under a team instead. |
| Create Scheduling Link In Scope | `createScopeSchedulingLink` | Creates a new scheduling link under a specific individual or team scope, identified by the scope's slug. Use Create Personal Scheduling Link when the link belongs to the authenticated user's own scope. Scope slugs are returned in the scope object of List Scheduling Links. |
| Create Webhook | `createWebhook` | Registers an HTTPS endpoint to receive SavvyCal event notifications. One endpoint receives every event type; there is no per-event filter. The response includes a signing secret unique to this endpoint, which SavvyCal uses to sign each delivery. |
| Delete Scheduling Link | `deleteSchedulingLink` | Permanently deletes a scheduling link. Anyone holding its URL can no longer book with it. Returns the link as it was at the moment of deletion. |
| Delete Webhook | `deleteWebhook` | Removes a webhook endpoint so SavvyCal stops posting event deliveries to it. Returns the webhook with state 'deleted'. |
| Duplicate Scheduling Link | `duplicateSchedulingLink` | Creates a copy of an existing scheduling link, carrying over its durations, increment and custom fields. The copy gets its own ID and slug. Returns the new link. |
| Get Current User | `getCurrentUser` | Retrieves the profile of the SavvyCal user the access token belongs to, including their email, display name, time zone, time and week formatting preferences, and current plan. |
| Get Event | `getEvent` | Retrieves a single scheduled meeting by its event ID or UUID, returning the full record: state, times, duration and buffers, organizer, scheduler and attendees, conferencing details, the scheduling link it was booked on, payment state and any custom metadata. |
| Get Scheduling Link | `getSchedulingLink` | Retrieves a single scheduling link by its ID, returning the slug, public and private names, description, available durations, slot increment, custom booking-form fields, owning scope and state. |
| Get Time Zone | `getTimeZone` | Get detailed info for a two-segment IANA time zone such as America/Chicago (GET /v1/time_zones/{area}/{location}). The engine URL-encodes '/' inside one value, so each segment is its own input. Use Get Time Zone (One Segment) for ids like UTC and Get Time Zone (Three Segments) for ids like America/Argentina/Buenos_Aires. |
| Get Time Zone (One Segment) | `getTimeZoneOneSegment` | Get detailed info for a single-segment time zone id such as UTC or EST (GET /v1/time_zones/{id}). |
| Get Time Zone (Three Segments) | `getTimeZoneThreeSegments` | Get detailed info for a three-segment IANA time zone such as America/Argentina/Buenos_Aires (GET /v1/time_zones/{area}/{location}/{subLocation}). |
| Get Webhook | `getWebhook` | Retrieves a single webhook endpoint by its ID, returning its URL, state, payload version, creation time and signing secret. |
| List Available Slots | `getLinkSlots` | Lists the bookable time slots on a scheduling link. When the organizer allows several durations, slots are returned for each duration, so the same start time can appear more than once with a different length. Use these exact start and end times when calling Create Event. The search window may not exceed 31 days. |
| List Events | `listEvents` | Lists meetings scheduled through SavvyCal, with the organizer, attendees, conferencing details, buffers, payment state and the link they were booked on. Filter by event state, by period (past, upcoming or a fixed date range), by scheduling link, and by whether the authenticated user is attending. Page with the cursor values returned in the metadata object. |
| List Scheduling Links | `listSchedulingLinks` | Lists the scheduling links belonging to the authenticated user, with each link's slug, public and private names, description, available durations, slot increment, custom fields, owning scope and state. Filter by state and page with the cursor values returned in the metadata object. |
| List Time Zones | `listTimeZones` | Returns the full IANA (Olson) time-zone directory with localized names, abbreviations, UTC offsets, daylight-saving state, aliases, Windows zone names and metazone grouping, described as of a chosen moment in time. Useful for building a time-zone picker. |
| List Webhooks | `listWebhooks` | Lists the webhook endpoints registered for the authenticated user, with each endpoint's URL, state, payload version and signing secret. Page with the cursor values returned in the metadata object. |
| List Workflow Rules | `listWorkflowRules` | Lists the rules that make up one workflow: what event triggers each rule, how long before or after that event it fires, and which actions it runs, such as sending a custom email or triggering an automation. |
| List Workflows | `listWorkflows` | Lists the automated workflows across the scopes the authenticated user manages, with each workflow's name, state and creation time. Use List Workflow Rules to see what triggers each one. |
| Toggle Scheduling Link State | `toggleSchedulingLink` | Flips a scheduling link between active and disabled. Disabling stops new bookings without deleting the link, so its URL can be re-enabled later by calling this action again. Returns the link with its new state. |
| Update Scheduling Link | `updateSchedulingLink` | Updates an existing scheduling link. Only the fields you supply are changed; anything you leave out keeps its current value. Returns the link after the update. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Event Approved | `event.approved` | Fires when an organizer approves a meeting that required approval. Carries the Event object. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
| Event Attendee Added | `event.attendee.added` | Fires when a new attendee joins an existing meeting, typically a group session. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
| Event Attendee Canceled | `event.attendee.canceled` | Fires when one attendee cancels out of a group session while the meeting itself continues. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
| Event Attendee Rescheduled | `event.attendee.rescheduled` | Fires when one attendee of a group session moves their own response to a different time. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
| Event Canceled | `event.canceled` | Fires when a meeting is cancelled by either party. The Event object carries state canceled plus canceled_at and cancel_reason. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
| Event Changed | `event.changed` | Fires when a meeting's details are updated. Carries the Event object as it now stands. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
| Event Checkout Completed | `event.checkout.completed` | Fires when payment for a paid meeting succeeds. The Event object's payment object carries state paid and a Stripe dashboard URL. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
| Event Checkout Expired | `event.checkout.expired` | Fires when checkout for a paid meeting is abandoned and the held slot is released. The Event object carries state checkout_expired. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
| Event Checkout Pending | `event.checkout.pending` | Fires when a scheduler starts booking a paid meeting and checkout has begun but not completed. The Event object carries a payment object with state awaiting_checkout. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
| Event Created | `event.created` | Fires when someone schedules a new meeting, or when an organizer approves a meeting that required approval. Note: a SavvyCal webhook endpoint receives EVERY event type; the API has no per-event filter, so subscribing to any one event registers the same endpoint for all of them. Payload schema taken from SavvyCal's own published OpenAPI description (https://api.savvycal.com/v1/spec), not from a captured delivery. |
| Event Declined | `event.declined` | Fires when an organizer declines a meeting that required approval. Carries the Event object with state declined. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
| Event Requested | `event.requested` | Fires when someone schedules a meeting on a link that requires the organizer's approval, before that approval is given. Carries the Event object with state awaiting_approval. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
| Event Rescheduled | `event.rescheduled` | Fires when an existing meeting is moved to a new time. The Event object carries original_start_at, original_end_at, rescheduled_at and reschedule_reason. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
| Poll Response Created | `poll.response.created` | Fires when someone submits their availability to a SavvyCal meeting poll. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
| Poll Response Updated | `poll.response.updated` | Fires when someone changes availability they had already submitted to a meeting poll. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
| Workflow Action Triggered | `workflow.action.triggered` | Fires when a SavvyCal workflow rule runs one of its actions, such as sending a custom email or triggering an automation. Payload schema taken from SavvyCal's published OpenAPI description, not from a captured delivery. |
