---
description: "Postcodes.io is a free, open-source API for UK postcodes and geolocation, built on Office for National Statistics and Ordnance Survey open data."
hidden: true
---

# Postcodes.io

<img src="../../.gitbook/assets/connectors/lg/postcodes-io.png" alt="Postcodes.io logo">

Postcodes.io is a free, open-source API for UK postcodes and geolocation, built on Office for National Statistics and Ordnance Survey open data. Look up, search, autocomplete and bulk-check postcodes, reverse geocode coordinates, and get outward codes, terminated and Scottish postcodes, and places. No API key needed.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [postcodes.io](https://postcodes.io) |
| **Authentication** | No authentication |
| **Slug** | `postcodesIo` |

## Use it

Add Postcodes.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.postcodesIo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Autocomplete Postcode</td><td><code>autocompletePostcode</code></td><td>Get a list of full postcodes that complete a partial postcode (GET /postcodes/{postcode}/autocomplete). Docs: https://postcodes.io/docs/postcode/autocomplete</td></tr><tr><td>Bulk Lookup Postcodes</td><td><code>bulkLookupPostcodes</code></td><td>Get data for up to 100 postcodes in one request (POST /postcodes with a postcodes array). Postcodes that are not found come back with result null. Docs: https://postcodes.io/docs/postcode/bulk</td></tr><tr><td>Bulk Reverse Geocode Postcodes</td><td><code>bulkReverseGeocodePostcodes</code></td><td>Find the nearest postcodes for up to 100 longitude/latitude points in one request (POST /postcodes with a geolocations array). Each point may set its own radius, limit and widesearch. Docs: https://postcodes.io/docs/postcode/bulk-reverse-geocode</td></tr><tr><td>Get Nearest Outward Codes</td><td><code>getNearestOutcodes</code></td><td>List the outward codes nearest to a given outward code, closest first (GET /outcodes/{outcode}/nearest). Docs: https://postcodes.io/docs/outcode/nearest</td></tr><tr><td>Get Nearest Postcodes</td><td><code>getNearestPostcodes</code></td><td>List the postcodes nearest to a given postcode, closest first, each with a distance in metres (GET /postcodes/{postcode}/nearest). Docs: https://postcodes.io/docs/postcode/nearest</td></tr><tr><td>Get Random Place</td><td><code>getRandomPlace</code></td><td>Get a random place with all its data (GET /random/places). Docs: https://postcodes.io/docs/place/random</td></tr><tr><td>Get Random Postcode</td><td><code>getRandomPostcode</code></td><td>Get a random postcode with all its data, optionally inside one outward code (GET /random/postcodes). An unknown outcode returns result null. Docs: https://postcodes.io/docs/postcode/random</td></tr><tr><td>Lookup Outward Code</td><td><code>lookupOutcode</code></td><td>Get data for a UK outward code (first half of a postcode): centroid and the districts, wards, parishes and constituencies it covers (GET /outcodes/{outcode}). Docs: https://postcodes.io/docs/outcode/lookup</td></tr><tr><td>Lookup Place</td><td><code>lookupPlace</code></td><td>Get one place by its Ordnance Survey Open Names code (GET /places/{code}). Docs: https://postcodes.io/docs/place/lookup</td></tr><tr><td>Lookup Postcode</td><td><code>lookupPostcode</code></td><td>Get all data for one UK postcode: location, admin areas, constituencies, NHS areas, statistical codes (GET /postcodes/{postcode}). Unknown postcodes return 404 'Postcode not found'. Docs: https://postcodes.io/docs/postcode/lookup</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Lookup Scottish Postcode</td><td><code>lookupScottishPostcode</code></td><td>Get Scotland-specific data for a Scottish postcode: council area, Scottish Parliament constituency, health board, data zones and more (GET /scotland/postcodes/{postcode}). Non-Scottish postcodes return 404. Docs: https://postcodes.io/docs/scottish-postcode/lookup</td></tr><tr><td>Lookup Terminated Postcode</td><td><code>lookupTerminatedPostcode</code></td><td>Get the termination date and last known location of a postcode that is no longer in use (GET /terminated_postcodes/{postcode}). Live or unknown postcodes return 404. Docs: https://postcodes.io/docs/terminated-postcode/lookup</td></tr><tr><td>Reverse Geocode Outward Codes</td><td><code>reverseGeocodeOutcodes</code></td><td>Find the outward codes nearest to a longitude/latitude point, closest first (GET /outcodes?lon=&amp;lat=). Docs: https://postcodes.io/docs/outcode/reverse-geocode</td></tr><tr><td>Reverse Geocode Postcodes</td><td><code>reverseGeocodePostcodes</code></td><td>Find the postcodes nearest to a longitude/latitude point, each with a distance in metres (GET /postcodes?lon=&amp;lat=). Docs: https://postcodes.io/docs/postcode/reverse-geocode</td></tr><tr><td>Search Places</td><td><code>searchPlaces</code></td><td>Find places (cities, towns, villages, suburbs and more from Ordnance Survey Open Names) by name, up to 100 (GET /places?q=). Docs: https://postcodes.io/docs/place/query</td></tr><tr><td>Search Postcodes</td><td><code>searchPostcodes</code></td><td>Find postcodes that start with a partial or full postcode, sorted, up to 100 (GET /postcodes?q=). Docs: https://postcodes.io/docs/postcode/query</td></tr></tbody></table>

</details>
