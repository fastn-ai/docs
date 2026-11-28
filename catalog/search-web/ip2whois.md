---
description: "IP2WHOIS looks up domain registration details. Get WHOIS records for a domain and list domains hosted on an IP address."
hidden: true
---

# IP2WHOIS

<img src="../../.gitbook/assets/connectors/lg/ip2whois.png" alt="IP2WHOIS logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ip2whois.com](https://ip2whois.com) |
| **Authentication** | API key |
| **Slug** | `ip2whois` |

## Setup

Your customers enter their API key for IP2WHOIS when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect IP2WHOIS from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **IP2WHOIS**.
2. Select **Connect** on the IP2WHOIS card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use IP2WHOIS's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Domain WHOIS</td><td><code>getDomainWhois</code></td><td>Retrieves the WHOIS record for a domain name, including domain ID and status, creation, update and expiration dates, domain age, WHOIS server, registrar details, registrant, admin, technical and billing contacts, and name servers.</td></tr><tr><td>List Hosted Domains</td><td><code>listHostedDomains</code></td><td>Lists the domain names hosted on an IPv4 or IPv6 address, with the total number of hosted domains and page-based pagination. Increment the page parameter to walk through all pages.</td></tr></tbody></table>

