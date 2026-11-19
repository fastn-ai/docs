---
description: "Demio is a webinar platform. List events and sessions, read session participants, and register attendees for events."
hidden: true
---

# Demio

<img src="../../.gitbook/assets/connectors/lg/demio.png" alt="Demio logo">

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [demio.com](https://demio.com) |
| **Authentication** | API key and secret |
| **Slug** | `demio` |

## Setup

Your customers enter their API key and secret for Demio when they connect. Nothing else needs setting up.

## Use it

Add Demio from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.demio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Event</td><td><code>getEvent</code></td><td>Get one Demio event with its registration URL, next date id, automated playback details and its dates. Errors: 403 for an id you may not read, 404 when no date matched. Docs: https://api-docs.demio.com/</td></tr><tr><td>Get Event Session</td><td><code>getEventSession</code></td><td>Get one date (session) of a Demio event: status, Unix timestamp, formatted datetime and IANA zone. An on-demand date is reported as status running with timestamp = now. Docs: https://api-docs.demio.com/</td></tr><tr><td>List Events</td><td><code>listEvents</code></td><td>List the account's Demio events, each with one representative date (date_id, status, timestamp, zone) and its registration URL. Optional type filter: upcoming, past, automated. Docs: https://api-docs.demio.com/</td></tr><tr><td>List Session Participants</td><td><code>listSessionParticipants</code></td><td>List the participants of a Demio event date: everyone registered, their custom registration fields, whether they attended, and their status. Optional status filter. Docs: https://api-docs.demio.com/</td></tr><tr><td>Register Attendee For Event</td><td><code>registerAttendee</code></td><td>Register a person for a Demio event date and get their join link. Identify the event by Event ID or Registration URL; omit Date ID to use the next date. Docs: https://api-docs.demio.com/</td></tr><tr><td>Register Attendee For Event (POST)</td><td><code>registerAttendeePost</code></td><td>Register a person for a Demio event date, identical to the PUT variant for clients that cannot send PUT) and get their join link. Identify the event by Event ID or Registration URL; omit Date ID to use the next date. Docs: https://api-docs.demio.com/</td></tr><tr><td>Verify API Credentials</td><td><code>ping</code></td><td>Verifies that the connected Demio API Key and API Secret are valid by calling the ping endpoint with the Api-Key and Api-Secret headers. Returns pong true when the credentials authenticate and the account is active.</td></tr></tbody></table>

## Events

Demio has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
