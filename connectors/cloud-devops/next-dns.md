---
description: "NextDNS is a cloud DNS firewall that blocks ads, trackers and threats and provides parental controls and DNS analytics."
hidden: true
---

# NextDNS

NextDNS is a cloud DNS firewall that blocks ads, trackers and threats and provides parental controls and DNS analytics. This connector covers the NextDNS API: profiles; security, privacy, parental control and settings (logs, log dropping, block page, performance); denylist, allowlist, security TLDs, privacy blocklists and native trackers, parental control services and categories; DNS rewrites; setup and linked IP; query logs (list, download, clear, stream); and analytics by status, domain, reason, IP, device, protocol, query type, IP version, DNSSEC, encryption and destination, each also as a time series.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [nextdns.io](https://nextdns.io) |
| **Authentication** | Credentials you enter |
| **Actions** | 84 |
| **Events** | 0 |
| **Slug** | `nextDns` |

## Use it

Add NextDNS from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nextDns.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Allowlist Domain | `addAllowlistDomain` | Adds a domain to a profile's allowlist so it is never blocked, optionally as an inactive entry. |
| Add Blocked TLD | `addBlockedTld` | Blocks a top-level domain (such as zip) for a profile. |
| Add Denylist Domain | `addDenylistDomain` | Adds a domain to a profile's denylist so it is blocked, optionally as an inactive entry. |
| Add Native Tracking Protection | `addNativeTrackingProtection` | Enables blocking of a vendor's native device tracking (such as Apple or Samsung telemetry) on a profile. |
| Add Parental Control Category | `addParentalControlCategory` | Blocks a content category (such as gambling) under a profile's parental control. |
| Add Parental Control Service | `addParentalControlService` | Blocks an app or service (such as TikTok) under a profile's parental control. |
| Add Privacy Blocklist | `addPrivacyBlocklist` | Enables an ad and tracker blocklist (such as oisd) on a profile. |
| Clear Logs | `clearLogs` | Permanently deletes all DNS query logs stored for a profile. |
| Create Profile | `createProfile` | Creates a NextDNS profile with a name and optional initial security, privacy, parental control, denylist, allowlist and settings configuration. Returns the new profile ID. |
| Create Rewrite | `createRewrite` | Adds a DNS rewrite to a profile so a domain resolves to a custom IP address or hostname. The record type (A, AAAA or CNAME) is inferred from the answer. |
| Delete Profile | `deleteProfile` | Permanently deletes a NextDNS profile and its logs. |
| Delete Rewrite | `deleteRewrite` | Deletes a DNS rewrite from a profile by its rewrite ID. |
| Get Block Page Settings | `getBlockPageSettings` | Retrieves whether a profile shows a block page instead of failing silently when a domain is blocked. |
| Get Block Reason Analytics | `getReasonAnalytics` | Returns counts of blocked queries grouped by the reason they were blocked, such as a blocklist or native tracking protection. |
| Get Block Reason Time Series | `getReasonAnalyticsSeries` | Returns a time series of blocked query counts per block reason, bucketed into tumbling windows. |
| Get Client IP Analytics | `getIpAnalytics` | Returns query counts per client IP address, with the network (ISP, ASN, VPN, cellular) and geolocation of each IP. |
| Get Client IP Time Series | `getIpAnalyticsSeries` | Returns a time series of query counts per client IP address, bucketed into tumbling windows. |
| Get Destination Analytics | `getDestinationAnalytics` | Returns query counts grouped by destination, either by the country where queried domains are hosted or by big-tech company (Google, Apple, Facebook, Amazon, Microsoft, others). |
| Get Destination Time Series | `getDestinationAnalyticsSeries` | Returns a time series of query counts per destination country or big-tech company, bucketed into tumbling windows. |
| Get Device Analytics | `getDeviceAnalytics` | Returns query counts per identified device, plus a bucket for unidentified devices. |
| Get Device Time Series | `getDeviceAnalyticsSeries` | Returns a time series of query counts per device, bucketed into tumbling windows. |
| Get DNSSEC Analytics | `getDnssecAnalytics` | Returns query counts split by whether the response was DNSSEC-validated. |
| Get DNSSEC Time Series | `getDnssecAnalyticsSeries` | Returns a time series of query counts split by DNSSEC validation, bucketed into tumbling windows. |
| Get Domain Analytics | `getDomainAnalytics` | Returns a profile's most-queried domains with query counts, optionally only blocked or allowed domains, or grouped by root domain. |
| Get Encryption Analytics | `getEncryptionAnalytics` | Returns query counts split by whether the DNS query was sent over an encrypted transport. |
| Get Encryption Time Series | `getEncryptionAnalyticsSeries` | Returns a time series of query counts split by encrypted versus unencrypted transport, bucketed into tumbling windows. |
| Get IP Version Analytics | `getIpVersionAnalytics` | Returns query counts grouped by client IP version (IPv4 or IPv6). |
| Get IP Version Time Series | `getIpVersionAnalyticsSeries` | Returns a time series of query counts per client IP version, bucketed into tumbling windows. |
| Get Linked IP | `getLinkedIp` | Retrieves a profile's linked IP configuration: the linked-IP DNS servers, the currently linked IP, the DDNS hostname and the update token. |
| Get Log Drop Settings | `getLogDropSettings` | Retrieves whether client IP addresses and queried domains are dropped from a profile's logs. |
| Get Logs Download URL | `getLogsDownloadUrl` | Generates a downloadable file of a profile's DNS query logs and returns its public URL. |
| Get Logs Settings | `getLogsSettings` | Retrieves a profile's query logging settings: whether logging is enabled, IP and domain dropping, retention period and storage location. |
| Get Parental Control Settings | `getParentalControl` | Retrieves a profile's parental control settings: blocked services and categories, SafeSearch, YouTube Restricted Mode, bypass blocking and recreation time schedule. |
| Get Performance Settings | `getPerformanceSettings` | Retrieves a profile's performance settings: EDNS Client Subnet, Cache Boost and CNAME flattening. |
| Get Privacy Settings | `getPrivacy` | Retrieves a profile's privacy settings: enabled blocklists, native tracking protections, disguised third-party tracker blocking and affiliate link handling. |
| Get Profile | `getProfile` | Retrieves a complete NextDNS profile: setup endpoints, security, privacy, parental control, denylist, allowlist, rewrites and settings. |
| Get Protocol Analytics | `getProtocolAnalytics` | Returns query counts grouped by DNS transport protocol, such as DNS-over-HTTPS, DNS-over-TLS or UDP. |
| Get Protocol Time Series | `getProtocolAnalyticsSeries` | Returns a time series of query counts per DNS transport protocol, bucketed into tumbling windows. |
| Get Query Status Analytics | `getStatusAnalytics` | Returns a profile's DNS query counts grouped by resolution status (default, blocked, allowed) for a date range. |
| Get Query Status Time Series | `getStatusAnalyticsSeries` | Returns a time series of a profile's DNS query counts per resolution status (default, blocked, allowed), bucketed into tumbling windows for charting. |
| Get Query Type Analytics | `getQueryTypeAnalytics` | Returns query counts grouped by DNS record type, such as A, AAAA or HTTPS. |
| Get Query Type Time Series | `getQueryTypeAnalyticsSeries` | Returns a time series of query counts per DNS record type, bucketed into tumbling windows. |
| Get Security Settings | `getSecurity` | Retrieves a profile's security settings: threat protections such as threat intelligence feeds, AI threat detection, Google Safe Browsing, cryptojacking, DNS rebinding and typosquatting protection, plus blocked TLDs. |
| Get Settings | `getSettings` | Retrieves all of a profile's settings: logging, block page, performance, bypass age verification and Web3 resolution. |
| Get Setup | `getSetup` | Retrieves a profile's setup information: IPv4 and IPv6 resolver addresses, linked IP servers and DDNS, and the DNSCrypt stamp. |
| List Allowlist | `listAllowlist` | Lists the domains on a profile's allowlist and whether each entry is active. |
| List Blocked TLDs | `listBlockedTlds` | Lists the top-level domains (such as ru or zip) blocked by a profile's security settings. |
| List Denylist | `listDenylist` | Lists the domains on a profile's denylist and whether each entry is active. |
| List Logs | `listLogs` | Lists a profile's DNS query logs, newest first by default, filterable by date range, device, status and search text, with cursor pagination. Raw mode includes all query types. |
| List Native Tracking Protections | `listNativeTrackingProtections` | Lists the native device and OS tracking protections (such as Apple, Samsung or Windows) enabled on a profile. |
| List Parental Control Categories | `listParentalControlCategories` | Lists the content categories (such as gambling or social networks) blocked by a profile's parental control, with their active and recreation-time status. |
| List Parental Control Services | `listParentalControlServices` | Lists the apps and services (such as TikTok or Fortnite) blocked by a profile's parental control, with their active and recreation-time status. |
| List Privacy Blocklists | `listPrivacyBlocklists` | Lists the ad and tracker blocklists enabled on a profile, with each list's name, website, description, entry count and last update. |
| List Profiles | `listProfiles` | Lists the NextDNS profiles the account can access, with each profile's ID, fingerprint, name and role. |
| List Rewrites | `listRewrites` | Lists a profile's DNS rewrites, each mapping a domain to a custom IP address or hostname. |
| Remove Allowlist Domain | `removeAllowlistDomain` | Removes a domain from a profile's allowlist. |
| Remove Blocked TLD | `removeBlockedTld` | Unblocks a top-level domain for a profile. |
| Remove Denylist Domain | `removeDenylistDomain` | Removes a domain from a profile's denylist. |
| Remove Native Tracking Protection | `removeNativeTrackingProtection` | Stops blocking a vendor's native device tracking on a profile. |
| Remove Parental Control Category | `removeParentalControlCategory` | Unblocks a content category by removing it from a profile's parental control. |
| Remove Parental Control Service | `removeParentalControlService` | Unblocks a service by removing it from a profile's parental control. |
| Remove Privacy Blocklist | `removePrivacyBlocklist` | Disables an ad and tracker blocklist on a profile. |
| Replace Allowlist | `replaceAllowlist` | Replaces a profile's entire allowlist with the given entries. Pass an empty list [] to clear it. |
| Replace Blocked TLDs | `replaceBlockedTlds` | Replaces the full list of top-level domains blocked by a profile. Pass an empty list [] to unblock all. |
| Replace Denylist | `replaceDenylist` | Replaces a profile's entire denylist with the given entries. Pass an empty list [] to clear it. |
| Replace Native Tracking Protections | `replaceNativeTrackingProtections` | Replaces the full set of native tracking protections enabled on a profile. Pass an empty list [] to disable all. |
| Replace Parental Control Categories | `replaceParentalControlCategories` | Replaces the full list of content categories blocked by a profile's parental control. Pass an empty list [] to clear it. |
| Replace Parental Control Services | `replaceParentalControlServices` | Replaces the full list of services blocked by a profile's parental control. Pass an empty list [] to clear it. |
| Replace Privacy Blocklists | `replacePrivacyBlocklists` | Replaces the full set of ad and tracker blocklists enabled on a profile. Pass an empty list [] to disable all. |
| Stream Logs | `streamLogs` | Opens a Server-Sent Events stream of a profile's DNS query logs in real time. The connection stays open; the executor returns whatever raw event-stream text was received before its ~30 second cap (typically only ':keepalive'), so use List Logs for request/response access. |
| Update Allowlist Domain | `updateAllowlistDomain` | Activates or deactivates a domain entry on a profile's allowlist. |
| Update Block Page Settings | `updateBlockPageSettings` | Enables or disables the block page shown when a profile blocks a domain. |
| Update Denylist Domain | `updateDenylistDomain` | Activates or deactivates a domain entry on a profile's denylist. |
| Update Linked IP | `updateLinkedIp` | Sets or clears the DDNS hostname used to keep a profile's linked IP up to date. |
| Update Log Drop Settings | `updateLogDropSettings` | Sets whether client IP addresses and queried domains are dropped from a profile's logs. |
| Update Logs Settings | `updateLogsSettings` | Enables or disables query logging for a profile and sets the log retention period and storage location. |
| Update Parental Control Category | `updateParentalControlCategory` | Activates or deactivates a blocked content category, or sets whether it is allowed during recreation time, under a profile's parental control. |
| Update Parental Control Service | `updateParentalControlService` | Activates or deactivates a blocked service, or sets whether it is allowed during recreation time, under a profile's parental control. |
| Update Parental Control Settings | `updateParentalControl` | Updates a profile's SafeSearch, YouTube Restricted Mode, bypass blocking and recreation time schedule. Manage blocked services and categories with their dedicated actions. |
| Update Performance Settings | `updatePerformanceSettings` | Turns EDNS Client Subnet, Cache Boost and CNAME flattening on or off for a profile. |
| Update Privacy Settings | `updatePrivacy` | Turns disguised third-party tracker blocking and affiliate and tracking link allowance on or off for a profile. Manage blocklists and native tracking protections with their dedicated actions. |
| Update Profile | `updateProfile` | Updates a NextDNS profile's name. Use the dedicated security, privacy, parental control and settings actions to change nested configuration. |
| Update Security Settings | `updateSecurity` | Turns individual security protections on or off for a profile. Only the protections you provide are changed. Manage blocked TLDs with the Security TLD actions. |
| Update Settings | `updateSettings` | Turns bypass age verification and Web3 domain resolution on or off for a profile. Use the logs, block page and performance settings actions for those groups. |
