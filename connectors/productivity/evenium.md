---
description: "Evenium event registration and ticketing platform (Evenium Net / ConnectMe)."
hidden: true
---

# Evenium

<img src="../../.gitbook/assets/connectors/evenium.png" alt="Evenium logo" width="64">

Evenium event registration and ticketing platform (Evenium Net / ConnectMe). Manage events, guests, participants, tickets, documents, sponsors, alerts, badges and the organisation-wide contact book through the Evenium REST API v1 at https://secure.evenium.com/api/1/.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [evenium.com](https://evenium.com) |
| **Authentication** | API key |
| **Slug** | `evenium` |

## Use it

Add Evenium from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.evenium.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Event Guest | `addEventGuest` | Add a guest to an Evenium event. At least one of firstName, lastName or email is required. Evenium creates or reuses the matching contact and returns the new guest with its contactId, guestId, guestCode and event-site password. No invitation email is sent by this endpoint. |
| Add Event Sponsor | `addEventSponsor` | Add a sponsor to an Evenium event. Evenium answers 204 No Content and assigns the sponsor id, so call List Event Sponsors afterwards to read it back. Evenium exposes no endpoint to update or remove a sponsor once added. |
| Broadcast Event Alert | `broadcastEventAlert` | Broadcast an alert to every participant of an Evenium event as a push notification in the ConnectMe attendee app. subject, text and type are all required - Evenium answers 500 if any is missing. The alert always goes to ALL participants; recipientsType and personIds are read-only. There is no endpoint to recall or delete an alert once sent. |
| Bulk Upsert Contacts | `bulkUpsertContacts` | Create or update many contacts in the Evenium account contact book in one call. Entries carrying an id are updated; entries without one are created. Returns a processing report with per-row status messages rather than the contact objects. |
| Bulk Upsert Event Guests | `bulkUpsertEventGuests` | Create or update many guests of an Evenium event in one call. Each entry carrying a contactId is updated; entries without one are created. Returns a processing report with per-row status messages rather than the guest objects. |
| Create Contact | `createContact` | Create a contact in the Evenium account's shared contact book. Every field is optional - Evenium accepts an empty body and returns a contact with only an id and a generated contactLogin. Returns 201 with the created contact. |
| Create Event | `createEvent` | Create a new Evenium event. title, startDate and endDate are required. Evenium assigns the id, the six-character join code, the public uniqueName and the website URL, and always sets the new event's status to FUTURE (a status supplied here is ignored). The event is created unpublished. |
| Delete Contact | `deleteContact` | Delete a contact from the Evenium account contact book. Returns the deleted contact's id. A subsequent Get Contact for that id answers 404 CONTACT_NOT_FOUND. Do not delete the contact that represents the account owner - it is the organiser record of every event. |
| Delete Event Guest | `deleteEventGuest` | Remove a guest from an Evenium event, identified by CONTACT id. Evenium answers 204 No Content with an empty body; confirm with Get Event Guest, which then answers 404 GUEST_NOT_FOUND. The underlying contact stays in the account contact book - only the event guest record is removed. |
| Delete Event Logo | `deleteEventLogo` | Remove the logo image from an Evenium event's public site. Returns the full updated event. |

<details>

