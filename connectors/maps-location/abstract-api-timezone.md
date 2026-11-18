---
description: "AbstractAPI Time, Date, and Timezone returns the current time and timezone for a location name, coordinates, or IP address, and converts a date and time from…"
---

# AbstractAPI Timezone

AbstractAPI Time, Date, and Timezone returns the current time and timezone for a location name, coordinates, or IP address, and converts a date and time from one location to another.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 2 |
| **Events** | 0 |
| **Slug** | `abstractApiTimezone` |

## Use it

Add AbstractAPI Timezone from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiTimezone.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert Time | `convertTime` | Converts a date and time at a base location into the corresponding date and time at a target location, returning timezone details for both. Converts the current time unless a base date and time is given. |
| Get Current Time | `getCurrentTime` | Returns the current date, time, and timezone details (name, abbreviation, GMT offset, daylight saving status, and coordinates) for a location given as a place name, latitude/longitude pair, or IP address. |
