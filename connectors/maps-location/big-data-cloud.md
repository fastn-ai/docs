---
description: "BigDataCloud provides location intelligence APIs."
hidden: true
---

# BigDataCloud

<img src="../../.gitbook/assets/connectors/lg/big-data-cloud.png" alt="BigDataCloud logo">

BigDataCloud provides location intelligence APIs. This connector covers the server-side BigDataCloud REST APIs on api-bdc.net: IP geolocation with confidence areas and hazard reports, country, time zone and user-agent lookups, user risk, reverse geocoding, phone number and email verification, and network engineering data (ASN details and peers, BGP prefixes, networks by CIDR, IPv4 address space, Tor exit nodes, ASN rankings), plus GraphQL queries for each API package.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [bigdatacloud.com](https://bigdatacloud.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `bigDataCloud` |

## Use it

Add BigDataCloud from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bigDataCloud.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Roaming Status | `checkRoamingStatus` | Detects whether a device is roaming by comparing the supplied GPS coordinates with the country resolved from the calling IP address. Returns true when the two disagree. This is a free BigDataCloud endpoint that needs no API key and evaluates the country of whichever machine issues the request. |
| Get ASN Info | `getAsnInfo` | Returns short information about an Autonomous System: organisation, registry, registered country, registration dates, announced IPv4 and IPv6 prefix counts and its global rank. |
| Get ASN Info Extended | `getAsnInfoExtended` | Returns extended information about an Autonomous System: registration details, prefix counts, rank, the networks it receives traffic from and transits traffic to, and the confidence area of its most active operating region. |
| Get Client Info | `getClientInfo` | Returns the caller's public IP address together with parsed user-agent details - browser family and version, operating system and device type - plus basic proxy detection from the X-Forwarded-For header. This is a free BigDataCloud endpoint that needs no API key. |
| Get Client IP Address | `getClientIpAddress` | Returns the public IP address of the caller together with basic proxy detection based on the X-Forwarded-For header. This is a free BigDataCloud endpoint that needs no API key and reports the address of whichever machine issues the request. |
| Get Country By IP | `getCountryByIp` | Returns country-level information for an IPv4 or IPv6 address: ISO names and codes, official languages, currency, calling code, flag, UN region and World Bank income level. |
| Get Country Info | `getCountryInfo` | Returns detailed information about a country identified by its ISO 3166-1 Alpha-2, Alpha-3 or numeric code: ISO names, official languages, currency, calling code, flag, UN region and World Bank region and income level. |
| Get IP Geolocation | `getIpGeolocation` | Resolves an IPv4 or IPv6 address to its geographic location using BigDataCloud's patented router-topology geolocation, returning country, locality, coordinates, time zone and the announcing network. Omit the IP address to geolocate the caller's own address. |
| Get IP Geolocation Full | `getIpGeolocationFull` | Returns the complete IP intelligence record for an address: geolocation, confidence area, announcing network, a plain-language security threat summary and the full Hazard Report of reactive and proactive risk signals. This is the most comprehensive IP Geolocation endpoint and consumes one request for all of it. |
| Get IP Geolocation With Confidence Area | `getIpGeolocationWithConfidence` | Returns the same geolocation data as Get IP Geolocation plus a confidence rating and a confidence area polygon estimating where else the IP address may be found when it is dynamically assigned or shared. Useful for fraud detection, risk scoring and compliance checks. |

<details>

<summary>See 25 more actions</summary>

* **Get IP Hazard Report** `getIpHazardReport`: Returns a risk assessment for an IPv4 or IPv6 address combining reactive signals (Tor, VPN and proxy detection, Spamhaus and other blocklists) with proactive indicators such as hosting likelihood, hosting ASN, cellular network and iCloud Private Relay.
* **Get IPv4 Address Space Stats** `getIpv4AddressSpaceStats`: Returns a consolidated status report for the entire IPv4 address space, combining regional registry allocation data with live BGP announcement status. BGP data is refreshed every two hours.
* **Get Network By IP** `getNetworkByIp`: Returns the active network an IPv4 or IPv6 address belongs to: registry, registration status, BGP prefix, address range, total addresses and the carrier Autonomous Systems announcing it, with their upstream peers.
* **Get Time Zone By IP** `getTimeZoneByIp`: Returns the IANA time zone for an IPv4 or IPv6 address with its display name, current UTC offset, daylight saving status and local time, optionally converting a supplied UTC reference time.
* **Get Time Zone By Location** `getTimeZoneByLocation`: Returns the IANA time zone for latitude and longitude coordinates with its display name, current UTC offset, daylight saving status and local time, optionally converting a supplied UTC reference time.
* **Get Time Zone Info** `getTimeZoneInfo`: Returns information about an IANA time zone: display name, effective zone names, current UTC offset, daylight saving status and the local time, optionally converting a supplied UTC reference time.
* **Get User Risk** `getUserRisk`: Returns a simple risk level (Low, Moderate or High) for an IPv4 or IPv6 address, indicating how likely the traffic is to come from a genuine human user, for example to decide whether to show a captcha.
* **List ASN Rankings** `listAsnRankings`: Returns a paginated list of Autonomous Systems ranked by the number of IPv4 addresses they announce on BGP, sortable by rank, ASN, organisation or country.
* **List ASN Receiving From** `listAsnReceivingFrom`: Returns a paginated list of the Autonomous Systems a given ASN currently receives traffic from (its upstream and peering relationships), along with the ASN summary.
* **List ASN Transit To** `listAsnTransitTo`: Returns a paginated list of the Autonomous Systems a given ASN currently transits traffic to (its downstream routing relationships), along with the ASN summary.
* **List BGP Active Prefixes** `listBgpActivePrefixes`: Returns a paginated list of IPv4 or IPv6 prefixes currently announced on BGP, optionally limited to one ASN or to bogon prefixes, with registry status and announcing carriers.
* **List Countries** `listCountries`: Returns detailed information for every country and territory in a single list: ISO names and codes, official languages, currency, calling code, flag, UN region and World Bank region and income level. The API returns a JSON array of country records.
* **List Networks By CIDR** `listNetworksByCidr`: Returns the networks currently announced on BGP within an IPv4 CIDR range, including the parent network, registration details, carriers and a paginated list of active sub-networks.
* **List Tor Exit Nodes** `listTorExitNodes`: Returns a paginated list of currently active Tor exit node IP addresses, geolocated to country level, with the carrier Autonomous Systems for each node.
* **Parse User Agent** `parseUserAgent`: Parses a raw browser user-agent string into device type, operating system, browser family and version, and flags for mobile devices and search engine spiders.
* **Reverse Geocode To City** `reverseGeocodeToCity`: Converts WGS 84 latitude and longitude coordinates into structured locality data - continent, country, principal subdivision, city, suburb and postcode - by resolving to administrative and non-administrative boundaries. This is the server-side endpoint and works reliably in rural and sparsely mapped areas.
* **Reverse Geocode To City Client Side** `reverseGeocodeToCityClient`: Free keyless reverse geocoding that turns coordinates into locality data, falling back to IP-based geolocation when no coordinates are supplied. BigDataCloud's fair use policy restricts this endpoint to calls made directly from a browser or mobile app using the device's own current location; server-side or batch use should call Reverse Geocode To City instead, and repeated server-side use can return HTTP 402 and temporarily ban the calling IP address.
* **Reverse Geocode With Time Zone** `reverseGeocodeWithTimeZone`: Combines Reverse Geocode To City and Time Zone By Location in a single request, returning locality data and the active IANA time zone for a set of coordinates. Halves the number of calls and the quota consumed compared with calling both endpoints separately.
* **Run IP Geolocation GraphQL Query** `runIpGeolocationGraphQlQuery`: Runs a GraphQL query against the IP Geolocation package so only the required fields are returned, which keeps payloads small. Root query fields are ipData, countryInfo, userAgent, asnInfo and timezoneInfo; ipData exposes ipAddress, latLng, confidence, country, locality, timezone, confidenceArea, hazardReport, inetnum and network.
* **Run Network Engineering GraphQL Query** `runNetworkEngineeringGraphQlQuery`: Runs a GraphQL query against the Network Engineering package so only the required fields are returned. Root query fields are ipV4, ipV6, asnInfoFull, inetnum and network, covering autonomous system detail, BGP prefixes and address space records.
* **Run Phone And Email GraphQL Query** `runPhoneEmailGraphQlQuery`: Runs a GraphQL query against the Phone and Email Verification package so only the required fields are returned. Root query fields are phoneNumber, which validates a number for a country code, and emailVerification.
* **Run Reverse Geocoding GraphQL Query** `runReverseGeocodingGraphQlQuery`: Runs a GraphQL query against the Reverse Geocoding package so only the required fields are returned. The single root query field is locationData, which accepts latitude, longitude and locale arguments and exposes latLng, country, locality and timezone.
* **Validate Phone Number** `validatePhoneNumber`: Normalises and validates a phone number against the E.164 international standard for a given country, returning the canonical E.164 form, international and national display formats, the detected line type and full country context such as calling code, currency and languages.
* **Validate Phone Number By IP** `validatePhoneNumberByIp`: Validates a phone number by inferring the expected country from an IP address instead of requiring an explicit country code, which suits signup and checkout forms that have no country selector. Returns the same normalised formats, line type and country context as Validate Phone Number.
* **Verify Email Address** `verifyEmailAddress`: Verifies an email address: syntax validity, whether the domain has a mail server, whether the domain is a known spammer and whether it is a disposable email provider. No email is sent.

</details>
