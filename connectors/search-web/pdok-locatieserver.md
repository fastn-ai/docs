---
description: "Connect PDOK Locatieserver to your product with fastn."
hidden: true
---

# PDOK Locatieserver

<img src="../../.gitbook/assets/connectors/lg/pdok-locatieserver.png" alt="PDOK Locatieserver logo">

PDOK Locatieserver is the Dutch government's free geocoding service built on the BAG, BRK and other national registers: free-text search and type-ahead suggestions for addresses, postcodes, streets, towns, municipalities and parcels in the Netherlands, lookup by id with full details and coordinates, and reverse geocoding from a point. No API key needed.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [pdok.nl](https://pdok.nl) |
| **Authentication** | No authentication |
| **Slug** | `pdokLocatieserver` |

## Use it

Add PDOK Locatieserver from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pdokLocatieserver.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Free Search</td><td><code>freeSearch</code></td><td>De Free API biedt de mogelijkheid om vrij te zoeken (klassiek geocoderen), waar zonder tussenkomst van suggesties de API direct resultaten teruggeeft op basis van de zoekopdracht. . Docs: https://api.pdok.nl/bzk/locatieserver/search/v3_1/ui/ (GET /free)</td></tr><tr><td>Lookup Location</td><td><code>lookup</code></td><td>Zodra er op basis van suggesties van de Suggest API een keuze is gemaakt, wordt de Lookup API aangeroepen, welke o.a. een (versimpelde) geometrie van de zoekopdracht teruggeeft. . Docs: https://api.pdok.nl/bzk/locatieserver/search/v3_1/ui/ (GET /lookup)</td></tr><tr><td>Reverse Geocode</td><td><code>reverseGeocode</code></td><td>De Reverse API biedt de mogelijkheid om een locatie (punt geometrie) op te geven om vervolgens verschillende gegevens in een range rondom deze locatie te ontvangen. . Docs: https://api.pdok.nl/bzk/locatieserver/search/v3_1/ui/ (GET /reverse)</td></tr><tr><td>Suggest Locations</td><td><code>suggest</code></td><td>De Suggest API biedt de mogelijkheid om een (gedeelte van een) zoekopdracht op te voeren, waarnaar er suggesties teruggegeven worden. . Docs: https://api.pdok.nl/bzk/locatieserver/search/v3_1/ui/ (GET /suggest)</td></tr></tbody></table>
