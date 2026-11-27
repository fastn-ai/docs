---
description: "AbstractAPI Timezone gives the time and timezone for a place. Get the current time for a location and convert times between locations."
hidden: true
---

# AbstractAPI Timezone

<img src="../../.gitbook/assets/connectors/lg/abstract-api-timezone.png" alt="AbstractAPI Timezone logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | API key |
| **Slug** | `abstractApiTimezone` |

## Setup

Your customers enter their API key for AbstractAPI Timezone when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect AbstractAPI Timezone from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AbstractAPI Timezone**.
2. Select **Connect** on the AbstractAPI Timezone card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AbstractAPI Timezone's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Convert Time</td><td><code>convertTime</code></td><td>Converts a date and time at a base location into the corresponding date and time at a target location, returning timezone details for both. Converts the current time unless a base date and time is given.</td></tr><tr><td>Get Current Time</td><td><code>getCurrentTime</code></td><td>Returns the current date, time, and timezone details (name, abbreviation, GMT offset, daylight saving status, and coordinates) for a location given as a place name, latitude/longitude pair, or IP address.</td></tr></tbody></table>

