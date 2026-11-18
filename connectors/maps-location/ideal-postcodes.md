---
description: "Ideal Postcodes provides UK and international address data: postcode lookup, address search and autocomplete, UDPRN and UMPRN retrieval, reverse geocoding,…"
hidden: true
---

# Ideal Postcodes

<img src="../../.gitbook/assets/connectors/lg/ideal-postcodes.png" alt="Ideal Postcodes logo">

Ideal Postcodes provides UK and international address data: postcode lookup, address search and autocomplete, UDPRN and UMPRN retrieval, reverse geocoding, address cleansing, place search, and email and phone number validation, plus API key management for usage, limits, licensees and configurations. This connector covers the full Ideal Postcodes v1 REST API.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [ideal-postcodes.co.uk](https://ideal-postcodes.co.uk) |
| **Authentication** | Credentials you enter |
| **Slug** | `idealPostcodes` |

## Use it

Add Ideal Postcodes from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.idealPostcodes.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Address | `autocompleteAddress` | Returns address suggestions for a partial address query, for use in address autocomplete inputs. Each suggestion carries an address id and UDPRN that can be resolved to a full address with Resolve Address. Supports geographic and postcode filters plus ranking bias parameters. |
| Cancel Licensee | `cancelLicensee` | Cancels a licensee registered against the connected API key, revoking that licensee's key. Requires the account user token. |
| Cleanse Address | `cleanseAddress` | Matches a freeform or impaired address string to the closest known address and returns the cleansed address with a confidence score between 0 and 1 and match level indicators describing how closely each element matched. |
| Create Configuration | `createConfiguration` | Stores a named configuration payload against the connected API key, for example settings for a hosted address-capture integration. Requires the account user token. |
| Create Licensee | `createLicensee` | Creates a licensee against the connected API key, issuing that licensee its own key with optional allowed URLs and daily lookup limit. Requires the account user token. |
| Delete Configuration | `deleteConfiguration` | Deletes a stored configuration from the connected API key by name. Requires the account user token. |
| Find Place | `findPlace` | Searches geographical places worldwide, returning place suggestions with a name, descriptive name, country and place id that can be resolved with Resolve Place. |
| Get Key Availability | `getKeyAvailability` | Reports whether the connected API key is currently able to serve lookups, along with the contexts and country datasets it can search. Requires no user token. |
| Get Key Details | `getKeyDetails` | Retrieves the configuration of the connected API key, including its name, lookup balance, daily, monthly and individual limits, allowed URLs, notification settings, enabled datasets and automated top-up configuration. Requires the account user token. |
| Get Key Lookup Logs | `getKeyLookupLogs` | Downloads the lookup history for the connected API key as CSV over an optional time window, optionally filtered by licensee. Requires the account user token. |
| Get Key Usage | `getKeyUsage` | Returns lookup usage statistics for the connected API key over an optional time window, broken down by day and resource, and optionally filtered by tags or licensee. Requires the account user token. |
| List Configurations | `listConfigurations` | Lists the stored configuration payloads associated with the connected API key, used to drive hosted address-capture integrations. Requires the account user token. |
| List Licensees | `listLicensees` | Lists the licensees registered against the connected API key, with cursor pagination and an optional search query. Requires the account user token. |
| Lookup Postcode | `lookupPostcode` | Returns every address registered at a UK postcode, with full Royal Mail PAF address elements, geolocation and administrative area data. |
| Mint Signup Token | `mintSignupToken` | Mints a one-shot signup token and returns a prefilled Ideal Postcodes account signup URL for a new customer to complete. Poll the returned token with Poll Signup Token to collect the new account's first API key once signup is finished. No API key is required for this request. |
| Poll Signup Token | `pollSignupToken` | Polls a signup token minted with Mint Signup Token. Returns HTTP 202 with status 'pending' while the user has not completed signup, HTTP 200 with the new account's credentials exactly once when signup completes, and HTTP 410 after the token has expired or the credentials have already been collected. |
| Regenerate Licensee Key | `regenerateLicenseeKey` | Issues a new key for a licensee registered against the connected API key, invalidating the previous licensee key. Requires the account user token. |
| Resolve Address | `resolveAddress` | Resolves an address suggestion id returned by Autocomplete Address into the full UK address record. |
| Resolve Place | `resolvePlace` | Resolves a place id returned by Find Place into the full place record, including geolocation, country, dataset and native source attributes such as alternate names and time zone. |
| Retrieve Address By UDPRN | `retrieveAddressByUdprn` | Retrieves a single address by its Unique Delivery Point Reference Number (UDPRN), returning the full address record. |
| Retrieve Address By UMPRN | `retrieveAddressByUmprn` | Retrieves a single multiple-residence address by its Unique Multiple Residence Reference Number (UMPRN), returning the full address record. |
| Retrieve Configuration | `retrieveConfiguration` | Retrieves a stored configuration payload by name from the connected API key. |
| Retrieve Licensee | `retrieveLicensee` | Retrieves a single licensee registered against the connected API key by licensee key. Requires the account user token. |
| Search Addresses | `searchAddresses` | Searches the address database by free-text query or by reverse geocoding a longitude and latitude, returning full address records with pagination. Supports postcode, town, country, UPRN and geospatial filters plus ranking bias parameters. |
| Update Configuration | `updateConfiguration` | Replaces the payload of a stored configuration on the connected API key. Requires the account user token. |
| Update Key Details | `updateKeyDetails` | Updates the configuration of the connected API key: its name, daily, monthly and per-IP lookup limits, allowed URLs, data retention period and notification emails. Only the fields supplied are changed. Requires the account user token. |
| Update Licensee | `updateLicensee` | Updates a licensee registered against the connected API key, changing its name, address, postcode, allowed URLs or daily lookup limit. Requires the account user token. Note: the live API routes this update over POST; the PUT method documented in the OpenAPI specification returns a router-level 404. |
| Validate Email Address | `validateEmailAddress` | Validates an email address and reports whether it is deliverable, a catch-all, a free provider, a role account or disposable, with spelling suggestions where available. |
| Validate Phone Number | `validatePhoneNumber` | Validates a phone number and returns national and international formats, country details and carrier information, optionally performing a live current-carrier lookup. |
