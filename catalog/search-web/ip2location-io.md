---
description: "IP2Location.io looks up where an IP address is located. Get geolocation for one or many IP addresses."
hidden: true
---

# IP2Location.io

<img src="../../.gitbook/assets/connectors/lg/ip2location-io.png" alt="IP2Location.io logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ip2location.io](https://ip2location.io) |
| **Authentication** | API key |
| **Slug** | `ip2locationIo` |

## Setup

Your customers enter their API key for IP2Location.io when they connect. Nothing else needs setting up.

## Use it

Add IP2Location.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ip2locationIo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Bulk IP Geolocation</td><td><code>bulkIpGeolocation</code></td><td>Looks up the geolocation of up to 1,000 IPv4 or IPv6 addresses in a single request and returns a result object keyed by IP address, optionally limited to selected fields. This endpoint requires a paid IP2Location.io plan; free-plan keys receive error 401 'Bulk lookup is not available with your plan'.</td></tr><tr><td>Get IP Geolocation</td><td><code>getIpGeolocation</code></td><td>Looks up the geolocation of an IPv4 or IPv6 address, returning country, region, city, ZIP code, latitude and longitude, time zone, ASN and proxy indicator. Higher plans add ISP, domain, usage type, mobile carrier, continent, country, region, city and time-zone objects, AS details, full proxy and threat flags, fraud score, advertising category and district. Translations via the lang parameter require the Plus plan or above.</td></tr></tbody></table>

## Events

IP2Location.io has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
