---
description: "Microsoft Outlook Calendar via Microsoft Graph v1.0 (https://graph.microsoft.com/v1.0)."
hidden: true
---

# Microsoft Outlook Calendar

<img src="../../.gitbook/assets/connectors/microsoft-outlook-calendar.svg" alt="Microsoft Outlook Calendar logo" width="64">

Microsoft Outlook Calendar via Microsoft Graph v1.0 (https://graph.microsoft.com/v1.0). Calendars and calendar groups, calendar sharing permissions, events (create, read, update, delete, permanent delete), calendar view and recurring-event instances, delta sync, meeting responses (accept, tentatively accept, decline, cancel, forward), event reminders (reminder view, snooze, dismiss), event attachments, free/busy schedule lookup and meeting time suggestions.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [graph.microsoft.com](https://graph.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `microsoftOutlookCalendar` |

## Use it

Add Microsoft Outlook Calendar from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.microsoftOutlookCalendar.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Event | `acceptEvent` | Accept a meeting invitation in the signed-in user's calendar, optionally sending a comment back to the organiser. |
| Add Event Attachment | `addEventAttachment` | Add a file or reference attachment to an event in the signed-in user's calendar. Use this for files under 3 MB; larger files require an upload session. |
| Cancel Event | `cancelEvent` | Cancel a meeting the signed-in user organised and send a cancellation message to every attendee. The event stays in the organiser's calendar marked as cancelled. |
| Create Calendar | `createCalendar` | Create a new calendar in the signed-in user's default calendar group. Returns the created calendar including its identifier. |
| Create Calendar Event | `createCalendarEvent` | Create an event in a specific calendar of the signed-in user. When attendees are supplied, Microsoft Graph sends meeting invitations to all of them automatically. |
| Create Calendar Group | `createCalendarGroup` | Create a new calendar group in the signed-in user's mailbox so that calendars can be organised under it. |
| Create Calendar In Group | `createCalendarInGroup` | Create a new calendar inside a specific calendar group in the signed-in user's mailbox. |
| Create Calendar Permission | `createCalendarPermission` | Share the signed-in user's default calendar with another person by creating a calendar permission at the requested access level. |
| Create Event | `createEvent` | Create an event in the signed-in user's default calendar. When attendees are supplied, Microsoft Graph sends meeting invitations to all of them automatically. |
| Decline Event | `declineEvent` | Decline a meeting invitation in the signed-in user's calendar, optionally proposing an alternative time and sending a comment to the organiser. |

<details>

<summary>See 36 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Calendar | `deleteCalendar` | Delete one of the signed-in user's calendars and move it to the Deleted Items folder. Returns an empty body on success. |
| Delete Calendar Group | `deleteCalendarGroup` | Delete a calendar group from the signed-in user's mailbox. Returns an empty body on success. |
| Delete Calendar Permission | `deleteCalendarPermission` | Stop sharing the signed-in user's default calendar with a person by removing their calendar permission. |
| Delete Event | `deleteEvent` | Delete an event from the signed-in user's mailbox and move it to the Deleted Items folder. If the caller is the organiser of a meeting, attendees receive a cancellation. |
| Delete Event Attachment | `deleteEventAttachment` | Remove an attachment from an event in the signed-in user's calendar. |
| Dismiss Event Reminder | `dismissEventReminder` | Dismiss the reminder for an event in the signed-in user's calendar so it no longer alerts. |
| Find Meeting Times | `findMeetingTimes` | Suggest meeting times and locations for the signed-in user based on the availability of the organiser and attendees together with any time and location constraints supplied. |
| Forward Event | `forwardEvent` | Forward a meeting request to additional recipients. Either the organiser or an attendee of the meeting may forward it. |
| Get Calendar | `getCalendar` | Retrieve the properties and relationships of a specific calendar owned by the signed-in user, identified by its calendar ID. |
| Get Calendar Group | `getCalendarGroup` | Retrieve the properties of a single calendar group in the signed-in user's mailbox. |
| Get Calendar Permission | `getCalendarPermission` | Retrieve a single sharing permission on the signed-in user's default calendar by its permission identifier. |
| Get Calendar View Delta | `getCalendarViewDelta` | Track incremental changes to events in a date range of the signed-in user's primary calendar. The first call returns the current set with a delta token; subsequent calls with that token return only what has been added, changed or removed. Graph always returns the full event properties here ($select, $expand, $filter, $orderby and $search are not supported on calendarView delta). |
| Get Default Calendar | `getDefaultCalendar` | Retrieve the properties of the signed-in user's default calendar, the calendar new events are created in unless another calendar is specified. |
| Get Event | `getEvent` | Retrieve the properties and relationships of a single event in the signed-in user's mailbox by its event identifier. |
| Get Event Attachment | `getEventAttachment` | Retrieve a single attachment on an event in the signed-in user's calendar, including the base64-encoded file contents for a file attachment. |
| Get Schedule | `getSchedule` | Get the free and busy availability of a set of users, distribution lists or room and equipment resources over a time period, returned as an availability view string plus the individual schedule items. |
| List Calendar Events | `listCalendarEvents` | Retrieve the events held in one specific calendar of the signed-in user. The list contains single-instance meetings and recurring series masters. |
| List Calendar Groups | `listCalendarGroups` | Retrieve the calendar groups in the signed-in user's mailbox. Calendar groups organise user calendars into folders in Outlook. |
| List Calendar Permissions | `listCalendarPermissions` | Retrieve the sharing permissions on the signed-in user's default calendar, showing who the calendar is shared with and at what level. |
| List Calendar View | `listCalendarView` | Retrieve the occurrences, exceptions and single instances of events in the signed-in user's default calendar within a date and time range. Unlike List Events, recurring series are expanded into individual occurrences. |
| List Calendar View For Calendar | `listCalendarViewForCalendar` | Retrieve the occurrences, exceptions and single instances of events within a date and time range from one specific calendar of the signed-in user. |
| List Calendars | `listCalendars` | Retrieve all calendars belonging to the signed-in user, across every calendar group. Returns a collection of calendar objects. |
| List Calendars In Group | `listCalendarsInGroup` | Retrieve the calendars that belong to a specific calendar group in the signed-in user's mailbox. |
| List Event Attachments | `listEventAttachments` | Retrieve the file, item and reference attachments on an event in the signed-in user's calendar. Graph returns all attachments of the event in one response (paging with $top/$skip is not applied on this route). |
| List Event Instances | `listEventInstances` | Retrieve the occurrences of a recurring series master within a date and time range. Occurrences cancelled from the series are not returned. |
| List Events | `listEvents` | Retrieve the events in the signed-in user's mailbox. The list contains single-instance meetings and recurring series masters, but not the expanded occurrences of a series; use List Calendar View or List Event Instances for those. |
| List Reminder View | `listReminderView` | Retrieve the event reminders that fire within a date and time range in the signed-in user's default calendar, including the reminder fire time and the event it belongs to. |
| Permanently Delete Calendar | `permanentlyDeleteCalendar` | Permanently delete a calendar folder and remove it from the mailbox, placing it in the purges folder of the recoverable items folder. This action is not reversible from the user interface. |
| Permanently Delete Event | `permanentlyDeleteEvent` | Permanently delete an event and place it in the purges folder of the recoverable items folder in the mailbox. The event can no longer be recovered by the user. |
| Snooze Event Reminder | `snoozeEventReminder` | Postpone the reminder for an event in the signed-in user's calendar until a new date and time. |
| Tentatively Accept Event | `tentativelyAcceptEvent` | Tentatively accept a meeting invitation in the signed-in user's calendar, optionally proposing an alternative time and sending a comment to the organiser. |
| Update Calendar | `updateCalendar` | Update the name, colour or default flag of one of the signed-in user's calendars. Only the properties supplied are changed. |
| Update Calendar Group | `updateCalendarGroup` | Rename an existing calendar group in the signed-in user's mailbox. |
| Update Calendar Permission | `updateCalendarPermission` | Change the access level of an existing share recipient or delegate on the signed-in user's default calendar. |
| Update Default Calendar | `updateDefaultCalendar` | Update the signed-in user's default calendar. Only the colour can be changed: Exchange rejects a rename of the default calendar with 400 ErrorInvalidRequest "The default calendar cannot be renamed." |
| Update Event | `updateEvent` | Update an existing event in the signed-in user's mailbox. Only the properties supplied are changed; everything omitted keeps its current value. |

</details>
