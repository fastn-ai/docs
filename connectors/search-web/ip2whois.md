---
description: "IP2WHOIS provides domain WHOIS lookups returning registrar, registrant, admin, technical and billing contacts, creation, update and expiration dates, domain…"
---

# IP2WHOIS

IP2WHOIS provides domain WHOIS lookups returning registrar, registrant, admin, technical and billing contacts, creation, update and expiration dates, domain age and name servers for 1,200+ TLDs, plus a Hosted Domain API that lists the domain names hosted on an IP address. This connector covers the IP2WHOIS Domain WHOIS API and the Hosted Domain API, authenticated with an IP2Location.io API key.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ip2whois.com](https://ip2whois.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 2 |
| **Events** | 0 |
| **Slug** | `ip2whois` |

## Use it

Add IP2WHOIS from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ip2whois.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Domain WHOIS | `getDomainWhois` | Retrieves the WHOIS record for a domain name, including domain ID and status, creation, update and expiration dates, domain age, WHOIS server, registrar details, registrant, admin, technical and billing contacts, and name servers. |
| List Hosted Domains | `listHostedDomains` | Lists the domain names hosted on an IPv4 or IPv6 address, with the total number of hosted domains and page-based pagination. Increment the page parameter to walk through all pages. |
