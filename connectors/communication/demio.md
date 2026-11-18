---
description: "Demio is a webinar platform for live, automated, and on-demand virtual events."
hidden: true
---

# Demio

<img src="../../.gitbook/assets/connectors/demio.png" alt="Demio logo" width="64">

Demio is a webinar platform for live, automated, and on-demand virtual events. This connector covers the complete Demio public REST API v1: verifying API credentials through both the header and query-string authorization schemes, listing events filtered by upcoming, past, or automated, retrieving a single event together with its full series of sessions, retrieving an individual event session, registering a person for an event or a specific session and returning their unique join link, and pulling a session's participant report filtered by attendance status.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [demio.com](https://demio.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `demio` |

## Use it

Add Demio from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.demio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Event | `getEvent` | Get one Demio event (GET /event/{id}) with its registration URL, next date id, automated playback details and its dates. Errors: 403 for an id you may not read, 404 when no date matched. Docs: https://api-docs.demio.com/ |
| Get Event Session | `getEventSession` | Get one date (session) of a Demio event (GET /event/{id}/date/{date_id}): status, Unix timestamp, formatted datetime and IANA zone. An on-demand date is reported as status running with timestamp = now. Docs: https://api-docs.demio.com/ |
| List Events | `listEvents` | List the account's Demio events (GET /events), each with one representative date (date_id, status, timestamp, zone) and its registration URL. Optional type filter: upcoming, past, automated. Docs: https://api-docs.demio.com/ |
| List Session Participants | `listSessionParticipants` | List the participants of a Demio event date (GET /report/{date_id}/participants): everyone registered, their custom registration fields, whether they attended, and their status. Optional status filter. Docs: https://api-docs.demio.com/ |
| Register Attendee For Event | `registerAttendee` | Register a person for a Demio event date (PUT /event/register) and get their join link. Identify the event by Event ID or Registration URL; omit Date ID to use the next date. Returns 201 with hash and join_link; 400 lists payload problems. Docs: https://api-docs.demio.com/ |
| Register Attendee For Event (POST) | `registerAttendeePost` | Register a person for a Demio event date (POST /event/register, identical to the PUT variant for clients that cannot send PUT) and get their join link. Identify the event by Event ID or Registration URL; omit Date ID to use the next date. Returns 201 with hash and join_link; 400 lists payload problems. Docs: https://api-docs.demio.com/ |
| Verify API Credentials | `ping` | Verifies that the connected Demio API Key and API Secret are valid by calling the ping endpoint with the Api-Key and Api-Secret headers. Returns pong true when the credentials authenticate and the account is active. |
