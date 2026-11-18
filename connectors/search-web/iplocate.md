---
description: "IPLocate is an IP geolocation and threat intelligence platform."
---

# IPLocate

IPLocate is an IP geolocation and threat intelligence platform. This connector covers the full IPLocate IP Intelligence API: single IP lookups, caller IP lookups, field- and object-filtered lookups (ASN, privacy and threat flags, hosting provider, company, abuse contact), batch lookups of up to 1,000 addresses, and the free current-IP echo endpoints.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [iplocate.io](https://iplocate.io) |
| **Authentication** | Credentials you enter |
| **Actions** | 11 |
| **Events** | 0 |
| **Slug** | `iplocate` |

## Use it

Add IPLocate from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.iplocate.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Look Up IP Addresses | `batchLookupIpAddresses` | Looks up up to 1,000 IPv4 and IPv6 addresses in a single request and returns a map keyed by each input address. Invalid or unknown addresses are returned inline as an error object for that key. Requires a paid IPLocate plan or purchased credits. |
| Get Current IP Address | `getCurrentIpAddress` | Returns the caller's public IP address as plain text from IPLocate's free, unlimited current-IP service. This endpoint needs no API key and is not rate limited, and returns only the address with no geolocation data. |
| Get Current IP Address As JSON | `getCurrentIpAddressAsJson` | Returns the caller's public IP address as a JSON object from IPLocate's free, unlimited current-IP service. This endpoint needs no API key and is not rate limited, and returns only the address with no geolocation data. |
| Get IP Abuse Contact | `getIpAbuseContact` | Returns only the registered network abuse contact for an IP address, sourced from public Whois data. IPLocate's terms restrict this data to cybersecurity, fraud prevention, network monitoring and research use. |
| Get IP Autonomous System | `getIpAutonomousSystem` | Returns only the autonomous system (ASN) and network details for an IP address, including the ASN number, announced route, network name, operating organization and its regional internet registry. |
| Get IP Company | `getIpCompany` | Returns only the company details for an IP address, identifying the organization that owns the address range along with its domain, country and business classification. |
| Get IP Field | `getIpField` | Returns a single top-level geolocation field for an IP address as a plain-text value, for example just the country code or the time zone. For the nested ASN, privacy, hosting, company and abuse objects use their dedicated actions. |
| Get IP Hosting Provider | `getIpHostingProvider` | Returns only the hosting or datacenter provider details for an IP address, including the provider name, domain, network range and, where published, the provider's region and service. Returns an empty result for addresses with no detailed hosting data. |
| Get IP Privacy And Threat Flags | `getIpPrivacy` | Returns only the privacy and threat detection flags for an IP address, indicating whether it is a proxy, VPN, Tor exit node, iCloud Private Relay address, hosting address, bogon address or a reported abuser. |
| Look Up Caller IP Address | `lookupCallerIpAddress` | Returns the full IPLocate intelligence record for the IP address the request originates from, without needing to supply an address. Use the include parameter to return only selected fields. |
| Look Up IP Address | `lookupIpAddress` | Returns the full IPLocate intelligence record for a single IPv4 or IPv6 address, including geolocation, autonomous system, privacy and threat flags, hosting provider, company and abuse contact data. Use the include parameter to return only selected fields. |
