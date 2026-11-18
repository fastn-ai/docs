---
description: "ipdata is an IP geolocation and threat intelligence API."
hidden: true
---

# ipdata

<img src="../../.gitbook/assets/connectors/lg/ipdata.png" alt="ipdata logo">

ipdata is an IP geolocation and threat intelligence API. This connector covers the full ipdata REST API: IP address lookups, caller IP lookups, ASN lookups, per-field lookups for the geolocation, ASN, carrier, company, currency, time zone, language and threat objects, and bulk lookups, against either the global or the EU data-residency endpoint.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ipdata.co](https://ipdata.co) |
| **Authentication** | Credentials you enter |
| **Slug** | `ipdata` |

## Use it

Add ipdata from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ipdata.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Bulk Look Up Resources</td><td><code>bulkLookupResources</code></td><td>Looks up a list of IP addresses, AS numbers, or a mix of both in a single request and returns one record per resource in the same order. Requires a paid ipdata plan.</td></tr><tr><td>Get IP Autonomous System</td><td><code>getIpAutonomousSystem</code></td><td>Returns only the autonomous system object for an IP address, giving the AS number, operating organization, domain, announced route and usage type.</td></tr><tr><td>Get IP Company</td><td><code>getIpCompany</code></td><td>Returns only the company object for an IP address, identifying the organization that owns the address range. Returns null when company data is not included in your ipdata plan.</td></tr><tr><td>Get IP Currency</td><td><code>getIpCurrency</code></td><td>Returns only the currency object for the country an IP address is located in, including the currency name, ISO 4217 code, symbol, native symbol and plural name.</td></tr><tr><td>Get IP Field</td><td><code>getIpField</code></td><td>Returns a single top-level field of the ipdata record for an IP address. Scalar fields come back as a bare plain-text value and object fields as JSON. Only the listed field names are valid; ipdata silently returns the whole record for any other name.</td></tr><tr><td>Get IP Languages</td><td><code>getIpLanguages</code></td><td>Returns only the official languages of the country an IP address is located in, each with its English name, native name and ISO 639-1 code.</td></tr><tr><td>Get IP Mobile Carrier</td><td><code>getIpCarrier</code></td><td>Returns only the mobile carrier object for an IP address, giving the carrier name and its mobile country and network codes. Returns null when the address is not on a mobile network or carrier data is not included in your plan.</td></tr><tr><td>Get IP Threat Intelligence</td><td><code>getIpThreat</code></td><td>Returns only the threat intelligence object for an IP address, flagging Tor exit nodes, proxies, iCloud Private Relay, datacenter addresses, known attackers and abusers, and listing the blocklists the address appears on.</td></tr><tr><td>Get IP Time Zone</td><td><code>getIpTimeZone</code></td><td>Returns only the time zone object for an IP address, including the tz database name, abbreviation, UTC offset, current daylight saving state and the current local time.</td></tr><tr><td>Look Up Autonomous System</td><td><code>lookupAutonomousSystem</code></td><td>Returns the full record for an autonomous system by AS number, including the operating organization, its announced IPv4 and IPv6 prefixes, total address count, registry, allocation date, and its upstream, downstream and peer AS numbers. This endpoint does not support field filtering.</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Look Up Caller IP Address</td><td><code>lookupCallerIpAddress</code></td><td>Returns the full ipdata record for the IP address the request originates from, without needing to supply an address. Use the fields parameter to return only selected top-level fields.</td></tr><tr><td>Look Up IP Address</td><td><code>lookupIpAddress</code></td><td>Returns the full ipdata record for a single IPv4 or IPv6 address, including geolocation, autonomous system, currency, languages, time zone, carrier and threat intelligence. Use the fields parameter to return only selected top-level fields.</td></tr></tbody></table>

</details>
