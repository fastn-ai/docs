---
description: "Sunrise Sunset gives sunrise and sunset times anywhere. Get sun times for a date or date range."
hidden: true
---

# Sunrise Sunset

<img src="../../.gitbook/assets/connectors/lg/sunrise-sunset.png" alt="Sunrise Sunset logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [sunrise-sunset.org](https://sunrise-sunset.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `sunriseSunset` |

## Setup

Sunrise Sunset needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Sunrise Sunset from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Sunrise Sunset**.
2. Select **Connect** on the Sunrise Sunset card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Sunrise Sunset needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Sunrise Sunset's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Sun Times</td><td><code>getSunTimes</code></td><td>Get sunrise, sunset, twilights, golden and blue hour, solar position and moon data for one place and day Times are in the place's local timezone by default. Attribution required: show a visible link to sunrise-sunset.org where the data is shown. Docs: https://sunrise-sunset.org/api</td></tr><tr><td>Get Sun Times (v1)</td><td><code>getSunTimesV1</code></td><td>Get sunrise, sunset, solar noon, day length and twilight times from the original v1 endpoint Always answers HTTP 200; check the status field (OK, INVALID_REQUEST, INVALID_DATE, INVALID_TZID, UNKNOWN_ERROR). Times are UTC unless tzid is set. Version 1 is kept unchanged for existing users (times slightly less accurate than v2; use Get Sun Times for new work). Docs: https://sunrise-sunset.org/api/v1</td></tr><tr><td>Get Sun Times for Date Range</td><td><code>getSunTimesForDateRange</code></td><td>Get sun and moon times for one place for every day in a date range of up to 366 days in a single request with date_start and date_end). Days that never happened locally are left out. Attribution required: show a visible link to sunrise-sunset.org where the data is shown. Docs: https://sunrise-sunset.org/api</td></tr></tbody></table>

