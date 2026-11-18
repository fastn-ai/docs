---
description: "Beach Day API provides beach data for more than 36,000 beaches in over 100 countries: beach profiles with location and access details, water quality grades,…"
hidden: true
---

# Beach Day API

Beach Day API provides beach data for more than 36,000 beaches in over 100 countries: beach profiles with location and access details, water quality grades, weather and ocean conditions, tide predictions, local rules, amenities and the proprietary 0-100 Beach Day Score. This connector covers the complete Beach Day API v1 REST surface. Every call except the health check spends pre-paid credits from the connected account.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [beachdayapi.com](https://beachdayapi.com) |
| **Authentication** | Bearer token |
| **Actions** | 9 |
| **Events** | 0 |
| **Slug** | `beachDayApi` |

## Use it

Add Beach Day API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.beachDayApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check API Health | `checkApiHealth` | Checks whether the Beach Day API service is operational. This call is free and does not spend credits. |
| Get Beach | `getBeach` | Retrieves the full profile of a single beach by ID, including its Beach Day Score, latest water quality, weather and ocean conditions, rules and amenities. Costs 5 credits per call. |
| Get Beach Amenities | `getBeachAmenities` | Retrieves the on-site amenities for a beach, such as restrooms, showers, lifeguards, parking, food and accessibility, with availability and hours. Costs 2 credits per call. |
| Get Beach Rules | `getBeachRules` | Retrieves the local rules for a beach, such as whether dogs, alcohol, fires, smoking, camping or drones are allowed. Costs 2 credits per call. |
| Get Tide Predictions | `getTidePredictions` | Retrieves tide predictions for a beach, grouped by date, with the high and low tide times and heights for each day. Costs 1 credit per call. |
| List Beach Conditions | `listBeachConditions` | Lists current and recent condition snapshots for a beach, newest first: water quality, weather, ocean conditions, tides and Beach Day Score, with offset and limit pagination. Costs 3 credits per call. |
| List Beaches | `listBeaches` | Searches and lists beaches, optionally filtered by name, state or province code, or country, with offset and limit pagination. Costs 1 credit per call. |
| List Countries | `listCountries` | Lists every country covered by Beach Day API with its beach count, ordered by count descending. Use the country names to filter List Beaches. Costs 1 credit per call. |
| List Scored Beaches | `listScoredBeaches` | Lists beaches ranked by their current Beach Day Score (0-100), highest first, with full beach profiles and offset and limit pagination. Costs 10 credits per call. |