<summary>See 27 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Generate Event Badges PDF | `generateEventBadgesPdf` | Generate the printable attendee badge sheet for an Evenium event as a PDF. The endpoint produces application/pdf only and rejects Accept: application/json. It returns a zero-byte PDF when the event has no badge template - badge templates are designed in the Evenium Net web app, not through the API. |
| Get Contact | `getContact` | Retrieve one contact from the Evenium account contact book by numeric contact id. |
| Get Event | `getEvent` | Retrieve a single Evenium event by its numeric id, including its dates, status, join code, public website URL, location and configuration fields. |
| Get Event Banner | `getEventBanner` | Fetch the banner image configured on an Evenium event's public site. Evenium answers 204 No Content when the event has no banner set. |
| Get Event Document | `getEventDocument` | Retrieve one document attached to an Evenium event by its storage path. The path segment is matched literally, so a missing document answers 404 RESOURCE_NOT_FOUND naming the path that was looked up. |
| Get Event Guest | `getEventGuest` | Retrieve one guest of an Evenium event. Identify the guest by its CONTACT id (the contactId field of the guest object), not by guestId - passing a guestId returns GUEST_NOT_FOUND. SECURITY: the response includes the guest's guestCode and plaintext event-site password. |
| Get Event Participant | `getEventParticipant` | Retrieve one participant of an Evenium event by person id (the id field returned by List Event Participants). Note the response is the GUEST representation - contactId, guestId, guestCode, password, registration status and fields - not the participant shape returned by the list endpoint. SECURITY: the response includes the attendee's guestCode and plaintext event-site password. |
| Get Event Ticket | `getEventTicket` | Retrieve one ticket of an Evenium event by ticket id, including its check-in code, product, buyer and customer names, order date and validity status. |
| Issue Event Ticket | `issueEventTicket` | Issue a ticket for an attendee of an Evenium event. The attendee is identified by contact details; Evenium matches or creates the guest, marks the registration CONFIRMED and returns the ticket with its check-in code. This endpoint takes form-encoded fields, not JSON. Note Evenium provides no endpoint to void or delete an issued ticket. |
| List Contact Events | `listContactEvents` | List every Evenium event a given contact is registered for, each with the contact's own registration details. Evenium returns a bare JSON array here rather than a paged envelope, so the events appear under the items key of this action's output. |
| List Contacts | `listContacts` | List the contacts in the Evenium account's shared contact book, with offset/limit paging. Contacts are account-wide people records that event guests are linked to. |
| List Event Alerts | `listEventAlerts` | List the alerts broadcast to an Evenium event's attendees, newest first. Each entry carries its messageId, subject, text, send date, recipient scope and the person ids it reached. The response envelope names the array "messages". |
| List Event Documents | `listEventDocuments` | List the documents attached to an Evenium event. Documents can only be uploaded through the Evenium Net web app - the API exposes no write verb for them. An event with no documents answers 404 RESOURCE_NOT_FOUND "No document found with path /" rather than an empty list. |
| List Event Guests | `listEventGuests` | List the guests invited to an Evenium event, with paging and registration-status filtering. SECURITY: Evenium returns each guest's guestCode and plaintext event-site password in this response - treat the output as confidential and do not forward it downstream. |
| List Event Organizers | `listEventOrganizers` | List the organisers of an Evenium event. Evenium returns a bare JSON array here rather than the usual paged envelope, so the organisers appear under the items key of this action's output. |
| List Event Participants | `listEventParticipants` | List the participants of an Evenium event - the people-facing view of the attendee list, including each person's category, photo preview and numeric registration status code. |
| List Event Sponsors | `listEventSponsors` | List the sponsors shown on an Evenium event, each with its id, name, description, website URL and logo. |
| List Event Tickets | `listEventTickets` | List the tickets issued for an Evenium event, with buyer and customer names, ticket code, product, order date and validity status. |
| List Events | `listEvents` | List the events in your Evenium account, newest first. Supports offset/limit paging via firstResult and maxResults, and filtering by event lifecycle status. Returns a paged envelope with nbrResults, maxResults, firstResult, more and an events array. |
| Log In For Access Token | `logInForAccessToken` | Exchange an Evenium user login and password for an API access token, sent as query parameters. WARNING: the success response contains a live credential - do not log or forward it. Evenium answers 401 AUTHENTICATION_REQUIRED "incorrect password or login" for a wrong pair, and repeated failures may lock the account, so do not retry in a loop. |
| Set Event Logo | `setEventLogo` | Upload the logo image shown on an Evenium event's public site, as a multipart file part. Any part name is accepted. Returns the full updated event. Text-safe image formats such as an ASCII Netpbm P3 PPM upload cleanly through this action. |
| Set Guest Photo From Data URI | `setGuestPhotoFromDataUri` | Replace an event guest's profile photo by sending a base64 data URI as a plain-text body, e.g. data:image/png;base64,iVBORw0KGgo... Evenium rejects bare base64, a remote URL and an empty body. This is the reliable way to set a binary image such as PNG or JPEG. Returns the updated guest. |
| Submit Login Form | `submitLoginForm` | Exchange an Evenium user login and password for an API access token, posted as a form body. This is the POST form of the login route; it accepts only application/x-www-form-urlencoded and rejects JSON with 406 NOT_ACCEPTABLE. WARNING: the success response contains a live credential. Repeated failures may lock the account, so do not retry in a loop. |
| Update Contact | `updateContact` | Update one contact in the Evenium account contact book. Send only the fields to change. Evenium answers 204 No Content with an empty body, so read the contact back with Get Contact to confirm the change. |
| Update Event | `updateEvent` | Update an existing Evenium event. Send only the fields you want to change; omitted fields are left untouched. Returns the full updated event. Note: Evenium accepts a status field but silently ignores it - the event lifecycle status cannot be changed through this endpoint, and there is no delete endpoint for events. |
| Update Event Guest | `updateEventGuest` | Update one guest of an Evenium event, identified by CONTACT id. Send only the fields to change. Returns the full updated guest. Evenium rejects a status value here with REQUEST_ERROR - registration status is driven by the attendee's own registration and by ticket purchase, not by this endpoint. |
| Upload Guest Photo | `uploadGuestPhoto` | Upload a profile photo for an event guest as a multipart file part. The part must be named "photo" - Evenium rejects any other part name with REQUEST_ERROR. Supply the raw image bytes in photoData and a matching boundary. Returns the updated guest. |

</details>
