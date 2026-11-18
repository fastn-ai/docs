---
description: "Postcodes.io is a free, open-source API for UK postcodes and geolocation, built on Office for National Statistics and Ordnance Survey open data."
hidden: true
---

# Postcodes.io

Postcodes.io is a free, open-source API for UK postcodes and geolocation, built on Office for National Statistics and Ordnance Survey open data. Look up, search, autocomplete and bulk-check postcodes, reverse geocode coordinates, and get outward codes, terminated and Scottish postcodes, and places. No API key needed.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [postcodes.io](https://postcodes.io) |
| **Authentication** | No authentication |
| **Actions** | 16 |
| **Events** | 0 |
| **Slug** | `postcodesIo` |

## Use it

Add Postcodes.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.postcodesIo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Postcode | `autocompletePostcode` | Get a list of full postcodes that complete a partial postcode (GET /postcodes/{postcode}/autocomplete). Docs: https://postcodes.io/docs/postcode/autocomplete |
| Bulk Lookup Postcodes | `bulkLookupPostcodes` | Get data for up to 100 postcodes in one request (POST /postcodes with a postcodes array). Postcodes that are not found come back with result null. Docs: https://postcodes.io/docs/postcode/bulk |
| Bulk Reverse Geocode Postcodes | `bulkReverseGeocodePostcodes` | Find the nearest postcodes for up to 100 longitude/latitude points in one request (POST /postcodes with a geolocations array). Each point may set its own radius, limit and widesearch. Docs: https://postcodes.io/docs/postcode/bulk-reverse-geocode |
| Get Nearest Outward Codes | `getNearestOutcodes` | List the outward codes nearest to a given outward code, closest first (GET /outcodes/{outcode}/nearest). Docs: https://postcodes.io/docs/outcode/nearest |
| Get Nearest Postcodes | `getNearestPostcodes` | List the postcodes nearest to a given postcode, closest first, each with a distance in metres (GET /postcodes/{postcode}/nearest). Docs: https://postcodes.io/docs/postcode/nearest |
| Get Random Place | `getRandomPlace` | Get a random place with all its data (GET /random/places). Docs: https://postcodes.io/docs/place/random |
| Get Random Postcode | `getRandomPostcode` | Get a random postcode with all its data, optionally inside one outward code (GET /random/postcodes). An unknown outcode returns result null. Docs: https://postcodes.io/docs/postcode/random |
| Lookup Outward Code | `lookupOutcode` | Get data for a UK outward code (first half of a postcode): centroid and the districts, wards, parishes and constituencies it covers (GET /outcodes/{outcode}). Docs: https://postcodes.io/docs/outcode/lookup |
| Lookup Place | `lookupPlace` | Get one place by its Ordnance Survey Open Names code (GET /places/{code}). Docs: https://postcodes.io/docs/place/lookup |
| Lookup Postcode | `lookupPostcode` | Get all data for one UK postcode: location, admin areas, constituencies, NHS areas, statistical codes (GET /postcodes/{postcode}). Unknown postcodes return 404 'Postcode not found'. Docs: https://postcodes.io/docs/postcode/lookup |
| Lookup Scottish Postcode | `lookupScottishPostcode` | Get Scotland-specific data for a Scottish postcode: council area, Scottish Parliament constituency, health board, data zones and more (GET /scotland/postcodes/{postcode}). Non-Scottish postcodes return 404. Docs: https://postcodes.io/docs/scottish-postcode/lookup |
| Lookup Terminated Postcode | `lookupTerminatedPostcode` | Get the termination date and last known location of a postcode that is no longer in use (GET /terminated_postcodes/{postcode}). Live or unknown postcodes return 404. Docs: https://postcodes.io/docs/terminated-postcode/lookup |
| Reverse Geocode Outward Codes | `reverseGeocodeOutcodes` | Find the outward codes nearest to a longitude/latitude point, closest first (GET /outcodes?lon=&lat=). Docs: https://postcodes.io/docs/outcode/reverse-geocode |
| Reverse Geocode Postcodes | `reverseGeocodePostcodes` | Find the postcodes nearest to a longitude/latitude point, each with a distance in metres (GET /postcodes?lon=&lat=). Docs: https://postcodes.io/docs/postcode/reverse-geocode |
| Search Places | `searchPlaces` | Find places (cities, towns, villages, suburbs and more from Ordnance Survey Open Names) by name, up to 100 (GET /places?q=). Docs: https://postcodes.io/docs/place/query |
| Search Postcodes | `searchPostcodes` | Find postcodes that start with a partial or full postcode, sorted, up to 100 (GET /postcodes?q=). Docs: https://postcodes.io/docs/postcode/query |
