---
description: "Data247 is a real-time data enrichment and verification API (by LogicTree, Inc.) for phone carrier lookups and email-to-SMS gateways,…"
hidden: true
---

# Data247

<img src="../../.gitbook/assets/connectors/lg/data247.png" alt="Data247 logo">

Data247 is a real-time data enrichment and verification API (by LogicTree, Inc.) for phone carrier lookups and email-to-SMS gateways, phone/email/postal-address verification, name/phone/email/zip append, property data, IP geolocation, Do-Not-Call and TCPA litigator checks, and signup fraud scoring (Trust247). This connector covers every service code in the Data247 API v3.0 user manual plus account balance, rate-card and usage queries and batch JSON posting.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [data247.com](https://data247.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `data247` |

## Use it

Add Data247 from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.data247.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Number To Do-Not-Call List | `addToDoNotCallList` | Do-Not-Call (Add): adds a phone number to your account's internal do-not-call list so later DNC checks report INTERNAL DNC. Service code DA. |
| Append Consumer Profile | `appendConsumerProfile` | Append247 (Profile Data): returns demographic and household profile attributes for a consumer identified by name and address (optionally email or phone). Requires profile data access on the account; accounts without it get a restricted status. The manual does not enumerate the profile fields, so the response is returned as-is. Service code AR. |
| Append Email Address | `appendEmail` | Append247 (Email): finds the email address associated with a residential or business name and address. Optional fields add business firmographics (website, employees, revenue, title, business type). Billed per hit (service code AE). |
| Append Gender | `appendGender` | Append247 (Gender): infers a person's probable gender from their given name and returns the likelihood percentage. Billed per hit (service code AG). |
| Append Name From Phone | `appendName` | Append247 (Name), also known as CNAM: returns the name associated with a phone number. Billed per hit (service code AN). |
| Append Phone Number | `appendPhone` | Append247 (Phone): finds the phone number(s) associated with a residential or business name and address, including line type and up to five additional numbers. Optional fields add business firmographics (website, employees, revenue, title, business type). Billed per hit (service code AP). |
| Append Property Data | `appendPropertyData` | Append247 (Property Data): returns ownership, mailing address, home statistics, assessed value, latest sale, equity and foreclosure status for a US property address. Billed per hit (service code ARE). |
| Append ZIP Code | `appendZipCode` | Append247 (Zipcode): returns the ZIP+4 and full postal metadata (parsed street components, county, FIPS, congressional district, area code, timezone, DPBC) for a US city/state and optional street address. Always billed (service code AZ). |
| Batch Lookup Phone Numbers | `batchLookupPhoneNumbers` | Runs one phone-based service against up to ten phone numbers in a single call (the API itself accepts up to 99 as p1...p99). Supported services: Text@ (MT), Carrier247 USA (CU), Carrier247 International (CI), Carrier Type (CT), Do-Not-Call check/add/remove (DC/DA/DR) and Reverse Phone (APR). Each result carries its own status, and each number is billed by that service's own rate. |
| Check Do-Not-Call Status | `checkDoNotCall` | Do-Not-Call (Check): tells you whether a phone number appears on the Federal DNC registry or your own internal do-not-call list before you dial it. Federal results require a subscription to the number's area code, otherwise the result is UNAUTHORIZED. Always billed (service code DC). |
| Check Phone Trust | `checkPhoneTrust` | Trust247 (Phone Check): a low-cost risk screen on a phone number supplied at signup, flagging numbers that are not safe to trust (for example invalid, out of service or high-risk VOIP). Always billed (service code TPC). |
| Check TCPA Litigator | `checkTcpaLitigator` | TCPA Litigator Check: screens a phone number or name against known TCPA litigators and serial plaintiffs before you call or text. Always billed (service code DT). |
| Get Account Balance | `getAccountBalance` | Returns the current prepaid balance of the account in USD. Free; service code B. |
| Get Account Rate Card | `getAccountRateCard` | Returns the account attached to the API key: current balance, access flags (Canada, international, IP-only auth, profile data), subscribed Do-Not-Call area codes and the full rate card listing every data service with its API code, per-query rate and billing mode (on_hit or always). Free; service code QR. |
| Get Account Usage | `getAccountUsage` | Returns API usage for today, the current month (default) or the current year: total spend, total queries and a per-service breakdown. Free; service code QU. |
| List Carriers | `listCarriers` | Carrier Name: returns Data247's carrier reference table - every carrier id with its current and legacy carrier name - so you can resolve the carrier_id values returned by the carrier lookup services. Free; service code CN. |
| Locate IP Address | `locateIpAddress` | Locate247: geolocates an IPv4 or IPv6 address to city, state, country, ZIP, latitude/longitude, area code and timezone. Optional fields add ISP and ASN details, mobile-carrier data, EU/currency/language info and risk flags (proxy, VPN, TOR, bogon, cloud provider, abuser, attacker). Always billed (service code GI). |
| Lookup Carrier (International) | `lookupCarrierInternational` | Carrier247 (International): worldwide carrier lookup for a phone number that includes its country code; returns wireless flag, carrier name/id, country and ISO country code, optionally phone type and SMS/MMS gateway addresses. Requires international access on the account (otherwise the status is D247_NOT_AUTHORIZED / D247_DATA_RESTRICTED). Service code CI. |
| Lookup Carrier (USA) | `lookupCarrierUsa` | Carrier247 (USA): looks up the carrier of a US or Canadian phone number and returns whether it is wireless, the carrier name and id, and its email-to-SMS and email-to-MMS gateway addresses. Optional fields add phone type, OCN, timezone, last port date, DBA, MNO and NPA/NXX city/state/zip. Billed per hit (service code CU). Use the batch action to look up many numbers at once. |
| Lookup Phone Type | `lookupPhoneType` | Carrier247 (Carrier Type): tells you whether a phone number is a mobile, landline or VOIP line. Billed per hit (service code CT). |
| Lookup SMS Gateway (Text@) | `lookupSmsGateway` | Text@: returns the email-to-SMS and email-to-MMS gateway addresses for a US/Canadian phone number together with its carrier, so you can text it by email. Same response as Carrier247 (USA); billed per hit (service code MT). |
| Lookup ZIP Code Details | `lookupZipCodeDetails` | Append247 (Reverse Zipcode): expands a 5- or 9-digit US ZIP code into its street, city, state, county, FIPS, congressional district, area code, timezone and delivery point barcode. Billed per hit (service code AZR). |
| Remove Number From Do-Not-Call List | `removeFromDoNotCallList` | Do-Not-Call (Remove): removes a phone number from your account's internal do-not-call list. Service code DR. |
| Reverse Email Lookup | `reverseEmailLookup` | Append247 (Reverse Email): returns the person behind an email address - name, middle initial, business, phone, full postal address, address type and inferred gender. Billed per hit (service code AER). |
| Reverse Phone Lookup | `reversePhoneLookup` | Append247 (Reverse Phone): returns the person or business behind a phone number - name, middle initial, business, full postal address, address type, email and inferred gender. Billed per hit (service code APR). |
| Run Batch Query | `runBatchQuery` | Runs one Data247 service over many input records in a single POST, using the JSON-document form of the API (up to 2,500 queries per call, fewer for slow services). Works with every service code: supply the code and a list of query objects whose keys are that service's input fields. Each result carries its own status and each query is billed by that service's own rate. Optional return fields (billable, cost, ...) are not available on this batch form; use the single-record actions when you need them. |
| Score Business Email | `scoreBusinessEmail` | Trust247 (Business Email): scores 1-100 how likely a signup email belongs to a real person at a legitimate business, so you can reject free, personal, disposable or throwaway addresses at registration. Returns the verdict, reason codes, email type, mail infrastructure, domain age band, website status, mailbox type and name match. This is a fraud/signup heuristic, not a mailbox deliverability check. Always billed (service code TB). |
| Score User Identity | `scoreUserIdentity` | Trust247 (User Identity): scores 1-100 how likely a new signup is who they claim to be by cross-matching the name, company, address, ZIP, phone, email and signup IP, and returns the individual match flags and explanatory notes. Under 50 is generally suspicious, over 80 generally legitimate. Always billed (service code TI). |
| Verify Email Address | `verifyEmail` | Verify247 (Email): checks whether an email address is valid and deliverable, why it is or is not, and whether it belongs to a free webmail provider (optionally whether it is disposable). Always billed (service code VE). |
| Verify Phone Number | `verifyPhone` | Verify247 (Phone): checks whether a phone number is in service and accepts inbound calls, with a confidence level. Billed per hit (service code VP). |
| Verify Phone Owner | `verifyPhoneOwner` | Verify247 (Verify Owner): confirms whether a phone number is registered to the person or company you name, returning the actual subscriber name, line type and whether the line is in service. Billed per hit (service code VO). |
| Verify Postal Address | `verifyPostalAddress` | Verify247 (Postal Address): validates a US postal address and returns the USPS-standardised version with parsed components, ZIP+4, county, FIPS, congressional district, area code, timezone and delivery point barcode. Always billed (service code VA). |
