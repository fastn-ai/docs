---
description: "IPGeolocation.io provides real-time IP intelligence: IP geolocation for IPv4, IPv6 and domain names, IP security and threat signals, ASN and abuse-contact…"
---

# IPGeolocation.io

IPGeolocation.io provides real-time IP intelligence: IP geolocation for IPv4, IPv6 and domain names, IP security and threat signals, ASN and abuse-contact lookups, time zone and time-conversion data, astronomy (sun and moon) data, and user-agent parsing.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ipgeolocation.io](https://ipgeolocation.io) |
| **Authentication** | Credentials you enter |
| **Actions** | 29 |
| **Events** | 0 |
| **Slug** | `ipgeolocationIo` |

## Use it

Add IPGeolocation.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ipgeolocationIo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert Time Between Addresses | `convertTimeBetweenAddresses` | Converts a timestamp from the time zone of one free-text address to the time zone of another, for example from 'New York, USA' to 'Lahore, Pakistan'. Costs 1 credit per successful conversion. |
| Convert Time Between Coordinates | `convertTimeBetweenCoordinates` | Converts a timestamp from the time zone of one pair of geographic coordinates to the time zone of another and returns the converted time and the offset between them. Costs 1 credit per successful conversion. |
| Convert Time Between IATA Codes | `convertTimeBetweenIataCodes` | Converts a timestamp between the time zones of two airports identified by their three-letter IATA codes. Costs 1 credit per successful conversion. |
| Convert Time Between ICAO Codes | `convertTimeBetweenIcaoCodes` | Converts a timestamp between the time zones of two airports identified by their four-letter ICAO codes. Costs 1 credit per successful conversion. |
| Convert Time Between Time Zones | `convertTimeBetweenTimeZones` | Converts a timestamp from one IANA time zone to another and returns the converted time and the offset between the two zones. Costs 1 credit per successful conversion. |
| Convert Time Between UN/LOCODEs | `convertTimeBetweenUnLocodes` | Converts a timestamp between the time zones of two cities identified by their five-character UN/LOCODEs. Costs 1 credit per successful conversion. |
| Get ASN Details By AS Number | `getAsnDetailsByAsNumber` | Returns registration and routing details for an Autonomous System Number, including the owning organization, country, ASN type, allocation date and status, announced route counts, and optionally its peers, upstreams, downstreams, announced prefixes and raw WHOIS record. Costs 1 credit per successful lookup and requires a paid subscription. |
| Get ASN Details By IP Address | `getAsnDetailsByIpAddress` | Resolves an IPv4 or IPv6 address to its Autonomous System and returns the same registration and routing details as a lookup by AS number, including optional peers, upstreams, downstreams, announced prefixes and raw WHOIS record. Costs 1 credit per successful lookup and requires a paid subscription. |
| Get Astronomy By Address | `getAstronomyByAddress` | Returns sunrise, sunset, moonrise, moonset, twilight boundaries, moon phase and the current position of the sun and moon for a free-text address such as 'New York, USA'. Costs 1 credit per successful lookup. |
| Get Astronomy By Coordinates | `getAstronomyByCoordinates` | Returns sunrise, sunset, moonrise, moonset, twilight boundaries, moon phase and the current position of the sun and moon for a pair of geographic coordinates. Costs 1 credit per successful lookup. |
| Get Astronomy By IP Address | `getAstronomyByIpAddress` | Returns sunrise, sunset, moonrise, moonset, twilight boundaries, moon phase and the current position of the sun and moon for the location of an IPv4 or IPv6 address. Omit the IP address to use the public IP address the request originates from. Costs 1 credit per successful lookup. |
| Get Astronomy By Time Zone | `getAstronomyByTimeZone` | Returns astronomical event times for the caller's location expressed in a specific IANA time zone, so that sunrise, sunset and twilight timestamps are reported against that zone rather than local time. Costs 1 credit per successful lookup. |
| Get Astronomy Time Series | `getAstronomyTimeSeries` | Returns one set of astronomical values per day across a date range of up to 90 days, for a location given as coordinates, an address or an IP address. Costs 1 credit per successful request. |
| Get Bulk IP Geolocation | `getBulkIpGeolocation` | Looks up geolocation details for up to 50,000 IPv4 addresses, IPv6 addresses or domain names in a single request and returns one result object per submitted entry, in the order supplied. Credits are charged per valid entry; private, bogon and malformed addresses are not charged. |
| Get Bulk IP Security | `getBulkIpSecurity` | Returns threat intelligence for up to 50,000 IPv4 or IPv6 addresses in a single request, one result object per submitted address. Costs 2 credits per valid address and requires a paid subscription. |
| Get Caller IP Address | `getCallerIpAddress` | Returns the public IP address the request originates from. This is the only IPGeolocation.io endpoint that requires no authentication, and it consumes no credits. |
| Get IP Abuse Contact | `getIpAbuseContact` | Returns the abuse-handling contact registered for an IPv4 or IPv6 address, including the responsible organization, its postal address, abuse email addresses and phone numbers, so that security incidents can be reported to the right party. Costs 1 credit per successful lookup and requires a paid subscription. |
| Get IP Geolocation | `getIpGeolocation` | Looks up real-time geolocation, network, ASN, company, currency and time zone details for a single IPv4 address, IPv6 address or domain name. Omit the IP address to look up the caller's own public IP. Costs 1 credit per successful lookup, plus 2 credits if the security module is included and 1 credit if the abuse module is included. |
| Get IP Security | `getIpSecurity` | Returns threat intelligence for a single IPv4 or IPv6 address, including VPN, proxy, residential proxy, Tor, relay, bot, spam, known-attacker and cloud-provider signals with confidence scores and an overall threat score. Omit the IP address to assess the caller's own public IP. Costs 2 credits per successful lookup and requires a paid subscription. |
| Get Time Zone By Address | `getTimeZoneByAddress` | Resolves a free-text address, preferably a city address such as 'London, UK', to its time zone and returns the current date, time, daylight-saving details and the resolved location. Costs 1 credit per successful lookup. |
| Get Time Zone By Coordinates | `getTimeZoneByCoordinates` | Returns the time zone, current date and time and daylight-saving details for a pair of geographic coordinates, along with the resolved location. Costs 1 credit per successful lookup. |
| Get Time Zone By IATA Code | `getTimeZoneByIataCode` | Returns airport details and the time zone in force at the airport identified by a three-letter IATA code such as 'LHR'. Costs 1 credit per successful lookup. |
| Get Time Zone By ICAO Code | `getTimeZoneByIcaoCode` | Returns airport details and the time zone in force at the airport identified by a four-letter ICAO code such as 'KATL'. Costs 1 credit per successful lookup. |
| Get Time Zone By IP Address | `getTimeZoneByIpAddress` | Returns the time zone, current date and time and daylight-saving details for an IPv4 or IPv6 address, along with the geolocation resolved for it. Omit the IP address to use the public IP address the request originates from. Costs 1 credit per successful lookup. |
| Get Time Zone By Name | `getTimeZoneByName` | Returns the current date, time and daylight-saving details for an IANA time zone name such as 'America/Los_Angeles'. Costs 1 credit per successful lookup. |
| Get Time Zone By UN/LOCODE | `getTimeZoneByUnLocode` | Returns city details and the time zone in force at the location identified by a five-character UN/LOCODE such as 'DEBER'. Costs 1 credit per successful lookup. |
| Parse Bulk User Agent Strings | `parseBulkUserAgentStrings` | Parses up to 50,000 user-agent strings in a single request and returns one parsed result per string, in the order supplied. Costs 1 credit per user-agent string and requires a paid subscription. |
| Parse Custom User Agent String | `parseCustomUserAgentString` | Parses a user-agent string supplied in the request body into browser, device, layout engine and operating system details. Intended for server-side use where the string cannot be sent in the User-Agent header. Costs 1 credit per successful parse and requires a paid subscription. |
| Parse User Agent | `parseUserAgent` | Parses a user-agent string sent in the User-Agent request header into browser, device, layout engine and operating system details, and classifies robots, crawlers and malformed strings. Available on every plan and costs 1 credit per successful parse. |
