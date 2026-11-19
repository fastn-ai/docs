---
description: "IPstack is a real-time IP geolocation and IP intelligence API by apilayer."
hidden: true
---

# IPstack

<img src="../../.gitbook/assets/connectors/lg/ipstack.png" alt="IPstack logo">

It resolves an IPv4 or IPv6 address (or the caller's own IP) to location, timezone, currency, connection, and security data.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ipstack.com](https://ipstack.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `ipstack` |

## Use it

Add IPstack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ipstack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Requester IP Location</td><td><code>getRequesterIpLocation</code></td><td>Looks up real-time geolocation data for the IP address the API request originates from (the caller's own public IP). Returns location fields by default; hostname lookup and additional response language can be requested via optional parameters.</td></tr><tr><td>Look Up IP Address</td><td><code>lookUpIpAddress</code></td><td>Resolves one IPv4/IPv6 address, or up to 50 comma-separated addresses in a single bulk request, to geolocation data. A single address returns one result object; multiple comma-separated addresses return an array of result objects (Bulk Endpoint).</td></tr></tbody></table>
