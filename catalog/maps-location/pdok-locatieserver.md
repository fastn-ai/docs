---
description: "PDOK Locatieserver is the Dutch government geocoding service. Search and suggest Dutch addresses and places, and reverse geocode."
hidden: true
---

# PDOK Locatieserver

<img src="../../.gitbook/assets/connectors/lg/pdok-locatieserver.png" alt="PDOK Locatieserver logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [pdok.nl](https://pdok.nl) |
| **Authentication** | No sign-in needed |
| **Slug** | `pdokLocatieserver` |

## Setup

PDOK Locatieserver needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect PDOK Locatieserver from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **PDOK Locatieserver**.
2. Select **Connect** on the PDOK Locatieserver card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. PDOK Locatieserver needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use PDOK Locatieserver's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Free Search</td><td><code>freeSearch</code></td><td>De Free API biedt de mogelijkheid om vrij te zoeken (klassiek geocoderen), waar zonder tussenkomst van suggesties de API direct resultaten teruggeeft op basis van de zoekopdracht.. Docs: https://api.pdok.nl/bzk/locatieserver/search/v3_1/ui/</td></tr><tr><td>Lookup Location</td><td><code>lookup</code></td><td>Zodra er op basis van suggesties van de Suggest API een keuze is gemaakt, wordt de Lookup API aangeroepen, welke o.a. een (versimpelde) geometrie van de zoekopdracht teruggeeft.. Docs: https://api.pdok.nl/bzk/locatieserver/search/v3_1/ui/</td></tr><tr><td>Reverse Geocode</td><td><code>reverseGeocode</code></td><td>De Reverse API biedt de mogelijkheid om een locatie (punt geometrie) op te geven om vervolgens verschillende gegevens in een range rondom deze locatie te ontvangen.. Docs: https://api.pdok.nl/bzk/locatieserver/search/v3_1/ui/</td></tr><tr><td>Suggest Locations</td><td><code>suggest</code></td><td>De Suggest API biedt de mogelijkheid om een (gedeelte van een) zoekopdracht op te voeren, waarnaar er suggesties teruggegeven worden.. Docs: https://api.pdok.nl/bzk/locatieserver/search/v3_1/ui/</td></tr></tbody></table>

