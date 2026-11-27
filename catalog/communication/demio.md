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

## Connect in Fastn

Your customers connect Demio from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Demio**.
2. Select **Connect** on the Demio card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Demio's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Event</td><td><code>getEvent</code></td><td>Get one Demio event with its registration URL, next date id, automated playback details and its dates. Errors: 403 for an id you may not read, 404 when no date matched. Docs: https://api-docs.demio.com/</td></tr><tr><td>Get Event Session</td><td><code>getEventSession</code></td><td>Get one date (session) of a Demio event: status, Unix timestamp, formatted datetime and IANA zone. An on-demand date is reported as status running with timestamp = now. Docs: https://api-docs.demio.com/</td></tr><tr><td>List Events</td><td><code>listEvents</code></td><td>List the account's Demio events, each with one representative date (date_id, status, timestamp, zone) and its registration URL. Optional type filter: upcoming, past, automated. Docs: https://api-docs.demio.com/</td></tr><tr><td>List Session Participants</td><td><code>listSessionParticipants</code></td><td>List the participants of a Demio event date: everyone registered, their custom registration fields, whether they attended, and their status. Optional status filter. Docs: https://api-docs.demio.com/</td></tr><tr><td>Register Attendee For Event</td><td><code>registerAttendee</code></td><td>Register a person for a Demio event date and get their join link. Identify the event by Event ID or Registration URL; omit Date ID to use the next date. Docs: https://api-docs.demio.com/</td></tr><tr><td>Register Attendee For Event (POST)</td><td><code>registerAttendeePost</code></td><td>Register a person for a Demio event date, identical to the PUT variant for clients that cannot send PUT) and get their join link. Identify the event by Event ID or Registration URL; omit Date ID to use the next date. Docs: https://api-docs.demio.com/</td></tr><tr><td>Verify API Credentials</td><td><code>ping</code></td><td>Verifies that the connected Demio API Key and API Secret are valid by calling the ping endpoint with the Api-Key and Api-Secret headers. Returns pong true when the credentials authenticate and the account is active.</td></tr></tbody></table>

