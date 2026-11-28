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

## Connect in Fastn

Your customers connect Sympla from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Sympla**.
2. Select **Connect** on the Sympla card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Sympla's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check In By QR Code</td><td><code>checkInByQrCode</code></td><td>Register a check-in from the data encoded in a Sympla ticket QR code. Sympla Public API v1.6.0 Body carries the signed QR payload (itemId, walletId, signature, timestamp, version) read from the attendee's QR code.</td></tr><tr><td>Check In By Ticket Number</td><td><code>checkInByTicketNumber</code></td><td>Register the check-in of a participant by ticket number. Sympla Public API v1.6.0</td></tr><tr><td>Check In Participant</td><td><code>checkInParticipant</code></td><td>Register the check-in of a participant by participant id. Sympla Public API v1.6.0 Toggles/records attendance for the ticket.</td></tr><tr><td>Get Event</td><td><code>getEvent</code></td><td>Fetch one event by its id hash. Sympla Public API v1.6.0</td></tr><tr><td>Get Order</td><td><code>getOrder</code></td><td>Fetch one order of an event by its order sk. Sympla Public API v1.6.0</td></tr><tr><td>Get Participant</td><td><code>getParticipant</code></td><td>Fetch one participant (attendee) of an event by participant id. Sympla Public API v1.6.0</td></tr><tr><td>Get Participant By Ticket Number</td><td><code>getParticipantByTicketNumber</code></td><td>Fetch one participant of an event by ticket number. Sympla Public API v1.6.0</td></tr><tr><td>Get Presentation</td><td><code>getPresentation</code></td><td>Fetch one presentation (session) of an event. Sympla Public API v1.6.0</td></tr><tr><td>List Event Orders</td><td><code>listEventOrders</code></td><td>List the orders of an event. Sympla Public API v1.6.0 Cursor-paginated.</td></tr><tr><td>List Event Participants</td><td><code>listEventParticipants</code></td><td>List the participants (attendees) of an event. Sympla Public API v1.6.0 Cursor-paginated.</td></tr></tbody></table>

<details>

<summary>View 5 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Events</td><td><code>listEvents</code></td><td>List the organizer's events. Sympla Public API v1.6.0 Cursor-paginated; returns {data:[...],pagination:{...},sort:{...}}.</td></tr><tr><td>List Order Participants</td><td><code>listOrderParticipants</code></td><td>List the participants (tickets) belonging to one order. Sympla Public API v1.6.0</td></tr><tr><td>List Presentation Orders</td><td><code>listPresentationOrders</code></td><td>List the orders placed for one presentation (session) of an event. Sympla Public API v1.6.0</td></tr><tr><td>List Presentation Participants</td><td><code>listPresentationParticipants</code></td><td>List the participants (attendees) of one presentation (session) of an event. Sympla Public API v1.6.0</td></tr><tr><td>List Presentations</td><td><code>listPresentations</code></td><td>List the presentations (sessions / dates) of an event. Sympla Public API v1.6.0</td></tr></tbody></table>

</details>

