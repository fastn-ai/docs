---
description: "IPinfo provides IP address data. Look up location, hostname and network details for an IP, your own IP, a network or a batch."
hidden: true
---

# IPinfo

<img src="../../.gitbook/assets/connectors/lg/ipinfo.png" alt="IPinfo logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ipinfo.io](https://ipinfo.io) |
| **Authentication** | Access token |
| **Slug** | `ipinfo` |

## Setup

Your customers enter their access token for IPinfo when they connect. Nothing else needs setting up.

## Use it

Add IPinfo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ipinfo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Lookup IP Addresses</td><td><code>batchLookupIpAddresses</code></td><td>Looks up up to 1000 IP addresses in a single call and returns a map of each IP to its geolocation and network details. Optionally drops entries with no data via the filter parameter.</td></tr><tr><td>Lookup ASN</td><td><code>lookupAsn</code></td><td>Returns details for an Autonomous System Number (ASN), including the organization name, allocated IP prefixes, registry, country, and domain. This is a paid-plan feature on IPinfo - accounts on the free Lite plan receive a 401 'Token does not have access to this API' response.</td></tr><tr><td>Lookup IP Address</td><td><code>lookupIpAddress</code></td><td>Returns geolocation and network details for a specific IPv4 or IPv6 address, including city, region, country, coordinates, hostname, timezone, and the organization/ASN operating it.</td></tr><tr><td>Lookup My IP Address</td><td><code>lookupMyIpAddress</code></td><td>Returns geolocation and network details for the caller's own public IP address, as seen by IPinfo, including city, region, country, coordinates, hostname, timezone, and the organization/ASN operating it.</td></tr></tbody></table>

## Events

IPinfo has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
