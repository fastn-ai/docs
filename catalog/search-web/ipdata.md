---
description: "ipdata provides IP location and threat data. Look up IPs in bulk, with network, carrier, company, currency and time zone details."
hidden: true
---

# ipdata

<img src="../../.gitbook/assets/connectors/lg/ipdata.png" alt="ipdata logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ipdata.co](https://ipdata.co) |
| **Authentication** | API key |
| **Slug** | `ipdata` |

## Setup

Your customers enter their API key for ipdata when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect ipdata from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **ipdata**.
2. Select **Connect** on the ipdata card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use ipdata's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Bulk Look Up Resources</td><td><code>bulkLookupResources</code></td><td>Looks up a list of IP addresses, AS numbers, or a mix of both in a single request and returns one record per resource in the same order. Requires a paid ipdata plan.</td></tr><tr><td>Get IP Autonomous System</td><td><code>getIpAutonomousSystem</code></td><td>Returns only the autonomous system object for an IP address, giving the AS number, operating organization, domain, announced route and usage type.</td></tr><tr><td>Get IP Company</td><td><code>getIpCompany</code></td><td>Returns only the company object for an IP address, identifying the organization that owns the address range. Returns null when company data is not included in your ipdata plan.</td></tr><tr><td>Get IP Currency</td><td><code>getIpCurrency</code></td><td>Returns only the currency object for the country an IP address is located in, including the currency name, ISO 4217 code, symbol, native symbol and plural name.</td></tr><tr><td>Get IP Field</td><td><code>getIpField</code></td><td>Returns a single top-level field of the ipdata record for an IP address. Scalar fields come back as a bare plain-text value and object fields as JSON. Only the listed field names are valid; ipdata silently returns the whole record for any other name.</td></tr><tr><td>Get IP Languages</td><td><code>getIpLanguages</code></td><td>Returns only the official languages of the country an IP address is located in, each with its English name, native name and ISO 639-1 code.</td></tr><tr><td>Get IP Mobile Carrier</td><td><code>getIpCarrier</code></td><td>Returns only the mobile carrier object for an IP address, giving the carrier name and its mobile country and network codes. Returns null when the address is not on a mobile network or carrier data is not included in your plan.</td></tr><tr><td>Get IP Threat Intelligence</td><td><code>getIpThreat</code></td><td>Returns only the threat intelligence object for an IP address, flagging Tor exit nodes, proxies, iCloud Private Relay, datacenter addresses, known attackers and abusers, and listing the blocklists the address appears on.</td></tr><tr><td>Get IP Time Zone</td><td><code>getIpTimeZone</code></td><td>Returns only the time zone object for an IP address, including the tz database name, abbreviation, UTC offset, current daylight saving state and the current local time.</td></tr><tr><td>Look Up Autonomous System</td><td><code>lookupAutonomousSystem</code></td><td>Returns the full record for an autonomous system by AS number, including the operating organization, its announced IPv4 and IPv6 prefixes, total address count, registry, allocation date, and its upstream, downstream and peer AS numbers. This endpoint does not support field filtering.</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Look Up Caller IP Address</td><td><code>lookupCallerIpAddress</code></td><td>Returns the full ipdata record for the IP address the request originates from, without needing to supply an address. Use the fields parameter to return only selected top-level fields.</td></tr><tr><td>Look Up IP Address</td><td><code>lookupIpAddress</code></td><td>Returns the full ipdata record for a single IPv4 or IPv6 address, including geolocation, autonomous system, currency, languages, time zone, carrier and threat intelligence. Use the fields parameter to return only selected top-level fields.</td></tr></tbody></table>

</details>

