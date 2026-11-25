---
description: "Sympla is a Brazilian event ticketing platform. Read events, orders and participants, and check participants in by ticket number or QR code."
hidden: true
---

# Sympla

<img src="../../.gitbook/assets/connectors/lg/sympla.png" alt="Sympla logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [sympla.com.br](https://sympla.com.br) |
| **Authentication** | API key |
| **Slug** | `sympla` |

## Setup

Your customers enter their API key for Sympla when they connect. Nothing else needs setting up.

## Use it

Add Sympla from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.sympla.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check In By QR Code</td><td><code>checkInByQrCode</code></td><td>Register a check-in from the data encoded in a Sympla ticket QR code. Sympla Public API v1.6.0 Body carries the signed QR payload (itemId, walletId, signature, timestamp, version) read from the attendee's QR code.</td></tr><tr><td>Check In By Ticket Number</td><td><code>checkInByTicketNumber</code></td><td>Register the check-in of a participant by ticket number. Sympla Public API v1.6.0</td></tr><tr><td>Check In Participant</td><td><code>checkInParticipant</code></td><td>Register the check-in of a participant by participant id. Sympla Public API v1.6.0 Toggles/records attendance for the ticket.</td></tr><tr><td>Get Event</td><td><code>getEvent</code></td><td>Fetch one event by its id hash. Sympla Public API v1.6.0</td></tr><tr><td>Get Order</td><td><code>getOrder</code></td><td>Fetch one order of an event by its order sk. Sympla Public API v1.6.0</td></tr><tr><td>Get Participant</td><td><code>getParticipant</code></td><td>Fetch one participant (attendee) of an event by participant id. Sympla Public API v1.6.0</td></tr><tr><td>Get Participant By Ticket Number</td><td><code>getParticipantByTicketNumber</code></td><td>Fetch one participant of an event by ticket number. Sympla Public API v1.6.0</td></tr><tr><td>Get Presentation</td><td><code>getPresentation</code></td><td>Fetch one presentation (session) of an event. Sympla Public API v1.6.0</td></tr><tr><td>List Event Orders</td><td><code>listEventOrders</code></td><td>List the orders of an event. Sympla Public API v1.6.0 Cursor-paginated.</td></tr><tr><td>List Event Participants</td><td><code>listEventParticipants</code></td><td>List the participants (attendees) of an event. Sympla Public API v1.6.0 Cursor-paginated.</td></tr></tbody></table>

<details>

<summary>View 5 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Events</td><td><code>listEvents</code></td><td>List the organizer's events. Sympla Public API v1.6.0 Cursor-paginated; returns {data:[...],pagination:{...},sort:{...}}.</td></tr><tr><td>List Order Participants</td><td><code>listOrderParticipants</code></td><td>List the participants (tickets) belonging to one order. Sympla Public API v1.6.0</td></tr><tr><td>List Presentation Orders</td><td><code>listPresentationOrders</code></td><td>List the orders placed for one presentation (session) of an event. Sympla Public API v1.6.0</td></tr><tr><td>List Presentation Participants</td><td><code>listPresentationParticipants</code></td><td>List the participants (attendees) of one presentation (session) of an event. Sympla Public API v1.6.0</td></tr><tr><td>List Presentations</td><td><code>listPresentations</code></td><td>List the presentations (sessions / dates) of an event. Sympla Public API v1.6.0</td></tr></tbody></table>

</details>

## Events

Sympla has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
