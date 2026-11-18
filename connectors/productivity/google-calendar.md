---
description: "Google Calendar API v3 connector — manage calendars, events, ACLs, free/busy queries, and push notification channels."
---

# Google Calendar

Google Calendar API v3 connector — manage calendars, events, ACLs, free/busy queries, and push notification channels.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [calendar.google.com](https://calendar.google.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 32 |
| **Events** | 3 |
| **Slug** | `googleCalendar` |

## Use it

Add Google Calendar from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCalendar.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Calendar To List | `insertCalendarListEntry` | Subscribes the signed-in user to an existing calendar by inserting it into their calendar list (Google Calendar calendarList.insert), e.g. a public holiday calendar or a colleague's shared calendar. Only changes the user's own list, not the calendar itself. Google scope: calendar.calendarlist (or calendar). Undo with Remove Calendar From List. Returns the new CalendarListEntry. |
| Create ACL Rule | `createAclRule` | Grant a user access to a calendar by creating an ACL rule. |
| Create Calendar | `createCalendar` | Create a new secondary calendar. |
| Create Event | `createEvent` | Create a new event on a calendar. |
| Create Event With Attendees | `createEventAdvanced` | Create a calendar event with the full Google Events.insert body, including attendees, Google Meet conferencing, recurrence, reminders and all-day dates — the fields the simpler Create Event action cannot express. Use Create Event for a plain timed event; use this when you need guests or any structured field. start and end are objects: pass dateTime (ISO 8601, with timeZone) for a timed event, or date (YYYY-MM-DD) for an all-day event, never both. WARNING: adding attendees makes Google email them unless sendUpdates is 'none'. sendUpdates defaults to 'none' here so nobody is notified by accident; set 'all' deliberately to send invitations. For a Google Meet link, set conferenceDataVersion to 1 and pass conferenceData.createRequest with a unique requestId. |
| Delete ACL Rule | `deleteAclRule` | Delete an ACL rule from a calendar. |
| Delete Calendar | `deleteCalendar` | Delete a secondary calendar. Cannot delete the primary calendar. |
| Delete Event | `deleteEvent` | Delete an event from a calendar. |
| Get ACL Rule | `getAclRule` | Get a specific ACL rule for a calendar. |
| Get Calendar | `getCalendar` | Get metadata for a calendar by ID. |
| Get Colors | `getColors` | Get the color IDs and hex codes available for calendars and events. |
| Get Event | `getEvent` | Get a single event by ID from a calendar. |
| Get Event Instances | `getEventInstances` | List all instances of a recurring event. |
| Get Setting | `getSetting` | Get a specific user setting (e.g. 'timezone', 'dateFieldOrder', 'format24HourTime'). |
| List ACL Rules | `listAclRules` | List access control rules for a calendar. |
| List Calendars | `listCalendars` | List all calendars in the authenticated user's calendar list. |
| List Events | `listEvents` | List events on a calendar. Use 'primary' as calendarId for the primary calendar. |
| List Settings | `listSettings` | List all user settings for the authenticated Google Calendar account. |
| Move Event | `moveEvent` | Move an event from one calendar to another. |
| Patch Event | `patchEvent` | Partially update an event. Only provided fields are changed. |
| Patch Event (advanced) | `patchEventAdvanced` | Change only the fields you send (start/end, attendees, title...). Fields you leave out keep their value, so attendees stay on a reschedule. Use this to reschedule; Update Event (PUT) replaces the whole event and clears attendees. sendUpdates is not sent unless set, so Google emails nobody by default. |
| Query Free/Busy | `queryFreeBusy` | Query free/busy information for a set of calendars and/or groups. |
| Query Free/Busy (multiple calendars) | `queryFreeBusyMultiple` | Free/busy for several calendars in one call. Pass items as a list of {id} (calendar ids or emails, e.g. [{"id":"primary"},{"id":"team@example.com"}]). Returns calendars keyed by id with their busy periods. For one calendar, Query Free/Busy also works. |
| Quick Add Event | `quickAddEvent` | Create an event from a natural-language text string (e.g. 'Lunch tomorrow at noon'). |
| Remove Calendar From List | `deleteCalendarListEntry` | Unsubscribes the signed-in user from a calendar by removing it from their calendar list (Google Calendar calendarList.delete). The calendar and its events are not deleted; it just disappears from the user's list. Google scope: calendar.calendarlist (or calendar). Returns an empty body on success. |
| Stop Watch Channel | `stopWatchChannel` | Stop receiving push notifications for a watch channel. |
| Update ACL Rule | `updateAclRule` | Update the role of an existing ACL rule. |
| Update Calendar | `updateCalendar` | Update metadata for a calendar. |
| Update Calendar List Entry | `patchCalendarListEntry` | Changes how a calendar appears in the signed-in user's calendar list (Google Calendar calendarList.patch): display name override, color, hidden/selected flags and default reminders. Partial update: only the fields you send change. Does not modify the calendar itself. Google scope: calendar.calendarlist (or calendar). Returns the updated CalendarListEntry. |
| Update Event | `updateEvent` | Replace an event (full update). Fields you leave out are cleared, including guests: send the full attendees list to keep them. To change only some fields (e.g. reschedule) use Patch Event (advanced). sendUpdates is not sent unless set. |
| Watch Calendar Events | `watchCalendarEvents` | Register a push notification channel to watch for changes on a calendar's events. |
| Watch Settings | `watchSettings` | Registers a push notification channel that calls your HTTPS webhook whenever the signed-in user's Calendar settings change (Google Calendar settings.watch). Google scope: calendar.settings or calendar.settings.readonly (calendar/calendar.readonly also work). Stop the channel with Stop Watch Channel using the returned id and resourceId. Returns the Channel with id, resourceId and expiration. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Calendar Event Created or Updated | `exists` | A resource on the watched calendar was created or changed. X-Goog-Resource-State: exists. Google sends no event body - call listEvents with a syncToken or updatedMin to fetch what changed. |
| Calendar Event Deleted | `not_exists` | A resource on the watched calendar no longer exists (deleted). X-Goog-Resource-State: not_exists. |
| Channel Sync | `sync` | Sent once immediately after a watch channel is created, confirming the subscription is live. X-Goog-Resource-State: sync. Carries no calendar data. |
