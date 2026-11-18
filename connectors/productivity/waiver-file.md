---
description: "WaiverFile digital waiver management."
hidden: true
---

# WaiverFile

<img src="../../.gitbook/assets/connectors/waiver-file.png" alt="WaiverFile logo" width="64">

WaiverFile digital waiver management. Manage waiver forms and signed waivers, events and event categories, event managers, SMS subscribers, and webhook subscriptions for new/edited waivers, events, check-ins and QR scans.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [waiverfile.com](https://waiverfile.com) |
| **Authentication** | API key |
| **Slug** | `waiverFile` |

## Use it

Add WaiverFile from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.waiverFile.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Event | `createEvent` | Quickly create an event from just a name, start and end date and the waiver forms to attach. Use Insert Event when you also need category, location, manager invites or a participant cap. |
| Delete Event | `deleteEvent` | Delete an event from the site by its GUID. Signed waivers already attached to the event are retained. |
| Delete Event Category | `deleteEventCategory` | Permanently delete an event category. Events previously assigned to it keep an empty category. |
| Event Service Ping | `evtPing` | Echo test for the WaiverFile event service: posts a string and receives the same string back. Use it to confirm the event endpoints are reachable. |
| Get Active Waiver Forms | `getActiveWaiverForms` | List every waiver form that is currently active on the site and can be signed. Returns an array of waiver form objects. |
| Get All Waiver Forms | `getAllWaiverForms` | List every waiver form on the site, including inactive and archived forms. Returns an array of waiver form objects. |
| Get All Waivers By Date Range | `getAllWaiversByDateRange` | Page through every signed waiver in a date range, with full waiver detail including participants and answers. Returns an XML-derived JSON document with an ArrayOfWaiver element. |
| Get All Waivers By Date Range Lite | `getAllWaiversByDateRangeLite` | Page through signed waivers in a date range without heavy payloads such as signature images and attachments. Use this instead of the full version for large exports. |
| Get All Waivers By Date Range Page Count | `getAllWaiversByDateRangePageCount` | Return how many waiver records fall in a date range, so you can size the paging loop for Get All Waivers By Date Range. Returns a bare integer. |
| Get Event Categories | `getEventCategories` | List the event categories defined on the site, optionally including categories that have been disabled. Returns an array of category objects. |

<details>

<summary>See 40 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Events By Category | `getEventsByCategory` | List events in a single event category whose start date falls between two UTC dates. Returns an array of event objects. |
| Get Events By Date Range | `getEventsByDateRange` | List all events whose start date falls between two UTC dates. Returns an array of event objects. |
| Get Opted Out SMS Subscribers By Opt Out Date | `getOptedOutSubscribersByOptOutDate` | List SMS subscribers who opted out between two UTC dates, so you can suppress them downstream. Returns an array of subscriber records. |
| Get Sample Edit Waiver Payload | `getSampleEditWaiverPayload` | Return a sample of the payload WaiverFile posts to an edit-waiver webhook subscriber, so you can build and test your receiver. |
| Get Sample New Check In Payload | `getSampleNewCheckInPayload` | Return a sample of the payload WaiverFile posts to a new-check-in webhook subscriber, so you can build and test your receiver. |
| Get Sample New Event Payload | `getSampleNewEventPayload` | Return a sample of the payload WaiverFile posts to a new-event webhook subscriber, so you can build and test your receiver. |
| Get Sample New Waiver Payload | `getSampleNewWaiverPayload` | Return a sample of the payload WaiverFile posts to a new-waiver webhook subscriber, so you can build and test your receiver before a real waiver is signed. |
| Get Site Details | `getSiteDetails` | Retrieve the full configuration of your WaiverFile waiver site, including the site name, URL slug, customer and subscription details, display labels and site settings. Useful as a connection health check. |
| Get SMS Subscribers By Date | `getSubscribersByDate` | List SMS subscribers who opted in between two UTC dates. Returns an array of subscriber records. |
| Get Upcoming Events | `getUpcomingEvents` | List upcoming events between two UTC dates, returned as a JSON-encoded string of event objects with their settings and participant counts. |
| Get Waiver | `getWaiver` | Retrieve one signed waiver in full, including participants, answers, signatures, images and attachments. Use Get Waiver Lite if you only need the header fields. |
| Get Waiver Data | `getWaiverData` | Return signed waivers in a date range as a flat, spreadsheet-style table, optionally including custom form columns and consolidating one row per participant. Best endpoint for exports and reporting. |
| Get Waiver Data Count | `getWaiverDataCount` | Return the number of rows Get Waiver Data would produce for a date range, so you can size the paging loop. Returns a bare integer. |
| Get Waiver Lite | `getWaiverLite` | Retrieve one signed waiver without heavy payloads such as signature images and attachments. Faster than Get Waiver when you only need the header fields. |
| Get Waiver PDF | `getWaiverPDF` | Download the rendered PDF of one signed waiver, suitable for archiving or emailing. |
| Get Waivers By Reference ID | `getWaiversByReferenceID` | Find signed waivers by the custom reference IDs your system passed into the waiver URL. Match on a specific reference slot, or on any slot. Pass an empty string for slots you do not want to filter on. |
| Get Waivers For Event | `getWaiversForEvent` | List every signed waiver attached to a single event. Returns an array of waiver objects. |
| Insert Event | `insertEvent` | Create a new WaiverFile event from a details package, including name, start and end date, category, location, manager invitations, participant cap and the waiver forms attached to the event. Returns the created event. |
| Insert Event Category | `insertEventCategory` | Create a new event category used to group events on the site. Returns the created category with its GUID. |
| Insert Or Update Event | `insertOrUpdateEvent` | Upsert a full WaiverEvent record. Pass the event as returned by Get Events By Date Range with your edits applied, including its settings: WaiverFile rejects a partial object with 400 "Error updating WaiverEvent" or 500. Returns the stored event. |
| Invite Event Managers | `inviteEventManagers` | Grant one or more email addresses manager access to an event, so they can see its signees and participants. WaiverFile emails each new manager an invitation; set Skip Sending Email If Account Exists to true to suppress the email for addresses that already have a WaiverFile account. Returns the event with its updated manager list. |
| Ping | `ping` | Check that the WaiverFile API is reachable and that the supplied API key and Site ID are valid. Returns the literal string "Service online". |
| Remove Event Managers | `removeEventManagers` | Revoke manager access to an event for one or more email addresses. Returns the event with its updated manager list. |
| Search Waivers | `searchWaivers` | Free-text search across signed waivers by participant name, email or other indexed fields. Returns an XML-derived JSON document with an ArrayOfWaiver element. |
| Subscribe To Edit Check In Webhook | `subscribeEditCheckIn` | Register a target URL that WaiverFile will POST to whenever an existing check-in is edited. Returns "OK" on success. |
| Subscribe To Edit Event Webhook | `subscribeEditEvent` | Register a target URL that WaiverFile will POST to whenever an existing event is edited. Returns "OK" on success. |
| Subscribe To Edit Waiver Webhook | `subscribeEditWaiver` | Register a target URL that WaiverFile will POST to whenever an existing waiver is edited. Returns "OK" on success. |
| Subscribe To New Check In Webhook | `subscribeNewCheckIn` | Register a target URL that WaiverFile will POST to whenever a participant checks in. Returns "OK" on success. |
| Subscribe To New Event Webhook | `subscribeNewEvent` | Register a target URL that WaiverFile will POST to whenever a new event is created. Returns "OK" on success. |
| Subscribe To New QR Scan Webhook | `subscribeNewQrScan` | Register a target URL that WaiverFile will POST to whenever a waiver QR code is scanned. Returns "OK" on success. |
| Subscribe To New Waiver Webhook | `subscribeNewWaiver` | Register a target URL that WaiverFile will POST to whenever a new waiver is signed on your site. Returns "OK" on success. |
| Unsubscribe From Edit Check In Webhook | `unsubscribeEditCheckIn` | Remove a previously registered edit-check-in webhook target URL. The same target URL used to subscribe must be supplied. Returns "OK" on success. |
| Unsubscribe From Edit Event Webhook | `unsubscribeEditEvent` | Remove a previously registered edit-event webhook target URL. The same target URL used to subscribe must be supplied. Returns "OK" on success. |
| Unsubscribe From Edit Waiver Webhook | `unsubscribeEditWaiver` | Remove a previously registered edit-waiver webhook target URL. The same target URL used to subscribe must be supplied. Returns "OK" on success. |
| Unsubscribe From New Check In Webhook | `unsubscribeNewCheckIn` | Remove a previously registered new-check-in webhook target URL. The same target URL used to subscribe must be supplied. Returns "OK" on success. |
| Unsubscribe From New Event Webhook | `unsubscribeNewEvent` | Remove a previously registered new-event webhook target URL. The same target URL used to subscribe must be supplied. Returns "OK" on success. |
| Unsubscribe From New QR Scan Webhook | `unsubscribeNewQrScan` | Remove a previously registered QR-scan webhook target URL. The same target URL used to subscribe must be supplied. Returns "OK" on success. |
| Unsubscribe From New Waiver Webhook | `unsubscribeNewWaiver` | Remove a previously registered new-waiver webhook target URL. The same target URL used to subscribe must be supplied. Returns "OK" on success. |
| Update Event | `updateEvent` | Update an existing event's name, dates, all-day flag, category and the set of waiver forms attached to it. Returns the updated event. |
| Update Event Category | `updateEventCategory` | Rename an existing event category or enable/disable it. Returns the updated category. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Check In Edited | `editcheckin` | Fires when an existing check-in is edited. MODELLED, not captured: WaiverFile publishes no sampledata endpoint for this event and no check-ins exist on this account. No signature header is sent. |
| Event Edited | `editevent` | Fires when an existing event is edited. CAPTURED from a real delivery on 2026-09-21: a SINGLE JSON object identical in shape to the newevent delivery, with no signature header. |
| New Check In | `newcheckin` | Fires when a participant checks in at an event. MODELLED, not captured: no waivers exist on this account to check in, and GET /api/v1/sampledata/newcheckin returns an empty array. No signature header is sent. |
| New Event Created | `newevent` | Fires when a new event is created on the site. CAPTURED from a real delivery on 2026-09-21: WaiverFile POSTs a SINGLE JSON object (not an array) with Content-Type application/json; charset=utf-8 and no signature header. There is no event-type discriminator in the body, which is why each event type is registered against its own target URL. |
| New QR Scan | `newqrscan` | Fires when a waiver QR code is scanned. MODELLED, not captured: WaiverFile publishes no sampledata endpoint for this event and no waivers exist on this account to scan. No signature header is sent. |
| New Waiver Signed | `newwaiver` | Fires when a participant signs a new waiver. MODELLED, not captured: this account has zero waiver forms so no waiver can be signed, and GET /api/v1/sampledata/newwaiver returns an empty array. Shape follows the vendor's Waiver definition and the single-object delivery convention proven on the event webhooks. No signature header is sent. |
| Waiver Edited | `editwaiver` | Fires when an existing waiver is edited. MODELLED, not captured: this account has zero waivers and GET /api/v1/sampledata/editwaiver returns an empty array. No signature header is sent. |
