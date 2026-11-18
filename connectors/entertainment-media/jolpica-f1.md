---
description: "Jolpica F1 is the free, open-source successor to the Ergast Formula 1 API, with data from 1950 to today."
hidden: true
---

# Jolpica F1

Jolpica F1 is the free, open-source successor to the Ergast Formula 1 API, with data from 1950 to today. Get seasons, circuits, constructors, drivers, race calendars, race, sprint and qualifying results, pit stops, lap times, championship standings and finishing statuses. No API key needed (500 requests per hour).

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [jolpi.ca](https://jolpi.ca) |
| **Authentication** | No authentication |
| **Actions** | 39 |
| **Events** | 0 |
| **Slug** | `jolpicaF1` |

## Use it

Add Jolpica F1 from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.jolpicaF1.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Circuit | `getCircuit` | Get one circuit by its id (GET /ergast/f1/circuits/{circuitId}.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/circuits.md |
| Get Constructor | `getConstructor` | Get one constructor by its id (GET /ergast/f1/constructors/{constructorId}.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/constructors.md |
| Get Constructor Standings | `getConstructorStandings` | Get the constructors' championship standings at the end of a season (from 1958) (GET /ergast/f1/{season}/constructorstandings.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/constructorStandings.md |
| Get Constructor Standings After Round | `getConstructorStandingsAfterRound` | Get the constructors' championship standings after a given round (GET /ergast/f1/{season}/{round}/constructorstandings.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/constructorStandings.md |
| Get Driver | `getDriver` | Get one driver by id (GET /ergast/f1/drivers/{driverId}.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/drivers.md |
| Get Driver Laps | `getDriverLaps` | Get one driver's lap timings in one race (GET /ergast/f1/{season}/{round}/drivers/{driverId}/laps.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/laps.md |
| Get Driver Pit Stops | `getDriverPitStops` | Get one driver's pit stops in one race (GET /ergast/f1/{season}/{round}/drivers/{driverId}/pitstops.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/pitstops.md |
| Get Driver Standing for Driver | `getDriverStandingForDriver` | Get one driver's championship standing in a season (GET /ergast/f1/{season}/drivers/{driverId}/driverstandings.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/driverStandings.md |
| Get Driver Standings | `getDriverStandings` | Get the drivers' championship standings at the end of a season (or now, for current) (GET /ergast/f1/{season}/driverstandings.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/driverStandings.md |
| Get Driver Standings After Round | `getDriverStandingsAfterRound` | Get the drivers' championship standings after a given round (GET /ergast/f1/{season}/{round}/driverstandings.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/driverStandings.md |
| Get Lap | `getLap` | Get every driver's timing for one lap of a race (GET /ergast/f1/{season}/{round}/laps/{lapNumber}.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/laps.md |
| Get Laps | `getLaps` | Get lap-by-lap timings of every driver in one race (data from 1996 onward) (GET /ergast/f1/{season}/{round}/laps.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/laps.md |
| Get Pit Stops | `getPitStops` | Get every pit stop of one race (data from 2011 onward) (GET /ergast/f1/{season}/{round}/pitstops.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/pitstops.md |
| Get Pit Stops by Stop Number | `getPitStopsByNumber` | Get the nth pit stop of every driver in one race (GET /ergast/f1/{season}/{round}/pitstops/{stopNumber}.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/pitstops.md |
| Get Qualifying Results | `getQualifyingResults` | Get the qualifying results (Q1, Q2, Q3) of one round (GET /ergast/f1/{season}/{round}/qualifying.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/qualifying.md |
| Get Race | `getRace` | Get the schedule of one race (round) in a season (GET /ergast/f1/{season}/{round}/races.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/races.md |
| Get Race Result by Position | `getRaceResultByPosition` | Get the result for one finishing position in a race (GET /ergast/f1/{season}/{round}/results/{position}.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/results.md |
| Get Race Results | `getRaceResults` | Get the results of one race (GET /ergast/f1/{season}/{round}/results.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/results.md |
| Get Sprint Results | `getSprintResults` | Get the sprint results of one round (GET /ergast/f1/{season}/{round}/sprint.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/sprint.md |
| List Circuits | `listCircuits` | List every circuit that has hosted a Formula 1 race, with location (GET /ergast/f1/circuits.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/circuits.md |
| List Constructor Season Results | `listConstructorSeasonResults` | List one constructor's race results in one season (GET /ergast/f1/{season}/constructors/{constructorId}/results.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/results.md |
| List Constructors | `listConstructors` | List every Formula 1 constructor (team) (GET /ergast/f1/constructors.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/constructors.md |
| List Driver Results | `listDriverResults` | List all race results of one driver across their career (GET /ergast/f1/drivers/{driverId}/results.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/results.md |
| List Driver Season Results | `listDriverSeasonResults` | List one driver's race results in one season (GET /ergast/f1/{season}/drivers/{driverId}/results.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/results.md |
| List Drivers | `listDrivers` | List every Formula 1 driver (GET /ergast/f1/drivers.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/drivers.md |
| List Finishing Statuses | `listStatuses` | List every finishing status (Finished, +1 Lap, Engine, Accident...) with how often it occurred (GET /ergast/f1/status.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/status.md |
| List Qualifying Results | `listQualifyingResults` | List qualifying results across all seasons (GET /ergast/f1/qualifying.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/qualifying.md |
| List Races | `listRaces` | List every Formula 1 race with circuit, date and session times (GET /ergast/f1/races.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/races.md |
| List Results | `listResults` | List race results across all seasons, page by page (GET /ergast/f1/results.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/results.md |
| List Season Circuits | `listSeasonCircuits` | List the circuits used in one season (GET /ergast/f1/{season}/circuits.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/circuits.md |
| List Season Constructors | `listSeasonConstructors` | List the constructors that raced in one season (GET /ergast/f1/{season}/constructors.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/constructors.md |
| List Season Drivers | `listSeasonDrivers` | List the drivers who raced in one season (GET /ergast/f1/{season}/drivers.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/drivers.md |
| List Season Finishing Statuses | `listSeasonStatuses` | List finishing statuses and counts for one season (GET /ergast/f1/{season}/status.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/status.md |
| List Season Qualifying Results | `listSeasonQualifyingResults` | List the qualifying results of one season (GET /ergast/f1/{season}/qualifying.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/qualifying.md |
| List Season Races | `listSeasonRaces` | List the race calendar of one season with session times (GET /ergast/f1/{season}/races.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/races.md |
| List Season Results | `listSeasonResults` | List the race results of every round in one season (GET /ergast/f1/{season}/results.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/results.md |
| List Season Sprint Results | `listSeasonSprintResults` | List the sprint race results of one season (GET /ergast/f1/{season}/sprint.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/sprint.md |
| List Seasons | `listSeasons` | List every Formula 1 season with its Wikipedia link (GET /ergast/f1/seasons.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/seasons.md |
| List Sprint Results | `listSprintResults` | List sprint race results across all seasons (GET /ergast/f1/sprint.json). Docs: https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/sprint.md |
