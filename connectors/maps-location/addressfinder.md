---
description: "Addressfinder provides address autocomplete, address verification, location and points-of-interest lookup, reverse geocoding, email verification and phone…"
hidden: true
---

# Addressfinder

<img src="../../.gitbook/assets/connectors/addressfinder.png" alt="Addressfinder logo" width="64">

Addressfinder provides address autocomplete, address verification, location and points-of-interest lookup, reverse geocoding, email verification and phone verification for Australia, New Zealand and 16 international countries. This connector wraps the Addressfinder API v2 at https://api.addressfinder.io/api, authenticating with OAuth 2.0 client credentials.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [addressfinder.com](https://addressfinder.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `addressfinder` |

## Use it

Add Addressfinder from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.addressfinder.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Australian Address Metadata | `getAustralianAddressMetadata` | Loads the full metadata for a single Australian address selected from Search Australian Addresses, including parsed address components, postcode, GPS coordinates, G-NAF and Australia Post identifiers, local government area and census statistical areas. Supply exactly one of Address ID, G-NAF ID or DPID to identify the address. |
| Get Australian Location Metadata | `getAustralianLocationMetadata` | Loads the full metadata for an Australian location selected from Search Australian Locations, including the location type, state, postcode, street details and GPS coordinates. |
| Get International Address Metadata | `getInternationalAddressMetadata` | Loads the full metadata for an international address selected from Search International Addresses, including formatted address lines, city, state, postcode, country, parsed street and unit components and optional GPS coordinates. The country code must match the one used for the original search. |
| Get New Zealand Address Metadata | `getNewZealandAddressMetadata` | Loads the full metadata for a single New Zealand address selected from Search New Zealand Addresses or Reverse Geocode New Zealand Address, including parsed address components, postal lines, GPS coordinates, LINZ and NZ Post identifiers and Statistics New Zealand geographic areas. Supply either the Address PXID or the NZ Post DPID. |
| Get New Zealand Location Metadata | `getNewZealandLocationMetadata` | Loads the metadata for a New Zealand location selected from Search New Zealand Locations, including the canonical location name, geographic coordinates, city and region. Fields not applicable to the location type, such as street or suburb for a region, are omitted. |
| Get New Zealand Point Of Interest Metadata | `getNewZealandPointOfInterestMetadata` | Loads the full metadata for a New Zealand point of interest selected from Search New Zealand Points Of Interest, including its name, geographic coordinates, linked street address, postal lines, territorial authority and LINZ identifiers. |
| Reverse Geocode New Zealand Address | `reverseGeocodeNewZealandAddress` | Takes a WGS84 longitude and latitude and returns the nearest matching New Zealand addresses ordered by distance. Use the returned pxid with Get New Zealand Address Metadata to load the full address record. |
| Search Australian Addresses | `searchAustralianAddresses` | Searches the Australian Addressfinder database for addresses closely matching a partial address string and returns a ranked list of completions. Use the returned id with Get Australian Address Metadata to load the full address record. Results can be sourced from the Geoscape G-NAF physical address dataset, the Australia Post PAF postal dataset, or both. |
| Search Australian Locations | `searchAustralianLocations` | Searches Australian locations - streets, localities (suburbs) and states - matching a partial query string, returning a ranked list of completions. Use the returned id with Get Australian Location Metadata to load the full location record. |
| Search International Addresses | `searchInternationalAddresses` | Searches addresses in a supported international country for matches to a partial address string and returns a ranked list of completions. Use the returned id with Get International Address Metadata to load the full address record. |

<details>

<summary>See 7 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Search New Zealand Addresses | `searchNewZealandAddresses` | Searches the New Zealand Addressfinder database for addresses closely matching a partial address string and returns a ranked list of completions. Use the returned pxid with Get New Zealand Address Metadata to load the full address record. Results can be filtered by NZ Post delivery status, PO Box or rural addresses, region and match strictness. |
| Search New Zealand Locations | `searchNewZealandLocations` | Searches New Zealand locations - streets, suburbs, cities and regions - matching a partial query string, returning a ranked list of completions. Use the returned pxid with Get New Zealand Location Metadata to load the full location record. The street, suburb, city and region filters are applied additively, so exclude the location types you do not want. |
| Search New Zealand Points Of Interest | `searchNewZealandPointsOfInterest` | Searches New Zealand points of interest - named businesses, buildings and landmarks - matching a partial name or address, returning a ranked list of completions. Use the returned id with Get New Zealand Point Of Interest Metadata to load the full record. |
| Verify Australian Address | `verifyAustralianAddress` | Verifies a free-text Australian address that may contain spelling mistakes or other errors against the Geoscape G-NAF and Australia Post PAF databases, returning the corrected, fully parsed address record and whether a match was found. At least one of the G-NAF or PAF dataset flags must be supplied, otherwise the API returns error code 1000. |
| Verify Email Address | `verifyEmailAddress` | Verifies an email address by validating its syntax, checking that the domain is configured to receive mail, confirming the mailbox exists, and identifying the email service provider. Returns a verified state plus deliverability, disposable, role-account, public-provider and catch-all indicators. Requires the email scope on your Addressfinder credentials. |
| Verify New Zealand Address | `verifyNewZealandAddress` | Verifies a free-text New Zealand address that may contain spelling mistakes or other errors against the Addressfinder database, returning the corrected, fully parsed address record, whether a match was found, and any part of the input that could not be matched. |
| Verify Phone Number | `verifyPhoneNumber` | Verifies a phone number by checking its syntax and number range and then performing a live network check for connection status. Returns the line type and status plus the number formatted in national and international notation. Requires the phone scope on your Addressfinder credentials. |

</details>
