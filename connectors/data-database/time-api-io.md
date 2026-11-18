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

| Action | Slug | What it does |
| --- | --- | --- |
| Check API Health | `checkHealth` | Check API Health. Returns 200 with an empty body when the service is up. Docs: https://timeapi.io/swagger/index.html (GET /api/health/check) |
| Get Current Time by Coordinates | `getCurrentTimeByCoordinate` | Gets the current time of a time zone by geo coordinates. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/coordinate) |
| Get Current Time by IP Address | `getCurrentTimeByIp` | Gets the current time of a time zone by IP address. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/ip) |
| Get Current Time by Time Zone | `getCurrentTimeByZone` | Gets the current time of a time zone. An unknown zone returns 400 'Invalid Timezone'. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/zone) |
| Get Current Unix Time | `getCurrentUnixTime` | Gets the current unix timestamp (seconds since 1970-01-01 UTC). Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/unix) |
| Get Current Unix Time (Microseconds) | `getCurrentUnixTimeUs` | Gets the current unix timestamp (microseconds since 1970-01-01 UTC). Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/unix_us) |
| Get Current Unix Time (Milliseconds) | `getCurrentUnixTimeMs` | Gets the current unix timestamp (milliseconds since 1970-01-01 UTC). Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/unix_ms) |
| Get Current Unix Time (Nanoseconds) | `getCurrentUnixTimeNs` | Gets the current unix timestamp (nanoseconds since 1970-01-01 UTC). Due to limitations in the OS clock resolution, the last 3 digits will often be zero. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/unix_ns) |
| Get Current UTC Time | `getCurrentUtcTime` | Gets the current UTC time. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/time/current/utc) |
| Get Time Zone Info | `getTimeZoneInfo` | Gets the timezone info and current time by IANA time zone name. Includes UTC offsets and the current DST period. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/timezone/zone) |

<details>

<summary>See 2 more actions</summary>

* **Get Time Zone Info by Coordinates** `getTimeZoneInfoByCoordinate`: Get the timezone info and current time by geo coordinates. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/timezone/coordinate)
* **List Available Time Zones** `listTimeZones`: Gets all the available IANA time zones. Docs: https://timeapi.io/swagger/index.html (GET /api/v1/timezone/availabletimezones)

</details>
