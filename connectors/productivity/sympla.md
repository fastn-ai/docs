---
description: "Sympla is Brazil's largest event ticketing and registration platform."
hidden: true
---

# Sympla

Sympla is Brazil's largest event ticketing and registration platform. This connector wraps the Sympla Public API v1.6.0 for event organizers: list and fetch events, list event presentations (sessions), list and fetch orders, list and fetch participants (attendees) by id or ticket number, and perform attendee check-in by participant id, ticket number or QR code.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [sympla.com.br](https://sympla.com.br) |
| **Authentication** | API key |
| **Actions** | 15 |
| **Events** | 0 |
| **Slug** | `sympla` |

## Use it

Add Sympla from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.sympla.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check In By QR Code | `checkInByQrCode` | Register a check-in from the data encoded in a Sympla ticket QR code. Sympla Public API v1.6.0 POST /public/v1.6.0/events/{eventIdHash}/qrcode/check-in. Body carries the signed QR payload (itemId, walletId, signature, timestamp, version) read from the attendee's QR code. |
| Check In By Ticket Number | `checkInByTicketNumber` | Register the check-in of a participant by ticket number. Sympla Public API v1.6.0 POST /public/v1.6.0/events/{eventIdHash}/participants/ticketNumber/{ticketNumber}/check-in. |
| Check In Participant | `checkInParticipant` | Register the check-in of a participant by participant id. Sympla Public API v1.6.0 POST /public/v1.6.0/events/{eventIdHash}/participants/{participantId}/check-in. Toggles/records attendance for the ticket. |
| Get Event | `getEvent` | Fetch one event by its id hash. Sympla Public API v1.6.0 GET /public/v1.6.0/events/{eventIdHash}. |
| Get Order | `getOrder` | Fetch one order of an event by its order sk. Sympla Public API v1.6.0 GET /public/v1.6.0/events/{eventIdHash}/orders/{orderSk}. |
| Get Participant | `getParticipant` | Fetch one participant (attendee) of an event by participant id. Sympla Public API v1.6.0 GET /public/v1.6.0/events/{eventIdHash}/participants/{participantId}. |
| Get Participant By Ticket Number | `getParticipantByTicketNumber` | Fetch one participant of an event by ticket number. Sympla Public API v1.6.0 GET /public/v1.6.0/events/{eventIdHash}/participants/ticketNumber/{ticketNumber}. |
| Get Presentation | `getPresentation` | Fetch one presentation (session) of an event. Sympla Public API v1.6.0 GET /public/v1.6.0/events/{eventIdHash}/presentations/{presentationId}. |
| List Event Orders | `listEventOrders` | List the orders of an event. Sympla Public API v1.6.0 GET /public/v1.6.0/events/{eventIdHash}/orders. Cursor-paginated. |
| List Event Participants | `listEventParticipants` | List the participants (attendees) of an event. Sympla Public API v1.6.0 GET /public/v1.6.0/events/{eventIdHash}/participants. Cursor-paginated. |
| List Events | `listEvents` | List the organizer's events. Sympla Public API v1.6.0 GET /public/v1.6.0/events. Cursor-paginated; returns {data:[...],pagination:{...},sort:{...}}. |
| List Order Participants | `listOrderParticipants` | List the participants (tickets) belonging to one order. Sympla Public API v1.6.0 GET /public/v1.6.0/events/{eventIdHash}/orders/{orderSk}/participants. |
| List Presentation Orders | `listPresentationOrders` | List the orders placed for one presentation (session) of an event. Sympla Public API v1.6.0 GET /public/v1.6.0/events/{eventIdHash}/presentations/{presentationId}/orders. |
| List Presentation Participants | `listPresentationParticipants` | List the participants (attendees) of one presentation (session) of an event. Sympla Public API v1.6.0 GET /public/v1.6.0/events/{eventIdHash}/presentations/{presentationId}/participants. |
| List Presentations | `listPresentations` | List the presentations (sessions / dates) of an event. Sympla Public API v1.6.0 GET /public/v1.6.0/events/{eventIdHash}/presentations. |
