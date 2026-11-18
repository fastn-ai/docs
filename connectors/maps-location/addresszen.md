---
description: "AddressZen address autocomplete, verification and data quality API."
hidden: true
---

# AddressZen

<img src="../../.gitbook/assets/connectors/lg/addresszen.png" alt="AddressZen logo">

AddressZen address autocomplete, verification and data quality API. Search and verify US and international addresses (USPS CASS-certified), autocomplete and retrieve addresses, look up UK postcodes/UDPRN/UMPRN, find and resolve geographic places, validate email addresses and phone numbers, and manage API keys, licensees, configurations and usage.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [addresszen.com](https://addresszen.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `addresszen` |

## Use it

Add AddressZen from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.addresszen.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Licensee | `cancelLicensee` | Cancels a licensee of the connected API key, permanently rendering that licensee key unusable for lookups. This cannot be undone. Requires the account User Token; without it the API returns 401 code 4011 Forbidden. |
| Create Configuration | `createConfiguration` | Creates a named configuration object against the connected API key, storing a serialized settings payload of up to 65536 characters that front-end integrations can fetch by name. Requires the account User Token; without it the API returns 401 code 4011 Forbidden. |
| Create Licensee | `createLicensee` | Creates a licensee under the connected API key so lookups can be attributed and rate limited per end customer. Returns the new licensee including its own lookup key. Requires the account User Token; without it the API returns 401 code 4011 Forbidden. SECURITY: the response contains a live licensee key - do not log or forward it. |
| Delete Configuration | `deleteConfiguration` | Permanently deletes a configuration object from the connected API key by its name. Any front-end integration fetching that configuration will stop receiving it. Requires the account User Token; without it the API returns 401 code 4011 Forbidden. |
| Download Key Lookup Logs | `downloadKeyLookupLogs` | Downloads a CSV of individual lookups made on the connected API key over a date range, including the query, the result and the tags attached to each request. Optionally restricted to one licensee. The response is CSV text, not JSON. Requires the account User Token; without it the API returns 401 code 4011 Forbidden. The CSV can contain personal data from past lookups - handle it accordingly. |
| Find Address | `findAddress` | Address autocomplete. Returns address suggestions for a partial address string, ranked by relevance, for search-as-you-type address forms. Each suggestion is a display label plus an id - call Retrieve Address (US) or Retrieve Address (UK) with that id to get the full address. This search step is free; the retrieve step is the one that decrements your lookup balance. AddressZen rate limits and then suspends keys that autocomplete without ever resolving suggestions. |
| Find Place | `findPlace` | Geographic place autocomplete. Searches cities, towns and administrative areas across countries and returns a list of place suggestions, each with a display name and a place id. Pass that id to Resolve Place to get coordinates, timezone and GeoNames metadata. |
| Get Key Availability | `getKeyAvailability` | Returns public information about the connected API key: whether it is currently usable for lookups, the search contexts (countries) it can serve, and the context most likely to apply. Needs no user token, so this is the cheapest way to confirm a key is live. NOTE: the key is carried in the URL path by the vendor's route design, so it appears in this action's request URL. |
| Get Key Details | `getKeyDetails` | Returns private settings for the connected API key: its name, remaining lookup balance, daily, monthly and per-IP limits, allowed URLs, licensed datasets, search contexts, data redaction period and email notification settings. Requires the account User Token; without it the API returns 401 code 4011 Forbidden. NOTE: both the key and the user token are carried in the URL by the vendor's route design, so they appear in this action's request URL. |
| Get Key Usage Statistics | `getKeyUsage` | Reports the number of lookups consumed on the connected API key over a range of days, optionally broken down by tag or restricted to a single licensee. Requires the account User Token; without it the API returns 401 code 4011 Forbidden. |

<details>

<summary>See 21 more actions</summary>

* **List Configurations** `listConfigurations`: Lists the named configuration objects stored against the connected API key. Configurations hold serialized settings for AddressZen front-end integrations such as the Address Lookup widget, so a deployed page can fetch its options by name. Requires the account User Token; without it the API returns 401 code 4011 Forbidden.
* **List Licensees** `listLicensees`: Lists the licensees attached to the connected API key, with paging and an optional name search. Requires the account User Token; without it the API returns 401 code 4011 Forbidden. SECURITY: each licensee record contains that licensee's own usable lookup key, so this response carries live credentials - do not log or forward it.
* **Look Up Postcode** `lookupPostcode`: Returns every address at a UK postcode. Undocumented in the AddressZen OpenAPI specification but live on the v1 API. Requires a key licensed for the UK Postcode Address File - an unlicensed key returns 4015 Inadequate licence. Each page of addresses counts against your lookup balance.
* **Look Up UDPRN** `lookupUdprn`: Looks up a delivery point address by its UDPRN (Unique Delivery Point Reference Number) on the dedicated /udprn resource. Undocumented in the AddressZen OpenAPI specification but live on the v1 API. Requires a key licensed for the UK Postcode Address File; an unknown or unlicensed UDPRN returns 4044 No UDPRN found. Counts as one paid lookup.
* **Look Up UMPRN** `lookupUmprn`: Looks up a multiple-residence address by its UMPRN (Unique Multiple Residence Reference Number). Undocumented in the AddressZen OpenAPI specification but live on the v1 API. Requires a key licensed for the UK Multiple Residence dataset; an unknown or unlicensed UMPRN returns 4046 No UMPRN found. Counts as one paid lookup.
* **Mint CLI Signup Token** `mintCliSignupToken`: Mints a one-shot CLI signup token and returns a prefilled AddressZen signup URL. The person opens that URL, clears the captcha, accepts the Terms of Service and creates the account; you then poll Poll CLI Signup Token until the credentials are issued. Minting a token creates no account on its own and needs no API key.
* **Poll CLI Signup Token** `pollCliSignupToken`: Polls a CLI signup token minted by Mint CLI Signup Token. Returns 202 Accepted with code 2020 Pending while the person has not finished signing up (and for a token the API has never seen), 200 with the new account's user token, test API key and user id once signup completes, and 410 Gone with code 4100 afterwards because the credentials are released exactly once. SECURITY: a 200 response contains live account credentials - do not log or forward it.
* **Regenerate Licensee Key** `regenerateLicenseeKey`: Issues a new lookup key for an existing licensee and invalidates the old one, for use when a licensee key has been exposed. Requires the account User Token; without it the API returns 401 code 4011 Forbidden. SECURITY: the response contains the new live licensee key - do not log or forward it.
* **Resolve Place** `resolvePlace`: Resolves a place suggestion id returned by Find Place into full place details, including the place name, country, administrative divisions, latitude and longitude, timezone and GeoNames metadata. An id that resolves to nothing returns 404.
* **Retrieve Address (UK Format)** `retrieveAddressGbr`: Resolves an autocomplete suggestion id from Find Address into a full address record in UK format (line_1, line_2, line_3, post_town, postcode and PAF fields). Undocumented sibling of Retrieve Address (US Format) - 'usa' and 'gbr' are the only two output formats the API accepts. This is the CHARGED step of address autocomplete and requires a key licensed for the UK PAF dataset.
* **Retrieve Address (US Format)** `retrieveAddressUsa`: Resolves an autocomplete suggestion id from Find Address into a full address record in US format (line_1, line_2, city, state, zip_code and more). This is the CHARGED step of address autocomplete - a successful retrieval decrements your lookup balance. An id that resolves to no address returns 404.
* **Retrieve Address by UDPRN** `retrieveAddressByUdprn`: Retrieves a single address record from the /addresses collection by its UDPRN (Unique Delivery Point Reference Number). Undocumented in the AddressZen OpenAPI specification but live on the v1 API. Requires a key licensed for the UK Postcode Address File; an unknown or unlicensed UDPRN returns 4044 No UDPRN found. Counts as one paid lookup.
* **Retrieve Configuration** `retrieveConfiguration`: Returns a single configuration object stored against the connected API key, looked up by its name, with its serialized payload. This route is the one a deployed front-end integration calls, so unlike the other configuration routes it takes no User Token.
* **Retrieve Licensee** `retrieveLicensee`: Returns a single licensee of the connected API key by its licensee key, including its name, address, allowed URLs and daily lookup limit. Requires the account User Token; without it the API returns 401 code 4011 Forbidden.
* **Search Addresses** `searchAddresses`: Full address search. Returns complete address records (not suggestions) matching a free-text query, optionally narrowed by postcode or post town, with paging. Undocumented in the AddressZen OpenAPI specification but live on the v1 API. Requires a key licensed for the dataset being queried - an unlicensed key returns 4015 Inadequate licence. Each returned page counts against your lookup balance.
* **Update Configuration** `updateConfiguration`: Replaces the serialized payload of an existing configuration object on the connected API key, addressed by its name. Requires the account User Token; without it the API returns 401 code 4011 Forbidden.
* **Update Key Details** `updateKeyDetails`: Updates the connected API key's settings: display name, daily, monthly and per-IP lookup limits, allowed URLs, data redaction period and email notification preferences. Only the fields you supply are changed. Requires the account User Token; without it the API returns 401 code 4011 Forbidden.
* **Update Licensee** `updateLicensee`: Updates a licensee of the connected API key: its name, address, postcode, allowed URLs and daily lookup limit. NOTE: AddressZen's published OpenAPI specification documents this route as PUT, but the live API only implements POST - a PUT returns the same '404 Page not found' as a route that does not exist. Requires the account User Token; without it the API returns 401 code 4011 Forbidden.
* **Validate Email Address** `validateEmail`: Validates a single email address: syntax, domain and mailbox checks, plus flags for disposable, role and free-provider addresses. Queries longer than 320 characters are rejected. Each query counts as one paid lookup, including addresses that turn out to be invalid.
* **Validate Phone Number** `validatePhoneNumber`: Validates a single phone number and returns its line type, country, formatting variants and network operator. The number must include a country code, e.g. '+442071128019'. Each query counts as one paid lookup, including a number that fails to parse.
* **Verify Address** `verifyAddress`: Validates, corrects and standardizes a US address against USPS CASS-certified data. Accepts either a single freeform address string or a first address line plus ZIP code, or city and state. Returns the standardized address, a deliverability verdict and the corrections applied. Each verified address counts as one paid lookup.

</details>
