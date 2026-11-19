---
description: "TimeAPI.io is a free time and time zone API."
hidden: true
---

# TimeAPI.io

<img src="../../.gitbook/assets/connectors/lg/time-api-io.png" alt="TimeAPI.io logo">

TimeAPI.io is a free time and time zone API. Get the current time as Unix timestamps or in UTC, look up the current time for an IANA time zone, a latitude/longitude or an IP address, list all IANA time zones and get time zone details such as UTC offset and daylight saving periods. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [timeapi.io](https://timeapi.io) |
| **Authentication** | No authentication |
| **Slug** | `timeApiIo` |

## Use it

Add TimeAPI.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.timeApiIo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check API Health</td><td><code>checkHealth</code></td><td>Check API Health. Returns 200 with an empty body when the service is up. Docs: https://timeapi.io/swagger/index.html (GET /api/health/check)</td></tr><tr><td>Get Current Time by Coordinates</td><td><code>getCurrentTimeByCoordinate</code></td><td>Gets the current time of a time zone by geo coordinates. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/coordinate)</td></tr><tr><td>Get Current Time by IP Address</td><td><code>getCurrentTimeByIp</code></td><td>Gets the current time of a time zone by IP address. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/ip)</td></tr><tr><td>Get Current Time by Time Zone</td><td><code>getCurrentTimeByZone</code></td><td>Gets the current time of a time zone. An unknown zone returns 400 'Invalid Timezone'. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/zone)</td></tr><tr><td>Get Current Unix Time</td><td><code>getCurrentUnixTime</code></td><td>Gets the current unix timestamp (seconds since 1970-01-01 UTC). Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/unix)</td></tr><tr><td>Get Current Unix Time (Microseconds)</td><td><code>getCurrentUnixTimeUs</code></td><td>Gets the current unix timestamp (microseconds since 1970-01-01 UTC). Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/unix_us)</td></tr><tr><td>Get Current Unix Time (Milliseconds)</td><td><code>getCurrentUnixTimeMs</code></td><td>Gets the current unix timestamp (milliseconds since 1970-01-01 UTC). Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/unix_ms)</td></tr><tr><td>Get Current Unix Time (Nanoseconds)</td><td><code>getCurrentUnixTimeNs</code></td><td>Gets the current unix timestamp (nanoseconds since 1970-01-01 UTC). Due to limitations in the OS clock resolution, the last 3 digits will often be zero. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/unix_ns)</td></tr><tr><td>Get Current UTC Time</td><td><code>getCurrentUtcTime</code></td><td>Gets the current UTC time. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/utc)</td></tr><tr><td>Get Time Zone Info</td><td><code>getTimeZoneInfo</code></td><td>Gets the timezone info and current time by IANA time zone name. Includes UTC offsets and the current DST period. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/timezone/zone)</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Time Zone Info by Coordinates</td><td><code>getTimeZoneInfoByCoordinate</code></td><td>Get the timezone info and current time by geo coordinates. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/timezone/coordinate)</td></tr><tr><td>List Available Time Zones</td><td><code>listTimeZones</code></td><td>Gets all the available IANA time zones. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/timezone/availabletimezones)</td></tr></tbody></table>

</details>
