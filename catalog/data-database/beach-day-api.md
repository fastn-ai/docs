---
description: "Beach Day provides data on beaches worldwide. List beaches and countries, and get beach conditions, amenities, rules and tide predictions."
hidden: true
---

# Beach Day API

<img src="../../.gitbook/assets/connectors/lg/beach-day-api.png" alt="Beach Day API logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [beachdayapi.com](https://beachdayapi.com) |
| **Authentication** | Access token |
| **Slug** | `beachDayApi` |

## Setup

Your customers enter their access token for Beach Day API when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Beach Day API from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Beach Day API**.
2. Select **Connect** on the Beach Day API card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Beach Day API's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check API Health</td><td><code>checkApiHealth</code></td><td>Checks whether the Beach Day API service is operational. This call is free and does not spend credits.</td></tr><tr><td>Get Beach</td><td><code>getBeach</code></td><td>Retrieves the full profile of a single beach by ID, including its Beach Day Score, latest water quality, weather and ocean conditions, rules and amenities. Costs 5 credits per call.</td></tr><tr><td>Get Beach Amenities</td><td><code>getBeachAmenities</code></td><td>Retrieves the on-site amenities for a beach, such as restrooms, showers, lifeguards, parking, food and accessibility, with availability and hours. Costs 2 credits per call.</td></tr><tr><td>Get Beach Rules</td><td><code>getBeachRules</code></td><td>Retrieves the local rules for a beach, such as whether dogs, alcohol, fires, smoking, camping or drones are allowed. Costs 2 credits per call.</td></tr><tr><td>Get Tide Predictions</td><td><code>getTidePredictions</code></td><td>Retrieves tide predictions for a beach, grouped by date, with the high and low tide times and heights for each day. Costs 1 credit per call.</td></tr><tr><td>List Beach Conditions</td><td><code>listBeachConditions</code></td><td>Lists current and recent condition snapshots for a beach, newest first: water quality, weather, ocean conditions, tides and Beach Day Score, with offset and limit pagination. Costs 3 credits per call.</td></tr><tr><td>List Beaches</td><td><code>listBeaches</code></td><td>Searches and lists beaches, optionally filtered by name, state or province code, or country, with offset and limit pagination. Costs 1 credit per call.</td></tr><tr><td>List Countries</td><td><code>listCountries</code></td><td>Lists every country covered by Beach Day API with its beach count, ordered by count descending. Use the country names to filter List Beaches. Costs 1 credit per call.</td></tr><tr><td>List Scored Beaches</td><td><code>listScoredBeaches</code></td><td>Lists beaches ranked by their current Beach Day Score (0-100), highest first, with full beach profiles and offset and limit pagination. Costs 10 credits per call.</td></tr></tbody></table>

