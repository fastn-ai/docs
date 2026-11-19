---
description: "Ipregistry is an IP geolocation, network and threat intelligence API."
hidden: true
---

# Ipregistry

<img src="../../.gitbook/assets/connectors/lg/ipregistry.png" alt="Ipregistry logo">

This connector covers all eight Ipregistry endpoints: single, batch and origin IP lookups, single, batch and origin autonomous system lookups, and user-agent parsing for both submitted and origin user agents, against the global, EU or GB base URL.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ipregistry.co](https://ipregistry.co) |
| **Authentication** | Credentials you enter |
| **Slug** | `ipregistry` |

## Use it

Add Ipregistry from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ipregistry.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Look Up Autonomous Systems</td><td><code>batchLookupAutonomousSystems</code></td><td>Looks up up to 16 autonomous systems in a single request and returns one record per AS number in the order submitted. Costs one credit per AS number plus one for the request itself.</td></tr><tr><td>Batch Look Up IP Addresses</td><td><code>batchLookupIpAddresses</code></td><td>Looks up up to 1,024 IPv4 and IPv6 addresses in a single request and returns one record per address in the order submitted. Costs one credit per address plus one for the request itself.</td></tr><tr><td>Look Up Autonomous System</td><td><code>lookupAutonomousSystem</code></td><td>Returns the full Ipregistry record for a single autonomous system by AS number, including the operating organization, registry, allocation date, announced IPv4 and IPv6 prefixes and its upstream, downstream and peer relationships. Costs one credit per request.</td></tr><tr><td>Look Up IP Address</td><td><code>lookupIpAddress</code></td><td>Returns the full Ipregistry record for a single IPv4 or IPv6 address, covering location, currency, time zone, connection and autonomous system, company, carrier and security signals. Costs one credit per request.</td></tr><tr><td>Look Up Origin Autonomous System</td><td><code>lookupOriginAutonomousSystem</code></td><td>Returns the autonomous system record for the network the request originates from, without needing to know the AS number or IP address in advance. Costs one credit per request.</td></tr><tr><td>Look Up Origin IP Address</td><td><code>lookupOriginIpAddress</code></td><td>Returns the full Ipregistry record for the IP address the request originates from, plus parsed user-agent data, without needing to know the address in advance. Called from a server this reflects the server's own address. Costs one credit per request.</td></tr><tr><td>Parse Origin User Agent</td><td><code>parseOriginUserAgent</code></td><td>Parses the User-Agent header of the calling client and returns the browser, engine, device and operating system detected, without submitting a string. Called from a server this reflects the server's own user agent. Costs one credit per request.</td></tr><tr><td>Parse User Agents</td><td><code>parseUserAgents</code></td><td>Parses up to 256 User-Agent header strings and returns the browser, engine, device and operating system detected for each, in the order submitted. Costs one credit per user agent plus one for the request itself.</td></tr></tbody></table>
