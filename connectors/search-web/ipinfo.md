---
description: "IPinfo.io provides IP address data - geolocation, hostname, and ASN/organization information - for a specific IP, the caller's own IP, an ASN, or a batch of…"
hidden: true
---

# IPinfo

<img src="../../.gitbook/assets/connectors/lg/ipinfo.png" alt="IPinfo logo">

IPinfo.io provides IP address data - geolocation, hostname, and ASN/organization information - for a specific IP, the caller's own IP, an ASN, or a batch of IPs in one call.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ipinfo.io](https://ipinfo.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `ipinfo` |

## Use it

Add IPinfo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ipinfo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Lookup IP Addresses | `batchLookupIpAddresses` | Looks up up to 1000 IP addresses in a single call and returns a map of each IP to its geolocation and network details. Optionally drops entries with no data via the filter parameter. |
| Lookup ASN | `lookupAsn` | Returns details for an Autonomous System Number (ASN), including the organization name, allocated IP prefixes, registry, country, and domain. This is a paid-plan feature on IPinfo - accounts on the free Lite plan receive a 401 'Token does not have access to this API' response. |
| Lookup IP Address | `lookupIpAddress` | Returns geolocation and network details for a specific IPv4 or IPv6 address, including city, region, country, coordinates, hostname, timezone, and the organization/ASN operating it. |
| Lookup My IP Address | `lookupMyIpAddress` | Returns geolocation and network details for the caller's own public IP address, as seen by IPinfo, including city, region, country, coordinates, hostname, timezone, and the organization/ASN operating it. |
