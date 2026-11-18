---
description: "Cal.com API v2 connector."
---

# Cal.com

Cal.com API v2 connector. Scheduling automation — bookings (list, get, create, cancel, reschedule, confirm, decline, reassign, mark no-show, attendees, guests, references, recordings, transcripts), event types (CRUD + history), schedules/availability (CRUD), slots (get available, reserve, manage reservations), calendars (list, busy times, connect/disconnect), conferencing apps, teams (CRUD, members, team event types, team bookings), webhooks (CRUD), out-of-office, verified resources, and the authenticated user profile (me). Base https://api.cal.com/v2. Auth: Bearer API key (cal_live_ / cal_ prefix). Each endpoint group requires a static cal-api-version date header.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [cal.com](https://cal.com) |
| **Authentication** | Bearer token |
| **Actions** | 72 |
| **Events** | 21 |
| **Slug** | `calcom` |

## Use it

Add Cal.com from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.calcom.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Booking Guests | `addBookingGuests` | Add guest emails to an existing booking (POST /v2/bookings/{bookingUid}/guests). |
| Cancel Booking | `cancelBooking` | Cancel a booking by UID (POST /v2/bookings/{bookingUid}/cancel). |
| Check Calendar Connection | `checkCalendarConnection` | Check whether a specific calendar app (Apple, Google, or Office365) is connected for the authenticated user (GET /v2/calendars/{calendar}/check). |
| Check ICS Feed | `checkIcsFeed` | Validate an ICS calendar feed URL before saving it (GET /v2/calendars/ics-feed/check). |
| Confirm Booking | `confirmBooking` | Confirm a pending booking (POST /v2/bookings/{bookingUid}/confirm). |
| Create Booking | `createBooking` | Create a booking (POST /v2/bookings). Provide start, attendee, and either eventTypeId or eventTypeSlug+username. |
| Create Event Type | `createEventType` | Create an event type (POST /v2/event-types). Requires lengthInMinutes, title, slug. |
| Create Out Of Office | `createOutOfOffice` | Create an out-of-office entry (POST /v2/ooo). Requires start, end. |
| Create Schedule | `createSchedule` | Create an availability schedule (POST /v2/schedules). Requires name, timeZone, isDefault. |
| Create Team | `createTeam` | Create a team inside a Cal.com organization (POST /v2/organizations/{orgId}/teams). Cal.com removed the old POST /v2/teams route; teams are now created per organization. Requires orgId and name; the account must belong to a Cal.com organization. |
| Create Webhook | `createWebhook` | Create a webhook subscription (POST /v2/webhooks). Requires subscriberUrl, triggers, active. |
| Decline Booking | `declineBooking` | Decline a pending booking request (POST /v2/bookings/{bookingUid}/decline). |
| Delete Event Type | `deleteEventType` | Delete an event type (DELETE /v2/event-types/{eventTypeId}). |
| Delete Out Of Office | `deleteOutOfOffice` | Delete an out-of-office entry (DELETE /v2/me/ooo/{outOfOfficeId}). |
| Delete Schedule | `deleteSchedule` | Delete an availability schedule (DELETE /v2/schedules/{scheduleId}). |
| Delete Slot Reservation | `deleteSlotReservation` | Release a reserved slot (DELETE /v2/slots/reservations/{reservationUid}). |
| Delete Team | `deleteTeam` | Delete a team (DELETE /v2/teams/{teamId}). |
| Delete Webhook | `deleteWebhook` | Delete a webhook subscription (DELETE /v2/webhooks/{webhookId}). |
| Disconnect Calendar | `disconnectCalendar` | Disconnect a connected calendar (DELETE /v2/calendars/{calendar}/disconnect). |
| Disconnect Conferencing App | `disconnectConferencingApp` | Disconnect a connected conferencing application (DELETE /v2/conferencing/{app}/disconnect). |
| Get Available Slots | `getSlots` | Get available time slots for an event type within a date range (GET /v2/slots). Free read. |
| Get Booking | `getBooking` | Get a single booking by its UID (GET /v2/bookings/{bookingUid}). Free read. |
| Get Booking By Seat UID | `getBookingBySeatUid` | Get a seated booking by its seat reference UID (GET /v2/bookings/by-seat/{seatUid}). Only applies to event types with seats enabled. |
| Get Booking Calendar Links | `getBookingCalendarLinks` | Get 'Add to Calendar' links for a booking, including Google Calendar, Microsoft Office, Outlook, and a downloadable ICS file (GET /v2/bookings/{bookingUid}/calendar-links). |
| Get Booking Recordings | `getBookingRecordings` | Get Cal Video recordings for a booking (GET /v2/bookings/{bookingUid}/recordings). Free read. |
| Get Booking References | `getBookingReferences` | Get external references (calendar/video) for a booking (GET /v2/bookings/{bookingUid}/references). Free read. |
| Get Booking Transcripts | `getBookingTranscripts` | Get Cal Video transcript download links for a booking (GET /v2/bookings/{bookingUid}/transcripts). Free read. |
| Get Calendar Busy Times | `getCalendarBusyTimes` | Get busy times across connected calendars for a date range (GET /v2/calendars/busy-times). Free read. |
| Get Calendar Connect URL | `getCalendarConnectUrl` | Get the OAuth URL to connect a calendar app such as Google or Office365 (GET /v2/calendars/{calendar}/connect). |
| Get Conferencing OAuth Auth URL | `getConferencingOAuthUrl` | Get the OAuth authorization URL to connect a conferencing app such as Zoom or Microsoft Teams (GET /v2/conferencing/{app}/oauth/auth-url). |
| Get Default Conferencing App | `getDefaultConferencingApp` | Get the user's default conferencing application (GET /v2/conferencing/default). Free read. |
| Get Default Schedule | `getDefaultSchedule` | Get the user's default availability schedule (GET /v2/schedules/default). Free read. |
| Get Event Type | `getEventType` | Get a single event type by ID (GET /v2/event-types/{eventTypeId}). Free read. |
| Get My Profile | `getMe` | Get the authenticated user's profile (GET /v2/me). Free read — ideal for credential validation. |
| Get Reserved Slot | `getReservedSlot` | Get details of a reserved slot (GET /v2/slots/reservations/{reservationUid}). Free read. |
| Get Schedule | `getSchedule` | Get a schedule by ID (GET /v2/schedules/{scheduleId}). Free read. |
| Get Team | `getTeam` | Get a team by ID (GET /v2/teams/{teamId}). Free read. |
| Get Verified Phone Number By ID | `getVerifiedPhoneNumberById` | Get a single verified phone number by its ID (GET /v2/verified-resources/phones/{phoneNumberId}). Free read. |
| Get Webhook | `getWebhook` | Get a webhook subscription by ID (GET /v2/webhooks/{webhookId}). Free read. |
| List Booking Attendees | `listBookingAttendees` | List attendees of a booking (GET /v2/bookings/{bookingUid}/attendees). Free read. |
| List Bookings | `listBookings` | List bookings with filters and cursor pagination (GET /v2/bookings). Free read. |
| List Calendars | `listCalendars` | List connected calendars and their connection status (GET /v2/calendars). Free read. |
| List Conferencing Apps | `listConferencing` | List connected conferencing apps (GET /v2/conferencing). Free read. |
| List Event Types | `listEventTypes` | List event types, optionally filtered by username/eventSlug (GET /v2/event-types). Free read. |
| List Organization Teams | `listOrgTeams` | List teams within the caller's organization (GET /v2/organizations/{orgId}/teams). Requires the account to belong to a Cal.com Organization (Enterprise-tier feature) — not available on Free/Individual plans. |
| List Out Of Office | `listOutOfOffice` | List the authenticated user's out-of-office entries (GET /v2/me/ooo). Free read. |
| List Schedules | `listSchedules` | List availability schedules (GET /v2/schedules). Free read. |
| List Team Bookings | `listTeamBookings` | List bookings for a team (GET /v2/teams/{teamId}/bookings). Free read. |
| List Team Event Types | `listTeamEventTypes` | List event types belonging to a team (GET /v2/teams/{teamId}/event-types). Free read. |
| List Team Memberships | `listTeamMemberships` | List members of a team (GET /v2/teams/{teamId}/memberships). Free read. |
| List Teams | `listTeams` | List teams the authenticated user belongs to (GET /v2/teams). Free read. |
| List Verified Emails | `listVerifiedEmails` | List the authenticated user's verified email addresses (GET /v2/verified-resources/emails). Free read. |
| List Verified Phone Numbers | `listVerifiedPhoneNumbers` | List the authenticated user's verified phone numbers (GET /v2/verified-resources/phones). Free read. |
| List Webhooks | `listWebhooks` | List webhook subscriptions (GET /v2/webhooks). Free read. |
| Mark Booking Absence | `markBookingAbsence` | Mark a host or attendee as no-show for a booking (POST /v2/bookings/{bookingUid}/mark-absent). |
| Reassign Booking (Auto) | `reassignBooking` | Automatically reassign a team booking to another available host (POST /v2/bookings/{bookingUid}/reassign). |
| Reassign Booking To Host | `reassignBookingToHost` | Reassign a team booking to a specific host (POST /v2/bookings/{bookingUid}/reassign/{userId}). |
| Request Reschedule | `requestReschedule` | Request that an attendee reschedule a booking (POST /v2/bookings/{bookingUid}/request-reschedule). |
| Reschedule Booking | `rescheduleBooking` | Reschedule a booking to a new start time (POST /v2/bookings/{bookingUid}/reschedule). |
| Reserve Slot | `reserveSlot` | Reserve a time slot temporarily so it cannot be double-booked (POST /v2/slots/reserve). |
| Save ICS Feed | `saveIcsFeed` | Save one or more read-only ICS calendar feed URLs as a connected calendar (POST /v2/calendars/ics-feed/save). |
| Set Default Conferencing App | `setDefaultConferencingApp` | Set which connected conferencing app is used by default for new bookings (POST /v2/conferencing/{app}/default). |
| Update Destination Calendar | `updateDestinationCalendar` | Set which connected calendar new bookings are synced to (PUT /v2/calendars/destination). |
| Update Event Type | `updateEventType` | Update an event type (PATCH /v2/event-types/{eventTypeId}). |
| Update My Profile | `updateMe` | Update the authenticated user's profile (PATCH /v2/me). |
| Update Out Of Office | `updateOutOfOffice` | Update an existing out-of-office entry (PATCH /v2/me/ooo/{outOfOfficeId}). |
| Update Schedule | `updateSchedule` | Update an availability schedule (PATCH /v2/schedules/{scheduleId}). |
| Update Slot Reservation | `updateSlotReservation` | Update an existing slot reservation's hold time or slot window (PATCH /v2/slots/reservations/{reservationUid}). |
| Update Team | `updateTeam` | Update a team (PATCH /v2/teams/{teamId}). |
| Update Webhook | `updateWebhook` | Update a webhook subscription (PATCH /v2/webhooks/{webhookId}). |
| Verify Email | `verifyEmail` | Verify an email address using a verification code previously sent by email (POST /v2/verified-resources/emails/verification-code/verify). |
| Verify Phone Number | `verifyPhoneNumber` | Verify a phone number using a verification code previously sent via SMS (POST /v2/verified-resources/phones/verification-code/verify). |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Booking Cancelled | `BOOKING_CANCELLED` | Fires when a booking is cancelled. |
| Booking Created | `BOOKING_CREATED` | Fires when a new booking is created. |
| Booking Location Updated | `BOOKING_LOCATION_UPDATED` | Fires when a booking's location is changed. |
| Booking No-Show Updated | `BOOKING_NO_SHOW_UPDATED` | Fires when an attendee or host no-show status changes. |
| Booking Paid | `BOOKING_PAID` | Fires when a booking payment succeeds. |
| Booking Payment Initiated | `BOOKING_PAYMENT_INITIATED` | Fires when payment for a booking is initiated. |
| Booking Reassigned | `BOOKING_REASSIGNED` | Fires when a round-robin team booking is reassigned to another host. |
| Booking Rejected | `BOOKING_REJECTED` | Fires when a pending booking is declined. |
| Booking Requested | `BOOKING_REQUESTED` | Fires when a booking requiring confirmation is requested. |
| Booking Rescheduled | `BOOKING_RESCHEDULED` | Fires when a booking is rescheduled. |
| Form Submitted | `FORM_SUBMITTED` | Fires when a routing form is submitted. |
| Form Submitted (No Event) | `FORM_SUBMITTED_NO_EVENT` | Fires when a routing form is submitted without booking an event. |
| Guest Cal Video No-Show | `AFTER_GUESTS_CAL_VIDEO_NO_SHOW` | Fires after the configured interval when a guest did not join the Cal Video meeting. |
| Host Cal Video No-Show | `AFTER_HOSTS_CAL_VIDEO_NO_SHOW` | Fires after the configured interval when the host did not join the Cal Video meeting. |
| Instant Meeting | `INSTANT_MEETING` | Fires when an instant meeting is booked. |
| Instant Meeting Accepted | `INSTANT_MEETING_ACCEPTED` | Fires when a host accepts an instant meeting. |
| Meeting Ended | `MEETING_ENDED` | Fires when a Cal Video meeting ends. |
| Meeting Started | `MEETING_STARTED` | Fires when a Cal Video meeting starts. |
| Out Of Office Created | `OOO_CREATED` | Fires when an out-of-office entry is created. |
| Recording Ready | `RECORDING_READY` | Fires when a Cal Video recording is ready. |
| Recording Transcription Generated | `RECORDING_TRANSCRIPTION_GENERATED` | Fires when a meeting transcript is generated. |
