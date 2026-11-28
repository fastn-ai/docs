---
description: "UK Police Data is open police data for England, Wales and Northern Ireland. Read forces, neighbourhoods, crime categories and crime outcomes."
hidden: true
---

# UK Police Data

<img src="../../.gitbook/assets/connectors/lg/uk-police-data.png" alt="UK Police Data logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [data.police.uk](https://data.police.uk) |
| **Authentication** | No sign-in needed |
| **Slug** | `ukPoliceData` |

## Setup

UK Police Data needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect UK Police Data from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **UK Police Data**.
2. Select **Connect** on the UK Police Data card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. UK Police Data needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use UK Police Data's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Crime Data Last Updated</td><td><code>getLastUpdated</code></td><td>Get the month of the latest crime data Docs: https://data.police.uk/docs/method/crime-last-updated/</td></tr><tr><td>Get Force</td><td><code>getForce</code></td><td>Get a force's details: description, website, phone and engagement channels Docs: https://data.police.uk/docs/method/force/</td></tr><tr><td>Get Neighbourhood</td><td><code>getNeighbourhood</code></td><td>Get a neighbourhood's details: contacts, centre, links and population Docs: https://data.police.uk/docs/method/neighbourhood/</td></tr><tr><td>Get Neighbourhood Boundary</td><td><code>getNeighbourhoodBoundary</code></td><td>Get the boundary of a neighbourhood as a list of lat/lng points Docs: https://data.police.uk/docs/method/neighbourhood-boundary/</td></tr><tr><td>Get Outcomes for Crime</td><td><code>getCrimeOutcomes</code></td><td>Get a crime and all of its outcomes by the crime's persistent id Docs: https://data.police.uk/docs/method/outcomes-for-crime/</td></tr><tr><td>List Available Dates</td><td><code>listAvailableDates</code></td><td>List the months with crime data and, for each, the forces that provided stop and search data Docs: https://data.police.uk/docs/method/crimes-street-dates/</td></tr><tr><td>List Crime Categories</td><td><code>listCrimeCategories</code></td><td>List the valid crime categories for a month Docs: https://data.police.uk/docs/method/crime-categories/</td></tr><tr><td>List Crimes at Location</td><td><code>listCrimesAtLocation</code></td><td>List crimes mapped to one location id, or to the location nearest a point, for a month Docs: https://data.police.uk/docs/method/crimes-at-location/</td></tr><tr><td>List Crimes with No Location</td><td><code>listCrimesWithNoLocation</code></td><td>List crimes a force reported that could not be mapped to a location, for a category and month Docs: https://data.police.uk/docs/method/crimes-no-location/</td></tr><tr><td>List Forces</td><td><code>listForces</code></td><td>List all police forces in England, Wales and Northern Ireland with their ids Docs: https://data.police.uk/docs/method/forces/</td></tr></tbody></table>

<details>

<summary>View 12 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Neighbourhood Events</td><td><code>listNeighbourhoodEvents</code></td><td>List upcoming events in a neighbourhood Docs: https://data.police.uk/docs/method/neighbourhood-events/</td></tr><tr><td>List Neighbourhood Priorities</td><td><code>listNeighbourhoodPriorities</code></td><td>List a neighbourhood's policing priorities and the action taken Docs: https://data.police.uk/docs/method/neighbourhood-priorities/</td></tr><tr><td>List Neighbourhood Team</td><td><code>listNeighbourhoodTeam</code></td><td>List the officers in a neighbourhood's policing team Docs: https://data.police.uk/docs/method/neighbourhood-team/</td></tr><tr><td>List Neighbourhoods</td><td><code>listNeighbourhoods</code></td><td>List a force's neighbourhoods Docs: https://data.police.uk/docs/method/neighbourhoods/</td></tr><tr><td>List Senior Officers</td><td><code>listSeniorOfficers</code></td><td>List a force's senior officers with rank, bio and contact links Docs: https://data.police.uk/docs/method/senior-officers/</td></tr><tr><td>List Stop and Searches at Location</td><td><code>listStopsAtLocation</code></td><td>List stop and searches at a location id for a month Docs: https://data.police.uk/docs/method/stops-at-location/</td></tr><tr><td>List Stop and Searches by Area</td><td><code>listStopsByArea</code></td><td>List stop and searches within 1 mile of a point, or in a custom polygon, for a month Docs: https://data.police.uk/docs/method/stops-street/</td></tr><tr><td>List Stop and Searches by Force</td><td><code>listStopsByForce</code></td><td>List all stop and searches reported by a force for a month Docs: https://data.police.uk/docs/method/stops-force/</td></tr><tr><td>List Stop and Searches with No Location</td><td><code>listStopsWithNoLocation</code></td><td>List a force's stop and searches that could not be mapped to a location, for a month Docs: https://data.police.uk/docs/method/stops-no-location/</td></tr><tr><td>List Street-Level Crimes</td><td><code>listStreetCrimes</code></td><td>List street-level crimes in a category within 1 mile of a point, or inside a custom polygon, for a month Docs: https://data.police.uk/docs/method/crime-street/</td></tr><tr><td>List Street-Level Outcomes</td><td><code>listStreetOutcomes</code></td><td>List outcomes of crimes at a location id, within 1 mile of a point, or in a custom polygon, for a month Docs: https://data.police.uk/docs/method/outcomes-at-location/</td></tr><tr><td>Locate Neighbourhood</td><td><code>locateNeighbourhood</code></td><td>Find the force and neighbourhood responsible for a point,lng). Docs: https://data.police.uk/docs/method/neighbourhood-locate/</td></tr></tbody></table>

</details>

