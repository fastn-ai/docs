---
description: "Zoho Meeting is Zoho's online meeting and webinar platform."
hidden: true
---

# Zoho Meeting

<img src="../../.gitbook/assets/connectors/zoho-meeting.jpg" alt="Zoho Meeting logo" width="64">

Zoho Meeting is Zoho's online meeting and webinar platform. This connector wraps the Zoho Meeting REST API v2 (https://meeting.zoho.com/api/v2): create, list, fetch, edit and delete meetings and webinars, register attendees in bulk for a webinar, pull meeting participant and webinar attendee reports, list session recordings, and read organization users. All operations are scoped to a Zoho Meeting organization ID (zsoid).

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [meeting.zoho.com](https://meeting.zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `zohoMeeting` |

## Use it

Add Zoho Meeting from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoMeeting.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Meeting | `createMeeting` | Schedules a new Zoho Meeting by supplying its topic, agenda, presenter, start time and duration. Returns the meeting key along with the join link and start link, and emails an invitation to any participants listed. |
| Create Webinar | `createWebinar` | Creates a new Zoho Meeting webinar with a topic, description, presenter, start time, duration and time zone. Returns the webinar key along with the registration link and the presenter's start link. |
| Delete Meeting | `deleteMeeting` | Deletes a scheduled Zoho Meeting. Once deleted the meeting can no longer be hosted and its join link stops working. Returns an empty 204 response on success. |
| Delete Webinar | `deleteWebinar` | Deletes a Zoho Meeting webinar. Once deleted the webinar can no longer be hosted and its registration link stops working. Returns an empty 204 response on success. |
| Get Current User | `getCurrentUser` | Fetches the profile of the currently authenticated Zoho Meeting user, including their organization ID. Call this first: every other action in this connector needs the organization ID it returns. |
| Get Meeting | `getMeeting` | Fetches the full details of a single Zoho Meeting by its meeting key, including topic, agenda, presenter, schedule, join link, start link and embed URL. |
| Get Meeting Participant Report | `getMeetingParticipantReport` | Fetches a detailed participation report for a Zoho Meeting, listing each attendee with their email, role, join and leave times, time spent in the meeting and the client they joined from. |
| Get User | `getUser` | Fetches the details of a single user in a Zoho Meeting organization, including their name, role, organization and meeting and webinar license editions. Only an organization administrator may call this. |
| Get Webinar | `getWebinar` | Fetches the full details of a single Zoho Meeting webinar by its webinar key, including the topic, organizer, schedule, registration link, start link, registration and attendee counts and whether the session has started or already finished. |
| Get Webinar Attendee Report | `getWebinarAttendeeReport` | Fetches an engagement report for a Zoho Meeting webinar, listing each attendee with their name and email plus the questions they asked and the poll answers they submitted during the session. |

<details>

<summary>See 7 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Meetings | `listMeetings` | Lists the meetings in a Zoho Meeting organization, filtered to all, past, today's or upcoming meetings. Each entry carries the meeting key, topic, presenter, schedule and join link, plus the total count of matching meetings. |
| List Recordings | `listRecordings` | Lists every meeting and webinar recording in a Zoho Meeting organization, with each recording's topic, duration, file size, upload status and the play, share and download URLs, plus whether a transcript or AI summary has been generated. |
| List Users | `listUsers` | Lists all users in a Zoho Meeting organization with their names, email addresses, roles and meeting and webinar license editions. Only an organization administrator may call this. Use it to obtain the organization ID and the Zoho user IDs needed as presenters elsewhere in this connector. |
| List Webinars | `listWebinars` | Lists the webinars in a Zoho Meeting organization, filtered to all, past, today's or upcoming webinars. Each entry carries the webinar key, topic, presenter, schedule, registration link and registration and attendee counts. |
| Register Webinar Attendees | `registerWebinarAttendees` | Registers multiple attendees for a Zoho Meeting webinar in one call. Returns a personalised join link per registrant along with success and failure counts. Setting Send Mail to true emails each registrant their join link. |
| Update Meeting | `updateMeeting` | Edits an existing Zoho Meeting, changing its topic, agenda, presenter, start time, duration, time zone or participant list. Only the fields supplied are altered. |
| Update Webinar | `updateWebinar` | Edits an existing Zoho Meeting webinar, changing its title, description, presenter, start time, duration or time zone. Registrants are notified of the changes by email. |

</details>
