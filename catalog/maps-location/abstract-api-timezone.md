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

## Use it

Add AbstractAPI Timezone from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiTimezone.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Convert Time</td><td><code>convertTime</code></td><td>Converts a date and time at a base location into the corresponding date and time at a target location, returning timezone details for both. Converts the current time unless a base date and time is given.</td></tr><tr><td>Get Current Time</td><td><code>getCurrentTime</code></td><td>Returns the current date, time, and timezone details (name, abbreviation, GMT offset, daylight saving status, and coordinates) for a location given as a place name, latitude/longitude pair, or IP address.</td></tr></tbody></table>

## Events

AbstractAPI Timezone has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
