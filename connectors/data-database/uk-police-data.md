---
description: "data.police.uk is the UK Home Office's open police data API for England, Wales and Northern Ireland."
hidden: true
---

# UK Police Data

<img src="../../.gitbook/assets/connectors/lg/uk-police-data.png" alt="UK Police Data logo">

data.police.uk is the UK Home Office's open police data API for England, Wales and Northern Ireland. Get forces and senior officers, street-level crimes and outcomes by point, area or location, crime categories, neighbourhoods with teams, events, priorities and boundaries, and stop and search records. No API key needed (15 requests per second).

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [data.police.uk](https://data.police.uk) |
| **Authentication** | No authentication |
| **Slug** | `ukPoliceData` |

## Use it

Add UK Police Data from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ukPoliceData.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Crime Data Last Updated | `getLastUpdated` | Get the month of the latest crime data (GET /crime-last-updated). Docs: https://data.police.uk/docs/method/crime-last-updated/ |
| Get Force | `getForce` | Get a force's details: description, website, phone and engagement channels (GET /forces/{force}). Docs: https://data.police.uk/docs/method/force/ |
| Get Neighbourhood | `getNeighbourhood` | Get a neighbourhood's details: contacts, centre, links and population (GET /{force}/{neighbourhood}). Docs: https://data.police.uk/docs/method/neighbourhood/ |
| Get Neighbourhood Boundary | `getNeighbourhoodBoundary` | Get the boundary of a neighbourhood as a list of lat/lng points (GET /{force}/{neighbourhood}/boundary). Docs: https://data.police.uk/docs/method/neighbourhood-boundary/ |
| Get Outcomes for Crime | `getCrimeOutcomes` | Get a crime and all of its outcomes by the crime's persistent id (GET /outcomes-for-crime/{persistent_id}). Docs: https://data.police.uk/docs/method/outcomes-for-crime/ |
| List Available Dates | `listAvailableDates` | List the months with crime data and, for each, the forces that provided stop and search data (GET /crimes-street-dates). Docs: https://data.police.uk/docs/method/crimes-street-dates/ |
| List Crime Categories | `listCrimeCategories` | List the valid crime categories for a month (GET /crime-categories). Docs: https://data.police.uk/docs/method/crime-categories/ |
| List Crimes at Location | `listCrimesAtLocation` | List crimes mapped to one location id, or to the location nearest a point, for a month (GET /crimes-at-location). Docs: https://data.police.uk/docs/method/crimes-at-location/ |
| List Crimes with No Location | `listCrimesWithNoLocation` | List crimes a force reported that could not be mapped to a location, for a category and month (GET /crimes-no-location). Docs: https://data.police.uk/docs/method/crimes-no-location/ |
| List Forces | `listForces` | List all police forces in England, Wales and Northern Ireland with their ids (GET /forces). Docs: https://data.police.uk/docs/method/forces/ |
| List Neighbourhood Events | `listNeighbourhoodEvents` | List upcoming events in a neighbourhood (GET /{force}/{neighbourhood}/events). Docs: https://data.police.uk/docs/method/neighbourhood-events/ |
| List Neighbourhood Priorities | `listNeighbourhoodPriorities` | List a neighbourhood's policing priorities and the action taken (GET /{force}/{neighbourhood}/priorities). Docs: https://data.police.uk/docs/method/neighbourhood-priorities/ |
| List Neighbourhood Team | `listNeighbourhoodTeam` | List the officers in a neighbourhood's policing team (GET /{force}/{neighbourhood}/people). Docs: https://data.police.uk/docs/method/neighbourhood-team/ |
| List Neighbourhoods | `listNeighbourhoods` | List a force's neighbourhoods (GET /{force}/neighbourhoods). Docs: https://data.police.uk/docs/method/neighbourhoods/ |
| List Senior Officers | `listSeniorOfficers` | List a force's senior officers with rank, bio and contact links (GET /forces/{force}/people). Docs: https://data.police.uk/docs/method/senior-officers/ |
| List Stop and Searches at Location | `listStopsAtLocation` | List stop and searches at a location id for a month (GET /stops-at-location). Docs: https://data.police.uk/docs/method/stops-at-location/ |
| List Stop and Searches by Area | `listStopsByArea` | List stop and searches within 1 mile of a point, or in a custom polygon, for a month (GET /stops-street). Docs: https://data.police.uk/docs/method/stops-street/ |
| List Stop and Searches by Force | `listStopsByForce` | List all stop and searches reported by a force for a month (GET /stops-force). Docs: https://data.police.uk/docs/method/stops-force/ |
| List Stop and Searches with No Location | `listStopsWithNoLocation` | List a force's stop and searches that could not be mapped to a location, for a month (GET /stops-no-location). Docs: https://data.police.uk/docs/method/stops-no-location/ |
| List Street-Level Crimes | `listStreetCrimes` | List street-level crimes in a category within 1 mile of a point, or inside a custom polygon, for a month (GET /crimes-street/{category}). Docs: https://data.police.uk/docs/method/crime-street/ |
| List Street-Level Outcomes | `listStreetOutcomes` | List outcomes of crimes at a location id, within 1 mile of a point, or in a custom polygon, for a month (GET /outcomes-at-location). Docs: https://data.police.uk/docs/method/outcomes-at-location/ |
| Locate Neighbourhood | `locateNeighbourhood` | Find the force and neighbourhood responsible for a point (GET /locate-neighbourhood?q=lat,lng). Docs: https://data.police.uk/docs/method/neighbourhood-locate/ |
