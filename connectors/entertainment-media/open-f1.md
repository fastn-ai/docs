---
description: "OpenF1 is an open-source Formula 1 data API with telemetry, timing and session data from 2023 onward."
hidden: true
---

# OpenF1

<img src="../../.gitbook/assets/connectors/lg/open-f1.png" alt="OpenF1 logo">

OpenF1 is an open-source Formula 1 data API with telemetry, timing and session data from 2023 onward. Get meetings, sessions, drivers, laps, car telemetry, car locations, intervals, positions, pit stops, stints, overtakes, race control messages, team radio, weather, starting grids, session results and championship standings. Historical data is free with no API key.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [openf1.org](https://openf1.org) |
| **Authentication** | No authentication |
| **Slug** | `openF1` |

## Use it

Add OpenF1 from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openF1.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| List Car Data | `listCarData` | Some data about each car, at a sample rate of about 3.7 Hz. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/car_data). Docs: https://openf1.org/docs/#car-data |
| List Car Locations | `listLocations` | The approximate location of the cars on the circuit, at a sample rate of about 3.7 Hz. Useful for gauging their progress along the track, but lacks details about lateral placement — i.e. whether the car is on the left or right side of the track. The origin point (0, 0, 0) appears to be arbitrary and not tied to any specific location on the track. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/location). Docs: https://openf1.org/docs/#location |
| List Drivers | `listDrivers` | Retrieve detailed information about the drivers participating in a specific session. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/drivers). Docs: https://openf1.org/docs/#drivers |
| List Drivers Championship Standings | `listDriversChampionship` | Provides championship standings for drivers. Only available for race sessions. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/championship_drivers). Docs: https://openf1.org/docs/#drivers-championship-beta |
| List Intervals | `listIntervals` | Fetches real-time interval data between drivers and their gap to the race leader. Available during races only, with updates approximately every 4 seconds. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/intervals). Docs: https://openf1.org/docs/#intervals |
| List Laps | `listLaps` | Provides detailed information about individual laps. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/laps). Docs: https://openf1.org/docs/#laps |
| List Meetings | `listMeetings` | Provides information about meetings. A meeting refers to a Grand Prix or testing weekend and usually includes multiple sessions (practice, qualifying, race, ...). Meetings are updated every day at midnight UTC. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/meetings). Docs: https://openf1.org/docs/#meetings |
| List Overtakes | `listOvertakes` | Provides information about overtakes. An overtake refers to one driver (the overtaking driver) exchanging positions with another driver (the overtaken driver). This includes both on-track passes and position changes resulting from pit stops or post-race penalties. This data is only available during races and may be incomplete. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/overtakes). Docs: https://openf1.org/docs/#overtakes |
| List Pit Stops | `listPitStops` | Provides information about cars going through the pit lane. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/pit). Docs: https://openf1.org/docs/#pit |
| List Positions | `listPositions` | Provides driver positions throughout a session, including initial placement and subsequent changes. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/position). Docs: https://openf1.org/docs/#position |
| List Race Control Messages | `listRaceControlMessages` | Provides information about race control (session status, racing incidents, flags, safety car, ...). Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/race_control). Docs: https://openf1.org/docs/#race-control |
| List Session Results | `listSessionResults` | Provides standings after a session. This data becomes available a few minutes after the official results are published on the official Formula 1 website. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/session_result). Docs: https://openf1.org/docs/#session-result |
| List Sessions | `listSessions` | Provides information about sessions. A session refers to a distinct period of track activity during a Grand Prix or testing weekend (practice, qualifying, sprint, race, ...). Sessions are updated every day at midnight UTC. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/sessions). Docs: https://openf1.org/docs/#sessions |
| List Starting Grid | `listStartingGrid` | Provides the starting grid for the upcoming race. This data becomes available a few minutes after the official results are published on the official Formula 1 website. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/starting_grid). Docs: https://openf1.org/docs/#starting-grid |
| List Stints | `listStints` | Provides information about individual stints. A stint refers to a period of continuous driving by a driver during a session. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/stints). Docs: https://openf1.org/docs/#stints |
| List Team Radio | `listTeamRadio` | Provides a collection of radio exchanges between Formula 1 drivers and their respective teams during sessions. Please note that only a limited selection of communications are included, not the complete record of radio interactions. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/team_radio). Docs: https://openf1.org/docs/#team-radio |
| List Teams Championship Standings | `listTeamsChampionship` | Provides championship standings for teams. Only available for race sessions. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/championship_teams). Docs: https://openf1.org/docs/#teams-championship-beta |
| List Weather | `listWeather` | The weather over the track, updated every minute. Every field can be used as an exact-match filter; historical data from 2023 is free (GET /v1/weather). Docs: https://openf1.org/docs/#weather |
