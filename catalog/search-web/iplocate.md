---
description: "IPLocate provides IP geolocation and threat data. Look up one or many IPs for location, network, company, abuse contacts and privacy flags."
hidden: true
---

# IPLocate

<img src="../../.gitbook/assets/connectors/lg/iplocate.png" alt="IPLocate logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [iplocate.io](https://iplocate.io) |
| **Authentication** | API key |
| **Slug** | `iplocate` |

## Setup

Your customers enter their API key for IPLocate when they connect. Nothing else needs setting up.

## Use it

Add IPLocate from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.iplocate.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Look Up IP Addresses</td><td><code>batchLookupIpAddresses</code></td><td>Looks up up to 1,000 IPv4 and IPv6 addresses in a single request and returns a map keyed by each input address. Invalid or unknown addresses are returned inline as an error object for that key. Requires a paid IPLocate plan or purchased credits.</td></tr><tr><td>Get Current IP Address</td><td><code>getCurrentIpAddress</code></td><td>Returns the caller's public IP address as plain text from IPLocate's free, unlimited current-IP service. This endpoint needs no API key and is not rate limited, and returns only the address with no geolocation data.</td></tr><tr><td>Get Current IP Address As JSON</td><td><code>getCurrentIpAddressAsJson</code></td><td>Returns the caller's public IP address as a JSON object from IPLocate's free, unlimited current-IP service. This endpoint needs no API key and is not rate limited, and returns only the address with no geolocation data.</td></tr><tr><td>Get IP Abuse Contact</td><td><code>getIpAbuseContact</code></td><td>Returns only the registered network abuse contact for an IP address, sourced from public Whois data. IPLocate's terms restrict this data to cybersecurity, fraud prevention, network monitoring and research use.</td></tr><tr><td>Get IP Autonomous System</td><td><code>getIpAutonomousSystem</code></td><td>Returns only the autonomous system (ASN) and network details for an IP address, including the ASN number, announced route, network name, operating organization and its regional internet registry.</td></tr><tr><td>Get IP Company</td><td><code>getIpCompany</code></td><td>Returns only the company details for an IP address, identifying the organization that owns the address range along with its domain, country and business classification.</td></tr><tr><td>Get IP Field</td><td><code>getIpField</code></td><td>Returns a single top-level geolocation field for an IP address as a plain-text value, for example just the country code or the time zone. For the nested ASN, privacy, hosting, company and abuse objects use their dedicated actions.</td></tr><tr><td>Get IP Hosting Provider</td><td><code>getIpHostingProvider</code></td><td>Returns only the hosting or datacenter provider details for an IP address, including the provider name, domain, network range and, where published, the provider's region and service. Returns an empty result for addresses with no detailed hosting data.</td></tr><tr><td>Get IP Privacy And Threat Flags</td><td><code>getIpPrivacy</code></td><td>Returns only the privacy and threat detection flags for an IP address, indicating whether it is a proxy, VPN, Tor exit node, iCloud Private Relay address, hosting address, bogon address or a reported abuser.</td></tr><tr><td>Look Up Caller IP Address</td><td><code>lookupCallerIpAddress</code></td><td>Returns the full IPLocate intelligence record for the IP address the request originates from, without needing to supply an address. Use the include parameter to return only selected fields.</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Look Up IP Address</td><td><code>lookupIpAddress</code></td><td>Returns the full IPLocate intelligence record for a single IPv4 or IPv6 address, including geolocation, autonomous system, privacy and threat flags, hosting provider, company and abuse contact data. Use the include parameter to return only selected fields.</td></tr></tbody></table>

</details>

## Events

IPLocate has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
