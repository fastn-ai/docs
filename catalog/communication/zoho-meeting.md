---
description: "Zoho Meeting hosts online meetings and webinars. Create, update and delete meetings and webinars, and read attendee reports."
hidden: true
---

# Zoho Meeting

<img src="../../.gitbook/assets/connectors/lg/zoho-meeting.png" alt="Zoho Meeting logo">

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [meeting.zoho.com](https://meeting.zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `zohoMeeting` |

## Setup

Your customers sign in to Zoho Meeting through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Zoho Meeting from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoMeeting.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Meeting</td><td><code>createMeeting</code></td><td>Schedules a new Zoho Meeting by supplying its topic, agenda, presenter, start time and duration. Returns the meeting key along with the join link and start link, and emails an invitation to any participants listed.</td></tr><tr><td>Create Webinar</td><td><code>createWebinar</code></td><td>Creates a new Zoho Meeting webinar with a topic, description, presenter, start time, duration and time zone. Returns the webinar key along with the registration link and the presenter's start link.</td></tr><tr><td>Delete Meeting</td><td><code>deleteMeeting</code></td><td>Deletes a scheduled Zoho Meeting. Once deleted the meeting can no longer be hosted and its join link stops working. Returns an empty 204 response on success.</td></tr><tr><td>Delete Webinar</td><td><code>deleteWebinar</code></td><td>Deletes a Zoho Meeting webinar. Once deleted the webinar can no longer be hosted and its registration link stops working. Returns an empty 204 response on success.</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Fetches the profile of the currently authenticated Zoho Meeting user, including their organization ID. Call this first: every other action in this connector needs the organization ID it returns.</td></tr><tr><td>Get Meeting</td><td><code>getMeeting</code></td><td>Fetches the full details of a single Zoho Meeting by its meeting key, including topic, agenda, presenter, schedule, join link, start link and embed URL.</td></tr><tr><td>Get Meeting Participant Report</td><td><code>getMeetingParticipantReport</code></td><td>Fetches a detailed participation report for a Zoho Meeting, listing each attendee with their email, role, join and leave times, time spent in the meeting and the client they joined from.</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Fetches the details of a single user in a Zoho Meeting organization, including their name, role, organization and meeting and webinar license editions. Only an organization administrator may call this.</td></tr><tr><td>Get Webinar</td><td><code>getWebinar</code></td><td>Fetches the full details of a single Zoho Meeting webinar by its webinar key, including the topic, organizer, schedule, registration link, start link, registration and attendee counts and whether the session has started or already finished.</td></tr><tr><td>Get Webinar Attendee Report</td><td><code>getWebinarAttendeeReport</code></td><td>Fetches an engagement report for a Zoho Meeting webinar, listing each attendee with their name and email plus the questions they asked and the poll answers they submitted during the session.</td></tr></tbody></table>

<details>

<summary>View 7 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Meetings</td><td><code>listMeetings</code></td><td>Lists the meetings in a Zoho Meeting organization, filtered to all, past, today's or upcoming meetings. Each entry carries the meeting key, topic, presenter, schedule and join link, plus the total count of matching meetings.</td></tr><tr><td>List Recordings</td><td><code>listRecordings</code></td><td>Lists every meeting and webinar recording in a Zoho Meeting organization, with each recording's topic, duration, file size, upload status and the play, share and download URLs, plus whether a transcript or AI summary has been generated.</td></tr><tr><td>List Users</td><td><code>listUsers</code></td><td>Lists all users in a Zoho Meeting organization with their names, email addresses, roles and meeting and webinar license editions. Only an organization administrator may call this. Use it to obtain the organization ID and the Zoho user IDs needed as presenters elsewhere in this connector.</td></tr><tr><td>List Webinars</td><td><code>listWebinars</code></td><td>Lists the webinars in a Zoho Meeting organization, filtered to all, past, today's or upcoming webinars. Each entry carries the webinar key, topic, presenter, schedule, registration link and registration and attendee counts.</td></tr><tr><td>Register Webinar Attendees</td><td><code>registerWebinarAttendees</code></td><td>Registers multiple attendees for a Zoho Meeting webinar in one call. Returns a personalised join link per registrant along with success and failure counts. Setting Send Mail to true emails each registrant their join link.</td></tr><tr><td>Update Meeting</td><td><code>updateMeeting</code></td><td>Edits an existing Zoho Meeting, changing its topic, agenda, presenter, start time, duration, time zone or participant list. Only the fields supplied are altered.</td></tr><tr><td>Update Webinar</td><td><code>updateWebinar</code></td><td>Edits an existing Zoho Meeting webinar, changing its title, description, presenter, start time, duration or time zone. Registrants are notified of the changes by email.</td></tr></tbody></table>

</details>

## Events

Zoho Meeting has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
