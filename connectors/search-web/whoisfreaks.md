---
description: "WhoisFreaks provides domain, DNS, IP and certificate intelligence: live, historical and reverse WHOIS, live, historical, reverse and bulk DNS, domain…"
hidden: true
---

# WhoisFreaks

<img src="../../.gitbook/assets/connectors/whoisfreaks.png" alt="WhoisFreaks logo" width="64">

WhoisFreaks provides domain, DNS, IP and certificate intelligence: live, historical and reverse WHOIS, live, historical, reverse and bulk DNS, domain availability and TLD suggestions, typosquatting discovery, SSL certificate lookup, IP geolocation and reputation, subdomain discovery, domain reputation, ASN and IP WHOIS, plus account usage and the downloadable newly registered, expiring and dropped domain, WHOIS, DNS, subdomain, IP snapshot and threat feed database files.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [whoisfreaks.com](https://whoisfreaks.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `whoisfreaks` |

## Use it

Add WhoisFreaks from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.whoisfreaks.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Bulk Domain Availability | `checkBulkDomainAvailability` | Checks registration availability for up to 100 fully qualified domain names in a single request. Costs 1 credit per domain checked. |
| Check Domain Availability | `checkDomainAvailability` | Checks whether a domain name is available for registration and optionally returns availability of suggested alternatives across other TLDs. Costs 1 credit per domain checked. |
| Check Domain Availability Across TLDs | `checkDomainAvailabilityAcrossTlds` | Checks registration availability of one domain label under each of up to 100 supplied top-level domains (for example 'example' under com, net and org). Costs 1 credit per TLD checked. |
| Download ASN WHOIS Snapshot | `downloadAsnWhoisSnapshot` | Downloads the ASN WHOIS database snapshot (a gzip-compressed JSON file) created on the given date. Use Get ASN WHOIS Snapshot Status to find the latest snapshot date. Requires an active ASN WHOIS database subscription. |
| Download Daily DNS Database Update | `downloadDailyDnsDatabaseUpdate` | Downloads the daily incremental update file of the DNS records database for a date. Requires an active DNS database subscription. |
| Download Daily Subdomains Database Update | `downloadDailySubdomainsDatabaseUpdate` | Downloads the daily incremental update file of the subdomains database for a date. Requires an active Subdomains database subscription. |
| Download Daily WHOIS Database Update | `downloadDailyWhoisDatabaseUpdate` | Downloads the daily incremental update file of the domain WHOIS database for a date. Requires an active WHOIS database subscription. |
| Download Dropped Domains | `downloadDroppedDomains` | Downloads the daily CSV file of domains that were dropped (deleted from the registry) on a date, either with full WHOIS records or as a plain domain list. Requires the Domainer package. |
| Download Dropped Domains With Backlinks | `downloadDroppedDomainsWithBacklinks` | Downloads the daily CSV file of dropped domains enriched with backlink metrics for a date, optionally including their WHOIS records. Requires the Domainer package. |
| Download Expiring Domains | `downloadExpiringDomains` | Downloads the daily CSV file of domains that are about to expire for a date, either with full WHOIS records or as a plain domain list. Requires the Domainer package. |

<details>

<summary>See 51 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Download Expiring Domains With Cleaned WHOIS | `downloadExpiringDomainsCleanedWhois` | Downloads the daily CSV file of expiring domains with cleaned, normalised WHOIS records for a date. Requires the Domainer package. |
| Download IP Security Snapshot | `downloadIpSecuritySnapshot` | Downloads the IP Security (reputation) database snapshot (a gzip-compressed CSV file) created on the given date. Use Get IP Security Snapshot Status to find the latest snapshot date. Requires an active IP Security database subscription. |
| Download IP To City Snapshot | `downloadIpToCitySnapshot` | Downloads the IP-to-City geolocation database snapshot (a ZIP file) created on the given date. Use Get IP To City Snapshot Status to find the latest snapshot date. Requires an active IP Geolocation database subscription. |
| Download IP To Country Snapshot | `downloadIpToCountrySnapshot` | Downloads the IP-to-Country geolocation database snapshot (a ZIP file) created on the given date. Use Get IP To Country Snapshot Status to find the latest snapshot date. Requires an active IP Geolocation database subscription. |
| Download IP WHOIS Snapshot | `downloadIpWhoisSnapshot` | Downloads the IP WHOIS database snapshot (a gzip-compressed JSON file) created on the given date. Use Get IP WHOIS Snapshot Status to find the latest snapshot date. Requires an active IP WHOIS database subscription. |
| Download Malware Domain Feed | `downloadMalwareDomainFeed` | Downloads the daily malware domain threat feed (compressed CSV) for a date. Requires the Domainer package. |
| Download Malware Domain Feed Sample | `downloadMalwareDomainFeedSample` | Downloads a free sample of the malware domain threat feed (compressed CSV) to evaluate its format before subscribing. |
| Download Monthly DNS Database Update | `downloadMonthlyDnsDatabaseUpdate` | Downloads the monthly incremental update file of the DNS records database for a date. Requires an active DNS database subscription. |
| Download Monthly Subdomains Database Update | `downloadMonthlySubdomainsDatabaseUpdate` | Downloads the monthly incremental update file of the subdomains database for a date. Requires an active Subdomains database subscription. |
| Download Monthly WHOIS Database Update | `downloadMonthlyWhoisDatabaseUpdate` | Downloads the monthly incremental update file of the domain WHOIS database for a date. Requires an active WHOIS database subscription. |
| Download Newly Registered ccTLD Domains | `downloadNewlyRegisteredCctldDomains` | Downloads the daily CSV file of newly registered country-code TLD domains for a date, either with full WHOIS records or as a plain domain list, optionally restricted to specific TLDs. Requires the Domainer package. |
| Download Newly Registered ccTLD Domains With Cleaned WHOIS | `downloadNewlyRegisteredCctldDomainsCleanedWhois` | Downloads the daily CSV file of newly registered country-code TLD domains with cleaned, normalised WHOIS records (privacy-protected and placeholder values removed) for a date. Requires the Domainer package. |
| Download Newly Registered Domains With DNS | `downloadNewlyRegisteredDomainsWithDns` | Downloads the daily file of newly registered domains together with their DNS records for a date. Requires the Domainer package. |
| Download Newly Registered gTLD Domains | `downloadNewlyRegisteredGtldDomains` | Downloads the daily CSV file of newly registered generic-TLD domains for a date, either with full WHOIS records or as a plain domain list, optionally restricted to specific TLDs. Requires the Domainer package. |
| Download Newly Registered gTLD Domains With Cleaned WHOIS | `downloadNewlyRegisteredGtldDomainsCleanedWhois` | Downloads the daily CSV file of newly registered generic-TLD domains with cleaned, normalised WHOIS records (privacy-protected and placeholder values removed) for a date. Requires the Domainer package. |
| Download Phishing Domain Feed | `downloadPhishingDomainFeed` | Downloads the daily phishing domain threat feed (compressed CSV) for a date. Requires the Domainer package. |
| Download Phishing Domain Feed Sample | `downloadPhishingDomainFeedSample` | Downloads a free sample of the phishing domain threat feed (compressed CSV) to evaluate its format before subscribing. |
| Download Spam Domain Feed | `downloadSpamDomainFeed` | Downloads the daily spam domain threat feed (compressed CSV) for a date. Requires the Domainer package. |
| Download Spam Domain Feed Sample | `downloadSpamDomainFeedSample` | Downloads a free sample of the spam domain threat feed (compressed CSV) to evaluate its format before subscribing. |
| Download Weekly DNS Database Update | `downloadWeeklyDnsDatabaseUpdate` | Downloads the weekly incremental update file of the DNS records database for a date. Requires an active DNS database subscription. |
| Download Weekly Subdomains Database Update | `downloadWeeklySubdomainsDatabaseUpdate` | Downloads the weekly incremental update file of the subdomains database for a date. Requires an active Subdomains database subscription. |
| Download Weekly WHOIS Database Update | `downloadWeeklyWhoisDatabaseUpdate` | Downloads the weekly incremental update file of the domain WHOIS database for a date. Requires an active WHOIS database subscription. |
| Find Typosquatting Domains | `findTyposquattingDomains` | Finds registered domains that are typo variants of a brand label (character substitution, transposition, omission, repetition) using either a plain keyword or a wildcard pattern. Returns the matching domains with creation, expiry and last-seen dates and a token for the next page. Costs 5 credits per page. |
| Get Account Usage | `getAccountUsage` | Returns the credit balance and request counters for the API key's WhoisFreaks account, including total credits, served requests and, when present, the active subscription's request limits and surcharge usage. |
| Get ASN WHOIS | `getAsnWhois` | Returns WHOIS and routing details for an autonomous system number: organisation, allocation status and date, route objects, upstreams, downstreams, peers, contacts, legacy routes and the parsed and raw WHOIS response. Costs 1 credit. |
| Get ASN WHOIS Snapshot Status | `getAsnWhoisSnapshotStatus` | Returns the name, creation date and scheduled deletion date of the latest ASN WHOIS database snapshot, so you know which date to pass when downloading it. |
| Get Bulk DNS Records | `getBulkDnsRecords` | Performs live DNS lookups for up to 100 domain names and up to 100 IP addresses (PTR) in a single request and returns the records for each. Provide domain names, IP addresses, or both. Costs 1 credit per queried domain or IP. |
| Get Bulk IP Geolocation | `getBulkIpGeolocation` | Returns geolocation, country metadata, network and currency details for up to 100 IP addresses in a single request. The response is a JSON array with one geolocation object per IP. Costs 1 credit per IP. |
| Get Bulk IP Reputation | `getBulkIpReputation` | Returns threat intelligence (threat score, Tor, proxy, VPN, attacker, bot, spam and cloud flags) plus location and network details for up to 100 IP addresses in a single request. The response is a JSON array with one object per IP. Costs 1 credit per IP. |
| Get Bulk WHOIS | `getBulkWhois` | Performs live WHOIS lookups for up to 100 domain names in a single request and returns a parsed WHOIS record for each domain in the same format as the single-domain lookup. Costs 1 credit per successfully resolved domain. |
| Get Database File Status | `getDatabaseFileStatus` | Returns the freshness of every downloadable WhoisFreaks database file: for the newly registered, expiring and dropped domain files, the threat feeds and the WHOIS, DNS, subdomain and IP database updates, the date each became available and when it was last updated. No credits are consumed. |
| Get Domain Reputation | `getDomainReputation` | Performs a real-time threat assessment of a domain and returns a risk verdict with confidence, a DGA (algorithmically generated domain) score, trust signals and indicators, email deliverability analysis, threat-intelligence matches and an evidence summary. Costs 1 credit. |
| Get Historical DNS Records | `getHistoricalDnsRecords` | Returns the historical DNS records captured over time for a domain name, filtered by record type and paginated at 100 records per page. Costs 2 credits per page. |
| Get IP Geolocation | `getIpGeolocation` | Returns the geographic location, country metadata, network and ASN details, company and local currency for an IPv4 or IPv6 address. Costs 1 credit. |
| Get IP Reputation | `getIpReputation` | Returns threat intelligence for an IP address: threat score and flags for Tor, proxy, VPN, anonymous, known attacker, bot, spam and cloud provider usage, together with its location, network and ASN. Costs 1 credit. |
| Get IP Security Snapshot Status | `getIpSecuritySnapshotStatus` | Returns the name, creation date and scheduled deletion date of the latest IP Security (reputation) database snapshot, so you know which date to pass when downloading it. |
| Get IP To City Snapshot Status | `getIpToCitySnapshotStatus` | Returns the name, creation date and scheduled deletion date of the latest IP-to-City geolocation database snapshot, so you know which date to pass when downloading it. |
| Get IP To Country Snapshot Status | `getIpToCountrySnapshotStatus` | Returns the name, creation date and scheduled deletion date of the latest IP-to-Country geolocation database snapshot, so you know which date to pass when downloading it. |
| Get IP WHOIS | `getIpWhois` | Returns the WHOIS registration record for an IPv4 or IPv6 address from the regional internet registry: network ranges (inetnums), owning organisation, technical and abuse contacts, routes and the raw WHOIS response. Costs 1 credit. |
| Get IP WHOIS Snapshot Status | `getIpWhoisSnapshotStatus` | Returns the name, creation date and scheduled deletion date of the latest IP WHOIS database snapshot, so you know which date to pass when downloading it. |
| Get Live DNS Records | `getLiveDnsRecords` | Performs a real-time DNS lookup for a domain name (A, AAAA, MX, NS, TXT, SOA, SPF, CNAME) or a PTR lookup for an IP address and returns the parsed records. Provide a domain name, an IP address, or both. Costs 1 credit per query. |
| Get Live WHOIS | `getLiveWhois` | Performs a real-time WHOIS lookup for a domain name against the authoritative registrar and registry servers and returns the parsed registration record: registrar, registrant, administrative, technical and billing contacts, creation, update and expiry dates, name servers, domain status codes and the raw WHOIS text. Costs 1 credit. |
| Get SSL Certificate | `getSslCertificate` | Retrieves the live SSL/TLS certificate presented by a domain, with subject, issuer, validity period, public key and extensions, and optionally the full certificate chain and the raw OpenSSL output. |
| Get WHOIS History | `getWhoisHistory` | Returns the deduplicated ownership timeline of a domain: every distinct historical WHOIS record captured for it, newest first, with registrar, contacts, dates, name servers and status for each record. Paginated. Costs credits per page. |
| List Dropped Domains | `listDroppedDomains` | Returns the domain names dropped (deleted from the registry) on a date as a JSON array of domain names, optionally restricted to specific TLDs. Requires the Domainer package. |
| List Newly Registered ccTLD Domains | `listNewlyRegisteredCctldDomains` | Returns the newly registered country-code TLD domain names for a date as a JSON array of domain names, optionally restricted to specific TLDs. Requires the Domainer package. |
| List Newly Registered gTLD Domains | `listNewlyRegisteredGtldDomains` | Returns the newly registered generic-TLD domain names for a date as a JSON array of domain names, optionally restricted to specific TLDs. Requires the Domainer package. |
| List Subdomains | `listSubdomains` | Lists the known subdomains of a domain, including nested subdomains, with first-seen, last-seen and inactive-from dates and their DNS records. Filter by status and by first-seen date range; paginated. Costs 2 credits per query. |
| Rotate API Key | `rotateApiKey` | Rotates the account's API key: the current key is revoked immediately and a new key is returned as plain text. After calling this, update the WhoisFreaks connection with the new key, since every subsequent request with the old key will be rejected. |
| Search Reverse DNS | `searchReverseDns` | Finds every domain whose DNS records point at a given value, such as an IP address or CIDR (A/AAAA), a mail server (MX), a name server (NS), a CNAME target or a TXT string. Paginated. Costs 5 credits per page. |
| Search Reverse WHOIS | `searchReverseWhois` | Searches the WHOIS database backwards and returns every domain connected to an owner attribute. Provide exactly one search dimension: a domain keyword, a registrant email address, an owner name or a company name. Paginated; 'mini' mode returns compact rows, 'default' mode returns full WHOIS records. Costs credits per page. |

</details>
